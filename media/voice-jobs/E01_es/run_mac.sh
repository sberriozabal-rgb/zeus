#!/usr/bin/env bash
# Pone voces a E01_es.mp4 con VoiceStudio en un Mac con Apple Silicon (M1/M2/M3/M4).
# Uso, desde la raíz del repo:   bash media/voice-jobs/E01_es/run_mac.sh
# Opciones extra se pasan a make_voices.py, p. ej.:   ... run_mac.sh --steps 16 --takes 1
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
VS_HOME="${OMNIVOICE_HOME:-$HOME/VoiceStudio}"
API="${OMNIVOICE_API_URL:-http://127.0.0.1:3900}"

[ "$(uname -m)" = "arm64" ] || { echo "Necesita un Mac con Apple Silicon (VoiceStudio no corre el modelo en Intel)."; exit 1; }

# 1. Dependencias: Homebrew, ffmpeg, uv
command -v brew >/dev/null || { echo "Instala Homebrew primero: https://brew.sh"; exit 1; }
command -v ffmpeg >/dev/null || brew install ffmpeg
command -v uv >/dev/null || brew install uv

# 2. VoiceStudio (solo la primera vez)
if [ ! -d "$VS_HOME" ]; then
  git clone --depth 1 https://github.com/debpalash/VoiceStudio.git "$VS_HOME"
fi
(cd "$VS_HOME" && uv sync)

# 3. Backend en segundo plano (si no está ya corriendo)
STARTED=0
if ! curl -sf --max-time 2 "$API/health" >/dev/null; then
  echo "Arrancando backend de VoiceStudio (log: $VS_HOME/backend.log)..."
  (cd "$VS_HOME" && nohup uv run uvicorn main:app --app-dir backend --host 127.0.0.1 --port 3900 \
     > "$VS_HOME/backend.log" 2>&1 &)
  STARTED=1
  for _ in $(seq 1 90); do
    curl -sf --max-time 2 "$API/health" >/dev/null && break
    sleep 2
  done
  curl -sf --max-time 2 "$API/health" >/dev/null || { echo "El backend no arrancó; revisa $VS_HOME/backend.log"; exit 1; }
fi
curl -s "$API/health"; echo
echo "Nota: la primera línea tarda más porque descarga el modelo k2-fsa/OmniVoice (~2.4 GB)."

# 4. Generar voces, mezclar y montar el video
(cd "$VS_HOME" && uv run python "$HERE/make_voices.py" --api "$API" "$@")

# 5. Apagar el backend si lo arrancamos nosotros
if [ "$STARTED" = 1 ]; then
  pkill -f "uvicorn main:app --app-dir backend --host 127.0.0.1 --port 3900" || true
fi

open "$HERE/E01_es_voicestudio.mp4" 2>/dev/null || true
