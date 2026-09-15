#!/usr/bin/env bash
#
# Prueba funcional del organizador sobre un árbol desechable.
#
# Se ejecuta el script REAL, sin adaptar, con HOME apuntando al arenero: así
# `~/Documentos` y `~/Descargas` son los del arenero y no se toca nada del
# usuario. En CI corre sobre macOS, que es la plataforma de destino.
#
set -uo pipefail
cd "$(dirname "$0")"
GUION="$PWD/organizador_documentos_y_descargas_mac_v1.2.sh"
[ -f "$GUION" ] || { echo "❌ no encuentro $GUION"; exit 1; }

ARENERO=$(mktemp -d)
trap 'rm -rf "$ARENERO"' EXIT
DOCS="$ARENERO/Documentos"
DESC="$ARENERO/Descargas"
mkdir -p "$DOCS/vieja/anidada" "$DESC/proyecto-web/src" \
         "$DESC/node_modules/left-pad" "$DESC/Instalador.app/Contents" \
         "$DESC/Propuesta.pages"

fallos=0
comprobar() { # comprobar <descripción> <condición-ya-evaluada:0|1>
  if [ "$2" -eq 0 ]; then echo "  ✅ $1"; else echo "  ❌ $1"; fallos=$((fallos + 1)); fi
}
hay() { [ -e "$DOCS/$1" ]; }          # existe en Documentos
cuantos() { find "$1" -type f 2>/dev/null | wc -l | tr -d ' '; }

# ---------------------------------------------------------------- el árbol
printf 'RECIBO IBERDROLA 181,20 EUR\n' > "$DOCS/factura luz enero.pdf"
printf 'NOMINA MARZO\n'                > "$DOCS/vieja/anidada/nomina marzo.pdf"
printf 'RECIBO IBERDROLA 181,20 EUR\n' > "$DESC/factura luz enero.pdf"   # duplicado exacto
printf 'CONTENIDO DISTINTO\n'          > "$DESC/DNI Sergio.pdf"          # colisión de nombre
printf 'DNI ORIGINAL\n'                > "$DOCS/DNI Sergio.pdf"
printf 'binario\n'                     > "$DESC/Xcode_15.dmg"
printf 'imagen\n'                      > "$DESC/captura pantalla.png"
printf 'escandallo\n'                  > "$DESC/escandallo otono.xlsx"
printf 'vete a saber\n'                > "$DESC/asdf.bin"
printf 'a medias\n'                    > "$DESC/pelicula.mp4.download"
printf '# proyecto\n'                  > "$DESC/proyecto-web/README.md"
printf 'console.log(1)\n'              > "$DESC/proyecto-web/src/app.js"
printf 'module.exports=0\n'            > "$DESC/node_modules/left-pad/index.js"
printf '<plist/>\n'                    > "$DESC/Instalador.app/Contents/Info.plist"
printf '<doc/>\n'                      > "$DESC/Propuesta.pages/index.xml"

antes=$(( $(cuantos "$DOCS") + $(cuantos "$DESC") ))
echo "── Primera pasada (entrada: $antes ficheros)"
HOME="$ARENERO" bash "$GUION" > "$ARENERO/salida1.txt" 2>&1 || true
grep -q "INFORME FINAL" "$ARENERO/salida1.txt"; comprobar "el script termina y emite su informe" $?

# ------------------------------------------------------------- la fusión
[ -f "$DESC/pelicula.mp4.download" ]; comprobar "la descarga a medias se queda en Descargas" $?
[ -f "$DESC/node_modules/left-pad/index.js" ]; comprobar "node_modules no se toca" $?
[ -d "$DESC" ]; comprobar "~/Descargas sigue existiendo (el Dock la necesita)" $?
[ -f "$DESC/Instalador.app/Contents/Info.plist" ]
comprobar "una app descargada no se arrastra a Documentos" $?
hay "99 · Sin clasificar/Propuesta.pages/index.xml"
comprobar "un paquete-documento sí se mueve, entero y sin abrirlo" $?
hay "99 · Sin clasificar/Carpetas de Descargas/proyecto-web/src/app.js"
comprobar "el proyecto descargado conserva su estructura" $?

# -------------------------------------------------- clasificación por tipo
hay "09 · Fotos y medios/captura pantalla.png"; comprobar "la imagen va a Fotos y medios" $?
hay "10 · Respaldos y volcados/Xcode_15.dmg";   comprobar "el .dmg va a Respaldos y volcados" $?
hay "04 · Método operativo de restauración/escandallo otono.xlsx"
comprobar "el escandallo va a Método operativo" $?
hay "07 · Personal · Administración y finanzas/nomina marzo.pdf"
comprobar "la nómina va a Administración y finanzas" $?
hay "99 · Sin clasificar/asdf.bin"; comprobar "lo que no delata el nombre queda en Sin clasificar" $?

# ------------------------------------------------------------- duplicados
n=$(find "$DOCS" -name "factura luz enero*.pdf" -type f | wc -l | tr -d ' ')
[ "$n" -eq 1 ]; comprobar "el duplicado exacto se borró y queda un solo ejemplar" $?

# ------------------------------------ colisión con contenido distinto
n=$(find "$DOCS" -name "DNI Sergio*" -type f | wc -l | tr -d ' ')
[ "$n" -eq 2 ]; comprobar "la colisión con contenido distinto conserva los dos ficheros" $?
find "$DOCS" -name "*A-VALIDAR*" -type f | grep -q .
comprobar "y el segundo queda marcado A-VALIDAR" $?

# ----------------------------------------------------------------- el LOG
[ -f "$DOCS/00 · SISTEMA/LOG.md" ]; comprobar "el LOG existe" $?
grep -q "BORRADO" "$DOCS/00 · SISTEMA/LOG.md"; comprobar "el LOG registra el borrado" $?

# ------------------------------------------------------------ idempotencia
echo "── Segunda pasada (no debe tocar nada)"
HOME="$ARENERO" bash "$GUION" > "$ARENERO/salida2.txt" 2>&1 || true
grep -qE "Duplicados borrados: 0" "$ARENERO/salida2.txt"; comprobar "no borra nada la segunda vez" $?
grep -qE "Movidos: 0 " "$ARENERO/salida2.txt";            comprobar "no mueve nada la segunda vez" $?

echo
if [ "$fallos" -eq 0 ]; then
  echo "🟢 TODAS LAS COMPROBACIONES PASAN"
else
  echo "🔴 $fallos COMPROBACIONES FALLAN"
  echo "── informe de la primera pasada ──"
  cat "$ARENERO/salida1.txt"
  echo "── árbol resultante ──"
  find "$DOCS" "$DESC" -type f | sed "s|$ARENERO/||" | sort
fi
exit $(( fallos > 0 ? 1 : 0 ))
