# CHANGELOG — apertura-cierre-turno

## [1.1.2] — 2026-09-15

**Atribución del umbral CERRADA**, y tres defectos de distribución que el validador destapó al
revisarla.

### Atribución — el motivo de esta versión

Desde el 15-ago-2026 las cuatro cifras de rotación estaban "en corrección centralizada" y la
skill llevaba el aviso de **no usarlas en material de venta**. Quedan ancladas:

| Cifra | Autor | Fuente |
|---|---|---|
| Rotación España **63,8 %** | **Synergie España** | *La situación del empleo en el sector Hospitality en España 2026* |
| Sustitución **2.800–5.000 €** | **Linkers** | análisis de la consultora, abr-2026 |
| Rotación México **80–120 %** | **CANIRAC** | vía La Jornada, 21-feb-2024, y portal propio |
| Vacante México **2–3× salario** | **CANIRAC** | misma fuente |

Las tres fuentes entran como #5, #6 y #7 de `references/FUENTES.md`, cada una con su URL, la
afirmación concreta que sostiene y su límite.

**Lo que sigue faltando, y se declara:** ninguna publica tamaño de muestra ni metodología. Dos
vienen de empresas del sector y una de la cámara patronal. Así que las cifras **se pueden usar
en venta pero siempre con el nombre de quien las publica**, marcadas
`[SIN TAMAÑO DE MUESTRA PUBLICADO]` y nunca como dato oficial. No son INE.

Las URLs van ahora **dentro de la sección del umbral**, no solo en el fichero de fuentes: la cifra
lleva su enlace donde se usa.

### Tres defectos corregidos

1. **`allowed-tools: []` rompía el empaquetado.** La especificación exige una cadena separada por
   espacios, no una lista, y el validador lo marca como error duro de subida. El campo es
   opcional y esta skill no restringe herramientas: **se retira**. Es el mismo tipo de defecto
   que el frontmatter YAML inválido corregido en otras tres piezas del catálogo: no se ve hasta
   que falla en casa del comprador.
2. **Los pasos 6 y 7 no tenían rama "si falta el dato"**, así que solo 5 de 7 cumplían el molde de
   la serie. Añadidas las dos.
3. **7 reglas NUNCA donde la rúbrica pide 8.** Añadidas dos, las dos derivadas del cierre de
   atribución: no presentar la tasa sectorial como si fuera la del local, y no asignar tareas por
   nombre en vez de por puesto.

Resultado: **19/20 declarado** (20/20 mecánico menos el punto 19 de criterio), desde 17/20 medido.

## [1.1.1] — 2026-08-16

**Tipo:** PARCHE (referencias, casos y corrección de trazabilidad). No cambia el
protocolo: quien usaba la 1.1.0 no tiene que releer nada.

### Corregido — incoherencia de versión (defecto de trazabilidad)
La 1.1.0 salió con **cinco declaraciones de versión y dos valores distintos**:
frontmatter `metadata.version: 1.1.0`, pie de `SKILL.md` `v1.0.0`,
`metadata.json` `1.0.0`, cabecera de `LICENSE.txt` `v1.0.0` y Anexo A `v1.0.0`.
Es el fallo que hace imposible saber qué versión tiene instalada un cliente
cuando llama para reportar un problema — y con la cadencia de actualización como
tesis de venta, no poder identificar la versión instalada es un defecto
comercial, no cosmético. Unificadas las cinco en **1.1.1**. Añadida en
`SKILL.md § Versión` la regla de que las cinco se leen juntas antes de empaquetar.

### Añadido
- **`cases/`** — los cuatro casos existían solo como párrafo dentro de
  `SKILL.md`, sin entrada real ni salida esperada completa, y el `README.md`
  anunciaba una carpeta `cases/` que no existía, con otros nombres de archivo.
  Ahora son cuatro archivos con encargo literal, tabla de entrada con estado por
  dato y salida completa: `case_01_happy_path.md` (restaurante de 42 cubiertos,
  turno partido, dos puntos de fricción reales), `case_02_edge_case.md` (bar de
  dos personas sin turnos, en México — la skill **suprime** el bloque de cambio
  de turno, añade uno de media jornada y regionaliza la cifra de cámara),
  `case_03_failure.md` ("hazme un checklist de cierre" y nada más — entrega diez
  tareas ejecutables con las horas en `[hora local]`, sin inventar horario) y
  `case_04_integration.md` (encadenado con `escandallo-ingenieria-menu` y
  `receta-estandar`, consumiendo la tolerancia ±10 % sin recalcularla).
- **`references/FUENTES.md`** — la skill no tenía ni una sola referencia externa
  con URL. Cuatro fuentes verificadas contra el documento primario, cada una con
  la afirmación concreta de la skill que sostiene: Reglamento (CE) 852/2004
  art. 5, AESAN flexibilidad APPCC, informe AESAN-2021-004 de combinaciones
  tiempo-temperatura, y NOM-251-SSA1-2009. Incluye la lista explícita de cifras
  de la skill que **no** tienen fuente externa, y por qué.
- Nuevo límite en `SKILL.md`: las temperaturas de los criterios de "hecho" son
  umbrales operativos, no la norma legal del país del cliente. El 0-4 °C de
  `tareas-maestras.md` es criterio de oficio, no máximo legal de ningún país.

### Pendiente, declarado
- Las cifras de tasa y coste de rotación de la sección `## Umbral que sostiene el
  producto` y de `scripts/coste_rotacion.py` están **en corrección centralizada**
  por la casa a fecha 15-ago-2026 y no se han tocado en este parche. Marcado
  también en `metadata.json`. Hasta que esa corrección cierre, esas cifras no
  entran en material de venta (G5 sigue sin levantar).

## [1.1.0] — 2026-08-15

**Fusión con `checklist-turno`.** La auditoría de puerta estrecha del 15-ago-2026
detectó que las dos skills tenían la `description` idéntica palabra por palabra:
competían por el mismo disparo y el cliente veía una skill que "a veces no
responde". Sergio firmó la fusión el mismo día.

### Añadido (procedente de `checklist-turno`)
- Sección **"Las cinco reglas que hacen que una lista se use"** — criterio de
  terminación, un responsable por puesto, momento exacto, longitud máxima por
  bloque y marcado de lo crítico. Es lo que separa una lista que se ejecuta de
  una que se firma en la puerta.
- Sección **"Implantación: dos semanas"** — la secuencia días 1-3 / 4-14 / 15 en
  adelante, con auditoría física de tres puntos al azar. Sin esto, una lista
  repartida deja de ejecutarse en unos diez días.
- `assets/plantilla-checklist.md` y `assets/plantilla-parte-incidencias.md` —
  plantillas en blanco listas para imprimir, con tres filas de ejemplo.

### Retirado del catálogo
- `checklist-turno` queda retirada. Todo su contenido está aquí. Ver
  `RETIRADA-checklist-turno.md`.

## [1.0.0] — 2026-08-14
Primera versión: plantillas por tipo de local, tareas maestras, parte de
incidencias y `scripts/coste_rotacion.py` con autotest.
