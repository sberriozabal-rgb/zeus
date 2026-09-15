# Caso 4 · Integration (encadenado con otra skill)

## Encargo real que escribiría un dueño

> "El mes pasado me hicisteis el escandallo y me salió una desviación de casi cuatro puntos entre lo que dice la receta y lo que dice el inventario. Llevo desde entonces apretando a la cocina con el porcionado y no baja. Ahora me sale que el aceite y la merluza me han subido. ¿Puede ser que parte de esa desviación no sea de la cocina?"

## Con qué se encadena

`escandallo-ingenieria-menu` (`metadata.enlaza_con`), en los dos sentidos.

## El hueco que cierra la integración

Un escandallo se hace con los precios de compra del día en que se hizo. A partir de ahí envejece en silencio: la receta no cambia, los gramos no cambian, pero el albarán sí. El food cost **teórico** sigue calculándose con precios viejos mientras el **real** —que sale de compras contra ventas— ya lleva los nuevos. La diferencia entre ambos se llama desviación, y el escandallo la lee como problema de control: porcionado, mermas, roturas, invitaciones.

**Parte de esa desviación puede ser, simplemente, que la compra ha subido.** Ninguna de las dos skills lo ve sola: la de compras sabe cuánto ha subido pero no qué le hace eso a la desviación; la de escandallo ve la desviación pero no sabe que sus precios están viejos.

## Cómo se encadena, paso a paso

1. `comparativa-proveedores` entrega dos subidas **verificadas** sobre la carta de prueba del escandallo: aceite de oliva **+12,9%** (estructural) y merluza **+22,7%** (estacional). Ver `cases/case_01_happy_path.md`.
2. Al escandallo entra **el porcentaje, no el euro absoluto**. El aceite del albarán es una garrafa de virgen extra a 9,60 €/L; el del escandallo es "Aceite oliva" a 9,20 €/kg, otra referencia y otra base. Lo que viaja entre las dos skills es la **variación**: 9,20 × 1,129 = **10,39 €/kg**; merluza entera 12,50 × 1,227 = **15,34 €/kg**.
3. Se recalcula la carta ya escandallada con esos precios y **nada más**: mismos gramajes, mismos rendimientos, mismas mermas, mismas ventas, mismo food cost real aportado (36,20%).

## Qué entrega este caso

Cifras reales, ejecutadas sobre `assets/plantilla-datos.json` de `escandallo-ingenieria-menu` con los dos precios actualizados:

```markdown
## 2 bis. Cuánto de tu desviación es compra, no cocina (requiere escandallo previo)
Tu informe de ingeniería de menú, con los precios de compra de julio:
  food cost teórico 32,35% · real 36,20% · desviación 3,85 puntos → banda de aviso.

El mismo informe, con los precios de compra de agosto y sin tocar nada más:
  food cost teórico 33,32% · real 36,20% · desviación 2,88 puntos.

Coste de materia prima del periodo: 7.700,48 € → 7.930,80 € (+230,32 €/mes).
De los 3,85 puntos de desviación que te llevas persiguiendo, 0,97 puntos —una
cuarta parte— no son de la cocina: son de la compra. Los otros 2,88 sí siguen ahí,
y siguen siendo porcionado o merma.

Y el plato que se lo lleva todo, tu caballo de batalla:
| Plato | Coste antes | Coste ahora | Margen antes | Margen ahora | FC% antes | FC% ahora |
|---|---|---|---|---|---|---|
| Merluza a la plancha | 6,37 € | 7,74 € | 14,54 € | 13,17 € | 30,4% | 37,0% |
| Alcachofa confitada | 3,13 € | 3,20 € | 9,60 € | 9,52 € | 24,6% | 25,2% |

La merluza pierde 1,37 € de margen por ración. Con 165 raciones al mes son 226 €/mes
y 2.713 €/año, y su food cost sube casi siete puntos sin que nadie haya tocado la
receta ni el precio de carta.
```

## Reglas de la integración

- **Entre las dos skills viaja el porcentaje, nunca el euro.** El producto del albarán y el ingrediente del escandallo casi nunca son la misma referencia —"merluza fresca" a 13,50 €/kg del pescadero contra "merluza entera" a 12,50 €/kg de la ficha técnica—, y sustituir un precio por el otro mete un error de referencia disfrazado de actualización.
- **Solo entran las subidas verificadas**, las que ya pasaron el filtro de normalización y de "no es un producto distinto". Una subida sospechosa de error de unidad no se propaga a la carta.
- **La estacional también entra en el recálculo, aunque no cuente como sobrecoste evitable.** Son dos cuentas distintas: al proveedor de merluza no se le persigue en agosto, pero el plato cuesta hoy lo que cuesta hoy. Confundirlas es el error contrario al antipatrón nº 2.
- **El aceite de fritura amortizado no se toca** (2,10 €/kg en la ficha): es aceite usado con su propio criterio de amortización, no la referencia que subió. Se declara que se dejó fuera.
- **La desviación la recalcula el escandallo, no esta skill.** Aquí solo se entregan los precios nuevos. Cada skill manda en su cifra.
- En sentido contrario: si el recálculo deja un plato con el coste por encima del precio de venta, eso es un hallazgo del escandallo, y la decisión de subir precio o retirar el plato sale de allí, no de aquí.

## Por qué importa

Porque cambia el diagnóstico, no el decorado. El dueño llevaba un mes apretando a la cocina por una desviación de la que **una cuarta parte no era suya**, y la ha estado buscando donde no estaba. Ese hallazgo no lo produce ninguna de las dos skills por separado: el escandallo no sabe que sus precios envejecieron, y la comparativa no sabe qué hace un +12,9% dentro de una ficha técnica. Es la diferencia entre un sistema y seis análisis sueltos vendidos juntos.

## Comprobación

```bash
# 1. Las dos subidas, del motor de esta skill
python3 scripts/proveedores.py --ejemplo > datos.json && python3 scripts/proveedores.py datos.json

# 2. La carta con los precios viejos
python3 ../escandallo-ingenieria-menu/scripts/escandallo.py \
        ../escandallo-ingenieria-menu/assets/plantilla-datos.json

# 3. La misma carta con "Merluza entera" a 15.34 y "Aceite oliva"/"Aceite confitado"
#    a 10.39 — desviación 2,88 puntos.
```
