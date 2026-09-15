# Caso 2 · Edge case (la sesión cruza la medianoche)

## Entrada

Historial de 38 tracks. El export trae las horas como reloj de pared, sin fecha, y la sesión
cruza la medianoche:

```
...
23:51  Track 17
23:58  Track 18
00:03  Track 19
00:09  Track 20
...
```

## El problema

Calculando duración como `hora_siguiente - hora_actual`, el Track 18 sale con **-1.435
minutos** en el aire. Si no se corrige, la curva de tempo se rompe entera, el track aparece
como el más corto de la noche y la duración total de la sesión sale negativa.

## Salida esperada

El motor detecta la diferencia negativa y suma 24 h:

```
CRUCES DE MEDIANOCHE DETECTADOS Y CORREGIDOS: 1
  23:58 -> 00:03   duracion corregida: 5m 00s

HECHOS DEL FICHERO
Tracks: 38   Duracion: 4h 12m   Tempo medio: 128.1 BPM
```

Y lo declara en el parte, no en silencio:

> **Nota de datos:** el historial cruza la medianoche y reinicia el reloj. Se ha detectado y
> corregido **1 cruce** sumando 24 h a la diferencia negativa. Las duraciones de esta sesión
> son correctas.

## Segundo hallazgo del caso: el hueco largo

En el mismo export hay un salto de 01:40 a 02:55 sin ningún track registrado.

**Lo que NO se hace:** tratarlo como un track de 75 minutos en el aire. Sería el "track más
sostenido de la historia" y es obviamente falso.

**Lo que se hace:** marcarlo como hueco y ofrecer las dos lecturas posibles sin elegir una:

> **HECHO** — Hueco de 1h 15m sin registro entre 01:40 y 02:55.
> **HIPÓTESIS** — Puede ser una pausa real (otro DJ, cambio de cabina, cierre de barra) o un
> fallo de registro del software. *Preguntar al DJ; el fichero no lo distingue.*

## Por qué es el caso decisivo

Los dos artefactos —cruce de medianoche y hueco largo— son los que convierten un parte
automático en basura convincente. Un número negativo se ve; un track de 75 minutos no, y el
DJ podría creérselo. La regla es declarar el artefacto siempre, incluso cuando se ha podido
corregir.
