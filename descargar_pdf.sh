#!/bin/bash

echo "📚 Descargando el libro 'Lina y el Bosque Mágico' en PDF..."
echo ""

# Descargar el archivo HTML optimizado
curl -L -o "Lina_Bosque_Magico_Español.html" \
  "https://raw.githubusercontent.com/sberriozabal-rgb/zeus/claude/wonderful-darwin-aao5yk/lina_español_imprimible.html"

if [ -f "Lina_Bosque_Magico_Español.html" ]; then
    echo "✅ Archivo descargado: Lina_Bosque_Magico_Español.html"
    echo ""
    echo "📖 Ahora:"
    echo "1. Abre el archivo en tu navegador"
    echo "2. Se abrirá automáticamente el diálogo de impresión"
    echo "3. Selecciona 'Guardar como PDF'"
    echo "4. ¡Listo!"
    echo ""
    echo "O ejecuta en Linux/Mac:"
    echo "  open Lina_Bosque_Magico_Español.html  (Mac)"
    echo "  xdg-open Lina_Bosque_Magico_Español.html  (Linux)"
else
    echo "❌ Error al descargar"
fi
