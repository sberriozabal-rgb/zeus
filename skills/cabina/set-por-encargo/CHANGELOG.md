# CHANGELOG — set-por-encargo

## [1.1.0] — 2026-09-15

**Alineación con el ADN de la casa y cierre del envoltorio de venta.** La auditoría mecánica
del 15-sep-2026 (`validar_skill.py`) dio **2/20** sobre la v1.0.0: contenido de oficio sólido
—las seis curvas de energía son la pieza más original del catálogo CABINA— sin la estructura
de serie ni los ficheros del peldaño P1.

Añadido:

- Estructura de 13 secciones del ADN.
- Procedimiento reescrito en 6 pasos atómicos con el molde Entrada → Acción → Salida → Si.
- Reglas ampliadas a 10 SIEMPRE y 9 NUNCA con su porqué.
- 5 antipatrones con síntoma, causa raíz y corrección. Añadidos dos nuevos: el obligatorio
  colocado en mitad del peak por pasarlo sin posición fija, y el set correcto sobre el papel
  que suena deslavazado por confiar en claves con ~31% de error esperable.
- Los 4 casos de prueba en `cases/`. El edge case documenta el cambio de slot a una hora del
  bolo con **tres variables cambiando a la vez**, que es el escenario que más tiempo ahorra.
- Viñeta de **dato sucio típico** en `Entrada`: el pool sin columna de energía.
- `README.md`, `LICENSE.txt`, `metadata.json`.

Reforzado:

- El límite honesto ("**no oye**") sube de nota al pie a sección `Límites` con seis viñetas, e
  incluye la recomendación explícita de usar DJ.Studio o Mixed In Key Pro cuando lo único que
  se necesita es ordenar por Camelot y BPM.

Precio fijado en esta versión: **49 €** pago único.

## [1.0.0] — 2026-08-XX

Creación inicial. Seis curvas de energía por franja, regla de relevo de BPM, ordenación por
pool y brief con `setbuilder.py`, y declaración de huecos (energía inferida, obligatorios no
colocados, estancamiento armónico).
