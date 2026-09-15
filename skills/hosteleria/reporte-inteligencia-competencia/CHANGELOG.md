# CHANGELOG — reporte-inteligencia-competencia

## [1.1.0] — 2026-09-15

**Cierre del envoltorio de venta.** La auditoría mecánica del 15-sep-2026 (`validar_skill.py`)
dio **1/20**. Era la pieza más desnuda del catálogo: tenía un `SKILL.md` bueno **y nada más**.
Sin `README`, sin `CHANGELOG`, sin `LICENSE`, sin `metadata.json`, sin `cases/`, sin
`references/` y sin ficha comercial. Su cabecera declaraba «Auditoría interna 17/20», nota que
nadie podía reproducir.

Añadido:

- Estructura de **13 secciones del ADN**, con los 8 pasos del protocolo reescritos al molde en
  línea Entrada → Acción → Salida → Si falta el dato.
- Reglas ampliadas de 7+6 a **10 SIEMPRE y 9 NUNCA**, cada una con su porqué.
- Los 5 antipatrones al molde de serie, conservando su marca `[DERIVADO, NO OBSERVADO EN CAMPO]`
  donde correspondía.
- Los **4 casos de prueba** en `cases/`. El edge case documenta una divergencia real de 0,7★
  entre Google y TripAdvisor sobre el mismo local, resuelta reportando ambas y convirtiendo la
  divergencia en el hallazgo principal: **una plataforma abandonada**.
- `references/FUENTES.md` con las tres ediciones de BrightLocal, la cifra que sostiene cada corte
  del semáforo, y la tabla de lo que es convención de la skill y no dato de fuente.
- Viñeta de **dato sucio típico** en `Entrada`: dos locales homónimos en la misma ciudad y la
  divergencia entre plataformas.
- `README.md`, `LICENSE.txt`, `metadata.json` y `ANEXO-A-ficha-comercial.md`.

**El contenido de oficio no se ha tocado**: los cuatro cortes del semáforo con su cifra de
BrightLocal, la regla del 5.0, la regla de cobertura de seis fuentes, el uso de mediana y el pie
legal literal están exactamente como estaban.

Declarado por primera vez en ficha:

- El **solape comercial con `reporte-inteligencia`**, del que esta pieza es la vertical de
  hostelería. No se venden las dos al mismo comprador.
- La **decisión de modelo pendiente**: es la única pieza del catálogo cuyo valor está en la
  cadencia y no en el entregable, así que es candidata a suscripción y no a pago único.

## [1.0.0] — 2026-08-11

Primera versión. 10 capas, umbrales BrightLocal 2026 con fuente, 4 casos descritos en el
`SKILL.md`, plantilla de una página y pie legal. Auditoría interna declarada: 17/20.
