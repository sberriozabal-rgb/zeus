# Anexo A — Ficha comercial

Nombre técnico     : apertura-cierre-turno
Nombre comercial   : [A VALIDAR — nombre comercial de la casa pendiente]
Peldaño            : P1 · SKILL (pieza 5 de 6 del sistema instalable Motor B)
Línea              : Hostelería
Comprador nombrado : Restaurante o grupo de restauración independiente, España o México, plantilla 8-30 personas, decide el dueño o el encargado general. Se vende dentro del sistema instalable de 6 skills (Motor B), no suelta.
Trabajo que quita  : Redactar y mantener a mano el protocolo de apertura/cierre/cambio de turno y el registro de incidencias — hoy vive en la cabeza del encargado o en una hoja de papel sin actualizar.
Umbral que aporta  : Rotación de plantilla 63,8% anual en España (2.800-5.000 € por sustitución) y 80-120% en México (2-3x el salario del puesto), todas [A VALIDAR] con la trazabilidad en references/FUENTES.md; coste anual de rotación calculado con datos reales del cliente vía script determinista.
Precio propuesto   : Dentro de Instalación Esencial (2.500 €) y Completa (4.900 €). **Ratificado 15-sep-2026.**
Canal              : Venta presencial dentro del sistema instalable (Motor B). No se publica suelta en directorio hasta que el sistema completo tenga el primer caso vendido.
Motor              : B · Instalación
Frase de anuncio   : "El checklist que se ejecuta, no el que se firma sin mirar."
Estado / Versión   : ACORDADO / v1.1.2
Auditoría          : **19/20** (`validar_skill.py`, 15-sep-2026, v1.1.2). El validador devuelve 20/20 mecánico; no se firma el 20 porque el punto 19 exige URLs verificadas una a una y no se han reconfirmado todas. **La atribución del umbral queda CERRADA** en esta versión: las cuatro cifras de rotación tienen autor nombrado, año y URL (Synergie España 2026, Linkers, CANIRAC). Historial: la v1.1.0 declaró 19/20 cuando valía 16/20, y la v1.1.1 mantuvo el 19 con la atribución en corrección y tres defectos sin ver que el validador ha destapado ahora —`allowed-tools` como lista en vez de cadena, que rompe el empaquetado; dos pasos sin rama "si falta el dato"; y 7 reglas NUNCA donde la rúbrica pide 8—. Los tres cerrados en la 1.1.2.
Gates              : G1 [x] G2 [ ] G3 [x] G4 [x] G5 [x]

Notas:
- G1 (producto) se levanta con 19/20 ≥ 16/20 sobre la v1.1.2. **La salvedad del umbral en corrección ya no aplica: la atribución está cerrada.** Las cifras se pueden usar en material de venta citando a su autor y su límite (ninguna tiene tamaño de muestra publicado).
- **La línea "Umbral que aporta" de esta ficha está EN CORRECCIÓN CENTRALIZADA** (atribución de la cifra de rotación y de los costes de reposición, en revisión por la casa desde el 15-ago-2026). Hasta que cierre esa corrección, esa línea **no se copia a ningún material de venta, propuesta ni correo** — es la razón principal por la que G5 sigue sin levantar. El resto de la ficha es utilizable.
- G3 (precio) se marca con comprador nombrado y precio propuesto dentro del sistema, aunque la cifra siga [A VALIDAR] hasta ratificación de Sergio — el gate exige ficha con precio, canal y comprador, no cifra firme.
- G4 (legal) se marca porque no deriva de material source-available prohibido, no usa marca ajena, y su licencia es de uso comercial sin redistribución (ver LICENSE.txt).
- G2 (prueba) pendiente hasta ejecutar contra 3 casos reales de un cliente real, no solo los 4 casos sintéticos de fabricación.
- G5 (público) pendiente porque esta ficha aún no se ha usado en material de venta enviado a nadie.
- Regla de freno (4.5 del protocolo TROQUEL): esta es la pieza 5 de 6. No se fabrica la nº7 (`cuadro-mando-semanal`, que además no tiene umbral propio definido en doctrina) hasta que las 6 estén instaladas en un cliente que pagó, según el gate ya vigente del proyecto.
