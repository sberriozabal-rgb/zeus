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
| Estado / Versión | ACORDADO / v1.0.0 |
| Auditoría | **2/20** contra la rúbrica de 20 puntos de la casa (`validar_skill.py`, 15-sep-2026). Faltan: cases/ (4 casos), CHANGELOG.md, tabla de reglas NUNCA, 5 antipatrones. La nota se declara sin redondear: **por debajo de 16 no se vende**. |
| Gates | G1 [ ] G2 [ ] G3 [x] G4 [x] G5 [ ] |

## Notas de gates

- **G1 (producto)** **NO levantado**: 2/20 frente al 16/20 que exige el peldaño P1. Es el bloqueo real de esta pieza: el precio está cerrado pero el producto no pasa todavía la rúbrica de la casa.
- **G3 (precio)** levantado el 15-sep-2026 por instrucción del dueño. Cifra cerrada: 49 €.
- **G2 (prueba)** pendiente.
- **G4 (legal)** en orden. Las menciones a rekordbox, DJ.Studio y Mixed In Key son cita de prestaciones y de un test publicado con URL, no uso de marca.
- **G5 (público)** pendiente.
