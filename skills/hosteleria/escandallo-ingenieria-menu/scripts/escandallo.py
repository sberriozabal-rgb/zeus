#!/usr/bin/env python3
"""Escandallo e ingenieria de menu.

Calcula el coste real por plato (con rendimiento de limpieza, merma de coccion y
costes ocultos), el margen de contribucion, y clasifica cada plato en la matriz
de Kasavana-Smith: estrella / caballo / rompecabezas / perro.

Uso:
    python3 escandallo.py datos.json
    python3 escandallo.py datos.json --csv salida.csv
    python3 escandallo.py --ejemplo          # imprime un JSON de entrada valido

Sin dependencias externas. Python 3.9+.
"""

import argparse
import json
import sys
from typing import Any, Dict, List

# El umbral de popularidad de Kasavana-Smith: 70% de la cuota media.
UMBRAL_POPULARIDAD = 0.70


def _num(valor: Any, campo: str, plato: str) -> float:
    try:
        return float(valor)
    except (TypeError, ValueError):
        raise SystemExit(f"ERROR en '{plato}': el campo '{campo}' no es un numero ({valor!r})")


def coste_ingrediente(ing: Dict[str, Any], plato: str) -> Dict[str, Any]:
    """Coste de un ingrediente a partir de peso neto en plato y rendimientos."""
    nombre = ing.get("nombre", "(sin nombre)")
    precio_kg = _num(ing.get("precio_kg", 0), "precio_kg", plato)
    gramos = _num(ing.get("gramos_en_plato", 0), "gramos_en_plato", plato)

    # rendimiento de limpieza: fraccion del producto comprado que llega al plato
    rendimiento = _num(ing.get("rendimiento", 1.0), "rendimiento", plato)
    if not 0 < rendimiento <= 1:
        raise SystemExit(
            f"ERROR en '{plato}' / '{nombre}': rendimiento debe estar entre 0 y 1 (recibido {rendimiento})"
        )

    # merma de coccion: fraccion de peso que se pierde al cocinar
    merma = _num(ing.get("merma_coccion", 0.0), "merma_coccion", plato)
    if not 0 <= merma < 1:
        raise SystemExit(
            f"ERROR en '{plato}' / '{nombre}': merma_coccion debe estar entre 0 y 0.99 (recibido {merma})"
        )

    # Si la receta se escribe en peso ya cocinado, hay que revertir a crudo.
    gramos_crudos = gramos / (1 - merma) if merma else gramos
    # Y del crudo neto al bruto comprado, dividiendo por el rendimiento.
    gramos_brutos = gramos_crudos / rendimiento

    coste = gramos_brutos / 1000.0 * precio_kg
    return {
        "nombre": nombre,
        "precio_kg": precio_kg,
        "gramos_en_plato": gramos,
        "gramos_comprados": round(gramos_brutos, 1),
        "coste_kg_neto": round(precio_kg / rendimiento, 2),
        "coste": round(coste, 4),
    }


def analizar_plato(plato: Dict[str, Any], iva_defecto: float) -> Dict[str, Any]:
    nombre = plato.get("nombre", "(sin nombre)")
    precio_carta = _num(plato.get("precio_carta", 0), "precio_carta", nombre)
    iva = _num(plato.get("iva", iva_defecto), "iva", nombre)
    unidades = _num(plato.get("unidades_vendidas", 0), "unidades_vendidas", nombre)

    # El precio de carta lleva IVA incluido; el escandallo va sobre base imponible.
    precio_neto = precio_carta / (1 + iva)

    ingredientes = [coste_ingrediente(i, nombre) for i in plato.get("ingredientes", [])]
    coste_receta = sum(i["coste"] for i in ingredientes)

    # Costes ocultos: mesa, coccion, bases, envase. Porcentaje sobre el coste de receta.
    pct_ocultos = _num(plato.get("costes_ocultos_pct", 0.0), "costes_ocultos_pct", nombre)
    coste_oculto = coste_receta * pct_ocultos
    coste_total = coste_receta + coste_oculto

    margen = precio_neto - coste_total
    food_cost = coste_total / precio_neto if precio_neto else 0.0

    return {
        "nombre": nombre,
        "familia": plato.get("familia", "carta"),
        "unidades": unidades,
        "precio_carta": round(precio_carta, 2),
        "precio_neto": round(precio_neto, 2),
        "coste_receta": round(coste_receta, 2),
        "coste_oculto": round(coste_oculto, 2),
        "coste_total": round(coste_total, 2),
        "margen_unitario": round(margen, 2),
        "margen_total": round(margen * unidades, 2),
        "food_cost": round(food_cost, 4),
        "intocable": bool(plato.get("intocable", False)),
        "ingredientes": ingredientes,
        "alertas": [],
    }


def clasificar(platos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Matriz de Kasavana-Smith, calculada por familia."""
    familias: Dict[str, List[Dict[str, Any]]] = {}
    for p in platos:
        familias.setdefault(p["familia"], []).append(p)

    for familia, grupo in familias.items():
        u_total = sum(p["unidades"] for p in grupo)
        m_total = sum(p["margen_total"] for p in grupo)
        n = len(grupo)
        cuota_media = 1.0 / n if n else 0.0
        umbral_pop = cuota_media * UMBRAL_POPULARIDAD
        # Margen medio ponderado por unidades vendidas, no media simple:
        # una media simple deja que un plato caro y sin ventas mueva el listón.
        margen_medio = m_total / u_total if u_total else 0.0

        for p in grupo:
            cuota = p["unidades"] / u_total if u_total else 0.0
            popular = cuota >= umbral_pop
            rentable = p["margen_unitario"] >= margen_medio
            p["cuota"] = round(cuota, 4)
            p["umbral_popularidad"] = round(umbral_pop, 4)
            p["margen_medio_familia"] = round(margen_medio, 2)
            if popular and rentable:
                p["cuadrante"] = "ESTRELLA"
                p["accion"] = "Proteger: calidad y disponibilidad. No usar para subir precio si es marcador."
            elif popular and not rentable:
                p["cuadrante"] = "CABALLO"
                p["accion"] = "Bajar coste antes que subir precio: porcionado, rendimiento, sustitucion, emplatado."
            elif not popular and rentable:
                p["cuadrante"] = "ROMPECABEZAS"
                p["accion"] = "Trabajar la venta: reubicar en carta, renombrar, formar a sala. Medir a 2 semanas."
            else:
                p["cuadrante"] = "PERRO"
                p["accion"] = "Candidato a retirada. Antes: comprobar si es ancla de cliente, comparte producto o marca precio."
            if p["intocable"]:
                p["accion"] = "MARCADOR DE PRECIO — no tocar el precio. " + p["accion"]
            # Con familias muy pequenas la matriz deja de discriminar: con un solo
            # plato, ese plato ES la media y siempre sale estrella. Conviene decirlo.
            p["familia_pequena"] = n < 3
    return platos


def alertas(p: Dict[str, Any]) -> List[str]:
    a = []
    if p["coste_total"] > p["precio_neto"]:
        a.append("PIERDE DINERO en cada unidad: revisa unidades o el precio de carta")
    if 0 < p["food_cost"] < 0.10:
        a.append("food cost < 10%: probablemente falta un ingrediente en la receta")
    if p["food_cost"] > 0.45:
        a.append("food cost > 45%: insostenible salvo que sea reclamo consciente")
    if p["unidades"] == 0:
        a.append("0 ventas: comprueba si sigue en carta o es un boton muerto del POS")
    if p.get("familia_pequena"):
        a.append(
            f"familia '{p['familia']}' con menos de 3 platos: el cuadrante no es "
            "concluyente, agrupa familias o interpreta con cautela"
        )
    return a


def informe(datos: Dict[str, Any]) -> Dict[str, Any]:
    iva_defecto = float(datos.get("iva_defecto", 0.10))
    platos = [analizar_plato(p, iva_defecto) for p in datos.get("platos", [])]
    if not platos:
        raise SystemExit("ERROR: no hay platos en el archivo de entrada.")
    platos = clasificar(platos)
    for p in platos:
        p["alertas"] = alertas(p)

    ventas_netas = sum(p["precio_neto"] * p["unidades"] for p in platos)
    coste_total = sum(p["coste_total"] * p["unidades"] for p in platos)
    margen_total = sum(p["margen_total"] for p in platos)
    fc_teorico = coste_total / ventas_netas if ventas_netas else 0.0

    resumen = {
        "periodo_meses": float(datos.get("periodo_meses", 1)),
        "platos_analizados": len(platos),
        "unidades_totales": sum(p["unidades"] for p in platos),
        "ventas_netas": round(ventas_netas, 2),
        "coste_materia_prima": round(coste_total, 2),
        "margen_contribucion": round(margen_total, 2),
        "food_cost_teorico": round(fc_teorico, 4),
    }

    fc_real = datos.get("food_cost_real")
    if fc_real is not None:
        fc_real = float(fc_real)
        desviacion = (fc_real - fc_teorico) * 100
        resumen["food_cost_real"] = round(fc_real, 4)
        resumen["desviacion_puntos"] = round(desviacion, 2)
        if desviacion > 5:
            resumen["lectura_desviacion"] = (
                "CRITICA: mas de 5 puntos. El problema no es la carta, es control "
                "(porcionado, mermas, roturas, invitaciones sin registrar). "
                "Subir precios aqui solo tapa el agujero."
            )
        elif desviacion > 2:
            resumen["lectura_desviacion"] = (
                "ATENCION: mas de 2 y hasta 5 puntos. Porcionado o mermas descontroladas. "
                "El analisis de carta es valido, pero no resuelve todo el problema."
            )
        else:
            resumen["lectura_desviacion"] = "NORMAL: la cocina ejecuta lo que dice la receta."
    else:
        resumen["lectura_desviacion"] = (
            "SIN CONTRASTE: no se aporto food cost real (hace falta inventario inicial, "
            "compras e inventario final). El analisis va sobre teorico."
        )

    orden = {"CABALLO": 0, "PERRO": 1, "ROMPECABEZAS": 2, "ESTRELLA": 3}
    platos.sort(key=lambda p: (orden.get(p["cuadrante"], 9), -p["unidades"]))
    return {"resumen": resumen, "platos": platos}


def imprimir(res: Dict[str, Any]) -> None:
    r = res["resumen"]
    print("=" * 78)
    print("ESCANDALLO E INGENIERIA DE MENU")
    print("=" * 78)
    print(f"Platos: {r['platos_analizados']}   Unidades: {r['unidades_totales']:.0f}")
    print(f"Ventas netas (sin IVA): {r['ventas_netas']:>12,.2f}")
    print(f"Coste materia prima:    {r['coste_materia_prima']:>12,.2f}")
    print(f"Margen de contribucion: {r['margen_contribucion']:>12,.2f}")
    print(f"Food cost teorico:      {r['food_cost_teorico']*100:>11.2f}%")
    if "food_cost_real" in r:
        print(f"Food cost real:         {r['food_cost_real']*100:>11.2f}%")
        print(f"Desviacion:             {r['desviacion_puntos']:>11.2f} puntos")
    print(f"\n>> {r['lectura_desviacion']}\n")

    print("-" * 78)
    print(f"{'PLATO':<26}{'UDS':>6}{'PVP':>8}{'COSTE':>8}{'MARGEN':>9}{'FC%':>7}{'CUADRANTE':>14}")
    print("-" * 78)
    for p in res["platos"]:
        print(
            f"{p['nombre'][:25]:<26}{p['unidades']:>6.0f}{p['precio_neto']:>8.2f}"
            f"{p['coste_total']:>8.2f}{p['margen_unitario']:>9.2f}"
            f"{p['food_cost']*100:>7.1f}{p['cuadrante']:>14}"
        )
    print("-" * 78)

    print("\nACCIONES POR PLATO (ordenadas por urgencia)\n")
    for p in res["platos"]:
        marca = " [INTOCABLE]" if p["intocable"] else ""
        print(f"  {p['nombre']}{marca} — {p['cuadrante']}")
        print(f"      {p['accion']}")
        if p["cuadrante"] == "CABALLO" and p["unidades"]:
            meses = res["resumen"].get("periodo_meses", 1) or 1
            anual = p["unidades"] * (12.0 / meses)
            print(
                f"      Referencia: bajar 1,00 de coste unitario = {anual:,.0f} al ano, "
                f"extrapolando el ritmo de venta de {meses:g} mes(es)."
            )
        for a in p["alertas"]:
            print(f"      !! {a}")
        print()


EJEMPLO = {
    "local": "Ejemplo",
    "periodo": "2026-07",
    "iva_defecto": 0.10,
    "food_cost_real": 0.34,
    "platos": [
        {
            "nombre": "Merluza a la plancha",
            "familia": "principales",
            "precio_carta": 24.00,
            "unidades_vendidas": 180,
            "costes_ocultos_pct": 0.06,
            "ingredientes": [
                {"nombre": "Merluza entera", "precio_kg": 12.00,
                 "gramos_en_plato": 180, "rendimiento": 0.55, "merma_coccion": 0.18},
                {"nombre": "Patata", "precio_kg": 1.20,
                 "gramos_en_plato": 120, "rendimiento": 0.82},
                {"nombre": "Aceite de oliva", "precio_kg": 8.50, "gramos_en_plato": 20}
            ]
        },
        {
            "nombre": "Ensalada de la casa",
            "familia": "principales",
            "precio_carta": 12.50,
            "unidades_vendidas": 240,
            "costes_ocultos_pct": 0.05,
            "intocable": True,
            "ingredientes": [
                {"nombre": "Lechuga", "precio_kg": 2.20,
                 "gramos_en_plato": 90, "rendimiento": 0.65},
                {"nombre": "Tomate", "precio_kg": 2.80, "gramos_en_plato": 80, "rendimiento": 0.95},
                {"nombre": "Atun", "precio_kg": 14.00, "gramos_en_plato": 50}
            ]
        }
    ]
}


def main() -> None:
    ap = argparse.ArgumentParser(description="Escandallo e ingenieria de menu")
    ap.add_argument("archivo", nargs="?", help="JSON con la carta y las ventas")
    ap.add_argument("--ejemplo", action="store_true", help="imprime un JSON de entrada valido")
    ap.add_argument("--json", metavar="RUTA", help="guarda el resultado completo en JSON")
    ap.add_argument("--csv", metavar="RUTA", help="guarda la tabla de platos en CSV")
    args = ap.parse_args()

    if args.ejemplo:
        print(json.dumps(EJEMPLO, indent=2, ensure_ascii=False))
        return
    if not args.archivo:
        ap.error("indica un archivo JSON, o usa --ejemplo para ver el formato")

    try:
        with open(args.archivo, encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"ERROR: no encuentro el archivo {args.archivo}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"ERROR: el JSON no es valido ({e})")

    res = informe(datos)
    imprimir(res)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2, ensure_ascii=False)
        print(f"JSON guardado en {args.json}")
    if args.csv:
        import csv
        campos = ["nombre", "familia", "unidades", "precio_carta", "precio_neto",
                  "coste_total", "margen_unitario", "margen_total", "food_cost", "cuadrante", "accion"]
        with open(args.csv, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
            w.writeheader()
            for p in res["platos"]:
                w.writerow(p)
        print(f"CSV guardado en {args.csv}")


if __name__ == "__main__":
    main()
