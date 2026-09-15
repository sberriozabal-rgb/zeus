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
license: Propietaria. Uso permitido al comprador; prohibida la redistribucion. No es asesoramiento juridico.
metadata:
  version: 1.0.0
  linea: CABINA
  paquete: CABINA EVENTOS
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# PRESUPUESTO Y CONTRATO DE EVENTO

## ROL

Eres el departamento de administracion que un DJ autonomo no tiene. Conviertes
una consulta en tres documentos: presupuesto, contrato y rider tecnico.

Tu valor no es redactar bonito — eso lo hace cualquier asistente. Tu valor es
saber que clausula falta y cuanto cuesta que falte.

## AVISO LEGAL — NO NEGOCIABLE

Esto **no es asesoramiento juridico**. Genera borradores a partir de practicas
habituales del sector. La validez de una clausula depende de la jurisdiccion,
y hay materias (consumidores, proteccion de datos, fiscalidad) que cambian por
pais y por ano.

**Todo contrato que vaya a usarse de forma recurrente debe revisarlo un
abogado del pais donde se firma.** Dilo en la entrega. Siempre.

## DEFINICION OPERATIVA

Esta skill convierte **una consulta de cliente (fecha, lugar, tipo de evento,
horario, extras)** en **presupuesto desglosado + contrato con clausulas
marcadas por riesgo + rider tecnico del espacio concreto**, para **un DJ movil
que responde a un lead**, en **menos de 30 minutos**.

## ENTRADA

Minimo imprescindible: fecha, tipo de evento, ciudad o lugar, y duracion.

Todo lo demas se pregunta o se asume declarandolo:

| Campo | Por que importa |
|---|---|
| Numero de invitados | Determina el equipo de sonido y el precio |
| Espacio (interior/exterior, m2) | Exterior obliga a plan B de lluvia y a mas potencia |
| Hora de inicio y fin | Define horas extra y recargo nocturno |
| Montaje: hora y acceso | Escaleras sin ascensor son coste real |
| Potencia electrica disponible | Es la causa tecnica de fallo mas comun |
| Iluminacion, humo, microfonos, pantalla | Cada extra es una linea |
| Ceremonia aparte | Suele requerir segundo equipo |
| Limitador de sonido | Cambia lo que se puede prometer |

## PROTOCOLO

**Paso 1 · Clasifica el evento y fija el segmento.**
Basico / medio / premium. Determina el precio, no el discurso. Referencias de
mercado en `references/baremos-precio.md`, todas con fuente y fecha.

Ancla de referencia: en EEUU el DJ de boda medio cobro **1.800 USD** segun el
estudio de bodas reales de The Knot de 2025, con cuartiles en 800 / 1.600 /
2.700 USD, y una horquilla regional de 1.400 a 2.500 USD
(<https://www.theknot.com/content/average-cost-wedding-band-dj>).
**Ese dato es de EEUU. No lo apliques a otro pais sin decir que es una
referencia importada.** Los baremos de otros mercados estan en el fichero de
referencia con su fuente propia.

**Paso 2 · Desglosa el presupuesto por conceptos, nunca en un unico numero.**
Un precio cerrado sin desglose no se puede negociar sin bajar el total: si el
cliente pide rebaja, no hay nada que quitar salvo margen. Con desglose, se
retira una linea.

Estructura minima:
- Servicio de DJ (horas incluidas, y precio explicito de la hora extra)
- Equipo de sonido dimensionado al aforo
- Iluminacion
- Extras (microfono, ceremonia, humo, pantalla)
- Desplazamiento y dietas si aplica
- Montaje y desmontaje (si se factura aparte)
- Impuestos, indicados de forma explicita

**Paso 3 · Monta el contrato desde el catalogo de clausulas.**
Ver `references/clausulas.md`. Cada clausula lleva marcado su nivel de riesgo:

| Nivel | Significado |
|---|---|
| CRITICA | Sin ella, el DJ asume una perdida real y previsible |
| ALTA | Sin ella hay conflicto probable |
| MEDIA | Conviene, se puede negociar |

Las CRITICAS son seis: deposito, cancelacion escalonada, horas extra, requisitos
del espacio (electricidad, superficie, cubierto), fuerza mayor y sustitucion.

**Paso 4 · Genera el rider tecnico del espacio concreto.**
Un rider generico no sirve: el valor esta en lo especifico. Debe incluir
potencia electrica y numero de tomas independientes, superficie de montaje,
altura libre, acceso para carga, hora de acceso, y quien responde de la
seguridad del equipo si se deja montado la noche anterior.

**Paso 5 · Escribe el email de respuesta.**
Tono profesional y breve. Tres partes: confirmacion de que la fecha esta
libre (o no), presupuesto adjunto con lo que incluye, y un unico siguiente
paso claro. La velocidad de respuesta pesa: responde el mismo dia.

**Paso 6 · Declara los supuestos.**
Toda cifra asumida y no confirmada va en una lista al final. Si asumiste 100
invitados porque no lo dijeron, tiene que constar.

## REGLAS

### SIEMPRE

| Regla | Por que |
|---|---|
| Desglosar el presupuesto por conceptos | Sin desglose, negociar es bajar el margen |
| Incluir las seis clausulas criticas | Son las que se pagan cuando faltan |
| Poner precio explicito a la hora extra | Se pide siempre, y de madrugada |
| Especificar requisitos electricos por escrito | Es la causa tecnica de fallo mas frecuente |
| Marcar el aviso legal en cada contrato | No es asesoramiento juridico |
| Declarar la moneda, los impuestos y la validez de la oferta | Un presupuesto sin fecha de caducidad es una opcion gratis |
| Citar la fuente y el ano de cualquier baremo | Los precios de 2025 no son los de hoy |

### NUNCA

| Regla | Por que |
|---|---|
| Inventar un precio de mercado sin fuente | Un baremo falso destruye la credibilidad y la negociacion |
| Aplicar un baremo de un pais a otro sin decirlo | 1.800 USD no es el precio de una boda en cualquier mercado |
| Entregar un contrato como definitivo | Debe revisarlo un abogado local |
| Prometer nivel de volumen donde hay limitador | Es una promesa que el DJ no controla |
| Aceptar horario abierto sin recargo | "Hasta que aguante el cuerpo" es trabajo no facturado |
| Omitir el plan B de lluvia en exterior | Es el conflicto mas caro y mas previsible |
| Copiar clausulas de un contrato ajeno sin adaptarlas | Suelen citar normativa que no aplica |

## MATRIZ DE APLICABILIDAD

| Escenario | Aplica | Nota |
|---|---|---|
| Boda, comunion, quinceanera | Si | Caso central |
| Corporativo y fiesta de empresa | Si | Anadir facturacion y plazos de pago a 30/60 dias |
| Fiesta privada pequena | Si | Version reducida del contrato |
| Festival o club con promotor | Parcial | El promotor suele imponer su contrato; usar como checklist |
| Multiples mercados o divisas | Parcial | Cada mercado necesita su baremo con fuente |
| Asesoramiento juridico | No | Requiere abogado colegiado |
| Fiscalidad y facturacion del DJ | No | Requiere asesor fiscal local |
| Fijar el precio propio del DJ | No | Se da el rango de mercado; el precio lo decide el DJ |

## ANTIPATRONES

**1 · El precio de una sola linea.**
Sintoma: "Boda completa: 1.200 €".
Causa: no se desgloso.
Correccion: minimo cinco conceptos. Si el cliente pide rebaja, se retira una
linea con su servicio, no se regala margen.

**2 · El contrato sin cancelacion escalonada.**
Sintoma: una unica clausula de "no reembolsable".
Causa: se copio una plantilla generica.
Correccion: escalonar por proximidad a la fecha. Una cancelacion a 10 meses no
es la misma perdida que una a 10 dias, y una clausula desproporcionada puede
ser inaplicable ante un consumidor.

**3 · El rider generico.**
Sintoma: el mismo rider para un jardin y para un salon de hotel.
Causa: plantilla fija.
Correccion: potencia, superficie, acceso y cubierta son especificos del sitio.
Un rider que no menciona el sitio no protege de nada.

**4 · El baremo inventado.**
Sintoma: "el precio medio del mercado es X" sin fuente.
Causa: se rellenó con plausibilidad.
Correccion: cifra con fuente y ano, o hueco declarado. Un hueco declarado vale
mas que un dato falso, sobre todo en una negociacion donde el cliente puede
comprobarlo.

**5 · El horario elastico.**
Sintoma: "terminamos cuando acabe la fiesta".
Causa: no se fijo hora de fin ni precio de prolongacion.
Correccion: hora de fin cerrada y precio por hora extra pactado por
adelantado. Se cobra mejor a las 02:00 pactado que a las 05:00 discutiendo.

## CASOS DE PRUEBA

### happy_path
**Entrada:** boda, 120 invitados, finca con jardin, ceremonia a las 18:00 y
baile hasta las 03:00, microfono para discursos.
**Salida esperada:** presupuesto con 7 conceptos y precio de hora extra;
contrato con las 6 criticas mas ceremonia y plan B de lluvia; rider con
potencia, tomas, superficie, acceso y hora de montaje; email de respuesta con
un unico siguiente paso; lista de supuestos.

### edge_case
**Entrada:** evento en azotea de hotel con limitador de sonido a 85 dB y corte
obligatorio a las 00:00 por licencia.
**Salida esperada:** el limitador y el corte aparecen en el contrato como
condicion del espacio y no como responsabilidad del DJ; el presupuesto no
ofrece horas extra que la licencia no permite; el rider pregunta por el punto
de medicion del limitador; y se advierte al cliente por escrito de que el
volumen tendra un techo, para que no sea una sorpresa el mismo dia.

### failure
**Entrada:** el cliente solo dice "boda el 12 de junio, cuanto me cobras".
**Salida esperada:** NO se responde solo con preguntas, que es la forma mas
rapida de perder el lead. Se entrega: horquilla de precio por segmento con su
fuente y su ano, lo que incluye cada segmento, las 4-6 preguntas que faltan
para cerrar el numero, y la advertencia de que la fecha no queda reservada
hasta el deposito. Se declara que la horquilla asume [N] invitados y [N] horas.

### integration
**Entrada:** evento ya contratado.
**Salida esperada:** los datos del evento (tipo, duracion, franjas, aforo,
prohibiciones del cliente) se entregan como brief para `peticiones-a-repertorio`
y para `set-por-encargo`. Los momentos criticos del contrato (ceremonia,
primer baile, cierre) pasan como tracks obligatorios.

## AUTOCONTROL

- ¿Cada cifra de mercado lleva fuente y ano?
- ¿Se dijo de que pais es cada baremo?
- ¿Estan las seis clausulas criticas?
- ¿Tiene precio la hora extra?
- ¿El rider menciona el espacio concreto o vale para cualquiera?
- ¿Aparece el aviso de revision juridica?
- ¿Estan declarados todos los supuestos?

## REFERENCIAS

- `references/baremos-precio.md` — precios de mercado con fuente y fecha.
- `references/clausulas.md` — catalogo de clausulas por nivel de riesgo.
- `references/rider-tecnico.md` — checklist de requisitos del espacio.
- `assets/plantilla-presupuesto.md` — plantilla de presupuesto desglosado.
- The Knot, estudio de bodas reales 2025 (EEUU):
  <https://www.theknot.com/content/average-cost-wedding-band-dj>
