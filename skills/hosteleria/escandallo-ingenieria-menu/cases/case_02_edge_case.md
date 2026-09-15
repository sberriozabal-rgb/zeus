# Caso 2 · Edge case — datos sucios y sin inventarios

## Encargo real que escribiría un dueño

> "No tengo inventarios ni sé lo que rinde nada. Te paso los precios del albarán, los gramos de la receta y lo que vendí. Mira a ver."

Es el caso más frecuente en la primera instalación: nadie mide rendimientos y nadie ha
hecho inventario en meses.

## Entrada

```json
{
  "local": "Bar sin datos limpios", "periodo": "2026-07", "iva_defecto": 0.10,
  "platos": [
    {"nombre": "Merluza a la plancha", "familia": "principales", "precio_carta": 23.00,
     "unidades_vendidas": 120,
     "ingredientes": [{"nombre": "Merluza entera", "precio_kg": 12.50, "gramos_en_plato": 190}]},
    {"nombre": "Bogavante del dia", "familia": "principales", "precio_carta": 30.00,
     "unidades_vendidas": 24,
     "ingredientes": [{"nombre": "Bogavante vivo", "precio_kg": 52.00, "gramos_en_plato": 350, "rendimiento": 0.40}]},
    {"nombre": "Tabla iberica", "familia": "principales", "precio_carta": 28.00,
     "unidades_vendidas": 0,
     "ingredientes": [{"nombre": "Jamon iberico", "precio_kg": 78.00, "gramos_en_plato": 120}]},
    {"nombre": "Cafe solo", "familia": "principales", "precio_carta": 1.60,
     "unidades_vendidas": 900,
     "ingredientes": [{"nombre": "Cafe grano", "precio_kg": 14.00, "gramos_en_plato": 7}]}
  ]
}
```

Cuatro suciedades a la vez: **sin `food_cost_real`** (no hay inventarios), **sin
rendimientos** en tres de cuatro platos, **sin costes ocultos** declarados, un plato con
**0 ventas** y un café con 900 unidades que descuadra la familia.

## Salida real (ejecutada)

```
Platos: 4   Unidades: 1044
Food cost teorico:            32.84%

>> SIN CONTRASTE: no se aporto food cost real (hace falta inventario inicial,
   compras e inventario final). El analisis va sobre teorico.

PLATO                        UDS     PVP   COSTE   MARGEN    FC%     CUADRANTE
Cafe solo                    900    1.45    0.10     1.36    6.7       CABALLO
Bogavante del dia             24   27.27   45.50   -18.23  166.8         PERRO
Merluza a la plancha         120   20.91    2.38    18.53   11.4  ROMPECABEZAS
Tabla iberica                  0   25.45    9.36    16.09   36.8  ROMPECABEZAS

  Cafe solo — CABALLO
      !! food cost < 10%: probablemente falta un ingrediente en la receta
  Bogavante del dia — PERRO
      !! PIERDE DINERO en cada unidad: revisa unidades o el precio de carta
      !! food cost > 45%: insostenible salvo que sea reclamo consciente
  Tabla iberica — ROMPECABEZAS
      !! 0 ventas: comprueba si sigue en carta o es un boton muerto del POS
```

## El hallazgo clave de este caso

**La merluza sale a 11,4% de food cost. Es mentira.** Con los mismos gramos, el mismo
precio de albarán y las dos capas que aquí faltan —rendimiento 52% y merma de plancha 18%,
que es lo que trae la carta de prueba del caso 1— ese plato cuesta 6,37 € y da **30,4%**.
Diecinueve puntos de diferencia por dos datos que nadie mide.

Un motor ingenuo entregaría el informe con la merluza como plato sano y el dueño la
protegería. Este entrega el informe igual, pero:

- Marca cada plato sin rendimiento declarado como **estimado** y lista los tres productos
  de más peso en compra que hay que medir esta semana.
- Abre con "análisis sin contraste": sin inventarios no hay desviación, y por tanto **no se
  puede afirmar si el problema es de carta o de control**. Lo dice en la primera línea,
  no en la última.
- El café al 6,7% no se celebra: la bandera `food cost < 10%` dice que a esa receta le
  falta un ingrediente (leche, azúcar, la merma del grano). Va al apartado 6 como pregunta.
- La tabla ibérica con 0 ventas no recibe la acción "trabajar la venta" que su cuadrante
  sugeriría: queda congelada hasta que el cliente confirme si el botón del POS está vivo.

## Por qué importa

Es la disciplina de la línea: un hueco de dato no se rellena con el valor cómodo. Aquí el
valor cómodo era "tu merluza va estupenda", y habría sido el error que rompe la instalación
en la segunda reunión, cuando el dueño mira su banco y no le cuadra.
