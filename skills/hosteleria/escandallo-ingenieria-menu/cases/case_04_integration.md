# Caso 4 · Integration — encadenado con `comparativa-proveedores`

## Encargo real que escribiría un dueño

> "Me dijiste el mes pasado que el aceite me había subido y que la merluza estaba cara. Vale. ¿Y eso qué me hace en la carta?"

## Cómo se encadena

1. `comparativa-proveedores` ya produjo, sobre albaranes reales, dos subidas verificadas
   entre abril y agosto de 2026 (ejecutables con `python3 scripts/proveedores.py --ejemplo`
   en esa skill):
   - **Aceite de oliva virgen extra**: 8,50 → 9,60 €/L, **+12,9%**, marcada
     **estructural** (no estacional). Impacto por compra: 792 €/año.
   - **Merluza fresca**: 11,00 → 13,50 €/kg, **+22,7%**, marcada **estacional**.
2. `escandallo-ingenieria-menu` toma esos dos precios como nuevo precio de compra sobre la
   misma carta del caso 1 —sin tocar una sola receta, un solo gramaje ni un solo precio de
   venta— y recalcula.

```bash
# la carta del caso 1 con los dos precios de compra actualizados
python3 scripts/escandallo.py datos_con_precios_agosto.json
```

## Qué cambia (ejecutado, mismas recetas, mismos precios de carta)

| | Antes (caso 1) | Después de las subidas |
|---|---|---|
| Food cost teórico de la carta | 32,35% | **33,32%** |
| Merluza a la plancha — coste | 6,37 € | **7,74 €** |
| Merluza a la plancha — margen unitario | 14,54 € | **13,17 €** |
| Merluza a la plancha — food cost | 30,4% | **37,0%** |
| Alcachofa confitada — coste | 3,13 € | 3,20 € |
| Desviación teórico-real | 3,85 puntos | **2,88 puntos** |

## Los dos hallazgos que ninguna de las dos skills ve sola

**1 · La merluza pierde 1,37 € por ración por la compra, no por la receta.** A 165
unidades en el periodo son **226 €/mes**, del orden de 2.700 €/año si el ritmo de venta se
mantiene. Y como `comparativa-proveedores` marcó esa subida como **estacional**, la acción
no es renegociar con el proveedor: es cambiar el pescado del día o mover el precio del plato
hasta el cambio de temporada. Un informe de carta que no supiera el origen de la subida
habría recomendado atacar el porcionado de un plato cuyo porcionado está bien.

**2 · La desviación baja de 3,85 a 2,88 puntos sin que nada haya mejorado en la cocina.**
El food cost real del periodo sigue siendo el mismo 36,2%; lo que subió es el teórico,
porque la materia prima cuesta más. Es decir: **una subida de proveedores maquilla el
semáforo de control**. Un local con un problema real de porcionado puede ver cómo su
desviación "mejora" mientras gana menos dinero. Esto se declara en el apartado 1 del
informe con esta frase exacta:

> La desviación baja de 3,85 a 2,88 puntos, pero no porque la cocina ejecute mejor: el
> teórico ha subido por las compras. El problema de porcionado sigue donde estaba.

## Formato de entrega en la integración

El informe estándar más una sección **"7. Lo que viene de la compra, no de la carta"**, que
solo aparece cuando el dueño aporta o referencia una salida de `comparativa-proveedores`.
Cada plato afectado se lista con su sobrecoste por ración, su euro al mes y la etiqueta
**estacional / estructural** heredada de la otra skill, porque decide la acción.

Si no hay informe de compras, la sección no aparece y ningún precio de compra se toca.

## Por qué importa

Es lo que convierte seis análisis sueltos en un sistema: las dos skills comparten unidad
(euros por ración y por año), comparten la distinción estacional/estructural y se citan sin
inventar nada. La comparativa sabe qué subió; el escandallo sabe qué plato lo paga. Ninguna
de las dos, sola, dice qué hacer el lunes.
