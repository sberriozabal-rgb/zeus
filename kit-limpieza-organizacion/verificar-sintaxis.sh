#!/usr/bin/env bash
#
# Comprueba la sintaxis de los organizadores.
#
# `bash -n fichero.sh` solo valida el ENVOLTORIO: el cuerpo real va dentro de
# un heredoc entrecomillado (<<'DOCS_EOF') y el intérprete no lo mira siquiera.
# Un error de sintaxis ahí dentro no se descubre hasta que alguien pega el
# script en su Terminal, que es el peor momento posible. Así que hay que
# extraer el cuerpo y validarlo por separado.
#
set -euo pipefail
cd "$(dirname "$0")"

fallos=0
encontrados=0

for f in organizador_*.sh; do
  [ -e "$f" ] || continue
  encontrados=$((encontrados + 1))

  if ! bash -n "$f" 2>/dev/null; then
    echo "❌ $f · el envoltorio tiene un error de sintaxis"
    fallos=$((fallos + 1))
    continue
  fi

  inicio=$(grep -n "DOCS_EOF'\$" "$f" | head -1 | cut -d: -f1 || true)
  fin=$(grep -n '^DOCS_EOF$' "$f" | head -1 | cut -d: -f1 || true)
  if [ -z "$inicio" ] || [ -z "$fin" ] || [ "$fin" -le "$inicio" ]; then
    echo "❌ $f · no se encuentran las marcas del heredoc DOCS_EOF"
    fallos=$((fallos + 1))
    continue
  fi

  if sed -n "$((inicio + 1)),$((fin - 1))p" "$f" | bash -n /dev/stdin; then
    echo "✅ $f · envoltorio y cuerpo con sintaxis correcta ($((fin - inicio - 1)) líneas)"
  else
    echo "❌ $f · el CUERPO tiene un error de sintaxis"
    fallos=$((fallos + 1))
  fi
done

if [ "$encontrados" -eq 0 ]; then
  echo "❌ no se encontró ningún organizador_*.sh que comprobar"
  exit 1
fi
[ "$fallos" -eq 0 ] || exit 1
echo "🟢 $encontrados script(s) verificados"
