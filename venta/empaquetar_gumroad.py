#!/usr/bin/env python3
"""Empaqueta los productos de catálogo (Motor A) para subirlos a Gumroad.

Uso:
    python3 venta/empaquetar_gumroad.py                 # todos los productos
    python3 venta/empaquetar_gumroad.py cabina-completa cobro-cartera-vencida

Antes de escribir nada valida cada skill (frontmatter YAML con name, description
y license; LICENSE.txt presente) y se niega a empaquetar si algo falla.

Genera un .zip por producto en dist/ (ignorado por git). Cada zip lleva las
skills completas —SKILL.md, references/, assets/, scripts/, cases/, README,
CHANGELOG y LICENSE.txt— más un LEEME.txt con la instalación y la licencia.

Se EXCLUYEN a propósito dos ficheros internos de cada skill:
  - ANEXO-A-ficha-comercial.md  (razón del precio, quién NO es comprador, gates)
  - metadata.json               (auditoría, gates, carencias declaradas)
Son material de fábrica, no del comprador. El mismo criterio se aplicó al
marketplace público del 15-sep-2026.
"""
import os
import sys
import zipfile
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(RAIZ, "skills")
DIST = os.path.join(RAIZ, "dist")
EXCLUIR = {"ANEXO-A-ficha-comercial.md", "metadata.json"}
EXCLUIR_DIRS = {"__pycache__"}

CABINA = {
    "auditoria-de-biblioteca": "cabina/auditoria-de-biblioteca",
    "postmortem-de-bolo": "cabina/postmortem-de-bolo",
    "set-por-encargo": "cabina/set-por-encargo",
    "peticiones-a-repertorio": "cabina/peticiones-a-repertorio",
    "presupuesto-y-contrato-evento": "cabina/presupuesto-y-contrato-evento",
    "demo-a-sello": "cabina/demo-a-sello",
}

# nombre del producto -> (título, lista de skills)
PRODUCTOS = {
    "cabina-core": ("CABINA CORE", ["auditoria-de-biblioteca", "postmortem-de-bolo", "set-por-encargo"]),
    "cabina-eventos": ("CABINA EVENTOS", ["peticiones-a-repertorio", "presupuesto-y-contrato-evento"]),
    "cabina-carrera": ("CABINA CARRERA", ["demo-a-sello"]),
    "cabina-completa": ("CABINA COMPLETA", list(CABINA)),
    "cobro-cartera-vencida": ("Plan de cobro de cartera vencida", ["neutro/cobro-cartera-vencida"]),
    "reporte-inteligencia": ("Reporte semanal de inteligencia competitiva", ["neutro/reporte-inteligencia"]),
    "respaldo-proyecto-ia-cl": ("Respaldo cifrado de proyecto de IA", ["neutro/respaldo-proyecto-ia-cl"]),
    "universal-compilador-contexto": ("Compilador de contexto de proyecto", ["neutro/universal-compilador-contexto"]),
    "pack-contexto": ("PACK CONTEXTO", ["neutro/respaldo-proyecto-ia-cl", "neutro/universal-compilador-contexto"]),
}
for k in CABINA:
    PRODUCTOS[k] = (k, [CABINA[k]])


def ruta_skill(ref):
    return ref if "/" in ref else CABINA[ref]


def leeme(titulo, skills):
    lineas = [
        f"{titulo} — skills para Claude (estándar abierto Agent Skills)",
        f"Empaquetado el {date.today().isoformat()}. Copyright 2026 Sergio Berriozábal Serrano.",
        "",
        "CONTENIDO",
    ]
    for s in skills:
        lineas.append(f"  - {os.path.basename(ruta_skill(s))}/")
    lineas += [
        "",
        "INSTALACIÓN",
        "  1. Descomprime el zip.",
        "  2. Copia cada carpeta de skill entera (con su SKILL.md dentro) al",
        "     directorio de skills de tu cliente: en Claude Code, .claude/skills/",
        "     del proyecto o ~/.claude/skills/ para tenerla en todos.",
        "  3. Abre una sesión nueva. La skill se activa sola cuando la",
        "     conversación encaja con su descripción; también puedes nombrarla.",
        "",
        "REQUISITOS",
        "  Los scripts de scripts/ son Python 3 sin dependencias externas.",
        "  Cada SKILL.md dice en su sección «Entrada» qué fichero necesita.",
        "",
        "LICENCIA",
        "  Uso comercial permitido en tu actividad. Prohibida la redistribución,",
        "  reventa o publicación. Texto completo en LICENSE.txt de cada skill.",
        "",
        "SOPORTE",
        "  Responde al correo de compra de Gumroad. Indica versión (CHANGELOG.md).",
    ]
    return "\n".join(lineas) + "\n"


def validar_skill(base):
    """Comprobaciones mínimas antes de empaquetar: la doctrina manda ejecutar el
    validador antes de empaquetar, sin excepción. Devuelve una lista de errores."""
    import re
    errores = []
    skill_md = os.path.join(base, "SKILL.md")
    if not os.path.exists(skill_md):
        return [f"{base}: falta SKILL.md"]
    if not os.path.exists(os.path.join(base, "LICENSE.txt")):
        errores.append(f"{base}: falta LICENSE.txt")
    texto = open(skill_md, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return errores + [f"{base}: SKILL.md sin frontmatter"]
    fm = m.group(1)
    try:
        import yaml  # opcional
        datos = yaml.safe_load(fm)
        if not isinstance(datos, dict):
            errores.append(f"{base}: frontmatter no es un mapa YAML")
        else:
            for campo in ("name", "description", "license"):
                if not datos.get(campo):
                    errores.append(f"{base}: frontmatter sin `{campo}`")
            if datos.get("name") and datos["name"] != os.path.basename(base):
                errores.append(f"{base}: `name` ({datos['name']}) no coincide con la carpeta")
    except ImportError:
        # Sin PyYAML: comprobación de superficie. Instala pyyaml para la completa.
        for campo in ("name:", "description:", "license:"):
            if not re.search(rf"^{campo}", fm, re.M):
                errores.append(f"{base}: frontmatter sin `{campo[:-1]}` (comprobación sin PyYAML)")
    return errores


def empaquetar(nombre):
    titulo, skills = PRODUCTOS[nombre]
    errores = []
    for ref in skills:
        errores += validar_skill(os.path.join(SKILLS, ruta_skill(ref)))
    if errores:
        sys.exit("NO SE EMPAQUETA. Errores de validación:\n  " + "\n  ".join(errores))
    os.makedirs(DIST, exist_ok=True)
    destino = os.path.join(DIST, f"{nombre}.zip")
    n = 0
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{nombre}/LEEME.txt", leeme(titulo, skills))
        for ref in skills:
            base = os.path.join(SKILLS, ruta_skill(ref))
            carpeta = os.path.basename(base)
            for raiz, dirs, ficheros in os.walk(base):
                dirs[:] = [d for d in dirs if d not in EXCLUIR_DIRS]
                for f in sorted(ficheros):
                    if f in EXCLUIR:
                        continue
                    abs_f = os.path.join(raiz, f)
                    rel = os.path.relpath(abs_f, base)
                    z.write(abs_f, f"{nombre}/{carpeta}/{rel}")
                    n += 1
    print(f"{destino}: {n} ficheros, {os.path.getsize(destino)//1024} KB")
    return destino


if __name__ == "__main__":
    pedidos = sys.argv[1:] or list(PRODUCTOS)
    malos = [p for p in pedidos if p not in PRODUCTOS]
    if malos:
        sys.exit(f"Producto desconocido: {', '.join(malos)}. Válidos: {', '.join(PRODUCTOS)}")
    for p in pedidos:
        empaquetar(p)
