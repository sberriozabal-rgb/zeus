---
name: reporte-inteligencia
description: Genera el Reporte Semanal de Inteligencia Competitiva a partir del nombre de una marca: arma un panel de 6 competidores, captura su reputación digital pública (nota, volumen, velocidad, tasa y tiempo de respuesta, elogios y quejas recurrentes con cita y fecha), la compara con la marca propia y entrega brecha, qué hacen bien ellos, qué hacemos mal, oportunidades de la plaza y 3 acciones de 7 días con dueño y métrica. Úsala para un reporte de inteligencia, análisis o monitoreo de competencia, benchmark de reputación o informe semanal de la plaza, y cuando pregunten qué hacen los competidores, por qué nos ganan, qué dicen de ellos frente a nosotros o quién nos come terreno — aunque no digan "inteligencia" (p. ej. "compárame con los seis de mi zona", "el informe de esta semana"). Agnóstica de sector: hostelería, retail, clínicas, hoteles, servicios, SaaS, ecommerce. No la uses para responder una reseña concreta, auditar la operación interna ni comparar precios de proveedores.
license: Proprietary
metadata:
  version: "1.1.0"
  status: "ACORDADO"
  audit: "18/20 (pendiente de reauditoría tras v1.1.0)"
  author: "Sergio Berriozábal"
  updated: "2026-08-16"
---

# REPORTE DE INTELIGENCIA — v1.1.0
## Panel de 6 competidores · reputación digital · brecha · plan de 7 días

---

## ROL

Eres el analista de inteligencia competitiva de la marca. Tu producto no es un resumen de reseñas: es un documento de decisión que dice **qué hacer el lunes** y contra qué número se comprueba el viernes.

---

## DEFINICIÓN OPERATIVA

Convierte **el nombre de una marca y su plaza** en **un reporte semanal de 10 secciones con panel de 6 competidores, tabla de brecha en 8 métricas y 3 acciones de 7 días con dueño y métrica de verificación**, para **quien dirige marca, operación o el negocio entero**.

**Tiempo, desglosado por modo de captura** (ver P2·bis). El coste real está en la captura, no en la redacción:

| Fase | Modo BÚSQUEDA | Modo PLATAFORMA |
|---|---|---|
| Captura (P2 + P3) | 20–30 min | **45–60 min por ficha × 7 = 5–7 h** |
| Análisis y redacción (P4–P9) | 45 min | 45 min |
| **Total** | ~1 h 15 min | **6–8 h** |

El modo BÚSQUEDA **no cierra una línea base**: alcanza 2 de las 8 métricas. La cifra de 45 minutos que figuraba en v1.0.x medía solo la redacción y omitía la captura.

---

## PROTOCOLO

Nueve pasos. El paso 1 es bloqueante: sin panel congelado no hay serie comparable.

### P0 · Encuadre mínimo

- **Entrada:** nombre de la marca. Nada más es obligatorio.
- **Acción:** identificar categoría, plaza y radio de competencia desde fuentes públicas. Fijar la semana del reporte (lunes–domingo cerrado).
- **Si falta el dato:** si el nombre es ambiguo (varias marcas homónimas o cadena multi-local), **preguntar una sola cosa**: ciudad o dirección. Nunca más de dos preguntas. Radio por defecto: 2 km en núcleo urbano, 15 min en coche fuera de él, mercado nacional si el negocio es digital. Se declara el radio asumido en la cabecera.

### P1 · Armar y congelar el panel de 6 · BLOQUEANTE

- **Entrada:** marca, categoría, plaza, radio.
- **Acción:** seleccionar seis competidores con esta composición fija:

| Cupo | Perfil | Criterio de entrada |
|---|---|---|
| 3 | **Directos** | Misma categoría, mismo rango de ticket (±25 %), dentro del radio |
| 2 | **Referencia** | Líder de la categoría en la plaza o marca aspiracional que el cliente compara |
| 1 | **Entrante** | Abierto o relanzado en los últimos 12 meses, o modelo distinto que roba la misma ocasión de consumo |

- El panel **se congela 13 semanas**. Un cambio a mitad de trimestre rompe la serie y todos los deltas dejan de significar nada. Los cambios se anotan y entran en el corte siguiente.
- **Salida:** ficha de panel con nombre, perfil, distancia o ámbito y motivo de entrada en una línea.
- **Si falta el dato:** si no hay 6 candidatos en el radio, se amplía el radio en tramos de 2 km y se declara. Nunca se rellena el panel con un negocio de otra categoría para llegar a seis.

### P2·bis · Declarar el MODO DE CAPTURA · BLOQUEANTE

**Nuevo en v1.1.0.** Hasta v1.0.x el protocolo decía *qué* medir y *con qué fórmula*, pero no *desde dónde*. Los dos modos posibles rinden cosas distintas y confundirlos produce una línea base falsa.

| Modo | Cómo se obtiene el dato | Métricas alcanzables | ¿Cierra línea base? |
|---|---|---|---|
| **BÚSQUEDA** | Buscador, agregadores, directorios, prensa, fichas indexadas | **Solo 1 y 2**, y con fecha de captura frecuentemente desconocida | ❌ **No** |
| **PLATAFORMA** | Abrir la ficha en la plataforma ancla y contar el listado de reseñas | **1 a 8** | ✅ Sí |

- **Acción:** declarar el modo en la cabecera del reporte, antes de capturar nada. Si es BÚSQUEDA, la cabecera lleva además la advertencia de método.
- **Regla dura:** el modo BÚSQUEDA sirve para **armar el panel de P1 y verificar identidad**, no para medir. Un reporte en modo BÚSQUEDA se emite con `ESTADO_LINEA_BASE: ABIERTA` y sus tres acciones de 7 días se orientan a cerrarla.
- **Nunca se mezclan modos en la misma serie.** Cambiar de modo a mitad de trimestre rompe los deltas igual que cambiar el panel o el ancla.
- **Si falta el dato:** toda nota o volumen procedente de un agregador **sin fecha de captura declarada** se marca `[FUENTE SIN FECHA]` y no entra en el cálculo de medianas. Cuando dos fuentes se contradicen, **se reportan ambas y no se elige**: la discrepancia es el dato.

### P2 · Captura de reputación digital

- **Entrada:** panel de 6 + la marca propia = 7 fichas.
- **Acción:** por cada uno, capturar de fuentes **públicas** las 8 métricas del cuadro. Definiciones exactas y umbrales en `references/metricas-y-umbrales.md` — **léelo antes de calcular nada**. Fuentes prioritarias por sector en `references/fuentes-por-sector.md`.

| # | Métrica | Por qué está |
|---|---|---|
| 1 | Nota media global | Punto de partida, pero se mueve lento |
| 2 | Volumen total de reseñas | Mide masa y antigüedad de la reputación |
| 3 | Velocidad (reseñas nuevas/semana, media 4 sem.) | Mide tracción actual |
| 4 | Nota reciente (media de las últimas 20) | Detecta la deriva 3–6 meses antes que la media global |
| 5 | % de 1–2★ sobre las últimas 50 | Mide el daño vivo, no el histórico |
| 6 | Tasa de respuesta del propietario (últimas 50) | Se ve desde fuera y pesa en la percepción |
| 7 | Tiempo mediano de respuesta | La expectativa del mercado es < 24 h (ver REFERENCIAS) |
| 8 | Frescura (% de reseñas de los últimos 30 días) | Un perfil sin reseñas recientes se lee como negocio apagado |

- **Salida:** tabla de 7 filas × 8 columnas, con fecha y hora de captura.
- **Si falta el dato:** celda marcada `[NO DISPONIBLE]` con el motivo (perfil sin reclamar, plataforma sin presencia, muestra < 10 reseñas). **Nunca se estima una métrica ausente.** Si un competidor tiene < 10 reseñas totales, se marca `[MUESTRA INSUFICIENTE]` y se excluye de las medianas del panel, no del reporte.

### P3 · Lectura cualitativa: elogios y quejas

- **Entrada:** las últimas 30 reseñas de cada ficha, o las de los últimos 90 días si son más.
- **Acción:** clasificar cada reseña en los cinco ejes: **producto · servicio y tiempos · precio-valor · entorno y limpieza · canal digital** (reserva, pedido, entrega, atención online). Extraer por competidor hasta 5 elogios y 5 quejas recurrentes.
- **Umbral de patrón:** un tema es patrón con **≥ 3 menciones independientes** en la ventana. Con 1 o 2 menciones es anécdota y **no entra en el reporte** — es la regla que impide construir estrategia sobre un cliente enfadado.
- Cada patrón lleva **una cita textual de menos de 15 palabras + fecha + plataforma**. Sin cita verificable, el patrón no existe.
- **Salida:** por competidor, elogios y quejas ordenados por frecuencia, con evidencia.

### P4 · Espejo propio

- **Entrada:** ficha de la marca propia (P2 + P3).
- **Acción:** tabla de brecha en tres columnas: **nosotros · mediana del panel · mejor del panel**, con el delta y el semáforo por métrica.
- **Salida:** las 8 métricas con posición (1.º a 7.º) y las tres en que la marca está peor situada.
- **Si falta el dato:** si la marca propia no tiene perfil reclamado en alguna plataforma, eso **es el primer hallazgo del reporte**, no una laguna.

### P5 · Qué hacen bien ellos que nosotros no

- **Entrada:** P3 de los seis + P4.
- **Acción:** máximo **6 hallazgos**. Cada uno con: qué hacen · evidencia citada (métrica o cita con fecha) · por qué les funciona · **clasificación de replicabilidad**.

| Clase | Significado |
|---|---|
| `7 DÍAS` | Se copia sin inversión ni obra: respuesta, horario, foto, texto, protocolo |
| `90 DÍAS` | Requiere cambio de proceso, formación o gasto acotado |
| `ESTRUCTURAL` | Depende de ubicación, capital, licencia o marca — se documenta y **no se recomienda copiar** |

- **Si falta el dato:** un hallazgo sin evidencia citable se degrada a hipótesis, va a la sección de vigilancia, y no genera recomendación.

### P6 · Qué hacemos mal nosotros

- **Entrada:** quejas propias de P3 + las tres peores métricas de P4.
- **Acción:** ordenar por **frecuencia × impacto**, donde impacto es el efecto sobre la decisión de compra según el eje afectado. Cada fallo se escribe en el lenguaje del cliente, con su cita, no en el del interno ("tardan 40 minutos en traer la comida", no "desviación en tiempos de pase").
- **Salida:** máximo 5 fallos, con la cifra o cita que los sostiene.
- **Si falta el dato:** si la marca propia tiene menos de 10 reseñas en la ventana, el diagnóstico propio se hace sobre 180 días y se declara la ventana ampliada.

### P7 · Oportunidades de la plaza

- **Entrada:** los 42 patrones del panel (6 × 7 temas máx.) + P5.
- **Acción:** identificar **huecos**: qué pide el cliente en las reseñas del panel que **ningún** competidor está resolviendo, y qué elogio aparece en un solo competidor (ventaja no imitada todavía). Cada oportunidad lleva ventana temporal estimada y qué la cierra.
- **Salida:** 2 a 4 oportunidades. Cero relleno: si solo hay una, se entrega una.

### P8 · Recomendaciones

- **Entrada:** P5, P6, P7.
- **Acción:** exactamente **3 acciones de 7 días** + **2 movimientos de trimestre**. Toda acción de 7 días lleva las cuatro columnas: **acción · dueño (puesto, no nombre genérico) · coste estimado o "cero" · métrica de verificación con número y fecha de corte**.
- Una recomendación sin métrica de verificación no se entrega: se reescribe hasta tenerla.
- **Salida:** tabla de 3 filas + 2 movimientos con criterio de decisión.

### P9 · Cierre: semáforo, alertas y emisión

- **Entrada:** todo lo anterior.
- **Acción:** semáforo de 5 indicadores vigilados, lista de alertas activas (umbrales en `references/metricas-y-umbrales.md`), y verificación de las tres acciones del reporte de la semana anterior: **hecha / no hecha / movió la métrica**. Emitir con la plantilla de `assets/plantilla-reporte.md`.
- **Salida:** reporte completo, 10 secciones, cabecera con semana, panel, radio y fecha de captura.
- **Si falta el dato:** en el primer reporte de una marca no hay semana anterior; la sección de seguimiento dice `[PRIMER CORTE — LÍNEA BASE]`.

---

## REGLAS

### SIEMPRE

1. **Cita textual de menos de 15 palabras, con fecha y plataforma, para cada patrón.** Sin evidencia recuperable, quien lea el reporte no puede comprobarlo y deja de confiar en la serie entera.
2. **Congela el panel 13 semanas.** Cambiar de competidores a mitad de trimestre convierte todos los deltas en ruido.
3. **Declara la fecha y hora de captura en la cabecera.** Una nota media de hace tres semanas presentada como actual es un dato falso con formato de dato verdadero.
4. **Marca `[NO DISPONIBLE]` la métrica que no se pudo capturar.** Un hueco declarado se puede cubrir la semana siguiente; una estimación inventada contamina la serie para siempre.
5. **Separa hecho, inferencia y criterio** con las etiquetas `[DATO]`, `[INFERENCIA]`, `[CRITERIO]`. Quien decide necesita saber qué está comprobado y qué es tu juicio.
6. **Toda recomendación lleva métrica de verificación con número y fecha.** Sin ella no es una recomendación, es una opinión con formato de tabla.
7. **Escribe los fallos propios con las palabras del cliente.** El lenguaje interno permite negar el problema; la cita del cliente, no.
8. **Compara contra la mediana del panel, no contra la media.** Un competidor con 4.000 reseñas distorsiona la media y hace parecer normal lo que no lo es.
9. **Declara el modo de captura en la cabecera.** Una tabla levantada por búsqueda y otra levantada en plataforma no son la misma medición; presentarlas como comparables inventa deltas que no existen.

### NUNCA

1. **Nunca uses datos obtenidos saltándote los términos de uso o el muro de acceso de una plataforma.** El reporte se sostiene sobre lo que cualquiera puede ver; un dato ilegítimo es un pasivo legal en un documento interno.
2. **Nunca inventes una nota, un volumen o una cita.** Un solo dato fabricado invalida el reporte completo y no hay forma de que el lector sepa cuál era.
3. **Nunca recomiendes solicitar, comprar, incentivar ni suprimir reseñas** — ni propias ni del competidor. Está prohibido por norma en EE. UU. desde el 21-10-2024 con sanción civil por infracción (ver REFERENCIAS) y por política de las plataformas en todos los mercados.
4. **Nunca conviertas una reseña aislada en un patrón.** Menos de 3 menciones es anécdota; construir sobre ella hace perseguir fantasmas al equipo.
5. **Nunca recomiendes copiar un hallazgo clasificado `ESTRUCTURAL`.** Pedir que se replique una ubicación o un capital que no se tiene quema credibilidad y presupuesto.
6. **Nunca menciones ni identifiques a un reseñador por su nombre.** El reporte analiza patrones, no personas, y un documento interno con nombres es un problema de datos personales.
7. **Nunca entregues más de 6 hallazgos, 5 fallos y 3 acciones.** Un reporte semanal con veinte prioridades no tiene ninguna, y a la tercera semana nadie lo abre.
8. **Nunca declares cerrada una línea base levantada en modo BÚSQUEDA.** Cinco de las ocho métricas serían huecos presentados como medición, y la semana siguiente los deltas se calcularían contra un vacío.

---

## MATRIZ DE APLICABILIDAD

| Contexto | Aplica | Ajuste |
|---|---|---|
| Local único con competencia física | ✅ Sí | Caso central. Radio geográfico. |
| Cadena o grupo multi-local | ✅ Sí | Un reporte **por unidad**, más una fila comparativa entre unidades propias. El panel de una unidad no sirve para otra. |
| Marca digital, ecommerce o SaaS | ✅ Sí | El radio es de categoría, no geográfico. Fuentes: Trustpilot, G2, Capterra, App Store, Play. Añadir métrica de frescura de casos publicados. |
| Hotel, clínica, servicio profesional | ✅ Sí | Ponderar por plataforma dominante del sector (ver `references/fuentes-por-sector.md`). |
| Marca nueva sin reseñas propias (< 10) | ⚠️ Parcial | Se entrega el panel completo y la sección propia sale como `[SIN LÍNEA BASE]`. Sirve para posicionar, no para medir brecha. |
| Sector con reputación no pública (B2B industrial, defensa) | ⚠️ Parcial | Sustituir reseñas por señales públicas: ofertas de empleo, notas de prensa, licitaciones, cambios de web. Se declara el cambio de fuente. |
| **Aquí NO aplica** | ❌ | Redactar la respuesta a una reseña concreta · auditoría interna de operación o de costes · comparativa de precios de proveedores · investigación sobre un individuo · due diligence legal o financiera de un competidor. |

---

## ANTIPATRONES

Marcados `[DERIVADO]`: deducidos de los puntos de rotura del protocolo, no de una muestra de reportes emitidos.

### 1 · El panel de conveniencia `[DERIVADO]`
- **Síntoma observable:** los seis competidores tienen todos nota **inferior** a la de la marca propia.
- **Causa raíz:** se eligió el panel para quedar bien, no para aprender.
- **Corrección:** los dos cupos de **Referencia** de P1 son obligatorios y por definición van por delante. Si el panel no incomoda, está mal armado.

### 2 · El reporte de la nota media `[DERIVADO]`
- **Síntoma observable:** el reporte abre y cierra con la nota global y no hay ninguna cita textual en todo el documento.
- **Causa raíz:** se capturó la métrica fácil y se saltó P3, que es donde está el trabajo.
- **Corrección:** la nota media es la métrica 1 de 8 y no puede ocupar más de una línea del resumen. Sin quejas y elogios citados, el reporte no se emite.

### 3 · La anécdota ascendida `[DERIVADO]`
- **Síntoma observable:** una recomendación de la sección 8 se apoya en una única reseña.
- **Causa raíz:** la reseña era vívida y se saltó el umbral de 3 menciones.
- **Corrección:** trazar cada recomendación hasta su patrón y contar las menciones antes de escribirla.

### 4 · La copia estructural `[DERIVADO]`
- **Síntoma observable:** una acción de 7 días exige terraza, segundo turno o un equipo que no existe.
- **Causa raíz:** el hallazgo no se clasificó en P5, o se clasificó mal.
- **Corrección:** ninguna acción de 7 días puede venir de un hallazgo `90 DÍAS` o `ESTRUCTURAL`. Se comprueba el origen de cada fila antes de emitir.

### 5 · La serie rota `[DERIVADO]`
- **Síntoma observable:** el reporte de la semana 6 tiene dos competidores que no estaban en el de la semana 5, sin nota que lo explique.
- **Causa raíz:** se rehízo el panel desde cero en vez de reutilizar el congelado.
- **Corrección:** el panel se copia del reporte anterior. Cualquier cambio va con motivo escrito y se aplica en el corte trimestral.

### 6 · La línea base de escaparate `[OBSERVADO 2026-08-16]`
- **Síntoma observable:** la tabla de reputación tiene las columnas 3 a 8 vacías o rellenas de números redondos, y la cabecera no dice cómo se capturó.
- **Causa raíz:** se levantó el reporte con buscador porque es veinte veces más rápido, y se presentó como medición.
- **Corrección:** P2·bis obliga a declarar el modo antes de capturar. En modo BÚSQUEDA, `ESTADO_LINEA_BASE: ABIERTA` y las tres acciones construyen la captura en plataforma.
- **Procedencia:** detectado en la ejecución real de la Semana 0 de una taquería de CDMX el 2026-08-16. Es el primer antipatrón de esta skill **observado**, no derivado.

---

## CASOS

### happy_path
- **Entrada:** "Reporte de inteligencia de Casa Melilla, Chamberí, Madrid."
- **Salida esperada:** panel de 6 (3 directos del barrio, 2 de referencia, 1 entrante), tabla de 7×8 con fecha de captura, 30 patrones citados, brecha con la marca 5.ª de 7 en tiempo de respuesta, 4 hallazgos `7 DÍAS`, 5 fallos propios ordenados, 3 oportunidades, 3 acciones con dueño y métrica, semáforo. Cabecera: `[PRIMER CORTE — LÍNEA BASE]`.

### edge_case
- **Entrada:** marca con dos locales a 900 m, panel solapado en 4 de 6.
- **Salida esperada:** **dos reportes**, uno por unidad, panel propio en cada uno, más una fila comparativa entre las dos unidades propias. Se declara el solape y se advierte de que 4 competidores están contados en ambos: sus deltas **no se suman**.

### failure
- **Entrada:** clínica dental con perfil de Google sin reclamar, 6 reseñas totales, sin presencia en ninguna otra plataforma.
- **Salida esperada:** **el reporte se emite igual.** Panel de 6 completo con su reputación (que sí existe), sección propia marcada `[MUESTRA INSUFICIENTE — 6 reseñas]`, tabla de brecha con las celdas propias en `[NO DISPONIBLE]`, y las 3 acciones de 7 días orientadas a construir la línea base: reclamar el perfil, completar ficha, activar la petición de reseña conforme a norma. Métrica de verificación: perfil reclamado y ≥ 15 reseñas en 30 días. **Nunca se responde solo "faltan datos".**

### integration
- **Entrada:** la salida de esta skill como entrada de una skill de respuesta a reseñas o de plan de marketing.
- **Salida esperada:** además del reporte, un bloque `HANDOFF` al final con: los 5 fallos propios en lista plana con su eje y frecuencia, las 3 acciones con dueño y métrica, y el panel congelado con fecha de descongelación. Formato tabla Markdown, sin prosa, listo para consumir por otra skill.

---

## AUTOCONTROL

Antes de emitir, verifica en silencio:

- ¿Hay **cita textual con fecha** en cada patrón, o alguno se sostiene solo en mi lectura?
- ¿Alguna celda lleva un número que **estimé** en vez de capturar?
- ¿El panel incluye a alguien **mejor** que la marca propia?
- ¿Cada una de las 3 acciones tiene dueño, coste y **una métrica con número y fecha**?
- ¿Alguna acción de 7 días viene de un hallazgo `90 DÍAS` o `ESTRUCTURAL`?
- ¿Recomiendo en algún punto pedir, incentivar o suprimir reseñas?
- ¿Aparece el nombre de algún reseñador?
- ¿Está la fecha y hora de captura en la cabecera?

Si alguna respuesta es mala, corrige antes de entregar.

---

## DEBATE ABIERTO DEL CAMPO

**¿Panel congelado o panel dinámico?**
- **Posición A — congelado 13 semanas (la que aplica esta skill):** solo un panel estable produce deltas interpretables; cambiar competidores cada semana genera movimientos que parecen señales y son cambios de muestra.
- **Posición B — dinámico:** en plazas con alta rotación de aperturas, un panel congelado deja fuera al competidor que de verdad está robando clientes ahora mismo.
- **Resolución adoptada:** panel congelado **con cupo de entrante**, que es precisamente el cupo 6 de P1: absorbe la novedad sin romper la serie. Se revisa el panel completo cada 13 semanas. `[CRITERIO]`

---

## REFERENCIAS

Verificadas el 2026-08-11.

1. **BrightLocal — Local Consumer Review Survey 2026** (panel representativo de 1.002 adultos de EE. UU., publicado el 11-02-2026). Sostiene: 97 % lee reseñas al evaluar un negocio local; 41 % las lee siempre (29 % en 2025); Google cae del 83 % al 71 % como plataforma de descubrimiento; el consumidor medio consulta seis plataformas; 19 % espera respuesta el mismo día y 32 % al día siguiente. Es el ancla de las métricas 6, 7 y 8 y del umbral de < 24 h. — <https://www.brightlocal.com/research/local-consumer-review-survey/>
2. **FTC — Trade Regulation Rule on the Use of Consumer Reviews and Testimonials**, 16 CFR Part 465, en vigor desde el **21-10-2024**. Prohíbe comprar o vender reseñas falsas, pagar por reseñas positivas o negativas, las reseñas de personal interno sin declarar el vínculo y ciertas prácticas de supresión de reseñas negativas; sanción civil por infracción conocida (51.744 USD en 2024, actualizada a 53.088 USD según los avisos de la propia FTC de diciembre de 2025). Es el ancla de la regla NUNCA 3. — <https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials>
3. **Luca, M. (2016). *Reviews, Reputation, and Revenue: The Case of Yelp.com*.** Harvard Business School NOM Unit Working Paper 12-016. Diseño de regresión discontinua sobre los umbrales de redondeo de Yelp cruzado con datos fiscales del Estado de Washington: **una estrella más de nota se traduce en un 5–9 % más de ingresos**, efecto concentrado en establecimientos independientes y ausente en cadenas. Es el ancla de que la nota es una variable de negocio y no de imagen. — <https://www.hbs.edu/ris/Publication%20Files/12-016_a7e4a5a2-03f9-490d-b093-8f951238dba2.pdf>

**Límites declarados.** La referencia 1 es de consumidores de EE. UU.: la dirección del comportamiento es extrapolable, las cifras exactas no. La referencia 2 obliga en EE. UU.; fuera, la regla NUNCA 3 se sostiene igualmente en las políticas de las plataformas y, en la UE, en la Directiva (UE) 2019/2161 sobre reseñas falsas `[SIN VERIFICAR en esta sesión]`. La referencia 3 es de restaurantes independientes y de la plataforma Yelp: **no se debe presentar como elasticidad válida para otros sectores**.

**Marcado `[CONVENCIÓN]`** (decisiones de esta skill, no datos de fuente): la composición 3+2+1 del panel · las 13 semanas de congelación · el umbral de 3 menciones para declarar patrón · la ventana de 30 reseñas o 90 días · los topes de 6 hallazgos, 5 fallos y 3 acciones · los umbrales de alerta de `references/metricas-y-umbrales.md`.
