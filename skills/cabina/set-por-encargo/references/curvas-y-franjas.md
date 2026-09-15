# Curvas de energia y franjas horarias

## Las cinco curvas del motor

| Curva | Forma | Cuando |
|---|---|---|
| `rampa` | Sube de forma continua de principio a fin | Telonero, calentamiento, apertura |
| `arco` | Sube al pico en el 70% y baja al cierre | Set completo de noche, sesion unica |
| `meseta` | Sube rapido, sostiene el pico, cierra bajando poco | Peak time |
| `descenso` | Empieza arriba y baja | Cierre, after, ultimo turno |
| `dientes` | Tres oleadas ascendentes con alivio entre ellas | Sesion larga, 3h+ |

Se eligen con `-c` y se acotan con `--energia-min` y `--energia-max`.

## Guia de referencia para slot de telonero de 90 minutos

Recogida de una guia operativa de preparacion de sets (marcada como referencia
del oficio, no como norma universal):

| Tramo | BPM | Energia |
|---|---|---|
| 0-20 min | 118-120 | 55-60% |
| 20-40 min | 120-122 | subiendo |
| 40-60 min | 122-124 | subiendo |
| 60-90 min | 123-124 | techo del telonero |

**Regla de relevo:** aterrizar los ultimos 20 minutos entre 4 y 8 BPM por
debajo del BPM al que abrira el siguiente DJ, y nunca igual o por encima. Si el
cabeza de cartel abre a 128, se cierra entre 120 y 124.

Esta regla es la diferencia entre que te vuelvan a llamar o no. El motor no la
aplica solo: hay que verificarla a mano (Paso 4 del protocolo).

## De la energia declarada a la energia real

El motor usa la energia en esta prioridad:

1. **Campo `energia` del CSV** — si existe, manda.
2. **`Energy N` en el campo Comments** — es donde Mixed In Key escribe su
   Energy Level. El script lo extrae automaticamente del rekordbox XML.
3. **Rating en estrellas** — se convierte (5 estrellas = E10, 3 = E6).
   rekordbox codifica el rating como 0/51/102/153/204/255, no como 0-5.
4. **Inferida del BPM** — ultimo recurso. Escala el BPM dentro del rango del
   pool. **Es una aproximacion, no una medicion**, y el script lo declara.

Un track lento puede ser altisimo en energia y uno rapido puede ser un relleno.
Cuando veas el aviso `energia_inferida_de_bpm` alto, la curva es una hipotesis.

## Calculo de numero de tracks

```
n = (duracion_slot_min / duracion_media_track_min) * 0.85
```

El 0.85 es margen: casi siempre se corta antes de tiempo, se alarga un track o
entra una peticion. Es preferible quedarse corto y tener fondo de armario a
llevar un set que no cabe.

Duracion media orientativa si el pool no la trae: 5 min en club, 3,5 min en
evento con formato mas corto. Declararlo siempre como estimacion.
