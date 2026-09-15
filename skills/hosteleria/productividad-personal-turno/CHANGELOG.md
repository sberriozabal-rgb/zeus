# CHANGELOG — productividad-personal-turno

## [1.1.1] — 2026-09-15

**Parche de conformidad con la rúbrica.** De 19/20 a 20/20 mecánico (19/20 declarado: el punto 19, URLs verificadas una a una, no se reconfirmó). Fecha del CHANGELOG 1.1.0 pasada de "16-ago-2026" a ISO 2026-08-16: el validador no la reconocía y la versión del metadata quedaba sin fecha asociada. El contenido de oficio no cambia.

## 1.1.0 — 2026-08-16 · auditoría del segundo lote

### Corregido — la franja más cara aparecía como la más eficiente
- `coste/ventas*100 if ventas else 0.0` imprimía **0,0 %** para una franja con horas pagadas y cero venta, colocándola en la tabla como el tramo más eficiente cuando es el más caro que existe. Ahora devuelve `n/d` y la línea se marca `<< HORAS PAGADAS SIN VENTA`.
- El ranking semanal usaba dos centinelas distintos (0 para el peor, 99 para el mejor) que hacían desaparecer esos días de ambos extremos sin avisar. Ahora se apartan y se declaran aparte.
- `scripts/productividad_turno.py` gana `--autotest` con 32 comprobaciones.
