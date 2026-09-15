#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
respaldo.py - Digiere, sella, verifica y reconstruye respaldos de Proyectos de Claude.
Parte de la skill `respaldo-proyecto-ia-cl` v2.0.0.

Modos:
  --preparar   CARPETA           Crea el arbol canonico vacio de las 5 capas (P2)
  --ingerir    EXPORT            Digiere el export oficial: filtra chats del proyecto,
                                 transcribe y redacta el borrador de resumen (P3)
  --recolectar CARPETA [...]     Barre carpetas de descargas, deduplica y clasifica (P4)
  --escanear   CARPETA           Busca credenciales y datos personales (P6)
  --restaurar-todo CARPETA       Genera RESTAURAR-TODO.md, el archivo maestro (P8)
  --empaquetar CARPETA           Checksums SHA-256 + ZIP anidado cifrado AES-256 (P9)
  --verificar  PAQUETE.zip       Comprueba integridad y checksums (P10)
  --auto       CARPETA           Encadena ingerir + recolectar + escanear +
                                 restaurar-todo + empaquetar + verificar
  --ejemplo                      Demostracion completa de extremo a extremo

La contrasena NUNCA se pasa como argumento. Se lee de la variable de entorno
RESPALDO_PASSWORD o se pide por consola. Un argumento queda en el historial del
shell y en la lista de procesos del sistema.

Dependencia opcional: pyzipper (AES-256).  pip install pyzipper
Sin pyzipper el paquete se genera SIN CIFRAR y se marca como tal en el nombre.
"""

import argparse
import getpass
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

VERSION = "2.0.0"

try:
    import pyzipper
    HAY_AES = True
except ImportError:
    pyzipper = None
    HAY_AES = False

# --- Estructura canonica --------------------------------------------------------

CAPAS = [
    ("01-instrucciones", "L1 Instrucciones"),
    ("02-conocimiento", "L2 Conocimiento"),
    ("03-adjuntos", "L3 Adjuntos"),
    ("04-skills", "L4 Skills"),
    ("05-chats", "L5 Chats"),
]

# --- P6 · Patrones de deteccion -------------------------------------------------
# Cada patron: (clase, etiqueta, regex). Se evalua de C3 hacia C2.
#
# v2.0.0 · El patron "contrasena en asignacion" excluye los marcadores de
# redaccion. En v1.0.0 el valor `password=[REDACTADO:credencial]` volvia a
# dispararlo, de modo que redactar no cerraba el hallazgo y el sellado entraba
# en bucle. Ver CHANGELOG, gotcha G-1.
MARCADOR_REDACCION = r"(?!\[REDACTADO:|\[NO EXPORTABLE:|<|\{\{|\*{3}|x{4,}\b|X{4,}\b)"

PATRONES = [
    ("C3", "clave OpenAI/Anthropic",  r"\b(?:sk|sk-ant)-[A-Za-z0-9_\-]{16,}"),
    ("C3", "token GitHub",            r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    ("C3", "clave AWS",               r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    ("C3", "clave Google",            r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    ("C3", "token Slack",             r"\bxox[abprs]-[A-Za-z0-9\-]{10,}"),
    ("C3", "token Stripe",            r"\b[rs]k_(?:live|test)_[A-Za-z0-9]{20,}"),
    ("C3", "cabecera Bearer",         r"\bBearer\s+" + MARCADOR_REDACCION + r"[A-Za-z0-9_\-\.=]{20,}"),
    ("C3", "clave privada PEM",       r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    ("C3", "cadena de conexion",      r"\b(?:postgres|postgresql|mysql|mongodb(?:\+srv)?)://[^\s:@/]+:[^\s@/]+@"),
    ("C3", "contrasena en asignacion",
     r"(?i)\b(?:password|passwd|contrase(?:n|ñ)a|secret|api[_\-]?key)\s*[:=]\s*[\"']?"
     + MARCADOR_REDACCION + r"[^\s\"']{8,}"),
    ("C2", "correo electronico",      r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b"),
    ("C2", "IBAN",                    r"\b[A-Z]{2}\d{2}[A-Z0-9]{10,30}\b"),
    ("C2", "tarjeta de pago",         r"\b(?:\d[ \-]?){13,19}\b"),
    ("C2", "telefono internacional",  r"(?<![\w.])\+\d{1,3}[ \-]?\d[\d \-]{7,14}(?![\w.])"),
]

EXT_TEXTO = {".md", ".txt", ".json", ".jsonl", ".yaml", ".yml", ".csv", ".py", ".js",
             ".ts", ".html", ".xml", ".ini", ".cfg", ".toml", ".sh", ".sql", ".env", ""}

# El escaner no lee su propio material de trabajo: chats.jsonl es una copia de las
# transcripciones y duplicaria cada hallazgo.
EXCLUIR_DEL_ESCANEO = {"CHECKSUMS.txt", "chats.jsonl"}

PALABRAS_CLAVE_INSTRUCCIONES = ("01-instrucciones",)

EXT_ADJUNTO = {
    "documento": {".pdf", ".docx", ".doc", ".odt", ".rtf", ".pages"},
    "hoja": {".xlsx", ".xls", ".csv", ".ods", ".numbers"},
    "presentacion": {".pptx", ".ppt", ".odp", ".key"},
    "imagen": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".heic", ".svg"},
    "texto": {".md", ".txt", ".json", ".yaml", ".yml", ".xml"},
    "paquete": {".skill", ".zip", ".tar", ".gz"},
}

# --- P3 · Senales de decision en un chat ----------------------------------------
# Regex de oficio: lo que en una conversacion de trabajo marca que algo quedo
# decidido, cuanto costo, o que sigue abierto. Salen de leer conversaciones
# reales de proyecto, no de un diccionario.
SENAL_DECISION = re.compile(
    r"(?i)\b(?:decidid[oa]s?|decidimos|hemos decidido|queda (?:as[ií]|claro|fijado|cerrado)|"
    r"acordad[oa]s?|acordamos|se aprueba|aprobado|vamos a|no vamos a|descartad[oa]s?|"
    r"descartamos|elegimos|nos quedamos con|el precio (?:es|ser[aá]|queda)|firmad[oa]|"
    r"confirmo|confirmad[oa]|conclusi[oó]n|resuelto|se descarta|a partir de ahora|"
    r"la regla es|regla:|por defecto ser[aá]|opci[oó]n elegida)\b")

SENAL_CIFRA = re.compile(
    r"\d[\d.,]*\s?(?:%|€|\$|USD|EUR|MXN|GBP|puntos|/20|/10|h\b|horas|d[ií]as|"
    r"semanas|meses|años|KB|MB|GB|caracteres|palabras)")

SENAL_PENDIENTE = re.compile(
    r"(?i)(?:\[A VALIDAR\]|\bpendiente\b|\bqueda pendiente\b|\bfalta (?:por|que|el|la)\b|"
    r"\bhay que\b|\bhabr[ií]a que\b|\bsiguiente paso\b|\bpr[oó]ximo paso\b|\brevisar\b|"
    r"\bTODO\b|\bpor definir\b|\bpor decidir\b)")

VACIAS = set("""
a al algo ante antes aqui asi aun aunque bajo bien cada casi como con contra cual cuando
de del desde donde dos el ella ellas ello ellos en entre era eran eres es esa ese eso esta
estaba estamos estan estar este esto estos fue fui ha haber habia hace hacer hacia han has
hasta hay incluso ir la las le les lo los mas me mi mis mucho muy nada ni no nos nosotros
nuestra nuestro o os otra otro para pero poco por porque pues que quien se ser si sido sin
sobre solo son su sus tambien tan tanto te tener tiene tienen todo todos tu tus un una uno
unos usted ustedes va vamos ver y ya yo the and for you your with that this from have has
are was were will would can could not but all any out its it's dont don't just about into
puede pueden podria deberia entonces cuanto cual cuales mismo misma cosa cosas hacerlo
""".split())


# --- utilidades -----------------------------------------------------------------

def ahora():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def hoy():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def sha256_archivo(ruta, bloque=1 << 20):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for trozo in iter(lambda: f.read(bloque), b""):
            h.update(trozo)
    return h.hexdigest()


def slug(texto, largo=48):
    t = unicodedata.normalize("NFKD", texto or "")
    t = t.encode("ascii", "ignore").decode("ascii").lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return (t[:largo].rstrip("-") or "sin-titulo")


def pedir_password(confirmar=False):
    pwd = os.environ.get("RESPALDO_PASSWORD")
    if pwd:
        return pwd
    if not sys.stdin.isatty():
        raise SystemExit(
            "ERROR: no hay terminal interactiva y RESPALDO_PASSWORD no esta definida.\n"
            "       Define la variable de entorno antes de ejecutar. No uses argumentos."
        )
    pwd = getpass.getpass("Contrasena del paquete: ")
    if confirmar and pwd != getpass.getpass("Repite la contrasena: "):
        raise SystemExit("ERROR: las contrasenas no coinciden. Nada se ha escrito.")
    if len(pwd) < 20:
        print("AVISO: contrasena de menos de 20 caracteres. "
              "Ver references/fuentes.md, nota [CRITERIO DEL AUTOR].", file=sys.stderr)
    return pwd


def archivos_de(carpeta):
    base = Path(carpeta)
    return sorted(p for p in base.rglob("*") if p.is_file())


def humano(n):
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024 or u == "GB":
            return f"{n:.0f} {u}" if u == "B" else f"{n:.1f} {u}"
        n /= 1024.0


# --- P2 · preparar el arbol -----------------------------------------------------

def preparar(carpeta, proyecto=None):
    base = Path(carpeta).resolve()
    nombre = proyecto or base.name
    for sub, _ in CAPAS:
        (base / sub).mkdir(parents=True, exist_ok=True)
    (base / "05-chats" / "transcripciones").mkdir(parents=True, exist_ok=True)
    marca = base / ".respaldo.json"
    if not marca.exists():
        marca.write_text(json.dumps({
            "proyecto": nombre,
            "version_skill": VERSION,
            "creado_en": ahora(),
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Arbol canonico listo en {base}")
    for sub, etiqueta in CAPAS:
        n = len(list((base / sub).rglob("*")))
        print(f"  {sub:<20} {etiqueta:<20} {n} elementos")
    print("\nSiguiente: --ingerir para los chats, --recolectar para los adjuntos.\n")
    return {"carpeta": str(base), "proyecto": nombre}


# --- P3 · ingerir el export oficial ---------------------------------------------

def _texto_de(bloque):
    """El export ha cambiado de forma entre versiones. Se aceptan las tres que se
    han visto: `text` plano, lista `content` de bloques, y `parts`."""
    if isinstance(bloque, str):
        return bloque
    if isinstance(bloque, list):
        return "\n".join(_texto_de(b) for b in bloque if b is not None)
    if isinstance(bloque, dict):
        for clave in ("text", "input_text", "value", "body"):
            if isinstance(bloque.get(clave), str):
                return bloque[clave]
        for clave in ("content", "parts", "blocks"):
            if bloque.get(clave):
                return _texto_de(bloque[clave])
    return ""


def _mensajes_de(chat):
    for clave in ("chat_messages", "messages", "conversation", "turns"):
        if isinstance(chat.get(clave), list):
            return chat[clave]
    return []


def _rol_de(msg):
    for clave in ("sender", "role", "author", "from"):
        v = msg.get(clave)
        if isinstance(v, str):
            return v.lower()
        if isinstance(v, dict) and isinstance(v.get("role"), str):
            return v["role"].lower()
    return "?"


def _proyecto_de(chat):
    """Devuelve (nombre, uuid) del proyecto del chat, si el export lo trae."""
    for clave in ("project", "project_uuid", "project_id", "conversation_project"):
        v = chat.get(clave)
        if isinstance(v, str):
            return (None, v) if len(v) > 24 and "-" in v else (v, None)
        if isinstance(v, dict):
            return v.get("name") or v.get("title"), v.get("uuid") or v.get("id")
    return None, None


def _cargar_json(datos):
    """Extrae la lista de conversaciones de cualquier envoltorio razonable."""
    if isinstance(datos, list):
        return datos
    if isinstance(datos, dict):
        for clave in ("conversations", "chats", "data", "items"):
            if isinstance(datos.get(clave), list):
                return datos[clave]
    return []


def _es_conversacion(o):
    return isinstance(o, dict) and bool(_mensajes_de(o))


def cargar_export(ruta):
    """Acepta el ZIP del export, la carpeta descomprimida o un .json suelto.
    NO depende del nombre del archivo: identifica el volcado por su estructura,
    porque Anthropic no publica el nombre exacto y ya ha cambiado antes."""
    p = Path(ruta).resolve()
    candidatos = []  # (origen, objeto json)

    def _mirar(nombre, texto):
        try:
            datos = json.loads(texto)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return
        lista = _cargar_json(datos)
        if lista and any(_es_conversacion(o) for o in lista[:20]):
            candidatos.append((nombre, [o for o in lista if _es_conversacion(o)]))

    if p.is_file() and p.suffix.lower() == ".zip":
        with zipfile.ZipFile(p) as z:
            for info in z.infolist():
                if info.is_dir() or not info.filename.lower().endswith(".json"):
                    continue
                if info.file_size > 600 * 1024 * 1024:
                    print(f"AVISO: {info.filename} pesa {humano(info.file_size)}; se omite.")
                    continue
                _mirar(info.filename, z.read(info).decode("utf-8", "replace"))
    elif p.is_dir():
        for f in sorted(p.rglob("*.json")):
            _mirar(str(f.relative_to(p)), f.read_text(encoding="utf-8", errors="replace"))
    elif p.is_file():
        _mirar(p.name, p.read_text(encoding="utf-8", errors="replace"))
    else:
        raise SystemExit(f"ERROR: {p} no existe.")

    if not candidatos:
        raise SystemExit(
            f"ERROR: en {p.name} no hay ningun JSON con estructura de conversaciones.\n"
            "       Comprueba que es el ZIP de Ajustes > Privacidad > Exportar datos\n"
            "       y no el correo ni el enlace. El enlace caduca a las 24 h."
        )
    candidatos.sort(key=lambda c: len(c[1]), reverse=True)
    origen, chats = candidatos[0]
    print(f"Volcado reconocido: {origen} -> {len(chats)} conversaciones.")
    return origen, chats


def filtrar_proyecto(chats, proyecto):
    """Devuelve (seleccionados, metodo, descartados). Si el export no trae campo de
    proyecto, se declara y se cae a coincidencia por texto: nunca se supone."""
    if not proyecto:
        return chats, "sin filtro (se toma el export entero)", []

    objetivo = slug(proyecto)
    con_campo = [c for c in chats if any(_proyecto_de(c))]
    if con_campo:
        sel = []
        for c in chats:
            nombre, uuid = _proyecto_de(c)
            if (nombre and slug(nombre) == objetivo) or (uuid and uuid == proyecto):
                sel.append(c)
        if sel:
            return sel, "campo de proyecto del export [FIABLE]", [c for c in chats if c not in sel]

    # Sin campo utilizable: coincidencia por titulo o por cuerpo. Es un indicio,
    # no una prueba; el metodo devuelto lo dice para que quede en el MANIFIESTO.
    aguja = re.escape(proyecto.strip())
    pat = re.compile(aguja, re.IGNORECASE)
    sel = []
    for c in chats:
        titulo = c.get("name") or c.get("title") or ""
        cuerpo = " ".join(_texto_de(m.get("content") or m.get("text") or m.get("parts") or "")
                          for m in _mensajes_de(c)[:6])
        if pat.search(titulo) or pat.search(cuerpo):
            sel.append(c)
    metodo = ("coincidencia de texto [INDICIO, NO PRUEBA] - el export no trae campo "
              "de proyecto utilizable; revisa la seleccion a mano")
    return sel, metodo, [c for c in chats if c not in sel]


def normalizar(chat, indice):
    msgs = []
    for m in _mensajes_de(chat):
        texto = _texto_de(m.get("content") or m.get("text") or m.get("parts") or "")
        if not texto.strip():
            continue
        msgs.append({
            "rol": _rol_de(m),
            "fecha": (m.get("created_at") or m.get("timestamp") or "")[:19],
            "texto": texto.strip(),
        })
    titulo = (chat.get("name") or chat.get("title") or "").strip() or f"chat-{indice:03d}"
    fechas = [m["fecha"] for m in msgs if m["fecha"]]
    proyecto_nombre, proyecto_uuid = _proyecto_de(chat)
    return {
        "n": indice,
        "uuid": chat.get("uuid") or chat.get("id") or "",
        "titulo": titulo,
        "slug": slug(titulo),
        "proyecto": proyecto_nombre,
        "proyecto_uuid": proyecto_uuid,
        "creado": (chat.get("created_at") or (fechas[0] if fechas else ""))[:19],
        "actualizado": (chat.get("updated_at") or (fechas[-1] if fechas else ""))[:19],
        "n_mensajes": len(msgs),
        "n_palabras": sum(len(m["texto"].split()) for m in msgs),
        "mensajes": msgs,
    }


def senales(chat):
    """Extraccion determinista: lo que el script puede afirmar sin interpretar."""
    decisiones, cifras, pendientes = [], [], []
    for m in chat["mensajes"]:
        for linea in m["texto"].splitlines():
            l = linea.strip()
            if len(l) < 12 or len(l) > 320:
                continue
            if SENAL_DECISION.search(l) and len(decisiones) < 12:
                decisiones.append({"rol": m["rol"], "cita": l})
            elif SENAL_PENDIENTE.search(l) and len(pendientes) < 10:
                pendientes.append({"rol": m["rol"], "cita": l})
        for c in SENAL_CIFRA.findall(m["texto"]):
            if c not in cifras and len(cifras) < 25:
                cifras.append(c)

    palabras = re.findall(r"[a-zA-ZáéíóúñüÁÉÍÓÚÑÜ]{5,}", " ".join(
        m["texto"] for m in chat["mensajes"]))
    cuenta = Counter(p.lower() for p in palabras if p.lower() not in VACIAS)
    return {
        "temas": [t for t, _ in cuenta.most_common(8)],
        "decisiones": decisiones,
        "cifras": cifras,
        "pendientes": pendientes,
        "primer_mensaje": next((m["texto"][:280] for m in chat["mensajes"]
                                if m["rol"] in ("human", "user")), ""),
    }


def escribir_transcripcion(chat, destino):
    p = destino / f"{chat['n']:03d}-{chat['slug']}.md"
    out = [f"# {chat['titulo']}", "",
           f"- **UUID:** `{chat['uuid'] or 'sin uuid'}`",
           f"- **Creado:** {chat['creado'] or '[sin fecha]'}",
           f"- **Ultimo mensaje:** {chat['actualizado'] or '[sin fecha]'}",
           f"- **Mensajes:** {chat['n_mensajes']} · **Palabras:** {chat['n_palabras']}",
           "", "---", ""]
    for m in chat["mensajes"]:
        quien = {"human": "SERGIO", "user": "SERGIO", "assistant": "CLAUDE"}.get(m["rol"], m["rol"].upper())
        out.append(f"### {quien}  ·  {m['fecha'] or '[sin fecha]'}")
        out.append("")
        out.append(m["texto"])
        out.append("")
    p.write_text("\n".join(out), encoding="utf-8")
    return p


def escribir_resumen(chats, sen, destino, proyecto, metodo, descartados, origen):
    """Borrador automatico. Es deterministico: solo cita, cuenta y ordena. La
    lectura de que significa cada decision la firma una persona (o el modelo,
    siguiendo el SKILL.md). Marcado como borrador hasta que alguien lo revise."""
    p = destino / "RESUMEN-CHATS.md"
    tot_msg = sum(c["n_mensajes"] for c in chats)
    tot_pal = sum(c["n_palabras"] for c in chats)
    fechas = sorted(c["creado"] for c in chats if c["creado"])

    o = [f"# RESUMEN DE CHATS · {proyecto or '[proyecto sin nombrar]'}", "",
         "> **[BORRADOR AUTOMATICO]** — generado por `respaldo.py --ingerir` el "
         f"{ahora()}.",
         "> El script cita, cuenta y ordena. **No interpreta.** Lo que cada decision",
         "> significa lo escribe una persona encima de este borrador; hasta entonces",
         "> este archivo es un indice de citas, no un resumen ejecutivo.", "",
         "## Recuento", "",
         f"- **Volcado de origen:** `{origen}`",
         f"- **Chats incluidos:** {len(chats)} · descartados por filtro: {len(descartados)}",
         f"- **Metodo de seleccion:** {metodo}",
         f"- **Mensajes:** {tot_msg} · **Palabras:** {tot_pal}",
         f"- **Periodo:** {fechas[0][:10] if fechas else '[sin fecha]'} a "
         f"{fechas[-1][:10] if fechas else '[sin fecha]'}", "",
         "## Indice", "",
         "| # | Chat | Fecha | Msj | Decisiones | Cifras | Pendientes |",
         "|---|---|---|---|---|---|---|"]
    for c in chats:
        s = sen[c["n"]]
        o.append(f"| {c['n']:03d} | [{c['titulo'][:52]}](transcripciones/"
                 f"{c['n']:03d}-{c['slug']}.md) | {c['creado'][:10] or '—'} | "
                 f"{c['n_mensajes']} | {len(s['decisiones'])} | {len(s['cifras'])} | "
                 f"{len(s['pendientes'])} |")
    o += ["", "---", ""]

    for c in chats:
        s = sen[c["n"]]
        o += [f"## {c['n']:03d} · {c['titulo']}", "",
              f"**Fechas:** {c['creado'][:16] or '—'} → {c['actualizado'][:16] or '—'} · "
              f"**{c['n_mensajes']} mensajes / {c['n_palabras']} palabras**  ",
              f"**Transcripcion:** [`transcripciones/{c['n']:03d}-{c['slug']}.md`]"
              f"(transcripciones/{c['n']:03d}-{c['slug']}.md)", "",
              f"**Temas por frecuencia:** {', '.join(s['temas']) or '—'}", ""]
        if s["primer_mensaje"]:
            o += ["**Como empezo (primer mensaje humano, literal):**", "",
                  "> " + s["primer_mensaje"].replace("\n", " ")[:280], ""]
        if s["decisiones"]:
            o += ["**Candidatos a decision (citas literales, sin interpretar):**", ""]
            o += [f"- `{d['rol']}` — {d['cita']}" for d in s["decisiones"]]
            o.append("")
        if s["cifras"]:
            o += [f"**Cifras que aparecen:** {', '.join(s['cifras'][:20])}", ""]
        if s["pendientes"]:
            o += ["**Marcado como pendiente o a validar:**", ""]
            o += [f"- `{d['rol']}` — {d['cita']}" for d in s["pendientes"]]
            o.append("")
        o += ["**LECTURA DE UNA PERSONA:** _[pendiente de escribir]_", "", "---", ""]

    if descartados:
        o += ["## Chats descartados por el filtro", "",
              "No viajan en el paquete. Si alguno contiene una decision que no esta",
              "escrita en otro sitio, subelo a mano y anotalo en HUECOS.md.", "",
              "| Titulo | Fecha | Msj |", "|---|---|---|"]
        for d in descartados[:80]:
            t = (d.get("name") or d.get("title") or "[sin titulo]")[:60]
            o.append(f"| {t} | {(d.get('created_at') or '')[:10] or '—'} | "
                     f"{len(_mensajes_de(d))} |")
        if len(descartados) > 80:
            o.append(f"| … y {len(descartados) - 80} mas | | |")
        o.append("")

    p.write_text("\n".join(o), encoding="utf-8")
    return p


def ingerir(export, carpeta, proyecto=None, max_chats=None):
    base = Path(carpeta).resolve()
    destino = base / "05-chats"
    (destino / "transcripciones").mkdir(parents=True, exist_ok=True)

    origen, crudos = cargar_export(export)
    sel, metodo, descartados = filtrar_proyecto(crudos, proyecto)
    if not sel:
        print(f"AVISO: ningun chat coincide con el proyecto «{proyecto}».")
        print("       Ejecuta sin --proyecto para volcar el export entero, o revisa el nombre.")
    sel.sort(key=lambda c: (c.get("created_at") or c.get("updated_at") or ""))
    if max_chats:
        sel = sel[:max_chats]

    chats, sen = [], {}
    for i, c in enumerate(sel, 1):
        n = normalizar(c, i)
        if n["n_mensajes"] == 0:
            continue
        chats.append(n)
        sen[n["n"]] = senales(n)
        escribir_transcripcion(n, destino / "transcripciones")

    resumen = escribir_resumen(chats, sen, destino, proyecto, metodo, descartados, origen)

    # jsonl para encadenar con otra skill: una linea por chat, sin transcripcion.
    with (destino / "chats.jsonl").open("w", encoding="utf-8") as f:
        for c in chats:
            f.write(json.dumps({k: v for k, v in c.items() if k != "mensajes"}
                               | {"senales": sen[c["n"]]}, ensure_ascii=False) + "\n")

    res = {
        "origen": origen,
        "chats_en_export": len(crudos),
        "chats_incluidos": len(chats),
        "chats_descartados": len(descartados),
        "metodo_seleccion": metodo,
        "mensajes": sum(c["n_mensajes"] for c in chats),
        "palabras": sum(c["n_palabras"] for c in chats),
        "resumen": str(resumen.relative_to(base)),
        "ingerido_en": ahora(),
    }
    print(json.dumps(res, ensure_ascii=False, indent=2))
    print(f"\n{len(chats)} transcripciones + RESUMEN-CHATS.md en {destino}")
    if "INDICIO" in metodo:
        print("AVISO: la seleccion es un indicio, no una prueba. Revisala antes de sellar.")
    print()
    return res


# --- P4 · recolectar descargas --------------------------------------------------

def _citados(base):
    """Nombres de archivo citados en L1 y L2. Es lo que convierte un barrido de la
    carpeta de Descargas en una recoleccion con criterio."""
    nombres = set()
    for sub in ("01-instrucciones", "02-conocimiento"):
        d = Path(base) / sub
        if not d.is_dir():
            continue
        for f in archivos_de(d):
            if f.suffix.lower() not in EXT_TEXTO:
                continue
            texto = f.read_text(encoding="utf-8", errors="replace")
            # Sin espacio en la clase de caracteres: con el, "Ver informe.pdf" se
            # capturaba entero como nombre de archivo y ningun barrido lo encontraba.
            for cita in re.findall(
                    r"(?<![\w\-.])[\w\-.]+\.(?:pdf|docx|xlsx|csv|pptx|png|jpg|jpeg|md|txt|json|skill|zip)",
                    texto):
                nombres.add(Path(cita.strip()).name.lower())
    return nombres


def _clase_ext(ext):
    for clase, exts in EXT_ADJUNTO.items():
        if ext in exts:
            return clase
    return "otro"


def recolectar(carpetas, carpeta, desde=None, copiar=True):
    base = Path(carpeta).resolve()
    destino = base / "03-adjuntos"
    destino.mkdir(parents=True, exist_ok=True)
    citados = _citados(base)
    corte = None
    if desde:
        try:
            corte = datetime.strptime(desde, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()
        except ValueError:
            raise SystemExit("ERROR: --desde espera formato AAAA-MM-DD.")

    # Pasada 1 · censo. Se agrupa por SHA-256, no por nombre: dos archivos con el
    # mismo contenido son uno, aunque uno se llame "copia de".
    grupos, omitidos = {}, 0
    for c in carpetas:
        raiz = Path(c).expanduser().resolve()
        if not raiz.is_dir():
            print(f"AVISO: {raiz} no es una carpeta accesible; se omite.")
            continue
        for f in sorted(raiz.rglob("*")):
            if not f.is_file() or f.name.startswith("."):
                continue
            st = f.stat()
            if (corte and st.st_mtime < corte) or st.st_size == 0 \
                    or st.st_size > 512 * 1024 * 1024:
                omitidos += 1
                continue
            grupos.setdefault(sha256_archivo(f), []).append((f, st))

    # Pasada 2 · de cada grupo se conserva la copia CITADA en L1/L2. Quedarse con
    # la primera por orden alfabetico tira el archivo que las instrucciones nombran
    # y guarda "copia de (2).pdf": el respaldo queda integro y aun asi ilegible.
    filas, duplicados = [], 0
    for h, miembros in grupos.items():
        miembros.sort(key=lambda m: (m[0].name.lower() not in citados,
                                     len(m[0].name), m[0].name))
        f, st = miembros[0]
        duplicados += len(miembros) - 1
        ext = f.suffix.lower()
        nuevo = f"{len(filas) + 1:03d}-{slug(f.stem, 40)}{ext}"
        if copiar:
            shutil.copy2(f, destino / nuevo)
        filas.append({
            "nombre_en_paquete": nuevo,
            "nombre_original": f.name,
            "clase_tipo": _clase_ext(ext),
            "bytes": st.st_size,
            "modificado": datetime.fromtimestamp(st.st_mtime, timezone.utc)
                          .strftime("%Y-%m-%d"),
            "sha256": h,
            "citado_en_L1_L2": f.name.lower() in citados,
            "origen": str(f.parent),
            "copias_descartadas": [str(m[0]) for m in miembros[1:]],
        })
    filas.sort(key=lambda r: (r["clase_tipo"], r["nombre_original"].lower()))
    for i, r in enumerate(filas, 1):
        antiguo = destino / r["nombre_en_paquete"]
        r["nombre_en_paquete"] = f"{i:03d}-{slug(Path(r['nombre_original']).stem, 40)}" \
                                 f"{Path(r['nombre_original']).suffix.lower()}"
        if copiar and antiguo.exists() and antiguo.name != r["nombre_en_paquete"]:
            antiguo.rename(destino / r["nombre_en_paquete"])

    idx = destino / "INDICE-ADJUNTOS.md"
    o = [f"# INDICE DE ADJUNTOS · {base.name}", "",
         f"Recolectado el {ahora()} desde: {', '.join(str(Path(c).expanduser()) for c in carpetas)}",
         f"Corte por fecha: {desde or 'ninguno'} · duplicados descartados por SHA-256: "
         f"{duplicados} · omitidos por tamano o fecha: {omitidos}", "",
         "**El nombre original es un dato.** En el paquete cada archivo va con nombre",
         "neutro; la correspondencia vive en esta tabla, que viaja dentro del cifrado.", "",
         "| # | En el paquete | Original | Tipo | Tamano | Fecha | Citado en L1/L2 | SHA-256 |",
         "|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(filas, 1):
        o.append(f"| {i} | `{r['nombre_en_paquete']}` | {r['nombre_original']} | "
                 f"{r['clase_tipo']} | {humano(r['bytes'])} | {r['modificado']} | "
                 f"{'si' if r['citado_en_L1_L2'] else 'no'} | `{r['sha256'][:12]}` |")

    sin_citar = [r for r in filas if not r["citado_en_L1_L2"]]
    faltantes = sorted(citados - {r["nombre_original"].lower() for r in filas})
    o += ["", f"## Citados en L1/L2 que NO aparecieron ({len(faltantes)})", ""]
    if faltantes:
        o += ["Antipatron 4. Cada uno va a `HUECOS.md` con su procedencia.", ""]
        o += [f"- `{n}`" for n in faltantes]
    else:
        o.append("Ninguno. Todo lo que citan las instrucciones se recolecto.")
    o += ["", f"## Recolectados que nadie cita ({len(sin_citar)})", "",
          "Sobran o falta una referencia. Decide uno por uno: entra o se descarta.", ""]
    o += [f"- `{r['nombre_en_paquete']}` ({r['nombre_original']})" for r in sin_citar[:60]]
    idx.write_text("\n".join(o) + "\n", encoding="utf-8")

    res = {"recolectados": len(filas), "duplicados": duplicados, "omitidos": omitidos,
           "citados_sin_encontrar": faltantes, "sin_citar": len(sin_citar),
           "indice": str(idx.relative_to(base)), "recolectado_en": ahora()}
    print(json.dumps(res, ensure_ascii=False, indent=2))
    print(f"\n{len(filas)} adjuntos en {destino}. Indice en {idx.name}.")
    if faltantes:
        print(f"AVISO (antipatron 4): {len(faltantes)} archivos citados no aparecieron.")
    print()
    return res


# --- P6 · escanear --------------------------------------------------------------

def escanear(carpeta):
    hallazgos = []
    base = Path(carpeta)
    for ruta in archivos_de(base):
        if ruta.suffix.lower() not in EXT_TEXTO or ruta.name in EXCLUIR_DEL_ESCANEO:
            continue
        try:
            texto = ruta.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for n, linea in enumerate(texto.splitlines(), 1):
            for clase, etiqueta, patron in PATRONES:
                m = re.search(patron, linea)
                if m:
                    frag = m.group(0)
                    visible = frag[:4] + "…" + frag[-2:] if len(frag) > 10 else "…"
                    hallazgos.append({
                        "archivo": str(ruta.relative_to(base)),
                        "linea": n,
                        "clase": clase,
                        "tipo": etiqueta,
                        "fragmento": visible,
                    })
                    break  # una clase por linea: se para en la primera que cumple
    return hallazgos


def informe_escaneo(hallazgos):
    c3 = [h for h in hallazgos if h["clase"] == "C3"]
    c2 = [h for h in hallazgos if h["clase"] == "C2"]
    print(f"\n== ESCANEO ==  C3 (secreto): {len(c3)}   C2 (confidencial): {len(c2)}")
    for h in hallazgos[:200]:
        print(f"  [{h['clase']}] {h['archivo']}:{h['linea']}  {h['tipo']}  ({h['fragmento']})")
    if len(hallazgos) > 200:
        print(f"  … y {len(hallazgos) - 200} hallazgos mas.")
    if c3:
        print("\nBLOQUEANTE: hay hallazgos C3. Regla NUNCA-1: un secreto se ROTA, no se respalda.")
        print("Sacalo del paquete, rotalo en su origen y deja [REDACTADO:credencial - rotada AAAA-MM-DD].")
        print("El marcador [REDACTADO:...] ya NO vuelve a disparar el patron (v2.0.0, gotcha G-1).")
    elif not hallazgos:
        print("  Sin hallazgos. El escaner detecta patrones conocidos, no todo dato sensible.")
    print("El script propone; la clasificacion la firma una persona.\n")
    return len(c3)


# --- P8 · RESTAURAR-TODO.md, el archivo maestro ---------------------------------

def _leer_capa(base, sub, max_bytes=None):
    d = Path(base) / sub
    if not d.is_dir():
        return []
    salida = []
    for f in sorted(archivos_de(d)):
        try:
            t = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            t = ""
        if max_bytes and len(t) > max_bytes:
            t = t[:max_bytes] + f"\n\n[… truncado. Integro en `{sub}/{f.relative_to(d).as_posix()}`]"
        salida.append((f.relative_to(d).as_posix(), t, f))
    return salida


def restaurar_todo(carpeta, proyecto=None, paquete=None):
    """UN archivo con todo lo necesario para volver a levantar el proyecto: las
    instrucciones integras, el inventario, el resumen de chats y los pasos.
    Quien lo abre no necesita ni el resto del paquete para saber que habia."""
    base = Path(carpeta).resolve()
    nombre = proyecto or base.name
    marca = base / ".respaldo.json"
    if not proyecto and marca.exists():
        try:
            nombre = json.loads(marca.read_text(encoding="utf-8")).get("proyecto", nombre)
        except json.JSONDecodeError:
            pass

    instrucciones = _leer_capa(base, "01-instrucciones")
    conocimiento = _leer_capa(base, "02-conocimiento", max_bytes=6000)
    adjuntos = [f for f in archivos_de(base / "03-adjuntos")] if (base / "03-adjuntos").is_dir() else []
    skills = sorted({p.parts[0] for p in
                     [f.relative_to(base / "04-skills") for f in archivos_de(base / "04-skills")]}) \
        if (base / "04-skills").is_dir() else []
    resumen_chats = base / "05-chats" / "RESUMEN-CHATS.md"
    transcripciones = list((base / "05-chats" / "transcripciones").glob("*.md")) \
        if (base / "05-chats" / "transcripciones").is_dir() else []
    huecos = base / "HUECOS.md"

    o = [f"# RESTAURAR TODO · {nombre}", "",
         f"**Generado:** {ahora()} · `respaldo.py` v{VERSION}  ",
         f"**Paquete previsto:** `{paquete or 'respaldo-' + base.name + '-' + hoy() + '.zip'}`  ",
         "**SHA-256 del paquete:** no puede figurar aqui — un archivo no puede contener",
         "la huella del contenedor que lo contiene. Te llega por el canal B y la",
         "comprueba `--verificar`. Si no coincide, para y avisa.  ",
         "**Verificado en frio (P10):** `[PENDIENTE hasta ejecutar --verificar]`", "",
         "> Este archivo es autosuficiente para saber **que habia** en el proyecto.",
         "> Para volver a tenerlo funcionando hacen falta ademas las carpetas del",
         "> paquete, porque los adjuntos binarios no caben en un texto.", "",
         "---", "",
         "## 0 · Lo primero, y no es opcional", "",
         "Anthropic **no soporta migrar datos entre cuentas personales**: *\"Exported",
         "data can't be imported into another personal Claude account, and we don't",
         "support migrating data between personal accounts.\"* (support.claude.com,",
         "art. 9450526). Esto no es una importacion: es **reconstruccion manual**.",
         "No busques un boton. No existe.", "",
         "---", "",
         "## 1 · Que hay en este respaldo", "",
         "| Capa | Elementos | Donde |", "|---|---|---|",
         f"| L1 Instrucciones | {len(instrucciones)} | integras mas abajo, seccion 3 |",
         f"| L2 Conocimiento | {len(conocimiento)} | `02-conocimiento/` · indice en seccion 4 |",
         f"| L3 Adjuntos | {len(adjuntos)} | `03-adjuntos/` · indice en `INDICE-ADJUNTOS.md` |",
         f"| L4 Skills | {len(skills)} | `04-skills/` |",
         f"| L5 Chats | {len(transcripciones)} | `05-chats/` · resumen en seccion 6 |", "",
         "---", "",
         "## 2 · Los 10 pasos, en este orden", "",
         "El orden no es estetico. Cada paso deja en pie lo que el siguiente necesita.", "",
         "1. **Verifica el paquete antes de tocar nada.**",
         "   `python3 scripts/respaldo.py --verificar <paquete>.zip`",
         "   Si la huella no coincide con la que te dieron por el canal B, **para y avisa**.",
         "2. **Crea el proyecto** en la cuenta destino. Nombre exacto: "
         f"`{nombre}`.",
         "3. **Pega L1 entero y de una vez** en el campo de instrucciones del proyecto.",
         "   Esta integro en la seccion 3 de este archivo. Es lo unico irremplazable.",
         "4. **Sube L3 antes que L2.** Si un documento de conocimiento cita un adjunto,",
         "   la referencia ya existe cuando se crea el documento.",
         "5. **Crea L2**, un documento por archivo de `02-conocimiento/`, **respetando el",
         "   nombre exacto**: L1 cita archivos por su nombre y una `s` de mas los rompe.",
         "6. **Instala L4**: cada `.skill` de `04-skills/` en la cuenta destino.",
         "7. **Sube el resumen de chats** (seccion 6) como un documento mas de L2. Es lo",
         "   que devuelve al proyecto la memoria de lo que se decidio y no se escribio.",
         "8. **Deshaz la redaccion** sustituyendo cada `[REDACTADO:tipo]` con",
         "   `DICCIONARIO.md`, **que llega por separado**. Sin el, el proyecto funciona",
         "   igual: solo pierde los nombres propios.",
         "9. **Repasa `HUECOS.md`** y decide que se recupera a mano y que se da por perdido.",
         "10. **Prueba de humo** (seccion 7). Si falla, algo de L2 no subio: cruza el",
         "    inventario contra lo que hay en el proyecto.", "",
         "---", "",
         "## 3 · L1 · INSTRUCCIONES DEL PROYECTO (integras, para pegar)", ""]

    if instrucciones:
        for rel, texto, _ in instrucciones:
            o += [f"### `{rel}`", "", "```markdown", texto.rstrip(), "```", ""]
    else:
        o += ["> **[HUECO]** No hay ningun archivo en `01-instrucciones/`. Esta es la",
              "> capa irremplazable: sin ella el proyecto no se reconstruye, se reinventa.", ""]

    o += ["---", "", "## 4 · L2 · BASE DE CONOCIMIENTO", ""]
    if conocimiento:
        o += ["| # | Documento | Tamano | Primeras lineas |", "|---|---|---|---|"]
        for i, (rel, texto, f) in enumerate(conocimiento, 1):
            cabeza = " ".join(texto.strip().splitlines()[:2])[:90].replace("|", "/")
            o.append(f"| {i} | `{rel}` | {humano(f.stat().st_size)} | {cabeza} |")
        o += ["", "### Contenido (hasta 6.000 caracteres por documento)", ""]
        for rel, texto, _ in conocimiento:
            o += [f"#### `{rel}`", "", texto.rstrip(), "", "---", ""]
    else:
        o += ["> **Capa vacia en origen.** No es un fallo del respaldo: no habia",
              "> documentos de conocimiento en el proyecto.", ""]

    o += ["## 5 · L3 y L4 · ADJUNTOS Y SKILLS", ""]
    if adjuntos:
        o += [f"{len(adjuntos)} archivos en `03-adjuntos/`. La correspondencia entre el",
              "nombre neutro del paquete y el nombre original esta en",
              "`03-adjuntos/INDICE-ADJUNTOS.md`. **No renombres antes de subir**: el",
              "indice es lo unico que sabe cual era cual.", ""]
    else:
        o += ["Sin adjuntos.", ""]
    if skills:
        o += ["Skills incluidas:", ""] + [f"- `{s}`" for s in skills] + [""]
    else:
        o += ["Sin skills asociadas.", ""]

    o += ["---", "", "## 6 · L5 · QUE SE DECIDIO EN LOS CHATS", ""]
    if resumen_chats.exists():
        cuerpo = resumen_chats.read_text(encoding="utf-8", errors="replace")
        cuerpo = re.sub(r"^# .*\n", "", cuerpo, count=1)
        o += [cuerpo.strip(), ""]
    else:
        o += ["> **[HUECO]** No se ha ingerido ningun export de chats.",
              "> Ejecuta `respaldo.py --ingerir <export>.zip --carpeta . --proyecto \"" + nombre + "\"`",
              "> o declara en `HUECOS.md` que el historial no viajo y por que.", ""]

    o += ["---", "", "## 7 · Prueba de humo", "",
          "Una pregunta cuya respuesta correcta **solo es posible si el proyecto se",
          "reconstruyo bien**. No \"¿funcionas?\", sino algo que obligue a usar un dato",
          "que solo vive en la base de conocimiento. **Se escribe aqui, en el origen**,",
          "porque quien reconstruye no sabe que deberia salir.", "",
          "- **Pregunta:** `[escribir antes de sellar]`",
          "- **Respuesta correcta:** `[escribir antes de sellar]`",
          "- **Dato exacto que debe aparecer:** `[escribir antes de sellar]`",
          "- **Donde vive ese dato:** `[archivo]`", "",
          "---", "", "## 8 · Huecos declarados", ""]
    if huecos.exists():
        o += [huecos.read_text(encoding="utf-8", errors="replace").strip(), ""]
    else:
        o += ["> `HUECOS.md` no existe todavia. **Mientras no exista o no este vacio,",
              "> este respaldo se declara PARCIAL, nunca COMPLETO.**", ""]

    o += ["---", "", "## 9 · Lo que NO se reconstruye, y no es un fallo", "",
          "- El historial de chats como conversaciones vivas: viajan como texto, no",
          "  como hilos que se puedan continuar.",
          "- Los permisos y miembros, si el origen era Team o Enterprise.",
          "- El comportamiento identico: en proyectos grandes la recuperacion puede",
          "  seleccionar fragmentos distintos. El contenido es el mismo; la respuesta",
          "  literal puede variar.", "",
          "---", "", "## 10 · Acta de reconstruccion", "",
          "| Campo | Valor |", "|---|---|",
          "| Reconstruido el | `[fecha]` |", "| Por | `[alias]` |",
          "| Prueba de humo | `[superada / fallida]` |",
          "| Huecos que siguen abiertos | `[n]` |",
          "| Diferencias observadas | `[texto]` |", ""]

    p = base / "RESTAURAR-TODO.md"
    p.write_text("\n".join(o), encoding="utf-8")
    print(f"Archivo maestro: {p}  ({humano(p.stat().st_size)})")
    if not instrucciones:
        print("AVISO: L1 vacia. Es la capa irremplazable; comprueba que la extrajiste.")
    if not resumen_chats.exists():
        print("AVISO: sin resumen de chats. Ejecuta --ingerir o declara el hueco.")
    return {"archivo": str(p.relative_to(base)), "bytes": p.stat().st_size,
            "l1": len(instrucciones), "l2": len(conocimiento), "l3": len(adjuntos),
            "l4": len(skills), "l5": len(transcripciones)}


# --- P9 · empaquetar ------------------------------------------------------------

def escribir_checksums(carpeta):
    base = Path(carpeta)
    destino = base / "CHECKSUMS.txt"
    if destino.exists():
        destino.unlink()
    lineas = []
    for ruta in archivos_de(base):
        rel = ruta.relative_to(base).as_posix()
        lineas.append(f"{sha256_archivo(ruta)}  {rel}")
    destino.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return len(lineas)


def comprobar_rutas_citadas(carpeta):
    """Antipatron 4: toda ruta citada en 01-instrucciones/ debe existir en el arbol."""
    base = Path(carpeta)
    existentes = {p.name for p in archivos_de(base)}
    faltan = []
    for ruta in archivos_de(base):
        if not any(k in ruta.as_posix() for k in PALABRAS_CLAVE_INSTRUCCIONES):
            continue
        if ruta.suffix.lower() not in EXT_TEXTO:
            continue
        texto = ruta.read_text(encoding="utf-8", errors="replace")
        for cita in set(re.findall(r"[\w\-/\.]+\.(?:md|txt|pdf|csv|xlsx|docx|json|skill)", texto)):
            nombre = Path(cita).name
            if nombre not in existentes and nombre not in faltan:
                faltan.append(nombre)
    return faltan


def empaquetar(carpeta, salida=None, sin_cifrar=False):
    base = Path(carpeta).resolve()
    if not base.is_dir():
        raise SystemExit(f"ERROR: {base} no es una carpeta.")

    hallazgos = escanear(base)
    n_c3 = informe_escaneo(hallazgos)
    if n_c3:
        raise SystemExit("Sellado abortado por hallazgos C3. Corrige y vuelve a ejecutar.")

    faltan = comprobar_rutas_citadas(base)
    if faltan:
        print("AVISO (antipatron 4): rutas citadas en 01-instrucciones/ sin archivo real:")
        for f in faltan:
            print(f"  - {f}   -> declarala en HUECOS.md")
        print()

    if not (base / "RESTAURAR-TODO.md").exists():
        print("AVISO: no hay RESTAURAR-TODO.md. Genera el archivo maestro antes de sellar")
        print("       (--restaurar-todo); sin el, el paquete no se explica solo.\n")

    n = escribir_checksums(base)
    nombre = salida or f"respaldo-{base.name}-{hoy()}.zip"
    cifrar = HAY_AES and not sin_cifrar
    if not cifrar:
        raiz, ext = os.path.splitext(nombre)
        nombre = f"{raiz}-SIN-CIFRAR{ext}"
        if not HAY_AES and not sin_cifrar:
            print("AVISO: pyzipper no esta instalado -> el paquete NO va cifrado.")
            print("       Instalalo con: pip install pyzipper")
            print("       O acepta el paquete marcado [SIN CIFRAR] y cifralo aparte.\n")
    destino = Path(nombre).resolve()

    # ZIP interno sin cifrar: es lo que oculta nombres y estructura (antipatron 2).
    tmp = Path(tempfile.mkdtemp(prefix="respaldo_"))
    interno = tmp / "contenido.zip"
    try:
        with zipfile.ZipFile(interno, "w", zipfile.ZIP_DEFLATED) as z:
            for ruta in archivos_de(base):
                z.write(ruta, ruta.relative_to(base).as_posix())

        if cifrar:
            pwd = pedir_password(confirmar=True)
            with pyzipper.AESZipFile(destino, "w",
                                     compression=pyzipper.ZIP_DEFLATED,
                                     encryption=pyzipper.WZ_AES) as z:
                z.setpassword(pwd.encode("utf-8"))
                z.setencryption(pyzipper.WZ_AES, nbits=256)
                z.write(interno, "contenido.zip")
        else:
            with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
                z.write(interno, "contenido.zip")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    huella = sha256_archivo(destino)
    por_clase = {}
    for h in hallazgos:
        por_clase[h["clase"]] = por_clase.get(h["clase"], 0) + 1

    resultado = {
        "version_skill": VERSION,
        "paquete": destino.name,
        "ruta": str(destino),
        "sha256": huella,
        "cifrado": "AES-256" if cifrar else "NINGUNO",
        "n_archivos": n,
        "por_clase": por_clase,
        "huecos": faltan,
        "hallazgos_escaneo": len(hallazgos),
        "sellado_en": ahora(),
        "verificado_en": None,
    }
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    print(f"\nPaquete: {destino}")
    print(f"SHA-256: {huella}")
    print("Envia esta huella por el MISMO canal que la contrasena, no con el paquete (P11).")
    print("Siguiente paso obligatorio: --verificar en una carpeta vacia distinta.\n")
    return resultado


# --- P10 · verificar ------------------------------------------------------------

def verificar(paquete):
    ruta = Path(paquete).resolve()
    if not ruta.is_file():
        raise SystemExit(f"ERROR: {ruta} no existe.")
    print(f"SHA-256 del paquete: {sha256_archivo(ruta)}")

    tmp = Path(tempfile.mkdtemp(prefix="verif_"))
    try:
        with zipfile.ZipFile(ruta) as z:
            cifrado = any(i.flag_bits & 0x1 for i in z.infolist())

        if cifrado:
            if not HAY_AES:
                raise SystemExit("ERROR: paquete cifrado y pyzipper no esta instalado.")
            pwd = pedir_password()
            try:
                with pyzipper.AESZipFile(ruta) as z:
                    z.setpassword(pwd.encode("utf-8"))
                    z.extractall(tmp)
            except RuntimeError:
                raise SystemExit(
                    "ERROR: contrasena incorrecta o paquete corrupto.\n"
                    "       Contrasta la huella SHA-256 impresa arriba con la que te\n"
                    "       enviaron por el canal B. Si coincide, es la contrasena."
                )
        else:
            print("AVISO: este paquete NO esta cifrado.")
            with zipfile.ZipFile(ruta) as z:
                z.extractall(tmp)

        interno = tmp / "contenido.zip"
        destino = tmp / "contenido"
        if interno.exists():
            with zipfile.ZipFile(interno) as z:
                z.extractall(destino)
        else:
            destino = tmp

        chk = destino / "CHECKSUMS.txt"
        if not chk.exists():
            raise SystemExit("ERROR: falta CHECKSUMS.txt. El paquete no es verificable.")

        ok = fallo = ausente = 0
        for linea in chk.read_text(encoding="utf-8").splitlines():
            if not linea.strip():
                continue
            esperado, rel = linea.split("  ", 1)
            f = destino / rel
            if rel == "CHECKSUMS.txt":
                continue
            if not f.exists():
                print(f"  AUSENTE  {rel}")
                ausente += 1
            elif sha256_archivo(f) == esperado:
                ok += 1
            else:
                print(f"  ALTERADO {rel}")
                fallo += 1

        maestro = destino / "RESTAURAR-TODO.md"
        print(f"\n== VERIFICACION ==  OK: {ok}   ALTERADOS: {fallo}   AUSENTES: {ausente}")
        print(f"Archivo maestro RESTAURAR-TODO.md: {'presente' if maestro.exists() else 'AUSENTE'}")
        if fallo or ausente:
            print("El paquete NO es valido. Se rehace completo, no se parchea.")
            return 1
        if not maestro.exists():
            print("El paquete es integro pero no se explica solo. Genera el maestro y resella.")
            return 1
        print(f"Paquete integro. Anota en MANIFIESTO.md: verificado_en = {ahora()}")
        print("Abre ademas 3 archivos de 3 carpetas distintas. El checksum prueba")
        print("integridad, no que el contenido sea el que creias respaldar.\n")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --- modo --auto ----------------------------------------------------------------

def auto(carpeta, export=None, descargas=None, proyecto=None, desde=None,
         salida=None, sin_cifrar=False):
    base = Path(carpeta).resolve()
    print("=" * 70)
    print(f"MODO AUTO · {base}")
    print("=" * 70)
    acta = {"carpeta": str(base), "iniciado_en": ahora(), "pasos": {}}

    acta["pasos"]["preparar"] = preparar(base, proyecto)
    if export:
        acta["pasos"]["ingerir"] = ingerir(export, base, proyecto)
    else:
        print("Sin --export: L5 queda vacia. Se declara como hueco en el maestro.\n")
        acta["pasos"]["ingerir"] = {"omitido": "no se aporto export de chats"}
    if descargas:
        acta["pasos"]["recolectar"] = recolectar(descargas, base, desde)
    else:
        print("Sin --descargas: no se barrio ninguna carpeta local.\n")
        acta["pasos"]["recolectar"] = {"omitido": "no se aportaron carpetas"}

    n_c3 = informe_escaneo(escanear(base))
    acta["pasos"]["escaneo_c3"] = n_c3
    if n_c3:
        print("AUTO DETENIDO: hay secretos. Rotalos y redactalos antes de sellar.")
        print("Nada se ha empaquetado. El arbol y el resumen quedan en la carpeta.\n")
        acta["resultado"] = "DETENIDO POR C3"
        return acta

    nombre_previsto = Path(salida).name if salida else f"respaldo-{base.name}-{hoy()}.zip"
    acta["pasos"]["maestro"] = restaurar_todo(base, proyecto, paquete=nombre_previsto)
    sello = empaquetar(base, salida, sin_cifrar)
    acta["pasos"]["empaquetar"] = sello

    codigo = verificar(sello["ruta"])
    acta["pasos"]["verificacion"] = "OK" if codigo == 0 else "FALLIDA"
    acta["resultado"] = "SELLADO Y VERIFICADO" if codigo == 0 else "SELLADO, VERIFICACION FALLIDA"
    acta["terminado_en"] = ahora()
    acta_p = base.parent / f"ACTA-{base.name}-{hoy()}.json"
    acta_p.write_text(json.dumps(acta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"resultado": acta["resultado"], "paquete": sello["ruta"],
                      "sha256": sello["sha256"], "acta": str(acta_p)},
                     ensure_ascii=False, indent=2))
    print("\nLa huella de arriba viaja por el canal B, NUNCA con el paquete.\n")
    return acta


# --- demostracion ---------------------------------------------------------------

def ejemplo():
    tmp = Path(tempfile.mkdtemp(prefix="ejemplo_"))
    base = tmp / "proyecto-demo"
    preparar(base, "proyecto-demo")
    (base / "01-instrucciones" / "INSTRUCCIONES.md").write_text(
        "# Instrucciones\nEl metodo completo esta en metodo.md y en CATALOGO_INEXISTENTE.md.\n",
        encoding="utf-8")
    (base / "02-conocimiento" / "metodo.md").write_text(
        "# Metodo\nTres fases: delimitar, construir, auditar.\n", encoding="utf-8")
    (base / "03-adjuntos" / "notas.txt").write_text(
        "Contacto de referencia: [REDACTADO:correo]\n"
        "password=[REDACTADO:credencial - rotada 2026-08-16]\n", encoding="utf-8")

    export = tmp / "export-demo.json"
    export.write_text(json.dumps([{
        "uuid": "aaaa-1111", "name": "Precio de la instalacion",
        "created_at": "2026-08-10T10:00:00Z", "updated_at": "2026-08-10T11:00:00Z",
        "project": {"name": "proyecto-demo", "uuid": "proj-1"},
        "chat_messages": [
            {"sender": "human", "created_at": "2026-08-10T10:00:00Z",
             "text": "Cuanto cobro por instalar el sistema en un restaurante mediano?"},
            {"sender": "assistant", "created_at": "2026-08-10T10:02:00Z",
             "content": [{"type": "text", "text":
                          "Decidimos que el precio queda en 2.500 EUR de instalacion mas "
                          "190 EUR/mes de mantenimiento. Queda pendiente validar el IVA con "
                          "el contador."}]},
        ]}, {
        "uuid": "bbbb-2222", "name": "Chat de otro proyecto",
        "created_at": "2026-08-01T09:00:00Z",
        "project": {"name": "otra-cosa", "uuid": "proj-9"},
        "chat_messages": [{"sender": "human", "text": "Esto no deberia viajar."}],
    }], ensure_ascii=False), encoding="utf-8")

    print("=" * 70)
    print("DEMOSTRACION 1/2 · ciclo completo con --auto")
    print("=" * 70)
    os.environ.setdefault("RESPALDO_PASSWORD", "demo-contrasena-larga-de-ejemplo-2026")
    auto(base, export=str(export), proyecto="proyecto-demo",
         salida=str(tmp / "demo.zip"))

    print("=" * 70)
    print("DEMOSTRACION 2/2 · se cuela un secreto C3 -> el sellado se detiene")
    print("=" * 70)
    (base / "02-conocimiento" / "config.md").write_text(
        "api_key: sk-ant-EJEMPLOFALSO000000000000000000\n", encoding="utf-8")
    try:
        empaquetar(base, salida=str(tmp / "demo2.zip"))
        print("FALLO DE LA PRUEBA: deberia haberse detenido.")
        return 1
    except SystemExit as e:
        print(f"Detenido como debe: {e}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0


def main():
    p = argparse.ArgumentParser(description=f"respaldo.py v{VERSION}")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--preparar", metavar="CARPETA")
    g.add_argument("--ingerir", metavar="EXPORT",
                   help="ZIP del export oficial, carpeta descomprimida o .json suelto")
    g.add_argument("--recolectar", metavar="CARPETA", nargs="+")
    g.add_argument("--escanear", metavar="CARPETA")
    g.add_argument("--restaurar-todo", metavar="CARPETA", dest="restaurar_todo")
    g.add_argument("--empaquetar", metavar="CARPETA")
    g.add_argument("--verificar", metavar="PAQUETE")
    g.add_argument("--auto", metavar="CARPETA")
    g.add_argument("--ejemplo", action="store_true")

    p.add_argument("--carpeta", metavar="CARPETA", default=".",
                   help="carpeta de trabajo del respaldo (destino de --ingerir/--recolectar)")
    p.add_argument("--proyecto", metavar="NOMBRE", default=None)
    p.add_argument("--export", metavar="ZIP", default=None, help="para --auto")
    p.add_argument("--descargas", metavar="CARPETA", nargs="+", default=None,
                   help="para --auto: carpetas locales a barrer")
    p.add_argument("--desde", metavar="AAAA-MM-DD", default=None,
                   help="al recolectar, ignora lo modificado antes de esta fecha")
    p.add_argument("--max-chats", type=int, default=None)
    p.add_argument("--salida", metavar="ZIP", default=None)
    p.add_argument("--sin-cifrar", action="store_true",
                   help="genera el paquete sin cifrar y lo marca [SIN CIFRAR] en el nombre")
    a = p.parse_args()

    if a.ejemplo:
        return ejemplo()
    if a.preparar:
        preparar(a.preparar, a.proyecto)
        return 0
    if a.ingerir:
        ingerir(a.ingerir, a.carpeta, a.proyecto, a.max_chats)
        return 0
    if a.recolectar:
        recolectar(a.recolectar, a.carpeta, a.desde)
        return 0
    if a.escanear:
        return 1 if informe_escaneo(escanear(a.escanear)) else 0
    if a.restaurar_todo:
        restaurar_todo(a.restaurar_todo, a.proyecto)
        return 0
    if a.empaquetar:
        empaquetar(a.empaquetar, a.salida, a.sin_cifrar)
        return 0
    if a.auto:
        r = auto(a.auto, a.export, a.descargas, a.proyecto, a.desde, a.salida, a.sin_cifrar)
        return 0 if r.get("resultado", "").startswith("SELLADO Y") else 1
    return verificar(a.verificar)


if __name__ == "__main__":
    sys.exit(main())
