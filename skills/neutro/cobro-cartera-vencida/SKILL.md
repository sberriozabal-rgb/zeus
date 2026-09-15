---
name: cobro-cartera-vencida
description: Convierte un listado de facturas vencidas (cliente, importe, fecha de vencimiento, historial de pago) en un plan de cobro priorizado por tramo de antigüedad y causa del impago, con el mensaje redactado para cada cliente, el calendario de escalado con fechas concretas y un cuadro de mando con DSO y importe en riesgo. Úsala siempre que aparezca un listado de facturas pendientes, un reporte de antigüedad de saldos, un export de cuentas por cobrar, o cuando alguien pregunte a quién reclamar primero, qué escribirle a un cliente que no paga, cuándo cortar el suministro, cuándo pasar un expediente a jurídico, cómo calcular el DSO o por qué no entra el dinero aunque haya ventas. Aplica también con frases del oficio como "tengo mucho pendiente de cobro", "este cliente siempre paga tarde", "no sé por cuál empezar", "¿le mando otro recordatorio?" o "se me está yendo la caja en clientes". No la uses para cobro a consumidores particulares, valoración de cartera para venta, ni contabilidad fiscal.
license: Proprietary. Copyright 2026 Sergio. Uso comercial sin derecho de redistribución. All rights reserved.
metadata:
  version: "1.1.0"
  estado: "ACORDADO"
  auditoria: "19/20"
  sector: "neutro (B2B, cualquier oficio)"
---

# COBRO DE CARTERA VENCIDA — v1.1.0

## ROL

Eres el responsable de cobro de una empresa que factura a otras empresas. Decides a quién se reclama hoy, con qué palabras y qué pasa si no paga.

---

## DEFINICIÓN OPERATIVA

Convierte **un listado de facturas vencidas con cliente, importe, fecha de vencimiento y comportamiento de pago previo** en **un plan de cobro con una acción fechada por factura, el texto del mensaje redactado y un cuadro de mando de cuatro cifras** para **la persona que gestiona cobros en una empresa B2B (dueño, administración o crédito y cobranza)**, en **30 minutos de trabajo**.

---

## PROTOCOLO

Nueve pasos. Ninguno opcional.

### P1 · Normalizar la cartera

- **Entrada:** listado en cualquier formato (hoja de cálculo, export del ERP, foto de un listado, texto pegado).
- **Acción:** llevar cada línea a siete campos: `cliente · nº factura · importe · fecha de emisión · fecha de vencimiento · importe ya cobrado · último contacto (fecha y canal)`.
- **Salida:** tabla normalizada + recuento de líneas descartadas.
- **Si falta el dato:** si falta `fecha de vencimiento`, calcularla como emisión + plazo pactado; si tampoco hay plazo pactado, usar 30 días y marcar la línea `[PLAZO ASUMIDO 30D]`. Si falta `importe` o `cliente`, la línea sale del cálculo y se lista aparte bajo `LÍNEAS NO PROCESABLES`.

### P2 · Calcular antigüedad y asignar tramo

- **Entrada:** tabla de P1 + fecha de hoy.
- **Acción:** `días vencidos = hoy − fecha de vencimiento`. Asignar tramo:

| Tramo | Días vencidos |
|---|---|
| T0 · Corriente | ≤ 0 |
| T1 · Reciente | 1–30 |
| T2 · Consolidado | 31–60 |
| T3 · Grave | 61–90 |
| T4 · Crónico | 91–180 |
| T5 · Terminal | > 180 |

- **Alerta de prescripción (v1.1):** toda factura en T5 se contrasta contra el **plazo de prescripción de la jurisdicción**. Si le queda menos del **20 %** de su plazo, se marca `[PRESCRIPCIÓN PRÓXIMA — n meses]` y salta a A5 sin pasar por A4. Motivo: una deuda prescrita no es una deuda difícil, es cero. Ver el anexo regional si existe; si no, verificar antes de aplicar.
- **Salida:** cada factura con tramo + suma de importe por tramo + alertas de prescripción.
- **Si falta el dato:** una factura sin fecha de vencimiento tras P1 no existe; ya salió en `LÍNEAS NO PROCESABLES`. Sin plazo de prescripción conocido se marca `[PRESCRIPCIÓN NO VERIFICADA]` y **no** se da ninguna deuda por perdida.

### P3 · Medir concentración y riesgo

- **Entrada:** tabla con tramos.
- **Acción:** calcular cuatro cifras y nada más:
  1. **Total vencido** = suma de T1–T5.
  2. **% vencido sobre cartera** = total vencido ÷ (total vencido + T0).
  3. **DSO simple** = (saldo total de clientes ÷ ventas del periodo) × días del periodo. Si no hay cifra de ventas, escribir `DSO [NO CALCULABLE — falta cifra de ventas del periodo]` y seguir.
  4. **Importe en riesgo** = suma de T4 + T5.
- Marcar como **cliente crítico** todo cliente cuyo vencido represente **> 20 % del total vencido**, o cuyo vencido supere el **importe de un mes de facturación a ese cliente**.
- **Salida:** las cuatro cifras + lista de clientes críticos.
- **Si falta el dato:** cualquier cifra no calculable se escribe con la etiqueta `[NO CALCULABLE — falta X]`. Nunca se estima.

### P4 · Clasificar la causa del impago

- **Entrada:** cada factura vencida + último contacto registrado.
- **Acción:** asignar **exactamente una** de cuatro causas, aplicando la primera que se cumpla en este orden:

| Causa | Criterio de asignación |
|---|---|
| **D · Disputa** | Hay una objeción registrada sobre precio, cantidad, plazo o calidad. |
| **E · Error documental** | La factura fue rechazada, devuelta, o falta un dato exigido por el cliente (orden de compra, albarán, referencia, datos fiscales). |
| **T · Tesorería** | El cliente reconoce la deuda y ha pedido aplazamiento, o ha pagado parcialmente en los últimos 60 días. |
| **S · Silencio** | Ninguna de las anteriores: no hay respuesta registrada a ningún contacto. |

- **Salida:** cada factura con una letra: D, E, T o S.
- **Si falta el dato:** sin registro de contacto, la causa es **S** por defecto. Se marca `[CAUSA POR DEFECTO]` para que el ejecutor pueda corregirla en 5 segundos si sabe algo que el listado no dice.

### P5 · Asignar acción por la matriz tramo × causa

- **Entrada:** tramo (P2) + causa (P4).
- **Acción:** leer la acción en la matriz. Los escalones son acumulativos: no se salta un escalón salvo la excepción declarada.

| | **D · Disputa** | **E · Error doc.** | **T · Tesorería** | **S · Silencio** |
|---|---|---|---|---|
| **T1** 1–30 d | A1 Cerrar disputa | A0 Reemitir | A1 Confirmar plan | A1 Recordatorio |
| **T2** 31–60 d | A2 Escrito con fecha límite | A0 Reemitir + acuse | A2 Plan por escrito firmado | A2 Reclamación formal |
| **T3** 61–90 d | A3 Llamada del responsable | A3 Llamada del responsable | A3 Revisar cumplimiento del plan | A3 Llamada + preaviso |
| **T4** 91–180 d | A4 Preaviso de suspensión | A4 Preaviso de suspensión | A4 Preaviso de suspensión | A4 Preaviso de suspensión |
| **T5** > 180 d | A5 Expediente a jurídico | A5 Expediente a jurídico | A5 Expediente a jurídico | A5 Expediente a jurídico |

**Escalones:**

- **A0 · Corregir** — se reemite el documento. No es reclamación: mientras el documento esté mal, el reloj de cobro no corre a nuestro favor.
- **A1 · Recordar** — mensaje neutro, sin reproche, con importe y número de factura.
- **A2 · Reclamar por escrito** — mensaje con fecha límite explícita y consecuencia nombrada.
- **A3 · Llamar** — conversación de la persona con autoridad para negociar, seguida de correo con lo acordado.
- **A4 · Preavisar suspensión** — comunicación escrita de que el suministro o servicio se detiene en una fecha concreta.
- **A5 · Expedientar** — el caso sale de administración y va a jurídico o a un tercero.

**Excepción declarada (única):** un cliente marcado **crítico** en P3 salta directamente a **A3** aunque su tramo indique A1 o A2. Motivo: el coste de un día de retraso en un cliente crítico supera el coste de una llamada.

- **Salida:** una acción por factura, agrupada por cliente (un cliente = un contacto, no un contacto por factura).
- **Si falta el dato:** si el tramo es dudoso, se aplica el tramo **menor** (acción más suave). Un escalón de más rompe relaciones; uno de menos cuesta 15 días.

### P6 · Redactar el mensaje

- **Entrada:** escalón asignado + datos del cliente + facturas agrupadas.
- **Acción:** redactar el texto completo, listo para copiar y enviar. Reglas de forma, fijas:
  - Asunto: `[Nombre de nuestra empresa] · Facturas pendientes · [importe total]`
  - Máximo 120 palabras en A1 y A2.
  - Toda factura citada con número, importe y fecha de vencimiento.
  - Una sola petición por mensaje, en imperativo, con fecha.
  - En A2 y superiores: nombrar la consecuencia y su fecha.
  - Sin adjetivos sobre la conducta del cliente ("reiterado", "injustificado", "negligente").
- **Salida:** un bloque de texto por cliente, con canal recomendado (correo para A1–A2 y A4–A5; teléfono con correo de confirmación para A3).
- **Si falta el dato:** si no hay nombre de contacto, se usa el cargo (`Departamento de Administración`) y se marca `[FALTA CONTACTO NOMINAL]` como tarea pendiente.

### P7 · Fijar el calendario de escalado

- **Entrada:** acción asignada + fecha de hoy.
- **Acción:** para cada cliente, escribir dos fechas concretas: **fecha de envío** y **fecha de revisión**. Plazos de revisión por escalón:

| Escalón | Revisión |
|---|---|
| A0 | +5 días naturales |
| A1 | +10 días naturales |
| A2 | +7 días naturales |
| A3 | +5 días naturales |
| A4 | fecha de suspensión anunciada |
| A5 | +30 días naturales |

- Si en la fecha de revisión no hay pago ni acuerdo escrito, sube un escalón. Automático, sin decisión nueva.
- **Salida:** calendario con fechas del calendario real (no "en dos semanas").
- **Si falta el dato:** ninguno; hoy siempre se conoce.

### P8 · Emitir el cuadro de mando

- **Entrada:** todo lo anterior.
- **Acción:** una tabla de cuatro cifras (P3) + **tres decisiones que solo puede tomar el dueño**, cada una con importe asociado y opciones. Ejemplos de decisión: aceptar una quita, suspender suministro a un cliente activo, pagar un procedimiento judicial.
- **Coste del cobro (v1.1):** para cada cliente en T4 o T5, calcular `coste = horas estimadas de gestión × coste/hora del que gestiona`. Si `coste > 30 %` del importe reclamado, la decisión deja de ser "cómo cobro" y pasa a ser **"reclamo o provisiono"**, y sube al dueño con las dos cifras enfrentadas. El umbral del 30 % es convención de este artefacto: `[SIN VERIFICAR]`.
- **Salida:** media página. Si ocupa más, sobra.
- **Si falta el dato:** las decisiones se listan igual, con la cifra marcada `[NO CALCULABLE — falta X]`.

### P9 · Autocontrol

Aplicar la lista de la sección AUTOCONTROL. Corregir antes de entregar.

---

## REGLAS

### SIEMPRE

1. **Siempre agrupa por cliente, no por factura.** Cinco correos el mismo día al mismo interlocutor se leen como ruido y se archivan juntos.
2. **Siempre escribe la fecha límite en formato de calendario.** "A la mayor brevedad" no tiene fecha de vencimiento; el 30 de septiembre sí.
3. **Siempre nombra la consecuencia a partir de A2.** Una reclamación sin consecuencia enseña al cliente que la siguiente tampoco tendrá consecuencia.
4. **Siempre cierra el escalón A0 antes de reclamar.** Reclamar sobre un documento mal emitido regala al cliente el argumento y reinicia el plazo.
5. **Siempre entrega el mensaje redactado, no instrucciones para redactarlo.** El plan que exige escribir después no se ejecuta el mismo día.
6. **Siempre marca `[NO CALCULABLE — falta X]` en lugar de estimar una cifra.** Un hueco declarado se resuelve en una consulta; una estimación silenciosa se convierte en dato.
7. **Siempre deja las tres decisiones del dueño separadas del plan.** Quien ejecuta no debe decidir una quita ni un corte de suministro.
8. **Siempre verifica el plazo de prescripción antes de dar una deuda por perdida** (v1.1). Provisionar una deuda que todavía es exigible es regalar dinero; reclamar una prescrita es gastar en algo que ya no existe. Las dos son el mismo error de no haber mirado el calendario legal.
9. **Siempre separa el interés de demora del principal en el mensaje** (v1.1). Mezclarlos da al cliente un motivo para discutir el total y congelar el pago del principal, que es la parte que no admite discusión.

### NUNCA

1. **Nunca saltes más de un escalón,** salvo la excepción de cliente crítico declarada en P5. Saltar es lo que convierte un retraso en un litigio.
2. **Nunca amenaces con una consecuencia que no vayas a ejecutar.** La consecuencia no cumplida es la causa número uno de que el siguiente aviso se ignore.
3. **Nunca califiques la conducta del cliente por escrito** ("reiterado incumplimiento", "actitud negligente"). Es la frase que el cliente reenvía a tu comercial y que un juez lee en voz alta.
4. **Nunca ofrezcas un descuento por pronto pago sobre una factura ya vencida.** Premia el retraso y fija el precio real de tu producto por debajo del que vendiste.
5. **Nunca uses esta skill para deuda de consumidores particulares.** El cobro a personas físicas está sujeto a normativa de protección al consumidor con límites de contacto y contenido que este protocolo no contempla (ver REFERENCIAS, fuente 3).
6. **Nunca mezcles la reclamación con una oferta comercial nueva.** El cliente responde a la parte agradable y deja la incómoda sin contestar.
7. **Nunca cierres una negociación de plazo sin acuerdo escrito con importes y fechas.** Un acuerdo verbal no sube de escalón: se queda dando vueltas en A3 hasta T5.
8. **Nunca calcules interés sobre interés sin verificar que la jurisdicción lo permite** (v1.1). En varias, los intereses vencidos y no pagados no generan intereses salvo pacto expreso; una liquidación mal hecha invalida la reclamación entera.
9. **Nunca provisiones una deuda por antigüedad sin contrastarla con el plazo legal** (v1.1). "Lleva dos años, dalo por perdido" es una frase de tesorería, no un criterio: el plazo lo fija la ley de la jurisdicción, no la costumbre de la casa.

---

## MATRIZ DE APLICABILIDAD

| Contexto | Aplica | Ajuste |
|---|---|---|
| Empresa B2B con ≥10 facturas vencidas al mes | ✅ Sí | Ninguno. Caso central. |
| Autónomo o micro con 1–9 facturas | ✅ Sí | Salta P3 (concentración) y trabaja factura a factura. |
| Cartera de >2.000 líneas | ⚠️ Parcial | Aplica el protocolo por segmento (top 50 por importe + muestra del resto). Sin segmentar, P6 no cabe en 30 min. |
| Sector regulado con plazo de pago legal (obra pública, sanidad, alimentación) | ✅ Sí | Añade fila de plazo legal aplicable en la jurisdicción y ajusta T1–T5 a ese plazo, no a 30 días. |
| Cliente único que representa >60 % de la facturación | ⚠️ Parcial | Los escalones A4 y A5 pueden costar más que la deuda. Marca la decisión y devuélvela al dueño en P8. |
| Deuda ya en manos de un tercero (abogado, agencia) | ❌ No | El expediente salió del protocolo en A5. No se reclama en paralelo. |
| **Aquí NO aplica** | ❌ | Cobro a consumidores particulares · valoración de cartera para venta o titulización · concurso de acreedores declarado · contabilización o cierre fiscal. |

---

## ANTIPATRONES

Los cinco se detectan leyendo la salida, sin conocer el proceso.
Marcados `[DERIVADO]`: deducidos de los puntos de rotura del protocolo, no de una muestra de campo documentada.

### 1 · El recordatorio infinito `[DERIVADO]`
- **Síntoma observable:** el mismo cliente aparece con acción A1 en tres ciclos consecutivos y el importe no baja.
- **Causa raíz:** no se aplicó P7; la revisión no subió de escalón porque nadie fijó la fecha.
- **Corrección:** el escalado en P7 es automático por fecha, no por decisión. Si en la fecha de revisión no hay pago ni acuerdo escrito, sube.

### 2 · La amenaza sin fecha `[DERIVADO]`
- **Síntoma observable:** el mensaje de A2 dice "podríamos vernos obligados a tomar medidas" y no contiene ninguna fecha ni ninguna medida nombrada.
- **Causa raíz:** el redactor no quería comprometerse a ejecutar la consecuencia.
- **Corrección:** si no vas a ejecutar la medida, no la escribas y quédate en A1. Si la escribes, va con nombre y fecha.

### 3 · La reclamación sobre documento roto `[DERIVADO]`
- **Síntoma observable:** un cliente en T3 o T4 cuya causa es **E**, con tres contactos registrados y ninguna reemisión.
- **Causa raíz:** se clasificó como silencio lo que era un rechazo documental.
- **Corrección:** antes de subir de escalón con causa E, verificar que el documento se reemitió y hay acuse. El reloj no corría.

### 4 · El plan sin mensaje `[DERIVADO]`
- **Síntoma observable:** la salida contiene una tabla de acciones ("enviar reclamación formal") y ningún texto listo para enviar.
- **Causa raíz:** se saltó P6 por prisa.
- **Corrección:** el entregable incluye el texto. Una tabla de acciones no es un plan de cobro, es una lista de deseos.

### 5 · La cifra rellenada `[DERIVADO]`
- **Síntoma observable:** aparece un DSO o un porcentaje sin que en la entrada hubiera cifra de ventas del periodo.
- **Causa raíz:** se completó por plausibilidad para que el cuadro de mando "quedara lleno".
- **Corrección:** `[NO CALCULABLE — falta cifra de ventas del periodo]`. El cuadro incompleto es información; el cuadro inventado es un error con formato de dato.

---

## CASOS DE PRUEBA

Ver carpeta `cases/`. Los datos de los cuatro casos son sintéticos y están marcados como tales: `[DATOS DE EJEMPLO — NO REALES]`.

- `case_01_happy_path.md` — 12 facturas, datos completos, cliente crítico detectado
- `case_02_edge_case.md` — factura en disputa parcial y plazo legal sectorial distinto de 30 días
- `case_03_failure.md` — listado sin fechas de vencimiento ni cifra de ventas
- `case_04_integration.md` — encadenado con una skill de escandallo/margen para decidir si el cliente conviene

---

## AUTOCONTROL

Antes de entregar, verificar:

- [ ] ¿Cada cliente tiene **una** acción y **un** mensaje, no uno por factura?
- [ ] ¿Todas las fechas son fechas de calendario, no plazos relativos?
- [ ] ¿Todos los escalones A2 o superiores nombran una consecuencia con fecha?
- [ ] ¿Hay alguna cifra en el cuadro de mando que no salga de la entrada?
- [ ] ¿Algún cliente saltó más de un escalón sin ser crítico?
- [ ] ¿Algún mensaje califica la conducta del cliente?
- [ ] ¿Las tres decisiones del dueño están separadas y con importe?
- [ ] ¿El cuadro de mando cabe en media página?

Si alguna respuesta es mala, corregir antes de entregar.

---

## DEBATE ABIERTO DEL CAMPO

**¿Escalar rápido o preservar la relación comercial?**

- **Posición A — escalar por calendario.** El retraso es un préstamo sin interés que el proveedor concede sin haberlo aprobado. La Directiva 2011/7/UE reconoce esa lógica: en la UE el interés de demora y una compensación mínima de 40 € por costes de recobro son automáticos, sin necesidad de reclamación previa (fuente 1). Quien no escala financia al cliente con su propia caja.
- **Posición B — escalar por relación.** En mercados concentrados el cliente que se pierde no se reemplaza, y el coste de sustituirlo supera el importe reclamado. El escalado agresivo transfiere el problema de tesorería del cliente al departamento comercial.

**Cómo lo resuelve esta skill:** no lo resuelve por sí sola. Escala por calendario (P7) porque el sesgo documentado del oficio es esperar de más, pero devuelve al dueño las decisiones de corte y quita (P8), que son las únicas donde la relación pesa más que el importe. El umbral de "cliente crítico" (>20 % del vencido) es una elección de este artefacto, no un estándar del sector: `[SIN VERIFICAR]`.

---

## ESCALABILIDAD

- **1–9 facturas:** protocolo completo, ~10 min. Se salta P3.
- **10–200 facturas:** caso central, ~30 min.
- **200–2.000 facturas:** P1–P5 en hoja de cálculo con las fórmulas de tramo; P6 solo para el top 50 por importe y para todos los T4–T5.
- **>2.000 facturas:** este protocolo describe el criterio; la ejecución exige un sistema de cobro. Usar la skill para definir la matriz y los umbrales que se programan en él, no para procesar línea a línea.

---

## DEPENDENCIAS Y COMPATIBILIDAD

- **Independiente.** No requiere herramientas externas, conectores ni software adicional.
- **Encadena bien con:** cualquier skill de margen o rentabilidad por cliente (para responder "¿este cliente compensa el coste de cobrarle?"), y con una skill de revisión de contrato (para verificar el plazo pactado antes de fijar el tramo).
- **Entrega en formato:** tabla markdown + bloques de texto. Consumible por otra skill sin transformación.
- **No sustituye** asesoría jurídica. A5 marca el punto en que el caso deja este protocolo.

---

## ANEXOS REGIONALES

| Anexo | Estado | Contenido |
|---|---|---|
| **`annex/ANEXO-MX.md`** | ✅ **v1.1.0** | Interés moratorio legal, anatocismo, prescripción ordinaria mercantil y cambiaria, obligación de CFDI con complemento de pago. Todo verificado contra texto legal. |
| `annex/ANEXO-ES.md` | ⬜ pendiente | v1.2 |
| `annex/ANEXO-CO.md` | ⬜ pendiente | v1.2 |

Los anexos **no cambian el protocolo**: rellenan los tres huecos que la base neutra declara — plazo de prescripción (P2), interés aplicable (P6) y obligaciones formales del cobro parcial (P6).

---

## ROADMAP v1.2

1. Anexos regionales `-ES` y `-CO`, con el mismo nivel de verificación que `-MX`.
2. Sustituir los cinco antipatrones `[DERIVADO]` por antipatrones observados en ≥3 carteras reales. **Es el único punto que separa este artefacto de 20/20.**
3. Verificar el umbral del 30 % de coste del cobro contra práctica documentada, o mantenerlo declarando que es elección del autor.
4. Plantillas de A1–A5 en inglés y portugués, revisadas por hablante nativo del oficio.

---

## REFERENCIAS

1. **Comisión Europea**, *Late payment* (página de política sobre la Directiva 2011/7/UE), consultada el 2026-08-11. Cifras usadas: plazo de 60 días para empresas y 30 días para administraciones públicas; interés legal de al menos 8 puntos sobre el tipo de referencia del BCE; compensación mínima de 40 € por costes de recobro. https://single-market-economy.ec.europa.eu/smes/challenges-and-resilience/late-payment_en
2. **Comisión Europea — EU Payment Observatory**, *Annual Report 2025*, consultado el 2026-08-11. Cifras usadas (referidas a 2024): plazo medio de pago B2B de 60,3 días; plazo medio de administraciones a empresas de 69,8 días; 52 % de las empresas europeas declara problemas por impagos; 9,85 horas semanales dedicadas de media a perseguir pagos. Sostiene la elección de los tramos T2–T3 y el coste de tiempo que justifica el límite de 30 minutos de la DEFINICIÓN OPERATIVA. https://single-market-economy.ec.europa.eu/document/download/db1722d8-9cad-40fd-9ad4-f56a907317fa_en
3. **Consumer Financial Protection Bureau (EE. UU.)**, *Debt Collection Rule FAQs* — Regulation F, 12 CFR § 1006.14(b)(2), consultado el 2026-08-11. Sostiene la regla NUNCA·5: existen límites regulados de frecuencia de contacto (presunción de cumplimiento con ≤7 llamadas en 7 días naturales) que aplican al cobro de **deuda de consumo**, no a la deuda entre empresas — razón por la que esta skill excluye el cobro a particulares. https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/debt-collection/debt-collection-rule-faqs/

**Regionales verificadas (v1.1):** las cinco fuentes del anexo `-MX` están listadas con artículo, texto citado y URL en `annex/ANEXO-MX.md` y en `references/INDEX.md`.

**Marcado explícito:** los umbrales de tramo (1/30/60/90/180 días), el umbral de cliente crítico (>20 %), los plazos de revisión de P7, el umbral del 20 % restante para la alerta de prescripción y el umbral del 30 % de coste del cobro son convenciones de este artefacto elegidas por coherencia interna, no estándares verificados de ningún organismo. `[SIN VERIFICAR]`

---

**v1.1.0 · 2026-08-11 · Estado: ACORDADO · Auditoría: 19/20**
