#!/usr/bin/env python3
"""Construye el repositorio de ENTREGA a compradores y, si se pide, lo empuja.

Un solo repositorio privado —`sberriozabal-rgb/zeus-entrega`— para Polar y para
cualquier otro canal que entregue por acceso revocable a repositorio (decisión 12
de catalogo/DECISIONES.md, 16-sep-2026). Contiene los 15 productos del catálogo
suelto tal como los recibe el comprador: los mismos ficheros que el zip de
Gumroad, sin material de fábrica.

Uso:
    python3 venta/publicar_entrega.py                      # construye dist/entrega/
    python3 venta/publicar_entrega.py --push               # además empuja a REPO_ENTREGA
    python3 venta/publicar_entrega.py --push --remote URL  # a otro remoto

Reutiliza de empaquetar_gumroad.py el mapa de productos, la validación previa y
el LEEME, para que zip y repositorio no puedan decir cosas distintas.

Lo que NO hace: crear el repositorio en GitHub. Eso lo hace el titular a mano
(repositorio vacío, privado, sin README); la sesión de fábrica no tiene permiso
para crear repositorios ni para cambiar su configuración.
"""
import os
import shutil
import subprocess
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import empaquetar_gumroad as eg  # noqa: E402

RAIZ = eg.RAIZ
DESTINO = os.path.join(RAIZ, "dist", "entrega")
REPO_ENTREGA = "https://github.com/sberriozabal-rgb/zeus-entrega.git"
RAMA = "main"

# Los 15 productos dados de alta en Gumroad (venta/LISTA-DE-VENTA.md §3), con su precio
# ratificado en catalogo/PRECIOS.md. `cabina-carrera` no entra: es demo-a-sello con otro nombre.
PRODUCTOS_ENTREGA = [
    ("cabina-completa", 249),
    ("cabina-core", 149),
    ("cabina-eventos", 99),
    ("auditoria-de-biblioteca", 49),
    ("postmortem-de-bolo", 49),
    ("set-por-encargo", 49),
    ("peticiones-a-repertorio", 49),
    ("presupuesto-y-contrato-evento", 49),
    ("demo-a-sello", 49),
    ("cobro-cartera-vencida", 79),
    ("pack-contexto", 89),
    ("reporte-inteligencia", 49),
    ("respaldo-proyecto-ia-cl", 49),
    ("universal-compilador-contexto", 49),
    ("productividad-personal-turno", 199),
]


def copiar_skill(ref, carpeta_destino):
    """Copia una skill entera sin los dos ficheros de fábrica ni __pycache__."""
    base = os.path.join(eg.SKILLS, eg.ruta_skill(ref))
    destino = os.path.join(carpeta_destino, os.path.basename(base))
    n = 0
    for raiz, dirs, ficheros in os.walk(base):
        dirs[:] = [d for d in dirs if d not in eg.EXCLUIR_DIRS]
        rel = os.path.relpath(raiz, base)
        os.makedirs(os.path.join(destino, rel) if rel != "." else destino, exist_ok=True)
        for f in sorted(ficheros):
            if f in eg.EXCLUIR:
                continue
            shutil.copy2(os.path.join(raiz, f), os.path.join(destino, rel, f) if rel != "." else os.path.join(destino, f))
            n += 1
    return n


def readme():
    filas = "\n".join(
        f"| `productos/{slug}/` | {eg.PRODUCTOS[slug][0]} | {precio} € | "
        + ", ".join(f"`{os.path.basename(eg.ruta_skill(s))}`" for s in eg.PRODUCTOS[slug][1])
        + " |"
        for slug, precio in PRODUCTOS_ENTREGA
    )
    return f"""# ZEUS — entrega a compradores

**Copyright © 2026 Sergio Berriozábal Serrano. Todos los derechos reservados.**
Ver [`LICENSE`](LICENSE) y el `LICENSE.txt` de cada skill.

Este repositorio es **privado** y es la vía de entrega por **acceso revocable** de las skills
de ZEUS / CABINA. Tienes acceso porque compraste uno o varios productos; el acceso se concede
al comprar y se retira al cesar la relación comercial. La copia que ya descargaste sigue
sujeta a su `LICENSE.txt`.

Generado el {date.today().isoformat()} desde el repositorio de fábrica con
`venta/publicar_entrega.py`. No se edita a mano: cada actualización se regenera entera.

## Qué hay en cada carpeta

Una carpeta por producto en `productos/`, con exactamente lo mismo que recibe quien compra en
Gumroad: la skill o skills completas (`SKILL.md`, `README.md`, `CHANGELOG.md`, `LICENSE.txt`,
`references/`, `assets/`, `scripts/`, `cases/`) y un `LEEME.txt` con la instalación.

| Carpeta | Producto | Precio | Skills |
|---|---|---|---|
{filas}

Los packs repiten las skills de sus piezas sueltas a propósito: cada carpeta de producto es
autosuficiente. Si compraste un pack, usa su carpeta y no las sueltas.

## Instalación

1. Copia cada carpeta de skill entera (la que tiene `SKILL.md` dentro) al directorio de
   skills de tu cliente: en Claude Code, `.claude/skills/` del proyecto o `~/.claude/skills/`
   para tenerla en todos.
2. Abre una sesión nueva. La skill se activa sola cuando la conversación encaja con su
   descripción; también puedes nombrarla.
3. Los scripts de `scripts/` son Python 3 sin dependencias externas. Cada `SKILL.md` dice en
   su sección «Entrada» qué fichero necesita.

## Licencia, en dos líneas

Uso comercial permitido en tu propia actividad, sin límite de ejecuciones. **Prohibida la
redistribución, reventa o publicación**, total o parcial, con o sin cambios.

## Soporte

Responde al correo de compra del canal por el que compraste (Polar, Gumroad u otro) e indica
la versión que aparece en el `CHANGELOG.md` de la skill.

## Nota sobre lo que no está

Cada skill tiene en fábrica una ficha comercial y un `metadata.json` de auditoría. No van en
la entrega: son material de fábrica. Si un `README.md` los cita, no falta nada.
"""


def licencia():
    return """# Titularidad y licencia — repositorio de entrega

**Titular de todos los derechos: Sergio Berriozábal Serrano.**
Copyright © 2026 Sergio Berriozábal Serrano. Todos los derechos reservados.

Este repositorio es privado. El acceso se concede al comprar un producto del catálogo ZEUS /
CABINA y es **revocable** al cesar la relación comercial. Tener acceso no convierte el contenido
en libre: no es software libre ni de código abierto y ninguna licencia OSI le es aplicable.

Cada skill lleva su `LICENSE.txt`, que es el texto que rige. En todas, en términos generales:

- Uso **personal, intransferible y no exclusivo**, incluido el uso comercial en la actividad
  propia del comprador, sin límite de ejecuciones ni de clientes finales atendidos.
- **Prohibida la redistribución**, reventa, cesión, sublicencia o puesta a disposición de
  terceros, total o parcial, con o sin modificaciones, a título oneroso o gratuito. Bifurcar
  este repositorio o compartir su contenido es redistribución.
- Los trabajos derivados para uso interno están permitidos y quedan sujetos a esta misma
  licencia.
- La licencia sobre la copia ya entregada subsiste tras la revocación del acceso, conforme a
  las cláusulas de cada `LICENSE.txt`.

Una skill es texto plano: no hay DRM ni firma. Este catálogo no promete lo contrario.

Las marcas citadas en las skills pertenecen a sus respectivos titulares; su mención es cita de
producto, precio, plazo, política o estudio publicado, con la URL de la fuente, y no implica
afiliación, patrocinio ni respaldo.

`ZEUS`, `FORJA`, `TROQUEL`, `OCTAVA` y `CABINA` son nombres comerciales del titular.
"""


def construir():
    errores = []
    for slug, _ in PRODUCTOS_ENTREGA:
        for ref in eg.PRODUCTOS[slug][1]:
            errores += eg.validar_skill(os.path.join(eg.SKILLS, eg.ruta_skill(ref)))
    if errores:
        sys.exit("NO SE CONSTRUYE. Errores de validación:\n  " + "\n  ".join(errores))
    if os.path.isdir(DESTINO):
        shutil.rmtree(DESTINO)
    os.makedirs(os.path.join(DESTINO, "productos"))
    with open(os.path.join(DESTINO, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme())
    with open(os.path.join(DESTINO, "LICENSE"), "w", encoding="utf-8") as f:
        f.write(licencia())
    with open(os.path.join(DESTINO, ".gitignore"), "w", encoding="utf-8") as f:
        f.write("__pycache__/\n.DS_Store\n")
    total = 0
    for slug, _ in PRODUCTOS_ENTREGA:
        titulo, skills = eg.PRODUCTOS[slug]
        carpeta = os.path.join(DESTINO, "productos", slug)
        os.makedirs(carpeta)
        with open(os.path.join(carpeta, "LEEME.txt"), "w", encoding="utf-8") as f:
            f.write(eg.leeme(titulo, skills).replace(
                "Responde al correo de compra de Gumroad.",
                "Responde al correo de compra del canal por el que compraste."))
        n = sum(copiar_skill(ref, carpeta) for ref in skills)
        total += n
        print(f"productos/{slug}: {n} ficheros")
    print(f"{DESTINO}: {len(PRODUCTOS_ENTREGA)} productos, {total} ficheros de skill")


def empujar(remoto):
    """Un solo commit con el estado entero: el repositorio de entrega no lleva historial de
    fábrica, solo la foto vigente. Se empuja con --force porque se regenera entero."""
    def git(*args):
        return subprocess.run(["git", *args], cwd=DESTINO, check=True, capture_output=True, text=True).stdout
    git("init", "-q", "-b", RAMA)
    git("config", "user.name", "Sergio Berriozábal Serrano")
    git("config", "user.email", "sberriozabal@gmail.com")
    git("add", "-A")
    git("commit", "-q", "-m", f"Entrega del catálogo suelto, {date.today().isoformat()}")
    git("remote", "add", "origin", remoto)
    git("push", "-u", "--force", "origin", RAMA)
    print(f"Empujado a {remoto} ({RAMA})")


if __name__ == "__main__":
    args = sys.argv[1:]
    remoto = REPO_ENTREGA
    if "--remote" in args:
        remoto = args[args.index("--remote") + 1]
    construir()
    if "--push" in args:
        empujar(remoto)
