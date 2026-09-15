# CASO 04 · INTEGRATION (encadenado con otra skill)
`[DATOS DE EJEMPLO — NO REALES]`

**Escenario:** un cliente en T4 exige mucho esfuerzo de cobro. Antes de decidir si se
reclama a fondo o se provisiona, se encadena con una skill de **margen/rentabilidad por
cliente** (p. ej. `escandallo-costos` o cualquier skill de margen) para responder:
**¿este cliente compensa el coste de cobrarle?** Fecha de hoy: 2026-08-11.

## ENTRADA (salida de cobro-cartera-vencida, P8)

Cliente **Kappa SA**, marcado en T4:
- Importe reclamado: 9.000
- Coste estimado de gestión de cobro (P8): 12 h × 45/h = 540 → 6% del importe. Bajo el umbral del 30%, así que se reclama sin dudar por el lado del cobro.
- PERO: el dueño pregunta si Kappa, como cliente, aporta margen o solo volumen.

## HANDOFF — qué entrega esta skill a la de margen

Formato de entrega (tabla markdown, consumible sin transformación):

| Campo | Valor |
|---|---|
| Cliente | Kappa SA |
| Importe vencido | 9.000 |
| Tramo | T4 |
| Coste de cobro estimado | 540 (6%) |
| Pregunta para la skill de margen | ¿Margen anual de Kappa > coste de mantenerlo como cliente moroso? |

## SALIDA ESPERADA DEL ENCADENADO

La skill de margen recibe la tabla y responde con el margen real de Kappa. Dos desenlaces:

- **Si Kappa deja margen positivo alto:** cobrar a fondo (A4/A5) y **conservar** la relación.
  El coste de cobro (540) es trivial frente al margen.
- **Si Kappa deja margen negativo o marginal:** la decisión del dueño en P8 cambia de
  "cómo cobro" a **"cobro lo que pueda y no le vuelvo a vender a crédito"**. La skill de
  cobro no toma esta decisión: la enmarca y la sube.

**Qué demuestra este caso:** el criterio de integración de la FASE 5 — la skill declara
**qué entrega y en qué formato** (tabla con importe, tramo, coste de cobro y la pregunta
exacta), de modo que otra skill la consuma sin reprocesar. El cobro no vive aislado: se
conecta con la rentabilidad para que la decisión del dueño tenga las dos cifras enfrentadas.
