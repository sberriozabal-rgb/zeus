# Fuentes externas verificadas — receta-estandar

Verificadas contra el documento primario el 15-ago-2026. Cada entrada declara
**la afirmación concreta de la skill que sostiene**. Una fuente que no sostiene
ninguna afirmación no está en esta lista.

Esta skill toca seguridad alimentaria. La regla es más dura que en el resto del
catálogo: **una temperatura o un tiempo que no se pueda anclar a norma o a
informe de autoridad competente va marcado `[A VALIDAR]`**, aunque parezca
obvio y aunque un blog lo repita. Un número inventado en una ficha de cocina no
es un error de redacción.

---

## 1 · AESAN — Informe del Comité Científico AESAN-2021-004 (España)

*Combinaciones tiempo-temperatura necesarias para el cocinado seguro de los
alimentos y temperaturas adecuadas para el mantenimiento en caliente y el
recalentamiento de las comidas preparadas.* Aprobado 17-feb-2021.

<https://www.aesan.gob.es/AECOSAN/docs/documentos/seguridad_alimentaria/evaluacion_riesgos/informes_comite/TIEMPO-TEMPERATURA.pdf>

**Cifras verificadas en el documento:** carne 70 °C/1 s · aves 74 °C/1 s ·
pescado 68 °C/15 s · pescado relleno 74 °C/15 s · moluscos bivalvos crudos
90 °C/90 s · huevo consumo no inmediato 70 °C/2 s · huevo consumo inmediato
63 °C/20 s · vegetales 70 °C/2 min · mantenimiento en caliente ≥63 °C ·
recalentamiento ≥74 °C/15 s.

**Qué sostiene:** la **tabla A** de `temperaturas_haccp.md` completa, el paso P6
del procedimiento, la regla SIEMPRE de temperatura numérica en proteína animal,
y el criterio de que el umbral es un **binomio tiempo-temperatura**, no un solo
número — que es lo que distingue una ficha española bien escrita de una copia de
una tabla americana.

**Ámbito:** España. Autoridad competente, documento primario.

---

## 2 · NOM-251-SSA1-2009 (México) — texto publicado en el DOF

*Prácticas de higiene para el proceso de alimentos, bebidas o suplementos
alimenticios.*

<https://dof.gob.mx/normasOficiales/3980/salud/salud.htm>

**Cifras verificadas con su apartado:** §7.3.1 cocción — pescado, trozos de res y
huevo con cascarón roto **63 °C**; cerdo en trozo, carnes molidas, carnes
inyectadas y huevo roto para buffet **68 °C**; aves, emulsiones de pescado y
alimentos rellenos **74 °C**. §7.3.2 recalentamiento **≥74 °C**. §7.3.3
mantenimiento: calientes **>60 °C**, fríos **≤7 °C**. §5.5.2 equipos de
refrigeración **máx. 7 °C**. §7.4.2 recepción de pescados y mariscos: frescos
máx. **4 °C**, congelados máx. **9 °C**, vivos **7 °C**.

**Qué sostiene:** la **tabla B** de `temperaturas_haccp.md`, el bloque de
conservación y servicio de la ficha, y la regla de declarar el país en la
cabecera. Es la fuente que un cliente mexicano puede oponer a una verificación
de COFEPRIS; la referencia británica de la v1.0.0 no lo era.

**Ámbito:** México. Norma oficial, texto publicado.

---

## 3 · Reglamento (CE) nº 852/2004, artículo 5 — higiene de los productos alimenticios

<https://www.boe.es/buscar/doc.php?id=DOUE-L-2004-81035>

**Texto verificado (art. 5.1):** los operadores de empresa alimentaria deberán
*"crear, aplicar y mantener un procedimiento o procedimientos permanentes basados
en los principios del APPCC"*. El art. 5.2 enumera los siete principios, incluida
la documentación y el registro.

**Qué sostiene:** el límite declarado en `SKILL.md` → **una ficha de receta
estándar no es un plan APPCC y no satisface el artículo 5**. Marcar un punto
crítico en una receta es una buena práctica de higiene documentada, no el sistema
de autocontrol que la ley exige al titular. Esta fuente es la razón por la que
ese límite existe.

Complemento sobre flexibilidad para negocios pequeños (AESAN): las Buenas
Prácticas de Higiene *"se pueden considerar suficientes para controlar los
peligros"* en determinados establecimientos, pero *"siempre se deben identificar
los peligros"* — y esa identificación no la hace esta skill.
<https://www.aesan.gob.es/AECOSAN/web/seguridad_alimentaria/ampliacion/flexibilidad_appcc.htm>

**Ámbito:** Unión Europea / España.

---

## 4 · Pennsylvania State University — *Introduction to Food Production and Service*, cap. 6: Standardized Recipes

<https://psu.pb.unizin.org/hmd329/chapter/chapter-6-standardized-recipes/>

**Verificado en la página:** enumera los componentes obligatorios de una receta
estándar — *menu item name · total yield · portion size · ingredient
list/quantity · preparation procedures · cooking temperatures and times,
including HACCP critical control points · special instructions · mise en place ·
service instructions, including hot/cold storage · plating/garnishing* — y el
principio **S.A.M.E.** (*Standardization Always Meets Expectations*). Afirma que
la receta estándar asegura *"not only consistent quality and quantity, but also a
reliable cost range"*.

**Qué sostiene:** **los 10 campos obligatorios** del paso P2 y de la sección
`## Entrada`. La lista de la skill es esa lista, no una invención de la casa. Es
la fuente que permite responder a un chef que pregunte por qué son diez y no
siete.

**Ámbito:** académico, EE. UU. Aplicable porque es estructura documental, no
normativa sanitaria.

---

## 5 · ProChefDesk — *Standardized Recipes: The Cheapest Consistency You Will Ever Buy*

<https://prochefdesk.com/blog/standardized-recipe-guide>

**Qué sostiene, y solo eso:** la estimación de **20-40 minutos de trabajo por
receta** que aparece en `## Qué hace`, y la descripción cualitativa de los
antipatrones de deriva de food cost y de fallo de escalado en eventos.

**Aviso de calidad de fuente:** es un blog sectorial, fuente única, no revisada.
La cifra de 20-40 min va marcada `[A VALIDAR]` en la skill. La afirmación del
artículo original sobre "30 % de pérdida de detalle en la transmisión verbal"
**no se reproduce** en ninguna parte de esta skill: es una ilustración de blog
sin estudio detrás y sería una cifra huérfana en material de venta.

---

## 6 · Codex Alimentarius CXC 1-1969 rev. 2020 — *General Principles of Food Hygiene*

Marco internacional de los principios APPCC.

**Qué sostiene:** el vocabulario de "punto crítico de control" usado en P6 y en
la ficha. **Qué NO sostiene, y conviene tenerlo claro:** el Codex **no** publica
una tabla universal de temperaturas internas de cocinado. No sirve para rellenar
un hueco de la tabla de temperaturas cuando el país no es España ni México — ese
hueco se marca `[A VALIDAR]` y se resuelve con la autoridad local.

---

## 7 · Real Decreto 3484/2000, de 29 de diciembre — normas de higiene para comidas preparadas (España)

Norma **reglamentaria** vigente en España, publicada en el BOE. A diferencia del informe
AESAN-2021-004 (fuente 1), que es una opinión científica, este Real Decreto es la norma que
aplica la inspección.

<https://www.boe.es/buscar/doc.php?id=BOE-A-2001-809>

**Cifras verificadas en el artículo 7** (temperaturas de almacenamiento, conservación,
transporte y venta de comidas preparadas):

| Comida preparada | Temperatura |
|---|---|
| Congelada | **≤ −18 °C** |
| Refrigerada, con periodo de duración **inferior a 24 h** | **≤ 8 °C** |
| Refrigerada, con periodo de duración **superior a 24 h** | **≤ 4 °C** |
| Caliente | **≥ 65 °C** |

**Qué sostiene:**
- La **conservación en frío** de la ficha para España, que hasta la v1.1.0 no tenía ancla y
  figuraba en `cases/case_01` como "práctica de oficio; ver nota de región" — nota que no
  existía. El umbral de 24 h que separa ≤8 °C de ≤4 °C es exactamente el que la ficha usa para
  la vida útil del porcionado.
- El **mantenimiento en caliente para España**, donde **discrepa con AESAN**: el informe dice
  ≥63 °C y el Real Decreto dice **≥65 °C**. Ante inspección prevalece el reglamento. Desde la
  v1.1.1 las fichas españolas usan **≥65 °C** y la discrepancia está declarada en
  `temperaturas_haccp.md`.

**Qué NO sostiene:** temperaturas de **cocinado**. El artículo 7 regula conservación y servicio;
los binomios de cocción (pescado 68 °C/15 s, aves 74 °C/1 s, etc.) siguen siendo de AESAN-2021-004.

**Ámbito:** España. Norma reglamentaria, documento primario en BOE. Consultado: 2026-09-15.

---

## Equivalencias de cocina — sin fuente citable, y declarado

`references/equivalencias_cocina.md` (taza = 240 ml, puñado de hierbas = 8-12 g,
etc.) es **conocimiento de oficio de uso extendido, no normado por ninguna
autoridad** y sin publicación única citable. Va marcado como tal dentro del propio
archivo y toda cifra que salga de ahí llega a la ficha con
`[CANTIDAD ESTIMADA — VERIFICAR CON PESAJE]`. Se mantiene porque es útil como
respaldo mientras no se ha pesado, no porque sea una autoridad.

---

## Debate documentado del oficio — cantidad exacta vs. rango con criterio

Una posición sostiene que la receta estándar debe fijar cantidades exactas sin
excepción, porque cualquier margen de "criterio" reintroduce la variabilidad que
la estandarización busca eliminar. La opuesta sostiene que ciertos ajustes (sal
final, punto de acidez) dependen de variables no controlables por receta —
madurez de un cítrico, salinidad de un lote — y que forzar un número fijo ahí
produce platos peores.

**Cómo lo resuelve esta skill (P3):** cantidad numérica siempre, declarada como
rango con punto de partida cuando el ingrediente es intrínsecamente variable. No
elimina el criterio del cocinero: lo acota. Un rango con ancla se puede costear;
un "al gusto" no.
