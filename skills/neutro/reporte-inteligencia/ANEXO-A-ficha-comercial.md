# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `reporte-inteligencia` |
| Nombre comercial | Reporte semanal de inteligencia competitiva |
| Peldaño | P1 · SKILL |
| Línea / Paquete | Neutra · sin oficio específico |
| Comprador nombrado | Quien dirige marca, operación o el negocio entero en un local o cadena pequeña con **reputación digital activa** —al menos un perfil con reseñas y competencia identificable en su plaza—. Decide el dueño o el responsable de marketing. |
| Quien NO es comprador | El negocio **sin competencia local identificable** (monopolio de plaza, B2B sin reputación pública) y quien busque un informe único: el valor está en la **serie semanal**, y un corte aislado no tiene deltas contra los que compararse. |
| Trabajo que quita | Mirar a ojo las fichas de los competidores cada cierto tiempo, sacar impresiones sin fecha ni cita, y no poder decir si algo ha cambiado o es la memoria del que mira. |
| Umbral que aporta | El **panel congelado 13 semanas con composición 3+2+1** y el **modo de captura declarado**. Lo primero hace que los deltas signifiquen algo; lo segundo impide presentar como medición una tabla levantada con buscador que solo alcanza 2 de las 8 métricas. Más los topes duros —6 hallazgos, 5 fallos, 3 acciones— que son lo que hace que el reporte se siga abriendo en la semana 8. |
| Límite declarado | Las cifras de BrightLocal son de consumidores de EE. UU. y la elasticidad de Luca es de restaurantes independientes en Yelp: **la dirección es extrapolable, las cifras exactas no**. El modo BÚSQUEDA **no cierra línea base**. No usa datos obtenidos saltándose términos de uso, y nunca recomienda solicitar, comprar, incentivar ni suprimir reseñas. |
| Precio propuesto | **49 €** pago único. **Ratificado 15-sep-2026.** |
| Razón del precio | Tramo 30-49 € de mejor conversión. Candidata natural a **suscripción** antes que a pago único, porque el producto es la serie semanal y no el corte: ahí la doctrina de la casa dice que la suscripción promedia casi el doble que el pago único, pero exige cadencia real que sostenerla. Decisión pendiente. |
| Canal | Polar · catálogo (Motor A). Entrega por acceso revocable a repositorio privado. |
| Motor | A · Catálogo |
| Frase de anuncio | «Seis competidores, ocho métricas y tres acciones para esta semana. Con la cita y la fecha de cada cosa, para que puedas comprobarlo.» |
| Estado / Versión | ACORDADO / v1.2.0 |
| Auditoría | **19/20** (`validar_skill.py`, 15-sep-2026). El validador devuelve 20/20 mecánico; **no se firma el 20** porque el punto 19 exige URLs verificadas y no se han reconfirmado una a una. Coincide con el 18/20 que la skill declaraba *"pendiente de reauditoría tras v1.1.0"*: la reauditoría es esta. |
| Gates | G1 [x] G2 [ ] G3 [x] G4 [x] G5 [x] |

## Notas de gates

- **G1 (producto)** levantado el 15-sep-2026: 19/20, desde **2/20** medido. La nota baja era de
  estructura, no de oficio: el panel 3+2+1, el modo de captura bloqueante, las 8 métricas y las
  tres fuentes con sus límites ya estaban y se conservan.
- **G2 (prueba)** **parcialmente levantado**, y es el único caso del catálogo. El antipatrón 1
  está marcado `[OBSERVADO 2026-08-16]` y procede de la ejecución real de la Semana 0 de una
  taquería de CDMX. **No son tres carteras reales**, así que el gate no se da por cerrado, pero
  esta pieza es la única que tiene contacto documentado con el campo.
- **G3 (precio)** pendiente: comprador nombrado y canal definidos, cifra `[A VALIDAR]`. Además
  hay una decisión de modelo sin tomar: pago único o suscripción.
- **G4 (legal)** en orden y es relevante aquí: la skill prohíbe expresamente recomendar
  solicitar, comprar, incentivar o suprimir reseñas, con la norma de la FTC citada y su sanción,
  y prohíbe usar datos obtenidos saltándose términos de uso o muros de acceso.
- **G5 (público)** pendiente.

## Solape comercial declarado

`reporte-inteligencia-competencia` es la **vertical de hostelería de esta misma pieza**: mismo
panel de seis, misma lógica de brecha, salida de una página en vez de diez secciones. **No se
venden las dos al mismo comprador.** A un restaurante se le vende la vertical; a cualquier otro
sector, esta.
