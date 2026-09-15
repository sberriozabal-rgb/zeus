# Anexo A — Ficha comercial

Nombre técnico     : comparativa-proveedores
Nombre comercial   : [A VALIDAR — nombre comercial de la casa pendiente]
Peldaño            : P1 · SKILL (pieza del sistema instalable Motor B)
Línea              : Hostelería
Comprador nombrado : Restaurante independiente o grupo pequeño, España o México, que compra a **dos o más proveedores del mismo producto** y guarda los albaranes (carpeta física o export del programa de compras). Plantilla 8-30 personas, compra de alimentación por encima de ~4.000 €/mes. Decide el dueño; lo ejecuta él o el jefe de cocina que hace los pedidos. **Quien no es comprador**: el local con proveedor único obligado por contrato o por central de compras del grupo —sin dos proveedores no hay comparativa, y la mitad del producto no aplica—; el local que tira los albaranes o solo guarda el resumen mensual del banco, porque sin línea de producto no hay nada que normalizar; y la franquicia con lista de precios impuesta, que no puede cambiar de proveedor aunque el informe se lo demuestre.
Trabajo que quita  : Cruzar a mano cincuenta líneas de albarán entre tres proveedores cada semana —que por eso no se hace nunca— y decidir a ojo si el que ofrece más barato es de verdad más barato o es otro producto.
Umbral que aporta  : Que una garrafa de 5 L a 42,50 € son **8,50 €/L** y gana al litro suelto de 8,90 €, y que hasta que todo no está en la misma base y sin IVA no se compara nada. La alerta en **+8%** entre dos fechas, defendida contra el IPC general de España (3,6% anual, INE julio 2026): más del doble de la inflación ya no es "todo sube", es una decisión de ese proveedor. La separación **estacional / estructural**, que es la que impide prometer un ahorro que el cambio de temporada desmiente solo. Y el **formato encubierto**: mismo precio de caja, menos gramos dentro, invisible en el albarán y visible solo en el €/base.
Precio propuesto   : No se vende suelta. Incluida en Instalación Completa 4.900 € (6 skills). Candidata al paquete Esencial de 3 (2.500 €) junto con escandallo y control-no-shows: es la pieza que produce el ahorro más fácil de comprobar —el dueño puede llamar al proveedor esa misma tarde—. [A VALIDAR — pendiente de ratificación por escrito de Sergio]
Canal              : Venta presencial dentro del sistema instalable (Motor B). No se publica suelta en directorio hasta que el sistema completo tenga el primer caso vendido.
Motor              : B · Instalación
Frase de anuncio   : "Te digo qué te ha subido de verdad, cuánto de eso se corrige solo con la temporada, y quién te lo tiene hoy más barato con el precio puesto en la misma unidad."
Estado / Versión   : ACORDADO / v1.1.0
Auditoría          : 18/20 — ver desglose abajo. No se redondea al alza.
Gates              : G1 [x] G2 [ ] G3 [x] G4 [x] G5 [ ]

## Desglose de auditoría (18/20)

**Punto 1 no conseguido: caso failure útil.** El motor con `{"lineas": []}` no devuelve
error —devuelve el esqueleto completo con todos los totales a 0 € y
`avisos_verificacion` vacío—. Un informe de ceros mudos es el antipatrón nº 3 de la
propia skill producido por su propio motor. El informe del caso 3 lo escribe el
ejecutor, no el script. Es peor asimetría que la de `control-no-shows`, donde al menos
el motor dice `error`.

**Punto 2 no conseguido: umbral con cifra.** El umbral declarado no es el umbral que
opera. `SKILL.md`, la regla SIEMPRE correspondiente y `familias-y-volatilidad.md` §5
fijan la sospecha de "no es el mismo producto" en **> 40-50%**; la función `verificar()`
del motor solo avisa por encima del **60%**. Una diferencia del 50% pasa hoy sin aviso.
Se cuenta como punto perdido y no como erratilla, porque la skill entera se sostiene
sobre que el número escrito es el número que se aplica.

Todos los demás puntos: disparo con jerga real (trece frases del gremio más el
vocabulario de albarán), trabajo en verbo, ejecutor definido con su momento y su
presión, entrada real con las cuatro combinaciones posibles, manejo de datos sucios con
mensaje literal del motor, umbral con cifra y fuente en el resto de casos, 10 pasos
atómicos todos con "si falta el dato", plantilla de salida en bloque con longitud
máxima, límites declarados, 11 reglas SIEMPRE, 9 reglas NUNCA, 5 antipatrones, los 4
casos ejecutados contra el motor, frontmatter conforme, versión y CHANGELOG, 5
referencias externas con URL y límite de uso, y esta ficha.

## Notas de gates

- **G1 (producto)** levantado: 18/20, por encima del 16 recomendado.
- **G2 (prueba)** pendiente: los 4 casos son de fabricación, ejecutados contra el motor
  pero con datos de fábrica. Falta probarla contra 3 carpetas de albaranes reales de un
  cliente real, una de ellas con datos sucios de verdad —que en compras significa
  fotos de albaranes en papel, no un JSON—.
- **G3 (precio)** marcado con comprador nombrado, no-comprador nombrado, canal y precio
  propuesto dentro del sistema, aunque la cifra siga [A VALIDAR] hasta la firma de
  Sergio.
- **G4 (legal)** marcado: no deriva de material source-available con prohibición de
  venta, no usa marca ajena en el nombre técnico ni comercial, licencia de uso comercial
  sin redistribución (ver LICENSE.txt). Las menciones a INE, AEAT, Junta de Andalucía,
  Ipsos y OCU son citas de fuente con URL, no uso de marca. Los nombres de proveedor de
  los casos ("Distribuidora A", "Mayorista B", "Pescados C", "Quesos D", "Frutas E") son
  deliberadamente genéricos: **ninguna empresa real aparece nombrada como cara ni como
  barata en ningún material de esta skill**, y esa regla se mantiene también en los
  informes de cliente que salgan de la casa.
- **G5 (público)** pendiente: esta ficha no se ha usado todavía en material de venta
  enviado a nadie.
- **Riesgo comercial declarado**: la frase de anuncio promete decir quién lo tiene más
  barato, y con un solo proveedor eso no se puede entregar. En la visita se pregunta
  antes —"¿a cuántos proveedores le compras el mismo producto?"— porque prometerlo y
  entregar medio informe quema la instalación entera, no solo esta pieza.
- **Riesgo legal declarado, distinto del anterior**: esta skill produce material que el
  dueño puede enseñar a su comercial. Por eso la regla NUNCA de no acusar de mala fe
  por un formato encubierto o un porte no es cortesía, es protección: un informe con la
  palabra "fraude" en la portada es una carta que el cliente firma sin saberlo.
