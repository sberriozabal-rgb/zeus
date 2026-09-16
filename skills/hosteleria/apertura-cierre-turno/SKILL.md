---
name: apertura-cierre-turno
description: >-
  Genera los checklists de apertura, cambio de turno y cierre de un local de hostelería, y
  el parte de incidencias que los acompaña, adaptados al tipo de local, a sus horarios y a
  quién los va a firmar. Cada tarea sale con su responsable por puesto, su momento exacto
  y su criterio de "hecho", porque una lista sin criterio de terminación se firma sin
  ejecutar. Úsala siempre que se hable de checklist, lista de apertura, lista de cierre,
  protocolo de turno, parte de incidencias, cambio de turno, procedimiento de arranque o
  de cierre de local, o cuando alguien pregunte qué hay que hacer al abrir, qué se revisa
  antes del servicio, cómo dejar el local al cerrar, cómo pasar el turno al siguiente
  encargado o cómo evitar que se olviden cosas. Aplica también con frases del oficio como
  "siempre se olvida algo al abrir", "quiero que quede por escrito", "el turno de tarde no
  se entera de nada" o "necesito un protocolo para el nuevo". No la uses para planes de
  higiene certificados ni para el cuadrante de personal.
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso comercial sin derecho de redistribución. Ver LICENSE.txt.
compatibility: Agent Skills — estándar abierto (agentskills.io). Sin dependencias de un motor concreto.
metadata:
  version: 1.1.2
  author: FORJA
  linea: hosteleria
  peldaño: P1
---

# Checklists de apertura, cambio de turno y cierre

## Qué hace

Convierte el protocolo que hoy vive en la cabeza del encargado —o en una hoja de papel que nadie actualiza— en tres checklists (apertura, cambio de turno, cierre) más un parte de incidencias, cada tarea con responsable nombrado por puesto, momento exacto del servicio, y un criterio de "hecho" que se puede verificar mirando el resultado, no preguntando si se hizo.

Esto no es una lista genérica de sentido común. Es la secuencia real de un local con su tipo de cocina, su horario, su plantilla y sus puntos donde históricamente se pierde dinero o se genera una incidencia: temperatura de cámara no registrada, caja no cuadrada, mise en place a medias, sala sin montar antes de la hora de reserva.

## Cuándo se dispara

- "hazme el checklist de apertura / cierre"
- "necesito una lista de lo que hay que hacer al abrir el restaurante"
- "protocolo de cambio de turno"
- "parte de incidencias" / "libro de incidencias"
- "siempre se nos olvida algo al abrir / cerrar"
- "el turno de tarde no se entera de lo que pasó en el de mañana"
- "quiero que quede por escrito quién hace qué"
- "necesito un protocolo para el empleado nuevo"
- "cómo dejamos el local listo para mañana"
- "qué se revisa antes de abrir puertas"
- "cuadre de caja al cierre"
- jerga del gremio: "mise en place", "pase", "servicio", "cámara", "libro de temperaturas", "arqueo"

## Quién lo ejecuta

El encargado o jefe de sala/cocina, en dos momentos de baja disponibilidad de atención: antes de abrir puertas (10-30 minutos de margen real) y al cerrar (con el cansancio del servicio ya encima). No lee 40 líneas ni interpreta ambigüedad. Cada tarea debe leerse y ejecutarse sin preguntar qué significa "revisar bien".

## Las cinco reglas que hacen que una lista se use

Esto es lo que separa un checklist que se ejecuta de uno que se firma en la puerta al salir. Las cinco se aplican a cada línea que generes, sin excepción.

**1 · Criterio de terminación, no verbo vago.** "Comprobar el género" no vale. "Anotar la temperatura de cámara de pescado; si supera 4 °C, avisar al encargado antes de sacar nada" sí. Sin criterio, la lista se firma sin ejecutar.

**2 · Un responsable por puesto y por tarea.** Una tarea de dos dueños es una tarea de ninguno. Y se asigna al puesto, no al nombre: la lista tiene que seguir sirviendo cuando esa persona se vaya, que en un sector con un 63,8% de rotación anual en España (informe Synergie España 2026) y hasta un 120% en México (CANIRAC) `[ver references/FUENTES.md]` es pronto.

**3 · Momento exacto, no "antes del servicio".** "T−90", "T−30", "al cerrar caja". Una tarea sin hora se acumula en los últimos diez minutos junto a todas las demás, y ahí es donde se pierden.

**4 · Corta o no se hace.** Apertura: entre 12 y 20 puntos. Cierre: entre 10 y 18. Cambio de turno: 6 a 10. Si sale más larga, hay dos listas metidas en una o hay tareas que en realidad son semanales. Sepáralas: **diaria, semanal y mensual**, y que la diaria sea la única que se firma cada día.

**5 · Lo crítico va primero y va marcado.** Seguridad alimentaria, seguridad de las personas y dinero. Si el turno se complica y la lista queda a medias, que lo que quede sin hacer sea lo prescindible. Marca esos puntos y di por qué lo son.

## Entrada

Lo que el usuario aporta, en cualquier combinación, y lo que se hace si falta:

- **Tipo de local** (bar, restaurante de mesa y mantel, fast-casual, cocina de producto, local con delivery) — determina qué tareas aplican. Si no se indica, se pregunta una vez; si no hay respuesta, se asume restaurante de mesa y mantel de tamaño medio y se declara el supuesto.
- **Horario de apertura/cierre y turnos** — si no se da, se deja el campo de hora en blanco marcado `[hora local]` para que el cliente lo rellene, nunca se inventa un horario.
- **Plantilla por puesto** (sala, cocina, encargado) — si no se da, las tareas se asignan por puesto genérico ("responsable de sala") en vez de nombre, y se declara que falta el reparto real.
- **Puntos de fricción conocidos** (lo que "siempre se olvida", incidencias repetidas) — si el cliente los da, se incorporan como tareas explícitas con su propio criterio de hecho; es la parte con más valor porque viene de su oficio, no del genérico.
- **Dato sucio típico**: el cliente pega una lista desordenada de tareas sin horario ni responsable, o dicta de memoria mezclando apertura y cierre. La skill reordena, asigna puesto por defecto donde falta, marca en una nota aparte qué se asumió, y nunca descarta una tarea mencionada por no encajar en la plantilla.

## Umbral que sostiene el producto

La hostelería española renueva cada año en torno al **63,8 % de su plantilla** —la tasa más alta
de toda la economía del país, según el informe *La situación del empleo en el sector Hospitality
en España 2026* de **Synergie España**
(<https://www.revistahosteleria.com/texto-diario/mostrar/5860927/tasa-rotacion-638-puestos-cubrir-obligan-reinventar-seleccion-personal>)—
y sustituir a una persona de sala o cocina cuesta entre
**2.800 y 5.000 €** sumando selección, formación y caída temporal de productividad, según el
análisis de **Linkers**
(<https://www.hosteleriasalamanca.es/noticias-hosteleria/abril-2026/hosteleria-espanola-crece-pierde-talento>).
En México, **CANIRAC** declara una rotación de entre el **80 % y el
120 % anual** y sitúa el coste de cubrir una vacante en **dos a tres veces el salario de ese
puesto**
(<https://www.jornada.com.mx/noticia/2024/02/21/economia/falta-de-personal-en-restaurantes-eleva-costos-canirac-7205>).

Las cuatro cifras tienen autor nombrado, año y URL recuperable en `references/FUENTES.md`. Lo que
**ninguna** tiene es tamaño de muestra ni metodología publicados: dos vienen de empresas del
sector y una de la cámara patronal, así que **se citan siempre con el nombre de quien las publica
y nunca como dato oficial** `[SIN TAMAÑO DE MUESTRA PUBLICADO]`.

Traducido al local: una plantilla española de diez personas sustituye a algo más de seis a lo largo del año, y eso son entre **17.900 y 31.900 € anuales** que no figuran en ninguna línea de la cuenta de explotación. Están repartidos en horas extra de quien cubre el hueco, en el rendimiento de las primeras semanas del que entra, en tiempo de encargado dedicado a seleccionar y en errores de servicio durante la adaptación. El multiplicador mexicano —dos a tres veces el salario— sirve al dueño de cualquier país, porque lo calcula con su propia nómina delante en vez de fiarse de una media ajena.

El checklist no reduce la rotación. Reduce lo que cuesta cada baja mientras se cubre el puesto: un empleado nuevo con criterio de "hecho" explícito llega antes a la autonomía y comete menos errores de apertura/cierre que uno al que se le explicó de palabra un martes con prisa. El cálculo exacto para el local del cliente se ejecuta con `scripts/coste_rotacion.py`, no se estima a ojo.

## Procedimiento

1. **Entrada: tipo de local y datos disponibles → Acción: clasificar contra las 5 plantillas base de `references/plantillas-por-tipo.md` → Salida: plantilla seleccionada o combinación de dos → Si falta el dato: usar restaurante de mesa y mantel medio y declararlo.**

2. **Entrada: horario y turnos → Acción: distribuir las tareas de `references/tareas-maestras.md` en apertura / cambio de turno / cierre según el momento del servicio en que cada una es ejecutable → Salida: tres bloques horarios con tareas asignadas → Si falta el dato: dejar `[hora local]` en cada bloque, nunca inventar un horario de ejemplo como si fuera el real.**

3. **Entrada: plantilla por puesto → Acción: asignar cada tarea a un puesto (nunca a "alguien" o "el equipo") → Salida: columna de responsable rellena → Si falta el dato: usar el puesto genérico del oficio (sala/cocina/encargado) y marcar que falta el nombre real.**

4. **Entrada: puntos de fricción del cliente → Acción: convertir cada uno en una tarea con criterio de hecho verificable, insertada en el bloque horario que corresponda → Salida: tareas añadidas, marcadas como específicas del local (no de la plantilla base) → Si falta el dato: no añadir nada inventado; la plantilla base ya cubre los puntos de fricción más comunes del oficio.**

5. **Entrada: todas las tareas reunidas → Acción: para cada una, redactar el criterio de "hecho" en forma verificable por inspección (no "revisar la cámara" sino "temperatura de cámara anotada en el registro, entre 0-4°C") → Salida: cada línea del checklist con su criterio de cierre → Si el criterio no se puede verificar sin preguntar, la tarea se reescribe hasta que se pueda.**

6. **Entrada: checklists completos → Acción: generar el parte de incidencias como plantilla separada, con campos fijos (fecha, turno, puesto que reporta, descripción, gravedad, acción tomada, pendiente para el siguiente turno) → Salida: plantilla de parte de incidencias lista para imprimir o volcar a hoja digital → Si falta el dato: se entregan los campos fijos del oficio y se marca `[a completar por el local]` el nombre de los turnos, nunca se inventan turnos de ejemplo.**

7. **Entrada: petición de cifra de negocio → Acción: ejecutar `scripts/coste_rotacion.py` con la plantilla real del cliente, o con la tasa sectorial si no la tiene → Salida: coste anual de rotación y rango de ahorro potencial, siempre con la fuente de la tasa usada declarada → Si falta el dato: sin plantilla real del cliente se usa la tasa sectorial con su autor citado (Synergie España o CANIRAC según el país) y el informe declara en su primera línea que la cifra es una referencia de mercado y no la del local.**

## Salida

```markdown
# Checklist de apertura — [nombre del local]

## Apertura ([hora local] – [hora local])
| # | Tarea | Responsable | Criterio de "hecho" |
|---|---|---|---|
| 1 | ... | [puesto] | [verificable por inspección] |

## Cambio de turno ([hora local])
| # | Tarea | Responsable (sale) | Responsable (entra) | Criterio de "hecho" |
|---|---|---|---|---|
| 1 | ... | [puesto] | [puesto] | [verificable] |

## Cierre ([hora local] – [hora local])
| # | Tarea | Responsable | Criterio de "hecho" |
|---|---|---|---|
| 1 | ... | [puesto] | [verificable por inspección] |

## Parte de incidencias
| Fecha | Turno | Puesto que reporta | Descripción | Gravedad (baja/media/alta) | Acción tomada | Pendiente para el siguiente turno |
|---|---|---|---|---|---|---|

## Coste de rotación de referencia (si se calculó)
[salida de scripts/coste_rotacion.py]

## Implantación: dos semanas, y sin esto la lista no sirve de nada

Una lista repartida y no auditada deja de ejecutarse en unos diez días. Entregar el documento sin esta secuencia es entregar papel. Va siempre con el checklist, en la misma entrega:

- **Días 1 a 3:** el encargado ejecuta la lista con el equipo delante y corrige lo que no encaja con el local real. Casi siempre hay dos o tres puntos imposibles a esa hora.
- **Días 4 a 14:** se ejecuta y se firma. Auditoría sorpresa dos veces por semana, comprobando **tres puntos al azar de forma física**, no la firma.
- **A partir del día 15:** auditoría semanal. Si un punto se salta tres veces, el problema es el punto, no la persona: o está mal colocado en el tiempo, o le falta criterio, o sobra.

Ese último criterio es el que mantiene la lista viva. La mayoría de los checklists mueren porque nadie los revisa nunca después de escribirlos.

Las plantillas en blanco listas para imprimir están en `assets/plantilla-checklist.md` y `assets/plantilla-parte-incidencias.md`: se entregan al cliente tal cual, con las tres primeras filas ya rellenas como ejemplo de criterio de terminación bien escrito.

## Supuestos de esta versión
- [qué se asumió por falta de dato, una línea por supuesto]
```

Longitud máxima: 120 líneas por checklist completo (los tres bloques + parte de incidencias). Si supera eso, es señal de que el local necesita dos protocolos separados (p. ej. cocina y sala por separado), no una lista más larga.

## Límites

- No es un plan de higiene alimentaria (APPCC/HACCP) certificado. Las tareas de temperatura y limpieza que incluye son de control operativo diario, no sustituyen el plan certificado que exige la autoridad sanitaria local. Se declara en cada entrega.
- No genera el cuadrante de personal ni calcula turnos legales (descansos, horas máximas). Eso es una skill distinta.
- No certifica cumplimiento normativo de ningún tipo. Cuando una tarea toca normativa (manipulación de alimentos, prevención de riesgos), se marca `[verificar con asesoría/consultoría local]`.
- El coste de rotación que calcula es una referencia de gestión, no una cifra contable ni fiscal.
- Las cifras de temperatura que aparecen en los criterios de "hecho" son **umbrales operativos**, no la norma legal del país del cliente. El rango de frío positivo 0-4 °C es criterio de oficio conservador; el máximo normado cambia por país (México: 7 °C, NOM-251-SSA1-2009 §5.5.2). Al instalar se cita la norma local. Fuentes verificadas y su ámbito: `references/FUENTES.md`.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Asignar cada tarea a un puesto nombrado, nunca a "el equipo" | Una tarea sin dueño no se hace: la responsabilidad difusa es la causa nº1 de checklist ignorado |
| Escribir el criterio de "hecho" en forma verificable por inspección | Si hay que preguntar si se cumplió, el checklist no sirve bajo presión de servicio |
| Declarar qué se asumió cuando falta un dato del cliente | Un checklist con horarios inventados se descarta en la primera lectura por el encargado real |
| Separar apertura, cambio de turno y cierre en bloques distintos | Se ejecutan en momentos distintos, con distinta gente y distinta urgencia; mezclarlos garantiza que algo se salte |
| Incluir el parte de incidencias como pieza separada, no como nota al pie | La incidencia de hoy es la tarea de mañana; si no tiene su propio espacio, se pierde en el cambio de turno |
| Marcar toda tarea de normativa sanitaria como referencia de control, no de certificación | Confundir checklist operativo con plan APPCC certificado genera falsa sensación de cumplimiento legal |
| Ejecutar el cálculo de coste de rotación con datos reales del cliente cuando existan, no con la cifra sectorial | El dato del cliente es siempre más defendible ante él mismo que una media nacional |
| Limitar cada checklist a lo ejecutable en el margen de tiempo real del turno | Una lista de 40 tareas para 15 minutos de margen antes de abrir puertas no se ejecuta, se firma sin mirar |
| Incorporar los puntos de fricción que el cliente ya conoce como tareas explícitas | Es la parte que un aficionado con ChatGPT genérico no puede replicar: el criterio de oficio de ESE local |
| Numerar cada tarea para que el parte de incidencias pueda referenciarla | Sin número, una incidencia no se puede vincular a la tarea del checklist que falló |

| NUNCA | Porqué |
|---|---|
| Inventar un horario de ejemplo como si fuera el real del cliente | Un horario de mentira en un documento operativo se copia y se usa por error |
| Dejar un criterio de "hecho" en forma de opinión ("revisar bien", "comprobar que todo esté correcto") | Es exactamente lo que un checklist debe eliminar: la interpretación bajo presión |
| Mezclar tareas de apertura y cierre en un mismo bloque | Genera confusión sobre cuándo se ejecuta cada una y duplica trabajo de lectura |
| Presentar el checklist como sustituto de un plan de higiene certificado | Expone al cliente a una falsa sensación de cumplimiento normativo que no tiene |
| Calcular el coste de rotación a mano en vez de con el script | Un cálculo con dinero que se estima en vez de ejecutarse es el error que rompe la confianza del cliente |
| Omitir la fuente de la tasa de rotación usada (real del cliente vs. sectorial) | Sin esa distinción, el cliente no sabe si la cifra es suya o una referencia externa |
| Generar más de 120 líneas totales sin avisar que el local necesita protocolos separados | Un checklist que nadie termina de leer es papel decorativo, no producto |
| Asignar una tarea de cocina a sala o viceversa sin que el cliente lo haya confirmado | Rompe la credibilidad del checklist frente a quien conoce la operación real del local |
| Presentar la tasa de rotación sectorial como si fuera la del local del cliente | Es una media de mercado de una empresa del sector, sin tamaño de muestra publicado: usarla como cifra propia es la cifra huérfana que el cliente pregunta y no se puede defender |
| Asignar una tarea a una persona por su nombre en vez de a su puesto | Con dos de cada tres empleados cambiando de trabajo al año, una lista atada a un nombre caduca antes de que se imprima la siguiente versión |

## Antipatrones

1. **Síntoma**: el checklist se firma cada día sin variación, incluso en días con incidencia real reportada. **Causa raíz**: el criterio de "hecho" es una casilla, no una verificación (falta el dato concreto: temperatura, cifra de caja, foto). **Corrección**: reescribir el criterio para que exija un dato, no una marca.

2. **Síntoma**: el turno de tarde repite un error que el de mañana ya había resuelto. **Causa raíz**: no existe parte de incidencias, o existe pero no se lee al iniciar el turno siguiente. **Corrección**: mover el parte de incidencias al primer punto del checklist de cambio de turno, no al final.

3. **Síntoma**: el empleado nuevo tarda semanas en no necesitar que le expliquen la apertura. **Causa raíz**: el procedimiento vive en la cabeza del encargado, no está escrito con criterio verificable. **Corrección**: esta skill resuelve exactamente esto — el punto de fricción es la ficha comercial del producto.

4. **Síntoma**: el checklist tiene 35 tareas y nadie lo completa entero. **Causa raíz**: se mezclaron tareas de apertura, cierre y limpieza profunda semanal en una sola lista diaria. **Corrección**: separar por frecuencia real (diaria vs. semanal) y dejar solo lo diario en el checklist de turno. `[DERIVADO, NO OBSERVADO EN CAMPO]`

5. **Síntoma**: el arqueo de caja no cuadra y nadie sabe en qué turno se descuadró. **Causa raíz**: el cuadre de caja no está en el checklist de cierre como tarea numerada con responsable y hora. **Corrección**: incluir el arqueo como tarea obligatoria de cierre con cifra registrada, no solo "cerrar caja".

## Casos de prueba

Los cuatro casos, con entrada real y salida esperada completa, están en `cases/`
(`case_01_happy_path.md`, `case_02_edge_case.md`, `case_03_failure.md`,
`case_04_integration.md`). Resumen:

**Happy path**: "Somos un restaurante de mesa y mantel, abrimos a las 12:00 y cerramos a las 23:30, tenemos 3 en sala, 3 en cocina y un encargado. Se nos olvida siempre revisar que la cámara esté a temperatura antes de abrir." → Genera los tres checklists completos con horarios reales, plantilla por puesto real, y la tarea de temperatura de cámara insertada en apertura con criterio de hecho verificable (temperatura anotada, rango 0-4°C).

**Edge case**: local con un solo turno partido y solo dos empleados que hacen de todo (sala y cocina indistintamente). → La skill no fuerza la plantilla de puestos separados: genera checklist con responsable "el que está" pero mantiene el criterio de hecho verificable, y declara en supuestos que con plantilla de 2 el reparto por puesto no aplica.

**Failure (encargo de una línea sin contexto)**: "hazme un checklist de cierre". → No se rinde ni pide todos los datos antes de producir. Entrega el checklist de cierre con la plantilla base de restaurante de mesa y mantel medio, horarios en `[hora local]`, puestos genéricos (sala/cocina/encargado), y declara en una línea final: "Asumido: restaurante tipo mesa y mantel, tamaño medio, sin datos de horario ni plantilla — ajusta los campos entre corchetes con tus datos reales."

**Integration (encadenado con otro activo)**: tras ejecutar `escandallo-ingenieria-menu` y detectar mise en place descontrolada como causa de mermas, se pide el checklist de apertura que incorpore verificación de mise en place por partida. → La skill añade como tarea de fricción específica "mise en place de [partida] verificada contra ficha técnica de escandallo", vinculando el criterio de hecho al umbral ya calculado por la otra skill, sin recalcular nada que no le corresponda.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.1 — ver `CHANGELOG.md`. La versión declarada aquí, en el frontmatter, en
`metadata.json`, en `LICENSE.txt` y en el Anexo A es siempre la misma cifra: si
divergen, la entrega no sale de fábrica.
