#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
respuesta-resenas · motor de cálculo determinista
====================================================

Convierte un export de reseñas en tres cosas que un dueño de restaurante
puede ejecutar el lunes:

  1) TENDENCIA DE ESTRELLAS    — media actual y su traducción a un rango
                                  de impacto en ingresos (referencia de mercado).
  2) PATRONES OPERATIVOS        — motivos repetidos ≥3 veces en 60 días,
                                  no ruido de "clientes difíciles" sueltos.
  3) CLASIFICACIÓN POR RESEÑA   — positiva / negativa con motivo / negativa
                                  injusta, lista para elegir plantilla de respuesta.

Principio de oficio: el impacto en ingresos es siempre un RANGO con fuente
declarada (Luca/HBS, +5% a +9% por estrella en independientes), nunca una
promesa de resultado. El script no razona ni inventa: si falta un dato
(fecha, motivo), lo deja como hueco declarado.

Uso:
    python3 resenas.py datos.json
    python3 resenas.py --ejemplo      # imprime el formato de entrada
    python3 resenas.py --autotest     # ejecuta la batería de comprobación

Sin dependencias externas. Python 3.9+.
"""

import json
import sys
from datetime import datetime, timedelta

# ----------------------------------------------------------------------
# Referencias de mercado (ver references/umbrales-resenas.md)
# ----------------------------------------------------------------------
IMPACTO_INGRESOS_MIN_PCT = 5.0   # por +1 estrella de media, en independientes
IMPACTO_INGRESOS_MAX_PCT = 9.0
UMBRAL_PATRON_MENCIONES = 3
UMBRAL_PATRON_DIAS = 60

# ----------------------------------------------------------------------
# Marcadores de escalado legal — reseñas que NO se responden con plantilla
#
# Una respuesta pública mal redactada a una acusación de intoxicación o a
# una amenaza legal puede leerse como reconocimiento de responsabilidad y
# acabar citada. Estas reseñas se separan del lote, no se autorredactan, y
# se derivan a un profesional colegiado antes de publicar nada.
# ----------------------------------------------------------------------
MARCADORES_ESCALADO = {
    "salud": [
        "intoxic", "intoxicación", "intoxicacion", "salmonel", "listeri",
        "anisakis", "e. coli", "gastroenteritis", "nos sentó mal",
        "nos sento mal", "me sentó mal", "me sento mal", "vomit", "diarrea",
        "urgencias", "hospital", "ambulancia", "alergia", "alérgen", "alergen",
        "anafila", "gluten", "envenenad",
    ],
    "legal": [
        "abogado", "abogada", "denuncia", "denunciar", "demanda", "demandar",
        "juzgado", "demandado", "hoja de reclamacion", "hoja de reclamación",
        "reclamación formal", "reclamacion formal", "inspección de sanidad",
        "inspeccion de sanidad", "sanidad", "consumo", "profeco", "acciones legales",
    ],
    "personas": [
        "agredi", "agresión", "agresion", "me pegó", "me pego", "insultó",
        "insulto", "racis", "discrimin", "acoso", "policía", "policia",
        "robo", "me robaron",
    ],
}


def _parse_fecha(f):
    if not f:
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(f.strip(), fmt).date()
        except (ValueError, AttributeError):
            continue
    return None


def _clasificar(resena):
    """Devuelve la categoría de una reseña: positiva, negativa_con_motivo,
    negativa_injusta, mixta. Basado en estrellas + presencia de motivo."""
    estrellas = resena.get("estrellas")
    if estrellas is None:
        return "sin-clasificar"
    estrellas = float(estrellas)
    motivo = (resena.get("motivo") or "").strip().lower()
    texto = (resena.get("texto") or "").strip()

    if estrellas >= 4:
        return "positiva"
    if estrellas <= 2:
        if motivo and motivo != "injusta" and motivo != "sospechosa":
            return "negativa_con_motivo"
        if not texto or motivo in ("injusta", "sospechosa", ""):
            return "negativa_injusta" if motivo in ("injusta", "sospechosa") else "negativa_sin_motivo_declarado"
        return "negativa_con_motivo"
    # estrellas == 3
    return "mixta"


def _escalado_legal(resena):
    """Devuelve la lista de motivos de escalado detectados en el texto de una
    reseña. Lista vacía = se puede redactar respuesta con plantilla.

    Deliberadamente sobreincluyente: un falso positivo cuesta que un humano
    lea la reseña; un falso negativo cuesta una respuesta pública que puede
    citarse como reconocimiento de responsabilidad."""
    texto = (resena.get("texto") or "").lower()
    motivo = (resena.get("motivo") or "").lower()
    campo = f"{texto} {motivo}"
    motivos = []
    for categoria, marcadores in MARCADORES_ESCALADO.items():
        if any(m in campo for m in marcadores):
            motivos.append(categoria)
    return motivos


def analizar(datos):
    """datos: dict con 'resenas' (obligatorio), 'umbral_patron_menciones'
    y 'umbral_patron_dias' (opcionales). Devuelve dict de resultados."""

    resenas = datos.get("resenas", [])
    umbral_menciones = int(datos.get("umbral_patron_menciones", UMBRAL_PATRON_MENCIONES))
    umbral_dias = int(datos.get("umbral_patron_dias", UMBRAL_PATRON_DIAS))
    errores = []

    if not resenas:
        return {"error": "Sin reseñas en la entrada. No se puede calcular nada.", "totales": {}}

    clasificadas = []
    estrellas_validas = []
    for i, r in enumerate(resenas):
        if r.get("estrellas") is None:
            errores.append(f"Reseña {i}: falta el campo 'estrellas'. Descartada del cálculo de media.")
            continue
        cat = _clasificar(r)
        escalado = _escalado_legal(r)
        fecha = _parse_fecha(r.get("fecha"))
        if not fecha:
            errores.append(f"Reseña {i}: sin fecha válida. Se incluye en la media pero no en la detección de patrones por periodo.")
        clasificadas.append({
            "indice": i,
            "categoria": cat,
            "estrellas": float(r["estrellas"]),
            "fecha": fecha,
            "motivo": (r.get("motivo") or "").strip().lower() or None,
            "motivo_inferido": r.get("motivo") is None,
            "texto": r.get("texto", ""),
            "escalado_legal": escalado,
        })
        if escalado:
            errores.append(
                f"Reseña {i}: ESCALADO OBLIGATORIO ({', '.join(escalado)}). "
                f"No se redacta respuesta con plantilla: derivar a profesional "
                f"colegiado antes de publicar nada.")
        estrellas_validas.append(float(r["estrellas"]))

    if not estrellas_validas:
        return {"error": "Ninguna reseña tiene el campo 'estrellas' válido.", "totales": {}}

    media_actual = round(sum(estrellas_validas) / len(estrellas_validas), 2)

    # --- Detección de patrones: agrupa negativas por motivo, cuenta
    # menciones dentro de cualquier ventana de umbral_dias días.
    negativas = [c for c in clasificadas
                 if c["categoria"] in ("negativa_con_motivo", "negativa_sin_motivo_declarado")
                 and c["motivo"]]
    por_motivo = {}
    for c in negativas:
        por_motivo.setdefault(c["motivo"], []).append(c)

    patrones = []
    for motivo, items in por_motivo.items():
        con_fecha = [c for c in items if c["fecha"]]
        sin_fecha = [c for c in items if not c["fecha"]]
        con_fecha.sort(key=lambda c: c["fecha"])
        # Ventana deslizante simple: para cada item, cuenta cuántos caen
        # dentro de umbral_dias desde el primero de una racha.
        max_en_ventana = 0
        mejor_ventana = None
        for start_idx, start in enumerate(con_fecha):
            fin_ventana = start["fecha"] + timedelta(days=umbral_dias)
            en_ventana = [c for c in con_fecha[start_idx:] if c["fecha"] <= fin_ventana]
            if len(en_ventana) > max_en_ventana:
                max_en_ventana = len(en_ventana)
                mejor_ventana = (start["fecha"], en_ventana[-1]["fecha"])
        total_menciones = len(items)
        # No confundir "no llega al umbral con fechas confirmadas" con
        # "no es patrón": si hay menciones sin fecha del MISMO motivo, el
        # total podría alcanzar el umbral y el hueco de dato lo estaría
        # ocultando. Se declara la ambigüedad en vez de decidir en silencio.
        podria_ser_patron_con_huecos = (
            not (max_en_ventana >= umbral_menciones)
            and (max_en_ventana + len(sin_fecha)) >= umbral_menciones
            and len(sin_fecha) > 0
        )
        es_patron = max_en_ventana >= umbral_menciones
        patrones.append({
            "motivo": motivo,
            "menciones_totales": total_menciones,
            "menciones_con_fecha_valida": len(con_fecha),
            "menciones_sin_fecha": len(sin_fecha),
            "menciones_max_en_ventana": max_en_ventana,
            "ventana_dias": umbral_dias,
            "periodo_ventana": [str(mejor_ventana[0]), str(mejor_ventana[1])] if mejor_ventana else None,
            "es_patron_operativo": es_patron,
            "posible_patron_oculto_por_fecha_faltante": podria_ser_patron_con_huecos,
        })
    patrones.sort(key=lambda p: p["menciones_max_en_ventana"], reverse=True)

    # --- Impacto estimado: rango de referencia de mercado, no promesa
    escenario_mejora_estrellas = float(datos.get("escenario_mejora_estrellas", 0.5))
    impacto_min_pct = round(IMPACTO_INGRESOS_MIN_PCT * escenario_mejora_estrellas, 2)
    impacto_max_pct = round(IMPACTO_INGRESOS_MAX_PCT * escenario_mejora_estrellas, 2)

    conteo_categorias = {}
    for c in clasificadas:
        conteo_categorias[c["categoria"]] = conteo_categorias.get(c["categoria"], 0) + 1

    return {
        "media_actual_estrellas": media_actual,
        "total_resenas_analizadas": len(clasificadas),
        "conteo_por_categoria": conteo_categorias,
        "patrones_detectados": patrones,
        "patrones_sobre_umbral": [p for p in patrones if p["es_patron_operativo"]],
        "escenario": {
            "mejora_estrellas_supuesta": escenario_mejora_estrellas,
            "impacto_ingresos_rango_pct": [impacto_min_pct, impacto_max_pct],
            "fuente": "Luca / Harvard Business School — +5% a +9% por +1 estrella, solo en restaurantes independientes",
            "nota": "Esto es un escenario de referencia de mercado, NO una promesa de resultado económico.",
        },
        "resenas_para_escalar": [
            {"indice": c["indice"], "estrellas": c["estrellas"],
             "motivos_escalado": c["escalado_legal"],
             "que_hacer": "No publicar respuesta redactada por esta skill. "
                          "Derivar a profesional colegiado. Si hay riesgo sanitario "
                          "real, la prioridad es el protocolo del local, no la reseña."}
            for c in clasificadas if c["escalado_legal"]
        ],
        "clasificacion_detalle": [
            {"indice": c["indice"], "categoria": c["categoria"], "estrellas": c["estrellas"],
             "motivo": c["motivo"], "motivo_inferido": c["motivo_inferido"],
             "escalado_legal": c["escalado_legal"],
             "redactar_respuesta": not c["escalado_legal"]}
            for c in clasificadas
        ],
        "errores_datos": errores,
    }


def verificar(res):
    avisos = []
    if res.get("error"):
        avisos.append(res["error"])
        return avisos
    if res["media_actual_estrellas"] < 1 or res["media_actual_estrellas"] > 5:
        avisos.append(f"Media de {res['media_actual_estrellas']} fuera de rango 1-5: revisa los datos de entrada.")
    sin_clasificar = res["conteo_por_categoria"].get("sin-clasificar", 0)
    if sin_clasificar:
        avisos.append(f"{sin_clasificar} reseña(s) sin clasificar por falta de estrellas.")
    if res.get("resenas_para_escalar"):
        idx = ", ".join(str(r["indice"]) for r in res["resenas_para_escalar"])
        avisos.append(
            f"ESCALADO LEGAL: {len(res['resenas_para_escalar'])} reseña(s) (índice {idx}) "
            f"mencionan salud, amenaza legal o agresión. NO se les redacta respuesta "
            f"con plantilla. Se derivan a profesional colegiado antes de publicar nada. "
            f"Ver 'Límites' en SKILL.md.")
    if res["errores_datos"]:
        avisos.append(f"{len(res['errores_datos'])} aviso(s) de datos incompletos o escalados — ver 'errores_datos'.")
    if not res["patrones_sobre_umbral"] and res["patrones_detectados"]:
        avisos.append("Ningún motivo negativo supera el umbral de patrón (3 en 60 días): tratar como ruido normal, no priorizar corrección operativa urgente.")
    ocultos = [p["motivo"] for p in res["patrones_detectados"] if p.get("posible_patron_oculto_por_fecha_faltante")]
    if ocultos:
        avisos.append(
            f"Posible patrón oculto por falta de fecha en algunas reseñas: {', '.join(ocultos)}. "
            f"Con las fechas confirmadas no llega al umbral, pero sumando las reseñas sin fecha "
            f"del mismo motivo SÍ lo alcanzaría. Pide las fechas exactas antes de descartarlo como ruido.")
    return avisos


EJEMPLO = {
    "escenario_mejora_estrellas": 0.5,
    "resenas": [
        {"estrellas": 5, "fecha": "2026-06-01", "texto": "Genial, el arroz espectacular"},
        {"estrellas": 1, "fecha": "2026-06-05", "motivo": "tiempo_espera", "texto": "Esperamos 45 minutos por la cena"},
        {"estrellas": 2, "fecha": "2026-06-20", "motivo": "tiempo_espera", "texto": "Mesa lista tarde otra vez, un sábado"},
        {"estrellas": 1, "fecha": "2026-07-10", "motivo": "tiempo_espera", "texto": "Mismo problema, sábado noche"},
        {"estrellas": 4, "fecha": "2026-06-15", "texto": "Muy buena atención"},
        {"estrellas": 2, "fecha": "2026-06-25", "motivo": "precio", "texto": "Caro para lo que ofrece"},
        {"estrellas": 3, "fecha": "2026-07-01", "texto": "Bien pero nada especial"},
    ],
}


def _autotest():
    """Batería mínima de comprobación aritmética."""
    res = analizar(EJEMPLO)

    # 1) Media: (5+1+2+1+4+2+3)/7 = 18/7 = 2.5714... -> 2.57
    assert abs(res["media_actual_estrellas"] - 2.57) < 0.01, res["media_actual_estrellas"]

    # 2) Patrón "tiempo_espera": 3 menciones (2026-06-05, 06-20, 07-10),
    #    dentro de una ventana de 60 días desde 06-05 hasta 08-04 -> las 3 caben
    tiempo_espera = [p for p in res["patrones_detectados"] if p["motivo"] == "tiempo_espera"][0]
    assert tiempo_espera["menciones_totales"] == 3, tiempo_espera["menciones_totales"]
    assert tiempo_espera["menciones_max_en_ventana"] == 3, tiempo_espera["menciones_max_en_ventana"]
    assert tiempo_espera["es_patron_operativo"] is True

    # 3) Patrón "precio": solo 1 mención -> no es patrón
    precio = [p for p in res["patrones_detectados"] if p["motivo"] == "precio"][0]
    assert precio["menciones_totales"] == 1
    assert precio["es_patron_operativo"] is False

    # 4) Solo un patrón sobre el umbral (tiempo_espera)
    assert len(res["patrones_sobre_umbral"]) == 1
    assert res["patrones_sobre_umbral"][0]["motivo"] == "tiempo_espera"

    # 5) Clasificación: 2 positivas (5,4), 3 negativas con motivo (1,2,1 con
    #    motivo tiempo_espera/precio), 1 mixta (3 estrellas), 1 negativa (2,
    #    precio) -> comprobamos conteo total = 7
    total_clasificadas = sum(res["conteo_por_categoria"].values())
    assert total_clasificadas == 7, total_clasificadas

    # 6) Escenario de impacto: mejora 0.5 estrellas -> rango 2.5% a 4.5%
    assert abs(res["escenario"]["impacto_ingresos_rango_pct"][0] - 2.5) < 0.01
    assert abs(res["escenario"]["impacto_ingresos_rango_pct"][1] - 4.5) < 0.01

    print("AUTOTEST OK — 6 comprobaciones aritméticas pasadas")
    return True


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--ejemplo":
        print(json.dumps(EJEMPLO, indent=2, ensure_ascii=False))
        return
    if len(sys.argv) >= 2 and sys.argv[1] == "--autotest":
        _autotest()
        return
    if len(sys.argv) < 2:
        print("Uso: python3 resenas.py datos.json | --ejemplo | --autotest")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        datos = json.load(f)
    res = analizar(datos)
    res["avisos_verificacion"] = verificar(res)
    print(json.dumps(res, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
