# Caso 1 · Happy path (primer corte, línea base cerrada)

## Entrada

> "Reporte de inteligencia de Casa Melilla, Chamberí, Madrid."

Nada más. Nombre y plaza.

## Paso 1 · Panel congelado (3+2+1)

| Cupo | Competidor | Perfil | Distancia | Motivo de entrada |
|---|---|---|---|---|
| Directo | [C1] | Misma categoría, ticket ±25 % | 400 m | Mismo público de barrio |
| Directo | [C2] | Misma categoría | 650 m | Mismo rango de ticket |
| Directo | [C3] | Misma categoría | 1,1 km | Mismo público de fin de semana |
| Referencia | [R1] | Líder de categoría en la plaza | 2,4 km | Referente al que el cliente compara |
| Referencia | [R2] | Marca aspiracional | — | Aparece citada en reseñas propias |
| Entrante | [E1] | Abierto hace 7 meses | 300 m | Roba la misma ocasión de consumo |

Radio declarado: **2 km** (núcleo urbano). Panel congelado hasta **[fecha + 13 semanas]**.

## Paso 2 · Modo de captura

**MODO: PLATAFORMA.** Se abren las siete fichas y se cuenta el listado. Coste: ~6 h.
`ESTADO_LINEA_BASE: CERRADA`.

## Paso 3 · Tabla 7×8 (extracto)

```
FICHA        NOTA  VOL   VEL   RECIENTE  %1-2*  RESP%  T.RESP  FRESCURA
Casa Melilla 4.2   312   2.1   4.0       14%    38%    72 h    9%
[C1]         4.4   520   3.8   4.5        8%    91%    11 h   17%
[C2]         4.1   180   1.2   4.1       15%     0%     --     6%
[R1]         4.6  1240   6.4   4.6        5%    88%     8 h   21%
...
MEDIANA      4.3   416   3.0   4.3       11%    63%    18 h   14%
```

## Paso 5 · Brecha

| Métrica | Nosotros | Mediana | Mejor | Posición | Semáforo |
|---|---|---|---|---|---|
| Tasa de respuesta | 38 % | 63 % | 91 % | **5.º de 7** | 🔴 |
| Tiempo de respuesta | 72 h | 18 h | 8 h | **6.º de 7** | 🔴 |
| Frescura | 9 % | 14 % | 21 % | 6.º de 7 | 🟠 |
| Nota media | 4,2 | 4,3 | 4,6 | 4.º de 7 | 🟡 |

Las tres peor situadas: **respuesta, tiempo de respuesta y frescura**. Las tres se corrigen sin
tocar el producto.

## Paso 7 · Las tres acciones de 7 días

| Acción | Dueño (puesto) | Coste | Métrica de verificación + fecha |
|---|---|---|---|
| Responder las 50 reseñas sin respuesta, empezando por las 1-2★ | Encargado de sala | Cero | Tasa de respuesta ≥ 70 % el [fecha +7] |
| Fijar rutina diaria de respuesta en el cierre de caja | Encargado de sala | Cero | Tiempo mediano < 24 h el [fecha +7] |
| Pedir reseña al cliente satisfecho al cobrar, sin incentivo | Jefe de sala | Cero | ≥ 12 reseñas nuevas el [fecha +7] |

**Ninguna cuesta dinero.** Las tres salen de la brecha medida, no de una impresión.

## Cabecera del reporte

```
[PRIMER CORTE — LÍNEA BASE]
Panel congelado hasta: [fecha]  ·  Radio: 2 km  ·  MODO: PLATAFORMA
Captura: [fecha] 09:40  ·  ESTADO_LINEA_BASE: CERRADA
```

## Por qué es el caso central

Demuestra lo que produce la skill: de un nombre y una ciudad salen **tres acciones de coste cero
con métrica de verificación a 7 días**, y la razón por la que son esas tres es una tabla que
cualquiera puede recomprobar.
