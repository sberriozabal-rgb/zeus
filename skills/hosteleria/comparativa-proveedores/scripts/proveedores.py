#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
comparativa-proveedores · motor de cálculo determinista
========================================================

Convierte líneas de factura/albarán de varios proveedores en tres cosas
que un dueño de restaurante puede ejecutar el lunes:

  1) ALERTA DE SUBIDAS   — qué producto subió, cuánto, y desde cuándo.
  2) COMPARATIVA          — qué proveedor tiene HOY cada producto más barato.
  3) IMPACTO EN LA CARTA  — cuánto margen pierde cada plato por las subidas
                            (solo si se aportan datos de la carta / escandallo).

Principio de oficio: todo se compara a UNIDAD BASE COMÚN (€/kg, €/L o €/ud) y
SIN IVA. Comparar €/caja con €/kg, o precio con IVA contra albarán sin IVA, es
el error de compras más común y desplaza la decisión varios puntos.

El script no razona ni inventa: solo calcula lo que se le da. Si falta un dato,
lo deja como hueco declarado, nunca lo rellena.

Uso:
    python3 proveedores.py datos.json
    python3 proveedores.py --ejemplo      # imprime el formato de entrada
    python3 proveedores.py --autotest     # ejecuta la batería de comprobación

Sin dependencias externas. Python 3.9+.
"""

import json
import sys
from datetime import datetime

# ----------------------------------------------------------------------
# Normalización de unidades a base común
# ----------------------------------------------------------------------
# Toda línea se lleva a una de tres bases: "kg", "L" o "ud".
# Factor = cuántas unidades base contiene una unidad de compra.
#   Ej.: caja de 5 kg  -> base "kg", factor 5   -> €/kg = precio_caja / 5
#        garrafa 5 L    -> base "L",  factor 5   -> €/L  = precio_garrafa / 5
#        docena         -> base "ud", factor 12
FACTORES = {
    "kg": ("kg", 1.0),
    "g": ("kg", 0.001),
    "gr": ("kg", 0.001),
    "l": ("L", 1.0),
    "lt": ("L", 1.0),
    "litro": ("L", 1.0),
    "cl": ("L", 0.01),
    "ml": ("L", 0.001),
    "ud": ("ud", 1.0),
    "unidad": ("ud", 1.0),
    "u": ("ud", 1.0),
    "docena": ("ud", 12.0),
    "pieza": ("ud", 1.0),
}


def _norm_unidad(unidad, formato):
    """Devuelve (base, factor_total) para llevar el precio a €/base.

    unidad: la unidad de venta declarada ('caja', 'kg', 'garrafa', 'saco'...)
    formato: cuántas unidades base contiene esa unidad de venta.
             Ej. caja de 5 kg -> unidad='caja', formato={'valor':5,'base':'kg'}
    Si la unidad ya es base (kg, L, ud), formato puede omitirse.
    """
    u = (unidad or "").strip().lower()

    # Caso 1: la unidad es directamente una base conocida.
    if u in FACTORES:
        base, factor = FACTORES[u]
        return base, factor

    # Caso 2: unidad de agregación (caja, saco, garrafa, palé, bandeja...)
    # Necesita formato explícito {valor, base}.
    if not formato:
        raise ValueError(
            f"Unidad '{unidad}' no es base (kg/L/ud) y falta 'formato' "
            f"con {{valor, base}}. No se puede comparar sin normalizar."
        )
    valor = float(formato["valor"])
    base_decl = formato["base"].strip().lower()
    if base_decl not in FACTORES:
        raise ValueError(f"Base de formato '{base_decl}' desconocida.")
    base, factor_base = FACTORES[base_decl]
    return base, valor * factor_base


def _sin_iva(precio, iva_pct, precio_lleva_iva):
    """Devuelve el precio base imponible. Los albaranes de proveedor casi
    siempre vienen SIN IVA; si el dato viene con IVA, se descuenta."""
    if not precio_lleva_iva:
        return precio
    return precio / (1.0 + iva_pct / 100.0)


def _precio_por_base(linea):
    """€ por unidad base, sin IVA, para una línea de compra."""
    base, factor_total = _norm_unidad(linea.get("unidad"), linea.get("formato"))
    precio = float(linea["precio"])
    iva = float(linea.get("iva_pct", 0.0))
    lleva_iva = bool(linea.get("precio_lleva_iva", False))
    precio_neto = _sin_iva(precio, iva, lleva_iva)
    if factor_total <= 0:
        raise ValueError(f"Formato con factor no positivo en {linea}")
    return round(precio_neto / factor_total, 6), base


def _parse_fecha(f):
    if not f:
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(f.strip(), fmt).date()
        except (ValueError, AttributeError):
            continue
    return None


# ----------------------------------------------------------------------
# Núcleo
# ----------------------------------------------------------------------
def analizar(datos):
    """datos: dict con 'lineas' (obligatorio), 'umbral_alerta_pct',
    'volatiles', 'carta' (opcional). Devuelve dict de resultados."""

    umbral = float(datos.get("umbral_alerta_pct", 8.0))
    # Familias que suben y bajan por temporada: su subida no es "clavada",
    # es estacional. Se marcan aparte para no confundir ruido con abuso.
    volatiles = set(x.lower() for x in datos.get("volatiles",
                    ["pescado", "marisco", "verdura", "fruta", "hoja"]))

    # Agrupa por producto normalizado (clave = nombre_normalizado)
    productos = {}
    errores = []
    for i, ln in enumerate(datos.get("lineas", [])):
        try:
            pxb, base = _precio_por_base(ln)
        except (ValueError, KeyError) as e:
            errores.append(f"Línea {i}: {e}")
            continue
        clave = ln["producto"].strip().lower()
        productos.setdefault(clave, {
            "nombre": ln["producto"].strip(),
            "base": base,
            "familia": (ln.get("familia") or "").strip().lower(),
            "registros": [],
        })
        # Coherencia de base: no se puede comparar un producto que aparece
        # una vez en kg y otra en ud. Es error de datos.
        if productos[clave]["base"] != base:
            errores.append(
                f"Línea {i}: '{ln['producto']}' aparece en base "
                f"'{base}' y antes en '{productos[clave]['base']}'. "
                f"Revisa la unidad."
            )
            continue
        productos[clave]["registros"].append({
            "proveedor": ln.get("proveedor", "sin-nombre").strip(),
            "precio_base": pxb,
            "fecha": _parse_fecha(ln.get("fecha")),
            "consumo_mes": float(ln.get("consumo_mes_base", 0) or 0),
            "raw": ln,
        })

    alertas = []       # subidas del mismo proveedor en el tiempo
    comparativas = []  # mismo producto, distinto proveedor, hoy
    formato_sospechoso = []

    for clave, p in productos.items():
        regs = p["registros"]
        familia = p["familia"]
        es_volatil = any(v in familia or v in p["nombre"].lower()
                         for v in volatiles)

        # --- Comparativa entre proveedores (foto de hoy: último de cada uno)
        ultimo_por_prov = {}
        for r in regs:
            prov = r["proveedor"]
            prev = ultimo_por_prov.get(prov)
            if prev is None or (r["fecha"] and prev["fecha"]
                                and r["fecha"] > prev["fecha"]):
                ultimo_por_prov[prov] = r
            elif prev["fecha"] is None:
                ultimo_por_prov[prov] = r
        if len(ultimo_por_prov) >= 2:
            ordenados = sorted(ultimo_por_prov.values(),
                               key=lambda r: r["precio_base"])
            barato, caro = ordenados[0], ordenados[-1]
            # Consumo mensual estimado: el mayor declarado en el producto
            consumo = max((r["consumo_mes"] for r in regs), default=0.0)
            dif_pct = ((caro["precio_base"] - barato["precio_base"])
                       / barato["precio_base"] * 100.0) if barato["precio_base"] else 0
            ahorro_mes = (caro["precio_base"] - barato["precio_base"]) * consumo
            comparativas.append({
                "producto": p["nombre"],
                "base": p["base"],
                "mas_barato": barato["proveedor"],
                "precio_barato": round(barato["precio_base"], 4),
                "mas_caro": caro["proveedor"],
                "precio_caro": round(caro["precio_base"], 4),
                "dif_pct": round(dif_pct, 1),
                "consumo_mes_base": consumo,
                "ahorro_mes_eur": round(ahorro_mes, 2),
                "ahorro_ano_eur": round(ahorro_mes * 12, 2),
            })

        # --- Alerta de subidas (mismo proveedor, dos fechas)
        por_prov = {}
        for r in regs:
            por_prov.setdefault(r["proveedor"], []).append(r)
        for prov, rr in por_prov.items():
            con_fecha = [r for r in rr if r["fecha"]]
            if len(con_fecha) < 2:
                continue
            con_fecha.sort(key=lambda r: r["fecha"])
            antes, ahora = con_fecha[0], con_fecha[-1]
            if antes["precio_base"] <= 0:
                continue
            var_pct = ((ahora["precio_base"] - antes["precio_base"])
                       / antes["precio_base"] * 100.0)
            consumo = max((r["consumo_mes"] for r in rr), default=0.0)
            impacto_mes = (ahora["precio_base"] - antes["precio_base"]) * consumo
            # Detección de formato encubierto: mismo precio de línea, distinto
            # peso -> subida disfrazada. Se detecta si el €/base sube pero el
            # precio de línea es idéntico.
            if (abs(float(ahora["raw"]["precio"]) - float(antes["raw"]["precio"])) < 0.001
                    and var_pct > 1.0):
                formato_sospechoso.append({
                    "producto": p["nombre"], "proveedor": prov,
                    "nota": "Mismo precio de línea, menos cantidad: subida encubierta por cambio de formato.",
                    "subida_real_pct": round(var_pct, 1),
                })
            if var_pct >= umbral:
                alertas.append({
                    "producto": p["nombre"],
                    "proveedor": prov,
                    "base": p["base"],
                    "precio_antes": round(antes["precio_base"], 4),
                    "precio_ahora": round(ahora["precio_base"], 4),
                    "var_pct": round(var_pct, 1),
                    "desde": str(antes["fecha"]),
                    "hasta": str(ahora["fecha"]),
                    "consumo_mes_base": consumo,
                    "impacto_mes_eur": round(impacto_mes, 2),
                    "impacto_ano_eur": round(impacto_mes * 12, 2),
                    "estacional": es_volatil,
                })

    # Ordena por impacto en euros: lo que mueve la caja va primero.
    alertas.sort(key=lambda a: abs(a["impacto_ano_eur"]), reverse=True)
    comparativas.sort(key=lambda c: abs(c["ahorro_ano_eur"]), reverse=True)

    # --- Impacto en la carta (enlace con escandallo), si se aporta
    impacto_carta = []
    carta = datos.get("carta")
    if carta:
        # Diccionario producto -> nuevo €/base y variación
        subida_por_prod = {}
        for a in alertas:
            subida_por_prod[a["producto"].lower()] = a
        for plato in carta:
            nombre_plato = plato.get("plato", "sin-nombre")
            ventas_mes = float(plato.get("ventas_mes", 0) or 0)
            margen_actual = plato.get("margen_actual_eur")
            sobrecoste = 0.0
            detalle = []
            for ing in plato.get("ingredientes", []):
                pnom = ing["producto"].strip().lower()
                cant = float(ing.get("cantidad_base", 0) or 0)  # en base del producto
                a = subida_por_prod.get(pnom)
                if a and cant > 0:
                    delta = (a["precio_ahora"] - a["precio_antes"]) * cant
                    sobrecoste += delta
                    detalle.append({
                        "ingrediente": ing["producto"],
                        "sobrecoste_unidad_eur": round(delta, 4),
                    })
            if sobrecoste > 0:
                fila = {
                    "plato": nombre_plato,
                    "sobrecoste_unidad_eur": round(sobrecoste, 4),
                    "ventas_mes": ventas_mes,
                    "sobrecoste_mes_eur": round(sobrecoste * ventas_mes, 2),
                    "sobrecoste_ano_eur": round(sobrecoste * ventas_mes * 12, 2),
                    "detalle": detalle,
                }
                if margen_actual is not None:
                    ma = float(margen_actual)
                    fila["margen_antes_eur"] = round(ma, 2)
                    fila["margen_despues_eur"] = round(ma - sobrecoste, 2)
                    if ma > 0:
                        fila["margen_perdido_pct"] = round(sobrecoste / ma * 100, 1)
                impacto_carta.append(fila)
        impacto_carta.sort(key=lambda x: x["sobrecoste_ano_eur"], reverse=True)

    # --- Totales
    total_ahorro_cambio = round(sum(c["ahorro_ano_eur"] for c in comparativas), 2)
    total_impacto_subidas = round(
        sum(a["impacto_ano_eur"] for a in alertas if not a["estacional"]), 2)
    total_impacto_carta = round(
        sum(x["sobrecoste_ano_eur"] for x in impacto_carta), 2)

    return {
        "alertas_subida": alertas,
        "comparativa_proveedores": comparativas,
        "impacto_en_carta": impacto_carta,
        "formato_encubierto": formato_sospechoso,
        "errores_datos": errores,
        "totales": {
            "ahorro_anual_si_cambio_al_barato_eur": total_ahorro_cambio,
            "impacto_anual_subidas_no_estacionales_eur": total_impacto_subidas,
            "sobrecoste_anual_en_carta_eur": total_impacto_carta,
        },
        "parametros": {
            "umbral_alerta_pct": umbral,
            "productos_analizados": len(productos),
            "lineas_validas": sum(len(p["registros"]) for p in productos.values()),
        },
    }


# ----------------------------------------------------------------------
# Verificación interna (autocontrol de la propia skill)
# ----------------------------------------------------------------------
def verificar(res):
    avisos = []
    for a in res["alertas_subida"]:
        if a["precio_ahora"] < 0 or a["precio_antes"] < 0:
            avisos.append(f"Precio negativo en {a['producto']}: revisar datos.")
        if a["var_pct"] > 100:
            avisos.append(
                f"{a['producto']}: subida del {a['var_pct']}% — probable error "
                f"de unidad o formato, verifica antes de enseñarlo al cliente.")
    for c in res["comparativa_proveedores"]:
        if c["dif_pct"] > 40:
            avisos.append(
                f"{c['producto']}: {c['dif_pct']}% entre proveedores — comprueba "
                f"que sea EL MISMO producto (calidad/calibre), no dos distintos.")
    sin_consumo = sorted({a["producto"] for a in res["alertas_subida"]
                          if not a.get("consumo_mes_base")}
                         | {c["producto"] for c in res["comparativa_proveedores"]
                            if not c.get("consumo_mes_base")})
    for prod in sin_consumo:
        avisos.append(
            f"{prod}: impacto NO calculable en euros — falta el consumo mensual "
            f"(kg/L/ud al mes). El 0 € que aparece es un hueco de dato, no un "
            f"coste cero: no lo presentes como tal.")
    if res["errores_datos"]:
        avisos.append(f"{len(res['errores_datos'])} línea(s) descartadas por datos "
                      f"incoherentes: no entran en el análisis.")
    return avisos


EJEMPLO = {
    "umbral_alerta_pct": 8.0,
    "volatiles": ["pescado", "marisco", "verdura", "fruta"],
    "lineas": [
        {"producto": "Aceite oliva virgen extra", "familia": "seco",
         "proveedor": "Distribuidora A", "unidad": "garrafa",
         "formato": {"valor": 5, "base": "L"}, "precio": 42.50,
         "fecha": "2026-04-01", "consumo_mes_base": 60},
        {"producto": "Aceite oliva virgen extra", "familia": "seco",
         "proveedor": "Distribuidora A", "unidad": "garrafa",
         "formato": {"valor": 5, "base": "L"}, "precio": 48.00,
         "fecha": "2026-08-01", "consumo_mes_base": 60},
        {"producto": "Aceite oliva virgen extra", "familia": "seco",
         "proveedor": "Mayorista B", "unidad": "L", "precio": 8.90,
         "fecha": "2026-08-01", "consumo_mes_base": 60},
        {"producto": "Merluza fresca", "familia": "pescado",
         "proveedor": "Pescados C", "unidad": "kg", "precio": 11.00,
         "fecha": "2026-04-01", "consumo_mes_base": 40},
        {"producto": "Merluza fresca", "familia": "pescado",
         "proveedor": "Pescados C", "unidad": "kg", "precio": 13.50,
         "fecha": "2026-08-01", "consumo_mes_base": 40},
    ],
    "carta": [
        {"plato": "Merluza a la plancha", "ventas_mes": 120,
         "margen_actual_eur": 9.50,
         "ingredientes": [
             {"producto": "Merluza fresca", "cantidad_base": 0.32}
         ]}
    ],
}


def _autotest():
    """Batería mínima de comprobación aritmética."""
    ok = True

    # 1) Normalización: garrafa 5L a 42,50 € = 8,50 €/L
    px, base = _precio_por_base({"unidad": "garrafa",
                                 "formato": {"valor": 5, "base": "L"},
                                 "precio": 42.50})
    assert base == "L" and abs(px - 8.50) < 1e-6, f"norm garrafa: {px}"

    # 2) IVA: 11,00 € con 10% IVA incluido -> 10,00 € neto
    px2, _ = _precio_por_base({"unidad": "kg", "precio": 11.00,
                               "iva_pct": 10, "precio_lleva_iva": True})
    assert abs(px2 - 10.0) < 1e-6, f"iva: {px2}"

    # 3) Subida aceite: 8,50 -> 9,60 €/L = +12,94%, impacto 60 L/mes
    res = analizar(EJEMPLO)
    aceite = [a for a in res["alertas_subida"]
              if "aceite" in a["producto"].lower()][0]
    assert abs(aceite["var_pct"] - 12.9) < 0.2, f"var aceite: {aceite['var_pct']}"
    # impacto mes = (9.60 - 8.50) * 60 = 66 €/mes -> 792 €/año
    assert abs(aceite["impacto_ano_eur"] - 792.0) < 1.0, aceite["impacto_ano_eur"]

    # 4) Comparativa: Mayorista B a 8,90 vs A a 9,60 -> B más barato
    comp = [c for c in res["comparativa_proveedores"]
            if "aceite" in c["producto"].lower()][0]
    assert comp["mas_barato"] == "Mayorista B", comp["mas_barato"]

    # 5) Merluza estacional: marcada como estacional (no cuenta en total abuso)
    merl = [a for a in res["alertas_subida"]
            if "merluza" in a["producto"].lower()][0]
    assert merl["estacional"] is True, "merluza debería marcarse estacional"

    # 6) Impacto en carta: merluza +2,50 €/kg * 0,32 kg = 0,80 €/plato
    #    * 120 ventas/mes = 96 €/mes -> 1.152 €/año
    ic = res["impacto_en_carta"][0]
    assert abs(ic["sobrecoste_unidad_eur"] - 0.80) < 0.01, ic["sobrecoste_unidad_eur"]
    assert abs(ic["sobrecoste_ano_eur"] - 1152.0) < 1.0, ic["sobrecoste_ano_eur"]

    print("AUTOTEST OK — 6 comprobaciones aritméticas pasadas")
    return ok


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--ejemplo":
        print(json.dumps(EJEMPLO, indent=2, ensure_ascii=False))
        return
    if len(sys.argv) >= 2 and sys.argv[1] == "--autotest":
        _autotest()
        return
    if len(sys.argv) < 2:
        print("Uso: python3 proveedores.py datos.json | --ejemplo | --autotest")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        datos = json.load(f)
    res = analizar(datos)
    res["avisos_verificacion"] = verificar(res)
    print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
