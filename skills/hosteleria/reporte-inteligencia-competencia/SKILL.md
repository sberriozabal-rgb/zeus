---
name: reporte-inteligencia-competencia
description: >-
  Genera un reporte semanal de inteligencia sobre la reputación digital de un
  restaurante frente a seis competidores nombrados. Cruza calificación media,
  volumen de reseñas, recencia y tasa de respuesta de Google, TripAdvisor/TheFork
  y una tercera fuente; señala qué hacen bien los competidores, qué hace peor la
  marca, y tres acciones para la semana. Úsala cuando alguien pida "un reporte de
  competencia", "qué dicen de mis competidores", "cómo voy contra los de mi zona",
  "vigilar reseñas de la competencia", "informe semanal de reputación" o "compara
  mi restaurante con otros" — aunque no diga la palabra inteligencia. Trabaja solo
  con fuentes públicas; nunca inventa reseñas. No la uses para responder reseñas
  propias (usa respuesta-resenas) ni para un dossier de venta a un grupo.
license: Propietario — TROQUEL. Prohibida la redistribución del artefacto.
compatibility: Requiere acceso a búsqueda y lectura web. Ejecutable en Claude Code y en app con herramientas de búsqueda activas.
allowed-tools: WebSearch, WebFetch, Read, Write
metadata:
  version: "1.1.0"
  estado: ACORDADO
  linea: hosteleria
  peldano: P1
  motor: B
  auditoria: 17/20
---

# reporte-inteligencia-competencia

## Qué hace

Convierte **el nombre de un restaurante y los de seis competidores** en **un reporte semanal de
una página con semáforo de cuatro métricas contra la mediana del panel, los temas de elogio que
ellos cargan y la marca no, y tres acciones para esta semana con responsable y fecha**, para **el
dueño de un restaurante independiente**, en **menos de 60 minutos**.

No opina, no vende y no adorna: produce evidencia con plataforma y fecha de consulta, y la
convierte en tres movimientos que el dueño puede hacer antes del próximo fin de semana. El
entregable es **una página**. Si no cabe, sobra análisis y falta decisión.

## Cuándo se dispara

- "qué dicen de mis competidores"
- "cómo voy contra los de mi zona"
- "quiero vigilar las reseñas de la competencia"
- "compara mi restaurante con otros"
- "necesito un informe semanal de reputación"
- "el de enfrente está lleno y yo no, ¿por qué?"
- "¿voy bien de valoración o mal?"
- "qué hacen ellos que yo no estoy haciendo"
- jerga del gremio: "reseñas", "estrellas", "valoración", "ficha de Google", "TripAdvisor",
  "TheFork", "competencia", "la zona", "mediana", "brecha", "semáforo", "recencia",
  "tasa de respuesta", "corte semanal"

## Quién lo ejecuta

El dueño del restaurante, o quien lleve su marketing, con **45 a 60 minutos** de atención para el
primer corte: confirmar los seis competidores, localizar las fichas en tres plataformas y leer el
reporte. Los cortes siguientes bajan a **20-30 minutos**, porque el panel ya está fijado y solo se
recapturan las cuatro métricas.

## Entrada

- **Obligatorio:** nombre y ciudad del restaurante.
- **Obligatorio:** los **seis competidores**, nombrados por el dueño. Si no los da, se piden
  **una vez**; si aun así faltan, se trabaja con los que haya (mínimo 3) marcando
  `[COMPETIDOR NO APORTADO]`.
- **Recomendado:** la tercera plataforma donde el local tiene presencia (Instagram público,
  prensa gastronómica local o agregador de delivery), porque el consumidor consulta de media
  **seis fuentes** y cubrir solo Google deja fuera la mayor parte de la decisión.
- **Recomendado:** el reporte de la semana anterior, para comparar la brecha y verificar si las
  tres acciones se ejecutaron.
- **Dato sucio típico:** dos locales con el mismo nombre en la misma ciudad. **Se reportan ambos
  y se pide desempate**, deteniendo solo esa ficha, nunca el reporte entero. El segundo dato
  sucio es la divergencia entre plataformas para la misma métrica: **se reportan las dos y no se
  promedia en silencio**, porque la divergencia es en sí misma un hallazgo.

## Umbral que sostiene el producto

**Los cuatro cortes de decisión del semáforo**, todos con fuente:

| Métrica | 🟢 Verde | 🟡 Ámbar | 🔴 Rojo | Por qué |
|---|---|---|---|---|
| Calificación media | ≥ 4,5★ | 4,0–4,4★ | < 4,0★ | El **31 %** solo usa negocios de 4,5★+ (subió desde 17 % en 2025). Por debajo de 4,5 te caes del set de elección |
| Volumen de reseñas | ≥ 100 | 20–99 | < 20 | El **47 %** no usa un negocio con menos de 20 reseñas: es umbral de credibilidad, no de vanidad |
| Recencia | ≤ 7 días | 8–14 días | > 14 días | El **32 %** solo se fía de reseñas de las últimas dos semanas y el 18 % de la última |
| Tasa de respuesta | 100 % | 50–99 % | < 50 % | Más del **80 %** cree que el negocio debe responder a **todas** las reseñas |

**Regla del 5.0: el objetivo no es 5,0.** Solo el 10 % de consumidores exige cinco estrellas y un
5,0 clavado puede leerse como falso. **La diana es 4,5-4,8.**

**Regla de cobertura:** el consumidor consulta de media **seis fuentes**; Google lidera con un
71 % **y cayendo** (desde 83 %), y los asistentes de IA ya pesan un 45 %. Por eso el reporte cubre
un mínimo de tres plataformas y no solo Google.

Todas las cifras proceden de BrightLocal *Local Consumer Review Survey*
(<https://www.brightlocal.com/research/local-consumer-review-survey/>), edición 2026 salvo la
tasa de respuesta que es de la 2025.

**`[CONTEXTO EE. UU. — A VALIDAR para ES/MX]`:** son la mejor cifra pública disponible, pero el
panel es de 1.002 adultos estadounidenses. El comportamiento hispanohablante puede diferir y
**debe reverificarse antes de usarlas como promesa de venta**.

## Procedimiento

1. **Entrada: nombre y ciudad de la marca más los seis competidores → Acción: confirmar sujetos,
   pidiendo los que falten una sola vez → Salida: lista de 1 marca y hasta 6 competidores, cada
   uno con su ciudad → Si faltan competidores: se trabaja con los que haya, mínimo 3, marcando
   `[COMPETIDOR NO APORTADO]`; si hay dos locales homónimos, se reportan ambos y se pide
   desempate.**

2. **Entrada: los nombres confirmados → Acción: localizar la ficha pública de cada local en
   Google, en TripAdvisor o TheFork y en una tercera fuente, usando WebFetch solo sobre páginas ya
   localizadas → Salida: la URL de cada ficha encontrada, por local → Si una fuente no tiene ficha
   del local: `[SIN DATO PÚBLICO]`, que es un hallazgo y no un hueco que rellenar.**

3. **Entrada: las fichas localizadas → Acción: capturar en el momento, con fecha de consulta, las
   cuatro métricas duras de cada local: calificación media, número de reseñas, fecha de la reseña
   más reciente visible y si el negocio responde → Salida: tabla de 4 columnas por local → Si dos
   fuentes divergen en un número: se reportan ambos y **no se promedia en silencio**.**

4. **Entrada: la tabla de métricas → Acción: calcular la **mediana** de los competidores en cada
   métrica y la diferencia de la marca contra ella → Salida: fila BRECHA con signo, + por delante
   y − por detrás → Si un competidor es atípico (5,0 con 6 reseñas): se señala como nota al pie,
   no se excluye ni se deja distorsionar la referencia, que por eso es mediana y no media.**

5. **Entrada: la brecha → Acción: aplicar los cuatro cortes del semáforo tal como están en la
   tabla, sin ajustarlos → Salida: cada métrica en verde, ámbar o rojo → Si el resultado sale
   todo verde y no encaja con lo que el dueño percibe: se revisa la captura, **no se aflojan los
   cortes**.**

6. **Entrada: las reseñas del panel → Acción: leer lo cualitativo y extraer los temas de elogio
   que se repiten en los competidores (mínimo 3 menciones) y las quejas propias que los
   competidores no cargan, cada uno anclado a plataforma y fecha → Salida: temas con su cita
   anclada → Si un tema no llega a 3 menciones: no entra; es anécdota.**

7. **Entrada: brecha y temas → Acción: escribir exactamente **tres acciones** para esta semana,
   cada una con verbo, responsable y día → Salida: tres filas, ni dos ni siete → Si salen más de
   tres: se eligen las tres de mayor impacto, porque más de tres no se ejecutan en una semana.**

8. **Entrada: todo lo anterior → Acción: montar el reporte en la plantilla de una página y cerrar
   con el anexo de fuentes, la lista de `[SIN DATO PÚBLICO]` y el pie legal literal → Salida:
   una página → Si no cabe en una página: sobra análisis y falta decisión, y se recorta el
   análisis.**

## Salida

```
REPORTE DE INTELIGENCIA — [MARCA] · Semana del [fecha]
Fecha de corte: [fecha de consulta]

SEMAFORO (marca vs. mediana de [n] competidores)
                     Marca      Mediana comp.   Brecha   Estado
Calificacion (*)     [ ]        [ ]             [+-]     [verde/ambar/rojo]
Volumen resenas      [ ]        [ ]             [+-]     [ ]
Recencia (dias)      [ ]        [ ]             [+-]     [ ]
Tasa de respuesta    [ ]%       [ ]%            [+-]     [ ]

LO QUE HACEN BIEN ELLOS (temas de elogio, >=3 menciones)
- [tema] — [competidor] · [plataforma] · [fecha]

LO QUE HACEMOS PEOR (quejas propias que los competidores no cargan)
- [tema] — [plataforma] · [fecha]

TRES ACCIONES PARA ESTA SEMANA
1. [verbo] — responsable: [ ] — para: [dia]

FUENTES: [URLs consultadas con fecha]
[SIN DATO PUBLICO]: [lo que no se pudo consultar]

## Supuestos de esta versión
[competidores no aportados, fichas sin dato publico, divergencias entre fuentes]

CONFIDENCIAL · Analisis basado exclusivamente en fuentes publicas ·
Investigacion de escritorio: no sustituye visita ni due diligence ·
No constituye asesoria legal ni financiera · Cifras a re-verificar a la
fecha de uso · Umbrales de comportamiento [CONTEXTO EE. UU. — A VALIDAR ES/MX].
```

## Límites

- **Solo fuentes públicas.** No accede a paneles privados de reseñas ni extrae datos personales.
- **No responde reseñas.** Ese trabajo es de `respuesta-resenas`, y mezclarlo rompe el límite del
  artefacto.
- No sustituye la decisión del dueño, ni asesoría legal o financiera. Es investigación de
  escritorio, no *due diligence*.
- Los umbrales de comportamiento son de mercado estadounidense y para ES/MX van marcados a
  validar. No se usan como promesa de venta sin esa etiqueta.
- Si un competidor está bajo relación contractual o personal con el cliente, **se detiene esa
  ficha y se avisa**.
- Un corte aislado vale poco: el producto es la serie semanal, y sin la semana anterior no hay
  brecha que comparar ni acciones que verificar.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Registrar cada cifra con plataforma y fecha de consulta | Un número sin fuente y fecha no se puede defender ante un dueño que pregunta de dónde sale |
| Usar la mediana de los competidores, nunca la media | Un competidor atípico —5,0 con 8 reseñas— distorsiona la media y dispara una falsa alarma |
| Marcar lo no consultable como `[SIN DATO PÚBLICO]` | Un hueco declarado es un hallazgo; un hueco rellenado es un fraude |
| Reportar temas, nunca reseñadores por su nombre | La persona es dato privado; el patrón es la inteligencia |
| Entregar exactamente tres acciones, ni dos ni siete | Más de tres no se ejecutan en una semana; menos de tres desaprovecha el reporte |
| Cerrar con el pie legal literal | Protege la casa y fija que es investigación de escritorio, no *due diligence* |
| Caber en una página | Si no cabe, sobra análisis y falta decisión |
| Cubrir un mínimo de tres plataformas | El consumidor consulta seis de media y Google ya solo pesa un 71 %, cayendo desde el 83 % |
| Exigir tres menciones antes de declarar un tema | Por debajo es anécdota, y construir una acción sobre una reseña suelta manda al equipo a perseguir fantasmas |
| Anclar toda cita de tema a plataforma y fecha | Sin ancla no es evidencia, y el dueño no puede recomprobarla |

| NUNCA | Porqué |
|---|---|
| Inventar una reseña, una cifra o un tema | Una sola reseña inventada quema la confianza del dueño para siempre y hunde el producto |
| Adivinar quiénes son los competidores | Si el dueño no los nombra, se piden; sugerirlos sin confirmar es meter ruido por diseño |
| Promediar en silencio dos fuentes que divergen | Se reportan ambas: la divergencia es en sí misma un hallazgo, y elegir sin decirlo lo oculta |
| Marcar verde una métrica que está en ámbar | El semáforo solo sirve si es honesto; un verde regalado desactiva la única alarma útil |
| Usar estas cifras como promesa de venta sin la etiqueta `[CONTEXTO EE. UU. — A VALIDAR]` | Prometer un dato de otro mercado como propio es una cifra huérfana que el cliente descubre |
| Responder reseñas desde aquí | Ese trabajo es de `respuesta-resenas`; mezclarlo rompe el límite del artefacto |
| Aflojar los cortes del semáforo para que el reporte dé buenas noticias | Los cortes son fijos y están en la tabla; ajustarlos por caso convierte el semáforo en decoración |
| Poner 5,0 como objetivo | Solo el 10 % de consumidores exige cinco estrellas y un 5,0 clavado se lee como falso: la diana es 4,5-4,8 |
| Analizar la ficha de un competidor con el que el cliente tenga relación contractual o personal | Se detiene esa ficha y se avisa; seguir adelante pone al cliente en un conflicto que no pidió |

## Antipatrones

1. **Síntoma**: el reporte cita una reseña con texto entrecomillado que no aparece en ninguna URL de la sección de fuentes. **Causa raíz**: se rellenó un hueco cualitativo de memoria en vez de dejarlo vacío. **Corrección**: toda cita de tema va anclada a plataforma y fecha; sin ancla, se borra.

2. **Síntoma**: la brecha marca "muy por detrás" pero resulta que un competidor tiene 5,0 con 6 reseñas. **Causa raíz**: se usó media en vez de mediana y un atípico la disparó. **Corrección**: mediana siempre, y el atípico se señala como nota al pie, nunca como referencia.

3. **Síntoma**: la marca sale toda en verde pero el dueño sabe que va mal. **Causa raíz**: se aflojaron los cortes para que el reporte diera buenas noticias. **Corrección**: los cortes son fijos y están en la tabla del umbral; si el verde no encaja con la realidad percibida, se revisa la captura, no el corte.

4. **Síntoma**: tres páginas de análisis y ninguna acción clara. **Causa raíz**: se documentó todo lo encontrado en vez de decidir. **Corrección**: una página y tres acciones; el detalle se va al anexo de fuentes.

5. **Síntoma**: aparece en el panel un competidor que el dueño no nombró y que no compite de verdad con el local. `[DERIVADO, NO OBSERVADO EN CAMPO]` **Causa raíz**: faltaban competidores y se completó el panel por proximidad geográfica en vez de por competencia real. **Corrección**: se piden una vez; si no llegan, se trabaja con un mínimo de 3 marcando `[COMPETIDOR NO APORTADO]`, y nunca se rellena el panel para llegar a seis.

## Casos de prueba

Los cuatro casos están en `cases/`, con entrada y salida reales.

**Happy path** (`cases/case_01_happy_path.md`): restaurante con los seis competidores aportados y
fichas en tres plataformas. Sale el semáforo completo con dos métricas en rojo y tres acciones de
coste cero.

**Edge case** (`cases/case_02_edge_case.md`): dos plataformas divergen en la calificación del
mismo local. Se reportan ambas y la divergencia se convierte en el hallazgo principal del corte.

**Failure** (`cases/case_03_failure.md`): el dueño no aporta ningún competidor y solo hay ficha de
Google. Se emite el reporte con 3 competidores marcados y las celdas sin dato declaradas.

**Integration** (`cases/case_04_integration.md`): encadenado con `respuesta-resenas`. Las quejas
propias que el semáforo identifica son la entrada del informe de respuestas.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
