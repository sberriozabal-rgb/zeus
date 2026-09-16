#!/usr/bin/env python3
"""Genera la cover (1280×720) y la thumbnail (600×600) de cada producto de Gumroad.

Uso:
    python3 venta/generar_portadas.py                  # los quince productos
    python3 venta/generar_portadas.py cabina-completa  # uno o varios

Lee nombre, slug, precio y frase de anuncio de la propia hoja de alta
(venta/GUMROAD-ALTA.md), para que la imagen nunca diga un precio distinto
del que se pega en el formulario. Escribe en venta/portadas/<slug>-portada.png
y venta/portadas/<slug>-miniatura.png.

Necesita Pillow (pip install pillow) y las fuentes DejaVu del sistema; si no
están, indica otra ruta en FUENTE_BOLD / FUENTE_REGULAR.
"""
import os
import re
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Falta Pillow: pip install pillow")

RAIZ = os.path.dirname(os.path.abspath(__file__))
HOJA = os.path.join(RAIZ, "GUMROAD-ALTA.md")
DESTINO = os.path.join(RAIZ, "portadas")

FUENTE_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FUENTE_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

FONDO = (17, 20, 23)
TEXTO = (245, 243, 238)
TEXTO_SUAVE = (170, 174, 180)
LINEAS = {
    "CABINA · DJ": (242, 177, 52),
    "HOSTELERÍA": (224, 100, 60),
    "B2B · LÍNEA NEUTRA": (63, 183, 166),
}
PIE = "skills para Claude · estándar abierto Agent Skills"
COPY = "© 2026 Sergio Berriozábal Serrano"

CABINA = {
    "cabina-completa", "cabina-core", "cabina-eventos", "auditoria-de-biblioteca",
    "postmortem-de-bolo", "set-por-encargo", "peticiones-a-repertorio",
    "presupuesto-y-contrato-evento", "demo-a-sello",
}
HOSTELERIA = {"productividad-personal-turno"}


def linea_de(slug):
    if slug in CABINA:
        return "CABINA · DJ"
    if slug in HOSTELERIA:
        return "HOSTELERÍA"
    return "B2B · LÍNEA NEUTRA"


def leer_productos():
    """Devuelve {slug: {nombre, precio, resumen}} leyendo las tablas de campos de la hoja."""
    productos, actual = {}, {}
    for linea in open(HOJA, encoding="utf-8"):
        m = re.match(r"\| \*\*(Name|URL|Price|Summary)\*\*[^|]*\| (.+?) \|\s*$", linea)
        if not m:
            continue
        campo, valor = m.groups()
        if campo == "Name":
            actual = {"nombre": valor.strip()}
        elif campo == "URL":
            actual["slug"] = valor.strip("` ")
        elif campo == "Price":
            actual["precio"] = re.match(r"\d+", valor.strip()).group(0)
        elif campo == "Summary":
            actual["resumen"] = valor.strip()
            productos[actual["slug"]] = actual
    return productos


def fuente(ruta, tam):
    return ImageFont.truetype(ruta, tam)


def envolver(draw, texto, f, ancho):
    lineas, actual = [], ""
    for palabra in texto.split():
        prueba = (actual + " " + palabra).strip()
        if draw.textlength(prueba, font=f) <= ancho:
            actual = prueba
        else:
            lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas


def ajustar(draw, texto, ruta, tam_max, tam_min, ancho, max_lineas):
    """Baja el cuerpo hasta que el texto cabe en max_lineas."""
    for tam in range(tam_max, tam_min - 1, -2):
        f = fuente(ruta, tam)
        lineas = envolver(draw, texto, f, ancho)
        if len(lineas) <= max_lineas:
            return f, lineas
    f = fuente(ruta, tam_min)
    return f, envolver(draw, texto, f, ancho)[:max_lineas]


def titulo_corto(nombre):
    """'CABINA CORE — 3 skills de cabina para DJ' -> ('CABINA CORE', '3 skills de cabina para DJ')."""
    if " — " in nombre:
        a, b = nombre.split(" — ", 1)
        return a.strip(), b.strip()
    return nombre, ""


def dibujar(prod, ancho, alto, ruta):
    slug = prod["slug"]
    linea = linea_de(slug)
    acento = LINEAS[linea]
    img = Image.new("RGB", (ancho, alto), FONDO)
    d = ImageDraw.Draw(img)
    margen = int(ancho * 0.07)
    cuadrado = ancho == alto
    util = ancho - 2 * margen

    # Banda de color a la izquierda
    d.rectangle([0, 0, int(ancho * 0.012), alto], fill=acento)

    # Línea de producto
    f_linea = fuente(FUENTE_BOLD, 22 if not cuadrado else 20)
    y = margen
    d.text((margen, y), linea, font=f_linea, fill=acento)
    y += f_linea.size + int(alto * 0.035)

    # Título y subtítulo
    titulo, sub = titulo_corto(prod["nombre"])
    f_tit, l_tit = ajustar(d, titulo, FUENTE_BOLD, 84 if not cuadrado else 56, 32, util, 2 if not cuadrado else 3)
    for l in l_tit:
        d.text((margen, y), l, font=f_tit, fill=TEXTO)
        y += int(f_tit.size * 1.12)
    if sub:
        f_sub = fuente(FUENTE_REGULAR, 30 if not cuadrado else 22)
        d.text((margen, y + 4), sub, font=f_sub, fill=TEXTO_SUAVE)
        y += f_sub.size + int(alto * 0.03)
    y += int(alto * 0.03)

    # Frase de anuncio
    f_res, l_res = ajustar(d, prod["resumen"], FUENTE_REGULAR, 34 if not cuadrado else 24, 20, util, 4 if not cuadrado else 5)
    for l in l_res:
        d.text((margen, y), l, font=f_res, fill=TEXTO)
        y += int(f_res.size * 1.35)

    # Precio, abajo a la izquierda
    f_precio = fuente(FUENTE_BOLD, 72 if not cuadrado else 48)
    precio = f"{prod['precio']} €"
    y_precio = alto - margen - f_precio.size - (34 if not cuadrado else 30)
    d.text((margen, y_precio), precio, font=f_precio, fill=acento)
    f_pago = fuente(FUENTE_REGULAR, 20 if not cuadrado else 16)
    d.text((margen + d.textlength(precio, font=f_precio) + 18, y_precio + f_precio.size - f_pago.size - 10),
           "pago único", font=f_pago, fill=TEXTO_SUAVE)

    # Pie
    f_pie = fuente(FUENTE_REGULAR, 18 if not cuadrado else 14)
    y_pie = alto - margen + 4
    if cuadrado:
        y_pie -= f_pie.size + 10  # dos líneas de pie en la miniatura
    d.text((margen, y_pie), PIE, font=f_pie, fill=TEXTO_SUAVE)
    ancho_copy = d.textlength(COPY, font=f_pie)
    if cuadrado:
        d.text((margen, y_pie + f_pie.size + 6), COPY, font=f_pie, fill=TEXTO_SUAVE)
    else:
        d.text((ancho - margen - ancho_copy, y_pie), COPY, font=f_pie, fill=TEXTO_SUAVE)

    img.save(ruta, optimize=True)


def main(pedidos):
    productos = leer_productos()
    if not productos:
        sys.exit(f"No se ha leído ningún producto de {HOJA}")
    malos = [p for p in pedidos if p not in productos]
    if malos:
        sys.exit(f"Producto desconocido: {', '.join(malos)}. Válidos: {', '.join(productos)}")
    os.makedirs(DESTINO, exist_ok=True)
    for slug in pedidos or productos:
        prod = productos[slug]
        portada = os.path.join(DESTINO, f"{slug}-portada.png")
        miniatura = os.path.join(DESTINO, f"{slug}-miniatura.png")
        dibujar(prod, 1280, 720, portada)
        dibujar(prod, 600, 600, miniatura)
        print(f"{slug}: {prod['precio']} € · portada y miniatura")


if __name__ == "__main__":
    main(sys.argv[1:])
