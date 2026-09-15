# Caso 4 · Integration (alimenta a `set-por-encargo`)

## Situación

El DJ del caso 1 tiene residencia: el mismo sábado del mes que viene, misma sala, mismo
formato. Quiere que `set-por-encargo` le prepare el siguiente set **con lo aprendido**.

## Por qué se encadenan

El parte cierra con decisiones, pero una decisión en prosa no la ejecuta nadie. Esta
integración las traduce a **parámetros concretos** de la otra skill, que es donde se aplican.

## Traducción decisión → parámetro

| Decisión del parte | Parámetro para `set-por-encargo` |
|---|---|
| Retrasar el pico de tempo unos 20 min | Curva `arco` con pico desplazado al 75% del slot en vez del 70% |
| Tres tracks puente en 5A/6A para el tramo 01:15–01:45 | `--incluir` los tres puentes; restricción armónica máx. 2 pasos en ese tramo |
| El track del cierre fue el más sostenido (7:12) | Entra al pool preferente como obligatorio de cierre |
| Tres tracks cortados < 90 s seguidos en 01:18–01:30 | `--vetar` esos tres para este slot |
| BPM de relevo: el DJ anterior cerró a 124 | `--bpm-entrada 124` |

## Entrada encadenada a `set-por-encargo`

```
Slot: sabado 23:00-03:00, club, residencia
Franja: set completo de noche -> curva arco
BPM entrada: 124   BPM salida: libre (cierra la noche)
Pico: 75% del slot  (ajustado desde el 70% por el parte del mes anterior)
Incluir: [3 puentes 5A/6A] + [track de cierre]
Vetar: [3 tracks cortados del tramo 01:18-01:30]
Restriccion armonica tramo 01:15-01:45: maximo 2 pasos
```

## Salida del ciclo completo

El set que sale ya lleva incorporado lo que se aprendió de la noche anterior, y el parte del
mes siguiente **comprueba si funcionó**: la decisión 1 se verifica mirando si la curva llega
al máximo después de la 01:30; la decisión 2 contando saltos armónicos ≥3 pasos en esa franja,
con objetivo cero.

## Qué demuestra el caso

Que el postmortem no es un ejercicio de memoria: es la entrada del siguiente set. Y que el
bucle se cierra solo cuando cada decisión nace con su forma de comprobación, porque si no,
el parte del mes que viene no puede decir si se acertó.

La otra integración natural es con `auditoria-de-biblioteca`: los tres tracks puente en 5A/6A
solo se pueden buscar si la biblioteca tiene la clave analizada, y ahí es donde el hallazgo
`sin_clave` de esa skill deja de ser una cifra abstracta.
