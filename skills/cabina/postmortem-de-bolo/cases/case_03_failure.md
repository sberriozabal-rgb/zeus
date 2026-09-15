# Caso 3 · Failure (export sin horas, sin BPM y sin clave)

## Entrada

El DJ exporta desde un software que solo vuelca título y artista:

```csv
title,artist
Midnight City,M83
Sun Is Shining,Axwell
...
```

37 filas. Sin hora, sin BPM, sin clave, sin duración.

## Lo que se pierde

Sin marca temporal no hay tiempo en el aire, ni curva de tempo, ni tracks cortados o
sostenidos, ni cruce del reloj con el relato. **Eso es aproximadamente la mitad del valor del
parte** y se dice así, en la primera línea, sin adornos.

## Salida real — lo que se entrega igual, sin rendirse

```
ALCANCE REDUCIDO: el historial no trae horas.
Analisis temporal no disponible. Se entrega secuencia y repeticiones.

Tracks: 37   Artistas unicos: 31
Artistas repetidos: 4
  - Axwell         x3   (posiciones 4, 11, 29)
  - M83            x2   (posiciones 1, 22)
  - Disclosure     x2   (posiciones 8, 19)
  - Rufus Du Sol   x2   (posiciones 15, 33)
Tracks repetidos: 1
  - "Sun Is Shining"  x2  (posiciones 11 y 29)
```

## Lo que sí se puede concluir, y se entrega

**HECHO** — "Sun Is Shining" sonó dos veces, en las posiciones 11 y 29. En una sesión de 37
tracks eso es repetir a poco más de la mitad de distancia del set.

**HECHO** — Axwell aparece tres veces en 37 tracks, dos de ellas en el último tercio.

**HIPÓTESIS** — La repetición literal en la posición 29 puede ser un recurso deliberado de
cierre o un despiste. *El fichero no lo distingue; lo sabe el DJ.*

**Contraste con el plan** — El set planificado sí existía y tenía 44 tracks. Se ejecutaron 37,
y a partir de la posición 24 la secuencia se separa del plan por completo. Ese es el punto de
improvisación, y se puede localizar sin horas porque el orden sí está.

## Los supuestos declarados

> **Asumido**: el export no incluye columna temporal, así que no se ha calculado ni un solo
> dato de duración. Todo lo que se entrega sale del **orden**, que sí es fiable. No se puede
> cruzar el relato de sala con el reloj, de modo que la pérdida que el DJ sitúa "sobre la una
> y media" no se ha podido localizar en ningún track concreto.
>
> **Para la próxima:** en rekordbox, exporta desde la pestaña Historial con botón derecho
> sobre la sesión; en Serato, desde History → Export en formato csv. Ambos incluyen la hora de
> inicio. Con eso el parte recupera la mitad que hoy falta.

## Lo que NO se hace

No se responde "necesito un export con horas". El DJ se lleva la repetición literal que no
había detectado, el patrón de Axwell y el punto exacto donde abandonó el plan. Eso es
accionable hoy. Lo que falta se declara como hueco, no como condición previa.

Tampoco se estiman horas a partir de una duración media de track. Sería inventar la columna
que falta, y la curva de tempo resultante tendría aspecto de dato y sería ficción.
