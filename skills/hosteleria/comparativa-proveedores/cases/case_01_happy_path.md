# Caso 1 · Happy path

## Encargo real que escribiría un dueño

> "Te paso los albaranes de los tres proveedores de abril y de agosto. Dime qué me ha subido, quién me lo tiene más barato y qué platos se lo están comiendo."

## Entrada

El juego de datos de fábrica, reproducible con `python3 scripts/proveedores.py --ejemplo`: **5 líneas · 3 proveedores · 2 productos · 2 fechas (01-04-2026 y 01-08-2026) · consumo mensual declarado · carta aportada**.

- **Aceite de oliva virgen extra**, familia `seco` (no volátil): Distribuidora A en garrafa de 5 L a 42,50 € en abril y a 48,00 € en agosto; Mayorista B por litro suelto a 8,90 € en agosto. Consumo 60 L/mes.
- **Merluza fresca**, familia `pescado` (volátil): Pescados C a 11,00 €/kg en abril y 13,50 €/kg en agosto. Consumo 40 kg/mes.
- **Carta**: "Merluza a la plancha", 120 ventas/mes, 0,32 kg de merluza por ración, margen actual 9,50 €.

## Salida esperada

Ejecutado con `python3 scripts/proveedores.py datos.json`, cifras reales del motor:

1. **Las dos trampas desactivadas antes de restar nada.** La garrafa de 5 L a 48,00 € es **9,60 €/L**; la de abril, **8,50 €/L**. El litro suelto de Mayorista B es 8,90 €/L. Sin normalizar, el número grande (48,00 contra 8,90) habría mandado al dueño a cambiar de proveedor por el motivo equivocado y con la cifra equivocada.

2. **Dos alertas, ordenadas por euros y no por porcentaje**:

| Producto | Proveedor | Antes → Ahora | % | €/año | ¿Estacional? |
|---|---|---|---|---|---|
| Merluza fresca | Pescados C | 11,00 → 13,50 €/kg | +22,7% | 1.200 € | **Sí** |
| Aceite oliva virgen extra | Distribuidora A | 8,50 → 9,60 €/L | +12,9% | **792 €** | No |

   **El hallazgo de oficio del caso**: la subida que más euros mueve —1.200 €/año de merluza— es la que **no se persigue**. Familia `pescado`, volátil, marcada estacional y **fuera del sobrecoste evitable**. El titular del informe es 792 €/año de aceite, no 1.992 €. Un informe que sumara las dos habría prometido un ahorro que el cambio de temporada desmiente solo, que es el antipatrón nº 2 de la skill.

3. **Comparativa de hoy**: el aceite lo tiene más barato **Mayorista B a 8,90 €/L** contra los 9,60 €/L de Distribuidora A. Diferencia 7,9% —muy por debajo del 40-50% de sospecha de producto distinto—, **504 €/año** de ahorro con 60 L/mes. Supera el umbral de 500 €/año: merece pedir oferta formal. La merluza no aparece en comparativa: un solo proveedor, y se dice.

4. **Impacto en la carta**: la merluza sube 2,50 €/kg × 0,32 kg = **0,80 € por ración**. Con 120 ventas/mes son 96 €/mes y **1.152 €/año en un solo plato**. El margen de "Merluza a la plancha" baja de 9,50 € a 8,70 €: **8,4% del margen del plato, sin haber tocado la receta ni el precio de carta**.

5. **Totales del motor**: sobrecoste estructural 792 €/año · ahorro por cambio 504 €/año · sobrecoste en carta 1.152 €/año. `errores_datos`: vacío. `avisos_verificacion`: vacío. `formato_encubierto`: vacío — no hay dos periodos con el mismo precio de línea y distinto peso.

## Por qué es el caso central

Cubre el flujo completo con datos limpios: normalización de formato, separación de estacional y estructural antes de sumar, comparativa entre proveedores con la diferencia por debajo del umbral de sospecha, y el cruce con la carta que convierte un porcentaje en margen perdido por plato. Es el camino de la mayoría de las instalaciones, y es el caso donde se ve que **la subida más grande y la subida que se ataca no son la misma**.

## Comprobación

```bash
python3 scripts/proveedores.py --autotest    # debe imprimir "AUTOTEST OK — 6 comprobaciones"
python3 scripts/proveedores.py --ejemplo > datos.json && python3 scripts/proveedores.py datos.json
```
