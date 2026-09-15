# Fuentes externas verificadas — apertura-cierre-turno

Verificadas contra el documento primario el 15-ago-2026. Cada entrada declara
**la afirmación concreta de la skill que sostiene**. Una fuente que no sostiene
ninguna afirmación no está en esta lista.

Regla de la casa: si una cifra no se puede anclar a una de estas fuentes, va
marcada `[A VALIDAR]` en el punto donde se usa. No se rellena con un número
plausible.

---

## 1 · Reglamento (CE) nº 852/2004, artículo 5 — higiene de los productos alimenticios

<https://www.boe.es/buscar/doc.php?id=DOUE-L-2004-81035>

**Texto verificado (art. 5.1):** los operadores de empresa alimentaria deberán
*"crear, aplicar y mantener un procedimiento o procedimientos permanentes
basados en los principios del APPCC"*. El art. 5.2 enumera los siete
principios, incluida la documentación y el registro.

**Qué afirmación sostiene:**
- El límite declarado en `SKILL.md` → *"No es un plan de higiene alimentaria
  (APPCC/HACCP) certificado"*. La obligación del art. 5 es del titular del
  negocio y no se satisface con un checklist operativo. Esta fuente es la razón
  por la que el límite existe, no una formalidad.
- La regla SIEMPRE *"Marcar toda tarea de normativa sanitaria como referencia de
  control, no de certificación"*.

**Ámbito:** Unión Europea (aplica en España). En México el equivalente funcional
es la NOM-251 (fuente 4).

---

## 2 · AESAN — Flexibilidad en la aplicación del APPCC

<https://www.aesan.gob.es/AECOSAN/web/seguridad_alimentaria/ampliacion/flexibilidad_appcc.htm>

**Texto verificado:** en determinados establecimientos, las Buenas Prácticas de
Higiene y de Fabricación *"se pueden considerar suficientes para controlar los
peligros y garantizar la seguridad de los alimentos"*; la Comisión Europea
aprobó un *"enfoque simplificado"* para el pequeño comercio minorista. Lo que
**no** es flexible: *"siempre se deben identificar los peligros que afectan al
proceso de producción de alimentos"*.

**Qué afirmación sostiene:**
- Por qué un checklist de apertura/cierre tiene valor real y no es papeleo
  decorativo: en un local pequeño, las BPH documentadas son la mayor parte de lo
  que la autoridad espera ver. El checklist es el soporte de esas BPH.
- Y a la vez por qué **no basta**: la identificación de peligros sigue siendo
  obligatoria y no la hace esta skill. Es exactamente la frontera del límite
  declarado.

**Ámbito:** España.

---

## 3 · AESAN — Informe del Comité Científico AESAN-2021-004, combinaciones tiempo-temperatura

<https://www.aesan.gob.es/AECOSAN/docs/documentos/seguridad_alimentaria/evaluacion_riesgos/informes_comite/TIEMPO-TEMPERATURA.pdf>

**Cifras verificadas en el documento (aprobado 17-feb-2021):** mantenimiento en
caliente **≥63 °C**; recalentamiento **≥74 °C durante al menos 15 segundos** en
el centro del producto; cocinado de carne 70 °C/1 s, aves 74 °C/1 s, pescado
68 °C/15 s.

**Qué afirmación sostiene:**
- El criterio de "hecho" de las tareas de temperatura en
  `references/tareas-maestras.md` (bloques de apertura y cierre): un criterio de
  temperatura con cifra es verificable; *"revisar que esté caliente"* no lo es.
- El umbral de 63 °C para las tareas de mantenimiento en caliente de un local
  con buffet, vitrina o línea de pase, cuando el cliente las pide.

**Ámbito:** España. Cifra oficial de la autoridad competente, no de un blog.

---

## 4 · NOM-251-SSA1-2009 — Prácticas de higiene para el proceso de alimentos, bebidas o suplementos alimenticios (México)

<https://dof.gob.mx/normasOficiales/3980/salud/salud.htm>

**Cifras verificadas contra el texto publicado en el DOF:**
- §5.5.2 — equipos de refrigeración: temperatura máxima **7 °C**.
- §7.3.3 — alimentos calientes: **>60 °C**; alimentos fríos: **≤7 °C**.
- §7.3.2 — recalentamiento: **≥74 °C**.
- §7.4.2 — recepción de pescados y mariscos frescos: máximo **4 °C**;
  congelados máximo **9 °C**; producto vivo **7 °C**.

**Qué afirmación sostiene:**
- La tarea de apertura *"Temperatura de cámaras registrada"* y la de cierre
  equivalente, cuando el local opera en México.
- La tarea *"Recepción de género del día verificada"* de la plantilla nº4
  (cocina de producto): la NOM da la cifra exacta de recepción de pescado, que
  es la que un encargado mexicano puede defender ante verificación de COFEPRIS.

**Aviso de región, importante:** el rango **0-4 °C** que usa
`tareas-maestras.md` como criterio de frío positivo es **práctica de oficio
conservadora**, no el máximo legal de ningún país concreto. En México el máximo
normado es 7 °C (§5.5.2). En España, tras el RD 1021/2022, no existe una cifra
única genérica para todo alimento refrigerado y rige la del fabricante o la
específica de cada producto. Al instalar en un cliente: se usa el rango de
oficio como criterio operativo interno **y** se cita la cifra normada del país
como mínimo legal. Nunca al revés.

---

## Cifras de esta skill que NO tienen fuente en esta lista

- **Coste y tasa de rotación de personal** (sección `## Umbral que sostiene el
  producto` de `SKILL.md` y constantes de `scripts/coste_rotacion.py`):
  ✅ **ATRIBUCIÓN CERRADA el 15-sep-2026.** Las cuatro cifras quedan ancladas a
  las fuentes 5, 6 y 7 de esta lista, cada una con autor nombrado, año y URL
  recuperable. **Ya se pueden usar en material de venta**, siempre citando a su
  autor y su límite. Lo que sigue faltando en las tres fuentes es el **tamaño de
  muestra publicado**, así que ninguna se presenta como dato oficial: van con la
  marca `[SIN TAMAÑO DE MUESTRA PUBLICADO]` y con el nombre de quien las publica.
- **Rango de reducción de errores por onboarding (15-30 %)**: ya marcado
  `[A VALIDAR]` dentro del propio script, sin estudio público que aísle la
  variable. Se mantiene como rango declarado, no como promesa.
- **Longitudes de checklist (12-20 apertura, 10-18 cierre, 6-10 cambio de
  turno)**: criterio de oficio de la casa (20 años de sala y cocina), no cifra
  publicada. `[A VALIDAR]` en el sentido de que no procede de fuente externa;
  se sostiene por criterio profesional declarado, que es lo que el comprador
  está pagando.
- **"Una lista repartida y no auditada deja de ejecutarse en unos diez días"**:
  criterio de oficio, no dato medido. `[A VALIDAR]`.

---

## 5 · Synergie España — *La situación del empleo en el sector Hospitality en España 2026*

<https://www.revistahosteleria.com/texto-diario/mostrar/5860927/tasa-rotacion-638-puestos-cubrir-obligan-reinventar-seleccion-personal>

**Dato verificado:** tasa de rotación laboral del **63,8 %** en el sector hospitality español, la
más alta de toda la economía del país. Contexto del mismo informe: la hostelería emplea al 8,6 %
de los trabajadores en España (más de 1,7 millones de personas), y el salario medio del subsector
se queda en 1.512 € frente a los 2.345 € de media nacional.

**Qué afirmación sostiene:**
- La cifra de rotación de `## Umbral que sostiene el producto` en `SKILL.md`.
- La constante `TASA_ROTACION_SECTORIAL = 0.638` de `scripts/coste_rotacion.py`.
- El argumento de asignar las tareas **al puesto y no al nombre**: con dos de cada tres empleados
  cambiando de trabajo en un año, una lista atada a una persona caduca pronto.

**Límite declarado:** es el informe de una **empresa de trabajo temporal**, no una estadística
oficial del INE. Autor y año están nombrados y el dato es recuperable, pero **no se ha localizado
el tamaño de muestra ni la metodología publicada**. Se cita siempre como *"según el informe de
Synergie España 2026"*, nunca como dato oficial. `[SIN TAMAÑO DE MUESTRA PUBLICADO]`

**Ámbito:** España. Consultado: 2026-09-15.

---

## 6 · Linkers — coste de sustitución de una persona en sala o cocina

<https://www.hosteleriasalamanca.es/noticias-hosteleria/abril-2026/hosteleria-espanola-crece-pierde-talento>

**Dato verificado:** sustituir a un empleado de cocina o sala cuesta de media **entre 2.800 y
5.000 €**, sumando tiempo de selección, formación del nuevo incorporado y caída temporal de la
productividad del equipo.

**Qué afirmación sostiene:**
- El rango de coste de reposición de `## Umbral que sostiene el producto`.
- Las constantes `COSTE_REPOSICION_EUR` del script (2.800 € sala, 5.000 € encargado).

**Límite declarado:** es el análisis de una **consultora de recursos humanos del sector**, no un
estudio académico ni oficial. Autor nombrado y dato recuperable, pero **sin metodología ni tamaño
de muestra publicados**. Se cita como *"según el análisis de Linkers"*.
`[SIN TAMAÑO DE MUESTRA PUBLICADO]`

**Ámbito:** España. Consultado: 2026-09-15.

---

## 7 · CANIRAC — rotación y coste de vacante en la industria restaurantera mexicana

<https://www.jornada.com.mx/noticia/2024/02/21/economia/falta-de-personal-en-restaurantes-eleva-costos-canirac-7205>
· <https://portal.canirac.org.mx/noticias/el-reto-del-talento-en-la-industria-restaurantera-de-la-rotacion-a-la-solucion/>

**Datos verificados**, declarados por la Cámara Nacional de la Industria de Restaurantes y
Alimentos Condimentados y recogidos por prensa nacional:

- Tasa de rotación del sector restaurantero de **entre el 80 % y el 120 % anual**, con segmentos
  que alcanzan el 180 %.
- Una vacante cuesta **de dos a tres veces el salario del puesto**, por la inversión en búsqueda,
  selección y capacitación del nuevo integrante.
- Contexto de permanencia del mismo cuerpo de datos: alrededor del 75 % de los cocineros deja su
  empleo antes de los cinco meses; a los 14 meses queda un 10 % de los meseros.

**Qué afirmación sostiene:**
- Las cifras de México de `## Umbral que sostiene el producto`.
- Las constantes `TASA_ROTACION_SECTORIAL_MX = 1.00` (punto medio del rango declarado) y
  `MULTIPLICADOR_SALARIO_MX = (2, 3)` del script.

**Límite declarado:** es la **declaración de la cámara del sector**, relayada por prensa, no un
estudio con metodología publicada. La horquilla 80-120 % es ancha por sí misma y el script usa su
punto medio, lo que **se declara en la salida**. `[SIN TAMAÑO DE MUESTRA PUBLICADO]`

**Ámbito:** México. Consultado: 2026-09-15.
