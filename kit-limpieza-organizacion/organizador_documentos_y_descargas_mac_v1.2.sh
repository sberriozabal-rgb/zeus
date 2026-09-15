/bin/bash <<'DOCS_EOF'
# ============================================================
# ORGANIZADOR DOCUMENTOS + DESCARGAS · Mac · Terminal v1.2
# Fusiona ~/Descargas dentro de ~/Documentos y organiza el conjunto.
# Taxonomía espejo de Google Drive: 01–10 + 99
# Regla de la casa: borrado directo, sin cuarentena
#   ACORDADO (Sergio, 2026-08-08)
# Todo queda en: Documentos/00 · SISTEMA/LOG.md
# ============================================================
set -u

# --- Interruptor de simulacro -------------------------------
# SIMULACRO=1  → no toca nada, solo escribe en el LOG lo que haría.
# SIMULACRO=0  → ejecuta (comportamiento por defecto de la casa).
SIMULACRO=0

# --- Localizar las bases ------------------------------------
if   [ -d "$HOME/Documentos" ]; then BASE="$HOME/Documentos"
elif [ -d "$HOME/Documents" ];  then BASE="$HOME/Documents"
else echo "🔴 Bloqueado: no existe ~/Documentos ni ~/Documents"; exit 1
fi

DESC=""
if   [ -d "$HOME/Descargas" ]; then DESC="$HOME/Descargas"
elif [ -d "$HOME/Downloads" ]; then DESC="$HOME/Downloads"
fi

# --- Snapshot APFS (red de seguridad local, sin preguntar) ---
if [ "$SIMULACRO" -eq 0 ] && tmutil localsnapshot >/dev/null 2>&1; then
  SNAP="sí"
else
  SNAP="no disponible"
fi

# --- Estructura ---------------------------------------------
S="00 · SISTEMA"
D01="01 · OCTAVA · Negocio y campaña"
D02="02 · OCTAVA · Marca y piezas"
D03="03 · OCTAVA · IA, prompts y skills"
D04="04 · Método operativo de restauración"
D05="05 · Archivo de calidad · Hotel Diagonal Barcelona"
D06="06 · Clientes y proyectos anteriores"
D07="07 · Personal · Administración y finanzas"
D08="08 · Personal · Identidad, carrera y salud"
D09="09 · Fotos y medios"
D10="10 · Respaldos y volcados"
D99="99 · Sin clasificar"
CARPDESC="$D99/Carpetas de Descargas"

mkstruct() {
  for d in "$S" "$D01" "$D02" "$D03" "$D04" "$D05" "$D06" \
           "$D07" "$D08" "$D09" "$D10" "$D99"; do
    mkdir -p "$BASE/$d"
  done
}
mkstruct

LOG="$BASE/$S/LOG.md"
touch "$LOG"
TS() { date '+%Y-%m-%d %H:%M:%S'; }
log() { printf -- "- [%s] %s\n" "$(TS)" "$1" >> "$LOG"; }
if [ "$SIMULACRO" -eq 1 ]; then MODO="SIMULACRO (no se toca nada)"; else MODO="EJECUCIÓN · borrado directo"; fi
log "=== $MODO · Organizador Documentos+Descargas v1.2 · base: $BASE · descargas: ${DESC:-(ninguna)} · snapshot APFS: $SNAP ==="

BORRADOS=0; BYTES=0; MOVIDOS=0; ARCHIVADOS=0; RENOMBRADOS=0; PEND=0
FUSFILES=0; FUSDIRS=0; INCOMPL=0; PROTEGIDOS=0
US=$(printf '\037')
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Solo dígitos. Si `stat` devuelve cualquier otra cosa (otra plataforma, un
# fichero que desaparece a media pasada), la aritmética recibiría texto y con
# `set -u` el script abortaría a mitad. Un contador de bytes no puede tumbar
# una organización ya empezada.
solo_digitos() { case "$1" in ''|*[!0-9]*) printf '0';; *) printf '%s' "$1";; esac; }
fsize()  { solo_digitos "$(stat -f '%z' "$1" 2>/dev/null)"; }
fmtime() { solo_digitos "$(stat -f '%m' "$1" 2>/dev/null)"; }
fhash()  { shasum -a 256 "$1" | awk '{print $1}'; }

do_rm() { if [ "$SIMULACRO" -eq 0 ]; then rm -f "$1"; fi; }
do_mv() { if [ "$SIMULACRO" -eq 0 ]; then mv "$1" "$2"; fi; }

# Destino libre: si el nombre está ocupado, añade sufijo numerado.
libre() {
  d="$1"; n="$2"
  if [ ! -e "$d/$n" ]; then printf '%s' "$d/$n"; return; fi
  case "$n" in
    *.*) st="${n%.*}"; ex=".${n##*.}";;
    *)   st="$n"; ex="";;
  esac
  i=1
  while [ -e "$d/$st · $i$ex" ]; do i=$((i+1)); done
  printf '%s' "$d/$st · $i$ex"
}

# --- Protecciones -------------------------------------------
# No se tocan: ocultos, node_modules, Library, descargas a medias,
# ni paquetes de macOS (.app .pages .key .numbers .rtfd …), porque
# romperlos rompe proyectos, instaladores y documentos-paquete.
# Tampoco se toca lo ya archivado ni las carpetas traídas de Descargas.
# ¿Es una app o una biblioteca? Eso no es un documento del usuario.
es_paquete_sistema() {
  case "$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')" in
    *.app|*.framework|*.bundle|*.sparsebundle|*.photoslibrary|*.fcpbundle|*.logicx|*.band) return 0;;
    *) return 1;;
  esac
}

# ¿Es un paquete que el usuario entiende como un documento suyo?
es_paquete_documento() {
  case "$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')" in
    *.pages|*.key|*.numbers|*.rtfd) return 0;;
    *) return 1;;
  esac
}

# ¿Es un directorio en el que no se entra ni se mueve?
es_dir_protegido() {
  case "$1" in
    node_modules|Library|.git|.*) return 0;;
    *) es_paquete_sistema "$1";;
  esac
}

scan() {
  find "$BASE" \
    \( -name '.*' -o -name 'node_modules' -o -name 'Library' \
       -o -name '*.app' -o -name '*.pages' -o -name '*.key' \
       -o -name '*.numbers' -o -name '*.rtfd' -o -name '*.photoslibrary' \
       -o -name '*.fcpbundle' -o -name '*.logicx' -o -name '*.band' \
       -o -name '*.sparsebundle' -o -name '*.download' -o -name '*.crdownload' \
       -o -name '*.part' \
       -o -path "$BASE/$S" -o -path "$BASE/$CARPDESC" \) -prune -o \
    -type f ! -name '.*' -print0
}

# Limpieza de basura de sistema
if [ "$SIMULACRO" -eq 0 ]; then
  find "$BASE" -name '.DS_Store' -type f -delete 2>/dev/null
  [ -n "$DESC" ] && find "$DESC" -name '.DS_Store' -type f -delete 2>/dev/null
fi

# ---------- FASE 0 · Fusión de Descargas → Documentos ----------
# Los ficheros sueltos entran en '99 · Sin clasificar' y siguen el
# circuito normal (dedup + clasificación).
# Las CARPETAS entran intactas en '99/Carpetas de Descargas' y NO se
# aplanan: un proyecto descomprimido pierde el sentido si lo desmontas.
# ~/Descargas se conserva (el Dock la necesita), solo queda vacía.
if [ -n "$DESC" ]; then
  [ "$SIMULACRO" -eq 0 ] && mkdir -p "$BASE/$CARPDESC"
  log "--- FASE 0 · fusionando $DESC → $BASE ---"

  # Ficheros sueltos del primer nivel
  find "$DESC" -maxdepth 1 -type f ! -name '.*' -print0 > "$TMP/desc_f" 2>/dev/null
  while IFS= read -r -d '' f; do
    name=$(basename "$f")
    case "$name" in
      *.download|*.crdownload|*.part|*.aria2)
        INCOMPL=$((INCOMPL+1))
        log "OMITIDO · $f · descarga incompleta, se queda en Descargas"
        continue;;
    esac
    tgt=$(libre "$BASE/$D99" "$name")
    do_mv "$f" "$tgt"
    FUSFILES=$((FUSFILES+1))
    log "FUSIONADO · $f → $tgt"
  done < "$TMP/desc_f"

  # Carpetas y paquetes del primer nivel.
  # Un .pages es un directorio, pero es un documento: va a la bandeja de
  # entrada como una unidad. Un node_modules o un .app, no: se quedan.
  find "$DESC" -maxdepth 1 -mindepth 1 -type d ! -name '.*' -print0 > "$TMP/desc_d" 2>/dev/null
  while IFS= read -r -d '' d; do
    name=$(basename "$d")

    if es_dir_protegido "$name"; then
      PROTEGIDOS=$((PROTEGIDOS+1))
      log "OMITIDO · $d · directorio protegido o paquete de aplicación: se queda en Descargas"
      continue
    fi

    if es_paquete_documento "$name"; then
      tgt=$(libre "$BASE/$D99" "$name")
      do_mv "$d" "$tgt"
      FUSFILES=$((FUSFILES+1))
      log "FUSIONADO (paquete-documento, entero) · $d → $tgt"
      continue
    fi

    tgt=$(libre "$BASE/$CARPDESC" "$name")
    do_mv "$d" "$tgt"
    FUSDIRS=$((FUSDIRS+1))
    log "FUSIONADO (carpeta intacta) · $d → $tgt"
  done < "$TMP/desc_d"
fi

# ---------- FASE 1 · Duplicados exactos → BORRADO ----------
# Solo byte a byte idénticos y con contenido (>0 bytes).
scan > "$TMP/all0"
while IFS= read -r -d '' f; do
  [ -s "$f" ] || continue
  h=$(fhash "$f"); m=$(fmtime "$f")
  case "$f" in *[Cc]opia*|*[Cc]opy*|*\(*\)*) mk=1;; *) mk=0;; esac
  printf '%s%s%s%s%s%s%s\n' "$h" "$US" "$mk" "$US" "$m" "$US" "$f"
done < "$TMP/all0" > "$TMP/hashes"

sort -t "$US" -k1,1 -k2,2n -k3,3nr "$TMP/hashes" > "$TMP/sorted"

prev=""; keep=""
while IFS="$US" read -r h mk m f; do
  [ -z "$h" ] && continue
  if [ "$h" = "$prev" ]; then
    sz=$(fsize "$f")
    do_rm "$f"
    BORRADOS=$((BORRADOS+1)); BYTES=$((BYTES+sz))
    log "BORRADO · $f · duplicado exacto de: $keep"
  else
    prev="$h"; keep="$f"
  fi
done < "$TMP/sorted"

# ---------- FASE 2 · Marcadores de copia/versión ----------
cleanname() {
  printf '%s' "$1" | sed -E \
    -e 's/ *\(([0-9]+)\)//g' \
    -e 's/ *- *[Cc]opia//g' -e 's/[Cc]opia de //g' -e 's/ [Cc]opia//g' \
    -e 's/ *- *[Cc]opy//g'  -e 's/[Cc]opy of //g'  -e 's/ [Cc]opy//g' \
    -e 's/ +/ /g' -e 's/ +\././g' -e 's/^ +//' -e 's/ +$//'
}

scan | tr '\0' '\n' | grep -Ei '(copia|copy|\([0-9]+\))' > "$TMP/marked" || true
while IFS= read -r f; do
  [ -f "$f" ] || continue
  case "$f" in "$BASE/$D10/"*) continue;; esac
  dir=$(dirname "$f"); name=$(basename "$f")
  clean=$(cleanname "$name")
  [ "$clean" = "$name" ] && continue
  [ -z "$clean" ] && continue
  if find "$BASE" -type f -name "$clean" ! -path "$f" 2>/dev/null | grep -q .; then
    stem="${clean%.*}"
    dest="$BASE/$D10/$stem"
    [ "$SIMULACRO" -eq 0 ] && mkdir -p "$dest"
    tgt=$(libre "$dest" "$name")
    do_mv "$f" "$tgt"
    ARCHIVADOS=$((ARCHIVADOS+1))
    log "ARCHIVADO · $f → $tgt · versión marcada con hermano vigente"
  else
    if [ -e "$dir/$clean" ]; then
      log "[A VALIDAR] · $f · nombre limpio ocupado, se conserva sin cambio"
      PEND=$((PEND+1))
    else
      do_mv "$f" "$dir/$clean"
      RENOMBRADOS=$((RENOMBRADOS+1))
      log "RENOMBRADO · $name → $clean · marcador de copia sin hermano"
    fi
  fi
done < "$TMP/marked"

# ---------- FASE 3 · Clasificación ----------
deaccent_lower() {
  printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | sed \
    -e 's/Á/á/g; s/É/é/g; s/Í/í/g; s/Ó/ó/g; s/Ú/ú/g; s/Ñ/ñ/g' \
    -e 's/á/a/g; s/é/e/g; s/í/i/g; s/ó/o/g; s/ú/u/g; s/ü/u/g; s/ñ/n/g'
}

dest_for() {
  ln=$(deaccent_lower "$1")
  case "$ln" in
    # --- Medios, archivos e instaladores: mandan por extensión ---
    *.zip|*.dmg|*.iso|*.tar|*.gz|*.tgz|*.rar|*.7z|*.sparseimage|*.pkg) printf '%s' "$D10";;
    *respaldo*|*backup*|*volcado*|*export*|*copia\ de\ seguridad*)      printf '%s' "$D10";;
    *.png|*.jpg|*.jpeg|*.heic|*.gif|*.tiff|*.webp|*.raw|*.cr2|*.svg) printf '%s' "$D09";;
    *.mov|*.mp4|*.avi|*.m4v|*.mkv|*.mp3|*.wav|*.aiff|*.m4a)          printf '%s' "$D09";;

    # --- Identidad y salud (antes que finanzas: 'certificado medico') ---
    *dni*|*pasaporte*|*\ nie*|*libro\ de\ familia*|*empadronamiento*) printf '%s' "$D08";;
    *curriculum*|*curriculo*|*\ cv*|*cv\ *|*vida\ laboral*|*titulo*|*diploma*) printf '%s' "$D08";;
    *medic*|*analitica*|*mutua*|*seguridad\ social*|*vacuna*|*informe\ clinico*) printf '%s' "$D08";;

    # --- OCTAVA ---
    *prompt*|*skill*|*agente*|*claude*|*apps\ script*|*.gs|*google\ script*) printf '%s' "$D03";;
    *manual\ de\ marca*|*isotipo*|*lockup*|*logotipo*|*logo*|*favicon*|*tipograf*) printf '%s' "$D02";;
    *octava*|*diagnostico\ expres*|*baremo*|*sello\ octava*|*indice\ octava*|*metodo\ 8*) printf '%s' "$D01";;

    # --- Método operativo de restauración ---
    *escandallo*|*ingenieria\ de\ menu*|*food\ cost*|*prime\ cost*) printf '%s' "$D04";;
    *appcc*|*alergen*|*trazabilidad*|*plan\ de\ higiene*) printf '%s' "$D04";;
    *inventario*|*merma*|*cierre\ de\ caja*|*arqueo*|*checklist*|*cuadrante*|*turno*) printf '%s' "$D04";;
    *carta\ de*|*receta*|*proveedor*|*albaran*|*no-show*|*reserva*) printf '%s' "$D04";;

    # --- Hotel Diagonal ---
    *diagonal*|*\ hdb*|*hdb\ *|*silken*) printf '%s' "$D05";;

    # --- Clientes ---
    *barry*|*belcebu*|*fimaraba*|*restaurante\ ikea*|*kamezi*|*allenrok*) printf '%s' "$D06";;

    # --- Personal · administración y finanzas ---
    *factura*|*recibo*|*nomina*|*banco*|*kutxabank*|*extracto*) printf '%s' "$D07";;
    *hipoteca*|*seguro*|*poliza*|*impuesto*|*renta*|*irpf*|*iva*|*modelo\ 3*) printf '%s' "$D07";;
    *herencia*|*notari*|*escritura*|*contrato*|*catastro*|*ibi*) printf '%s' "$D07";;

    # --- Resto ---
    *) printf '%s' "$D99";;
  esac
}

scan > "$TMP/cls0"
while IFS= read -r -d '' f; do
  [ -f "$f" ] || continue
  # Lo ya archivado como versión no se vuelve a sacar del archivo.
  case "$f" in "$BASE/$D10/"*) continue;; esac
  name=$(basename "$f")
  dest=$(dest_for "$name")
  case "$f" in "$BASE/$dest/"*) continue;; esac
  tgt="$BASE/$dest/$name"
  if [ -e "$tgt" ]; then
    if [ "$(fhash "$f")" = "$(fhash "$tgt")" ]; then
      sz=$(fsize "$f"); do_rm "$f"
      BORRADOS=$((BORRADOS+1)); BYTES=$((BYTES+sz))
      log "BORRADO · $f · idéntico al ya clasificado: $tgt"
      continue
    fi
    stem="${name%.*}"; ext="${name##*.}"; n=1
    while [ -e "$BASE/$dest/$stem · A-VALIDAR-$n.$ext" ]; do n=$((n+1)); done
    tgt="$BASE/$dest/$stem · A-VALIDAR-$n.$ext"
    PEND=$((PEND+1))
    log "[A VALIDAR] · $f → $tgt · mismo nombre, contenido distinto"
  fi
  do_mv "$f" "$tgt"
  MOVIDOS=$((MOVIDOS+1))
  log "MOVIDO · $f → $tgt"
done < "$TMP/cls0"

# ---------- FASE 4 · Carpetas vacías en cascada ----------
# Nunca se borra ~/Descargas ni las carpetas raíz de la taxonomía.
if [ "$SIMULACRO" -eq 0 ]; then
  for i in 1 2 3 4 5 6 7 8; do
    find "$BASE" -mindepth 1 -type d -empty \
      ! -name '.*' ! -path "$BASE/$S*" ! -path "$BASE/$CARPDESC/*" -delete 2>/dev/null
  done
  if [ -n "$DESC" ]; then
    find "$DESC" -mindepth 1 -type d -empty ! -name '.*' -delete 2>/dev/null
  fi
fi
mkstruct

# ---------- INFORME FINAL ----------
MB=$(awk -v b="$BYTES" 'BEGIN{printf "%.1f", b/1048576}')
{
  echo ""
  echo "════════ INFORME FINAL · ORGANIZADOR DOCUMENTOS+DESCARGAS v1.2 ════════"
  echo " Base:      $BASE"
  echo " Descargas: ${DESC:-(no encontrada, fase 0 omitida)}"
  echo " Modo:      $MODO"
  echo "──────────────────────────────────────────────────────────────────────"
  if [ -n "$DESC" ]; then
    echo " Fusionado desde Descargas: $FUSFILES ficheros · $FUSDIRS carpetas intactas"
    echo " Descargas incompletas respetadas: $INCOMPL"
    echo " Protegidos no tocados (node_modules, apps…): $PROTEGIDOS"
    echo "──────────────────────────────────────────────────────────────────────"
  fi
  for d in "$D01" "$D02" "$D03" "$D04" "$D05" "$D06" \
           "$D07" "$D08" "$D09" "$D10" "$D99"; do
    c=$(find "$BASE/$d" -type f ! -name '.*' 2>/dev/null | wc -l | tr -d ' ')
    printf ' %-52s %s archivos\n' "$d" "$c"
  done
  echo "──────────────────────────────────────────────────────────────────────"
  echo " Duplicados borrados: $BORRADOS · Liberados: ${MB} MB"
  echo " Movidos: $MOVIDOS · Archivados: $ARCHIVADOS · Renombrados: $RENOMBRADOS"
  echo " Pendientes [A VALIDAR]: $PEND · Snapshot APFS: $SNAP"
  if [ "$PEND" -eq 0 ]; then
    echo " 🟢 Consolidado; $BORRADOS duplicados borrados, todos en el LOG."
  else
    echo " 🟡 Consolidado con $PEND pendientes [A VALIDAR] — revisa el LOG."
  fi
  echo " Revisa '$D99': es la cola que el nombre no delata."
  echo " Las carpetas traídas de Descargas están intactas en '$CARPDESC'."
  echo " LOG: $LOG"
  echo "══════════════════════════════════════════════════════════════════════"
} | tee -a "$LOG"
DOCS_EOF
