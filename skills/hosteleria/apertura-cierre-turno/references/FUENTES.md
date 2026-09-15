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
  **en corrección centralizada por la casa a fecha 15-ago-2026.** La atribución
  actual está en revisión y no se toca desde esta ficha. Hasta que cierre esa
  corrección, ninguna de esas cifras se usa en material de venta.
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
