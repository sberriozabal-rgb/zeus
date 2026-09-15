# cobro-cartera-vencida

Skill de la **línea neutra** (B2B, cualquier oficio). Agent Skills, estándar abierto.

Convierte un listado de facturas vencidas en un plan de cobro con **una acción fechada por
factura, el mensaje ya redactado y un cuadro de mando de cuatro cifras**.

## Lo que lo diferencia de reclamar por antigüedad

La acción no sale del calendario: sale del cruce entre **cuántos días lleva vencida** y **por qué
no se ha pagado**.

| | D · Disputa | E · Error doc. | T · Tesorería | S · Silencio |
|---|---|---|---|---|
| **T1** 1–30 d | A1 | **A0 Reemitir** | A1 | A1 |
| **T2** 31–60 d | A2 | **A0 Reemitir** | A2 | A2 |
| **T3** 61–90 d | A3 | A3 | A3 | A3 |
| **T4** 91–180 d | A4 | A4 | A4 | A4 |
| **T5** > 180 d | A5 | A5 | A5 | A5 |

Una factura parada 90 días porque falta una orden de compra **no necesita una llamada del
responsable**: necesita que se reemita el documento. Mientras el papel esté mal, el reloj de
cobro no corre a tu favor.

## Las dos reglas que más dinero recuperan

1. **El escalado es automático por fecha, no por decisión.** Si en la fecha de revisión no hay
   pago ni acuerdo escrito, sube un escalón. Sin esto aparece el recordatorio infinito: el mismo
   cliente en A1 tres ciclos seguidos y el importe sin bajar.
2. **El entregable incluye el texto.** Una tabla que dice "enviar reclamación formal" no es un
   plan de cobro, es una lista de deseos. El plan que exige escribir después no se ejecuta el
   mismo día.

## Cuánto tarda

| Cartera | Tiempo |
|---|---|
| 1–9 facturas | ~10 min (se salta el paso de concentración) |
| 10–200 facturas | ~30 min · **caso central** |
| 200–2.000 | P1-P5 en hoja de cálculo; mensajes solo para el top 50 y todos los T4-T5 |
| > 2.000 | Define el criterio que se programa en un sistema de cobro |

Contexto: en Europa se dedican **9,85 horas semanales** de media a perseguir pagos
([EU Payment Observatory, 2024](https://single-market-economy.ec.europa.eu/document/download/db1722d8-9cad-40fd-9ad4-f56a907317fa_en)).

## Límites

**No es asesoría jurídica** — A5 marca el punto en que el caso sale del protocolo. **No sirve
para cobrar a consumidores particulares**: hay normativa con límites de frecuencia y contenido
que este protocolo no contempla. Los umbrales de tramo, cliente crítico y coste del cobro son
convenciones de este artefacto, `[SIN VERIFICAR]`, no estándares de ningún organismo.

## Ficheros

- `references/FUENTES.md` — las tres fuentes externas y la tabla de umbrales sin verificar.
- `references/INDEX.md` — índice de referencias, incluidas las regionales.
- `annex/ANEXO-MX.md` — interés moratorio, anatocismo, prescripción y CFDI, contra texto legal.
- `cases/` — los 4 casos de prueba, con datos sintéticos marcados como tales.

## Licencia

Propietaria. Uso comercial sin derecho de redistribución. Ver `LICENSE.txt`.
