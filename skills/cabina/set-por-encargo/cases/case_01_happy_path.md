# Caso 1 · Happy path (slot de telonero con relevo definido)

## Brief

| Campo | Valor |
|---|---|
| Duración | 90 min |
| Franja | Calentamiento / telonero |
| BPM entrada | libre (abre la noche) |
| Relevo | el cabeza de cartel abre a **128** |
| Público | club, 300 personas, 25-40 |
| Prohibiciones | ninguna |
| Obligatorios | ninguno |

Pool: 180 tracks filtrados, con `bpm`, `key`, `energia` y `duracion_s`.

## Ejecución

```bash
python3 scripts/setbuilder.py pool.csv -n 21 -c rampa \
  --energia-min 3 --energia-max 7
```

Cálculo del paso 2: 90 min / 4,7 min de media = 19 tracks, +15% de margen = **21**.

## Salida esperada (extracto)

```
SET — Club, sabado   Slot: 90 min · rampa (energia 3-7)
Relevo: el siguiente abre a 128 -> cerrar entre 120 y 124

 #  BPM  KEY  EN  TRACK                      TRANSICION
 1  118  5A   3   Artista A - Titulo         apertura baja, sala vacia
 2  119  5A   3   Artista B - Titulo         misma clave, +1 BPM
 3  120  6A   4   Artista C - Titulo         +1 paso Camelot
 ...
18  126  9A   7   Artista R - Titulo         techo de la rampa
19  124  9A   6   Artista S - Titulo         inicio de aterrizaje
20  123  8A   6   Artista T - Titulo         -1 paso
21  122  8A   5   Artista U - Titulo         cierre a 122 (relevo 128: OK)

DECLARACIONES
 - ninguna
```

## Los tres puntos de riesgo, revisados

1. **Track 1** — No hay BPM de entrada porque abre la noche. Arranca a 118 con energía 3, que
   es lo correcto para sala vacía. ✔
2. **El pico** — Máximo de energía (7) en la posición 18 de 21, es decir al 86% del slot. En
   curva `rampa` es lo buscado: **sube sin llegar al techo** para no quemarle la pista al
   cabeza de cartel. ✔
3. **El cierre** — Aterriza a **122**, que está 6 BPM por debajo de los 128 del relevo, dentro
   del rango recomendado de 4-8. ✔

## Por qué es el caso central

Es el escenario donde la skill se gana el precio frente a un ordenador armónico: ninguna
herramienta que ordene solo por Camelot y BPM sabe que eres el telonero, y por tanto ninguna
te impide cerrar a 128 y dejar al cabeza de cartel sin margen. El criterio contextual es todo
el producto.
