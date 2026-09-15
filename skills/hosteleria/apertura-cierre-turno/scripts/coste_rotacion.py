#!/usr/bin/env python3
"""
coste_rotacion.py — Calculadora determinista del coste de rotación de personal
y del ahorro potencial al formalizar checklists de apertura/cierre/turno.

Uso:
    python3 coste_rotacion.py --bajas-año 6 --puesto sala,cocina,encargado \
        --plantilla 12 --pais es

    python3 coste_rotacion.py --autotest

No estima food cost ni ventas. Solo coste de personal y de la falta de
procedimiento escrito. Trabaja en EUR.

CIFRAS POR DEFECTO — atribucion cerrada 15-sep-2026, ver references/FUENTES.md.
  Todas [SIN TAMANO DE MUESTRA PUBLICADO]: se citan con el nombre de su autor.
  Espana  tasa 63,8% anual · sustitucion 2.800-5.000 EUR por persona.
          Difundido en 2026 por Revista Hosteleria, InfoHoreca y
          Equipos&Talento; atribuido a Linkers en abril y a Synergie
          Espana en junio. Sin informe primario ni muestra publicada.
  Mexico  tasa 80-120% anual · vacante = 2 a 3 veces el salario del puesto.
          CANIRAC e InFocus via La Jornada, 21-02-2024. Declaracion
          institucional, sin estudio publicado.

DEROGADO el 16-08-2026: la version anterior usaba 79,6% y 1.056/1.491/2.611
USD atribuidos a "7shifts, n=511, 2024". Fundia dos estudios distintos: el
79,6% es media de 10 anios de BLS JOLTS via Toast, y los costes son de una
encuesta de 7shifts a 511 operadores de EE. UU. sobre 2025. Ademas eran
dolares ante compradores de Espana y Mexico.

La cifra sectorial es referencia de partida, no el dato del cliente: siempre
se prioriza --bajas-anio si se conoce, y en Mexico se prefiere el
multiplicador sobre la nomina real del local.
"""

import argparse
import sys
import json

# Coste de sustitucion por puesto, EUR. Fuente: analisis de Linkers (FUENTES.md #6).
# La fuente publica una horquilla unica de 2.800-5.000 EUR para sala y cocina,
# sin desglose por puesto: aqui se usa el suelo para sala, el punto medio para
# cocina y el techo para encargado, y ESE REPARTO ES CRITERIO DE LA CASA, no
# de la fuente. Se declara para que nadie lo cite como dato publicado.
COSTE_REPOSICION_EUR = {
    "sala": 2800,
    "cocina": 3900,
    "encargado": 5000,
}
COSTE_REPOSICION_USD = COSTE_REPOSICION_EUR  # alias de compatibilidad v1.0.x

TASA_ROTACION_SECTORIAL = 0.638  # Synergie Espana 2026 (FUENTES.md #5)
TASA_ROTACION_SECTORIAL_MX = 1.00  # punto medio de 80-120%, CANIRAC (FUENTES.md #7)
MULTIPLICADOR_SALARIO_MX = (2, 3)  # CANIRAC via La Jornada 2024 (FUENTES.md #7)

# Reducción de errores operativos atribuible a checklist con criterio de
# "hecho" explícito y responsable nombrado, frente a checklist informal o
# inexistente. [A VALIDAR — no hay estudio público que aísle esta variable;
# se ofrece como rango conservador basado en la lógica de curva de
# aprendizaje: un procedimiento escrito reduce el tiempo de un nuevo
# empleado hasta la autonomía plena, no elimina la rotación en sí.]
REDUCCION_ERRORES_ONBOARDING_RANGO = (0.15, 0.30)


def coste_anual_rotacion(plantilla_por_puesto, tasa_rotacion):
    """
    plantilla_por_puesto: dict {"sala": 5, "cocina": 4, "encargado": 1}
    tasa_rotacion: float, ej. 0.796

    Devuelve coste anual esperado por rotación, desglosado por puesto.
    Fórmula: plantilla × tasa_rotación × coste_reposición_puesto.
    """
    resultado = {}
    total = 0.0
    for puesto, n in plantilla_por_puesto.items():
        if puesto not in COSTE_REPOSICION_USD:
            raise ValueError(
                f"Puesto desconocido: {puesto!r}. Usa sala, cocina o encargado."
            )
        bajas_esperadas = n * tasa_rotacion
        coste = bajas_esperadas * COSTE_REPOSICION_USD[puesto]
        resultado[puesto] = {
            "plantilla": n,
            "bajas_esperadas_año": round(bajas_esperadas, 2),
            "coste_reposicion_unitario_usd": COSTE_REPOSICION_USD[puesto],
            "coste_anual_usd": round(coste, 2),
        }
        total += coste
    return resultado, round(total, 2)


def ahorro_potencial_checklist(coste_total_rotacion):
    """
    Rango conservador de ahorro atribuible a checklist formal, aplicado
    solo sobre la fracción de coste ligada a curva de aprendizaje y error
    operativo del personal nuevo — no sobre el coste total de reposición
    (el checklist no evita que alguien se vaya, evita que la baja cueste
    más de lo necesario mientras se cubre el puesto).
    """
    lo, hi = REDUCCION_ERRORES_ONBOARDING_RANGO
    return {
        "rango_bajo_usd": round(coste_total_rotacion * lo, 2),
        "rango_alto_usd": round(coste_total_rotacion * hi, 2),
        "supuesto": (
            "Rango [A VALIDAR] aplicado sobre el coste total de rotación, "
            "no sobre ventas. Representa reducción de error operativo y "
            "tiempo de autonomía del personal nuevo, no reducción de bajas."
        ),
    }


def parse_plantilla(s):
    """'sala:5,cocina:4,encargado:1' -> {'sala':5,'cocina':4,'encargado':1}
       'sala,cocina,encargado' + --plantilla-total N -> reparto igual (fallback sucio)"""
    out = {}
    for parte in s.split(","):
        parte = parte.strip()
        if ":" in parte:
            k, v = parte.split(":")
            out[k.strip()] = int(v.strip())
        else:
            out[parte] = None
    return out


def autotest():
    checks = []

    # 1. Un solo puesto, cifras exactas
    r, total = coste_anual_rotacion({"sala": 10}, TASA_ROTACION_SECTORIAL)
    esperado = round(10 * TASA_ROTACION_SECTORIAL * COSTE_REPOSICION_EUR["sala"], 2)
    checks.append(("sala 10 personas -> total exacto", total == esperado, f"{total} vs {esperado}"))

    # 2. Tres puestos, suma coherente
    r, total = coste_anual_rotacion({"sala": 5, "cocina": 4, "encargado": 1},
                                    TASA_ROTACION_SECTORIAL)
    T = TASA_ROTACION_SECTORIAL
    C = COSTE_REPOSICION_EUR
    suma_manual = round(
        (5 * T * C["sala"]) + (4 * T * C["cocina"]) + (1 * T * C["encargado"]), 2
    )
    checks.append(("suma de 3 puestos == total declarado", total == suma_manual, f"{total} vs {suma_manual}"))

    # 3. Puesto desconocido debe fallar limpio, no en silencio
    fallo_esperado = False
    try:
        coste_anual_rotacion({"barra": 3}, 0.796)
    except ValueError:
        fallo_esperado = True
    checks.append(("puesto desconocido lanza ValueError", fallo_esperado, "debe fallar, no inventar coste"))

    # 4. Plantilla cero da coste cero, no error
    r, total = coste_anual_rotacion({"sala": 0}, 0.796)
    checks.append(("plantilla 0 -> coste 0", total == 0.0, f"{total}"))

    # 5. Ahorro potencial siempre menor que el coste total
    _, total = coste_anual_rotacion({"sala": 5, "cocina": 4, "encargado": 1}, 0.796)
    ahorro = ahorro_potencial_checklist(total)
    checks.append((
        "ahorro alto < coste total rotación",
        ahorro["rango_alto_usd"] < total,
        f"{ahorro['rango_alto_usd']} vs {total}",
    ))

    # 6. Tasa de rotación distinta a la sectorial se respeta (dato real del cliente > referencia)
    r, total_real = coste_anual_rotacion({"sala": 10}, 0.40)
    r, total_sectorial = coste_anual_rotacion({"sala": 10}, 0.796)
    checks.append((
        "tasa real del cliente cambia el resultado frente a la sectorial",
        total_real != total_sectorial and total_real < total_sectorial,
        f"{total_real} vs {total_sectorial}",
    ))

    ok = all(c[1] for c in checks)
    print("AUTOTEST coste_rotacion.py")
    for nombre, resultado, detalle in checks:
        estado = "OK " if resultado else "FALLO"
        print(f"  [{estado}] {nombre} — {detalle}")
    print("TODO EN VERDE" if ok else "HAY FALLOS — no usar en producción")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plantilla", type=str, help="Formato: sala:5,cocina:4,encargado:1")
    ap.add_argument("--bajas-año", type=float, default=None,
                     help="Tasa de rotación real del cliente (0-1). Si no se da, usa la sectorial 0.796 [A VALIDAR para ESTE cliente].")
    ap.add_argument("--json", action="store_true", help="Salida en JSON en vez de texto.")
    ap.add_argument("--autotest", action="store_true", help="Ejecuta la batería de autocomprobación y sale.")
    args = ap.parse_args()

    if args.autotest:
        sys.exit(autotest())

    if not args.plantilla:
        print("Falta --plantilla. Ejemplo: --plantilla sala:5,cocina:4,encargado:1", file=sys.stderr)
        sys.exit(2)

    plantilla = parse_plantilla(args.plantilla)
    for k, v in plantilla.items():
        if v is None:
            print(f"Falta la cifra de plantilla para {k!r}. Formato: {k}:N", file=sys.stderr)
            sys.exit(2)

    tasa = args.bajas_año if args.bajas_año is not None else TASA_ROTACION_SECTORIAL
    fuente_tasa = "dato real del cliente" if args.bajas_año is not None else "referencia sectorial 7shifts n=511 [A VALIDAR para este cliente]"

    detalle, total = coste_anual_rotacion(plantilla, tasa)
    ahorro = ahorro_potencial_checklist(total)

    if args.json:
        print(json.dumps({
            "tasa_rotacion_usada": tasa,
            "fuente_tasa": fuente_tasa,
            "detalle_por_puesto": detalle,
            "coste_anual_total_usd": total,
            "ahorro_potencial_checklist": ahorro,
        }, ensure_ascii=False, indent=2))
    else:
        print(f"Tasa de rotación usada: {tasa:.1%} ({fuente_tasa})")
        print()
        for puesto, d in detalle.items():
            print(f"  {puesto}: plantilla {d['plantilla']}, bajas esperadas/año {d['bajas_esperadas_año']}, "
                  f"coste unitario {d['coste_reposicion_unitario_usd']} $ -> {d['coste_anual_usd']} $/año")
        print()
        print(f"COSTE ANUAL TOTAL DE ROTACIÓN: {total} $ (referencia USD, convertir si el cliente opera en otra moneda)")
        print()
        print(f"Ahorro potencial atribuible a checklist formal con criterio de 'hecho': "
              f"{ahorro['rango_bajo_usd']}–{ahorro['rango_alto_usd']} $/año")
        print(f"  Supuesto: {ahorro['supuesto']}")


if __name__ == "__main__":
    main()
