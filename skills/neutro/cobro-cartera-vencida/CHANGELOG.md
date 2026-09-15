# CHANGELOG — cobro-cartera-vencida

## [1.2.0] — 2026-09-15

**Cierre del envoltorio de venta.** La auditoría mecánica del 15-sep-2026 (`validar_skill.py`)
dio **1/20** frente al **19/20** que la skill declaraba en su propio frontmatter. La nota
declarada era honesta en sustancia —el contenido vale eso— pero el fichero no cumplía la
estructura de serie de la casa, y **una nota declarada que nadie puede reproducir con el
validador es, a efectos de venta, una nota regalada**.

Qué fallaba, y no era el oficio:

- Secciones con nomenclatura propia (`## ROL`, `## DEFINICIÓN OPERATIVA`, `## PROTOCOLO`,
  `## MATRIZ DE APLICABILIDAD`) en lugar de las 13 del ADN.
- Las nueve reglas SIEMPRE y las nueve NUNCA estaban como **listas numeradas**, no como tablas
  con columna de porqué.
- Los cinco antipatrones usaban `**Síntoma observable:**` y `**Causa raíz:**` con los dos puntos
  dentro de la negrita, que no es el molde de la serie.
- Los nueve pasos P1-P9 tenían el molde correcto pero repartido en viñetas, no en línea.
- Las tres fuentes europeas y estadounidenses vivían en el `SKILL.md`, no en `references/`, de
  modo que el recuento de URLs verificables daba **cero**.
- Sin `CHANGELOG.md`, sin `README.md`, sin `metadata.json` y sin ficha comercial `ANEXO-A`.

Qué se ha hecho:

- Reestructurado a las **13 secciones del ADN**, con los nueve pasos comprimidos a **8 pasos
  atómicos** con el molde en línea Entrada → Acción → Salida → Si falta el dato.
- Reglas convertidas a tabla: **10 SIEMPRE y 9 NUNCA**, cada una con su porqué.
- Los cinco antipatrones al molde de serie, conservando su marca `[DERIVADO]`.
- `references/FUENTES.md` con las tres fuentes externas, sus cifras usadas, su fecha de consulta
  y la tabla de **umbrales `[SIN VERIFICAR]`** que son convención de este artefacto.
- Viñeta de **dato sucio típico** en `Entrada`: el listado sin fecha de vencimiento y la
  ausencia de registro de contacto que manda todo a causa **S** por defecto.
- `README.md`, `metadata.json` y `ANEXO-A-ficha-comercial.md`.

**El contenido de oficio no se ha tocado**: la matriz tramo × causa, los cuatro escalones de
causa, los seis escalones de acción A0-A5, el escalado automático por fecha, el umbral de coste
del cobro y el anexo mexicano están exactamente como estaban.

Resultado: **19/20** declarado (20/20 mecánico, menos el punto 19 de criterio).

## [1.1.0] — 2026-08-11

Alerta de prescripción en T5, separación de interés de demora y principal en el mensaje, umbral
de coste del cobro al 30 %, y anexo regional `-MX` verificado contra texto legal.

## [1.0.0] — 2026-08-XX

Creación inicial. Cinco tramos de antigüedad, cuatro causas de impago, matriz tramo × causa con
seis escalones de acción, mensajes redactados por escalón, calendario de escalado automático por
fecha y cuadro de mando de cuatro cifras.
