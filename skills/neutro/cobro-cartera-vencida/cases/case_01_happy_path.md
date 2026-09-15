# CASO 01 · HAPPY PATH
`[DATOS DE EJEMPLO — NO REALES]`

**Escenario:** empresa B2B de suministro. 12 facturas vencidas, datos completos, un cliente concentra >20% del vencido. Fecha de hoy: 2026-08-11.

## ENTRADA

| Cliente | Nº factura | Importe | Emisión | Vencimiento | Cobrado | Último contacto |
|---|---|---|---|---|---|---|
| Alfa SA | F-1012 | 48.000 | 2026-01-15 | 2026-02-14 | 0 | 2026-03-01 correo, sin respuesta |
| Alfa SA | F-1044 | 22.000 | 2026-02-10 | 2026-03-12 | 0 | 2026-03-01 correo, sin respuesta |
| Beta SL | F-1050 | 3.200 | 2026-06-20 | 2026-07-20 | 0 | ninguno |
| Beta SL | F-1071 | 1.900 | 2026-07-01 | 2026-07-31 | 0 | ninguno |
| Gamma SA | F-1005 | 6.500 | 2026-05-02 | 2026-06-01 | 3.000 | 2026-07-10, pidió aplazamiento |
| Delta SC | F-0980 | 12.400 | 2025-12-10 | 2026-01-09 | 0 | 2026-02-15 correo |
| Delta SC | F-0991 | 8.100 | 2026-01-05 | 2026-02-04 | 0 | 2026-02-15 correo |
| Épsilon | F-1060 | 2.700 | 2026-06-28 | 2026-07-28 | 0 | ninguno |
| Zeta SA | F-0955 | 15.000 | 2025-10-01 | 2025-10-31 | 0 | objeción de calidad registrada |
| Eta SL | F-1030 | 4.400 | 2026-04-15 | 2026-05-15 | 0 | ninguno |
| Theta | F-1041 | 900 | 2026-07-05 | 2026-08-04 | 0 | ninguno |
| Iota SA | F-1000 | 5.600 | 2026-03-01 | 2026-03-31 | 0 | factura devuelta, falta OC |

Ventas del periodo (para DSO): 620.000 en el trimestre (90 días). Saldo total de clientes: 210.000.

## SALIDA ESPERADA (resumen)

**Tramos y causa (P2, P4):**
- Alfa SA F-1012: T4 (179 d) · S — **crítico** (70.000 = >20% del vencido)
- Alfa SA F-1044: T4 (152 d) · S — crítico
- Beta SL: ambas T1 · S
- Gamma SA: T3 (71 d) · T (pago parcial + aplazamiento)
- Delta SC: ambas T4 · S
- Épsilon: T1 · S
- Zeta SA: T5 (285 d) · D (objeción de calidad) → **alerta prescripción a verificar**
- Eta SL: T2 · S
- Theta: T1 · S
- Iota SA: T3 (133 d) · E (documento devuelto, falta OC)

**Cuadro de mando (P3):**
- Total vencido: 130.700 (12 facturas menos parcial de Gamma)
- Importe en riesgo (T4+T5): 98.500
- DSO simple: (210.000 ÷ 620.000) × 90 = **30,5 días**
- Cliente crítico: Alfa SA (70.000)

**Acciones clave (P5):**
- Alfa SA → salta a A3 (llamada) por crítico, pese a que S+T4 daría A4. Regla: crítico salta a A3.
- Iota SA → A0 (reemitir con la OC) ANTES de reclamar. El reloj no corre mientras falte la OC.
- Zeta SA → A5 (jurídico) por T5, PERO al ser causa D con objeción registrada, primero cerrar disputa; verificar prescripción antes de expedientar.
- Gamma SA → A3 revisar cumplimiento del plan (causa T).

**Qué demuestra este caso:** priorización correcta, detección de cliente crítico, A0 antes de reclamar en causa E, y agrupación por cliente (Alfa recibe UN contacto por sus dos facturas, no dos).
