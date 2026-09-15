# Caso 1 · Happy path

## Encargo real que escribiría un dueño

> "Te paso la carta con los precios, las ventas de julio del TPV y las fichas de los platos. Dime qué me está comiendo el margen y qué quito."

## Entrada

`assets/plantilla-datos.json`: 9 platos de dos familias, 1.154 unidades vendidas en el
periodo, recetas con gramajes, rendimientos declarados por ingrediente, mermas de cocción,
porcentaje de costes ocultos por plato, IVA 10% y **food cost real aportado (36,2%)**,
es decir con inventarios hechos.

```bash
python3 scripts/escandallo.py assets/plantilla-datos.json
```

## Salida real (ejecutada, no narrada)

```
Platos: 9   Unidades: 1154
Ventas netas (sin IVA):    23,805.12
Coste materia prima:        7,700.48
Margen de contribucion:    16,105.98
Food cost teorico:            32.35%
Food cost real:               36.20%
Desviacion:                    3.85 puntos

>> ATENCION: mas de 2 y hasta 5 puntos. Porcionado o mermas descontroladas.
   El analisis de carta es valido, pero no resuelve todo el problema.

PLATO                        UDS     PVP   COSTE   MARGEN    FC%     CUADRANTE
Solomillo a la brasa         190   23.64   10.55    13.08   44.6       CABALLO
Merluza a la plancha         165   20.91    6.37    14.54   30.4       CABALLO
Ensalada de la casa           96   10.45    1.56     8.90   14.9         PERRO
Pulpo a la brasa              88   21.82    7.02    14.80   32.2         PERRO
Bogavante del dia             24   27.27   47.77   -20.50  175.2         PERRO
Alcachofa confitada           61   12.73    3.13     9.60   24.6  ROMPECABEZAS
Tabla iberica                  0   25.45   11.97    13.48   47.0  ROMPECABEZAS
Croquetas (6u)               320   10.91    1.69     9.22   15.5      ESTRELLA
Arroz de marisco (2p)        210   38.18    9.52    28.66   24.9      ESTRELLA
```

## Lo que el informe dice con esto

1. **Diagnóstico primero**: desviación de 3,85 puntos. Banda de aviso. El análisis de carta
   es válido, pero se declara por escrito que una parte del agujero no se arregla con
   precios: hay porcionado o merma sin controlar.
2. **El titular no es el plato más caro, es el bogavante**: 175,2% de food cost, margen de
   **−20,50 € por unidad servida**, 24 unidades en el periodo = 492 € perdidos. Antes de
   recomendar nada se lleva al apartado 6 como pregunta, porque un coste por encima del
   precio de venta suele ser error de unidades. Si no lo es, es el titular del informe.
3. **Solomillo, caballo de batalla con 44,6%**: se ataca por rendimiento y porcionado antes
   que por precio. El script cuantifica: bajar 1,00 € de coste unitario vale 2.280 €/año
   extrapolando el ritmo de venta de un mes — y esa extrapolación se declara.
4. **La ensalada es perro y además intocable** (marcada `intocable: true` en los datos): el
   informe la deja fuera de cualquier subida de precio y lo explica, porque es marcador de
   precio de la carta.
5. **Tabla ibérica con 0 ventas**: bandera del script. No entra en acciones hasta que el
   cliente confirme si sigue en carta o es un botón muerto del POS.

## Por qué es el caso central

Es el flujo completo con datos limpios: contraste teórico-real, las tres capas de coste
aplicadas, la matriz clasificada contra el 70% de la cuota media y dos anomalías tratadas
como preguntas y no como conclusiones. Todo lo demás son variantes de este camino.
