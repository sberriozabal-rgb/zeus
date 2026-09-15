# Caso 1 · Happy path (revisión antes de bolo)

## Encargo real

> "Tengo boda el sábado. Te paso el XML, dime si hay algo que me vaya a petar."

## Entrada

- `collection.xml` de rekordbox, 8.400 tracks.
- Bolo: sábado, boda, ~120 invitados.
- Playlists del bolo identificadas: `SABADO_CEREMONIA`, `SABADO_COCTEL`, `SABADO_FIESTA`.
- Ejecutado en la máquina del DJ, así que `--comprobar-rutas` es válido.

## Comando

```bash
python3 scripts/dj_toolkit.py audit collection.xml --comprobar-rutas
```

## Salida esperada

```
Indice de salud: 71/100    (8.400 tracks)

CATEGORIA              N      %   RIESGO   CONSECUENCIA
ruta_rota             12   0.1%   CRITICO  El track no carga
sin_beatgrid         312   3.7%   CRITICO  No se puede sincronizar
sin_clave          1.204  14.3%   ALTO     Fuera de mezcla armonica
bitrate_bajo          88   1.0%   ALTO     Se oye en equipo de club
sin_cue_points     3.910  46.5%   MEDIO    Se entra a ciegas
duplicados           440   5.2%   MEDIO    Dudas de version en directo
```

## Top 3 para el bolo del sábado

1. **4 tracks de `SABADO_FIESTA` sin beatgrid** — son estos cuatro: [lista de 4]. Analizar en
   rekordbox y comprobar la rejilla a mano, porque dos tienen intro sin percusión. ~15 min.
2. **2 rutas rotas en `SABADO_CEREMONIA`** — incluido el track marcado como primer baile.
   Relocalizar desde el propio software. ~5 min. **Esto es lo primero de todo.**
3. **1 track a 128 kbps en `SABADO_COCTEL`** — se va a oír en el equipo de la sala. Sustituir
   por una versión de mayor bitrate o quitarlo. ~5 min.

## Mantenimiento sin prisa

Los 1.204 sin clave y los 3.910 sin cue points no son del bolo del sábado. Trabajo estimado:
el análisis de clave es en lote y automático (una tarde de máquina, cero atención); los cue
points exigen oír track a track y no se hacen en bloque. Si el objetivo es cerrar el lote,
Lexicon lo resuelve por 199 USD (<https://www.lexicondj.com/pricing>).

## Por qué este caso es el central

Demuestra la aportación real de la skill: de 8.400 tracks y más de 5.900 hallazgos, lo que
importa el sábado son **7 tracks concretos** y 25 minutos de trabajo. Un informe ordenado por
volumen habría empezado por los 3.910 sin cue points y no habría mencionado el primer baile.
