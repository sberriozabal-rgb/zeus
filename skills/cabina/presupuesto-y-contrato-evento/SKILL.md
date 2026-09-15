---
name: presupuesto-y-contrato-evento
description: >-
  Convierte la consulta de un cliente de evento (boda, corporativo, quinceanera, fiesta
  privada) en un presupuesto desglosado, un contrato con las clausulas que evitan los
  conflictos reales del oficio y un rider tecnico adaptado al espacio concreto. Incluye
  baremos de precio de mercado con fuente y las clausulas cuya ausencia cuesta dinero:
  deposito, cancelacion, horas extra, potencia electrica, superficie, comida de proveedor y
  limitador de sonido. Para DJ movil y de eventos. Usar cuando entre un lead, cuando haya que
  cerrar condiciones, cuando el cliente pida cambios sobre lo pactado o cuando haya que fijar
  precio.
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso permitido al comprador; prohibida la redistribución. No es asesoramiento jurídico. Ver LICENSE.txt.
metadata:
  version: "1.1.0"
  linea: CABINA
  paquete: CABINA EVENTOS
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# presupuesto-y-contrato-evento

## AVISO LEGAL — NO NEGOCIABLE

Esto **no es asesoramiento jurídico**. Genera borradores a partir de prácticas habituales del
sector. La validez de una cláusula depende de la jurisdicción, y hay materias —consumidores,
protección de datos, fiscalidad— que cambian por país y por año.

**Todo contrato que vaya a usarse de forma recurrente debe revisarlo un abogado del país donde
se firma.** Esto se dice en la entrega. Siempre.

## Qué hace

Convierte **una consulta de cliente de evento (fecha, lugar, tipo, horario, extras)** en
**presupuesto desglosado por conceptos, contrato con las cláusulas marcadas por nivel de riesgo
y rider técnico del espacio concreto**, para **un DJ móvil o de eventos que responde a un lead
sin manager ni agencia**, en **menos de 30 minutos de atención**.

El valor no es redactar bonito, que eso lo hace cualquier asistente. El valor es **saber qué
cláusula falta y cuánto cuesta que falte**: las seis críticas son las que, ausentes, convierten
un evento cobrado en una pérdida previsible. Y el desglose por conceptos, que es lo que permite
negociar quitando alcance en vez de bajando el margen.

## Cuándo se dispara

- "me ha entrado una consulta para una boda en junio, ¿cuánto cobro?"
- "el cliente quiere que le baje el precio"
- "me han pedido dos horas más a las tres de la mañana y no sabía qué cobrar"
- "se me ha caído una boda a dos semanas y no había depósito"
- "¿qué pongo en el contrato?"
- "el sitio es un jardín y no sé qué pedirles de luz"
- "¿esto lo cubre el seguro o lo pago yo?"
- "necesito un rider para mandarles"
- jerga del gremio: "lead", "depósito", "señal", "cancelación", "horas extra", "rider",
  "limitador", "potencia", "aforo", "montaje", "desmontaje", "fuerza mayor", "sustitución",
  "ceremonia aparte", "dietas", "kilometraje"

## Quién lo ejecuta

El propio DJ al recibir el lead, con **20 a 30 minutos** de atención para los tres documentos.
La velocidad de respuesta pesa en la conversión, así que el objetivo operativo es **responder
el mismo día**, aunque sea con supuestos declarados.

## Entrada

- **Mínimo imprescindible:** fecha, tipo de evento, ciudad o lugar, y duración. Con eso ya se
  produce.
- **Recomendado:** número de invitados (determina el equipo y el precio), espacio y si es
  interior o exterior (exterior obliga a plan B de lluvia y más potencia), hora de inicio y
  fin (define horas extra y recargo nocturno).
- **Recomendado:** potencia eléctrica disponible y número de tomas independientes, que es **la
  causa técnica de fallo más común**; superficie y altura libre de montaje; hora y acceso de
  carga.
- **Recomendado:** extras (iluminación, humo, micrófonos, pantalla), si hay ceremonia aparte
  —suele requerir segundo equipo— y si el espacio tiene **limitador de sonido**, porque cambia
  lo que se puede prometer.
- **Dato sucio típico:** la consulta que solo dice "boda en junio, ¿precio?". No se responde
  pidiendo un cuestionario: se asume el escenario más habitual del segmento, se produce el
  presupuesto completo y **cada supuesto va declarado en una lista al final**. Si se asumieron
  100 invitados porque no lo dijeron, tiene que constar.

## Umbral que sostiene el producto

**Las seis cláusulas CRÍTICAS**, definidas por un criterio operativo y no por costumbre:
CRÍTICA es aquella sin la cual el DJ asume una pérdida real y previsible. Son depósito,
cancelación escalonada, horas extra, requisitos del espacio (electricidad, superficie,
cubierto), fuerza mayor y sustitución. Catálogo completo con su nivel en
`references/clausulas.md`.

El segundo umbral son los **baremos de mercado por país, cada uno con su fuente**, y con una
regla dura: **no aplicar el baremo de un país a otro sin declarar que es una referencia
importada.**

- **España**: media nacional 350–500 €, boda completa 400–1.500 €, hora extra 75–250 €,
  desplazamiento 0,50–1 €/km. **El escalón medio real está en 1.000–1.500 €, muy por encima de
  los 717 € de promedio que publican los portales de presupuestos**, porque esos portales
  atraen la demanda más sensible al precio. Un DJ que fija su tarifa mirando solo ahí se ancla
  al segmento más bajo del mercado.
- **EE. UU.**: DJ de boda medio en **1.800 USD** según el estudio de bodas reales de The Knot
  de 2025, con cuartiles en 800 / 1.600 / 2.700 y horquilla regional de 1.400 a 2.500
  (<https://www.theknot.com/content/average-cost-wedding-band-dj>).
- **Contexto de negociación**: el coste medio de una boda en España es de **25.183 €** con 123
  invitados de media, es decir 225 € por invitado
  (<https://gironanoticies.com/comunicado/292790-25183-euros-el-coste-medio-de-celebrar-una-boda-en-espana-segun-bodasnet.htm>).
  1.200 € sobre 25.183 € es **menos del 5% del presupuesto total**, y esa es la frase que
  sostiene el precio sin bajarlo.

**El baremo no es el precio del DJ.** Es el contexto. Sirve para saber si estás fuera de
mercado, no para fijar tarifa: el precio lo decide el DJ según su coste, su agenda y su
posicionamiento.

## Procedimiento

1. **Entrada: la consulta del cliente → Acción: clasificar el evento en segmento básico, medio
   o premium y localizar el baremo del país correspondiente en `references/baremos-precio.md` →
   Salida: segmento asignado y horquilla de precio con su fuente → Si el país no tiene baremo
   propio en el fichero: se usa el más cercano y se declara explícitamente que es una
   referencia importada.**

2. **Entrada: segmento, aforo y duración → Acción: desglosar el presupuesto por conceptos —
   servicio de DJ con horas incluidas y precio explícito de hora extra, sonido dimensionado al
   aforo, iluminación, extras, desplazamiento y dietas, montaje si se factura aparte, impuestos
   explícitos— → Salida: presupuesto por líneas, nunca un número único → Si falta el aforo: se
   asume el habitual del segmento, se dimensiona sobre él y se declara el supuesto.**

3. **Entrada: tipo de evento y espacio → Acción: montar el contrato desde el catálogo de
   `references/clausulas.md`, incluyendo obligatoriamente las seis CRÍTICAS y marcando el nivel
   de riesgo de cada una → Salida: borrador de contrato con niveles visibles → Si el cliente
   rechaza una cláusula CRÍTICA: se declara por escrito qué pérdida asume el DJ con esa
   ausencia, y la decisión es suya.**

4. **Entrada: los datos del espacio concreto → Acción: generar el rider técnico específico con
   potencia y número de tomas independientes, superficie, altura libre, acceso de carga, hora
   de acceso y responsable de la custodia del equipo si queda montado la noche anterior →
   Salida: rider del espacio, no genérico → Si faltan los datos eléctricos: se especifica el
   requisito mínimo como condición del presupuesto y se pide confirmación antes de firmar.**

5. **Entrada: los tres documentos → Acción: escribir el email de respuesta con tres partes —si
   la fecha está libre, qué incluye el presupuesto adjunto, y un único siguiente paso claro— →
   Salida: email listo para enviar el mismo día → Si la fecha no está libre: se dice en la
   primera línea y se ofrece alternativa, sin enterrarlo al final.**

6. **Entrada: todo lo producido → Acción: recopilar cada cifra asumida y no confirmada en una
   lista de supuestos al final de la entrega, y añadir el aviso de revisión por abogado →
   Salida: entrega completa con sus supuestos y su aviso legal → Si algún supuesto cambia el
   precio de forma relevante: se señala cuál y en cuánto.**

## Salida

```markdown
# Presupuesto — [Tipo de evento], [fecha]
[Lugar] · [N invitados] · [horario] · Segmento: [básico/medio/premium]

| # | Concepto | Detalle | Importe |
|---|---|---|---|
| 1 | Servicio de DJ | [N] horas incluidas | [€] |
| 2 | Hora extra | precio unitario explícito | [€]/h |
| 3 | Equipo de sonido | dimensionado a [N] invitados | [€] |
| 4 | Iluminación | [detalle] | [€] |
| 5 | Extras | [micro / ceremonia / humo / pantalla] | [€] |
| 6 | Desplazamiento | [N] km a [tarifa]/km | [€] |
| 7 | Montaje y desmontaje | [si se factura aparte] | [€] |
|   | **Impuestos** | [tipo explícito] | [€] |
|   | **TOTAL** | | **[€]** |

## Cláusulas del contrato
[cada una con su nivel: CRÍTICA / ALTA / MEDIA]

## Rider técnico — [espacio concreto]
Potencia: [N] kW, [N] tomas independientes · Superficie: [N] m² · Altura libre: [N] m
Acceso de carga: [detalle] · Hora de acceso: [hora] · Custodia nocturna: [responsable]

## Supuestos de esta versión
[cada cifra asumida y no confirmada, y cuál de ellas movería el precio]

> Este documento no es asesoramiento jurídico. Si vas a usar este contrato de forma
> recurrente, que lo revise un abogado del país donde se firma.
```

Los tres niveles de cláusula del paso 3:

| Nivel | Significado |
|---|---|
| **CRÍTICA** | Sin ella, el DJ asume una pérdida real y previsible |
| **ALTA** | Sin ella hay conflicto probable |
| **MEDIA** | Conviene, se puede negociar |

## Límites

- **No es asesoramiento jurídico.** Produce borradores de práctica sectorial, y la validez de
  cada cláusula depende de la jurisdicción. El uso recurrente exige revisión de abogado.
- No es asesoramiento fiscal. Los impuestos se indican de forma explícita en el presupuesto,
  pero el tipo aplicable lo confirma el asesor del DJ.
- Los baremos son **contexto de mercado, no tarifa recomendada**. Sirven para saber si estás
  fuera de precio; el precio lo fija el DJ con su coste y su agenda.
- **No se aplica el baremo de un país a otro** sin declararlo como referencia importada. El
  dato de The Knot es de EE. UU. y no vale para España sin ese aviso.
- No negocia por el DJ ni decide qué cláusula ceder. Marca el riesgo de cada ausencia; la
  decisión es del DJ.
- No dimensiona equipo por especificación acústica: propone según aforo y espacio, y el cálculo
  fino lo hace quien conoce el material.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Desglosar el presupuesto por conceptos, nunca un número único | Sin desglose, negociar es bajar el margen; con desglose se retira una línea |
| Incluir las seis cláusulas CRÍTICAS en todo contrato | Son exactamente las que se pagan cuando faltan, y el coste es previsible |
| Poner precio explícito a la hora extra | Se pide casi siempre y de madrugada, cuando ya no hay margen para negociar |
| Especificar los requisitos eléctricos por escrito | Es la causa técnica de fallo más frecuente del oficio, y sin constancia escrita el problema es del DJ |
| Citar el baremo con su país, su fuente y su fecha | Una cifra de mercado sin país es inútil, y sin fuente es indefendible cuando el cliente pregunta |
| Declarar cada cifra asumida en la lista de supuestos | Un presupuesto con supuestos ocultos se convierte en discusión el día del montaje |
| Generar el rider del espacio concreto, no uno genérico | El valor del rider está en lo específico; uno genérico no lo lee nadie y no protege de nada |
| Responder el mismo día, aunque sea con supuestos | La velocidad de respuesta pesa en la conversión del lead tanto como el precio |
| Advertir del limitador de sonido cuando exista | Cambia lo que se puede prometer, y prometer de más con limitador es un conflicto seguro |
| Incluir el aviso de revisión por abogado en toda entrega | Es la frontera del producto y omitirla expone al DJ y a la casa |

| NUNCA | Porqué |
|---|---|
| Presentar esto como asesoramiento jurídico | No lo es, y afirmarlo expone legalmente a la casa y al DJ que lo usa |
| Aplicar el baremo de un país a otro sin declararlo | Los mercados no son comparables, y una tarifa importada en silencio descoloca el precio entero |
| Dar un precio cerrado sin desglose | Deja al DJ sin nada que quitar en la negociación salvo su propio margen |
| Omitir una cláusula CRÍTICA porque el cliente la incomoda | Son las que evitan la pérdida previsible; si se cede, se declara qué se asume |
| Prometer nivel de sonido en un espacio con limitador | El limitador manda sobre cualquier promesa, y el incumplimiento lo paga el DJ |
| Inventar una cifra de baremo sin fuente | Es la cifra huérfana que el cliente pregunta y no se puede defender |
| Usar el promedio de los portales de presupuestos como tarifa | Atraen la demanda más sensible al precio y ancla al DJ al segmento más bajo |
| Entregar un rider genérico | No protege de nada: el fallo eléctrico ocurre en un espacio concreto con tomas concretas |
| Cerrar un presupuesto sin la lista de supuestos | Toda cifra asumida y no declarada es una discusión aplazada al día del evento |

## Antipatrones

1. **Síntoma**: se cae una boda a dos semanas y el DJ no cobra nada. **Causa raíz**: no había cláusula de depósito ni de cancelación escalonada, las dos primeras CRÍTICAS. **Corrección**: depósito no reembolsable a la firma y escala de cancelación por tramos de antelación; sin ellas, el DJ financia gratis la reserva de fecha del cliente.

2. **Síntoma**: el cliente pide rebaja y el DJ baja el total un 15%. **Causa raíz**: el presupuesto era un número cerrado, así que no había ninguna línea que retirar. **Corrección**: desglosar siempre por conceptos; ante la petición de rebaja se quita iluminación, humo o una hora, no margen.

3. **Síntoma**: el equipo salta a media fiesta y la culpa recae en el DJ. **Causa raíz**: no se especificó por escrito la potencia ni el número de tomas independientes en el rider del espacio. **Corrección**: requisito eléctrico como condición del presupuesto, confirmado antes de firmar, con el número de tomas y los kW por escrito.

4. **Síntoma**: el DJ cobra 700 € en una boda de 25.000 € y pierde dinero con las horas extra. **Causa raíz**: fijó su tarifa mirando el promedio de un portal de presupuestos, que atrae la demanda más sensible al precio. **Corrección**: usar el escalón medio real del mercado (1.000–1.500 € en España) y el contexto de que 1.200 € es menos del 5% del presupuesto de la boda.

5. **Síntoma**: el cliente se queja de que el volumen es bajo y exige lo prometido. **Causa raíz**: se prometió nivel de sonido sin comprobar que el espacio tenía limitador instalado. **Corrección**: preguntar siempre por el limitador, y cuando exista, escribir en el presupuesto qué se puede y qué no se puede garantizar con él.

## Casos de prueba

Los cuatro casos están en `cases/`, con entrada y salida reales.

**Happy path** (`cases/case_01_happy_path.md`): boda de 120 invitados en finca con jardín,
7 horas más ceremonia. Presupuesto desglosado en 7 líneas, seis cláusulas críticas y rider con
los requisitos eléctricos del exterior.

**Edge case** (`cases/case_02_edge_case.md`): el cliente rechaza la cláusula de cancelación y
pide precio cerrado. Se declara por escrito la pérdida que asume el DJ y se ofrece alcance
reducido en vez de rebaja.

**Failure** (`cases/case_03_failure.md`): consulta de una línea, "boda en junio, ¿precio?". Se
entregan los tres documentos completos sobre supuestos declarados, sin pedir un cuestionario.

**Integration** (`cases/case_04_integration.md`): encadenado con `peticiones-a-repertorio`. La
cláusula de repertorio y prohibidos del contrato se rellena con el cubo PROHIBIDO del cruce.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
