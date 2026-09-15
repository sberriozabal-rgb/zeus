# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `demo-a-sello` |
| Nombre comercial | Demo a sello |
| Peldaño | P1 · SKILL |
| Línea / Paquete | CABINA · **CABINA CARRERA** |
| Comprador nombrado | Productor o DJ que manda demos **sin manager**, con al menos un track terminado y la intención de publicar en sello. Decide y paga el propio productor. |
| Quien NO es comprador | Quien ya tiene manager o A&R que le coloca el material, y quien no tenga todavía un track terminado: aquí no se produce música. |
| Trabajo que quita | Mandar el mismo email genérico a cien sellos y no recibir una sola respuesta, sin saber si el problema era el canal, el texto, el clip o la fecha. |
| Umbral que aporta | Los **motivos de descarte automático documentados por los propios sellos**, el canal correcto verificado por sello (LabelRadar cuesta créditos y lo usan Toolroom, Armada, Defected, Drumcode, Anjunabeats, Monstercat; los pequeños van por email con link privado, nunca adjunto), y el calendario real de la industria: **Beatport al menos 3 semanas antes**, **Spotify con pitch 7 días antes** y solo una canción. Más la regla del clip: no empieces por el principio, la intro está hecha para mezclar. |
| Límite declarado | Un envío bien hecho no compra una firma: ordena el envío y elimina los descartes automáticos, no decide el criterio artístico del sello. Se manda **un solo track, el mejor** —tres dicen que no sabes cuál es bueno— y si no está masterizado se declara. |
| Precio propuesto | **49 €** pago único |
| Razón del precio | Tramo 30–49 € de mejor conversión. Es el único producto de la línea CARRERA, así que no tiene paquete propio: se vende suelto o dentro de CABINA COMPLETA. |
| Canal | Polar · catálogo (Motor A). Entrega por acceso revocable a repositorio privado. |
| Motor | A · Catálogo |
| Frase de anuncio | «El canal que pide cada sello, la frase que lo distingue de los otros cien envíos, y la fecha correcta para que Beatport y Spotify lleguen a tiempo.» |
| Estado / Versión | ACORDADO / v1.1.0 |
| Auditoría | **19/20**. El validador de la casa (`validar_skill.py`, 15-sep-2026) devuelve 20/20 mecánico, frente al **2/20** de la v1.0.0. **No se firma el 20**: el punto 19 exige URLs verificadas, no solo presentes, y en esta pasada no se han reverificado una a una. La casa no redondea al alza. |
| Gates | G1 [x] G2 [ ] G3 [x] G4 [x] G5 [x] |

## Notas de gates

- **G1 (producto)** **levantado** el 15-sep-2026: 19/20 declarado, por encima del 16 que exige P1. Venía de 2/20. Se cerró el envoltorio —13 secciones del ADN, 6 pasos atómicos, 10 reglas SIEMPRE y 9 NUNCA, 5 antipatrones, los 4 casos de prueba, CHANGELOG, README, LICENSE y metadata—. El contenido de oficio ya estaba; faltaba la forma.
- **G3 (precio)** levantado el 15-sep-2026 por instrucción del dueño. Cifra cerrada: 49 €.
- **G2 (prueba)** pendiente: sin envíos reales registrados de un comprador que haya pagado.
- **G4 (legal)** en orden. Los nombres de sello y plataforma son cita de canal y de plazo publicado, no uso de marca ni afiliación.
- **G5 (público)** pendiente. Al publicar, **nunca prometer respuesta ni firma**: el material de venta habla del envío bien hecho, no del resultado.
