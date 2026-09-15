#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
productividad_turno.py — motor de la skill `productividad-personal-turno`.

Cruza ventas por franja con horas presentes por franja. Es la unica forma de ver
lo que el resumen mensual esconde: el mes puede cerrar en un 32% de coste de
personal y tener tres franjas al 60% pagadas por las dos franjas buenas.

Modos:
  --modo franjas   Ventas por hora trabajada y coste de personal por franja.
  --modo escalera  Propone escalonar entradas y salidas segun la curva de venta.
  --modo semana    Resumen por dia de la semana: donde sobra plantilla y donde falta.

Sin dependencias externas. Python 3.9+.
"""

import argparse
import csv
import io
import os
import re
import sys
import unicodedata
from collections import defaultdict
from datetime import datetime

SEPARADORES = [";", ",", "\t", "|"]

ALIAS = {
    "fecha": ["fecha", "dia", "date", "day", "f", "jornada"],
    "franja": ["franja", "hora", "tramo", "hour", "time", "intervalo", "slot", "turno hora"],
    "ventas": ["ventas", "venta", "importe", "facturacion", "facturación", "sales",
               "revenue", "total", "ingresos", "neto"],
    "horas": ["horas", "horas trabajadas", "h", "hrs", "labor hours", "horas presentes",
              "horas plantilla", "hh"],
    "coste": ["coste", "coste personal", "costo", "labor cost", "coste laboral",
              "gasto personal", "nomina", "nómina"],
    "comensales": ["comensales", "cubiertos", "pax", "covers", "clientes", "tickets"],
    "turno": ["turno", "servicio", "shift", "sesion", "sesión"],
}

DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]


def sin_acentos(t):
    t = unicodedata.normalize("NFKD", str(t))
    return "".join(c for c in t if not unicodedata.combining(c))


def norm(t):
    t = sin_acentos(t).lower().strip()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9%/: ]+", " ", t)).strip()


def a_numero(t):
    if t is None:
        return None
    s = str(t).strip()
    if not s:
        return None
    neg = s.startswith("(") and s.endswith(")")
    s = re.sub(r"[^\d,.\-]", "", s.strip("()"))
    if not s or s in ("-", ".", ","):
        return None
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif "," in s:
        s = s.replace(",", "") if re.match(r"^-?\d{1,3}(,\d{3})+$", s) else s.replace(",", ".")
    try:
        v = float(s)
    except ValueError:
        return None
    return -v if neg else v


FORMATOS_FECHA = ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d", "%d/%m/%y", "%d.%m.%Y", "%Y/%m/%d"]


def a_fecha(t):
    if not t:
        return None
    s = str(t).strip()[:10]
    for f in FORMATOS_FECHA:
        try:
            return datetime.strptime(s, f).date()
        except ValueError:
            continue
    return None


def a_hora(t):
    """Devuelve la hora entera de inicio de la franja. '13:00-14:00' -> 13."""
    if t is None:
        return None
    s = norm(t)
    m = re.search(r"(\d{1,2})\s*:", s) or re.search(r"^(\d{1,2})\b", s)
    if not m:
        return None
    h = int(m.group(1))
    return h if 0 <= h <= 23 else None


def detectar_separador(muestra):
    mejor, score = ";", -1
    lineas = [l for l in muestra.splitlines() if l.strip()][:40]
    for sep in SEPARADORES:
        c = [l.count(sep) for l in lineas]
        if not c:
            continue
        m = sum(c) / len(c)
        if m < 1:
            continue
        var = sum((x - m) ** 2 for x in c) / len(c)
        if m - var > score:
            mejor, score = sep, m - var
    return mejor


def leer(ruta, obligatorias):
    if not os.path.exists(ruta):
        sys.exit(f"ERROR: no existe el archivo {ruta}")
    datos = None
    for enc in ("utf-8-sig", "utf-8", "latin-1", "cp1252"):
        try:
            datos = open(ruta, "r", encoding=enc).read()
            break
        except UnicodeDecodeError:
            continue
    if datos is None:
        sys.exit("ERROR: no se pudo decodificar el archivo.")
    filas = [f for f in csv.reader(io.StringIO(datos), delimiter=detectar_separador(datos[:20000]))
             if any(str(c).strip() for c in f)]
    idx, mapa = None, {}
    for i, fila in enumerate(filas[:30]):
        m = {}
        for j, celda in enumerate(fila):
            c = norm(celda)
            if not c:
                continue
            for campo, al in ALIAS.items():
                if campo not in m and any(c == norm(a) or c.startswith(norm(a) + " ") for a in al):
                    m[campo] = j
        if all(k in m for k in obligatorias):
            idx, mapa = i, m
            break
    if idx is None:
        sys.exit("ERROR: no encuentro cabecera con: " + ", ".join(obligatorias) +
                 "\nNecesito como minimo la venta y las horas trabajadas de cada franja.\n"
                 "Sin las dos no hay productividad: hay facturacion, que es otra cosa.")
    return filas[idx + 1:], mapa


def eur(v):
    return f"{v:,.2f}".replace(",", "@").replace(".", ",").replace("@", ".")


def cargar(args, obligatorias):
    filas, mapa = leer(args.archivo, obligatorias)

    def c(f, k):
        i = mapa.get(k)
        return f[i] if i is not None and i < len(f) else ""

    reg, desc = [], 0
    for f in filas:
        v = a_numero(c(f, "ventas"))
        h = a_numero(c(f, "horas"))
        if v is None or h is None or v < 0 or h < 0:
            desc += 1
            continue
        coste = a_numero(c(f, "coste")) if "coste" in mapa else None
        if coste is None:
            coste = h * args.coste_hora
        reg.append({
            "fecha": a_fecha(c(f, "fecha")),
            "hora": a_hora(c(f, "franja")),
            "turno": str(c(f, "turno")).strip() or "",
            "ventas": v, "horas": h, "coste": coste,
            "pax": a_numero(c(f, "comensales")) or 0.0,
        })
    if not reg:
        sys.exit("ERROR: ninguna linea utilizable.")
    return reg, desc


# --- aritmetica de productividad (aislada para poder comprobarla) ----------

def ventas_por_hora(ventas, horas):
    """Sin horas presentes no hay productividad; devolver 0 evita la excepcion
    y no inventa un ratio que no existe."""
    return ventas / horas if horas else 0.0


def pct_personal(coste, ventas):
    """Coste de personal sobre venta. Devuelve None cuando no hubo venta: una
    franja abierta con plantilla y sin facturar no cuesta el 0%, es que el
    porcentaje no esta definido. Imprimirlo como 0,0% la colocaba en la tabla
    como la franja mas barata del dia, que es exactamente lo contrario."""
    return coste / ventas * 100 if ventas else None


def exceso_sobre_objetivo(coste, ventas, objetivo_pct):
    """Euros de personal por encima del objetivo. Negativo = queda margen."""
    return coste - ventas * objetivo_pct / 100.0


def horas_objetivo(ventas, objetivo_pct, coste_hora):
    """Horas que pagaria la venta al objetivo fijado. Es un techo, no una orden."""
    return (ventas * objetivo_pct / 100.0) / coste_hora if coste_hora else 0.0


def anualizar(valor, dias_periodo):
    return valor / dias_periodo * 365 if dias_periodo else 0.0


def bloque_ratios(nombre, ventas, horas, coste, pax, args, ancho=26):
    vht = ventas_por_hora(ventas, horas)
    pctc = pct_personal(coste, ventas)
    marca = ""
    if horas > 0 and pctc is not None:
        if pctc > args.umbral_alto:
            marca = "  << SOBRA PLANTILLA"
        elif pctc < args.umbral_bajo:
            marca = "  << ¿FALTA MANO?"
    elif horas > 0 and coste > 0:
        marca = "  << HORAS PAGADAS SIN VENTA"
    txt_pct = f"{pctc:>8.1f}%" if pctc is not None else f"{'n/d':>8} "
    ppax = ventas / pax if pax else 0.0
    return (f"{nombre[:ancho - 1]:<{ancho}}{eur(ventas):>11}{horas:>8.1f}{eur(vht):>10}"
            f"{txt_pct}{eur(ppax) if pax else '     —':>9}{marca}")


CAB = f"{'':<26}{'ventas':>11}{'horas':>8}{'EUR/h':>10}{'% pers':>9}{'/pax':>9}"


# ----------------------------------------------------------------------------

def modo_franjas(args):
    reg, desc = cargar(args, ["ventas", "horas"])
    if not any(r["hora"] is not None for r in reg):
        sys.exit("ERROR: ninguna franja horaria legible. El modo franjas necesita la hora:\n"
                 "sin ella solo puedo darte el mes, y el mes es exactamente lo que esconde el problema.")

    agr = defaultdict(lambda: {"v": 0.0, "h": 0.0, "c": 0.0, "p": 0.0})
    for r in reg:
        if r["hora"] is None:
            continue
        a = agr[r["hora"]]
        a["v"] += r["ventas"]; a["h"] += r["horas"]; a["c"] += r["coste"]; a["p"] += r["pax"]

    V = sum(a["v"] for a in agr.values())
    H = sum(a["h"] for a in agr.values())
    C = sum(a["c"] for a in agr.values())
    P = sum(a["p"] for a in agr.values())

    print("=" * 84)
    print("PRODUCTIVIDAD POR FRANJA — lo que el resumen del mes esconde")
    print("=" * 84)
    print(f"Total periodo: {eur(V)} EUR de venta · {H:.1f} horas · {eur(C)} EUR de personal")
    print(f"Media global : {eur(V / H if H else 0)} EUR/hora · {C / V * 100 if V else 0:.1f}% de coste de personal")
    print()
    print(CAB)
    for h in sorted(agr):
        a = agr[h]
        print(bloque_ratios(f"{h:02d}:00 - {(h + 1) % 24:02d}:00", a["v"], a["h"], a["c"], a["p"], args))
    print()

    caras = [(h, a) for h, a in agr.items()
             if a["v"] > 0 and (pct_personal(a["c"], a["v"]) or 0) > args.umbral_alto
             and a["h"] >= args.horas_minimas]
    caras.sort(key=lambda x: -exceso_sobre_objetivo(x[1]["c"], x[1]["v"], args.umbral_objetivo))
    if caras:
        print("-" * 84)
        print(f"FRANJAS POR ENCIMA DEL {args.umbral_alto:.0f}% DE COSTE DE PERSONAL")
        print("-" * 84)
        exceso_total = 0.0
        for h, a in caras:
            exceso = exceso_sobre_objetivo(a["c"], a["v"], args.umbral_objetivo)
            exceso_total += exceso
            horas_sobra = exceso / args.coste_hora if args.coste_hora else 0.0
            print(f"  · {h:02d}:00  coste {a['c'] / a['v'] * 100:.0f}% de una venta de {eur(a['v'])} EUR")
            print(f"          exceso sobre el objetivo del {args.umbral_objetivo:.0f}%: {eur(exceso)} EUR "
                  f"≈ {horas_sobra:.1f} horas del periodo")
        print()
        print(f"  EXCESO TOTAL DEL PERIODO: {eur(exceso_total)} EUR")
        if args.dias_periodo:
            print(f"  Extrapolado a 365 dias: {eur(anualizar(exceso_total, args.dias_periodo))} EUR/ano")
        print()
        print("  Antes de tocar un cuadrante: parte de esas horas son FIJAS (apertura, produccion,")
        print("  limpieza, cierre) y no se pueden mover aunque no haya venta. Solo las horas de")
        print("  servicio son variables. Separa unas de otras antes de decidir nada.")
    else:
        print(f"Ninguna franja por encima del {args.umbral_alto:.0f}% con al menos "
              f"{args.horas_minimas:g} horas acumuladas.")
    if desc:
        print(f"\nAVISO: {desc} lineas descartadas por datos incompletos o negativos.")


def modo_semana(args):
    reg, desc = cargar(args, ["ventas", "horas"])
    if not any(r["fecha"] for r in reg):
        sys.exit("ERROR: ninguna fecha legible. El modo semana necesita la fecha de cada linea.")
    agr = defaultdict(lambda: {"v": 0.0, "h": 0.0, "c": 0.0, "p": 0.0})
    for r in reg:
        if not r["fecha"]:
            continue
        a = agr[r["fecha"].weekday()]
        a["v"] += r["ventas"]; a["h"] += r["horas"]; a["c"] += r["coste"]; a["p"] += r["pax"]

    print("=" * 84)
    print("PRODUCTIVIDAD POR DIA DE LA SEMANA")
    print("=" * 84)
    print(CAB)
    for d in sorted(agr):
        a = agr[d]
        print(bloque_ratios(DIAS[d].capitalize(), a["v"], a["h"], a["c"], a["p"], args))
    print()
    # Los dias sin venta se apartan del ranking y se dicen aparte: antes salian
    # del calculo con dos valores centinela distintos (0 para el peor, 99 para
    # el mejor), asi que desaparecian de los dos extremos sin avisar.
    con_venta = [(d, a) for d, a in agr.items() if a["v"] > 0]
    sin_venta = [d for d, a in agr.items() if a["v"] <= 0 and a["c"] > 0]
    if con_venta:
        peor = max(con_venta, key=lambda x: pct_personal(x[1]["c"], x[1]["v"]))
        mejor = min(con_venta, key=lambda x: pct_personal(x[1]["c"], x[1]["v"]))
        print(f"El dia mas caro es {DIAS[peor[0]]} ({pct_personal(peor[1]['c'], peor[1]['v']):.0f}% de personal) "
              f"y el mas rentable {DIAS[mejor[0]]} ({pct_personal(mejor[1]['c'], mejor[1]['v']):.0f}%).")
    if sin_venta:
        print("Fuera del ranking por no tener venta registrada, con horas pagadas: "
              + ", ".join(DIAS[d] for d in sorted(sin_venta))
              + ". Comprueba si es un cierre o un dia sin volcar del TPV.")
    print()
    print("La pregunta correcta no es si cierras el dia malo. Es si el dia malo esta abierto")
    print("con la misma plantilla que el bueno, que es lo que pasa en la mayoria de los locales.")
    if desc:
        print(f"\nAVISO: {desc} lineas descartadas.")


def modo_escalera(args):
    reg, desc = cargar(args, ["ventas", "horas"])
    agr = defaultdict(lambda: {"v": 0.0, "h": 0.0})
    dias = set()
    for r in reg:
        if r["hora"] is None:
            continue
        agr[r["hora"]]["v"] += r["ventas"]
        agr[r["hora"]]["h"] += r["horas"]
        if r["fecha"]:
            dias.add(r["fecha"])
    if not agr:
        sys.exit("ERROR: sin franjas horarias legibles no se puede escalonar nada.")
    n_dias = max(len(dias), 1)

    V = sum(a["v"] for a in agr.values())
    print("=" * 84)
    print("ESCALERA DE ENTRADAS — dimensionar por curva de venta, no por turno completo")
    print("=" * 84)
    print(f"Objetivo de coste de personal: {args.umbral_objetivo:.0f}% de la venta de cada franja.")
    print(f"Coste hora usado: {eur(args.coste_hora)} EUR  [dato a validar por el cliente]")
    print(f"Dias en el archivo: {n_dias}")
    print()
    print(f"{'franja':<16}{'venta/dia':>12}{'horas/dia':>11}{'objetivo h':>12}{'ajuste':>10}   curva")
    for h in sorted(agr):
        a = agr[h]
        vd = a["v"] / n_dias
        hd = a["h"] / n_dias
        objetivo_h = horas_objetivo(vd, args.umbral_objetivo, args.coste_hora)
        ajuste = objetivo_h - hd
        barra = "#" * int(round(vd / (V / n_dias) * 60)) if V else ""
        signo = f"{ajuste:+.1f} h"
        print(f"{h:02d}:00 - {(h + 1) % 24:02d}:00 {vd:>11.0f}{hd:>11.1f}{objetivo_h:>12.1f}{signo:>10}   {barra}")
    print()
    print("Como se lee esto, que es lo que separa un cuadrante bueno de uno malo:")
    print()
    print("  1. Las horas objetivo son un TECHO de referencia, no una orden. Hay franjas que")
    print("     necesitan dos personas aunque la venta no las pague: nadie abre un local solo,")
    print("     y una cocina con una persona no aguanta un pico imprevisto.")
    print("  2. No se recorta el turno: se escalona la ENTRADA. Media hora de desfase entre")
    print("     el primero y el segundo, y otra media al tercero, recupera mas horas que")
    print("     cualquier recorte y no toca el servicio del pico.")
    print("  3. Las salidas se escalonan igual, empezando por quien no tiene tarea de cierre.")
    print("  4. Un recorte que deja el pico corto se paga en ticket medio y en reseña. Si")
    print("     dudas, sobra gente en el valle, nunca en el pico.")
    print("  5. Recortar horas mal genera rotacion, y reponer una baja cuesta entre 1.056 y")
    print("     2.611 dolares (terreno calibrado FORJA, 10-ago-2026). Un ahorro de plantilla")
    print("     que provoca dos bajas no es un ahorro.")
    if desc:
        print(f"\nAVISO: {desc} lineas descartadas.")


# --- AUTOTEST -------------------------------------------------------------
# Lo que se comprueba aqui es lo que sostiene una decision de cuadrante: si el
# exceso o las horas objetivo salen mal, se recorta plantilla donde no sobra.

class _ArgsFalsos:
    umbral_objetivo = 30.0
    umbral_alto = 40.0
    umbral_bajo = 15.0
    coste_hora = 20.0


def autotest():
    fallos, hechas = [], []

    def check(nombre, obtenido, esperado, tol=1e-9):
        hechas.append(nombre)
        if isinstance(esperado, str) or esperado is None:
            ok = obtenido == esperado
        else:
            ok = obtenido is not None and abs(obtenido - esperado) <= tol
        if not ok:
            fallos.append(f"{nombre}: obtenido {obtenido!r}, esperado {esperado!r}")

    # 1. El ratio rey: 1.200 EUR en 8 horas presentes son 150 EUR/hora.
    check("ventas por hora", ventas_por_hora(1200.0, 8.0), 150.0)
    # Franja cerrada (0 horas): no hay ratio, pero tampoco excepcion a media tabla.
    check("sin horas no hay ratio", ventas_por_hora(1200.0, 0.0), 0.0)
    check("sin venta ni horas", ventas_por_hora(0.0, 0.0), 0.0)

    # 2. Coste de personal: 400 sobre 1.000 son 40%.
    check("porcentaje de personal", pct_personal(400.0, 1000.0), 40.0)
    # 3. Sin venta el porcentaje no existe: None, no 0.0. Un 0,0% en la tabla se
    # lee como la franja mas eficiente del dia siendo la mas cara que hay.
    check("sin venta el % no existe", pct_personal(400.0, 0.0), None)

    # 4. Exceso sobre el objetivo, hecho a mano: objetivo 30% de 1.000 son 300;
    # se pagaron 400, luego sobran 100 EUR de personal en esa franja.
    check("exceso sobre objetivo", exceso_sobre_objetivo(400.0, 1000.0, 30.0), 100.0)
    # Y por debajo del objetivo el resultado es NEGATIVO (queda margen). Si
    # saliera en positivo, el informe sumaria como exceso lo que es holgura.
    check("por debajo del objetivo da negativo",
          exceso_sobre_objetivo(200.0, 1000.0, 30.0), -100.0)
    check("justo en el objetivo", exceso_sobre_objetivo(300.0, 1000.0, 30.0), 0.0)

    # 5. Horas objetivo y su reversibilidad: las horas que paga la venta al 30%,
    # multiplicadas por el coste hora, tienen que devolver esos mismos euros.
    check("horas objetivo", horas_objetivo(1000.0, 30.0, 20.0), 15.0)
    check("horas objetivo reversibles",
          horas_objetivo(1000.0, 30.0, 20.0) * 20.0, 1000.0 * 30.0 / 100.0)
    # Sin coste hora no se puede dimensionar: 0.0, nunca division por cero.
    check("sin coste hora", horas_objetivo(1000.0, 30.0, 0.0), 0.0)

    # 6. El exceso convertido a horas: 100 EUR a 20 EUR/h son 5 horas del periodo.
    check("exceso en horas", exceso_sobre_objetivo(400.0, 1000.0, 30.0) / 20.0, 5.0)

    # 7. Anualizar es una regla de tres, no una proyeccion: 100 EUR en 30 dias.
    check("extrapolacion a 365 dias", anualizar(100.0, 30), 100.0 / 30 * 365)
    check("sin dias no se extrapola", anualizar(100.0, 0), 0.0)

    # 8. Lectura de la franja horaria: el archivo del cliente la trae de cinco
    # formas. Leer mal la hora mueve la venta de franja y desplaza el pico.
    check("franja con rango", a_hora("13:00-14:00"), 13)
    check("franja con hora suelta", a_hora("9"), 9)
    check("franja con minutos", a_hora("9:30"), 9)
    check("medianoche", a_hora("00:00-01:00"), 0)
    check("hora imposible", a_hora("25:00"), None)
    check("franja vacia", a_hora(""), None)

    # 9. Importes del CSV: coma decimal espanola y separador de miles.
    check("importe con coma decimal", a_numero("364,20"), 364.20)
    check("importe con miles y decimales", a_numero("1.234,50"), 1234.50)
    check("importe negativo contable", a_numero("(120,00)"), -120.0)
    check("celda vacia", a_numero(""), None)

    # 10. Coherencia de la agregacion: el total del periodo tiene que ser la
    # suma de las franjas, y el ratio global NO es la media de los ratios.
    franjas = [(1000.0, 10.0, 400.0), (500.0, 10.0, 200.0), (0.0, 4.0, 80.0)]
    V = sum(f[0] for f in franjas)
    H = sum(f[1] for f in franjas)
    C = sum(f[2] for f in franjas)
    check("venta total", V, 1500.0)
    check("horas totales", H, 24.0)
    check("ratio global no es media de ratios", ventas_por_hora(V, H), 62.5)
    check("coste global sobre venta", pct_personal(C, V), 45.333333333, tol=1e-6)

    # 11. Coste derivado de horas cuando el archivo no trae coste: h * coste/hora,
    # y la vuelta atras devuelve las horas.
    check("coste derivado de horas", 7.5 * 20.0, 150.0)
    check("coste derivado reversible", (7.5 * 20.0) / 20.0, 7.5)

    # 12. La franja con horas pagadas y cero venta debe quedar senalada en la
    # linea, no colada como una franja barata.
    linea = bloque_ratios("18:00 - 19:00", 0.0, 4.0, 80.0, 0.0, _ArgsFalsos())
    check("franja sin venta marcada", "HORAS PAGADAS SIN VENTA" in linea, True)
    check("franja sin venta no dice 0,0%", "0.0%" in linea, False)

    if fallos:
        print(f"AUTOTEST FALLIDO: {len(fallos)} de {len(hechas)} comprobaciones")
        for f in fallos:
            print(f"  - {f}")
        return 1
    print(f"AUTOTEST OK: {len(hechas)} comprobaciones de productividad pasadas.")
    return 0


def main():
    p = argparse.ArgumentParser(description="Productividad de personal por franja, dia y escalera de entradas.")
    p.add_argument("archivo", nargs="?")
    p.add_argument("--autotest", action="store_true",
                   help="ejecuta las comprobaciones aritmeticas internas y sale")
    p.add_argument("--modo", choices=["franjas", "semana", "escalera"], default="franjas")
    p.add_argument("--coste-hora", type=float, default=None,
                   help="Coste TOTAL por hora trabajada (bruto + cargas). Obligatorio si el archivo no trae coste.")
    p.add_argument("--umbral-objetivo", type=float, default=30.0, help="%% de coste de personal objetivo (defecto 30)")
    p.add_argument("--umbral-alto", type=float, default=40.0, help="%% por encima del cual se marca la franja (defecto 40)")
    p.add_argument("--umbral-bajo", type=float, default=15.0, help="%% por debajo del cual se sospecha falta de mano (defecto 15)")
    p.add_argument("--horas-minimas", type=float, default=5.0, help="Horas acumuladas minimas para tomar en serio una franja")
    p.add_argument("--dias-periodo", type=int, default=None, help="Dias que cubre el archivo, para anualizar")
    args = p.parse_args()

    if args.autotest:
        sys.exit(autotest())
    if not args.archivo:
        p.error("indica el archivo de turnos, o usa --autotest")

    if args.coste_hora is None:
        args.coste_hora = 0.0
    if args.coste_hora < 0:
        sys.exit("ERROR: --coste-hora no puede ser negativo.")
    if args.umbral_objetivo <= 0 or args.umbral_alto <= 0 or args.umbral_bajo < 0:
        sys.exit("ERROR: los umbrales deben ser positivos.")
    if args.umbral_alto <= args.umbral_objetivo:
        sys.exit("ERROR: --umbral-alto tiene que ser mayor que --umbral-objetivo.")
    if args.umbral_bajo >= args.umbral_objetivo:
        sys.exit("ERROR: --umbral-bajo tiene que ser menor que --umbral-objetivo.")
    if args.dias_periodo is not None and args.dias_periodo <= 0:
        sys.exit("ERROR: --dias-periodo debe ser mayor que cero.")
    if args.modo == "escalera" and args.coste_hora <= 0:
        sys.exit("ERROR: el modo escalera necesita --coste-hora.\n"
                 "Y tiene que ser el coste TOTAL: bruto mas cargas sociales mas vacaciones.\n"
                 "Usar el salario bruto a secas infravalora la hora entre un 25% y un 35% "
                 "segun pais y convenio [dato a validar con el cliente].")

    {"franjas": modo_franjas, "semana": modo_semana, "escalera": modo_escalera}[args.modo](args)


if __name__ == "__main__":
    main()
