#!/usr/bin/env python3
"""
escalar_receta.py — Escala una ficha de receta-estandar (formato JSON del
contrato de interfaz) a un nuevo número de porciones o por un factor directo.

Corrige el antipatrón "la escala rota" (SKILL.md, ANTIPATRONES #3): multiplica
SOLO las cantidades de ingredientes en gramos/mililitros. Deliberadamente NO
toca tiempos de cocción, temperaturas ni pasos de procedimiento, porque esos
NO escalan linealmente — eso lo decide un cocinero, no un script.

Uso:
    python3 escalar_receta.py --json receta.json --porciones 50
    python3 escalar_receta.py --json receta.json --factor 12.5
    python3 escalar_receta.py --ejemplo

Sin dependencias externas. Python 3.9+.
"""

import argparse
import json
import sys


EJEMPLO_RECETA = {
    "plato": "Salsa madre de tomate",
    "rendimiento_total": {"porciones": 4, "peso_g": 800},
    "porcion_individual_g": 200,
    "tolerancia_porcion_pct": 10,
    "ingredientes": [
        {"nombre": "tomate concassé", "cantidad": 600, "unidad": "g", "marca": "CONFIRMADO"},
        {"nombre": "cebolla picada", "cantidad": 100, "unidad": "g", "marca": "CONFIRMADO"},
        {"nombre": "aceite de oliva", "cantidad": 30, "unidad": "ml", "marca": "CONFIRMADO"},
        {"nombre": "sal", "cantidad": 5, "unidad": "g", "marca": "ESTIMADO"},
    ],
    "puntos_criticos_haccp": [
        {"paso": 3, "temp_min_c": 74, "metodo_verificacion": "sonda"}
    ],
    "mise_en_place": ["cuchillo de chef", "olla mediana", "tabla de picar"],
    "conservacion": "refrigerar a ≤4°C, consumir en 3 días",
    "estado": "ACORDADO",
}


def escalar(receta, factor):
    """Devuelve una copia de la receta con ingredientes y rendimiento
    escalados por `factor`. No modifica tiempos, temperaturas ni pasos."""
    nueva = json.loads(json.dumps(receta))  # copia profunda sin dependencias

    porciones_orig = nueva.get("rendimiento_total", {}).get("porciones")
    peso_orig = nueva.get("rendimiento_total", {}).get("peso_g")

    if porciones_orig:
        nueva["rendimiento_total"]["porciones"] = round(porciones_orig * factor, 2)
    if peso_orig:
        nueva["rendimiento_total"]["peso_g"] = round(peso_orig * factor, 1)

    for ing in nueva.get("ingredientes", []):
        if isinstance(ing.get("cantidad"), (int, float)):
            ing["cantidad"] = round(ing["cantidad"] * factor, 2)

    nueva["_aviso_escalado"] = (
        f"Escalado por factor {factor:.4f}. SOLO se multiplicaron cantidades "
        f"de ingredientes y rendimiento total. Tiempos de cocción, "
        f"temperaturas y ratios de reducción NO se escalaron automáticamente "
        f"— revisar el antipatrón 'la escala rota' antes de producir "
        f"(SKILL.md, sección ANTIPATRONES #3)."
    )
    nueva["estado"] = "BORRADOR"  # una receta recién escalada exige reverificación
    return nueva


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", help="Ruta al archivo JSON de la receta a escalar")
    parser.add_argument("--porciones", type=float, help="Número de porciones destino")
    parser.add_argument("--factor", type=float, help="Factor de multiplicación directo")
    parser.add_argument("--ejemplo", action="store_true", help="Imprime una receta de ejemplo y su escalado a 50 porciones")
    args = parser.parse_args()

    if args.ejemplo:
        print("--- Receta original ---")
        print(json.dumps(EJEMPLO_RECETA, ensure_ascii=False, indent=2))
        factor = 50 / EJEMPLO_RECETA["rendimiento_total"]["porciones"]
        print("\n--- Escalada a 50 porciones ---")
        print(json.dumps(escalar(EJEMPLO_RECETA, factor), ensure_ascii=False, indent=2))
        return

    if not args.json:
        print("Error: falta --json (o usa --ejemplo para ver una demostración).", file=sys.stderr)
        sys.exit(1)

    with open(args.json, "r", encoding="utf-8") as f:
        receta = json.load(f)

    if args.factor:
        factor = args.factor
    elif args.porciones:
        porciones_orig = receta.get("rendimiento_total", {}).get("porciones")
        if not porciones_orig:
            print("Error: la receta no declara rendimiento_total.porciones; usa --factor en su lugar.", file=sys.stderr)
            sys.exit(1)
        factor = args.porciones / porciones_orig
    else:
        print("Error: especifica --porciones o --factor.", file=sys.stderr)
        sys.exit(1)

    resultado = escalar(receta, factor)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
