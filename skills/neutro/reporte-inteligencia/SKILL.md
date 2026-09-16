---
name: reporte-inteligencia
description: >-
  Genera el Reporte Semanal de Inteligencia Competitiva a partir del nombre de una marca: arma
  un panel de 6 competidores, captura su reputación digital pública (nota, volumen, velocidad,
  tasa y tiempo de respuesta, elogios y quejas recurrentes con cita y fecha), la compara con
  la marca propia y entrega brecha, qué hacen bien ellos, qué hacemos mal, oportunidades de la
  plaza y 3 acciones de 7 días con dueño y métrica. Úsala para un reporte de inteligencia,
  análisis o monitoreo de competencia, benchmark de reputación o informe semanal de la plaza,
  y cuando pregunten qué hacen los competidores, por qué nos ganan, qué dicen de ellos frente
  a nosotros o quién nos come terreno — aunque no digan "inteligencia" (p. ej. "compárame con
  los seis de mi zona", "el informe de esta semana"). Agnóstica de sector: hostelería, retail,
  clínicas, hoteles, servicios, SaaS, ecommerce. No la uses para responder una reseña
  concreta, auditar la operación interna ni comparar precios de proveedores.
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso comercial sin derecho de redistribución. Ver LICENSE.txt.
metadata:
  version: "1.2.0"
  status: "ACORDADO"
  audit: "19/20 (validar_skill.py, 2026-09-15)"
  author: "Sergio Berriozábal"
  updated: "2026-09-15"
---

# reporte-inteligencia

## Qué hace

Convierte **el nombre de una marca y su plaza** en **un reporte semanal de 10 secciones con
panel congelado de 6 competidores, tabla de brecha en 8 métricas y 3 acciones de 7 días con
dueño y métrica de verificación**, para **quien dirige marca, operación o el negocio entero**.

El coste real está en la captura, no en la redacción, y eso cambia la promesa: en modo BÚSQUEDA
son **~1 h 15 min** pero solo se alcanzan 2 de las 8 métricas; en modo PLATAFORMA son **6-8
horas** y se cierra la línea base. La cifra de 45 minutos que figuraba en la v1.0.x medía solo la
redacción y omitía la captura. Declarar el modo antes de medir es lo que separa este reporte de
una tabla de números redondos con aspecto de medición.

## Cuándo se dispara

- "quiero saber cómo voy contra los de mi zona"
- "qué están haciendo mis competidores que yo no"
- "necesito un informe semanal de reputación"
- "por qué nos están bajando las valoraciones"
- "quién es el líder de mi categoría en la plaza"
- "ha abierto uno nuevo y quiero saber si me afecta"
- "compara mi marca con seis parecidas"
- "qué piden los clientes que nadie está dando"
- jerga del gremio: "panel", "línea base", "benchmark", "competencia", "plaza", "cuota",
  "nota media", "velocidad de reseñas", "tasa de respuesta", "brecha", "delta", "serie",
  "corte semanal", "entrante"

## Quién lo ejecuta

Quien dirige la marca o el negocio, o el analista al que se lo encarga. **1 h 15 min** en modo
BÚSQUEDA —que no cierra línea base y sirve para armar el panel— y **6 a 8 horas** en modo
PLATAFORMA para el primer corte completo. Los cortes siguientes bajan mucho: el panel ya está
congelado y solo se recapturan las métricas.

## Entrada

- **Obligatorio:** el nombre de la marca. Nada más es obligatorio.
- **Recomendado:** ciudad o dirección. Es la **única** pregunta que se hace si el nombre es
  ambiguo, y nunca se hacen más de dos.
- **Recomendado:** la plataforma ancla donde vive la reputación del sector, para no mezclar
  fuentes en la misma serie.
- **Recomendado:** el reporte de la semana anterior, si existe, para reutilizar el panel
  congelado y verificar si las tres acciones movieron la métrica.
- **Dato sucio típico:** la nota o el volumen que vienen de un agregador **sin fecha de captura
  declarada**. Se marca `[FUENTE SIN FECHA]` y **no entra en el cálculo de medianas**. Y cuando
  dos fuentes se contradicen, **se reportan ambas y no se elige**: la discrepancia es el dato.
  El segundo dato sucio es el competidor con menos de 10 reseñas totales, que se marca
  `[MUESTRA INSUFICIENTE]` y sale de las medianas del panel, no del reporte.

## Umbral que sostiene el producto

**El panel congelado 13 semanas con composición fija 3+2+1.** Tres directos (misma categoría,
ticket ±25 %, dentro del radio), dos de referencia (líder de la plaza o marca aspiracional) y un
entrante (abierto o relanzado en 12 meses). Cambiar de competidores a mitad de trimestre
convierte **todos los deltas en ruido**, y los dos cupos de referencia son obligatorios
precisamente porque van por delante: si el panel no incomoda, está mal armado.

El segundo umbral es el **modo de captura**, y es bloqueante: BÚSQUEDA alcanza solo las métricas
1 y 2 y se emite con `ESTADO_LINEA_BASE: ABIERTA`; PLATAFORMA alcanza las 8 y sí cierra línea
base. **Nunca se mezclan modos en la misma serie.**

Las anclas externas, verificadas:

- **97 % lee reseñas** al evaluar un negocio local y **41 % las lee siempre** (29 % en 2025);
  Google cae del 83 % al 71 % como plataforma de descubrimiento y el consumidor medio consulta
  **seis plataformas**; **19 % espera respuesta el mismo día** y 32 % al día siguiente, de donde
  sale el umbral de **< 24 h**. (BrightLocal, *Local Consumer Review Survey 2026*, panel de
  1.002 adultos de EE. UU., 11-02-2026,
  <https://www.brightlocal.com/research/local-consumer-review-survey/>.) **Límite: es EE. UU.;
  la dirección del comportamiento es extrapolable, las cifras exactas no.**
- **Una estrella más de nota se traduce en un 5-9 % más de ingresos**, efecto concentrado en
  establecimientos independientes y **ausente en cadenas** (Luca, HBS 12-016,
  <https://www.hbs.edu/ris/Publication%20Files/12-016_a7e4a5a2-03f9-490d-b093-8f951238dba2.pdf>).
  **Límite: es Yelp y son restaurantes independientes; no se presenta como elasticidad válida
  para otros sectores.**
- Comprar, vender o suprimir reseñas está **prohibido por norma en EE. UU. desde el
  21-10-2024**, con sanción civil por infracción conocida (FTC, 16 CFR Part 465,
  <https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials>).

`[CONVENCIÓN]` de esta skill, no dato de fuente: la composición 3+2+1, las 13 semanas de
congelación, el umbral de **3 menciones** para declarar patrón, la ventana de 30 reseñas o 90
días, y los topes de 6 hallazgos, 5 fallos y 3 acciones.

## Procedimiento

1. **Entrada: el nombre de la marca → Acción: identificar categoría, plaza y radio desde fuentes
   públicas, fijar la semana (lunes-domingo cerrado) y armar el panel de 6 con la composición
   3+2+1, congelándolo 13 semanas → Salida: ficha de panel con nombre, perfil, distancia y
   motivo de entrada en una línea → Si falta el dato: si el nombre es ambiguo se pregunta **una
   sola cosa**, ciudad o dirección; radio por defecto 2 km urbano, 15 min en coche fuera, y
   nacional si el negocio es digital, siempre declarado en cabecera.**

2. **Entrada: el panel armado → Acción: declarar el MODO DE CAPTURA en la cabecera **antes** de
   capturar nada, BÚSQUEDA o PLATAFORMA → Salida: modo declarado y, si es BÚSQUEDA, la
   advertencia de método y `ESTADO_LINEA_BASE: ABIERTA` → Si se cambia de modo a mitad de
   trimestre: se rompe la serie igual que cambiando el panel, así que no se hace.**

3. **Entrada: las 7 fichas (panel de 6 más la marca propia) → Acción: capturar de fuentes
   públicas las 8 métricas del cuadro, leyendo antes `references/metricas-y-umbrales.md` →
   Salida: tabla de 7 filas × 8 columnas con fecha y hora de captura → Si falta el dato: celda
   `[NO DISPONIBLE]` con su motivo, y **nunca se estima una métrica ausente**.**

4. **Entrada: las reseñas del panel → Acción: leer lo cualitativo y extraer patrones de elogio y
   de queja, cada uno con cita textual de menos de 15 palabras, con fecha y plataforma → Salida:
   patrones citados y recuperables → Si un patrón tiene menos de 3 menciones: es anécdota y no
   sube a patrón.**

5. **Entrada: la tabla de métricas → Acción: construir la brecha en tres columnas —nosotros,
   mediana del panel, mejor del panel— con delta y semáforo por métrica → Salida: las 8 métricas
   con posición de 1.º a 7.º y las tres peor situadas → Si el panel tiene fichas con muestra
   insuficiente: salen de la mediana pero no del reporte, y se declara.**

6. **Entrada: brecha y patrones → Acción: escribir máximo 6 hallazgos de lo que ellos hacen bien
   (cada uno con evidencia citada y clasificación de replicabilidad) y máximo 5 fallos propios
   ordenados por frecuencia × impacto, **en el lenguaje del cliente y no en el interno** →
   Salida: 6 hallazgos y 5 fallos con su cita → Si un hallazgo es `ESTRUCTURAL`: no puede
   originar ninguna acción de 7 días.**

7. **Entrada: hallazgos, fallos y huecos de la plaza → Acción: identificar de 2 a 4
   oportunidades —lo que piden los clientes que ningún competidor resuelve— y cerrar con
   exactamente 3 acciones de 7 días (acción, dueño por puesto, coste y métrica de verificación
   con número y fecha) más 2 movimientos de trimestre → Salida: tabla de 3 filas y 2 movimientos
   → Si solo hay una oportunidad real: se entrega una; cero relleno.**

8. **Entrada: todo lo anterior → Acción: montar el semáforo de 5 indicadores, listar las alertas
   activas y verificar las tres acciones del reporte anterior como hecha / no hecha / movió la
   métrica, emitiendo con `assets/plantilla-reporte.md` → Salida: reporte de 10 secciones con
   cabecera de semana, panel, radio, modo y fecha de captura → Si es el primer corte: la
   cabecera lleva `[PRIMER CORTE — LÍNEA BASE]` y no hay deltas que mostrar.**

## Salida

```markdown
# Reporte de inteligencia — [Marca] · Semana [n]
Panel congelado hasta: [fecha] · Radio: [n] · MODO: [BÚSQUEDA|PLATAFORMA]
Captura: [fecha y hora] · ESTADO_LINEA_BASE: [ABIERTA|CERRADA]

## 1. Resumen  ## 2. Panel  ## 3. Reputación (7×8)  ## 4. Brecha
## 5. Qué hacen bien ellos (máx. 6)   ## 6. Qué hacemos mal (máx. 5)
## 7. Oportunidades (2-4)             ## 8. Acciones de 7 días (exactamente 3)
| Acción | Dueño (puesto) | Coste | Métrica de verificación + fecha |
## 9. Movimientos de trimestre (2)    ## 10. Semáforo y alertas

## Supuestos de esta versión
[radio asumido, celdas NO DISPONIBLE, fuentes sin fecha, muestras insuficientes]
```

Las 8 métricas del paso 3, y por qué está cada una:

| # | Métrica | Por qué está |
|---|---|---|
| 1 | Nota media global | Punto de partida, pero se mueve lento |
| 2 | Volumen total de reseñas | Mide masa y antigüedad de la reputación |
| 3 | Velocidad (nuevas/semana, media 4 sem.) | Mide tracción actual |
| 4 | Nota reciente (media de las últimas 20) | Detecta la deriva 3-6 meses antes que la global |
| 5 | % de 1-2★ sobre las últimas 50 | Mide el daño vivo, no el histórico |
| 6 | Tasa de respuesta del propietario (últimas 50) | Se ve desde fuera y pesa en la percepción |
| 7 | Tiempo mediano de respuesta | La expectativa del mercado es < 24 h |
| 8 | Frescura (% de reseñas de los últimos 30 días) | Un perfil sin reseñas recientes se lee como negocio apagado |

## Límites

- **El modo BÚSQUEDA no cierra una línea base.** Alcanza 2 de 8 métricas y se emite siempre con
  `ESTADO_LINEA_BASE: ABIERTA`.
- No usa datos obtenidos saltándose términos de uso ni muros de acceso: el reporte se sostiene
  sobre lo que cualquiera puede ver.
- No identifica ni nombra a ningún reseñador. Analiza patrones, no personas.
- **No recomienda solicitar, comprar, incentivar ni suprimir reseñas**, ni propias ni del
  competidor: está prohibido por norma en EE. UU. y por política de plataforma en todos los
  mercados.
- Las cifras de BrightLocal son de consumidores de EE. UU. y la elasticidad de Luca es de
  restaurantes independientes en Yelp: la dirección es extrapolable, las cifras exactas no.
- No sustituye la respuesta a reseñas ni el plan de marketing: produce la evidencia y el bloque
  `HANDOFF` para quien haga eso.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Citar textualmente en menos de 15 palabras, con fecha y plataforma, cada patrón | Sin evidencia recuperable, quien lee no puede comprobarlo y deja de confiar en la serie entera |
| Congelar el panel 13 semanas | Cambiar de competidores a mitad de trimestre convierte todos los deltas en ruido |
| Declarar fecha y hora de captura en la cabecera | Una nota media de hace tres semanas presentada como actual es un dato falso con formato de dato verdadero |
| Marcar `[NO DISPONIBLE]` la métrica que no se pudo capturar | Un hueco declarado se cubre la semana siguiente; una estimación inventada contamina la serie para siempre |
| Separar hecho, inferencia y criterio con `[DATO]`, `[INFERENCIA]` y `[CRITERIO]` | Quien decide necesita saber qué está comprobado y qué es juicio del analista |
| Dar a toda recomendación su métrica de verificación con número y fecha | Sin ella no es una recomendación, es una opinión con formato de tabla |
| Escribir los fallos propios con las palabras del cliente | El lenguaje interno permite negar el problema; la cita del cliente, no |
| Comparar contra la mediana del panel, nunca contra la media | Un competidor con 4.000 reseñas distorsiona la media y hace parecer normal lo que no lo es |
| Declarar el modo de captura en la cabecera | Una tabla levantada por búsqueda y otra en plataforma no son la misma medición |
| Reportar ambas fuentes cuando se contradicen, sin elegir | La discrepancia **es** el dato, y elegir en silencio oculta el único hallazgo real de esa celda |

| NUNCA | Porqué |
|---|---|
| Usar datos obtenidos saltándose términos de uso o muros de acceso | Un dato ilegítimo es un pasivo legal dentro de un documento interno |
| Inventar una nota, un volumen o una cita | Un solo dato fabricado invalida el reporte completo y el lector no puede saber cuál era |
| Recomendar solicitar, comprar, incentivar o suprimir reseñas | Prohibido por norma en EE. UU. desde el 21-10-2024 con sanción civil, y por política de plataforma en todos los mercados |
| Convertir una reseña aislada en un patrón | Menos de 3 menciones es anécdota, y construir sobre ella hace perseguir fantasmas al equipo |
| Recomendar copiar un hallazgo clasificado `ESTRUCTURAL` | Pedir que se replique una ubicación o un capital que no se tiene quema credibilidad y presupuesto |
| Mencionar o identificar a un reseñador por su nombre | El reporte analiza patrones, no personas, y un documento interno con nombres es un problema de datos personales |
| Entregar más de 6 hallazgos, 5 fallos y 3 acciones | Un reporte semanal con veinte prioridades no tiene ninguna, y a la tercera semana nadie lo abre |
| Declarar cerrada una línea base levantada en modo BÚSQUEDA | Cinco de las ocho métricas serían huecos presentados como medición, y los deltas se calcularían contra un vacío |
| Mezclar modos de captura dentro de la misma serie | Rompe los deltas exactamente igual que cambiar el panel o la plataforma ancla a mitad de trimestre |

## Antipatrones

1. **Síntoma**: la tabla de reputación tiene las columnas 3 a 8 vacías o rellenas de números redondos, y la cabecera no dice cómo se capturó. `[OBSERVADO 2026-08-16]` **Causa raíz**: se levantó el reporte con buscador porque es veinte veces más rápido, y se presentó como medición. **Corrección**: el paso 2 obliga a declarar el modo antes de capturar; en modo BÚSQUEDA, `ESTADO_LINEA_BASE: ABIERTA` y las tres acciones se orientan a construir la captura en plataforma. *Procedencia: detectado en la ejecución real de la Semana 0 de una taquería de CDMX el 2026-08-16. Es el primer antipatrón de esta skill observado, no derivado.*

2. **Síntoma**: los seis competidores tienen todos nota inferior a la de la marca propia, o el reporte de la semana 6 tiene dos competidores que no estaban en el de la semana 5 sin nota que lo explique. `[DERIVADO]` **Causa raíz**: el panel se eligió para quedar bien en vez de para aprender, o se rehízo desde cero en lugar de reutilizar el congelado. **Corrección**: los dos cupos de referencia del paso 1 son obligatorios y por definición van por delante —si el panel no incomoda, está mal armado—, y el panel se copia del reporte anterior: cualquier cambio va con motivo escrito y se aplica en el corte trimestral.

3. **Síntoma**: el reporte abre y cierra con la nota global y no hay ninguna cita textual en todo el documento. `[DERIVADO]` **Causa raíz**: se capturó la métrica fácil y se saltó la lectura cualitativa, que es donde está el trabajo. **Corrección**: la nota media es la métrica 1 de 8 y no puede ocupar más de una línea del resumen; sin quejas y elogios citados, el reporte no se emite.

4. **Síntoma**: una recomendación se apoya en una única reseña. `[DERIVADO]` **Causa raíz**: la reseña era vívida y se saltó el umbral de 3 menciones. **Corrección**: trazar cada recomendación hasta su patrón y contar las menciones antes de escribirla.

5. **Síntoma**: una acción de 7 días exige terraza, segundo turno o un equipo que no existe. `[DERIVADO]` **Causa raíz**: el hallazgo no se clasificó por replicabilidad, o se clasificó mal. **Corrección**: ninguna acción de 7 días puede venir de un hallazgo `90 DÍAS` o `ESTRUCTURAL`; se comprueba el origen de cada fila antes de emitir.

## Casos de prueba

Los cuatro casos están en `cases/`, con entrada y salida reales.

**Happy path** (`cases/case_01_happy_path.md`): marca con plaza clara y panel completo en el
radio. Primer corte con cabecera `[PRIMER CORTE — LÍNEA BASE]`, tabla 7×8 y las tres acciones
con su métrica de verificación.

**Edge case** (`cases/case_02_edge_case.md`): marca con dos locales a 900 m y panel solapado en
4 de 6. Salen **dos reportes**, uno por unidad, y se declara que los deltas de los solapados no
se suman.

**Failure** (`cases/case_03_failure.md`): clínica dental con perfil sin reclamar, 6 reseñas y sin
presencia en otras plataformas. **El reporte se emite igual**, con las celdas propias en
`[NO DISPONIBLE]` y las tres acciones orientadas a construir la línea base.

**Integration** (`cases/case_04_integration.md`): encadenado con `respuesta-resenas`. El bloque
`HANDOFF` entrega los 5 fallos propios en lista plana con eje y frecuencia, listos para consumir.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.2.0 — ver `CHANGELOG.md`.
