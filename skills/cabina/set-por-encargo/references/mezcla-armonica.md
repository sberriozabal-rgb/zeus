# Rueda Camelot: tabla, reglas y limites

Tabla verificada contra dos fuentes independientes (agosto 2026):
<https://neume.io/camelot-wheel> · <https://vibesdj.io/dj-tools/harmonic-mixing-chart>

## Las 24 claves

| Camelot | Open Key | Clave | Camelot | Open Key | Clave |
|---|---|---|---|---|---|
| 1A | 6m | Ab menor | 1B | 6d | B mayor |
| 2A | 7m | Eb menor | 2B | 7d | F# mayor |
| 3A | 8m | Bb menor | 3B | 8d | Db mayor |
| 4A | 9m | F menor | 4B | 9d | Ab mayor |
| 5A | 10m | C menor | 5B | 10d | Eb mayor |
| 6A | 11m | G menor | 6B | 11d | Bb mayor |
| 7A | 12m | D menor | 7B | 12d | F mayor |
| 8A | 1m | A menor | 8B | 1d | C mayor |
| 9A | 2m | E menor | 9B | 2d | G mayor |
| 10A | 3m | B menor | 10B | 3d | D mayor |
| 11A | 4m | F# menor | 11B | 4d | A mayor |
| 12A | 5m | Db menor | 12B | 5d | E mayor |

`A` = menor, `B` = mayor. En Open Key es al reves: `m` = menor, `d` = mayor.
Es la fuente de error mas comun al mezclar bibliotecas de distinta procedencia:
Beatport da notacion clasica, Mixed In Key da Camelot y Traktor da Open Key.

Para traducir sin equivocarse:

```bash
python3 scripts/dj_toolkit.py key "F#m"      # -> 11A | 4m | F# minor
python3 scripts/dj_toolkit.py key "1m"       # -> 8A  | 1m | A minor
python3 scripts/dj_toolkit.py key "Abm" --avanzado
```

## Movimientos

**Base (bajo riesgo).** Son los tres documentados por la rueda:

| Movimiento | Ejemplo | Efecto |
|---|---|---|
| Misma clave | 8A -> 8A | Energia plana, mezcla invisible |
| +1 misma letra | 8A -> 9A | Sube un paso |
| -1 misma letra | 8A -> 7A | Baja un paso |
| Mismo numero, otra letra | 8A -> 8B | Cambia el modo sin mover la tonica |

**Avanzados (riesgo medio, se oyen).**

| Movimiento | Ejemplo | Efecto |
|---|---|---|
| +7 (dominante) | 8A -> 3A | Salto de energia marcado |
| +2 / -2 | 8A -> 10A / 6A | Subida o bajada agresiva; mejor sobre percusion |

## Limites de la rueda: lo que no dice

1. **La clave detectada puede estar mal.** Es el limite dominante. Un test de
   laboratorio sobre 200 tracks dio 69% de acierto a rekordbox 7 y 60% a los
   metadatos de Beatport, frente al 89% de Mixed In Key
   (<https://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport>).
   Mezclar en armonico sobre claves mal detectadas produce choques reales.

2. **Un track no tiene una sola clave.** Muchos temas modulan o tienen un
   breakdown en otra tonalidad. La rueda asume una clave por track.

3. **Compatible no es igual a bueno.** Dos tracks en 8A pueden chocar por
   timbre, por densidad o por linea de bajo. La rueda descarta choques
   evidentes; no garantiza que la mezcla funcione.

4. **En generos sin contenido tonal marcado importa menos.** En techno duro,
   drum & bass o hip-hop instrumental el criterio armonico pesa mucho menos
   que la energia y el groove.

5. **El pitch mueve la clave.** Un cambio de tempo grande sin master tempo
   desplaza la tonalidad y anula el calculo.

Por eso el motor no trata la armonia como restriccion dura sino como uno de
cinco costes (clave, tempo, energia, repeticion de artista, coherencia de
genero), y por eso siempre imprime la razon de cada transicion: para que el DJ
pueda estar en desacuerdo con criterio.
