# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `postmortem-de-bolo` |
| Nombre comercial | Parte de bolo |
| Peldaño | P1 · SKILL |
| Línea / Paquete | CABINA · **CABINA CORE** |
| Comprador nombrado | DJ residente o móvil con bolos recurrentes —una residencia, un circuito de salas, temporada de bodas— que quiere mejorar con datos y no solo con memoria. Decide y paga el propio DJ. |
| Quien NO es comprador | El DJ de un bolo suelto al trimestre: sin recurrencia no hay serie que comparar y el parte no tiene con qué cruzarse. |
| Trabajo que quita | Reconstruir de memoria qué pasó en una noche que salió mal, sin poder señalar el momento exacto. |
| Umbral que aporta | La separación visible de **HECHO / RELATO / HIPÓTESIS**: lo que sale del fichero, lo que recuerda el DJ, y lo que es cruce de ambos y hay que contrastar la próxima vez. Cierra con 1–3 decisiones comprobables, porque un parte sin decisión es entretenimiento. |
| Límite declarado | El fichero **no sabe si había gente**. Nunca afirma que un track «vació la pista»: eso es hipótesis y se marca como tal. Tampoco juzga la selección musical ni deduce éxito del número de tracks. |
| Precio propuesto | **49 €** pago único |
| Razón del precio | Tramo 30–49 € que convierte un 28 % mejor que el sub-10 €. Entre el 3 % y el 5 % de un bolo de boda medio (1.000–1.500 €). |
| Canal | Gumroad · catálogo (Motor A). Entrega por descarga (`venta/GUMROAD-ALTA.md`); decisión 8 del 15-sep-2026. |
| Motor | A · Catálogo |
| Frase de anuncio | «Qué se cortó pronto, qué se sostuvo y dónde saltó el tempo. Con la hora exacta, no con lo que recuerdes.» |
| Estado / Versión | ACORDADO / v1.1.0 |
| Auditoría | **19/20**. El validador de la casa (`validar_skill.py`, 15-sep-2026) devuelve 20/20 mecánico, frente al **1/20** de la v1.0.0. **No se firma el 20**: el punto 19 exige URLs verificadas, no solo presentes, y en esta pasada no se han reverificado una a una. La casa no redondea al alza. |
| Gates | G1 [x] G2 [ ] G3 [x] G4 [x] G5 [x] |

## Notas de gates

- **G1 (producto)** **levantado** el 15-sep-2026: 19/20 declarado, por encima del 16 que exige P1. Venía de 1/20. Se cerró el envoltorio —13 secciones del ADN, 6 pasos atómicos, 10 reglas SIEMPRE y 9 NUNCA, 5 antipatrones, los 4 casos de prueba, CHANGELOG, README, LICENSE y metadata—. El contenido de oficio ya estaba; faltaba la forma.
- **G3 (precio)** levantado el 15-sep-2026 por instrucción del dueño. Cifra cerrada: 49 €.
- **G2 (prueba)** pendiente: sin ejecuciones contra historiales reales de un comprador que haya pagado.
- **G4 (legal)** en orden: licencia de comprador sin derecho de redistribución.
- **G5 (público)** pendiente.
