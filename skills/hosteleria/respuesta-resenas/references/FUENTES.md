# FUENTES — respuesta-resenas

Cada cifra que sale en un informe al cliente tiene que estar en esta tabla, o ir marcada
`[A VALIDAR]`. Una cifra sin fuente en material de venta es la que rompe la confianza
cuando el dueño pregunta "¿eso de dónde lo sacas?". Y en esta skill hay una capa más: se
toca reputación pública, y **la línea entre pedir reseñas y manipularlas está escrita en
la política de las plataformas y en la ley española**. Esa línea va aquí, no en la
intuición del que instala.

Verificadas el 16-ago-2026. Revalidar cada trimestre.

---

## 1. Efecto de una estrella sobre los ingresos — la cifra que sostiene la venta

**Afirmación que sostiene:** "Una estrella adicional de media equivale a un +5% a +9% de
ingresos, y el efecto solo existe en restaurantes independientes, no en cadena."

- **Fuente primaria localizada:** Michael Luca, *Reviews, Reputation, and Revenue: The
  Case of Yelp.com*, Harvard Business School Working Paper **12-016**.
- **URL (PDF del working paper en HBS):** https://www.hbs.edu/ris/Publication%20Files/12-016_a7e4a5a2-03f9-490d-b093-8f951238dba2.pdf
- **URL (ficha del paper):** https://www.hbs.edu/faculty/Pages/item.aspx?num=41233
- **Texto verificado, literal del abstract:** *"(1) a one-star increase in Yelp rating
  leads to a 5-9 percent increase in revenue, (2) this effect is driven by independent
  restaurants; ratings do not affect restaurants with chain affiliation."*
- **Muestra:** Seattle (Washington, EE. UU.), datos trimestrales **2003-2009**, 3.582
  restaurantes (≈1.587 operando por trimestre), cruzando ingresos declarados al
  Departamento de Ingresos del Estado de Washington con reseñas de Yelp. En cadenas el
  efecto es *"statistically insignificant and close to zero"*.
- **Límites de uso, que se dicen en la visita si el cliente pregunta:**
  1. Es **Yelp**, no Google ni TripAdvisor. La mecánica es la misma —media pública que
     el cliente ve antes de decidir— pero la plataforma no es la misma.
  2. Es **Seattle 2003-2009**. No es España, no es México y no es 2026.
  3. Es un efecto sobre **ingresos declarados**, no sobre margen ni sobre beneficio.
  4. Lo que sí es sólido y es lo que se vende: el efecto **existe en independientes y no
     en cadenas**, y eso es exactamente el comprador de esta skill.
- **Cómo se presenta siempre:** como rango de referencia de mercado con su fuente, nunca
  como promesa de resultado económico. Está en `umbrales-resenas.md` §1 y es regla de la
  casa.

## 2. El medio punto de estrella — de dónde sale el "+2,5% a +4,5%"

**Afirmación que sostiene:** el escenario que imprime `scripts/resenas.py` y que aparece
en `cases/case_01_happy_path.md`: "con una mejora de 0,5 estrellas, el rango de
referencia es +2,5% a +4,5%".

- **Fuente:** el mismo paper. Y aquí hay un matiz que **juega a favor** y que conviene
  conocer antes de que lo pregunte alguien: el diseño de regresión discontinua de Luca
  explota el redondeo de Yelp **a la media estrella**, de modo que el salto real que
  mide es de medio punto. Texto verificado: *"I find that an exogenous one-star
  improvement leads to a roughly 9% increase in revenue. (Note that the shock is
  one-half star, but I renormalize for ease of interpretation)"*.
- **Qué significa eso, exactamente:** el **+4,5%** del extremo alto no es una
  interpolación nuestra, es prácticamente el efecto bruto que el paper estima para medio
  punto antes de renormalizar. El **+2,5%** del extremo bajo **sí es una división por dos
  del 5% del rango**, y esa división la hacemos nosotros: el paper no afirma que la
  relación sea lineal (usa términos cuadráticos y pendientes distintas a cada lado del
  corte). `[A VALIDAR — el extremo bajo del rango es derivado, no publicado]`
- **Regla operativa:** si un cliente pide la cifra exacta para 0,3 estrellas o para 0,8,
  no se interpola: se le da el rango de una estrella con su fuente y se dice que el
  efecto no es proporcional.

## 3. Política de Google sobre incentivar reseñas — el límite que no se cruza

**Afirmación que sostiene:** el apartado 5 del informe ("cómo conseguir más reseñas
buenas") recomienda **pedir** reseñas, y eso es legítimo; **comprarlas, premiarlas o
filtrar quién las deja** no lo es, y la diferencia está escrita.

- **Fuente:** Google, *Prohibited & restricted content* — política de contenido generado
  por usuarios de Maps / Perfil de Empresa.
- **URL:** https://support.google.com/contributionpolicy/answer/7400114
- **URL (misma política en la ayuda de Perfil de Empresa):** https://support.google.com/business/answer/7400114
- **Texto verificado, literal.** Prohibido para el comerciante:
  - *"Offer incentives – such as payment, discounts, free goods and/or services - in
    exchange for posting any review or revision or removal of a negative review."*
  - *"Discourage or prohibit negative reviews, or selectively solicit positive reviews
    from customers"* — esto es **review gating**, y está prohibido con esas palabras.
  - No *"require or pressure users to leave ratings or write reviews while on the
    premises"*, ni pedir que la reseña incluya un contenido concreto.
  - En "Fake engagement": *"Reviews or ratings that have been paid for, directly or in
    kind."* En "Rating manipulation": *"Content that has been posted due to an incentive
    offered by a business - such as payment, discounts, free goods and/or services."*
- **Y lo que SÍ está permitido, literal** —que es justo lo que la skill recomienda—:
  *"Solicit or encourage the posting of content that does represent a genuine
  experience, without offering incentives to do so or attempting to influence the rating
  or the contents of the review."*
- **Traducción operativa para el guion de instalación:** pedir la reseña al cliente
  contento, en persona, con un QR, **sí**. El postre gratis, el 10% de descuento, el
  sorteo, el "déjame cinco estrellas" y el preguntar primero si le ha gustado para pedir
  reseña solo a los que dicen que sí, **no**. Esta última es la que más se hace sin
  saber que está prohibida.

## 4. Política de Tripadvisor sobre incentivar reseñas

**Afirmación que sostiene:** la misma línea, en la otra plataforma donde vive un
restaurante.

- **Fuente:** Tripadvisor, *Trust & Safety — Review Posting Guidelines*.
- **URL:** https://www.tripadvisor.com/Trust-lvBd3L1aU38Y.html
- **Texto verificado, literal:**
  - *"It is against our guidelines to offer or promise anything in exchange for any
    reviews, irrespective of rating."* — **cualquier cosa, y con cualquier puntuación**:
    incluye premiar una reseña buena ya publicada.
  - *"Tripadvisor is staunchly opposed to the selling, purchasing, or quid-pro-quo
    exchange of reviews."*
  - *"It is a violation of our guidelines for a property to offer incentives designed to
    reward employees for encouraging reviews."* — **el incentivo al camarero por reseñas
    conseguidas también está prohibido**, y esa es la que más aparece en un restaurante.
  - Prohíbe igualmente el **review gating** y que personas vinculadas al negocio
    intervengan en la redacción de las reseñas.
- **Nota de verificación:** la página de ayuda específica sobre incentivos
  (`tripadvisorsupport.com/hc/en-us/articles/200614977`) **no se pudo recuperar el
  16-ago-2026** (bloqueada por `robots.txt`). El texto de arriba procede de las
  directrices de publicación de Tripadvisor, que es la fuente normativa.

## 5. Qué dice la ley española — porque una política de plataforma no es una multa

**Afirmación que sostiene:** en España esto no es solo "te pueden borrar las reseñas".
Es una práctica de competencia desleal con régimen sancionador propio, y el dueño de un
restaurante independiente no lo sabe.

- **Fuente:** Real Decreto-ley 24/2021, que modifica los artículos **26 y 27 de la Ley
  3/1991 de Competencia Desleal** (transposición de la Directiva (UE) 2019/2161,
  "Ómnibus"). En vigor desde el **28-may-2022**.
- **URL (análisis jurídico con el articulado):** https://www.garrigues.com/es_ES/noticia/fake-reviews-real-decreto-ley-242021-introduce-nuevas-medidas-evitar-resenas-falsas-bienes-o
- **Conductas desleales en todo caso, verificadas:**
  - **Art. 27.7** — presentar como reseñas de consumidores reales las que no se han
    verificado como tales, sin haber *"tomado las medidas razonables y proporcionadas
    para garantizar que realmente pertenecen a los mismos"*.
  - **Art. 27.8** — *"Añadir o encargar a terceros que incluyan reseñas o aprobaciones
    de consumidores falsas, o distorsionarlas"*. **"Distorsionarlas" es donde cae el
    review gating.**
  - **Art. 26.2** — clasificaciones superiores sin revelar que obedecen a publicidad
    retribuida o a un pago específico.
- **Sanciones (art. 49 del Real Decreto Legislativo 1/2007, TRLGDCU):** infracciones
  leves **150 a 10.000 €**, graves **10.001 a 100.000 €**, muy graves **100.001 a
  1.000.000 €**, con posibilidad de superar esas cuantías en función del beneficio
  ilícito, y hasta el **4% del volumen de negocio anual** (o 2.000.000 € si no consta)
  en el marco del Reglamento (UE) 2017/2394.
  https://www.iberley.es/legislacion/articulo-49-ley-defensa-consumidores-usuarios
- **Cobertura sectorial del caso concreto de hostelería:** InfoHoreca, 05-feb-2024,
  "El filtrado de reseñas de restaurantes puede ser sancionado con hasta 100.000 euros",
  que describe el review gating como *"solicitar un feedback como mecanismo de
  identificación de clientes satisfechos para posteriormente pedir una reseña solo a
  aquellos que están satisfechos"*.
  https://www.infohoreca.com/noticias/20240205/filtrado-resenas-restaurantes-sanciones
- **Límite de uso, sin excepción:** esto **no es asesoría legal**, coincide con el
  límite ya declarado en `SKILL.md`. Se cita para explicar por qué la skill no
  recomienda incentivos ni filtrado, no para decirle a un cliente qué multa le
  corresponde. Ante un caso concreto, profesional colegiado.

---

## 6. Cifras en uso que NO se sostienen — se declaran, no se borran

Retirarlas del `SKILL.md` no es competencia de esta revisión de fuentes. Quedan aquí
nombradas para que quien haga la v1.1 sepa exactamente qué tocar.

| Afirmación en uso | Dónde aparece | Qué se encontró al verificarla |
|---|---|---|
| *"Google y TripAdvisor penalizan (y los lectores lo notan) las respuestas idénticas"* | `SKILL.md` §4 del Método | **No se sostiene la parte de la penalización.** La política de contenido prohibido de Google no dice nada sobre respuestas del propietario repetidas o copiadas: su regla de *"posting the same content multiple times"* está en el apartado de contenido de usuario, no de respuestas. La ayuda de Google confirma que las respuestas se revisan contra las políticas de contenido, pero ninguna política publicada las penaliza por ser iguales. Las directrices de Tripadvisor tampoco lo recogen. **La parte de "los lectores lo notan" es criterio de oficio defendible; la palabra "penalizan" es una cifra huérfana en forma de afirmación.** Corrección sugerida para la v1.1: sustituir por "los lectores lo notan, y una respuesta intercambiable no protege ante el siguiente cliente, que es para quien se escribe". |
| *"Tres ya empieza a ser estadísticamente significativo"* | `umbrales-resenas.md` §2 | **No se sostiene como afirmación estadística.** No hay contraste de hipótesis detrás, ni serie publicada de la que salga. Es criterio de oficio, y como criterio de oficio se defiende bien; como estadística, no. Corrección sugerida: "tres ya deja de parecer casualidad para un local con este volumen de reseñas". |
| Umbral de patrón **3 menciones en 60 días** | `SKILL.md` §3, `umbrales-resenas.md` §2, constantes `UMBRAL_PATRON_MENCIONES` y `UMBRAL_PATRON_DIAS` del motor | **`[A VALIDAR]`.** Ninguna fuente publica ese corte. El propio archivo ya lo declara orientativo y ajustable por volumen, que es lo correcto. Se mantiene como criterio de oficio calibrable en la instalación, igual que los umbrales de `comparativa-proveedores`. |
| *"Rara vez más de 10-20 reseñas nuevas al mes"* en un independiente | `umbrales-resenas.md` §2 | **`[A VALIDAR]`.** No se localizó fuente publicada y fechada del volumen medio de reseñas nuevas de un restaurante independiente en España o México. Se usa como orden de magnitud para justificar el umbral, no como dato. |
| *"Pedirlo por email genérico días después tiene una tasa de respuesta mucho menor"* | `umbrales-resenas.md` §3 | Ya venía marcado **[SIN VERIFICAR]** en el propio archivo, y así sigue. Búsqueda de ago-2026 sin cifra publicada y fechada para hostelería. Se mantiene declarado, no se rellena. |

## 7. Huecos declarados — cifras que NO tenemos

| Cifra que haría falta | Estado | Por qué no se rellena |
|---|---|---|
| Efecto de una estrella sobre ingresos medido en **Google** (no Yelp) | `[A VALIDAR]` | No localizada con metodología publicada. La cifra que se usa es la de Yelp y se dice que lo es. |
| Efecto de una estrella en **España** o **México** | `[A VALIDAR]` | No localizado ningún estudio con datos fiscales equivalentes al de Luca. Se declara que la referencia disponible es de EE. UU., 2003-2009. |
| Efecto de **responder** a las reseñas sobre la media futura | `[A VALIDAR]` | Es la afirmación implícita de todo el producto y no tenemos fuente propia verificada. Hoy la skill no promete ninguna cifra por responder, y así debe seguir hasta que la haya. |
| Momento óptimo del servicio para pedir la reseña | `[A VALIDAR]` | Criterio de oficio, ver §6. Lo que sí está anclado con fuente es **a quién no pedírsela y de qué forma no pedirla** (puntos 3, 4 y 5 de este documento). |
