# ANEXO REGIONAL — MÉXICO (`-MX`)
**Versión:** 1.1.0 · **Estado:** VERIFICADO contra texto legal · **Fecha:** 2026-08-11

Este anexo **no cambia el protocolo**. Rellena los tres huecos que la base neutra
declara: plazo de prescripción (P2), interés aplicable (P6) y obligaciones formales
del cobro parcial (P6). Todo dato lleva su artículo.

---

## 1 · PRESCRIPCIÓN — rellena el hueco de P2

| Tipo de deuda | Plazo | Fuente |
|---|---|---|
| Deuda mercantil ordinaria (factura entre empresas, sin título) | **10 años** | Código de Comercio, art. 1047 |
| Deuda documentada en **pagaré o letra de cambio** | **3 años** (36 meses) desde el vencimiento | LGTOC, art. 165 |

**Regla operativa del anexo:** la factura simple prescribe a 10 años, pero el título de
crédito (pagaré) a 3. Esto invierte la intuición: **el documento que da más fuerza para
cobrar es el que caduca antes.** Por eso, para todo cliente en T3 o superior sin título
firmado, la decisión que sube al dueño en P8 es: **¿pedimos pagaré?** — porque a partir de
ese momento el reloj real pasa a ser de 36 meses y hay que vigilarlo.

**Lo que este anexo NO cubre** (es de abogado, escalón A5):
- Los actos concretos que **interrumpen** la prescripción (reinician el conteo).
- El concurso mercantil declarado.
- La vía procesal (juicio ejecutivo mercantil, requisitos del título).

---

## 2 · INTERÉS MORATORIO — rellena el hueco de P6

- **Interés legal mercantil:** **6 % anual** cuando no hay pacto expreso de otra tasa
  (Código de Comercio, art. 362). Si las partes pactaron una tasa en el contrato o la
  factura, rige la pactada.
- **Anatocismo (interés sobre interés):** en materia mercantil, **los intereses vencidos
  y no pagados no generan intereses** salvo pacto posterior expreso, o se capitalizan por
  convenio (Código de Comercio, art. 363). Aplica directamente la regla NUNCA·8 de la base:
  no se calcula interés sobre interés sin verificar que hay pacto.

**En el mensaje (P6):** separar siempre el principal del interés moratorio, y expresar el
interés como "6 % anual sobre el principal desde la fecha de vencimiento" (o la tasa
pactada), nunca como una cifra redonda sin base.

---

## 3 · COBRO PARCIAL Y COMPROBANTES — rellena el hueco de P6

- Todo cobro (total o parcial) de una factura ya timbrada exige emitir el **CFDI con
  complemento para recepción de pagos** (comprobante de "pago en parcialidades o
  diferido"), conforme a la **Regla 2.7.1.32 de la Resolución Miscelánea Fiscal (SAT)**.
- **Consecuencia operativa:** cuando un cliente en causa **T (tesorería)** paga
  parcialmente, la tarea no termina con el ingreso: hay que emitir el complemento de pago.
  Se añade como paso pendiente en la salida de P6 para ese cliente.

---

## 4 · AJUSTE DE TRAMOS PARA MÉXICO

México **no fija un plazo de pago legal máximo entre empresas** (a diferencia de la UE,
que fija 60 días). Por tanto, en México los tramos T1–T5 se cuentan desde la **fecha de
vencimiento pactada en la factura o el contrato**, no desde un plazo legal. Si no hay plazo
pactado, se mantiene el supuesto de 30 días de la base, marcado `[PLAZO ASUMIDO 30D]`.

---

## FUENTES (verificadas 2026-08-11)

1. **Código de Comercio (México)**, art. 362 — interés legal mercantil del 6 % anual a falta de pacto.
2. **Código de Comercio (México)**, art. 363 — los intereses vencidos no producen intereses salvo pacto.
3. **Código de Comercio (México)**, art. 1047 — prescripción ordinaria mercantil de 10 años.
4. **Ley General de Títulos y Operaciones de Crédito (LGTOC)**, art. 165 — prescripción de la acción cambiaria a los 3 años.
5. **SAT — Resolución Miscelánea Fiscal**, regla 2.7.1.32 — CFDI con complemento para recepción de pagos.

> Aviso: este anexo prepara material de gestión de cobro. No es asesoría jurídica ni
> fiscal. Los actos que interrumpen la prescripción, la vía procesal y el complemento de
> pago concreto deben validarse con profesional colegiado (abogado / contador).
