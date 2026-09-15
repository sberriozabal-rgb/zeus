# Anexo A — Ficha comercial

Nombre técnico     : escandallo-ingenieria-menu
Nombre comercial   : [A VALIDAR — nombre comercial de la casa pendiente]
Peldaño            : P1 · SKILL (pieza 1 de 6 del sistema instalable Motor B)
Línea              : Hostelería
Comprador nombrado : Restaurante independiente de mesa y mantel o cocina de producto, España o México, 8-30 personas de plantilla y carta de 20 a 60 referencias. Decide el dueño; en grupo pequeño, el gerente con el jefe de cocina delante. En México el mercado objetivo es la microempresa restaurantera, que es 96 de cada 100 unidades del sector (INEGI/CANIRAC, ver `references/FUENTES.md`).
Trabajo que quita  : Calcular a mano el coste de cada plato en una hoja de cálculo —normalmente sin rendimiento ni merma, que es lo que la hace estar mal— y decidir a ojo qué platos quitar de la carta. Hoy o no se hace, o se hace una vez al año cuando ya se perdió el margen.
Umbral que aporta  : El umbral de popularidad del 70% de la cuota media (Kasavana & Smith, 1982, verificado en literatura académica) y las tres capas de coste que casi nadie imputa. Cifra propia reproducible: en la carta de prueba, la merluza pasa de 11,4% a 30,4% de food cost solo por aplicar rendimiento (52%) y merma de plancha (18%). Diecinueve puntos en un plato, la misma receta.
Precio propuesto   : No se vende suelta. Incluida en Instalación Completa 4.900 € (6 skills) [A VALIDAR — cifra de doctrina comercial, pendiente de que Sergio la fije por escrito]. Es la primera candidata a entrar en la Instalación Esencial de 3 skills (2.500 € [A VALIDAR]), porque es la que produce la cifra que abre la conversación: euros al año.
Canal              : Venta presencial dentro del sistema instalable (Motor B). No se publica suelta en directorio hasta que el sistema tenga el primer caso vendido con cifras.
Motor              : B · Instalación
Frase de anuncio   : "Tu merluza no cuesta lo que pone el albarán. Cuesta el doble, y está en tu carta."
Estado / Versión   : ACORDADO / v1.1.0
Auditoría          : 19/20 (revisión de cierre, 16-ago-2026). **Corregida a la baja desde el 20/20 que declaraba esta misma ficha esta mañana.** Punto que falla: `cases/case_01_happy_path.md` y `case_03_failure.md` manejan porcentajes de sector sin fuente ni fecha — lo levanta el validador de la casa (`puerta-estrecha`, hallazgo `cifra-sin-fuente`). Un 20/20 en una pieza que nunca se ha ejecutado contra los datos reales de un cliente es una nota regalada, y la casa no las firma.
Gates              : G1 [x] G2 [ ] G3 [x] G4 [x] G5 [ ]

Notas:
- **G1 (producto)** levantado: 20/20, por encima del mínimo de 16. La versión anterior
  (v1.0.0) estaba en 7/20 real pese a declararse 18/20; la corrección está en el CHANGELOG.
- **G2 (prueba)** pendiente: los cuatro casos de `cases/` son reproducibles y ejecutados,
  pero salen de la carta de prueba de la casa, no de tres clientes reales. Hasta que tres
  cartas reales pasen por el motor —una de ellas con datos sucios de verdad— este gate no
  se levanta.
- **G3 (precio)** levantado con comprador nombrado, canal y precio propuesto, aunque la
  cifra siga `[A VALIDAR]` hasta la firma de Sergio.
- **G4 (legal)** levantado: no deriva de material source-available con prohibición de
  venta, no usa marca ajena en el nombre técnico ni comercial, y la licencia de uso
  comercial sin redistribución está en `LICENSE.txt`. La skill no da asesoría fiscal y lo
  declara en `## Límites`.
- **G5 (público)** pendiente: la frase de anuncio no se ha usado todavía en ningún material
  enviado a nadie, y antes de usarse debe pasar la comprobación de que las dos cifras que
  contiene (11,4% y 30,4%) se presentan siempre como carta de prueba de la casa, no como
  caso de cliente.
- **Regla de freno (4.5)**: esta es la pieza 1 de 6 de una línea con cero compradores
  nombrados hasta la fecha. La prioridad de la casa no es fabricar la séptima skill, es
  instalar estas seis en un cliente que pague.
