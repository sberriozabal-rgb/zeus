# CHANGELOG — productividad-personal-turno

## 1.1.0 — 16-ago-2026 · auditoría del segundo lote

### Corregido — la franja más cara aparecía como la más eficiente
- `coste/ventas*100 if ventas else 0.0` imprimía **0,0 %** para una franja con horas pagadas y cero venta, colocándola en la tabla como el tramo más eficiente cuando es el más caro que existe. Ahora devuelve `n/d` y la línea se marca `<< HORAS PAGADAS SIN VENTA`.
- El ranking semanal usaba dos centinelas distintos (0 para el peor, 99 para el mejor) que hacían desaparecer esos días de ambos extremos sin avisar. Ahora se apartan y se declaran aparte.
- `scripts/productividad_turno.py` gana `--autotest` con 32 comprobaciones.
