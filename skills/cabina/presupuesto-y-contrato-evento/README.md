# presupuesto-y-contrato-evento

Skill de la línea **CABINA**, paquete **CABINA EVENTOS** (Agent Skills, estándar abierto).

Convierte la consulta de un cliente de evento en tres documentos: **presupuesto desglosado**,
**contrato con las cláusulas marcadas por riesgo** y **rider técnico del espacio concreto**.

> ⚠️ **No es asesoramiento jurídico.** Genera borradores a partir de prácticas habituales del
> sector. Todo contrato de uso recurrente debe revisarlo un abogado del país donde se firma.

## El valor no es redactar bonito

Es **saber qué cláusula falta y cuánto cuesta que falte**.

| Nivel | Significado |
|---|---|
| **CRÍTICA** | Sin ella, el DJ asume una pérdida real y previsible |
| **ALTA** | Sin ella hay conflicto probable |
| **MEDIA** | Conviene, se puede negociar |

**Las seis críticas:** depósito, cancelación escalonada, horas extra, requisitos del espacio,
fuerza mayor y sustitución.

## La regla de negociación

**Ante una petición de rebaja se quita alcance, jamás se baja el precio del servicio completo.**
Por eso el presupuesto va siempre desglosado por conceptos: sin desglose, la única respuesta a
"déjalo en 1.800" es sí o no, y el sí sale entero del margen.

## Baremos de mercado

En `references/baremos-precio.md`, cada uno con su fuente y su fecha. **Regla dura: no apliques
el baremo de un país a otro sin decir que es una referencia importada.**

- **España** — media nacional 350–500 €; boda completa 400–1.500 €; **escalón medio real
  1.000–1.500 €**; hora extra 75–250 €; desplazamiento 0,50–1 €/km.
- **EE. UU.** — mediana de 1.800 USD (The Knot 2025), cuartiles 800 / 1.600 / 2.700.
- **Contexto de negociación** — la boda media en España cuesta 25.183 €. 1.200 € es **menos del
  5%** del presupuesto total.

Un DJ que fija su tarifa mirando solo el promedio de los portales de presupuestos se está
anclando al segmento más sensible al precio del mercado.

## Ficheros

- `references/clausulas.md` — catálogo completo con nivel de riesgo.
- `references/baremos-precio.md` — precios por mercado, con fuente.
- `references/rider-tecnico.md` — requisitos por tipo de espacio.
- `assets/plantilla-presupuesto.md` — plantilla desglosada.
- `cases/` — los 4 casos de prueba.

## Licencia

Propietaria. Uso permitido al comprador; prohibida la redistribución. **No es asesoramiento
jurídico.** Ver `LICENSE.txt`.
