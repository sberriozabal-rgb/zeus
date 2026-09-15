#!/usr/bin/env python3
"""
chats.py — Digiere el historial de chats del proyecto y produce:
  <trabajo>/chats/transcripciones/NNN-<slug>.md   (una por chat)
  <trabajo>/chats/chats.jsonl                      (una línea por chat, normalizado)
  <trabajo>/chats/RESUMEN_CHATS_BORRADOR.md        (índice, temas, decisiones candidatas,
                                                    cifras, pendientes, documentos producidos)

Dos entradas posibles, y se declara cuál fue:
  A) --export <ZIP|carpeta|json>   el export oficial (Ajustes → Privacidad → Exportar datos).
                                   Filtra por --proyecto. Método [FIABLE] si el export trae
                                   campo de proyecto; [INDICIO] si se cae a texto.
  B) --jsonl <archivo>             volcado que el propio Claude escribe en sesión con las
                                   herramientas recent_chats / conversation_search /
                                   read_conversation. Formato por línea:
                                   {"titulo": "...", "fecha": "AAAA-MM-DD", "url": "...",
                                    "mensajes": [{"rol": "usuario|asistente", "texto": "..."}]}
                                   Método [SESIÓN: parcial por diseño].

El resumen es un BORRADOR: cita, cuenta y ordena. No interpreta. La lectura de
cada chat (qué se decidió de verdad) la escribe el modelo en la FASE 3, no este script.
"""
import argparse, json, re, sys, zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path

DECISION = re.compile(r"(?i)\b(decidimos|queda acordado|acordamos|aprobado|se aprueba|ACORDADO|"
                      r"vamos con|nos quedamos con|definitivo|confirmo|confirmado|cerramos)\b")
PENDIENTE = re.compile(r"(?i)\b(pendiente|falta|por definir|a validar|A VALIDAR|TODO|hay que|"
                       r"queda abierto|sin resolver|bloqueado)\b")
CIFRA = re.compile(r"(?:\$|MXN|USD|€|EUR)\s?\d[\d.,]*|\d[\d.,]*\s?(?:%|MXN|USD|pesos|euros|€|semanas?|meses?|días?)")
DOCUMENTO = re.compile(r"(?i)(?<![\w/])[\w\-.áéíóúñ]{2,80}\.(?:docx|pdf|pptx|xlsx|md|html|zip|skill|csv|png|jpg|gs)\b")
STOP = set("""de la que el en y a los del se las por un para con no una su al lo como más pero sus le
ya o este sí porque esta entre cuando muy sin sobre también me hasta hay donde quien desde todo nos
durante todos uno les ni contra otros ese eso ante ellos e esto mí antes algunos qué unos yo otro
otras otra él tanto esa estos mucho quienes nada muchos cual poco ella estar estas algunas algo
nosotros the of and to in is it for on that this with as be are or an at by from""".split())


def slug(t, n=48):
    t = re.sub(r"[^\w\s-]", "", (t or "chat").lower()).strip()
    return re.sub(r"[\s_-]+", "-", t)[:n] or "chat"


# ---------- A) export oficial ----------
def _texto(b):
    if isinstance(b, str): return b
    if isinstance(b, dict):
        for k in ("text", "content", "value"):
            v = b.get(k)
            if isinstance(v, str): return v
            if isinstance(v, list): return "\n".join(_texto(x) for x in v)
    if isinstance(b, list): return "\n".join(_texto(x) for x in b)
    return ""


def _es_conv(o):
    return isinstance(o, dict) and any(k in o for k in ("chat_messages", "messages", "conversation"))


def cargar_export(ruta):
    ruta = Path(ruta); brutos = []
    def mirar(nombre, texto):
        try: d = json.loads(texto)
        except Exception: return
        if isinstance(d, list): brutos.extend(x for x in d if _es_conv(x))
        elif _es_conv(d): brutos.append(d)
        elif isinstance(d, dict):
            for v in d.values():
                if isinstance(v, list): brutos.extend(x for x in v if _es_conv(x))
    if ruta.is_file() and ruta.suffix.lower() == ".zip":
        with zipfile.ZipFile(ruta) as z:
            for n in z.namelist():
                if n.lower().endswith(".json"): mirar(n, z.read(n).decode("utf-8", "replace"))
    elif ruta.is_dir():
        for p in ruta.rglob("*.json"): mirar(p.name, p.read_text("utf-8", "replace"))
    else:
        mirar(ruta.name, ruta.read_text("utf-8", "replace"))
    return brutos


def normalizar_export(c):
    msgs = c.get("chat_messages") or c.get("messages") or []
    out = []
    for m in msgs:
        rol = (m.get("sender") or m.get("role") or "").lower()
        rol = "usuario" if rol in ("human", "user") else "asistente"
        t = _texto(m.get("content") or m.get("text") or "")
        if t.strip(): out.append({"rol": rol, "texto": t.strip()})
    fecha = (c.get("created_at") or c.get("updated_at") or "")[:10]
    proy = c.get("project") or c.get("project_name") or c.get("project_uuid") or ""
    if isinstance(proy, dict): proy = proy.get("name") or proy.get("uuid") or ""
    return {"titulo": c.get("name") or c.get("title") or "(sin título)", "fecha": fecha,
            "url": c.get("uuid") and f"claude.ai/chat/{c['uuid']}" or "", "proyecto": str(proy),
            "mensajes": out}


def filtrar(chats, proyecto):
    if not proyecto: return chats, "SIN FILTRO"
    con_campo = [c for c in chats if c["proyecto"]]
    if con_campo:
        sel = [c for c in chats if proyecto.lower() in c["proyecto"].lower()]
        return sel, "FIABLE (campo de proyecto del export)"
    sel = [c for c in chats if proyecto.lower() in (c["titulo"] + " " +
           " ".join(m["texto"][:400] for m in c["mensajes"][:3])).lower()]
    return sel, "INDICIO, NO PRUEBA (coincidencia de texto; revisar a mano)"


# ---------- señales ----------
def senales(chat):
    dec, pen, cif, docs, palabras = [], [], Counter(), Counter(), Counter()
    for m in chat["mensajes"]:
        for fr in re.split(r"(?<=[.!?\n])\s+", m["texto"]):
            f = fr.strip()
            if not f or len(f) > 400: continue
            if DECISION.search(f): dec.append((m["rol"], f))
            if PENDIENTE.search(f): pen.append((m["rol"], f))
        cif.update(x.strip() for x in CIFRA.findall(m["texto"]))
        docs.update(x.group(0).strip() for x in DOCUMENTO.finditer(m["texto"]))
        palabras.update(w for w in re.findall(r"[a-záéíóúñ]{4,}", m["texto"].lower()) if w not in STOP)
    return {"decisiones": dec[:12], "pendientes": pen[:12], "cifras": cif.most_common(10),
            "documentos": docs.most_common(20), "temas": [w for w, _ in palabras.most_common(8)]}


def escribir(chats, metodo, origen, trabajo):
    base = Path(trabajo) / "chats"; tr = base / "transcripciones"; tr.mkdir(parents=True, exist_ok=True)
    chats = sorted(chats, key=lambda c: c["fecha"] or "0000")
    L = [f"# RESUMEN DE CHATS — BORRADOR AUTOMÁTICO", "",
         f"Origen: {origen} · Método de selección: **{metodo}** · Chats: {len(chats)} · "
         f"Generado: {datetime.now():%Y-%m-%d %H:%M}", "",
         "> Este borrador cita, cuenta y ordena. **No interpreta.** Cada chat lleva la línea "
         "`LECTURA:` que el compilador debe escribir en la FASE 3 antes de entregar.", "",
         "## Índice", "", "| # | Fecha | Chat | Mensajes | Temas |", "|---|---|---|---|---|"]
    todas_docs, todas_dec, todas_pen, temas_g = Counter(), [], [], Counter()
    with open(base / "chats.jsonl", "w", encoding="utf-8") as jl:
        for i, c in enumerate(chats, 1):
            s = senales(c); c["senales"] = s
            temas_g.update(s["temas"]); todas_docs.update(dict(s["documentos"]))
            todas_dec += [(c["titulo"], r, f) for r, f in s["decisiones"]]
            todas_pen += [(c["titulo"], r, f) for r, f in s["pendientes"]]
            jl.write(json.dumps(c, ensure_ascii=False) + "\n")
            nombre = f"{i:03d}-{slug(c['titulo'])}.md"
            L.append(f"| {i} | {c['fecha']} | [{c['titulo']}](transcripciones/{nombre}) | {len(c['mensajes'])} | {', '.join(s['temas'][:4])} |")
            T = [f"# {c['titulo']}", "", f"Fecha: {c['fecha']} · Enlace: {c['url'] or '—'} · Mensajes: {len(c['mensajes'])}", "",
                 f"**Temas:** {', '.join(s['temas'])}", "", "**Decisiones candidatas:**"]
            T += [f"- ({r}) {f}" for r, f in s["decisiones"]] or ["- (ninguna detectada)"]
            T += ["", "**Pendientes candidatos:**"] + ([f"- ({r}) {f}" for r, f in s["pendientes"]] or ["- (ninguno detectado)"])
            T += ["", "**Cifras:** " + (", ".join(f"{k} (×{v})" for k, v in s["cifras"]) or "—"),
                  "**Documentos mencionados:** " + (", ".join(k for k, _ in s["documentos"]) or "—"), "",
                  "LECTURA: [pendiente de escribir — qué se decidió, qué quedó abierto, qué cifra hay que defender]", "",
                  "---", "", "## Transcripción", ""]
            for m in c["mensajes"]:
                T.append(f"**{'Usuario' if m['rol']=='usuario' else 'Claude'}:** {m['texto']}\n")
            (tr / nombre).write_text("\n".join(T), encoding="utf-8")
    L += ["", "## Temas más frecuentes (todo el historial)", "",
          ", ".join(f"{w} ({n})" for w, n in temas_g.most_common(25)), "",
          "## Decisiones candidatas (citas literales, atribución usuario/asistente)", "",
          "> Una frase del **asistente** es una propuesta, no una decisión, salvo que el usuario la confirme.", ""]
    L += [f"- [{t}] ({r}) {f}" for t, r, f in todas_dec[:60]] or ["- (ninguna)"]
    L += ["", "## Pendientes candidatos", ""] + ([f"- [{t}] ({r}) {f}" for t, r, f in todas_pen[:60]] or ["- (ninguno)"])
    L += ["", "## Documentos producidos o mencionados en los chats", "",
          "| Documento | Menciones | Ubicación conocida |", "|---|---|---|"]
    L += [f"| {d} | {n} | [a resolver en INVENTARIO_DOCUMENTOS] |" for d, n in todas_docs.most_common(80)] or ["| (ninguno) | | |"]
    (base / "RESUMEN_CHATS_BORRADOR.md").write_text("\n".join(L), encoding="utf-8")
    print(f"CHATS: {len(chats)} chats · método {metodo} → {base}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--export"); g.add_argument("--jsonl")
    ap.add_argument("--proyecto", required=True, help="nombre del proyecto (filtro y etiqueta)")
    ap.add_argument("--trabajo", required=True)
    a = ap.parse_args()
    if a.export:
        brutos = cargar_export(a.export)
        if not brutos: sys.exit("Sin conversaciones en el export: ¿archivo equivocado o enlace caducado (24 h)?")
        chats, metodo = filtrar([normalizar_export(c) for c in brutos], a.proyecto)
        escribir([c for c in chats if c["mensajes"]], metodo, f"export oficial {a.export}", a.trabajo)
    else:
        chats = [json.loads(l) for l in Path(a.jsonl).read_text("utf-8").splitlines() if l.strip()]
        for c in chats: c.setdefault("url", ""); c.setdefault("fecha", ""); c.setdefault("proyecto", a.proyecto)
        escribir(chats, "SESIÓN: parcial por diseño (herramientas de búsqueda de chats)", f"volcado {a.jsonl}", a.trabajo)
