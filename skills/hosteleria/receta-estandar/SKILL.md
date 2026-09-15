---
name: receta-estandar
description: >-
  Convierte la forma de cocinar un plato que hoy solo vive en la cabeza de un cocinero (o
  en notas sueltas, fotos, videos de WhatsApp) en una ficha de receta estándar completa y
  ejecutable por cualquier cocinero del turno, con ingredientes en gramos exactos,
  procedimiento en pasos numerados, puntos críticos de control HACCP y criterio de
  emplatado verificable. Úsala siempre que se pida estandarizar una receta, escribir una
  ficha técnica de cocina, documentar "cómo se hace" un plato, resolver que "cada cocinero
  lo hace distinto", preparar el traspaso de una receta a un cocinero nuevo, o escalar una
  receta a más porciones — aunque el usuario no diga "receta estándar" explícitamente (p.
  ej. "escríbeme cómo se hace este plato para que lo pueda hacer cualquiera", "el turno de
  tarde lo hace diferente al de mañana", "necesito dejar esto documentado antes de irme").
license: Propiedad de ZEUS Suite — ver condiciones de distribución del catálogo FORJA
compatibility: Cualquier cliente de Agent Skills conforme a la especificación agentskills.io. No requiere herramientas externas para el uso base; el script de escalado requiere Python 3.9+.
metadata:
  vertical: gastronomia
  posicion_cola: "2"
  version: 1.1.0
  estado: ACORDADO
  contrato_entrada: "ficha de receta-estandar (JSON o tabla) con gramaje por porción"
  contrato_salida_hacia: "escandallo-ingenieria-menu, apertura-cierre-turno"
---

# Ficha de receta estándar

## Qué hace

Convierte la descripción verbal, manuscrita o parcial de cómo se prepara un plato
en una ficha ejecutable por un cocinero que nunca vio ese plato hacerse: gramaje
exacto por ingrediente, procedimiento en pasos numerados con tiempo y
temperatura, puntos críticos de control marcados con la cifra de la norma del
país, y criterio de emplatado verificable. En 20-40 minutos por receta
`[A VALIDAR — estimación de fuente sectorial única, ver references/FUENTES.md]`.

No cocina. Extrae, pregunta lo mínimo imprescindible y escribe con el nivel de
precisión que permite que dos personas distintas, en turnos distintos, produzcan
el mismo plato dentro de una tolerancia declarada.

Lo que la separa de pedirle una receta a un modelo genérico: el modelo genérico
devuelve una receta bonita. Esto devuelve **la receta de ESE local**, con las
cantidades que ese chef usa, la temperatura interna que exige la norma de su
país, la tolerancia de porción que su food cost aguanta, y una marca visible en
cada dato que todavía no se ha pesado. Un hueco declarado vale más que un número
plausible que alguien cocinará como si fuera cierto.

## Cuándo se dispara

- "necesito estandarizar las recetas de la carta"
- "hazme la ficha técnica de este plato"
- "escríbeme cómo se hace esto para que lo pueda hacer cualquiera"
- "cada cocinero lo hace distinto" / "el turno de tarde lo hace diferente al de mañana"
- "se me va el chef y no quiero perder las recetas"
- "necesito dejar esto documentado antes de irme"
- "tengo que escalar esta receta para un catering de 80"
- "el plato ya no sale como antes"
- "quiero abrir el segundo local y que la comida sea igual"
- "necesito las recetas para poder sacar el escandallo"
- jerga del gremio: "ficha técnica", "receta madre", "gramaje", "rendimiento",
  "mise en place", "partida", "punto crítico", "sonda", "merma", "porcionado",
  "food cost", "line cook", "86", "escandallo"

## Quién lo ejecuta

El jefe de cocina, el chef propietario o el segundo, **fuera de servicio**: entre
turnos, en la sobremesa, o el día de cierre. No es una tarea de servicio y no se
hace con el pase lleno. Dispone de 20-40 minutos por receta y trabaja con lo que
recuerda, con notas sueltas y con el producto delante si hay suerte.

Quien **lee** la ficha después es otro: el cocinero de línea, a menudo recién
incorporado, de pie, con las manos ocupadas y la ficha plastificada colgada en su
partida. Esa asimetría manda sobre todo el formato: la escribe alguien con
tiempo, la ejecuta alguien que no lo tiene. Un paso que exige releerse dos veces
en plena partida es un paso mal escrito.

## Entrada

Lo que el usuario aporta, en cualquier combinación, y qué se hace si falta:

- **Descripción del plato** en cualquier formato (texto, notas a mano,
  transcripción de un vídeo, receta antigua en otro formato, foto). Si no hay
  **ningún** dato de ingredientes ni de procedimiento, ni siquiera aproximado, es
  el único caso en que se detiene: no hay materia prima sobre la que estandarizar
  y se dice, en vez de inventar un plato.
- **Cantidades**. Si vienen en unidades caseras se convierten con
  `references/equivalencias_cocina.md`. Si no vienen, se propone el valor de
  partida más defendible marcado `[CANTIDAD ESTIMADA — VERIFICAR CON PESAJE]`,
  nunca un rango sin ancla.
- **Rendimiento y número de porciones**. Si falta uno de los dos, se deriva del
  otro y se marca. Si faltan los dos, se asume la producción declarada por el
  chef para un servicio y se declara el supuesto.
- **País de operación**. Determina qué tabla de temperaturas aplica: España
  (AESAN) y México (NOM-251) **no coinciden**. Si no se indica, se pregunta una
  vez; si no hay respuesta, la ficha no pasa de BORRADOR y sus puntos críticos
  van marcados `[A VALIDAR — PAÍS SIN DECLARAR]`.
- **Quién ejecuta la receta en el día a día** (line cook junior o chef con
  oficio). Si no se indica, se asume el nivel más bajo: se escribe para el
  junior. Una ficha escrita para el junior también la puede usar el chef; al
  revés no.
- **Foto o descripción del emplatado**. Si falta, la sección se entrega igual con
  los elementos disponibles y `[EMPLATADO PENDIENTE DE FOTO DE REFERENCIA]`.
  Nunca se omite la sección.
- **Dato sucio típico**: llega una nota de voz transcrita o un papel de libreta
  donde el chef mezcla dos preparaciones distintas en el mismo párrafo, salta del
  paso 2 al 5, dice "lo de siempre" para una elaboración que no describe en
  ningún sitio, y da cantidades para "una olla" sin decir cuántas porciones sale
  esa olla. La skill separa las dos preparaciones en dos fichas relacionadas
  (madre + derivada), numera los pasos en el orden real de ejecución aunque la
  fuente no lo traiga, marca "lo de siempre" como campo FALTA con su pregunta
  concreta, y deriva el rendimiento del peso total de la olla si el chef lo
  conoce. **No descarta ningún ingrediente mencionado** por no encajar en el
  formato.

## Umbral que sostiene el producto

Tres cifras hacen de esto un producto y no una plantilla de Word:

**1 · Las temperaturas internas mínimas, con la norma del país y el binomio
completo.** No "hasta que esté cocido". España, informe AESAN-2021-004: aves
**74 °C/1 s**, carne **70 °C/1 s**, pescado **68 °C/15 s**, mantenimiento en
caliente **≥63 °C**, recalentamiento **≥74 °C/15 s**. México,
NOM-251-SSA1-2009: aves y rellenos **74 °C** (§7.3.1), carnes molidas y cerdo en
trozo **68 °C**, pescado y trozos de res **63 °C**, mantenimiento en caliente
**>60 °C** y en frío **≤7 °C** (§7.3.3), refrigeración máx. **7 °C** (§5.5.2).
Las dos tablas y sus discrepancias, en `references/temperaturas_haccp.md`; las
URLs, en `references/FUENTES.md`.

El umbral no es saber que el pollo va a 74 °C — eso lo dice cualquiera. El umbral
es **saber que el pescado no lleva la misma cifra en Madrid que en Monterrey**
(68 °C/15 s frente a 63 °C), que AESAN exige binomio y no solo grados, y que una
ficha que viaja entre los dos países se reescribe en lugar de copiarse. Eso es lo
que un aficionado no sabe y lo que un inspector sí pregunta.

**2 · La tolerancia de porción: ±10 % sobre el peso de plato servido**, no sobre
ingrediente crudo. `[A VALIDAR — criterio de oficio de la casa, no normado]`. Sin
tolerancia declarada cada cocinero fija la suya y el food cost se mueve sin que
nadie sepa por qué; con ella, el descuadre se detecta pesando tres platos al azar
en el pase.

**3 · El corte de estado: más de 4 de los 10 campos obligatorios ausentes → la
ficha no pasa de BORRADOR.** `[A VALIDAR — criterio de oficio de la casa]`. Es la
línea que impide que una hipótesis de receta circule por la cocina con aspecto de
estándar.

Y una regla de estado que no es una cifra pero funciona como tal: **ninguna ficha
es ACORDADO hasta que se ha pesado una vez.** Una ficha nunca pesada es una
hipótesis, por bien escrita que esté.

## Procedimiento

1. **Entrada: la descripción del plato en el formato que llegue → Acción: cotejar
   contra los 10 campos obligatorios del paso 2 e identificar qué existe → Salida:
   tabla de campos con estado CONFIRMADO / FALTA / AMBIGUO → Si falta el dato: se
   pasa al paso 2 igualmente; no se detiene aquí ni se pide todo antes de
   empezar.**

2. **Entrada: la tabla de estado del paso 1 → Acción: verificar los 10 campos —
   nombre del plato · rendimiento total (porciones + peso/volumen) · tamaño de
   porción · ingredientes con cantidad exacta en g o ml · procedimiento numerado ·
   temperaturas y tiempos de cocción · puntos críticos de control · mise en place
   (utensilios y preparación previa) · conservación y servicio · criterio de
   emplatado → Salida: los 10 campos completos o marcados con su convención → Si
   faltan más de 4 de los 10: la ficha se entrega igual, pero sale marcada
   BORRADOR en la cabecera y no como estándar de trabajo.**

3. **Entrada: cantidades en unidades caseras ("un puñado", "al gusto", "una
   taza") → Acción: convertir a gramos o mililitros con
   `references/equivalencias_cocina.md`; si el ingrediente es intrínsecamente
   variable (sal, especia, acidez final), declarar un rango con un punto de
   partida numérico → Salida: cada ingrediente con cantidad numérica y unidad de
   peso o volumen → Si falta el dato: marcar
   `[CANTIDAD ESTIMADA — VERIFICAR CON PESAJE]` con el valor de partida más
   defendible. Nunca queda un "al gusto" solo ni un rango sin ancla.**

4. **Entrada: cantidad total y número de porciones → Acción: dividir peso o
   volumen total entre porciones y declarar la tolerancia sobre el peso de plato
   servido, no sobre ingredientes crudos → Salida: peso de porción individual +
   tolerancia → Si falta el dato: aplicar ±10 % marcado
   `[TOLERANCIA POR DEFECTO — AJUSTAR SEGÚN PLATO]`, y derivar el rendimiento del
   dato que sí exista (porciones o peso), nunca inventar los dos.**

5. **Entrada: la descripción de cómo se cocina, en el orden que venga → Acción:
   partir en pasos numerados de una sola acción cada uno, con su tiempo, su
   temperatura si aplica y el resultado observable que indica que el paso terminó
   → Salida: procedimiento ejecutable sin preguntar nada al chef → Si un paso dice
   "hasta que esté listo": se reescribe hasta que nombre la señal observable
   (color, textura, sonido, punto) que un cocinero puede verificar en su puesto
   con lo que tiene a mano.**

6. **Entrada: el país de operación y el procedimiento del paso 5 → Acción:
   identificar los pasos donde un error compromete la inocuidad (cocción de
   proteína animal, enfriamiento, recalentado, alérgenos) y marcarlos con la
   temperatura interna mínima **y el tiempo** de la tabla del país en
   `references/temperaturas_haccp.md` → Salida: pasos críticos con su binomio y
   método de verificación por sonda → Si el producto no está en la tabla del país
   (caza, curados, fermentados, sous-vide): se marca
   `[A VALIDAR — CONSULTAR AUTORIDAD SANITARIA LOCAL]`. **No se extrapola por
   analogía ni se toma la cifra de otro país.**

7. **Entrada: descripción del emplatado, o su ausencia total → Acción: convertir
   en instrucciones de posición, cantidad de guarnición y salsa, vajilla y
   temperatura de servicio → Salida: criterio de emplatado con al menos 3
   elementos verificables → Si falta el dato: se entrega con los elementos
   disponibles y `[EMPLATADO PENDIENTE DE FOTO DE REFERENCIA]`. La sección nunca
   se omite: el plato sale de cocina igual con ficha o sin ella, y el emplatado es
   el último tramo del proceso.**

8. **Entrada: la ficha completa → Acción: pasar el autocontrol — ¿podría
   ejecutarla un cocinero que nunca vio el plato, sin preguntar? ¿queda algún "al
   gusto" sin convertir? ¿tiene todo punto crítico su cifra, su tiempo y su método
   de verificación? ¿está declarada la tolerancia? ¿hay alguna cifra técnica sin
   fuente y sin marca `[A VALIDAR]`? ¿está declarado el país? → Salida: ficha en
   el formato de la sección `## Salida`, con todas las marcas de dato faltante
   visibles → Si alguna respuesta es mala: se reescribe antes de entregar, no se
   entrega con una nota de disculpa.**

## Salida

```markdown
# [Nombre del plato tal como aparece en la carta]

**Estado:** BORRADOR / ACORDADO · **Versión:** v0.0 · **País de operación:** [país]
**Último pesaje real:** [fecha] · **Escrita para:** [line cook junior / chef]

## 1. Rendimiento
- Rendimiento total: [n] porciones · [n] g / ml
- Porción individual: [n] g
- Tolerancia: ±[n] % sobre peso de plato servido

## 2. Ingredientes
| Ingrediente | Cantidad | Unidad | Estado | Nota |
|---|---|---|---|---|
| [nombre] | [n] | g / ml / ud | CONFIRMADO / ESTIMADO / PENDIENTE | [unidad de compra si difiere] |

## 3. Mise en place
- Utensilios: [lista]
- Preparación previa: [lista]

## 4. Procedimiento
| # | Acción | Tiempo | Temp. | Señal de que el paso terminó | PCC |
|---|---|---|---|---|---|
| 1 | [una sola acción] | [n min] | [n °C] | [observable en el puesto] | ● |

## 5. Puntos críticos de control
| Paso | Qué se controla | Umbral (temp + tiempo) | Verificación | Norma |
|---|---|---|---|---|
| [n] | [cocción / enfriamiento / recalentado] | [n °C durante n s] | Sonda en la parte más gruesa | [AESAN-2021-004 / NOM-251 §x] |

## 6. Conservación y servicio
- Conservación: [temperatura] · [caducidad interna]
- Servicio: [temperatura de pase]

## 7. Emplatado
- Vajilla: [pieza]
- Posición: [descripción verificable]
- Cantidades: [salsa n ml · guarnición n g]
- Temperatura de servicio: [n °C]

## 8. Notas de escalado
Elementos que NO escalan linealmente: [reducciones, sellados, ratio sartén/producto]

## 9. Datos pendientes de verificar
- [campo] — [qué haría falta para cerrarlo]

## 10. Supuestos de esta ficha
- [qué se asumió por falta de dato, una línea por supuesto]
```

Longitud máxima: **2 páginas A4 por ficha** (unas 90 líneas). Si se pasa, no es
una receta: son dos, y se separan en ficha madre y ficha derivada relacionadas —
el caso 2 lo resuelve así. Una ficha que no cabe plastificada en la partida no se
consulta, y una ficha que no se consulta no existe.

**Contrato de interfaz hacia las otras skills del sistema** (se entrega junto a la
ficha cuando se pide, no en lugar de ella):

```json
{
  "plato": "nombre exacto de carta",
  "pais_operacion": "ES|MX",
  "rendimiento_total": {"porciones": 0, "peso_g": 0},
  "porcion_individual_g": 0,
  "tolerancia_porcion_pct": 10,
  "ingredientes": [
    {"nombre": "", "cantidad": 0, "unidad": "g|ml|unidad", "marca": "CONFIRMADO|ESTIMADO|PENDIENTE"}
  ],
  "puntos_criticos_haccp": [
    {"paso": 0, "temp_min_c": 0, "tiempo_min_s": 0, "metodo_verificacion": "sonda", "norma": ""}
  ],
  "mise_en_place": [""],
  "conservacion": "",
  "estado": "BORRADOR|ACORDADO"
}
```

Consumen este contrato: `escandallo-ingenieria-menu` (ingrediente + cantidad +
unidad de compra, para calcular el coste — que **no** calcula esta skill) y
`apertura-cierre-turno` (bloque de mise en place y conservación, como tareas de
checklist de apertura o de estación).

## Límites

- **Una ficha de receta estándar no es un plan APPCC y no cumple el artículo 5 del
  Reglamento (CE) 852/2004**, que obliga al titular del negocio a *"crear, aplicar
  y mantener un procedimiento o procedimientos permanentes basados en los
  principios del APPCC"*. Marcar puntos críticos en una receta es una buena
  práctica de higiene documentada, no el sistema de autocontrol que la ley exige,
  y no sustituye la identificación de peligros ni la certificación por quien
  corresponda. Se declara en cada entrega. En México el marco equivalente es la
  NOM-251-SSA1-2009. Ver `references/FUENTES.md`.
- **No calcula coste ni escandallo.** Entrega el gramaje que otro calcula. El
  porcentaje de costes indirectos, el food cost objetivo y el precio de venta son
  trabajo de `escandallo-ingenieria-menu`, con la estructura real del negocio.
- **No valida binomios de sous-vide, curados, fermentados, conservas ni caza.**
  Esas categorías no están en las tablas de AESAN ni de la NOM-251 y salen
  marcadas `[A VALIDAR]` para que las cierre la autoridad sanitaria local o un
  consultor de seguridad alimentaria.
- **No sustituye el pesaje.** Toda cantidad no pesada sale marcada. La ficha no
  pasa a ACORDADO por estar bien escrita, sino por haberse pesado una vez.
- **No decide alérgenos ni etiquetado.** Marca dónde hay manejo de alérgenos como
  punto de atención; la declaración legal de alérgenos al comensal es materia
  normativa aparte y va a asesoría.

**Dónde aplica y dónde no:**

| Aplica bien | Aplica con ajuste | No aplica |
|---|---|---|
| Platos de carta con producción repetida (≥1 vez/semana) | Recetas de temporada corta — la ficha se declara vigente solo esa temporada | Alta cocina de autor irrepetible, pieza única de degustación sin repetición prevista |
| Recetas ya cocinadas al menos una vez, aunque no estén escritas | Recetas nuevas en desarrollo — la ficha sale BORRADOR hasta el primer pesaje | Recetas cuyo valor comercial depende de no documentarse (decisión del propietario, no técnica) |
| Cocina con más de una persona por turno | Cocina de una sola persona sin rotación: no aplica el beneficio de consistencia entre cocineros, sí el de costeo y escalado | — |
| Restaurantes que van a escalar (2ª sucursal, franquicia, catering de volumen) | — | — |

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Convertir toda cantidad a gramos o mililitros exactos | Las unidades caseras ("puñado", "chorrito") producen un plato distinto por cocinero: es la causa nº1 de inconsistencia del oficio |
| Declarar el rendimiento total Y la porción individual | Sin los dos números no se puede escalar la receta ni calcular coste por porción, y ambos alimentan a `escandallo-ingenieria-menu` |
| Declarar el país de operación en la cabecera de la ficha | Las temperaturas de AESAN y de la NOM-251 no coinciden: una ficha sin país no se puede defender ante ninguna inspección de ninguno de los dos |
| Marcar con temperatura numérica **y tiempo** todo punto de cocción de proteína animal | AESAN expresa binomios tiempo-temperatura; "hasta que esté cocido" no es verificable ni defendible, y solo los grados dejan el umbral a medias |
| Numerar los pasos en el orden real de ejecución | Un cocinero que nunca vio el plato debe poder seguir la ficha sin preguntar por dónde se empieza |
| Declarar una tolerancia de porción explícita (± % sobre plato servido) | Sin tolerancia, cada cocinero fija su propio margen y el food cost se mueve sin que nadie sepa por qué |
| Incluir el criterio de "terminado" observable en cada paso de cocción | Sustituye el criterio subjetivo del cocinero de turno por una señal que cualquiera verifica: color, textura, punto |
| Marcar con convención visible todo dato estimado, no medido o pendiente | Un hueco declarado vale más que un dato inventado que alguien cocinará como si fuera cierto |
| Verificar unidades de compra frente a unidades de receta antes de fijar cantidades | Un ingrediente comprado en kilo y usado en gramos, o en pieza y usado en porción, es el error de conversión silencioso más común |
| Escribir la ficha para el nivel más bajo que la vaya a ejecutar | Una ficha escrita para el junior también la usa el chef; al revés, no |
| Declarar la fecha del último pesaje real en la cabecera | Es lo único que distingue un estándar verificado de una hipótesis con buena maquetación |
| Declarar dónde vive físicamente la ficha en la cocina | Una ficha en un PDF de oficina no se consulta en la partida; el formato de entrega forma parte del producto |

| NUNCA | Porqué |
|---|---|
| Dejar "al gusto" como única cantidad de un ingrediente | Impide costear el plato y garantiza que cada cocinero decida un sabor distinto |
| Verificar un punto crítico de cocción solo por criterio visual | Un color similar puede corresponder a temperaturas internas muy distintas; lo visual no es evidencia ante una inspección |
| Escalar una receta multiplicando cantidades sin ajustar tiempos de cocción y reducción | Multiplicar x10 una salsa no multiplica x10 su tiempo de reducción: es el antipatrón nº3, documentado del oficio |
| Fusionar dos acciones distintas en un solo paso numerado | Rompe el paso atómico: quien lee no sabe si terminó un paso o dos |
| Inventar una temperatura de seguridad para un producto que no está en la tabla del país | Se marca `[A VALIDAR]` y se remite a la autoridad sanitaria local. Nunca se estima por analogía ni se toma la cifra de otro país |
| Mezclar la tabla de temperaturas de España con la de México en una misma ficha | Produce una ficha que no es defendible en ninguno de los dos países, que es peor que no tener ficha |
| Cerrar la ficha sin sección de emplatado, aunque no haya foto de referencia | El plato sale de cocina igual con ficha o sin ella; omitir emplatado deja el último tramo del proceso sin estándar |
| Preguntar más de 4 datos antes de entregar un primer borrador | Con más de 4 preguntas se bloquea el trabajo: se completa con supuestos declarados y se entrega |
| Declarar una ficha ACORDADO sin que haya pasado el pesaje real al menos una vez | Una ficha nunca pesada es una hipótesis de receta, no un estándar: va `[REQUIERE VALIDACIÓN POR PESAJE]` hasta la primera verificación |
| Calcular el coste del plato dentro de esta ficha | El coste es trabajo de `escandallo-ingenieria-menu` con la estructura real del negocio; duplicarlo aquí garantiza que las dos cifras diverjan |

**Manejo de datos faltantes — qué se asume, qué se pregunta, qué detiene:**

- Se **ASUME** sin preguntar: tolerancia de porción ±10 %, unidad de peso en
  gramos, formato de salida, y nivel de ejecutor = junior.
- Se **PREGUNTA** (máximo 4, solo si es imprescindible): país de operación ·
  nombre exacto del plato en la carta · quién ejecuta la receta a diario · si
  existe una versión previa por escrito que deba respetarse.
- **DETIENE** la ejecución solo si no hay ningún dato de ingredientes ni de
  procedimiento, ni aproximado: no hay materia prima que estandarizar y se dice,
  en vez de inventar un plato.

## Antipatrones

1. **La receta fantasma.** **Síntoma**: la ficha existe en papel o PDF, pero el
   plato que sale de cocina no se le parece — otros ingredientes, otras
   cantidades. **Causa raíz**: se escribió una vez y nunca se volvió a pesar ni a
   contrastar contra lo que se cocina hoy. **Corrección**: pesaje real como
   condición de paso a ACORDADO, y fecha de última verificación en la cabecera de
   toda ficha.

2. **El "al gusto" que se comió el food cost.** **Síntoma**: el food cost del
   plato se mueve más de 3 puntos porcentuales entre semanas sin cambio de
   proveedor. **Causa raíz**: ingredientes caros (aceite, mantequilla, especias)
   quedaron sin cantidad numérica y cada cocinero decide cuánto echa.
   **Corrección**: aplicar el paso 3 sin excepción — todo ingrediente lleva
   cantidad numérica, incluidos los variables, con su valor de partida declarado.

3. **La escala rota.** **Síntoma**: la receta multiplicada para un evento de 50
   sale distinta a la de 4 — más salada, más líquida, otra textura. **Causa
   raíz**: se multiplicaron las cantidades pero no los tiempos de reducción y
   cocción ni los ratios de sartén/producto, que no escalan linealmente.
   **Corrección**: la ficha declara qué elementos NO escalan linealmente como nota
   de escalado, además de la tabla de cantidades. Para escalar el gramaje de forma
   consistente se usa `scripts/escalar_receta.py`, que multiplica ingredientes y
   deja intactos tiempo y temperatura a propósito, devolviendo la ficha a estado
   BORRADOR para forzar la reverificación.

4. **El punto crítico invisible.** **Síntoma**: una intoxicación o un rechazo de
   inspección en un plato que "siempre se hizo así". **Causa raíz**: el paso de
   cocción de la proteína nunca tuvo temperatura numérica verificable, solo un
   criterio visual heredado de palabra. **Corrección**: aplicar el paso 6 sin
   excepción — binomio temperatura + tiempo de la tabla del país, y sonda como
   método de verificación.

5. **La ficha que nadie consulta.** **Síntoma**: la ficha existe, está bien
   escrita, y el cocinero de línea sigue haciendo el plato "como me enseñaron".
   **Causa raíz**: vive en un archivo de oficina y no en la partida, o su criterio
   de "terminado" exige instrumentos que ese puesto no tiene a mano.
   **Corrección**: redactar cada criterio con lo que el cocinero puede verificar
   en su puesto real, y declarar dónde vive físicamente la ficha (plastificada en
   la partida) como parte de la entrega, no como nota al pie.

## Casos de prueba

Los cuatro casos, con entrada real y salida esperada completa, están en `cases/`
(`case_01_happy_path.md`, `case_02_edge_case.md`, `case_03_failure.md`,
`case_04_integration.md`). Resumen:

**Happy path**: salmón a la plancha con puré y espárragos, cantidades ya en
gramos, procedimiento descrito, 4 porciones, local en España. → Ficha completa con
los 10 campos, punto crítico marcado con el binomio de AESAN para pescado
(68 °C/15 s, no el 63 °C que usaría una tabla mexicana o americana), tolerancia
±10 %, sin marcas de dato faltante.

**Edge case**: una salsa madre que entra en 6 platos distintos de la carta, con
una cantidad y un ajuste propios en cada uno. → Ficha de la salsa madre como
receta independiente con su rendimiento, más una tabla de usos derivados que
declara cuánta salsa entra en cada plato. Se resuelve como relación entre fichas,
no repitiendo la receta seis veces.

**Failure (encargo sin contexto)**: el usuario solo tiene una foto del plato y una
lista de ingredientes sin cantidades ni procedimiento. → No se rinde: entrega una
ficha BORRADOR con los ingredientes marcados `[IDENTIFICADO POR IMAGEN —
VERIFICAR]`, un procedimiento propuesto marcado como propuesto, y la lista
concreta de qué falta para pasar a ACORDADO. Lo entregado sirve como guion de la
primera prueba de cocina.

**Integration (encadenado)**: una ficha ya ACORDADA alimenta a
`escandallo-ingenieria-menu` (ingrediente + cantidad + unidad de compra) y a
`apertura-cierre-turno` (mise en place y conservación como tareas de checklist),
mediante el contrato JSON de la sección `## Salida`. Ninguna de las tres recalcula
lo que le toca a otra.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`. La versión declarada aquí, en el frontmatter, en
`metadata.json`, en `LICENSE.txt` y en el Anexo A es siempre la misma cifra: si
divergen, la entrega no sale de fábrica.
