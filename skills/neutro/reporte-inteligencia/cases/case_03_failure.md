# Caso 3 · Failure (marca sin reputación medible)

## Entrada

> "Reporte de inteligencia de [Clínica dental]."

Al capturar: perfil de Google **sin reclamar**, **6 reseñas totales**, sin presencia en ninguna
otra plataforma. Cinco de las ocho métricas propias son incalculables.

## Lo que NO se hace

No se responde "no hay datos suficientes para un reporte". Sería técnicamente cierto **sobre la
marca propia** y completamente falso sobre el encargo: el panel de 6 competidores sí tiene
reputación, y ahí está casi todo el valor.

## Salida real — el reporte se emite igual

```
[PRIMER CORTE — LÍNEA BASE]
MODO: PLATAFORMA  ·  ESTADO_LINEA_BASE: ABIERTA (marca propia)

FICHA          NOTA  VOL   VEL   RECIENTE  %1-2*  RESP%  T.RESP  FRESCURA
CLINICA PROPIA  4.3     6   [MUESTRA INSUFICIENTE — 6 resenas]
[C1]            4.6   340   2.8   4.7        6%    82%    14 h   16%
[C2]            4.2   510   3.1   4.1       13%    45%    50 h   12%
[R1]            4.8   890   5.2   4.8        3%    95%     6 h   22%
...
MEDIANA PANEL   4.5   425   3.0   4.4        9%    64%    18 h   15%
```

**La marca propia sale de la mediana, no del reporte.** Sus celdas van en `[NO DISPONIBLE]` con
el motivo, no en blanco.

## Lo que sí se entrega y es lo más valioso del caso

**El panel completo con su reputación real.** Qué nota tienen los seis, a qué velocidad crecen,
quién responde y en cuánto tiempo, y qué dicen sus pacientes. Eso no depende de que la clínica
tenga reseñas.

Y los seis hallazgos y las oportunidades de la plaza siguen siendo válidos: qué piden los
pacientes que ningún competidor está resolviendo.

## Las tres acciones, orientadas a cerrar la línea base

| Acción | Dueño (puesto) | Coste | Métrica de verificación + fecha |
|---|---|---|---|
| Reclamar el perfil de Google | Responsable de clínica | Cero | Perfil verificado el [fecha +7] |
| Completar ficha: horario, servicios, fotos, teléfono | Recepción | Cero | Ficha al 100 % el [fecha +7] |
| Pedir reseña al paciente satisfecho al finalizar tratamiento, **sin incentivo** | Recepción | Cero | ≥ 15 reseñas el [fecha +30] |

La tercera lleva "sin incentivo" en negrita por la regla NUNCA: incentivar está prohibido por
norma en EE. UU. desde el 21-10-2024 y por política de plataforma en todos los mercados.

## Los supuestos declarados

> **Asumido**: la marca propia no tiene línea base medible. Cinco de sus ocho métricas van en
> `[NO DISPONIBLE]` y la sexta en `[MUESTRA INSUFICIENTE — 6 reseñas]`. **No se ha estimado
> ninguna.** `ESTADO_LINEA_BASE: ABIERTA` para la marca propia; el panel sí está cerrado.
>
> El delta de la semana que viene se calculará **solo sobre el panel**. Hasta que la clínica
> pase de 15 reseñas, su propia serie no empieza, y la métrica de verificación de la acción 3 es
> exactamente eso.

## Por qué es el caso decisivo

El antipatrón sería entregar media página diciendo que faltan datos. Aquí el dueño se lleva la
foto completa de sus seis competidores —que es lo que preguntaba sin saberlo— y tres acciones de
coste cero que en 30 días le construyen la línea base que hoy no tiene.
