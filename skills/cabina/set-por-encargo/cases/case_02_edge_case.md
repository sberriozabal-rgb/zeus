# Caso 2 · Edge case (cambio de slot a una hora del bolo)

## Situación

El DJ tiene el set del caso anterior preparado: 90 minutos, peak time, curva `meseta`. A una
hora de entrar, el promotor le dice:

> "Se ha retrasado todo. Tienes 50 minutos y cierras tú la noche."

Cambian **tres cosas a la vez**: la duración (90 → 50), la franja (peak → cierre) y el relevo
(había DJ después, ahora no hay).

## Lo que hace un DJ sin herramienta

Recorta por el final, que es lo rápido. El resultado es un set que arranca en peak, no baja
nunca y termina de golpe a 130 BPM con las luces encendidas.

## Reejecución

```bash
python3 scripts/setbuilder.py pool.csv -n 13 -c descenso \
  --energia-min 4 --energia-max 8
```

Paso 2 rehecho: 50 min / 4,7 = 11 tracks, +15% = **13**.
Paso 1 rehecho: franja `cierre` → curva `descenso`, energía 8 → 4.

**Tiempo total de la reejecución: menos de 2 minutos.**

## Salida esperada (extracto)

```
SET — Club, sabado   Slot: 50 min · descenso (energia 8-4)
Relevo: ninguno (cierra la noche)

 #  BPM  KEY  EN  TRACK                      TRANSICION
 1  128  9A   8   Artista R - Titulo         entra alto: viene de peak
 2  127  9A   8   Artista K - Titulo         sostiene
 ...
11  120  7A   5   Artista M - Titulo         descenso controlado
12  118  7A   4   Artista N - Titulo         -1 BPM
13  115  6A   4   Artista P - Titulo         cierre de noche

DECLARACIONES
 - Sin relevo: regla de aterrizaje omitida, cierre segun curva
```

## La diferencia

El set nuevo **entra alto** (energía 8) porque viene de peak time y la sala está caliente, y
**baja de forma controlada** hasta energía 4. No es el set anterior recortado: es otro set,
con otra forma, construido en dos minutos con el mismo pool.

## Por qué este caso vende la skill

Es el escenario que más veces se repite en el oficio y el que más tiempo ahorra. Preparar un
set nuevo a mano a una hora del bolo no se hace: se improvisa. Aquí se rehace entero antes de
terminar el café.
