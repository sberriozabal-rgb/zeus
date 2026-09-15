# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `peticiones-a-repertorio` |
| Nombre comercial | Peticiones a repertorio |
| Peldaño | P1 · SKILL |
| Línea / Paquete | CABINA · **CABINA EVENTOS** |
| Comprador nombrado | DJ móvil de bodas, corporativos y eventos privados que recibe listas de peticiones del cliente en texto sucio —WhatsApp, Excel mal escrito, notas de voz transcritas— y trabaja con biblioteca propia de miles de tracks. Decide y paga el propio DJ. |
| Quien NO es comprador | El DJ de club que pincha su propio criterio sin lista de cliente: no hay peticiones que cruzar. |
| Trabajo que quita | Cruzar a mano 20 peticiones mal escritas contra 8.000 tracks, y descubrir en el evento que una no estaba o estaba en la versión que no servía. |
| Umbral que aporta | Los **cuatro cubos** con umbral de similitud: TENGO, DUDOSO, COMPRAR, PROHIBIDO. Todo lo que no supere el umbral queda en DUDOSO y sube al cliente en su idioma, porque un falso positivo se descubre en el evento, que es el peor sitio posible. Y la lista de prohibidos se repite literalmente por escrito, que es la parte que genera conflicto. |
| Límite declarado | Nunca inventa que un track está en la biblioteca —es la única mentira que arruina el evento entero— ni afirma BPM, clave o duración que no venga del export. La elección Clean/Dirty o Radio/Extended la firma una persona, nunca se resuelve en silencio. |
| Precio propuesto | **49 €** pago único |
| Razón del precio | Tramo 30–49 € de mejor conversión. Un solo incidente evitado —la Dirty en una comunión, el track del primer baile que no estaba— cuesta más que la skill. |
| Canal | Polar · catálogo (Motor A). Entrega por acceso revocable a repositorio privado. |
| Motor | A · Catálogo |
| Frase de anuncio | «Qué tengo, qué hay que comprar, qué está en una versión que no sirve y qué me han pedido que no ponga. Con el documento para el cliente ya escrito.» |
| Estado / Versión | ACORDADO / v1.0.0 |
| Auditoría | **2/20** contra la rúbrica de 20 puntos de la casa (`validar_skill.py`, 15-sep-2026). Faltan: cases/ (4 casos), CHANGELOG.md, tabla de reglas NUNCA, 5 antipatrones. La nota se declara sin redondear: **por debajo de 16 no se vende**. |
| Gates | G1 [ ] G2 [ ] G3 [x] G4 [x] G5 [ ] |

## Notas de gates

- **G1 (producto)** **NO levantado**: 2/20 frente al 16/20 que exige el peldaño P1. Es el bloqueo real de esta pieza: el precio está cerrado pero el producto no pasa todavía la rúbrica de la casa.
- **G3 (precio)** levantado el 15-sep-2026 por instrucción del dueño. Cifra cerrada: 49 €.
- **G2 (prueba)** pendiente: sin ejecuciones contra listas y bibliotecas reales de un comprador que haya pagado.
- **G4 (legal)** en orden: licencia de comprador sin derecho de redistribución.
- **G5 (público)** pendiente.
