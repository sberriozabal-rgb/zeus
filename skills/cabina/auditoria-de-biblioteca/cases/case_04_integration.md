# Caso 4 · Integration (encadenado con `set-por-encargo`)

## Situación

El mismo DJ del caso 1 quiere, además del parte, que le preparen el set de la fiesta del
sábado con `set-por-encargo`. Las dos skills trabajan sobre el mismo `collection.xml`.

## Por qué se encadenan

`set-por-encargo` **no oye**: lee clave, BPM y energía del export. Si la clave falta, el track
simplemente no entra en el set armónico. Es decir: **cada hallazgo `sin_clave` de esta
auditoría es pool que el DJ pierde sin saberlo.**

Eso convierte un hallazgo abstracto ("1.204 tracks sin clave, 14,3%") en una cifra que duele:
cuántos de los tracks candidatos al set del sábado quedan fuera por un metadato que falta.

## Entrada encadenada

1. Esta skill produce la lista de `sin_clave` y `sin_bpm`.
2. Se cruza contra el pool declarado para `SABADO_FIESTA` (420 tracks candidatos).

## Salida del cruce

```
Pool declarado para SABADO_FIESTA:        420 tracks
  - sin clave:                             58  (13.8%)  -> fuera del set armonico
  - sin BPM:                               11  ( 2.6%)  -> invisible al filtrar por tempo
  - ambos:                                  9
Pool realmente utilizable por set-por-encargo:  351 (83.6%)
```

## Recomendación conjunta

> Antes de encargar el set, lanza el análisis de rekordbox sobre esos **60 tracks** (58 sin
> clave + 11 sin BPM, con 9 solapados). Es automático, no exige oír nada y tarda unos minutos.
> Recuperas un **16,4% de pool** para el set del sábado.
>
> Aviso que viaja con el dato: rekordbox 7 acierta la clave en el 69% de los casos
> (<https://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport>), así que en las
> transiciones que `set-por-encargo` marque como armónicas conviene confiar en el oído antes
> que en la etiqueta.

## Qué demuestra el caso

Que el parte de esta skill no termina en sí mismo: alimenta la siguiente decisión. Y que el
orden correcto es auditar **antes** de encargar el set, no después, porque analizar 60 tracks
cuesta minutos y rehacer un set cuesta una tarde.
