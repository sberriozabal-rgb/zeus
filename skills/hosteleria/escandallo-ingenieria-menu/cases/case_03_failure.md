# Caso 3 · Failure (encargo de una línea, sin contexto)

## Encargo real que escribiría un dueño

> "¿cuánto me cuesta el arroz de marisco?"

Sin carta, sin ventas, sin inventarios, sin tipo de IVA, sin decir de qué local se trata.

## Entrada mínima construible

Se construye con lo único que el encargo permite deducir —un plato y su receta habitual de
arroz de marisco para dos— y se declara que la receta es la de referencia de la casa, no la
del cliente:

```json
{
  "local": "[sin nombre]", "periodo": "[sin periodo]", "iva_defecto": 0.10,
  "platos": [
    {"nombre": "Arroz de marisco (2p)", "familia": "principales", "precio_carta": 42.00,
     "unidades_vendidas": 1, "costes_ocultos_pct": 0.07,
     "ingredientes": [
       {"nombre": "Gamba entera", "precio_kg": 22.00, "gramos_en_plato": 120, "rendimiento": 0.55},
       {"nombre": "Mejillon con concha", "precio_kg": 3.50, "gramos_en_plato": 100, "rendimiento": 0.30},
       {"nombre": "Arroz bomba", "precio_kg": 3.90, "gramos_en_plato": 320},
       {"nombre": "Fumet y sofrito", "precio_kg": 4.20, "gramos_en_plato": 400}
     ]}
  ]
}
```

## Salida real — lo que se entrega igual, sin rendirse

```
Platos: 1   Unidades: 1
Ventas netas (sin IVA):        38.18
Food cost teorico:            24.93%

>> SIN CONTRASTE: no se aporto food cost real. El analisis va sobre teorico.

PLATO                        UDS     PVP   COSTE   MARGEN    FC%     CUADRANTE
Arroz de marisco (2p)          1   38.18    9.52    28.66   24.9      ESTRELLA

  Arroz de marisco (2p) — ESTRELLA
      !! familia 'principales' con menos de 3 platos: el cuadrante no es
         concluyente, agrupa familias o interpreta con cautela
```

Y la respuesta al dueño, en tres líneas, que es lo que él pidió:

> Tu arroz de marisco para dos te cuesta **9,52 €** de materia prima —con el mejillón
> valorado por su carne real, no por el peso con concha, y con un 7% de costes de mesa y
> cocción— y a 42 € de carta te deja **28,66 € de margen** por ración doble, con un food
> cost del **24,9%**. El mejillón es lo que más engaña: a 3,50 €/kg con concha, la carne te
> sale a 11,67 €/kg.

## Los tres supuestos declarados, en una línea al final

> Asumido: receta de referencia de la casa (gamba 120 g, mejillón 100 g, arroz bomba 320 g,
> fumet 400 g) porque no se aportó la tuya; IVA 10% de hostelería en España; costes de mesa
> y cocción al 7%. Cambia cualquiera de los tres y te recalculo en un minuto.

## Lo que NO se hace

No se responde "necesito tu carta, tus ventas y tus inventarios". El dueño preguntó por un
plato y recibe el escandallo de ese plato, ejecutable y con la cifra que buscaba. Lo que
falta se declara como supuesto, no como condición previa.

Sí se dice, sin alarmismo, qué no se puede afirmar con un solo plato: **el cuadrante
"ESTRELLA" no significa nada aquí** y el propio motor lo avisa, porque la matriz clasifica
contra la media de la carta y con un plato no hay media. Se entrega tachado.

## Por qué es el caso decisivo

El antipatrón "caso failure cobarde" sería pedir el paquete completo de datos antes de
producir. Aquí el dueño se lleva a casa una cifra que puede usar hoy —9,52 € de coste,
28,66 € de margen— y un motivo para volver: el resto de la carta.
