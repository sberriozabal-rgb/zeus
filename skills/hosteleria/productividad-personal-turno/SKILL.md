---
name: productividad-personal-turno
description: Cruza el export de ventas por franja horaria con las horas trabajadas de esa misma franja y entrega un informe de productividad por turno — ventas por hora trabajada, coste de personal sobre venta sin IVA por franja y por día de la semana, euros de exceso del periodo y una escalera de entradas y salidas escalonadas en lugar de un recorte de turno completo. Úsala siempre que aparezca un cuadrante, un fichaje, un export de ventas por hora, un parte de horas o el coste de personal de un turno, o cuando alguien diga "se me come la nómina", "no sé si me sobra gente", "los lunes estamos cuatro y no entra nadie", "el turno de tarde no lo paga nadie", "cuánta gente pongo el sábado", "me planteo cerrar los lunes" o "por qué se me ha disparado el personal este mes". No la uses para calcular nóminas ni para montar el cuadrante legal con jornadas, descansos y convenio — eso es trabajo de asesoría laboral o graduado social.
license: Ver LICENSE.txt — uso comercial sin derecho de redistribución.
compatibility: Agent Skills — estándar abierto (agentskills.io). Sin dependencias de un motor concreto. El cálculo con dinero requiere Python 3.9+ para scripts/productividad_turno.py, sin librerías externas.
metadata:
  version: 1.1.0
  author: FORJA
  estado: ACORDADO
  linea: hosteleria
  peldano: P1
  revisado: '2026-08-16'
---

# Productividad de personal por turno

## Qué hace

Convierte el export de ventas por franja horaria y el parte de horas del mismo periodo en un informe de dos páginas para el dueño o el encargado, en unos 20 minutos: ventas por hora trabajada y coste de personal sobre venta sin IVA de cada franja y de cada día de la semana, los euros de exceso del periodo, qué parte de ese exceso es de horas fijas que no se pueden tocar, y una propuesta de escalonar entradas y salidas con las horas concretas que recupera.

Un modelo generalista te divide ventas entre horas y te dice que el lunes va mal: eso ya lo sabe el dueño. Lo que hace este activo es lo contrario de un promedio. Separa las horas fijas (apertura, producción, mise en place, recepción de género, limpieza, cierre y arqueo, mínimo de seguridad) de las horas variables de servicio antes de calcular ningún porcentaje, porque un informe que propone recortar la franja de las once sin saber que ahí se hace la producción del día lo desmonta el jefe de cocina en treinta segundos. Y calcula sobre el coste **total** de la hora, no sobre el salario bruto: en hostelería española las cotizaciones obligatorias del empleador son un 34,9% adicional sobre sueldos y salarios (INE, Encuesta Anual de Coste Laboral 2025, publicada 23-jul-2026), y ese diferencial es exactamente lo que separa una franja que parece aceptable de una que no lo es.

## Cuándo se dispara

- "no sé si me sobra o me falta gente"
- "se me come la nómina" / "se me ha disparado el personal este mes"
- "cuánta gente pongo el sábado" / "cuántos meto en el turno de noche"
- "los lunes estamos cuatro y no entra nadie"
- "el turno de tarde no lo paga nadie"
- "me planteo cerrar los lunes" / "¿merece la pena abrir a mediodía?"
- "tengo el export de ventas por horas del TPV, ¿qué hago con esto?"
- "quiero cuadrar los fichajes con la venta"
- "cuánto me cuesta cada hora de verdad"
- "el mes cierra bien pero no me llega el dinero"
- "voy a recortar un turno entero, dime si me equivoco"
- "cuántas ventas por hora trabajada estoy haciendo"
- jerga del gremio: "cuadrante", "fichaje", "parte de horas", "escandallo de personal", "prime cost", "franja", "pico y valle", "mise en place", "mínimo de seguridad", "hora punta"

## Quién lo ejecuta

El dueño o el encargado general de un local independiente de 1 a 3 unidades, fuera de servicio, el día que escribe el cuadrante de la semana siguiente: entre 20 y 30 minutos reales de atención, con el TPV abierto en otra pestaña y la conversación con el jefe de cocina pendiente. No es analista y no lee tablas de 40 filas. La salida completa no pasa de **90 líneas**: el mapa de franjas, el de la semana, el reparto fijas/variables, la escalera y lo que no se sabe. Si un bloque no cabe, se recorta el detalle, nunca la sección de "lo que no sé".

## Entrada

- **Ventas por franja horaria, sin IVA** (export del TPV: fecha, franja, importe) — es el dato obligatorio. Si el export viene con IVA, se pide el tipo aplicado y se descuenta antes de calcular nada; si no se conoce, se calcula igual y se marca en la cabecera del informe que los porcentajes de coste están inflados por el IVA incluido.
- **Horas trabajadas de esa misma franja** (fichajes, parte de horas o cuadrante ejecutado) — dato obligatorio. Sin ventas y horas del mismo periodo no hay productividad: hay facturación, que es otra cosa, y el activo se detiene y lo dice.
- **Coste total de la hora** (bruto + cotizaciones del empleador + vacaciones + pagas + indemnización devengada) — si el cliente no lo tiene, se usa el factor país de `references/coste-hora-por-pais.md`, se declara como estimación en el informe y se recalcula cuando llegue el dato de su asesoría. Nunca se usa el salario bruto a secas.
- **Comensales o tickets por franja** — si falta, se calcula sin la tercera cifra de control y se avisa: sin venta por comensal no se puede distinguir una mejora de productividad de un servicio corto de personal.
- **Contenido de trabajo de cada franja** (qué se hace ahí: producción, recepción de género, limpieza, servicio) — si falta, ninguna franja se clasifica como variable: todas se marcan `[contenido de trabajo desconocido]` y ninguna propuesta de ajuste sale sin esa pregunta contestada.
- **Periodo y anomalías** (festivos, obras, vacaciones, evento puntual, baja sin cubrir) — si el cliente no las menciona, se pregunta una vez; si no responde, se declara que el periodo se ha tratado como representativo.
- **Dato sucio típico**: llega un CSV del TPV con dos líneas de cabecera de marketing antes de la tabla, separador de punto y coma, importes con coma decimal y punto de millar entre comillas, columnas en inglés (`Sales`, `Labor Hours`, `Covers`), franjas escritas de seis maneras (`13:00`, `13-14h`, `13:00-14:00`) y algunas filas vacías o negativas por devoluciones; y por otro lado el parte de horas dictado de memoria ("de lunes a jueves somos tres al mediodía"). El script normaliza separador, cabecera enterrada, coma decimal, alias de columna y formatos de hora y fecha, descarta las filas sin ventas o sin horas contándolas en un aviso, y nunca elimina en silencio una franja que el cliente mencionó: si no es legible, aparece listada como descartada con su motivo.

## Umbral que sostiene el producto

**1 · La hora no cuesta el bruto.** En hostelería española, por trabajador y año: coste laboral bruto 23.690,02 €, sueldos y salarios 17.190,75 €, cotizaciones obligatorias del empleador 6.003,78 € y otros costes 495,49 € (INE, Encuesta Anual de Coste Laboral 2025, nota de prensa de 23-jul-2026, sector Hostelería). Es decir: **las cotizaciones son un +34,9% sobre el bruto y el coste total un +37,8%**. Los tipos vigentes que lo componen: contingencias comunes 23,60% y MEI 0,75% a cargo de la empresa (Orden PJC/297/2026, de 30 de marzo, BOE-A-2026-7296), más desempleo, FOGASA y formación profesional según los presupuestos vigentes `[A VALIDAR con la asesoría del cliente]`. En México el equivalente se compone de cuotas patronales IMSS por ramo, INFONAVIT 5% y retiro 2% sobre el salario base de cotización más el impuesto sobre nóminas estatal (2%–3% según estado): factor de coste patronal habitual 1,25–1,35 `[A VALIDAR con contador mexicano]`. Quien calcula con el bruto se equivoca por más de un tercio y siempre a la baja.

**2 · El coste de personal se juzga sobre venta sin IVA y por franja, nunca por mes.** Referencia externa verificada: mediana de salarios y beneficios sobre ventas de **36,5% en restaurante de servicio completo y 31,7% en servicio limitado** (National Restaurant Association, *2025 Restaurant Operations Data Abstract*, más de 900 operadores de EE. UU., datos de 2024, publicado 27-ago-2025). No es un objetivo español ni mexicano: es la referencia de encuadre. El objetivo por defecto de esta skill es 30% y **se calibra contra el histórico del propio local** `[A VALIDAR por local]`. Tabla de lectura por franja: por debajo del 15%, sospecha de falta de mano — comprueba esperas y venta por comensal antes de celebrarlo; 15–30%, rango de trabajo; 30–40%, atención, mira qué horas fijas contiene; por encima del 40%, la franja no se paga y hay que saber qué se hace ahí antes de decidir.

**3 · Ventas por hora trabajada.** Rangos de oficio de referencia: 50–80 USD/hora en servicio completo, 80–120 en fast-casual, 100–150+ en servicio rápido (7shifts, guía de *sales per labor hour*, **sin fuente primaria ni muestra declarada** — se usa solo para ordenar la conversación, `[A VALIDAR]`). La cifra que vale es la del propio local contra su histórico, no contra esta tabla.

**4 · El coste de equivocarse.** Rotación media en restauración **79,6% anual**, y reponer una baja cuesta **1.056 USD en sala, 1.491 USD en cocina y 2.611 USD en un puesto de encargado** (7shifts, encuesta a 511 operadores de restaurante de EE. UU.). Antes de proponer un recorte de X euros al mes hay que comprobar que X supera con holgura las bajas evitables que puede provocar. Un ahorro que produce dos bajas no es un ahorro: es un intercambio con pérdida.

Todas las cifras de dinero del informe se calculan con `scripts/productividad_turno.py`. **Estimar a ojo un porcentaje de coste de personal está prohibido**: es el error que rompe la confianza del cliente en la primera reunión, porque él sí tiene el dato exacto.

## Procedimiento

1. **Entrada: export de ventas y parte de horas → Acción: comprobar que ambos cubren el mismo periodo y las mismas franjas, y que las ventas están sin IVA → Salida: periodo declarado en la cabecera del informe con su número de días → Si falta el dato: recortar al periodo solapado, decir cuántos días se han quedado fuera y, si el IVA no se puede descontar, marcar todos los porcentajes como inflados.**

2. **Entrada: coste de la hora → Acción: usar el coste total del cliente; si no lo tiene, aplicar el factor país de `references/coste-hora-por-pais.md` sobre el bruto y marcarlo → Salida: valor de `--coste-hora` con su origen declarado (real del cliente o estimado) → Si falta el dato: nunca usar el salario bruto sin factor; el informe sale con la etiqueta `[coste hora estimado, a validar]` en cada cifra de euros.**

3. **Entrada: contenido de trabajo de cada franja → Acción: clasificar cada franja como FIJA (apertura, producción y mise en place, recepción de género, limpieza profunda, cierre y arqueo, mínimo de seguridad) o VARIABLE de servicio, según la lista de `references/umbrales-productividad.md` → Salida: cada franja etiquetada, y las fijas excluidas de cualquier propuesta de ajuste → Si falta el dato: etiquetar todas como `[contenido desconocido]` y no proponer ningún ajuste hasta que el cliente conteste.**

4. **Entrada: archivo normalizado → Acción: ejecutar `python3 scripts/productividad_turno.py <archivo> --modo franjas --coste-hora <valor> --dias-periodo <n>` → Salida: ventas por hora trabajada, coste de personal y venta por comensal de cada franja, franjas marcadas por encima del 40% y exceso total en euros del periodo → Si falta el dato: si no hay franja horaria legible, detenerse y pedirla; el mes es exactamente lo que esconde el problema.**

5. **Entrada: mismo archivo con fecha → Acción: ejecutar `--modo semana` y comparar el día más caro con el más rentable → Salida: qué día está abierto con el cuadrante del día bueno → Si falta el dato: omitir el mapa de la semana y decirlo en el informe, no rellenarlo con el promedio.**

6. **Entrada: curva de venta por franja y horas actuales → Acción: ejecutar `--modo escalera` y traducir las horas objetivo a movimientos concretos de entrada y salida, en el orden de la tabla de `references/umbrales-productividad.md` (escalonar entradas 30 min → escalonar salidas 30-45 min → mover una persona de turno → recortar turno → cerrar un día), sin reducir personal en ninguna franja de pico → Salida: escalera propuesta con horas recuperadas y su valor en euros, por franja y puesto, nunca por persona → Si falta el dato: proponer solo el escalonamiento de entradas, que es el movimiento de menor riesgo.**

7. **Entrada: ahorro propuesto → Acción: contrastarlo con el coste de rotación de las bajas que puede provocar (1.056–2.611 USD por baja, 7shifts) y con la venta por comensal de las franjas afectadas → Salida: propuesta confirmada, o rebajada a escalonamiento si el ahorro no supera con holgura ese coste → Si falta el dato: declarar que la comprobación no se ha podido hacer y marcar la propuesta como provisional.**

8. **Entrada: informe completo → Acción: pasar la lista de "Verificación antes de entregar" punto por punto → Salida: informe entregable con su sección de supuestos → Si falla algún punto: no se entrega; se corrige o se declara el hueco en `Lo que no sé`.**

## Salida

```markdown
# Productividad de personal por turno — [nombre del local]
Periodo: [fecha inicio] a [fecha fin] ([n] días) · Ventas sin IVA · Coste hora usado: [x,xx] € ([real del cliente / estimado, a validar])

## 1 · El titular
Media global [xx,xx] €/hora trabajada y [xx,x]% de coste de personal. [n] franjas por
encima del [umbral]%, que suman [x.xxx] € de exceso en [n] días ([x.xxx] €/año extrapolado).

## 2 · Mapa de franjas
| Franja | Ventas | Horas | €/hora | % personal | € por comensal | Tipo | Marca |
|---|---|---|---|---|---|---|---|
| [hh:00-hh:00] | [x.xxx,xx] € | [x,x] | [xx,xx] € | [xx,x]% | [xx,xx] € | [FIJA/VARIABLE/desconocido] | [sobra plantilla / ¿falta mano? / —] |

## 3 · Mapa de la semana
| Día | Ventas | Horas | €/hora | % personal | € por comensal | Lectura |
|---|---|---|---|---|---|---|
| [lunes] | [x.xxx,xx] € | [x,x] | [xx,xx] € | [xx,x]% | [xx,xx] € | [abierto con el cuadrante del sábado / correcto] |

## 4 · Fijas contra variables
- Horas fijas del periodo: [x,x] h ([x.xxx] €) — [qué se hace: producción, recepción, cierre]. No se tocan.
- Horas variables de servicio: [x,x] h ([x.xxx] €) — sobre estas se decide.
- Exceso atribuible a horas variables: [x.xxx] € de los [x.xxx] € totales.

## 5 · La escalera propuesta
| Movimiento | Franja | Puesto | Horas/semana recuperadas | € /mes | Riesgo |
|---|---|---|---|---|---|
| [Escalonar entrada 30 min] | [hh:00] | [sala/cocina] | [x,x] | [xxx] € | [bajo/medio/alto] |
Total recuperable: [x,x] h/semana ≈ [xxx] €/mes. Ninguna franja de pico pierde personal.
Contraste con rotación: [xxx] €/mes frente a [1.056-2.611 USD] por baja evitable (7shifts).

## 6 · Lo que no sé
- [franjas con contenido de trabajo desconocido]
- [coste hora estimado / periodo con festivo o baja / falta de comensales]

## Supuestos de esta versión
- [una línea por supuesto: origen del coste hora, IVA, representatividad del periodo, objetivo de % usado]
```

Longitud máxima: 90 líneas. Si se supera, se recorta el detalle del mapa de franjas agrupando por turno (mediodía / tarde / noche) y se mantienen íntegras las secciones 4, 5 y 6; nunca se entrega un informe sin `Lo que no sé`.

## Verificación antes de entregar

1. Ventas y horas cubren **exactamente el mismo periodo y las mismas franjas**, y las ventas son sin IVA (o el informe lo declara).
2. El coste hora usado es el total con cargas, o está etiquetado como estimación con su factor país.
3. Las horas fijas están identificadas y excluidas de toda propuesta de ajuste.
4. Ninguna franja con menos de 5 horas acumuladas se usa para concluir nada.
5. El exceso total cuadra con la suma de los excesos por franja (lo comprueba `--autotest`).
6. La escalera no reduce personal en ninguna franja de pico.
7. El informe no contiene ningún nombre propio: franjas y puestos.
8. Toda cifra de euros del informe procede del script, ninguna está estimada a ojo.

## Límites

- **No calcula el cuadrante legal ni sustituye a asesoría laboral.** No interpreta convenio colectivo, no valida jornada máxima, descansos entre jornadas, festivos, horas complementarias ni registro horario. Toda modificación de jornada, horario o turno se valida con **asesoría laboral o graduado social (España)** o con **abogado laboral (México)** y, donde exista, con la representación legal de los trabajadores. Este informe prepara la decisión; no la autoriza.
- No calcula nóminas, finiquitos, indemnizaciones ni cotizaciones. Los factores de coste hora son de gestión, no de nómina.
- No propone despidos ni evalúa a personas. Trabaja con franjas y puestos. Si el encargo pide señalar a alguien, queda fuera de alcance y se dice.
- No sustituye conocer el local: sin saber qué se hace en cada franja, los porcentajes engañan y el informe lo declara en vez de rellenar el hueco.
- Un periodo con festivos, obras, vacaciones, evento puntual o una baja sin cubrir no es representativo: se excluye o se declara distorsionado.
- No mide calidad de servicio. Si la venta por comensal cae mientras las ventas por hora suben, la conclusión es la contraria a la que sugieren los números.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Calcular sobre el coste total de la hora, con cargas | En hostelería española las cotizaciones del empleador son un +34,9% sobre el bruto (INE, EACL 2025): con el bruto el problema se subestima en más de un tercio |
| Expresar los porcentajes de coste sobre venta sin IVA y decirlo | Un porcentaje sobre venta con IVA sale entre 2 y 4 puntos por debajo del real y el cliente decide con un número falso |
| Separar horas fijas de horas variables antes de calcular ningún porcentaje | Proponer recortar la franja de producción es lo que hace que el jefe de cocina desmonte el informe delante del dueño |
| Mirar la franja primero, luego el día, nunca el mes | El mes promedia y consuela: un 33% mensual puede esconder cuatro franjas por encima del 85% |
| Ejecutar todo cálculo con dinero con `scripts/productividad_turno.py` | Una cifra estimada a ojo frente a un cliente que tiene el dato exacto quema la venta entera |
| Dar las tres cifras juntas: €/hora, % de personal y € por comensal | Con solo las dos primeras, un servicio corto de personal parece una mejora de productividad |
| Declarar si el coste hora es real del cliente o estimado | El cliente necesita saber qué parte del informe es suya y qué parte es una referencia externa |
| Proponer escalonar entradas y salidas antes que recortar un turno | El recorte quita horas del valle y del pico a la vez, rompe el servicio y genera rotación al 79,6% sectorial (7shifts) |
| Contrastar el ahorro propuesto contra el coste de reposición de una baja | Reponer una baja cuesta 1.056–2.611 USD (7shifts, n=511): un ahorro menor que eso es un intercambio con pérdida |
| Escribir la escalera por franja y puesto, nunca por persona | Un informe con nombres propios se convierte en un expediente laboral y deja de ser una herramienta de gestión |
| Marcar como no concluyente toda franja con menos de 5 horas acumuladas | Con muestra corta el porcentaje oscila tanto que sugiere ajustes que no existen |
| Declarar el periodo y sus anomalías en la cabecera | Un agosto con obras o una baja sin cubrir distorsiona todo y quien lea el informe en octubre no lo recordará |

| NUNCA | Porqué |
|---|---|
| Usar el salario bruto como coste de la hora | Es el error más frecuente del sector y siempre subestima el problema, entre un 25% y un 38% según país y convenio |
| Concluir nada a partir del porcentaje mensual de coste de personal | Es exactamente el promedio que oculta las franjas que no se pagan solas |
| Proponer recortar personal en una franja de pico | Se paga en tiempo de espera, en venta por comensal y en reseña, y no se recupera con la hora ahorrada |
| Tocar una franja de contenido de trabajo desconocido | Detrás de una franja "vacía" suele haber producción, recepción de género o cierre de caja |
| Bajar del mínimo de seguridad | Nadie abre ni cierra un local solo, y una cocina de una persona no aguanta un pico imprevisto ni un accidente |
| Presentar el análisis como un cuadrante legal o como instrucción laboral | Jornada, descansos y convenio son materia de graduado social o abogado laboral; confundirlo expone al cliente |
| Incluir nombres propios o valorar a personas concretas | El activo analiza franjas; señalar a alguien lo convierte en otra cosa y en un riesgo para el cliente |
| Estimar a ojo un porcentaje de coste o un ahorro en euros | Toda cifra de dinero sale del script; una cifra huérfana no se puede defender cuando el cliente pregunta de dónde sale |
| Anualizar el exceso sin declarar los días del periodo usados | Extrapolar 28 días a 365 sin decirlo convierte una referencia en una promesa falsa |
| Comparar el local contra la mediana estadounidense como si fuera su objetivo | El 36,5% de la NRA es referencia de encuadre de EE. UU., no un objetivo para un local español o mexicano |
| Concluir "cierra el lunes" antes de comprobar el cuadrante del lunes | Casi siempre el problema no es el día abierto, sino abrirlo con la plantilla del sábado |
| Entregar el informe sin la sección `Lo que no sé` | Un informe sin huecos declarados se lee como certeza y la primera cifra que falle arrastra a las demás |

## Antipatrones

1. **Síntoma**: el informe concluye que el local está en un 33% de coste de personal y no propone nada, mientras el dueño sigue sin llegar a fin de mes. **Causa raíz**: se calculó el porcentaje mensual agregado en vez de por franja. **Corrección**: ejecutar `--modo franjas` y ordenar por exceso en euros; el mes solo se usa para la cabecera.

2. **Síntoma**: la propuesta de ajuste señala la franja de 10:00-12:00 como la más cara y el jefe de cocina la tumba en la reunión. **Causa raíz**: esa franja es producción y mise en place, no servicio, y se clasificó como variable sin preguntar el contenido de trabajo. **Corrección**: etiquetar cada franja FIJA/VARIABLE antes de calcular y excluir las fijas de toda propuesta.

3. **Síntoma**: las ventas por hora trabajada suben un 12% tras el ajuste y en el trimestre siguiente caen el ticket medio y la puntuación de reseñas. **Causa raíz**: se recortó personal en franjas de pico y se leyó la productividad sin la tercera cifra, la venta por comensal. **Corrección**: bloquear cualquier reducción en franjas de pico y exigir la venta por comensal en el mapa de franjas.

4. **Síntoma**: el ahorro calculado son 380 €/mes y en dos meses se van dos personas del turno afectado. **Causa raíz**: se cambió el cuadrante sin contrastar el ahorro contra el coste de reposición ni explicar el cambio al equipo, y un cuadrante que cambia sin explicación se lee como recorte. **Corrección**: aplicar el paso 7 del procedimiento y entregar el guion de presentación al equipo de `references/umbrales-productividad.md`. `[DERIVADO, NO OBSERVADO EN CAMPO]`

5. **Síntoma**: los porcentajes del informe salen dos o tres puntos por debajo de los que maneja la gestoría del cliente y este deja de fiarse del resto. **Causa raíz**: las ventas del export venían con IVA incluido, o el coste hora usado era el bruto sin cargas. **Corrección**: comprobar IVA y factor de coste hora en los pasos 1 y 2 antes de ejecutar nada, y declarar el origen de ambos en la cabecera.

## Casos de prueba

**Happy path**: export del TPV de 28 días con fecha, franja, ventas sin IVA, horas y comensales; el dueño aporta coste hora total de 14,50 € y explica que de 11:00 a 12:00 se hace producción. → Informe completo: media 48,55 €/hora y 29,9% de coste de personal, cuatro franjas por encima del 40% con 2.927,82 € de exceso en el periodo, la franja de producción etiquetada FIJA y fuera de la propuesta, y una escalera de entradas con las horas recuperadas por franja. Ver `cases/case_01_happy_path.md`.

**Edge case**: local de dos personas con turno partido, sin fichajes digitales y con las horas dictadas de memoria, sin comensales por franja y con dos semanas de obras dentro del periodo. → No se fuerza la plantilla: se calcula con las horas declaradas, se excluyen los días de obra del cálculo y se listan aparte, se omite la columna de venta por comensal advirtiendo qué conclusión no se puede sacar sin ella, y se propone únicamente escalonar la entrada del segundo turno porque con mínimo de seguridad de dos personas no hay más margen. Ver `cases/case_02_edge_case.md`.

**Failure (encargo de una línea sin contexto)**: "dime si me sobra gente". → No se rinde ni pide todos los datos antes de producir. Entrega la plantilla de recogida (`assets/plantilla-turnos.csv`), el método de las tres cifras, la tabla de lectura por franja y el factor de coste hora del país, con un ejemplo numérico marcado como ilustrativo, y cierra con la única pregunta bloqueante: "pásame ventas por franja y horas del mismo periodo, aunque sean cuatro semanas a mano, y te lo calculo". Ver `cases/case_03_failure.md`.

**Integration (encadenado con otro activo)**: `escandallo-ingenieria-menu` ha dejado el coste de materia prima en el 34% de la venta sin IVA y el dueño pregunta por qué sigue sin ganar dinero. → Esta skill calcula el coste de personal del mismo periodo, suma el prime cost y devuelve el reparto entre las dos partidas; si el personal está dentro de rango y el prime cost sigue disparado, lo dice y devuelve el trabajo a la otra skill en vez de apretar más al equipo. La escalera resultante se cruza con `apertura-cierre-turno` para colocar las tareas fijas de apertura y cierre en las franjas que la escalera deja cubiertas. Ver `cases/case_04_integration.md`.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
