# CHANGELOG — peticiones-a-repertorio

## [1.1.0] — 2026-09-15

**Alineación con el ADN de la casa y cierre del envoltorio de venta.** La auditoría mecánica
del 15-sep-2026 (`validar_skill.py`) dio **2/20** sobre la v1.0.0: contenido de oficio sólido
sin la estructura de serie ni los ficheros del peldaño P1.

Añadido:

- Estructura de 13 secciones del ADN.
- Procedimiento reescrito en 6 pasos atómicos con el molde Entrada → Acción → Salida → Si.
- Reglas ampliadas a 10 SIEMPRE y 9 NUNCA con su porqué.
- 5 antipatrones con síntoma, causa raíz y corrección.
- Los 4 casos de prueba en `cases/`. El edge case es una transcripción de audio real de la
  madre de la novia, con un **conflicto entre contratante y familiar** (un tema prohibido por
  la novia que la madre intenta colar): la skill declara el conflicto y no decide.
- Viñeta de **dato sucio típico** en `Entrada`: la línea de conversación mezclada con
  peticiones, y la referencia vaga que nunca se normaliza.
- `README.md`, `LICENSE.txt`, `metadata.json`.

Declarado con más claridad:

- **La asimetría de los umbrales.** `--umbral-duda` se puede bajar; subir los umbrales nunca,
  porque el coste del error no es simétrico: un falso negativo cuesta una pregunta al cliente,
  un falso positivo cuesta el momento del primer baile.
- **Cero dudosos es señal de fallo.** Una lista real de 25 peticiones produce entre 2 y 6
  `[A VALIDAR — calibración de oficio]`.
- Los umbrales 0.86 / 0.62 se marcan explícitamente como criterio de casa sin corpus publicado
  detrás.

Precio fijado en esta versión: **49 €** pago único.

## [1.0.0] — 2026-08-XX

Creación inicial. Cuatro cubos TENGO/NO TENGO/DUDOSO/PROHIBIDO con umbrales de similitud,
lista de compra por criticidad, documento de confirmación para el cliente en su idioma, y
sección APARTADAS para las líneas que parecen conversación.
