# Anexo A — Ficha comercial

Nombre técnico     : respuesta-resenas
Nombre comercial   : [A VALIDAR — nombre comercial de la casa pendiente]
Peldaño            : P1 · SKILL (pieza del sistema instalable Motor B)
Línea              : Hostelería
Comprador nombrado : Restaurante independiente, España o México, plantilla 8-30 personas, con ficha activa en Google y volumen suficiente para que un patrón signifique algo (a partir de ~10-15 reseñas nuevas al mes [A VALIDAR — sin fuente localizada, es calibración de oficio]). Decide el dueño. **Quien NO es comprador**: un grupo con marca consolidada o una cadena — el efecto de ingresos por estrella está medido solo en independientes, así que el argumento central no le aplica y venderlo ahí es venderle humo.
Trabajo que quita  : Redactar a mano cada respuesta a reseña —o no responder nunca— y no llegar a saber si las negativas repiten el mismo problema operativo o son casos sueltos.
Umbral que aporta  : El umbral de patrón (3 menciones del mismo motivo en 60 días) que separa señal operativa de ruido, y la traducción de estrellas a ingresos con la elasticidad de Luca (+5-9% por estrella, HBS Working Paper 12-016, 3.582 restaurantes de Seattle, 2003-2009) **citada siempre con sus tres límites: es Yelp, es EE. UU., y es ingresos, no margen**. Más el límite legal de incentivos, que es donde un dueño bienintencionado se mete en problemas él solo.
Precio propuesto   : No se vende suelta. Incluida en Instalación Completa 4.900 € (6 skills) y candidata al paquete Esencial (2.500 €). [A VALIDAR — pendiente de ratificación por escrito de Sergio]
Canal              : Venta presencial dentro del sistema instalable (Motor B), ejecutada en la visita con las reseñas reales del local, nunca con una demo de ejemplo. No se publica suelta en directorio hasta que el sistema completo tenga el primer caso vendido.
Motor              : B · Instalación
Frase de anuncio   : "Te digo si tus reseñas malas repiten siempre el mismo problema, y te dejo escritas las respuestas."
Estado / Versión   : ACORDADO / v1.1.0
Auditoría          : 19/20 — ver desglose abajo. No se redondea al alza.
Gates              : G1 [x] G2 [ ] G3 [x] G4 [x] G5 [ ]

## Desglose de auditoría (19/20)

**Corrección de nota respecto a la v1.0.0.** Esta ficha declaraba 19/20 cuando la
skill valía **16/20**: le faltaban cuatro piezas del ADN de la línea —procedimiento
en pasos atómicos con rama "si falta el dato", tabla de reglas SIEMPRE, tabla de
reglas NUNCA y sección de antipatrones—. Era una nota regalada. Las cuatro se
fabricaron el 16-ago-2026 y ahora sí se sostienen.

Punto no conseguido: **umbral con cifra**. El umbral operativo de la skill —3
menciones en 60 días— es calibración de oficio sin fuente externa, igual que el
"~10-15 reseñas nuevas al mes" y el "tres ya empieza a ser estadísticamente
significativo" de `umbrales-resenas.md` §2, que no tiene contraste de hipótesis
detrás. La cifra que sí está verificada (Luca) es de mercado, no del local. Se
declara en vez de redondearse.

Todos los demás puntos: disparo con jerga real, trabajo en verbo, ejecutor
definido, entrada real, manejo de datos sucios, pasos atómicos con "si falta el
dato", plantilla de salida en bloque, límites declarados, 11 reglas SIEMPRE, 10
reglas NUNCA, 5 antipatrones, los 4 casos, frontmatter de seis campos, versión y
CHANGELOG, referencias externas con URL en `references/FUENTES.md`, y esta ficha.

## Notas de gates

- **G1 (producto)** levantado: 19/20, por encima del 16 exigido. Antes de la
  corrección del 16-ago estaba en 16/20 y la ficha decía 19: el gate se había
  dado por levantado con una nota que no era la real.
- **G2 (prueba)** pendiente: los 4 casos son de fabricación. Falta ejecutarla
  contra 3 exports reales de un cliente real, uno con datos sucios.
- **G3 (precio)** marcado con comprador nombrado y canal, aunque la cifra siga
  [A VALIDAR] hasta la firma de Sergio.
- **G4 (legal)** marcado, y es el gate delicado de esta pieza. La skill declara
  ahora el límite de incentivos con la política publicada de cada plataforma
  ([Google](https://support.google.com/contributionpolicy/answer/7400114),
  [Tripadvisor](https://www.tripadvisor.com/Trust-lvBd3L1aU38Y.html)) y el ancla
  legal española: art. 27.8 de la Ley 3/1991 de Competencia Desleal tras el
  RDL 24/2021, con sanciones del art. 49 TRLGDCU de 150 € a 1.000.000 €. Sin ese
  límite escrito, la skill podía llevar a un dueño a incentivar reseñas creyendo
  que hacía marketing. Las menciones a Google y Tripadvisor son cita de política
  con URL, no uso de marca.
- **G5 (público)** pendiente: esta ficha no se ha usado en material de venta
  enviado a nadie.
- **Riesgo comercial declarado**: la v1.0.0 afirmaba que Google y TripAdvisor
  "penalizan" las respuestas idénticas. **Ninguna política publicada de las dos
  plataformas dice eso.** Se retiró el 16-ago-2026. Si esa frase llegó a algún
  material de venta ya enviado, hay que corregirla ahí también.
