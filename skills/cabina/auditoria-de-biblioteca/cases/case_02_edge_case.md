# Caso 2 · Edge case (biblioteca nueva, porcentaje alto que no es problema)

## Encargo real

> "Me he montado la colección de cero hace un mes. ¿Está bien?"

## Entrada

- `collection.xml` con 300 tracks.
- Todo analizado en rekordbox: BPM y clave presentes en el 100%.
- Sin un solo cue point y sin ratings.
- Sin bolo próximo declarado.

## Salida esperada

```
Indice de salud: 88/100    (300 tracks)

CATEGORIA              N       %   RIESGO   CONSECUENCIA
sin_cue_points       300  100.0%   MEDIO    Se entra a ciegas
sin_rating           300  100.0%   BAJO     Solo importa si organizas por estrellas
ruta_rota              0    0.0%   -        -
sin_beatgrid           0    0.0%   -        -
```

## Lectura correcta del parte

El 100% en dos categorías **no baja la salud a 0**, y esa es la enseñanza del caso. Una
biblioteca recién montada y bien analizada está sana: lo que le falta es uso, no reparación.

- `sin_cue_points` al 100% en una colección nueva es **normal**, no un defecto. Los cue
  points se ponen pinchando, no importando.
- `sin_rating` al 100% solo importa si el DJ organiza por estrellas. Si no lo hace, es ruido
  y así se dice.

## Lo que NO se hace

No se recomienda "poner cue points a los 300 tracks". Es trabajo de meses que exige oír cada
uno, y el retorno depende de cuáles se vayan a pinchar de verdad. La recomendación correcta
es ponerlos **según se usen**, empezando por los que entren en la primera playlist de bolo.

Tampoco se infla el problema para justificar el parte. Una biblioteca a 88/100 se dice que
está bien.

## Priorización sin bolo declarado

Al no haber fecha de bolo, el parte se ordena por riesgo genérico y lo declara en los
supuestos: *"sin bolo declarado, la priorización no está cruzada con playlists; ordena por
riesgo general"*.
