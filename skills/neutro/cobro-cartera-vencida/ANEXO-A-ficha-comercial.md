# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `cobro-cartera-vencida` |
| Nombre comercial | Plan de cobro de cartera vencida |
| Peldaño | P1 · SKILL |
| Línea / Paquete | Neutra · B2B, sin oficio específico |
| Comprador nombrado | Empresa B2B con **10 o más facturas vencidas al mes**, que factura a otras empresas y no a particulares. Decide y paga el dueño en una micro, o el responsable de administración / crédito y cobranza cuando hay estructura. Sirve igual a un autónomo con 1-9 facturas, saltando el paso de concentración. |
| Quien NO es comprador | Quien cobra a **consumidores particulares**: hay normativa de protección al consumidor con límites de frecuencia y contenido que este protocolo no contempla, y venderlo ahí expone al comprador. Tampoco quien tenga más de 2.000 líneas: ahí hace falta un sistema de cobro, y la skill sirve para definir lo que se programa en él. |
| Trabajo que quita | Perseguir pagos a ojo, por orden de antigüedad y con el correo escrito de cero cada vez. En Europa son **9,85 horas semanales** de media (EU Payment Observatory, 2024). |
| Umbral que aporta | La **matriz tramo × causa**: la acción no sale del calendario sino del cruce entre cuántos días lleva vencida y por qué no se ha pagado. Una factura parada 90 días porque falta una orden de compra no necesita una llamada del responsable, necesita que se reemita el documento. Más los cuatro escalones de causa (Disputa, Error documental, Tesorería, Silencio) y el escalado automático por fecha, que es lo que impide el recordatorio infinito. |
| Límite declarado | **No es asesoría jurídica** — A5 marca el punto en que el caso sale del protocolo. **No sirve para deuda de consumidores.** Los umbrales de tramo, cliente crítico y coste del cobro son convenciones de este artefacto `[SIN VERIFICAR]`, no estándares de ningún organismo. |
| Precio propuesto | **49–79 €** pago único `[A VALIDAR — pendiente de ratificación por escrito de Sergio]` |
| Razón del precio | Es la pieza neutra mejor posicionada del catálogo: sector agnóstico, dolor con cifra directa (DSO, importe en riesgo) y comprador que ya sabe que tiene el problema. Va por encima del tramo estándar de 49 € porque el entregable incluye los mensajes redactados y un cuadro de mando, no solo un análisis. |
| Canal | Polar · catálogo (Motor A). Entrega por acceso revocable a repositorio privado. |
| Motor | A · Catálogo |
| Frase de anuncio | «A quién reclamar primero, qué escribirle exactamente, y en qué fecha subes el tono si no paga.» |
| Estado / Versión | ACORDADO / v1.2.0 |
| Auditoría | **19/20** (`validar_skill.py`, 15-sep-2026). El validador devuelve 20/20 mecánico; **no se firma el 20** porque el punto 19 exige URLs verificadas, no solo presentes, y no se han reconfirmado una a una en esta pasada. Coincide con la nota que la skill ya se autodeclaraba, y con el motivo que su propio roadmap daba: los cinco antipatrones son `[DERIVADO]`, no observados en carteras reales. |
| Gates | G1 [x] G2 [ ] G3 [ ] G4 [x] G5 [ ] |

## Notas de gates

- **G1 (producto)** levantado el 15-sep-2026: 19/20 declarado, por encima del 16 que exige P1.
  Venía de **1/20** medido, no por falta de oficio sino de estructura: el contenido —la matriz,
  los cuatro escalones de causa, las reglas y las fuentes europeas— ya estaba y se conserva.
- **G2 (prueba)** pendiente. Los cuatro casos son sintéticos y están marcados `[DATOS DE
  EJEMPLO — NO REALES]`. El propio roadmap de la skill lo señala como **el único punto que la
  separa del 20/20**: sustituir los cinco antipatrones `[DERIVADO]` por antipatrones observados
  en tres carteras reales.
- **G3 (precio)** **pendiente**: hay comprador nombrado y canal, pero la cifra sigue
  `[A VALIDAR]` hasta ratificación por escrito. La línea neutra no tiene tarifa cerrada.
- **G4 (legal)** en orden. La skill declara que no es asesoría jurídica, excluye expresamente el
  cobro a consumidores con la fuente regulatoria que lo sostiene, y el anexo mexicano cita
  artículo y texto legal.
- **G5 (público)** pendiente: esta ficha no se ha usado en material de venta enviado a nadie.
