# CHANGELOG — presupuesto-y-contrato-evento

## [1.1.0] — 2026-09-15

**Alineación con el ADN de la casa y cierre del envoltorio de venta.** La auditoría mecánica
del 15-sep-2026 (`validar_skill.py`) dio **1/20** sobre la v1.0.0: el contenido de oficio es el
que más dinero protege del catálogo CABINA, pero le faltaba la estructura de serie y los
ficheros del peldaño P1.

Añadido:

- Estructura de 13 secciones del ADN, con el **aviso legal en cabecera**, antes que cualquier
  otra sección, por ser la frontera del producto.
- Procedimiento reescrito en 6 pasos atómicos con el molde Entrada → Acción → Salida → Si.
- Reglas ampliadas a 10 SIEMPRE y 9 NUNCA con su porqué.
- 5 antipatrones con síntoma, causa raíz y corrección, todos con su coste en euros.
- Los 4 casos de prueba en `cases/`. El edge case documenta la situación comercial más
  delicada del oficio: **el cliente que rechaza una cláusula CRÍTICA y pide precio cerrado**,
  resuelta declarando por escrito la pérdida asumida y ofreciendo alcance reducido en lugar de
  rebaja.
- Viñeta de **dato sucio típico** en `Entrada`: la consulta de una línea, que se responde
  produciendo sobre supuestos declarados en vez de con un cuestionario.
- `README.md`, `LICENSE.txt`, `metadata.json`.

Declarado con más claridad:

- **El baremo no es el precio del DJ**, es contexto de mercado. Sirve para saber si estás fuera
  de precio, no para fijar tarifa.
- **Regla dura de país**: no aplicar el baremo de un mercado a otro sin declarar que es una
  referencia importada. El dato de The Knot (1.800 USD de mediana en EE. UU.) lleva ahora esa
  advertencia pegada a la cifra.
- **El escalón medio real en España está en 1.000–1.500 €**, muy por encima del promedio que
  publican los portales de presupuestos, que atraen la demanda más sensible al precio. Un DJ
  que fija tarifa mirando solo ahí se ancla al segmento más bajo. Es ahora un antipatrón con
  su corrección.

Precio fijado en esta versión: **49 €** pago único.

## [1.0.0] — 2026-08-XX

Creación inicial. Presupuesto desglosado por conceptos, catálogo de cláusulas con nivel de
riesgo CRÍTICA/ALTA/MEDIA, las seis críticas, rider técnico del espacio concreto y baremos de
precio por mercado con fuente.
