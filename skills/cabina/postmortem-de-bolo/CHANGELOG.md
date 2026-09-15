# CHANGELOG — postmortem-de-bolo

Formato: `[versión] — fecha`. Tipo de cambio y motivo, siempre.

## [1.1.0] — 2026-09-15

**Alineación con el ADN de la casa y cierre del envoltorio de venta.** La auditoría mecánica
del 15-sep-2026 (`validar_skill.py`) dio **1/20** sobre la v1.0.0: buen contenido de oficio,
sin la estructura de serie ni los ficheros que exige el peldaño P1.

Añadido:

- Estructura de 13 secciones del ADN.
- Procedimiento reescrito en 6 pasos atómicos con el molde Entrada → Acción → Salida → Si.
- Reglas ampliadas a 10 SIEMPRE y 9 NUNCA con su porqué.
- 5 antipatrones con síntoma, causa raíz y corrección.
- Los 4 casos de prueba en `cases/`. El edge case cubre ahora **dos** artefactos, el cruce de
  medianoche y el hueco largo sin registro, que es el que produce el falso "track de 75
  minutos".
- `references/FUENTES.md` con los cuatro umbrales del motor declarados como criterio de
  oficio `[A VALIDAR]` y configurables, más las fuentes de software y de precisión de clave.
- Viñeta de **dato sucio típico** en `Entrada`.
- `README.md`, `LICENSE.txt`, `metadata.json`.

Declarado con más claridad:

- Los umbrales de 120 s, 420 s, 5 BPM y 3 pasos Camelot **no tienen fuente externa**. Son
  criterio de la casa y se marcan `[A VALIDAR]`. Un DJ de techno y uno de bodas no comparten
  esas fronteras, y por eso son configurables.
- La advertencia de que no haberse localizado una herramienta comercial equivalente **no
  prueba que no exista** se mantiene en el producto, no solo en notas internas.

Precio fijado en esta versión: **49 €** pago único.

## [1.0.0] — 2026-08-XX

Creación inicial. Extracción de hechos del historial, las tres cajas
HECHO/RELATO/HIPÓTESIS, cruce del reloj con el relato de sala, contraste plan contra
ejecución y cierre con un máximo de tres decisiones comprobables.
