# CASO 02 · EDGE CASE
`[DATOS DE EJEMPLO — NO REALES]`

**Escenario:** disputa parcial (el cliente acepta parte de la factura y objeta el resto) + plazo legal sectorial distinto de 30 días. Fecha de hoy: 2026-08-11.

## ENTRADA

Proveedor de alimentación a cadena de supermercados. Sector con plazo de pago legal
sectorial de **30 días** (perecederos), no el genérico.

| Cliente | Nº factura | Importe | Vencimiento | Cobrado | Nota |
|---|---|---|---|---|---|
| SuperMart | F-2200 | 40.000 | 2026-07-05 | 25.000 | Cliente acepta 25.000, objeta 15.000 por merma en entrega |
| SuperMart | F-2210 | 18.000 | 2026-06-20 | 0 | Sin objeción, sin respuesta |

## EL RETO DEL CASO

1. **Disputa parcial:** la factura F-2200 no es enteramente D ni enteramente S. La parte
   aceptada (25.000, ya cobrada) está cerrada; los 15.000 objetados son causa **D**.
   → La skill debe **separar la línea**: no clasificar toda la factura como disputa.

2. **Plazo sectorial:** en perecederos el vencimiento pactado ya refleja el plazo legal
   corto. Los tramos se cuentan desde ese vencimiento, no desde un supuesto de 30 días
   genérico. F-2210 (vencida 2026-06-20) → 52 días → **T2**, no recalcular.

## SALIDA ESPERADA (resumen)

- **F-2200 (parte objetada, 15.000):** T1 (37 d) · D → A1 cerrar disputa. Pedir prueba de
  la merma; si no la aporta en fecha de revisión, la objeción decae y sube a A2.
- **F-2210 (18.000):** T2 (52 d) · S → A2 reclamación formal con fecha límite.
- **Un solo contacto a SuperMart** que trate las dos facturas: agradece el pago de los
  25.000, pide resolver los 15.000 con evidencia, y reclama en firme los 18.000.
- **Cuadro de mando:** total vencido 33.000 (15.000 objetados + 18.000). Ninguno en T4/T5,
  importe en riesgo = 0.

**Qué demuestra este caso:** que la skill separa el importe aceptado del objetado dentro de
una misma factura, respeta el vencimiento sectorial en vez de imponer 30 días, y no mezcla
el tono (gracias por lo pagado / reclama lo debido) en un mismo mensaje mal calibrado.
