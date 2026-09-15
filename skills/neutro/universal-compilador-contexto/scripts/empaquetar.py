#!/usr/bin/env python3
"""
empaquetar.py — FASE 4: inventario de documentos y ZIP único.

  python3 empaquetar.py --trabajo <trabajo> --biblioteca <CONTEXTO> \
      [--proyecto /mnt/project] [--outputs /mnt/user-data/outputs] \
      [--fuente <carpeta_original>] --salida CONTEXTO_<fecha>.zip

Hace tres cosas, en este orden:
1. INVENTARIO_DOCUMENTOS.md — listado y ubicación de todo lo producido:
   (a) biblioteca compilada, (b) conocimiento del proyecto Claude, (c) archivos
   producidos en esta sesión, (d) carpeta fuente, (e) documentos mencionados en
   los chats cruzados contra (a)–(d): si el nombre aparece en alguna, se anota la
   ubicación; si no, queda [NO LOCALIZADO] y va a huecos.
2. CHECKSUMS.txt — SHA-256 de cada archivo del paquete.
3. El ZIP único, con la estructura declarada en SKILL.md, y su verificación en frío
   (se extrae en una carpeta temporal y se comprueban los checksums).
"""
import argparse, hashlib, io, json, os, re, tempfile, zipfile
from datetime import datetime
from pathlib import Path


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()


def listar(raiz, etiqueta):
    raiz = Path(raiz)
    if not raiz.exists(): return []
    return [{"nombre": p.name, "ruta": str(p), "ubicacion": etiqueta, "bytes": p.stat().st_size,
             "modificado": datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")}
            for p in sorted(raiz.rglob("*")) if p.is_file() and not p.name.startswith(".")]


def inventario(trabajo, biblioteca, proyecto, outputs, fuente):
    filas = (listar(biblioteca, "Biblioteca compilada (CONTEXTO)") +
             listar(proyecto, "Conocimiento del proyecto Claude") +
             listar(outputs, "Producido en esta sesión") +
             listar(fuente, "Carpeta fuente original"))
    nombres = {}
    for f in filas: nombres.setdefault(f["nombre"].lower(), []).append(f)
    men = []
    rb = Path(trabajo) / "chats" / "RESUMEN_CHATS_BORRADOR.md"
    if rb.exists():
        for l in rb.read_text("utf-8").splitlines():
            m = re.match(r"\| (.+?) \| (\d+) \| \[a resolver", l)
            if m: men.append((m.group(1).strip(), int(m.group(2))))
    L = [f"# INVENTARIO DE DOCUMENTOS — {datetime.now():%Y-%m-%d}", "",
         "Listado y ubicación de todo lo producido y de todo lo que alimentó la biblioteca. "
         "Un documento citado en los chats que no aparece en ninguna ubicación es un hueco, no una omisión silenciosa.", ""]
    for et in ["Biblioteca compilada (CONTEXTO)", "Conocimiento del proyecto Claude",
               "Producido en esta sesión", "Carpeta fuente original"]:
        sub = [f for f in filas if f["ubicacion"] == et]
        L += [f"## {et} — {len(sub)} archivos", "", "| Archivo | Ruta | Modificado | Tamaño |", "|---|---|---|---|"]
        L += [f"| {f['nombre']} | {f['ruta']} | {f['modificado']} | {f['bytes']:,} |" for f in sub] or ["| (vacío) | | | |"]
        L.append("")
    no_loc = []
    L += ["## Documentos mencionados en los chats → ubicación", "", "| Documento | Menciones | Ubicación |", "|---|---|---|"]
    for d, n in men:
        hit = nombres.get(d.lower()) or [v for k, vs in nombres.items() for v in vs if Path(d).stem.lower() in k]
        if hit:
            L.append(f"| {d} | {n} | {hit[0]['ubicacion']}: `{hit[0]['ruta']}` |")
        else:
            no_loc.append(d); L.append(f"| {d} | {n} | [NO LOCALIZADO] |")
    if not men: L.append("| (sin chats digeridos) | | |")
    L += ["", f"## Huecos de ubicación — {len(no_loc)}", ""] + ([f"- {d}" for d in no_loc] or ["- (ninguno)"])
    Path(biblioteca, "INVENTARIO_DOCUMENTOS.md").write_text("\n".join(L), encoding="utf-8")
    return no_loc


def empaquetar(trabajo, biblioteca, salida):
    biblioteca, trabajo, salida = Path(biblioteca), Path(trabajo), Path(salida)
    piezas = [(p, f"CONTEXTO/{p.relative_to(biblioteca)}") for p in biblioteca.rglob("*")
              if p.is_file() and p.name != "CHECKSUMS.txt"]
    for sub, dest in [("chats", "CHATS"), ("extracciones", "EXTRACCIONES_FUENTE")]:
        d = trabajo / sub
        if d.exists():
            piezas += [(p, f"{dest}/{p.relative_to(d)}") for p in d.rglob("*") if p.is_file()]
    for extra in ["CENSO.md", "ILEGIBLES.md", "MANIFEST_EXTRACCION.md"]:
        if (trabajo / extra).exists(): piezas.append((trabajo / extra, f"CENSO/{extra}"))
    ck = "\n".join(f"{sha(p)}  {n}" for p, n in sorted(piezas, key=lambda x: x[1]))
    (biblioteca / "CHECKSUMS.txt").write_text(ck, encoding="utf-8")
    piezas.append((biblioteca / "CHECKSUMS.txt", "CONTEXTO/CHECKSUMS.txt"))
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        for p, n in piezas: z.write(p, n)
    # verificación en frío
    with tempfile.TemporaryDirectory() as td, zipfile.ZipFile(salida) as z:
        z.extractall(td)
        mal = [l.split("  ", 1)[1] for l in ck.splitlines()
               if sha(Path(td, l.split("  ", 1)[1])) != l.split("  ", 1)[0]]
    if mal: raise SystemExit(f"CHECKSUM FALLIDO en {len(mal)} archivos: {mal[:5]} — rehacer el paquete")
    print(f"ZIP: {salida} · {len(piezas)} archivos · {salida.stat().st_size:,} bytes · verificado en frío")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", required=True); ap.add_argument("--biblioteca", required=True)
    ap.add_argument("--proyecto", default="/mnt/project"); ap.add_argument("--outputs", default="/mnt/user-data/outputs")
    ap.add_argument("--fuente", default=None); ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    nl = inventario(a.trabajo, a.biblioteca, a.proyecto, a.outputs, a.fuente)
    if nl: print(f"AVISO: {len(nl)} documentos citados en chats sin ubicación → INVENTARIO_DOCUMENTOS.md")
    empaquetar(a.trabajo, a.biblioteca, a.salida)
