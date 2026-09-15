# Caso 2 · Edge case

## Encargo real que escribiría un chef

> "El problema no es un plato, es la salsa. Hago una salsa de tomate madre en
> marmita para toda la semana y de ahí salen seis cosas: la pizza, los canelones,
> el pollo a la cazadora, la lasaña, las albóndigas y la base de la sopa. Cada
> uno le mete algo distinto. Si te escribo seis recetas te vas a volver loco y yo
> también. ¿Cómo lo hago?"

## Entrada

| Dato | Valor aportado | Estado |
|---|---|---|
| Preparación base | Salsa de tomate madre, producción semanal en marmita | CONFIRMADO |
| Rendimiento de la base | "una marmita" — sin peso ni porciones | AMBIGUO |
| Platos derivados | 6, nombrados | CONFIRMADO |
| Cantidad de base por derivado | No aportada | FALTA |
| Ajuste propio de cada derivado | Mencionado, no descrito | FALTA |
| País de operación | No declarado | FALTA |

**Lo que hace raro este caso:** la unidad de trabajo de la skill es "un plato",
y aquí la unidad real es **una preparación que no se sirve nunca sola**. Un motor
ingenuo hace una de dos cosas malas: escribe seis fichas que repiten la salsa
completa seis veces (y cuando el chef cambie la salsa, cinco fichas quedan
mintiendo), o escribe una ficha de salsa suelta que no dice para qué sirve y
nadie usa.

## Salida esperada — completa

### Decisión estructural, declarada en la entrega

**Una ficha madre + una tabla de usos derivados. No seis fichas.** Razón escrita
en la propia entrega, no en la cabeza de quien la hizo: la salsa se produce una
vez y se consume seis veces; si su gramaje vive en seis documentos, diverge en
tres semanas y nadie sabe cuál es la buena. La ficha madre es la fuente única.

### Ficha madre — `Salsa de tomate madre`

Se entrega la ficha completa según la plantilla de `SKILL.md § Salida`, con dos
particularidades:

1. **El rendimiento se resuelve, no se deja en blanco.** El chef dice "una
   marmita". La skill pregunta **una** cosa (dentro del límite de 4): el peso o
   volumen que sale de esa marmita. Si el chef no lo sabe, la ficha declara
   `rendimiento_total: [PENDIENTE — PESAR LA PRODUCCIÓN DE UNA MARMITA]` y fija
   la **porción de referencia en 100 g**, porque sin una unidad de referencia la
   tabla de usos derivados no se puede escribir. Ese es el truco: no hace falta
   saber cuánto sale la marmita para saber cuánta salsa lleva un canelón.
2. **La porción individual no es una ración de comensal**, es la unidad de
   transferencia hacia los derivados. Se declara explícitamente para que
   `escandallo-ingenieria-menu` no la confunda con una ración vendible y le
   asigne un precio.

### Tabla de usos derivados — la pieza nueva

| Plato derivado | Salsa madre por ración | Ajuste propio del derivado | Ficha propia |
|---|---|---|---|
| Pizza margarita | 80 g | Sin ajuste; se usa tal cual, en frío sobre la masa | `pizza-margarita` |
| Canelones | 120 g | + 40 ml de nata y nuez moscada, montado en caliente | `canelones` |
| Pollo a la cazadora | 150 g | + 30 ml de vino blanco reducido, + laurel | `pollo-cazadora` |
| Lasaña | 140 g | + carne del sofrito de la casa, sin más líquido | `lasana` |
| Albóndigas | 130 g | + 50 ml de caldo, cocción conjunta 12 min | `albondigas` |
| Base de sopa | 100 g | + 250 ml de caldo por ración, triturado y colado | `sopa-tomate` |

Toda cantidad de esta tabla llega con
`[CANTIDAD ESTIMADA — VERIFICAR CON PESAJE]` hasta que el chef pese un cazo real
de cada una. **Se entregan igualmente**: un valor de partida que se corrige en el
primer servicio vale más que seis huecos que nadie rellena.

### Contrato de interfaz — la parte que evita el desastre

```json
{
  "plato": "Salsa de tomate madre",
  "tipo": "preparacion_base_no_vendible",
  "porcion_referencia_g": 100,
  "consumida_por": [
    {"ficha": "pizza-margarita",  "cantidad_g": 80},
    {"ficha": "canelones",        "cantidad_g": 120},
    {"ficha": "pollo-cazadora",   "cantidad_g": 150},
    {"ficha": "lasana",           "cantidad_g": 140},
    {"ficha": "albondigas",       "cantidad_g": 130},
    {"ficha": "sopa-tomate",      "cantidad_g": 100}
  ],
  "estado": "BORRADOR"
}
```

`tipo: preparacion_base_no_vendible` existe para que
`escandallo-ingenieria-menu` **no** meta la salsa madre en la matriz de
ingeniería de menú como si fuera un plato de carta: no tiene precio de venta ni
margen propio, y colarla ahí ensucia el análisis de los seis platos que sí lo
tienen.

### Nota de mantenimiento, en la entrega

> Cuando cambie la salsa madre, se cambia **esta** ficha y las seis derivadas
> heredan el cambio automáticamente al recalcular. Si alguien copia la receta de
> la salsa dentro de una ficha derivada, esa herencia se rompe en silencio y las
> dos versiones divergen sin que nadie lo note hasta que el food cost se mueve.

## Por qué importa

Es el caso que decide si la skill produce **documentos** o produce un **sistema
de fichas**. La respuesta cómoda (seis fichas completas) es la que rompe el
producto tres semanas después de entregarlo, cuando el chef cambia la marca de
tomate y actualiza una de las seis.

Misma disciplina que `apertura-cierre-turno` aplica al consumir la tolerancia
±10 % sin recalcularla: **un umbral vive en un solo sitio**. Copiado a mano en
dos documentos, diverge.

## Supuestos declarados en la entrega

- País de operación no aportado: los puntos críticos de la ficha madre (cocción y
  enfriamiento de la salsa para conservación) salen marcados
  `[A VALIDAR — PAÍS SIN DECLARAR]` y la ficha **no pasa de BORRADOR** hasta que
  el chef diga el país. Es el único campo cuya ausencia bloquea el ascenso de
  estado, porque de él depende una cifra de inocuidad.
- Cantidades de la tabla de derivados: valores de partida de oficio, no pesados.
