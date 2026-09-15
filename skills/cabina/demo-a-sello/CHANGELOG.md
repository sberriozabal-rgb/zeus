# CHANGELOG — demo-a-sello

## [1.1.0] — 2026-09-15

**Alineación con el ADN de la casa y cierre del envoltorio de venta.** La auditoría mecánica
del 15-sep-2026 (`validar_skill.py`) dio **2/20** sobre la v1.0.0: es la skill mejor
documentada del catálogo CABINA en cuanto a fuentes externas, pero no tenía la estructura de
serie ni los ficheros del peldaño P1.

Añadido:

- Estructura de 13 secciones del ADN.
- Procedimiento reescrito en 6 pasos atómicos con el molde Entrada → Acción → Salida → Si.
- Reglas ampliadas a 10 SIEMPRE y 9 NUNCA con su porqué.
- 5 antipatrones con síntoma, causa raíz y corrección.
- Los 4 casos de prueba en `cases/`. El edge case es el **bootleg**, donde la skill vale
  precisamente por decir que no: se detiene en el paso 1, explica el coste del envío imposible
  (5 créditos, el envío del mes) y redirige a la vía de publicación que sí existe.
- Viñeta de **dato sucio típico** en `Entrada`: "mándalo a los grandes" sin poder nombrar una
  referencia del catálogo.
- `README.md`, `LICENSE.txt`, `metadata.json`.

Reforzado:

- El **presupuesto de créditos** pasa a ser el umbral central declarado: 5 créditos gratis al
  mes y 5 por envío es **un demo al mes**, y eso convierte la selección de sello en la decisión
  que more importa de todo el proceso.
- El precio de LabelRadar PRO (179,88 USD/año) lleva ahora advertencia explícita de
  **reverificar antes de recomendarlo**, por ser dato de abril de 2025, y es además una regla
  SIEMPRE.
- El calendario de tienda —Beatport 3 semanas, Spotify 7 días y una sola canción— sube de nota
  al pie a antipatrón con corrección, porque firmar a tiempo y entregar tarde deja el
  lanzamiento sin features.

Precio fijado en esta versión: **49 €** pago único.

## [1.0.0] — 2026-08-XX

Creación inicial. Filtro de admisibilidad, selección de sellos por encaje con tres preguntas,
tres familias de canal, administración del presupuesto de LabelRadar, criterio del clip de 20
segundos y calendario coordinado con Beatport y Spotify.
