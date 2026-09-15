---
name: peticiones-a-repertorio
description: Convierte la lista de canciones que el cliente manda en texto sucio (WhatsApp, email, Excel mal escrito, notas de voz transcritas) en un informe accionable cruzado contra la biblioteca real del DJ - que tengo, que hay que comprar, que esta en una version que no sirve y que entra en la lista de prohibidos. Para DJ movil, de bodas, corporativos y eventos privados. Usar cuando llegue una lista de peticiones o un cuestionario de novios, cuando haya que preparar la compra de musica antes de un evento, o cuando haya que devolver al cliente un documento de confirmacion del repertorio.
license: Propietaria. Uso permitido al comprador; prohibida la redistribucion.
metadata:
  version: "1.1.0"
  linea: CABINA
  paquete: CABINA EVENTOS
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# peticiones-a-repertorio

## Qué hace

Convierte **una lista de peticiones en lenguaje natural más un export de la biblioteca del
DJ** en **un informe de cuatro cubos (TENGO / NO TENGO / DUDOSO / PROHIBIDO) con lista de
compra priorizada y documento de confirmación redactado para el cliente**, para **un DJ móvil
que prepara un evento contratado**, en **menos de 10 minutos de trabajo asistido**.

No es crítica musical y no opina sobre el gusto del cliente. Convierte texto sucio en
decisiones clasificadas, y deja por escrito las dos cosas que generan conflicto en un evento:
lo que va a sonar seguro y lo que el cliente ha pedido que no suene. La aportación no es
buscar canciones, es **no dar por bueno lo que no lo está**: un falso positivo no se descubre
preparando, se descubre en el evento.

## Cuándo se dispara

- "los novios me han mandado una lista por WhatsApp hecha un desastre"
- "tengo que decirles qué tengo y qué hay que comprar"
- "me han pasado un Excel con 40 canciones mal escritas"
- "¿cómo sé si tengo esto en la biblioteca?"
- "necesito mandarles un documento de confirmación del repertorio"
- "me han dicho que nada de reggaetón y quiero que conste"
- "la madre de la novia me ha mandado un audio con peticiones"
- "cuánto me va a costar comprar lo que me falta"
- jerga del gremio: "peticiones", "lista de novios", "cuestionario", "prohibidos", "primer
  baile", "momentos críticos", "Clean", "Dirty", "Radio Edit", "Extended", "cubo", "pool",
  "biblioteca", "collection xml", "lista de compra"

## Quién lo ejecuta

El propio DJ, al recibir la lista del cliente y con tiempo de sobra antes del evento, con
**10 a 15 minutos** de atención: pegar la lista, lanzar el cruce, revisar uno por uno el cubo
DUDOSO —que es el único paso donde hace falta criterio humano— y enviar el documento de
confirmación.

## Entrada

- **Obligatorio · Lista del cliente**, pegada tal cual. Vale WhatsApp con marcas de hora,
  email, lista numerada, prosa continua o transcripción de audio. **No se pide que la
  limpien: limpiarla es el trabajo.**
- **Obligatorio · Export de biblioteca**: `collection.xml` de rekordbox, o CSV con al menos
  `artist` y `title` (Lexicon, Serato, Engine DJ y VirtualDJ exportan CSV).
- **Recomendado:** tipo de evento, duración y franja horaria. Deciden la versión correcta de
  un tema cuando hay varias.
- **Recomendado:** perfil de invitados e idioma dominante, y el presupuesto de compra de
  música, que acota la lista de compra.
- **Dato sucio típico:** la línea de conversación mezclada con peticiones —"oye y si pones
  algo de los 80 que le gustan a mi madre", "mañana te llamo"—. El motor las separa a una
  sección APARTADAS que **hay que leer siempre**, porque a veces hay una petición real
  escondida ahí. El segundo dato sucio es la referencia vaga ("la de la peli", "la del
  anuncio"), que nunca se normaliza: se propone candidato y se marca para confirmar.

## Umbral que sostiene el producto

**Los dos umbrales de similitud del cruce: seguro en 0.86 y duda en 0.62.** Todo lo que no
supere 0.86 cae a DUDOSO y sube al cliente en su idioma. Son criterio de oficio de la casa
`[A VALIDAR]`, calibrados contra listas reales mal escritas, no contra un corpus publicado.

La regla de manejo es asimétrica y deliberada: `--umbral-duda` **se puede bajar** si el
cliente escribe muy mal y el resultado sale vacío; **subirlos nunca**. Subir el umbral produce
un informe limpio y falso, y el coste del error no es simétrico: un falso negativo cuesta una
pregunta al cliente, un falso positivo cuesta el momento del primer baile.

Umbral de control de calidad: **una lista real de 25 peticiones produce entre 2 y 6 dudosos**
`[A VALIDAR — calibración de oficio]`. **Cero dudosos es señal de fallo, no de éxito.**

Formatos de biblioteca y sus límites documentados en
<https://rekordbox.com/en/support/faq/operation-hints-7/> y, para Serato, en la ingeniería
inversa comunitaria de <https://github.com/mixxxdj/mixxx/wiki/Serato-Database-Format>.

## Procedimiento

1. **Entrada: la lista del cliente y el export de biblioteca → Acción: localizar los dos
   ficheros y comprobar que el export trae al menos `artist` y `title` → Salida: los dos
   insumos listos → Si falta el export de biblioteca: no se detiene, se ejecuta el análisis de
   la lista (parseo, prohibidos, agrupación), se marca todo el cruce como PENDIENTE DE
   BIBLIOTECA y se indica la ruta exacta de exportación del software del DJ.**

2. **Entrada: los dos ficheros → Acción: ejecutar `python3 scripts/cruzar.py <biblioteca>
   <peticiones.txt> --formato texto` con los umbrales por defecto → Salida: las peticiones
   repartidas en los cuatro cubos → Si el resultado sale vacío por lista muy mal escrita: se
   baja `--umbral-duda`, nunca se suben los umbrales.**

3. **Entrada: el cubo DUDOSO → Acción: revisarlo uno por uno aportando criterio de evento —
   Clean para boda con familia, Extended para sesión de baile de 90 min, Radio Edit o acústica
   para ceremonia— y proponer resolución marcada como propuesta → Salida: cada dudoso con su
   candidato y su motivo → Si la referencia es vaga: se propone el candidato más probable y se
   marca para confirmar, sin resolverlo en silencio.**

4. **Entrada: el cubo NO TENGO → Acción: construir la lista de compra ordenada por criticidad
   (momentos críticos primero, después petición explícita y repetida, después relleno de
   ambiente), indicando formato mínimo aceptable y coste estimado → Salida: lista de compra
   con prioridad y presupuesto → Si no se conoce el precio real de tienda: se deja el hueco
   declarado, jamás se inventa la cifra.**

5. **Entrada: los cuatro cubos resueltos → Acción: redactar el documento de confirmación en el
   idioma del cliente con tres bloques —Confirmado, Necesito que me confirmes, Anotado como no
   poner— sin una sola palabra de jerga técnica → Salida: documento listo para enviar → Si
   aparece jerga: se reescribe, porque a un novio no se le escribe "similitud 0.62".**

6. **Entrada: la sección APARTADAS del motor → Acción: leer todas las líneas que el sistema
   separó por parecer conversación → Salida: peticiones rescatadas a mano y declaradas como
   rescate → Si hay alguna duda sobre si una línea es petición: se trata como petición y se
   manda a DUDOSO.**

## Salida

```
CRUCE DE PETICIONES — [Evento], [fecha]
Peticiones detectadas: 28   Biblioteca: 8.412 tracks

TENGO (19)
  [artista - titulo]                    coincidencia 0.94
  ...
NO TENGO (5)  -> lista de compra
DUDOSO (3)    -> confirmar con cliente
PROHIBIDO (2)

APARTADAS (4 lineas que parecen conversacion) — REVISAR A MANO

## Supuestos de esta versión
[umbrales usados, qué se rescató de APARTADAS, qué dudosos quedan abiertos]
```

Y el documento que se envía al cliente, en su idioma y sin jerga:

```markdown
## Confirmado — sonará seguro
[lista en lenguaje de cliente]

## Necesito que me confirmes
- "La de Bizarrap con Shakira": ¿te refieres a la Session #53? Tengo esa.
- "Despacito": ¿la original o la versión con Justin Bieber?

## Anotado como no poner
- Reggaetón
- "Paquito el Chocolatero"
```

Los cuatro cubos del paso 2:

| Cubo | Qué es | Destino |
|---|---|---|
| **TENGO** | Coincidencia por encima de 0.86 | Playlist directa |
| **NO TENGO** | Sin coincidencia | Lista de compra por criticidad |
| **DUDOSO** | Entre 0.62 y 0.86, o varias versiones | Confirmación del cliente |
| **PROHIBIDO** | Vetado por el cliente | Se repite literal por escrito |

## Límites

- **No oye.** No elige qué versión suena mejor: propone por contexto de evento y la decisión
  la firma una persona.
- No consulta tiendas digitales ni verifica disponibilidad comercial: genera la lista de
  compra, no compra ni comprueba que el track esté a la venta.
- No sirve para peticiones que llegan **durante** el evento. Esto es preparación, no tiempo
  real.
- Sin biblioteca exportable solo entrega parseo, prohibidos y agrupación, y lo declara. Es
  aproximadamente medio informe.
- No afirma BPM, clave ni duración que no venga del export, porque el dato inventado se
  propaga a la playlist.
- No traduce ni corrige el título que pidió el cliente: "la de la peli" es información sobre
  cómo la conoce, y normalizarla destruye esa información.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Ejecutar el script para el cruce, nunca cruzar a ojo | Con 20 peticiones y 8.000 tracks el ojo falla, y además no es reproducible ante una discusión |
| Dejar en DUDOSO todo lo que no supere el umbral de 0.86 | Un falso positivo se descubre en el evento, que es el peor sitio posible para descubrirlo |
| Repetir la lista de prohibidos literalmente al cliente | Es la parte que genera conflicto y tiene que constar por escrito, con sus palabras |
| Marcar el formato y la versión elegidos cuando hay varias | Poner la Dirty en una comunión es un incidente, no un matiz de estilo |
| Reportar las líneas apartadas por parecer charla | Si el sistema se come una petición real, el DJ tiene que poder verlo y rescatarla |
| Declarar el hueco cuando falte la biblioteca | Medio informe útil vale más que ninguno, y el DJ sabe exactamente qué le falta |
| Ordenar la lista de compra por criticidad, no alfabéticamente | El track del primer baile se compra sí o sí; el relleno de ambiente solo si sobra presupuesto |
| Escribir el documento de cliente en su idioma y sin jerga | El cliente no sabe qué es un umbral de similitud, y una confirmación que no se entiende no se firma |
| Indicar el formato mínimo aceptable de compra | Los CDJ no leen todos los formatos, y descubrirlo en cabina es un incidente evitable |
| Tratar como petición cualquier línea dudosa de APARTADAS | El coste de preguntar de más es una línea en el documento; el de perder una petición es el evento |

| NUNCA | Porqué |
|---|---|
| Inventar que un track está en la biblioteca | Es la única mentira que arruina el evento entero y no tiene arreglo en directo |
| Resolver un DUDOSO en silencio | La elección Clean/Dirty o Radio/Extended la firma una persona, porque las consecuencias las paga ella |
| Afirmar BPM, clave o duración que no venga del export | El dato inventado se propaga a la playlist y nadie vuelve a comprobarlo |
| Traducir o "corregir" el título que pidió el cliente | "La de la peli" es información sobre cómo la conoce; normalizarla la destruye |
| Prometer que se puede comprar algo sin verificarlo | Hay tracks que no están a la venta en ningún sitio, y prometerlo crea una expectativa imposible |
| Escribir jerga técnica en el documento del cliente | A un novio no se le escribe "similitud 0.62": es la frase que hace que deje de leer |
| Subir los umbrales para que el informe salga limpio | Produce un informe elegante y falso; el coste del error no es simétrico |
| Dar por bueno un informe con cero dudosos | Una lista real de 25 peticiones produce entre 2 y 6: cero es señal de fallo |
| Opinar sobre el gusto musical del cliente | No es el objeto del encargo y es la forma más rápida de perder un evento ya contratado |

## Antipatrones

1. **Síntoma**: el informe sale con 0 dudosos y todo en TENGO. **Causa raíz**: se bajó el umbral de seguridad o se cruzó a ojo. **Corrección**: reejecutar con los umbrales por defecto; una lista real de 25 peticiones produce entre 2 y 6 dudosos, y cero es señal de fallo, no de éxito.

2. **Síntoma**: en el evento suena la versión Dirty de un tema en una comunión. **Causa raíz**: había varias versiones del mismo título y se resolvió el DUDOSO en silencio eligiendo la primera coincidencia. **Corrección**: todo tema con varias versiones sube al cliente con la pregunta concreta, y la versión elegida se marca por escrito en el documento de confirmación.

3. **Síntoma**: el cliente responde al documento de confirmación preguntando qué significa todo. **Causa raíz**: se volcó el informe técnico en lugar de redactar el documento de cliente. **Corrección**: tres bloques, idioma del cliente, cero jerga; el informe de cubos es para el DJ y no sale de sus manos.

4. **Síntoma**: falta una petición que el cliente había hecho y jura haber mandado. **Causa raíz**: la línea parecía conversación y el motor la mandó a APARTADAS, y nadie leyó esa sección. **Corrección**: revisar APARTADAS línea a línea siempre, y ante la duda tratar la línea como petición y mandarla a DUDOSO.

5. **Síntoma**: la lista de compra se sale del presupuesto y el DJ compra por orden alfabético hasta que se acaba. **Causa raíz**: la lista no estaba priorizada por criticidad. **Corrección**: ordenar por momentos críticos, después petición explícita y repetida, y por último relleno de ambiente; si el presupuesto no llega, lo que se cae es el relleno.

## Casos de prueba

Los cuatro casos están en `cases/`, con entrada y salida reales.

**Happy path** (`cases/case_01_happy_path.md`): lista de boda por WhatsApp con 28 peticiones y
marcas de hora, biblioteca de 8.412 tracks. Salen 19 TENGO, 5 NO TENGO, 3 DUDOSO y 2
PROHIBIDO, más el documento de confirmación redactado.

**Edge case** (`cases/case_02_edge_case.md`): transcripción de audio de la madre de la novia,
sin puntuación y con referencias vagas. La mitad de las líneas son conversación.

**Failure** (`cases/case_03_failure.md`): sin export de biblioteca. Se entrega el parseo, los
prohibidos y la agrupación con todo el cruce marcado PENDIENTE DE BIBLIOTECA, más la ruta
exacta de exportación.

**Integration** (`cases/case_04_integration.md`): encadenado con `set-por-encargo`. El cubo
TENGO más las compras aprobadas forman el pool de entrada del set del evento.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
