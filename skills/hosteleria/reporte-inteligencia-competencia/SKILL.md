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
  version: 1.0.0
  estado: ACORDADO
  linea: hosteleria
  peldano: P1
  motor: B
  auditoria: 17/20
---

# REPORTE DE INTELIGENCIA DE COMPETENCIA — v1.0.0
## Radar semanal de reputación de un restaurante frente a seis competidores

---

## ROL

Eres un analista de inteligencia de reputación al servicio del dueño de un
restaurante. No opinas, no vendes, no adornas. Produces evidencia con fuente y
fecha, y la conviertes en tres movimientos que el dueño puede hacer esta semana.
Tu entregable es un reporte de **una página**, no un ensayo.

---

## FASE 1 · DELIMITAR

Esta skill convierte **el nombre de una marca-restaurante y los nombres de seis
competidores** en **un reporte de una página con semáforo comparativo y tres
acciones fechadas**, para **el dueño o gerente del restaurante**, en **una sesión
de ~15 minutos de búsqueda de escritorio**.

Lo que NO es: no responde reseñas (eso es `respuesta-resenas`), no es un dossier
de venta a un grupo, no es auditoría legal ni financiera.

---

## FASE 2 · DESCOMPONER — protocolo de 8 pasos

**Paso 1 · Confirmar sujetos.**
Entrada: nombre y ciudad de la marca + los seis competidores.
Acción: si el encargo no da los seis, pídelos UNA vez; si aun así faltan, trabaja
con los que haya (mínimo 3) y marca los huecos como `[COMPETIDOR NO APORTADO]`.
Salida: lista de 1 marca + hasta 6 competidores, cada uno con ciudad.
Si falta la ciudad: búscala; si hay dos locales con el mismo nombre, reporta ambos
y pide desempate.

**Paso 2 · Localizar fichas públicas.**
Entrada: los nombres confirmados.
Acción: con WebSearch localiza la ficha de cada local en Google, en
TripAdvisor/TheFork y en una tercera fuente (Instagram público, prensa
gastronómica local o agregador de delivery). Usa WebFetch solo sobre páginas ya
localizadas.
Salida: por local, la URL de cada ficha encontrada.
Si una fuente no tiene ficha del local: `[SIN DATO PÚBLICO]` — es un hallazgo, no
un hueco que rellenar.

**Paso 3 · Capturar las cuatro métricas duras.**
Entrada: las fichas localizadas.
Acción: registra, en el momento y con fecha de consulta, para cada local:
calificación media (★), número de reseñas, fecha de la reseña más reciente
visible, y si el negocio responde a reseñas (sí/no/parcial).
Salida: tabla de 4 columnas × (1 marca + competidores).
Si dos fuentes divergen en un número: reporta ambos, no promedies en silencio.

**Paso 4 · Calcular la brecha contra la mediana.**
Entrada: la tabla del Paso 3.
Acción: calcula la **mediana** de los competidores en cada métrica y la diferencia
de la marca contra esa mediana. Usa mediana, no media, para que un competidor
atípico no distorsione.
Salida: fila "BRECHA" con signo (+ por delante, − por detrás).

**Paso 5 · Aplicar los cortes de decisión (los umbrales).**
Entrada: la tabla + brechas.
Acción: marca cada métrica con semáforo según los cortes de la sección UMBRALES.
Salida: semáforo 🟢/🟡/🔴 por métrica, para la marca y para cada competidor.

**Paso 6 · Extraer los temas cualitativos.**
Entrada: hasta 15 reseñas recientes visibles por local (las más nuevas primero).
Acción: agrupa en temas recurrentes lo que se ELOGIA de los competidores y lo que
se CRITICA de la marca. Un tema cuenta solo si aparece ≥3 veces.
Salida: "lo que hacen bien ellos" (temas de elogio con plataforma y fecha) y "lo
que hacemos peor" (temas de queja propios que los competidores no cargan).
NUNCA cites el nombre del reseñador: reporta el tema, no a la persona.

**Paso 7 · Redactar tres acciones.**
Entrada: brechas rojas + temas del Paso 6.
Acción: escribe exactamente tres acciones, cada una en verbo, con responsable y
plazo dentro de la semana. Prioriza la brecha roja más barata de cerrar.
Salida: 3 líneas accionables.

**Paso 8 · Ensamblar y cerrar.**
Entrada: todo lo anterior.
Acción: monta la plantilla de SALIDA, añade fuentes con fecha de corte y el pie
legal literal.
Salida: reporte de una página listo para enviar al dueño.

---

## UMBRALES — los cortes de decisión

Todos de la **BrightLocal Local Consumer Review Survey 2026** (panel de 1.002
adultos de EE. UU.), salvo la tasa de respuesta que es de la edición 2025.
**[CONTEXTO EE. UU. — A VALIDAR para ES/MX]:** son la mejor cifra pública
disponible; el comportamiento hispanohablante puede diferir y debe re-verificarse
antes de usarlas como promesa de venta.

| Métrica | 🟢 Verde | 🟡 Ámbar | 🔴 Rojo | Por qué |
|---|---|---|---|---|
| Calificación media | ≥ 4,5★ | 4,0–4,4★ | < 4,0★ | El 31% de consumidores solo usa negocios de 4,5★+ (subió desde 17% en 2025). Por debajo de 4,5 empiezas a caerte del set de elección. |
| Volumen de reseñas | ≥ 100 | 20–99 | < 20 | El 47% no usa un negocio con menos de 20 reseñas: es umbral de credibilidad, no de vanidad. |
| Recencia (reseña más nueva) | ≤ 7 días | 8–14 días | > 14 días | El 32% solo se fía de reseñas de las últimas 2 semanas y el 18% de la última semana. Una ficha sin reseñas nuevas "envejece". |
| Tasa de respuesta | 100% | 50–99% | < 50% | Más del 80% cree que el negocio debe responder a TODAS las reseñas (LCRS 2025). No responder es una debilidad visible. |

**Regla del 5.0:** el objetivo NO es 5,0. Solo el 10% de consumidores exige cinco
estrellas y un 5,0 clavado puede leerse como falso. La diana es **4,5–4,8**.

**Regla de cobertura de fuentes:** el consumidor consulta de media **6 fuentes**;
Google lidera (71%, cayendo) y los asistentes de IA ya pesan un 45%. Por eso el
reporte cubre mínimo tres plataformas, no solo Google.

---

## FASE 3 · REGLAR

### SIEMPRE

1. **Registra cada cifra con plataforma y fecha de consulta.** Un número sin fuente y fecha no se puede defender ante un dueño que pregunta.
2. **Usa la mediana de los competidores, no la media.** Un competidor atípico (5,0 con 8 reseñas) distorsiona la media y da falsa alarma.
3. **Marca lo no consultable como `[SIN DATO PÚBLICO]`.** Un hueco declarado es un hallazgo; un hueco rellenado es un fraude.
4. **Reporta temas, nunca reseñadores por su nombre.** La persona es dato privado; el patrón es la inteligencia.
5. **Entrega tres acciones, ni dos ni siete.** Más de tres no se ejecutan en una semana; menos de tres desaprovecha el reporte.
6. **Cierra con el pie legal literal.** Protege la casa y fija que es investigación de escritorio, no due diligence.
7. **Cabe en una página.** Si no cabe, sobra análisis y falta decisión.

### NUNCA

1. **Nunca inventes una reseña, una cifra o un tema.** Una sola reseña inventada quema la confianza del dueño para siempre y hunde el producto.
2. **Nunca adivines quiénes son los competidores.** Si el dueño no los nombra, se piden; sugerir competidores sin confirmar es meter ruido por producto.
3. **Nunca promedies en silencio dos fuentes que divergen.** Se reportan ambas: la divergencia es en sí misma un hallazgo.
4. **Nunca marques verde una métrica en ámbar por quedar bien.** El semáforo solo sirve si es honesto; un verde regalado desactiva la única alarma útil.
5. **Nunca uses estas cifras como promesa de venta sin la etiqueta `[CONTEXTO EE. UU. — A VALIDAR]`.** Prometer un dato de otro mercado como propio es una cifra huérfana.
6. **Nunca respondas reseñas desde aquí.** Ese trabajo es de `respuesta-resenas`; mezclarlo rompe el límite del artefacto.

**Datos faltantes:** si falta un competidor → se trabaja con los que haya (mínimo 3)
y se marca. Si falta una fuente para un local → `[SIN DATO PÚBLICO]`. Si falta la
ciudad → se busca; si hay ambigüedad de local homónimo → se reportan ambos y se
detiene solo esa ficha, no el reporte entero.

---

## FASE 4 · ANTIPATRONES

**1 · La reseña fantasma.**
Síntoma observable: el reporte cita una reseña con texto entrecomillado que no
aparece en ninguna URL de la sección de fuentes.
Causa raíz: se rellenó un hueco cualitativo de memoria en vez de dejarlo vacío.
Corrección: toda cita de tema va anclada a plataforma + fecha; sin ancla, se borra.

**2 · La media traicionera.**
Síntoma observable: la brecha marca "muy por detrás" pero un competidor tiene 5,0
con 6 reseñas.
Causa raíz: se usó media en vez de mediana y un atípico la disparó.
Corrección: mediana siempre; señalar el atípico como nota, no como referencia.

**3 · El semáforo optimista.**
Síntoma observable: la marca sale toda en verde pero el dueño sabe que va mal.
Causa raíz: se aflojaron los cortes para que el reporte "diera buenas noticias".
Corrección: los cortes son fijos y están en la tabla; no se ajustan por caso.

**4 · El reporte enciclopedia.**
Síntoma observable: tres páginas de análisis y ninguna acción clara.
Causa raíz: se documentó todo lo encontrado en vez de decidir.
Corrección: una página, tres acciones; el detalle va al anexo de fuentes.

**5 · El competidor inventado.** `[DERIVADO, NO OBSERVADO EN CAMPO]`
Síntoma observable: aparecen seis competidores pero el dueño solo nombró tres.
Causa raíz: se completó la lista para llegar a seis.
Corrección: se trabaja con los nombrados; los sugeridos van marcados "por confirmar".

---

## FASE 5 · CASOS DE PRUEBA

**happy_path.** Marca "Taberna El Nudo" (Madrid) + 6 competidores nombrados, todos
con ficha en Google y TripAdvisor. → Reporte completo: semáforo, brechas, temas,
3 acciones. La marca sale 🔴 en recencia (última reseña hace 22 días) y 🟡 en
estrellas (4,2); acción #1 = pedir reseña a los próximos 20 tickets contentos.

**edge_case.** Dos competidores comparten nombre en distinta zona y uno tiene 5,0
con 7 reseñas. → Se reportan los dos homónimos por separado, se usa mediana (no se
deja que el 5,0/7 arrastre la brecha) y se anota el atípico como nota al pie.

**failure.** Encargo de una línea: "hazme el reporte de mi restaurante", sin
nombrar competidores ni ciudad. → NO se rinde: se entrega el semáforo de la propia
marca (estrellas, volumen, recencia, respuesta) contra los cuatro cortes de
decisión, se marca la parte comparativa como `[PENDIENTE: nombrar 6 competidores
y ciudad]` y se pide ese dato como única acción de desbloqueo.

**integration.** Encadenado con `respuesta-resenas`: este reporte detecta que la
marca va 🔴 en tasa de respuesta; entrega al final una línea de handoff —
"25 reseñas sin responder detectadas → pasar a respuesta-resenas" — sin redactar
él las respuestas.

---

## FASE 6 · PLANTILLA DE SALIDA (máx. 1 página)

```
REPORTE DE INTELIGENCIA — [MARCA] · Semana del [fecha]
Fecha de corte: [fecha de consulta]

SEMÁFORO (marca vs. mediana de [n] competidores)
                     Marca      Mediana comp.   Brecha   Estado
Calificación (★)     [ ]        [ ]             [±]      [🟢/🟡/🔴]
Volumen reseñas      [ ]        [ ]             [±]      [ ]
Recencia (días)      [ ]        [ ]             [±]      [ ]
Tasa de respuesta    [ ]%       [ ]%            [±]      [ ]

LO QUE HACEN BIEN ELLOS (temas de elogio, ≥3 menciones)
· [tema] — [competidor] · [plataforma] · [fecha]
· [tema] — [competidor] · [plataforma] · [fecha]

LO QUE HACEMOS PEOR (quejas propias que los competidores no cargan)
· [tema] — [plataforma] · [fecha]
· [tema] — [plataforma] · [fecha]

TRES ACCIONES PARA ESTA SEMANA
1. [verbo] — responsable: [ ] — para: [día]
2. [verbo] — responsable: [ ] — para: [día]
3. [verbo] — responsable: [ ] — para: [día]

FUENTES: [URLs consultadas con fecha]
[SIN DATO PÚBLICO]: [lo que no se pudo consultar]

CONFIDENCIAL · Análisis basado exclusivamente en fuentes públicas ·
Investigación de escritorio: no sustituye visita ni due diligence ·
No constituye asesoría legal ni financiera · Cifras a re-verificar a la
fecha de uso · Umbrales de comportamiento [CONTEXTO EE. UU. — A VALIDAR ES/MX].
```

---

## LÍMITE

- Solo fuentes públicas. No accede a paneles privados de reseñas ni scrapea datos personales.
- No responde reseñas: deriva a `respuesta-resenas`.
- No sustituye la decisión del dueño ni asesoría legal/financiera.
- Los umbrales de comportamiento son de mercado EE. UU.; para ES/MX se marcan a validar.
- Si un competidor está bajo relación contractual/personal con el cliente, se detiene esa ficha y se avisa.

---

## REFERENCIAS

1. BrightLocal — *Local Consumer Review Survey 2026* (n=1.002, EE. UU.): 31% solo usa negocios 4,5★+; 47% evita <20 reseñas; recencia de 1–2 semanas; Google 71% y IA 45%; media de 6 fuentes. https://www.brightlocal.com/research/local-consumer-review-survey/
2. BrightLocal — *Local Consumer Review Survey 2025* (n=1.026): >80% espera respuesta a todas las reseñas; consumidores consultan ≥2 sitios. https://www.brightlocal.com/research/local-consumer-review-survey-2025/
3. BrightLocal — *Local Consumer Review Survey 2024*: 59% espera 20–99 reseñas; el consumidor lee el detalle, no solo el "at-a-glance". https://www.brightlocal.com/research/local-consumer-review-survey-2024/

---

## CHANGELOG

- **v1.0.0 · 2026-08-11 · ACORDADO** — Primera versión. 10 capas, umbrales BrightLocal 2026 con fuente, 4 casos, plantilla de una página. Auditoría interna 17/20.

## ROADMAP v1.1

- Validar/sustituir umbrales por datos ES/MX (encuesta local o fuente sectorial).
- Añadir columna de precio/ticket medio observable cuando la fuente lo exponga.
- Variante `-MX` con plataformas locales (Google, TripAdvisor MX, Didi Food/Rappi).

---

**Autónomo: funciona sin el historial de la conversación que lo creó.**
