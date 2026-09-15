# Caso 3 · Failure (pool sin clave y sin energía)

## Entrada

CSV exportado de un software antiguo, 95 tracks:

```csv
artista,titulo,bpm
Artista A,Titulo 1,124
Artista B,Titulo 2,126
...
```

Sin `key`, sin `energia`, sin `duracion_s`. Brief: 60 minutos, peak time, relevo a 130.

## Lo que se pierde

Sin clave **no hay mezcla armónica posible**: desaparecen las notas de transición en Camelot,
que son la mitad visible del entregable. Es una degradación seria y se dice en la primera
línea, no en una nota al pie.

## Salida real — lo que se entrega igual, sin rendirse

```
SET — 60 min · meseta (energia 6-9)
>> MODO DEGRADADO: el pool no trae clave. Orden por BPM y energia inferida.
>> Las transiciones NO estan verificadas armonicamente.

 #  BPM  EN*  TRACK                      TRANSICION
 1  124   6   Artista A - Titulo 1       entrada
 2  125   6   Artista F - Titulo 9       +1 BPM
 3  126   7   Artista B - Titulo 2       +1 BPM, sube energia
 ...
14  128   7   Artista Q - Titulo 31      aterrizaje
15  126   6   Artista T - Titulo 44      cierre a 126 (relevo 130: OK)

* EN = energia INFERIDA del BPM, no medida.

DECLARACIONES
 - Pool sin columna 'key': 95 de 95 tracks. Sin verificacion armonica.
 - Energia inferida del BPM en 95 de 95 tracks.
 - Pool sin 'duracion_s': numero de tracks estimado a 4 min/track (club).
```

## Lo que sí sigue siendo válido

- **La curva de energía se respeta**, aunque la energía sea inferida: la forma del set
  (meseta 6-9) está construida.
- **La regla de relevo se aplica igual**, porque solo necesita BPM: cierra a 126 contra los
  130 del siguiente, dentro del rango de 4-8 por debajo.
- **El progresivo de tempo funciona**: no hay saltos bruscos de BPM.

## Los supuestos declarados

> **Asumido**: energía inferida del BPM en los 95 tracks, lo que es una aproximación gruesa
> —un tema de 128 puede ser atmosférico o demoledor y el BPM no lo distingue—. Duración media
> de 4 min/track para calcular el número de tracks. **No se ha verificado ni una sola
> transición armónica.**
>
> **Para cerrar el hueco:** analiza el pool en rekordbox o en Mixed In Key y reexporta con la
> columna `key`. Son minutos de máquina y recuperas la mitad del entregable.

## Lo que NO se hace

No se responde "necesito un pool con clave". El DJ se lleva un set con la curva construida,
el tempo progresivo y el relevo resuelto, que es utilizable esta noche. Y no se inventa una
clave por proximidad de BPM: sería fabricar el dato que falta y las transiciones resultantes
tendrían aspecto de verificadas sin serlo, que es peor que no tenerlas.
