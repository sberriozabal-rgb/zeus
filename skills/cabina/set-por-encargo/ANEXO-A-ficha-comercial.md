# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `set-por-encargo` |
| Nombre comercial | Set por encargo |
| Peldaño | P1 · SKILL |
| Línea / Paquete | CABINA · **CABINA CORE** |
| Comprador nombrado | DJ de club, residente, móvil o de eventos que prepara sets para slots concretos con condiciones dadas: franja, duración, BPM de relevo, prohibiciones del cliente. Decide y paga el propio DJ. |
| Quien NO es comprador | Quien solo necesita ordenar por Camelot y BPM: eso lo hacen DJ.Studio («Harmonize») y Mixed In Key Pro con un clic, mejor y más barato. |
| Trabajo que quita | Rehacer el set a mano cuando el slot cambia a última hora —menos tiempo, otra franja, otro BPM de relevo— y perder el criterio de sala en el camino. |
| Umbral que aporta | Las **seis curvas de energía por franja** con su rango: rampa 3→7 en calentamiento (no se le quema la pista al cabeza de cartel), meseta 6→9 en peak, arco 3→9 con pico al 70 % en set de noche, descenso, dientes. Más la regla de relevo de BPM y la justificación de cada transición en clave, tempo y energía. |
| Límite declarado | **No oye.** Lee clave, BPM y energía del export; no los detecta. Dato relevante y declarado: rekordbox 7 acierta la clave en 138/200 tracks (69 %) frente a 178/200 de Mixed In Key, así que alrededor de un tercio de las claves de una biblioteca analizada solo con rekordbox pueden estar mal, y desde aquí no hay forma de detectarlo. |
| Precio propuesto | **49 €** pago único |
| Razón del precio | Tramo 30–49 € de mejor conversión. Se justifica frente a las herramientas armónicas puras porque el criterio es contextual —franja, público, prohibiciones, cambio de slot— y eso no lo resuelve un clic. |
| Canal | Polar · catálogo (Motor A). Entrega por acceso revocable a repositorio privado. |
| Motor | A · Catálogo |
| Frase de anuncio | «Te cambian el slot a las siete de la tarde y a las ocho tienes el set reordenado, con el por qué de cada transición.» |
| Estado / Versión | ACORDADO / v1.1.0 |
| Auditoría | **19/20**. El validador de la casa (`validar_skill.py`, 15-sep-2026) devuelve 20/20 mecánico, frente al **2/20** de la v1.0.0. **No se firma el 20**: el punto 19 exige URLs verificadas, no solo presentes, y en esta pasada no se han reverificado una a una. La casa no redondea al alza. |
| Gates | G1 [x] G2 [ ] G3 [x] G4 [x] G5 [x] |

## Notas de gates

- **G1 (producto)** **levantado** el 15-sep-2026: 19/20 declarado, por encima del 16 que exige P1. Venía de 2/20. Se cerró el envoltorio —13 secciones del ADN, 6 pasos atómicos, 10 reglas SIEMPRE y 9 NUNCA, 5 antipatrones, los 4 casos de prueba, CHANGELOG, README, LICENSE y metadata—. El contenido de oficio ya estaba; faltaba la forma.
- **G3 (precio)** levantado el 15-sep-2026 por instrucción del dueño. Cifra cerrada: 49 €.
- **G2 (prueba)** pendiente.
- **G4 (legal)** en orden. Las menciones a rekordbox, DJ.Studio y Mixed In Key son cita de prestaciones y de un test publicado con URL, no uso de marca.
- **G5 (público)** pendiente.
