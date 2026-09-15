# Caso 3 · Failure (encargo sin contexto utilizable)

## Encargo real que escribiría un dueño

> "El cocinero se fue el viernes sin avisar y este plato es el que más vendemos.
> Tengo esta foto del plato montado y la lista de lo que compraba para hacerlo:
> panceta, huevo, pecorino, pimienta negra, espagueti. Nada más. Nadie sabe
> cómo lo hacía. ¿Puedes hacer algo?"

Sin cantidades. Sin procedimiento. Sin tiempos. Sin nadie a quien preguntar.

## Entrada mínima construible

```
plato:            [foto del plato montado]
ingredientes:     panceta · huevo · pecorino · pimienta negra · espagueti
cantidades:       [FALTA]
procedimiento:    [FALTA]
tiempos_temp:     [FALTA]
rendimiento:      [FALTA]
emplatado:        [derivable de la foto]
pais:             [FALTA]
transmision_oral: NINGUNA — el cocinero no está localizable
```

**9 de los 10 campos obligatorios ausentes o derivables.** Muy por encima del
corte de 4: la ficha **no puede salir como ACORDADO** bajo ninguna
interpretación. Lo que se decide aquí es qué se entrega, no si se entrega.

## Salida esperada — lo que se entrega igual, sin rendirse

**El antipatrón que aquí sería un suspenso:** responder *"con una foto y una lista
de ingredientes no puedo escribir una receta estándar; necesito cantidades,
procedimiento y tiempos"* y detenerse. Es cierto y es inútil. El dueño abre
mañana y tiene que vender ese plato igual.

Se entrega una **ficha BORRADOR de primera prueba de cocina**, completa:

### Lo que va en la ficha y con qué marca

| Sección | Qué se entrega | Marca |
|---|---|---|
| Identificación | "Espagueti a la carbonara (reconstrucción)" — identificado por los cinco ingredientes, que son los canónicos del plato | `[NOMBRE PROPUESTO — CONFIRMAR CON LA CARTA]` |
| Ingredientes | Cantidades de partida por ración: 100 g espagueti · 60 g panceta · 1 yema + 1 huevo entero · 30 g pecorino · 1 g pimienta negra | `[CANTIDAD ESTIMADA — VERIFICAR CON PESAJE]` en cada línea |
| Rendimiento | 1 ración; escalable con `scripts/escalar_receta.py` | `[RENDIMIENTO PROPUESTO]` |
| Procedimiento | 7 pasos con la técnica estándar del plato: rendir la panceta, cocer la pasta, montar la crema de huevo y queso fuera del fuego, ligar con agua de cocción | `[PROCEDIMIENTO PROPUESTO — VERIFICAR EN PRUEBA DE COCINA]` |
| Punto crítico | Huevo sin cocción completa: es el riesgo real de este plato | **Marcado y con cifra** — ver abajo |
| Emplatado | Derivado de la foto: pasta enrollada en nido, panceta visible en superficie, pimienta molida encima, plato hondo blanco | `[DERIVADO DE IMAGEN]` |
| Conservación | No aplica: plato de servicio inmediato, no se regenera | CONFIRMADO por técnica |

### El punto crítico no se entrega estimado, ni siquiera aquí

Esta es la línea que no se cruza. Todo lo demás de esta ficha es una propuesta
razonable marcada como tal; **la cifra de inocuidad no**:

> **Punto crítico — huevo.** La carbonara liga con huevo que no alcanza cocción
> completa. AESAN fija para platos con huevo de **consumo inmediato 63 °C durante
> 20 s**, y para consumo **no** inmediato 70 °C/2 s (informe AESAN-2021-004). En
> México, NOM-251 §7.3.1 fija 63 °C para huevo con cascarón roto y 68 °C si va a
> buffet. **La cifra aplicable depende del país, que no se ha declarado, y de si
> el plato sale al momento o espera en el pase.**
>
> Hasta que se declaren las dos cosas, esta ficha va marcada
> `[A VALIDAR — PAÍS Y RÉGIMEN DE SERVICIO SIN DECLARAR]` en su punto crítico y
> **no se cuelga en la partida como estándar**. Se cuelga como guion de prueba.
> Si el local usa huevo pasteurizado, díganlo: cambia el análisis entero.

### Lista de cierre — qué falta para pasar de BORRADOR a ACORDADO

1. Ejecutar la receta una vez con esta ficha delante y **pesar** lo que se usa.
2. Declarar el país y si el plato sale al momento o espera en el pase.
3. Confirmar el nombre exacto que figura en la carta.
4. Foto del emplatado como sale hoy, no la del cocinero que se fue.
5. Confirmar si el huevo es pasteurizado.

Con esos cinco puntos, en un servicio, la ficha pasa a ACORDADO. Sin ellos, sirve
para cocinar el plato mañana con criterio, que es lo que el dueño necesitaba.

### Línea final de la entrega, literal

> **Asumido:** el plato es una carbonara clásica, identificada por sus cinco
> ingredientes. Todas las cantidades son puntos de partida sin pesar. El punto
> crítico del huevo queda sin cerrar a propósito: dime el país y si el plato sale
> al momento, y te lo cierro con la cifra de la norma que os aplica.

## Por qué es el caso decisivo

Aquí se juegan dos cosas a la vez, y casi todo el mundo falla una:

1. **No se rinde.** Sale una ficha ejecutable mañana, con cantidades de partida,
   procedimiento completo y emplatado derivado de la foto. El dueño puede vender
   el plato.
2. **No inventa la cifra que mata.** Todo lo demás se propone marcado; la
   temperatura de inocuidad del huevo **no se propone**, porque un número
   plausible en una casilla de punto crítico es peor que un hueco: el hueco se ve,
   y el número falso se cocina.

Esa asimetría es la regla de la casa aplicada donde duele. Se entrega mucho, y se
declara con precisión lo único que no se puede entregar.
