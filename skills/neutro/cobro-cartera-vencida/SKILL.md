---
name: cobro-cartera-vencida
description: Convierte un listado de facturas vencidas (cliente, importe, fecha de vencimiento, historial de pago) en un plan de cobro priorizado por tramo de antigüedad y causa del impago, con el mensaje redactado para cada cliente, el calendario de escalado con fechas concretas y un cuadro de mando con DSO y importe en riesgo. Úsala siempre que aparezca un listado de facturas pendientes, un reporte de antigüedad de saldos, un export de cuentas por cobrar, o cuando alguien pregunte a quién reclamar primero, qué escribirle a un cliente que no paga, cuándo cortar el suministro, cuándo pasar un expediente a jurídico, cómo calcular el DSO o por qué no entra el dinero aunque haya ventas. Aplica también con frases del oficio como "tengo mucho pendiente de cobro", "este cliente siempre paga tarde", "no sé por cuál empezar", "¿le mando otro recordatorio?" o "se me está yendo la caja en clientes". No la uses para cobro a consumidores particulares, valoración de cartera para venta, ni contabilidad fiscal.
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso comercial sin derecho de redistribución. No es asesoría jurídica. Ver LICENSE.txt.
metadata:
  version: "1.2.0"
  estado: "ACORDADO"
  auditoria: "19/20"
  sector: "neutro (B2B, cualquier oficio)"
---

# cobro-cartera-vencida

## Qué hace

Convierte **un listado de facturas vencidas con cliente, importe, fecha de vencimiento y
comportamiento de pago previo** en **un plan de cobro con una acción fechada por factura, el
texto del mensaje ya redactado y un cuadro de mando de cuatro cifras**, para **la persona que
gestiona cobros en una empresa B2B —dueño, administración o crédito y cobranza—**, en **30
minutos de trabajo**.

La aportación no es recordar que hay que reclamar: es **ordenar por causa y no por antigüedad**,
y entregar el mensaje escrito. Un plan que dice "enviar reclamación formal" no se ejecuta el
mismo día; uno que trae el texto listo para copiar, sí. Y separar las tres decisiones que solo
puede tomar el dueño —una quita, un corte de suministro, pagar un procedimiento— del trabajo que
puede ejecutar administración sin preguntar nada.

## Cuándo se dispara

- "tengo mucho pendiente de cobro y no sé por dónde empezar"
- "este cliente siempre paga tarde"
- "¿le mando otro recordatorio?"
- "se me está yendo la caja en clientes"
- "¿cuándo corto el suministro?"
- "¿esto ya lo paso a un abogado?"
- "vendo mucho pero no entra el dinero"
- "¿cuánto tengo realmente en riesgo?"
- "llevo tres correos y no contesta"
- jerga del gremio: "cartera vencida", "aging", "antigüedad de saldos", "DSO", "días de
  cobro", "impagado", "moroso", "reclamación", "quita", "provisión", "prescripción",
  "interés de demora", "expediente a jurídico", "cuentas por cobrar"

## Quién lo ejecuta

Quien gestiona cobros: el dueño en una micro, o administración / crédito y cobranza en una
empresa con estructura, con **30 minutos** de atención para una cartera de 10 a 200 facturas.
Con 1 a 9 facturas baja a **10 minutos** y se salta el paso de concentración. Por encima de 200
hace falta segmentar, y por encima de 2.000 la skill define el criterio que se programa en un
sistema, no procesa línea a línea.

## Entrada

- **Obligatorio:** el listado de facturas, en cualquier formato — hoja de cálculo, export del
  ERP, foto de un listado, texto pegado. No hace falta limpiarlo antes.
- **Obligatorio:** por línea, al menos `cliente`, `importe` y `fecha de vencimiento`. Sin
  cliente o sin importe la línea sale del cálculo y se lista aparte.
- **Recomendado:** fecha de emisión, importe ya cobrado y último contacto con fecha y canal. El
  último contacto es lo que permite clasificar la causa; sin él, todo cae en "silencio".
- **Recomendado:** la cifra de ventas del periodo, que es lo único que permite calcular el DSO.
- **Recomendado:** la jurisdicción, para el plazo de prescripción y el interés aplicable.
- **Dato sucio típico:** el listado sin fecha de vencimiento. Se calcula como emisión más plazo
  pactado; si tampoco hay plazo pactado se usan 30 días y la línea se marca
  `[PLAZO ASUMIDO 30D]`. El segundo dato sucio es la ausencia de registro de contacto, que
  manda la factura a causa **S · Silencio** por defecto, marcada `[CAUSA POR DEFECTO]` para que
  el ejecutor la corrija en cinco segundos si sabe algo que el listado no dice.

## Umbral que sostiene el producto

**Los cinco tramos de antigüedad y la matriz tramo × causa.** Ordenar solo por días vencidos es
el error que convierte un error de facturación en un litigio: una factura parada 90 días porque
falta una orden de compra no necesita una llamada del responsable, necesita que se reemita el
documento. De ahí que la acción salga del cruce y no del calendario solo.

| Tramo | Días vencidos | | Causa | Criterio |
|---|---|---|---|---|
| T0 · Corriente | ≤ 0 | | **D** Disputa | Objeción registrada sobre precio, cantidad, plazo o calidad |
| T1 · Reciente | 1–30 | | **E** Error documental | Factura rechazada, devuelta, o falta un dato exigido |
| T2 · Consolidado | 31–60 | | **T** Tesorería | Reconoce la deuda, pidió aplazamiento o pagó parcial en 60 días |
| T3 · Grave | 61–90 | | **S** Silencio | Ninguna de las anteriores: sin respuesta registrada |
| T4 · Crónico | 91–180 | | | |
| T5 · Terminal | > 180 | | | |

Los umbrales de tramo (1/30/60/90/180), el de **cliente crítico (> 20 % del total vencido)**,
los plazos de revisión, el **20 % restante de plazo** que dispara la alerta de prescripción y el
**30 % de coste del cobro** son convenciones de este artefacto elegidas por coherencia interna,
**no estándares verificados de ningún organismo** `[SIN VERIFICAR]`.

Lo que sí tiene fuente y sostiene el diseño: en la UE el interés de demora y una compensación
mínima de **40 €** por costes de recobro son automáticos, sin reclamación previa (Directiva
2011/7/UE, <https://single-market-economy.ec.europa.eu/smes/challenges-and-resilience/late-payment_en>).
Y el plazo medio de pago B2B europeo era de **60,3 días** en 2024, con **52 %** de las empresas
declarando problemas por impagos y **9,85 horas semanales** dedicadas de media a perseguir
pagos (EU Payment Observatory, *Annual Report 2025*). Esas 9,85 horas son exactamente lo que
justifica el límite de 30 minutos de este protocolo.

## Procedimiento

1. **Entrada: el listado en bruto → Acción: normalizar cada línea a siete campos (cliente, nº de
   factura, importe, emisión, vencimiento, cobrado, último contacto) → Salida: tabla normalizada
   y recuento de líneas descartadas → Si falta el dato: sin vencimiento se calcula como emisión
   más plazo pactado, o 30 días marcando `[PLAZO ASUMIDO 30D]`; sin importe o sin cliente la
   línea va a `LÍNEAS NO PROCESABLES`.**

2. **Entrada: tabla normalizada y fecha de hoy → Acción: calcular días vencidos y asignar tramo
   T0-T5, contrastando toda factura en T5 contra el plazo de prescripción de la jurisdicción →
   Salida: cada factura con su tramo, el importe sumado por tramo y las alertas de prescripción
   → Si falta el dato: sin plazo de prescripción conocido se marca `[PRESCRIPCIÓN NO VERIFICADA]`
   y **no se da ninguna deuda por perdida**.**

3. **Entrada: tabla con tramos → Acción: calcular las cuatro cifras —total vencido, % vencido
   sobre cartera, DSO simple e importe en riesgo (T4+T5)— y marcar como crítico todo cliente que
   supere el 20 % del vencido o un mes de su facturación → Salida: las cuatro cifras y la lista
   de clientes críticos → Si falta la cifra de ventas: se escribe
   `DSO [NO CALCULABLE — falta cifra de ventas del periodo]` y se sigue; nunca se estima.**

4. **Entrada: cada factura vencida y su último contacto → Acción: asignar exactamente una causa
   de las cuatro (D, E, T, S), aplicando la primera que se cumpla en ese orden → Salida: cada
   factura con su letra → Si no hay registro de contacto: la causa es **S** y se marca
   `[CAUSA POR DEFECTO]`.**

5. **Entrada: tramo y causa → Acción: leer la acción en la matriz sin saltar escalones, salvo la
   única excepción declarada (cliente crítico salta directo a A3) → Salida: una acción por
   factura, **agrupada por cliente**, porque un cliente es un contacto y no un contacto por
   factura → Si el tramo es dudoso: se aplica el tramo menor, es decir la acción más suave; un
   escalón de más rompe relaciones y uno de menos cuesta 15 días.**

6. **Entrada: escalón asignado y facturas agrupadas → Acción: redactar el texto completo listo
   para copiar y enviar, con asunto fijo, máximo 120 palabras en A1 y A2, toda factura citada
   con número, importe y fecha, una sola petición en imperativo con fecha, y la consecuencia
   nombrada a partir de A2 → Salida: un bloque de texto por cliente con su canal recomendado →
   Si falta el contacto nominal: se usa el cargo y se marca `[FALTA CONTACTO NOMINAL]` como
   tarea pendiente.**

7. **Entrada: acción asignada y fecha de hoy → Acción: fijar dos fechas de calendario real por
   cliente —envío y revisión— según el plazo de revisión de cada escalón, de modo que el
   escalado sea automático por fecha y no por decisión nueva → Salida: calendario con fechas
   concretas, nunca "en dos semanas" → Si en la fecha de revisión no hay pago ni acuerdo
   escrito: sube un escalón, sin discusión.**

8. **Entrada: todo lo anterior → Acción: emitir el cuadro de mando de media página con las
   cuatro cifras y las tres decisiones que solo puede tomar el dueño, calculando además el coste
   del cobro de cada cliente en T4-T5 → Salida: media página; si ocupa más, sobra → Si el coste
   supera el 30 % del importe reclamado: la decisión deja de ser "cómo cobro" y pasa a ser
   "reclamo o provisiono", y sube al dueño con las dos cifras enfrentadas.**

## Salida

```markdown
# Plan de cobro — [Empresa] · [fecha]
[N facturas] · [N clientes] · Periodo analizado: [periodo]

## Cuadro de mando
| Cifra | Valor |
|---|---|
| Total vencido | [€] |
| % vencido sobre cartera | [%] |
| DSO simple | [días] o [NO CALCULABLE — falta X] |
| Importe en riesgo (T4+T5) | [€] |

Clientes críticos: [lista]

## Plan por cliente
| Cliente | Facturas | Importe | Tramo | Causa | Acción | Envío | Revisión |
|---|---|---|---|---|---|---|---|

## Mensajes listos para enviar
[un bloque de texto por cliente, con su canal]

## Tres decisiones del dueño
1. [decisión] — importe asociado: [€] — opciones: [A] / [B]

## Supuestos de esta versión
[plazos asumidos, causas por defecto, cifras no calculables, prescripción no verificada]
```

La matriz que resuelve el paso 5. Los escalones son acumulativos:

| | **D · Disputa** | **E · Error doc.** | **T · Tesorería** | **S · Silencio** |
|---|---|---|---|---|
| **T1** 1–30 d | A1 Cerrar disputa | A0 Reemitir | A1 Confirmar plan | A1 Recordatorio |
| **T2** 31–60 d | A2 Escrito con fecha límite | A0 Reemitir + acuse | A2 Plan por escrito firmado | A2 Reclamación formal |
| **T3** 61–90 d | A3 Llamada del responsable | A3 Llamada del responsable | A3 Revisar cumplimiento | A3 Llamada + preaviso |
| **T4** 91–180 d | A4 Preaviso de suspensión | A4 Preaviso de suspensión | A4 Preaviso de suspensión | A4 Preaviso de suspensión |
| **T5** > 180 d | A5 Expediente a jurídico | A5 Expediente a jurídico | A5 Expediente a jurídico | A5 Expediente a jurídico |

**A0 · Corregir** (reemitir; mientras el documento esté mal, el reloj no corre a nuestro favor) ·
**A1 · Recordar** (neutro, sin reproche) · **A2 · Reclamar por escrito** (fecha límite y
consecuencia nombrada) · **A3 · Llamar** (quien tiene autoridad para negociar, con correo de
confirmación) · **A4 · Preavisar suspensión** (fecha concreta) · **A5 · Expedientar**.

Plazos de revisión: A0 +5 días · A1 +10 · A2 +7 · A3 +5 · A4 la fecha anunciada · A5 +30.

## Límites

- **No es asesoría jurídica.** El escalón A5 marca exactamente el punto en que el caso sale de
  este protocolo y pasa a un profesional.
- **No sirve para deuda de consumidores particulares.** El cobro a personas físicas está sujeto
  a normativa de protección al consumidor con límites de frecuencia y contenido que este
  protocolo no contempla.
- No vale para valoración de cartera para venta o titulización, ni para concurso de acreedores
  ya declarado, ni para contabilización o cierre fiscal.
- No reclama en paralelo una deuda que ya está en manos de un tercero: si salió en A5, salió.
- Los umbrales de tramo, de cliente crítico y de coste del cobro son **convenciones de este
  artefacto** `[SIN VERIFICAR]`, no estándares de ningún organismo.
- Con más de 2.000 líneas describe el criterio, no lo ejecuta: ahí hace falta un sistema de
  cobro y esta skill sirve para definir la matriz y los umbrales que se programan en él.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Agrupar por cliente, no por factura | Cinco correos el mismo día al mismo interlocutor se leen como ruido y se archivan juntos |
| Escribir la fecha límite en formato de calendario | "A la mayor brevedad" no tiene fecha de vencimiento; el 30 de septiembre sí |
| Nombrar la consecuencia a partir de A2 | Una reclamación sin consecuencia enseña al cliente que la siguiente tampoco la tendrá |
| Cerrar el escalón A0 antes de reclamar | Reclamar sobre un documento mal emitido regala al cliente el argumento y reinicia el plazo |
| Entregar el mensaje redactado, no instrucciones para redactarlo | El plan que exige escribir después no se ejecuta el mismo día |
| Marcar `[NO CALCULABLE — falta X]` en lugar de estimar una cifra | Un hueco declarado se resuelve en una consulta; una estimación silenciosa se convierte en dato |
| Separar del plan las tres decisiones del dueño | Quien ejecuta no debe decidir una quita ni un corte de suministro |
| Verificar el plazo de prescripción antes de dar una deuda por perdida | Provisionar lo que aún es exigible regala dinero; reclamar lo prescrito gasta en lo que ya no existe |
| Separar el interés de demora del principal en el mensaje | Mezclarlos da al cliente un motivo para discutir el total y congelar el pago del principal |
| Aplicar el tramo menor cuando el tramo sea dudoso | Un escalón de más rompe relaciones; uno de menos cuesta quince días |

| NUNCA | Porqué |
|---|---|
| Saltar más de un escalón, salvo la excepción de cliente crítico | Saltar es lo que convierte un retraso en un litigio |
| Amenazar con una consecuencia que no se vaya a ejecutar | La consecuencia no cumplida es la causa número uno de que el siguiente aviso se ignore |
| Calificar por escrito la conducta del cliente | "Reiterado incumplimiento" es la frase que el cliente reenvía a tu comercial y que un juez lee en voz alta |
| Ofrecer descuento por pronto pago sobre una factura ya vencida | Premia el retraso y fija el precio real de tu producto por debajo del que vendiste |
| Usar esta skill para deuda de consumidores particulares | Hay límites regulados de contacto y contenido que este protocolo no contempla |
| Mezclar la reclamación con una oferta comercial nueva | El cliente responde a la parte agradable y deja la incómoda sin contestar |
| Cerrar una negociación de plazo sin acuerdo escrito con importes y fechas | Un acuerdo verbal no sube de escalón: se queda dando vueltas en A3 hasta T5 |
| Calcular interés sobre interés sin verificar que la jurisdicción lo permite | En varias, los intereses vencidos no generan intereses salvo pacto expreso, y una liquidación mal hecha invalida la reclamación entera |
| Provisionar una deuda por antigüedad sin contrastarla con el plazo legal | "Lleva dos años, dalo por perdido" es una frase de tesorería, no un criterio: el plazo lo fija la ley |

## Antipatrones

Los cinco se detectan leyendo la salida, sin conocer el proceso. Van marcados `[DERIVADO]`:
deducidos de los puntos de rotura del protocolo, no de una muestra de campo documentada.

1. **Síntoma**: el mismo cliente aparece con acción A1 en tres ciclos consecutivos y el importe no baja. `[DERIVADO]` **Causa raíz**: no se aplicó el paso 7 y la revisión nunca subió de escalón porque nadie fijó la fecha. **Corrección**: el escalado es automático por fecha, no por decisión; si en la fecha de revisión no hay pago ni acuerdo escrito, sube.

2. **Síntoma**: el mensaje de A2 dice "podríamos vernos obligados a tomar medidas" y no contiene ninguna fecha ni ninguna medida nombrada. `[DERIVADO]` **Causa raíz**: el redactor no quería comprometerse a ejecutar la consecuencia. **Corrección**: si no vas a ejecutar la medida, no la escribas y quédate en A1; si la escribes, va con nombre y fecha.

3. **Síntoma**: un cliente en T3 o T4 con causa **E**, tres contactos registrados y ninguna reemisión. `[DERIVADO]` **Causa raíz**: se clasificó como silencio lo que era un rechazo documental. **Corrección**: antes de subir de escalón con causa E, verificar que el documento se reemitió y hay acuse; el reloj no corría.

4. **Síntoma**: la salida contiene una tabla de acciones ("enviar reclamación formal") y ningún texto listo para enviar. `[DERIVADO]` **Causa raíz**: se saltó el paso 6 por prisa. **Corrección**: el entregable incluye el texto; una tabla de acciones no es un plan de cobro, es una lista de deseos.

5. **Síntoma**: aparece un DSO o un porcentaje sin que en la entrada hubiera cifra de ventas del periodo. `[DERIVADO]` **Causa raíz**: se completó por plausibilidad para que el cuadro de mando quedara lleno. **Corrección**: `[NO CALCULABLE — falta cifra de ventas del periodo]`; el cuadro incompleto es información, el cuadro inventado es un error con formato de dato.

## Casos de prueba

Los cuatro casos están en `cases/`. Los datos son sintéticos y están marcados como tales:
`[DATOS DE EJEMPLO — NO REALES]`.

**Happy path** (`cases/case_01_happy_path.md`): 12 facturas con datos completos y un cliente
crítico detectado. Sale el plan completo con mensajes redactados y las tres decisiones del dueño.

**Edge case** (`cases/case_02_edge_case.md`): cartera con causa documental dominante, donde
ordenar por antigüedad habría escalado sobre facturas que solo necesitaban reemisión.

**Failure** (`cases/case_03_failure.md`): listado sin fechas de vencimiento y sin cifra de
ventas. Se entrega el plan con los plazos asumidos declarados y el DSO marcado como no
calculable, en vez de pedir datos antes de producir.

**Integration** (`cases/case_04_integration.md`): encadenado con una skill de margen por cliente,
para responder a la pregunta que el cuadro de mando abre: *¿este cliente compensa el coste de
cobrarle?*

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.2.0 — ver `CHANGELOG.md`.
