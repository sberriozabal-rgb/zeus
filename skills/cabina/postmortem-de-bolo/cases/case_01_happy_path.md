# Caso 1 · Happy path (residencia, historial completo y relato)

## Entrada

Historial de 42 tracks con hora, BPM y clave. Sesión de sábado en sala de club, 23:00 a 03:00.

Relato del DJ, recogido con las cinco preguntas de sala:

> "Se llenó a las 00:30. Sobre la 01:20 noté que la perdía, no sabría decirte por qué. El
> momento top fue con el track del cierre. El DJ anterior cerró a 124 y yo entré ahí."

## Salida esperada

```
HECHOS DEL FICHERO
Tracks: 42   Duracion: 3h 58m   Tempo medio: 126.4 BPM

Curva de tempo (tramos de 15 min)
23:00  122.0  |=====
23:45  124.5  |======
00:30  127.0  |========
01:15  131.5  |===========
01:30  125.0  |=======
02:30  128.0  |=========

Cortados pronto (<120s):  6      Sostenidos (>420s):  3
Saltos de tempo >=5 BPM:  4      Saltos armonicos >=3 pasos:  5
Artistas repetidos: 2            Tracks repetidos: 0
```

## El cruce del reloj

**RELATO** — El DJ sitúa la pérdida "sobre la 01:20".

**HECHO** — En la ventana 01:15–01:32 el fichero registra: un salto de +7 BPM (124 → 131) en
la transición de las 01:18, dos saltos armónicos de 6 pasos seguidos (8A → 2A → 8B), y tres
tracks consecutivos cortados por debajo de 90 segundos.

**HIPÓTESIS** — La subida de tempo llegó antes que la sala y los dos saltos armónicos
seguidos pudieron sonar a corte. Los tres tracks cortados seguidos parecen una reacción a algo
que el DJ estaba viendo. *Podría estar relacionado — contrastar la próxima vez.*

**HECHO** — El track del cierre fue el más sostenido de la noche: 7:12 en el aire, el único
por encima de 420 s en el último tramo. Coincide con el "momento top" del relato.

## Decisiones para el próximo (2)

1. **Retrasar el pico de tempo unos 20 minutos.** Esa noche se llegó a 131,5 BPM a la 01:15,
   45 minutos después de llenarse. Probar el pico hacia la 01:35.
   *Se comprueba:* mirando en el próximo parte si la curva llega al máximo después de la
   01:30 y si el DJ vuelve a notar pérdida en esa franja.

2. **Preparar tres tracks puente en 5A/6A para el tramo 01:15–01:45.** Ese tramo concentró
   los dos saltos de 6 pasos.
   *Se comprueba:* contando saltos armónicos ≥3 pasos en esa franja en el siguiente bolo.
   Objetivo: cero.

## Supuestos de esta versión

> Ventana de ±10 min aplicada al "sobre la 01:20" del relato, porque el recuerdo es
> aproximado. La clave es la calculada por rekordbox, con su margen conocido: los saltos
> armónicos son pregunta, no sentencia. No se controló el aforo real, solo el recuerdo.
