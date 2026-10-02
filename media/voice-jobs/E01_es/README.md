# E01_es — voces con VoiceStudio (Mac)

El video original no tiene audio. `plan.json` tiene el guion (sacado de los subtítulos), los tiempos de cada línea, el diseño de voz de cada personaje, los efectos de sonido y la receta de mezcla.

## Cómo generarlo (Mac con Apple Silicon)

Desde la raíz del repo:

```bash
bash media/voice-jobs/E01_es/run_mac.sh
```

El script:

1. Instala `ffmpeg` y `uv` con Homebrew si faltan.
2. Clona VoiceStudio en `~/VoiceStudio` (solo la primera vez) y arranca el backend.
3. Genera cada línea con 3 tomas y se queda con la mejor que quepa en su ventana. Si ninguna cabe, regenera forzando la duración.
4. Mezcla las voces con los efectos y monta el resultado en `E01_es_voicestudio.mp4`.

La primera ejecución descarga el modelo `k2-fsa/OmniVoice` (~2.4 GB).

- Versión rápida para probar: `... run_mac.sh --steps 16 --takes 1`
- Salida: `E01_es_voicestudio.mp4`, más `lines/NN.wav` y `lines/report.json` (seed, duración y tiempo de generación de cada línea)

## Voces

OmniVoice solo entiende un vocabulario fijo para el diseño de voz: género, edad, tono, `whisper` y acentos ingleses. El acento hispano sale del idioma (`language=es`). La seed fija por personaje mantiene la misma voz en todas sus líneas.

| Personaje | instruct | seed |
|---|---|---|
| Concha | female, middle-aged, high pitch | 1101 |
| Sombrero | male, young adult, low pitch | 2202 |

Para cambiar una voz, edita `instruct` o `seed` en `plan.json` y vuelve a correr el script. Probar con otra seed es la forma más rápida de buscar otro timbre.

## Pendiente de validar en el Mac

- El script se probó contra un backend simulado. Falta validarlo con VoiceStudio real.
- La línea 07 usa la etiqueta `[laughter]` para la risa.
- Que el reparto de "Todo." al Sombrero sea el correcto.
