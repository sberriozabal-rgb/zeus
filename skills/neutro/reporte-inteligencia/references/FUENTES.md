# Fuentes externas — reporte-inteligencia

Verificadas el 2026-08-11, revalidadas el 2026-09-15.

## 1 · Comportamiento del consumidor ante las reseñas

**BrightLocal — Local Consumer Review Survey 2026.** Panel representativo de 1.002 adultos de
EE. UU., publicado el 11-02-2026.
<https://www.brightlocal.com/research/local-consumer-review-survey/>

Cifras usadas: **97 %** lee reseñas al evaluar un negocio local; **41 %** las lee siempre (29 %
en 2025); Google cae del **83 % al 71 %** como plataforma de descubrimiento; el consumidor medio
consulta **seis plataformas**; **19 %** espera respuesta el mismo día y **32 %** al día
siguiente.

Es el ancla de las métricas 6, 7 y 8 y del umbral de **< 24 h** de tiempo de respuesta.

**Límite declarado:** es una muestra de consumidores de EE. UU. La dirección del comportamiento
es extrapolable; **las cifras exactas no**.

## 2 · Prohibición de reseñas falsas y de supresión (EE. UU.)

**FTC — Trade Regulation Rule on the Use of Consumer Reviews and Testimonials**, 16 CFR Part 465,
en vigor desde el **21-10-2024**.
<https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials>

Prohíbe comprar o vender reseñas falsas, pagar por reseñas positivas o negativas, las reseñas de
personal interno sin declarar el vínculo y ciertas prácticas de supresión de reseñas negativas.
Sanción civil por infracción conocida: 51.744 USD en 2024, actualizada a **53.088 USD** según los
avisos de la propia FTC de diciembre de 2025.

Es el ancla de la regla NUNCA de no recomendar solicitar, comprar, incentivar ni suprimir
reseñas.

**Límite declarado:** obliga en EE. UU. Fuera, la regla se sostiene igualmente en las políticas
de las plataformas y, en la UE, en la Directiva (UE) 2019/2161 sobre reseñas falsas
`[SIN VERIFICAR en esta sesión]`.

## 3 · La nota como variable de negocio

**Luca, M. (2016).** *Reviews, Reputation, and Revenue: The Case of Yelp.com.* Harvard Business
School NOM Unit Working Paper 12-016.
<https://www.hbs.edu/ris/Publication%20Files/12-016_a7e4a5a2-03f9-490d-b093-8f951238dba2.pdf>

Diseño de regresión discontinua sobre los umbrales de redondeo de Yelp cruzado con datos fiscales
del Estado de Washington: **una estrella más de nota se traduce en un 5-9 % más de ingresos**,
efecto concentrado en establecimientos independientes y **ausente en cadenas**.

Es el ancla de que la nota es una variable de negocio y no de imagen.

**Límite declarado:** es de restaurantes independientes y de la plataforma Yelp. **No se debe
presentar como elasticidad válida para otros sectores.**

## Marcado `[CONVENCIÓN]` — decisiones de esta skill, no datos de fuente

| Convención | Valor |
|---|---|
| Composición del panel | 3 directos + 2 referencia + 1 entrante |
| Congelación del panel | 13 semanas |
| Umbral para declarar patrón | 3 menciones |
| Ventana de lectura | 30 reseñas o 90 días |
| Topes del reporte | 6 hallazgos · 5 fallos · 3 acciones |
| Radio por defecto | 2 km urbano · 15 min en coche fuera · nacional si es digital |

Los umbrales de alerta están en `references/metricas-y-umbrales.md` y son igualmente convención.
