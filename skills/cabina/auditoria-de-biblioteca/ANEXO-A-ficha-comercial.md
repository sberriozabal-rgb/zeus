# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `auditoria-de-biblioteca` |
| Nombre comercial | Auditoría de biblioteca |
| Peldaño | P1 · SKILL |
| Línea / Paquete | CABINA · **CABINA CORE** |
| Comprador nombrado | DJ de club, móvil o residente con biblioteca de más de ~3.000 tracks acumulada en varios años y al menos un bolo de pago al mes. Decide y paga el propio DJ. |
| Quien NO es comprador | El DJ que quiere **reparación automática en lote**: eso es Lexicon (199 USD vitalicio) y esta skill no lo hace ni lo promete. |
| Trabajo que quita | Descubrir en cabina que un track no carga, no tiene beatgrid o está en un bitrate que se oye mal en un equipo de club. |
| Umbral que aporta | La priorización por **riesgo real en cabina**, no por cantidad: `ruta_rota` y `sin_beatgrid` son CRÍTICO, `sin_rating` es BAJO. Traduce cada cifra a consecuencia («312 que no podrás sincronizar», no «312 sin beatgrid») y prioriza por proximidad al bolo. |
| Límite declarado | **Diagnostica, no repara.** Decisión deliberada: escribir en `master.db` (SQLite cifrada con SQLCipher4) o en los `.crate` de Serato puede destruir playlists, cue points y beatgrids. Solo lectura, siempre. |
| Precio propuesto | **49 €** pago único |
| Razón del precio | Una cuarta parte de Lexicon (199 USD) por un trabajo que Lexicon no hace: leer el estado con criterio de bolo. Entre el 3 % y el 5 % de un bolo de boda medio en España (1.000–1.500 €). |
| Canal | Gumroad · catálogo (Motor A). Entrega por descarga (`venta/GUMROAD-ALTA.md`); decisión 8 del 15-sep-2026. |
| Motor | A · Catálogo |
| Frase de anuncio | «Te digo qué tracks te van a fallar en el próximo bolo, y en qué orden arreglarlos.» |
| Estado / Versión | ACORDADO / v1.1.0 |
| Auditoría | **19/20**. El validador de la casa (`validar_skill.py`, 15-sep-2026) devuelve 20/20 mecánico, frente al **0/20** de la v1.0.0. **No se firma el 20**: el punto 19 exige URLs verificadas, no solo presentes, y en esta pasada no se han reverificado una a una. La casa no redondea al alza. |
| Gates | G1 [x] G2 [ ] G3 [x] G4 [x] G5 [x] |

## Notas de gates

- **G1 (producto)** **levantado** el 15-sep-2026: 19/20 declarado, por encima del 16 que exige P1. Venía de 0/20. Se cerró el envoltorio —13 secciones del ADN, 6 pasos atómicos, 10 reglas SIEMPRE y 9 NUNCA, 5 antipatrones, los 4 casos de prueba, CHANGELOG, README, LICENSE y metadata—. El contenido de oficio ya estaba; faltaba la forma.
- **G3 (precio)** levantado el 15-sep-2026 por instrucción del dueño. Cifra cerrada: 49 €.
- **G2 (prueba)** pendiente: sin ejecuciones registradas contra bibliotecas reales de un comprador que haya pagado.
- **G4 (legal)** en orden: licencia *uso permitido al comprador; prohibida la redistribución*. La mención a Lexicon es cita de precio publicado con URL, no uso de marca.
- **G5 (público)** pendiente hasta que la ficha se use en material de venta enviado.
