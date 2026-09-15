---
name: escandallo-ingenieria-menu
description: >-
  Calcula el escandallo real de una carta de restaurante y aplica ingeniería de menú para
  señalar qué platos se están comiendo el margen y qué hacer con cada uno. Úsala siempre
  que aparezca una carta, un listado de platos, un escalandallo, un export del POS o una
  hoja de ventas por producto, o cuando alguien pregunte cuánto le cuesta un plato, qué
  precio poner, por qué no le cuadra la comida, por qué baja el margen, si conviene subir
  precios, qué platos quitar de la carta, cómo calcular el food cost o el prime cost,
  cuánto rinde un producto después de limpiarlo, o pida un análisis de rentabilidad de la
  carta, un cambio de carta o una revisión de precios. Aplica también con frases
  informales del oficio como "me está comiendo el margen", "no me salen las cuentas de la
  comida", "este plato lo hago casi regalado", "el pescado se ha puesto imposible" o
  "quiero quitar platos". No la uses para carta de vinos con rotación de bodega ni para
  contabilidad fiscal.
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso comercial sin derecho de redistribución. Ver LICENSE.txt.
compatibility: Requiere Python 3.9+ para ejecutar scripts/escandallo.py. Sin dependencias externas.
metadata:
  version: "1.1.1"
  sector: "hosteleria-restauracion"
  entregable: "informe-ingenieria-menu"
---

# Escandallo e ingeniería de menú

## Qué hace

Convierte una carta con precios, un export de ventas por plato del POS y las recetas con gramajes en un informe que dice, plato por plato, cuánto cuesta de verdad, cuántos euros de margen deja cada unidad vendida, en qué cuadrante de la matriz de Kasavana-Smith cae, y qué hacer con él el lunes: proteger, bajar coste, trabajar la venta o retirar. Cierra en una cifra: los euros al año que valen las acciones recomendadas.

Esto no es una tabla de costes que cualquier hoja de cálculo produce. Un escandallo hecho con el precio del albarán por los gramos de la receta está mal por construcción: le faltan tres capas —rendimiento tras limpieza, merma de cocción y costes que nadie imputa (pan y aceite de mesa, fondos, aceite de fritura, envase de reparto)— que en conjunto mueven el coste del plato varios puntos enteros. En la carta de prueba de esta skill, la merluza pasa de 11,4% de food cost a 30,4% con solo aplicar rendimiento (52%) y merma de plancha (18%): tres veces más coste, la misma receta. Y la decisión final no se toma con el porcentaje, sino con el margen de contribución en euros, porque el banco cobra en euros.

## Cuándo se dispara

- "cuánto me cuesta este plato"
- "hazme el escandallo de la carta" / "necesito los escalandallos"
- "no me salen las cuentas de la comida"
- "me está comiendo el margen"
- "este plato lo hago casi regalado"
- "el pescado se ha puesto imposible y no sé si subir el precio"
- "quiero quitar platos de la carta" / "voy a cambiar la carta"
- "qué precio le pongo al arroz"
- "por qué me baja el margen si vendo lo mismo"
- "te paso el export del TPV con las ventas por producto"
- "cuánto rinde una merluza después de limpiarla"
- "me cuadra el food cost en el papel y no en el banco"
- jerga del gremio: "escandallo", "food cost", "prime cost", "ficha técnica", "gramaje", "rendimiento", "merma", "mise en place", "ratio de materia prima", "TPV/POS", "familia", "ticket medio"

## Quién lo ejecuta

El dueño o el gerente de un local independiente, o el jefe de cocina con responsabilidad de compras. Nunca en servicio: esto se ejecuta fuera de horario o en la mañana de un lunes de cierre, con 45 a 90 minutos de margen real y los papeles delante (albaranes, export del POS, recetario). La presión no es de tiempo, es de credibilidad: quien lee este informe conoce sus números mejor que quien lo escribe, y detecta un error aritmético o un gramaje inventado en la primera página. Por eso todo cálculo con dinero pasa por `scripts/escandallo.py` y todo hueco se declara en vez de rellenarse.

## Las cuatro decisiones de oficio que separan esto de una hoja de cálculo

Se aplican a todo informe, sin excepción.

**1 · Antes de tocar recetas, se contrasta teórico contra real.** Teórico = suma de (coste de receta × unidades vendidas) ÷ ventas netas. Real = (inventario inicial + compras − inventario final) ÷ ventas netas. La distancia entre ambos se llama desviación, y decide si el problema está en la carta o en la cocina: son problemas opuestos con soluciones opuestas. Subir precios con una desviación de 6 puntos tapa el agujero un mes.

**2 · Se decide con margen de contribución en euros, no con porcentaje.** Un arroz al 38% de food cost que deja 14 € de margen es mejor negocio que una ensalada al 22% que deja 4,50 €. Quien gestiona por porcentaje quita el arroz y llena la carta de ensaladas: acaba con la carta más "eficiente" del barrio y sin caja. El porcentaje solo se usa para dos cosas: detectar coste desbocado (>45%) y comparar familias entre sí.

**3 · La matriz cruza popularidad contra margen, cada plato contra su propia carta.** Popularidad = unidades del plato ÷ unidades totales de su familia, contra el umbral del 70% de la cuota media (regla de Kasavana-Smith, ver `## Umbral`). Margen = euros por unidad contra el margen medio ponderado de la carta.

| | Margen alto | Margen bajo |
|---|---|---|
| **Popular** | **ESTRELLA** — protege calidad y disponibilidad | **CABALLO DE BATALLA** — baja el coste antes de subir el precio |
| **Impopular** | **ROMPECABEZAS** — trabaja la venta, mide a 2 semanas | **PERRO** — decide: rediseñar o retirar |

Orden de ataque en un caballo de batalla, y en este orden: (1) rendimiento y porcionado, (2) sustitución parcial de un ingrediente que no se note en boca, (3) rediseño del emplatado para reducir guarnición cara, (4) subida de precio, y solo al final. Un perro no se retira sin comprobar tres cosas: si es ancla de un tipo de cliente que trae mesa (el filete del que no come nada raro, la opción infantil, la sin gluten), si comparte producto con una estrella, o si es marcador de precio. Una carta sin ningún perro no es señal de buena gestión: suele ser una carta corta y sin ganchos.

**4 · Dos o tres precios de la carta son intocables.** El plato más conocido, la copa de vino de la casa y el café son los precios con los que el cliente decide si el sitio es caro. Subirlos mueve la percepción de precio de todo el local más que su aportación al margen. Se identifican preguntando al dueño y a sala —no se deducen de la hoja— y se marcan como intocables en el informe. Cuando toque subir: dos ajustes pequeños al año antes que uno grande, y sin cruzar de golpe una barrera psicológica (de 18 a 22 se nota; de 18 a 19,50 y luego a 21, no).

## Entrada

Lo que el usuario aporta, en cualquier combinación, y lo que se hace si falta:

- **Carta con precios de venta** (con IVA incluido, que es como está escrita) y el tipo de IVA aplicable — sin esto no hay análisis. Si falta el tipo de IVA, se usa 10% en España (tipo reducido de hostelería) o 16% en México, se declara el supuesto y se avisa de que un error de tipo mueve el food cost casi seis puntos.
- **Ventas por plato del periodo** (export del POS, número de unidades) — si falta, se calculan costes y márgenes unitarios pero **no** se clasifica la matriz, porque sin unidades no hay eje de popularidad. Se dice en el informe en vez de repartir ventas a ojo.
- **Recetas con gramajes** por plato — si faltan las de algunos platos, se analizan solo los que sí las tienen y se lista aparte qué platos quedaron fuera. Nunca se estima un gramaje que el cliente no ha dado.
- **Precios de compra** por kg/L/ud de cada ingrediente (albarán, sin IVA) — si falta el de un ingrediente, ese plato queda fuera del cálculo y se declara; un precio inventado contamina el margen de toda la carta.
- **Rendimientos medidos en esa cocina** (cuánto queda de una merluza tras limpiarla) — si faltan, se usan los rangos orientativos de `references/rendimientos-y-umbrales.md`, se marca cada plato afectado como **estimado** y se pide medir los tres productos de más peso en compra.
- **Inventario inicial, compras e inventario final del periodo** (para el food cost real) — si faltan, el informe sale sobre teórico y arranca declarando "análisis sin contraste": el script ya imprime ese aviso, y no se sustituye por una desviación supuesta.
- **Qué platos son intocables** (marcadores de precio y anclas de cliente) — si el cliente no lo dice, se pregunta una vez; si no hay respuesta, no se marca ninguno y se advierte de que subir precio a ciegas puede tocar un marcador.
- **Dato sucio típico**: el export del POS trae platos retirados con 0 ventas, botones que agrupan varios platos bajo un mismo nombre, y precios de carta pegados con IVA mezclado (unos con y otros sin). La skill no descarta ninguna línea en silencio: calcula lo que puede, marca cada anomalía con su bandera (`0 ventas: comprueba si es un botón muerto del POS`, `food cost < 10%: falta un ingrediente`, `coste > precio de venta`) y las lleva al apartado 6 del informe. Un plato con datos raros es una pregunta al cliente, no un plato eliminado.

## Umbral que sostiene el producto

**El umbral de popularidad no es la media: es el 70% de la media.** Con una carta de 10 platos en una familia, la cuota media es del 10% y el umbral de popularidad es 7%. Por debajo, el plato es impopular. Es la regla de Kasavana & Smith (*Menu Engineering: A Practical Guide to Menu Analysis*, Okemos MI, 1982), replicada en literatura académica revisada: la fórmula publicada es `(100 / nº de platos) × 70%` (Deturope, vol. 14 nº1, 2022, aplicación sobre una carta real húngara 2016-2019 — ver `references/FUENTES.md`). Un aficionado clasifica contra la media y sentencia como impopular a un plato que está a un punto de ella; con el 70% el cuadrante deja de moverse cada mes por ruido de ventas.

**La desviación teórico-real es el semáforo que decide si el problema es la carta o la cocina:**

| Desviación | Qué significa | Qué hacer |
|---|---|---|
| ≤ 2 puntos | La cocina ejecuta lo que dice la receta. | Sigue con el análisis de carta. |
| 3 a 5 puntos | Porcionado descontrolado o mermas altas. | Analiza la carta, pero avisa: parte del problema no se arregla con precios. |
| > 5 puntos | El problema no es la carta: es control (porciones, mermas, roturas, invitaciones sin registrar, sustracción). | Dilo antes que nada. Subir precios aquí tapa el agujero un mes. |

Contraste con las fuentes disponibles: los operadores de referencia trabajan con desviaciones "en el entorno del 1% o menos" (Restaurant365, 2025) y un jefe de cocina que midió cinco locales durante 12 meses observó 1 punto en formato bocadillería y 1,5-2 puntos en pescado fresco de gama alta, declarando explícitamente que no existe un umbral universal publicado (Chefs Resources, David Buchanan). Es decir: **la banda de 3 a 5 puntos de esta skill ya es generosa, y el corte en 5 es criterio de oficio, no dato publicado** — va marcado `[A VALIDAR]` hasta que se contraste con datos de tres clientes instalados.

**La cifra que un aficionado no conoce: el rendimiento.** El coste real de materia prima es `precio_compra ÷ rendimiento`, y luego se revierte la merma de cocción. Ejecutado sobre la carta de prueba de esta skill (`assets/plantilla-datos.json`, reproducible con el script): la merluza a la plancha con rendimiento 52% y merma de plancha 18% cuesta 6,37 € y da 30,4% de food cost; la misma receta, mismo precio de albarán, sin aplicar ninguna de las dos capas, cuesta 2,38 € y da 11,4%. Diecinueve puntos de food cost de diferencia en un solo plato, y el segundo número es el que sale de la mayoría de las hojas de Excel del sector. Los factores por producto están en `references/rendimientos-y-umbrales.md` y siempre ceden ante el rendimiento medido en esa cocina.

Los rangos de food cost sano por tipología (25-30% QSR, 28-35% casual, 35-42% cocina de producto) proceden de guías sectoriales sin metodología publicada y van marcados `[A VALIDAR]` en `references/FUENTES.md`: se usan como referencia de conversación, nunca como sentencia sobre un plato.

## Procedimiento

1. **Entrada: carta, ventas y datos de inventario → Acción: calcular food cost teórico y real y su desviación, y clasificarla en la tabla de tres bandas → Salida: una línea de diagnóstico que dice si el problema es de carta o de control → Si falta el dato: sin inventarios se trabaja sobre teórico y el informe abre con "análisis sin contraste", que es lo que imprime el script.**

2. **Entrada: precios de carta → Acción: pasarlos a base imponible con el tipo de IVA del país y del servicio → Salida: precio neto por plato → Si falta el dato: usar 10% (España) o 16% (México), declararlo en supuestos y avisar de que el error de tipo desplaza el food cost casi seis puntos.**

3. **Entrada: recetas con gramajes y precios de compra → Acción: calcular el coste de cada ingrediente aplicando rendimiento de limpieza y merma de cocción con `scripts/escandallo.py`, y sumar después las capas que no están en la receta (mesa, cocción, bases, envase de reparto y merma de servicio) como porcentaje declarado por plato → Salida: coste total por plato, con el coste por kg neto de cada ingrediente visible → Si falta el rendimiento: usar el rango de `references/rendimientos-y-umbrales.md` y marcar el plato como estimado; si falta un precio de compra, dejar el plato fuera y listarlo; si faltan las capas, usar 5-8% en sala y declararlo, y en reparto no estimar sino pedir el desglose de envase y comisión de plataforma, porque cambia el signo del plato.**

4. **Entrada: coste total y precio neto → Acción: calcular margen de contribución unitario en euros y food cost porcentual → Salida: tabla plato · unidades · precio s/IVA · coste · margen € · FC% → Si falta el dato de unidades: se entrega la tabla sin las dos columnas de volumen y se dice que la matriz no se puede clasificar.**

5. **Entrada: margen unitario y unidades vendidas por familia → Acción: clasificar cada plato en la matriz contra el umbral de popularidad del 70% de la cuota media y contra el margen medio ponderado → Salida: cada plato con su cuadrante → Si la familia tiene menos de 3 platos: el script lo avisa y el cuadrante se interpreta con reserva o se agrupan familias.**

6. **Entrada: cuadrante de cada plato → Acción: asignar la acción de su cuadrante siguiendo el orden de ataque (en caballo de batalla: rendimiento y porcionado antes que precio) → Salida: acción por plato con su euro anual, calculada extrapolando el ritmo de venta del periodo → Si falta el dato: si el periodo es de un mes, se dice que la anualización extrapola un mes y no una temporada completa.**

7. **Entrada: lista de platos y criterio del dueño y de sala → Acción: marcar los intocables (marcadores de precio y anclas de cliente) → Salida: apartado 5 del informe con los platos que no se tocan y por qué → Si falta el dato: no se marca ninguno y se advierte por escrito de que subir precios sin esa lista puede tocar un marcador.**

8. **Entrada: informe montado y acciones con su valor → Acción: pasar las cinco verificaciones (IVA correcto, ningún coste por encima del precio de venta, ningún food cost por debajo del 10%, unidades cuadradas con el POS, cada acción con euros) y ordenar las acciones por impacto anual sumándolas → Salida: informe verificado —o lista de anomalías para preguntar al cliente— cerrado con "impacto estimado de las acciones: X €/año" → Si una anomalía persiste: se publica como pregunta en el apartado 6, no se corrige a ojo; y si las unidades son de un periodo corto, se declara el número de meses extrapolados junto a la cifra.**

## Salida

```markdown
# Ingeniería de menú — [Nombre del local]
[Periodo analizado] · [Nº de platos] · [Ventas netas del periodo, sin IVA]

## 1. Diagnóstico en tres líneas
Food cost teórico X% · real Y% · desviación Z puntos. [Qué significa según la tabla de bandas.]

## 2. Los cinco platos que se comen el margen
| Plato | Unidades | Precio s/IVA | Coste | Margen € | Food cost % | Cuadrante |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

## 3. La matriz completa
Los cuatro cuadrantes con sus platos.

## 4. Acciones, por orden de impacto
| # | Qué hacer | Vale al año | Cuesta hacerlo | Quién |
|---|---|---|---|---|
| 1 | ... | ... € | ... | [puesto] |

## 5. Intocables
Platos marcados como marcador de precio o ancla de cliente, y por qué.

## 6. Supuestos de esta versión y huecos de dato
- Qué se asumió (rendimientos estimados, tipo de IVA, periodo extrapolado).
- Qué platos quedaron fuera del cálculo y por qué.
- Qué anomalías hay que preguntar al cliente antes de decidir.

**Impacto estimado de las acciones: X €/año.**
```

Longitud máxima: 2 páginas más la tabla de platos. Si el informe pasa de ahí, es que la carta necesita analizarse por familias en entregas separadas (sala y reparto son dos cartas distintas, no una carta larga).

## Límites

- No es contabilidad ni asesoría fiscal, y no es una auditoría. Los tipos de IVA que aplica son los vigentes verificados en `references/FUENTES.md`; el tipo real de cada línea lo confirma el asesor del cliente.
- No calcula la carta de vinos con rotación de bodega ni valora existencias a efectos contables.
- No cambia precios en ningún sistema: recomienda, y la decisión de precio la firma el dueño.
- No sustituye la medición de rendimientos en esa cocina. Con rendimientos estimados el informe es una hipótesis de trabajo, y así se declara plato por plato.
- El análisis de reparto a domicilio queda fuera del informe estándar: la comisión de plataforma cambia el signo de platos rentables en sala y exige una carta analizada aparte.
- Cuando el diagnóstico apunte a sustracción o a un descuadre que implique a personas, se entrega la cifra y se deriva la decisión al dueño y, si procede, a asesoría laboral. Esta skill no acusa a nadie.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Calcular sobre base imponible, con el tipo de IVA declarado en el informe | Cruzar precio de carta con IVA contra albarán sin IVA desplaza el food cost varios puntos enteros y invalida todas las decisiones que salen detrás |
| Aplicar rendimiento de limpieza y merma de cocción a todo producto fresco | Sin las dos capas, la merluza de la carta de prueba sale a 11,4% de food cost en vez de 30,4%: el informe recomendaría proteger un plato que sangra |
| Ejecutar los cálculos con `scripts/escandallo.py`, nunca a mano | Un error aritmético delante de un dueño que conoce sus albaranes cuesta el cliente entero, y el script es reproducible ante una discusión |
| Contrastar teórico contra real antes de tocar la carta | Con desviación superior a 5 puntos el problema es de control y ninguna decisión de precio lo arregla |
| Decidir con margen de contribución en euros y usar el porcentaje solo como señal | Gestionar por porcentaje empuja a retirar los platos que más euros aportan |
| Clasificar la popularidad contra el 70% de la cuota media, no contra la media | Es la regla de Kasavana-Smith (1982): con la media pura el cuadrante de un plato cambia cada mes por ruido de ventas |
| Marcar como estimado todo plato con rendimiento no medido en esa cocina | El lector debe saber qué línea del informe es medición y cuál es hipótesis antes de retirar un plato de la carta |
| Preguntar por los intocables antes de recomendar cualquier subida de precio | Subir el café o el plato conocido mueve la percepción de precio de todo el local más de lo que aporta al margen |
| Cerrar el informe con una cifra anual de impacto y el número de meses extrapolados | Sin cifra, el informe no se ejecuta; sin el número de meses, la cifra no se puede defender cuando el cliente la revise |
| Declarar en el apartado 6 cada plato excluido del cálculo y el motivo | Un plato que desaparece sin explicación se lee como error del analista y tumba la credibilidad del resto |
| Llevar las anomalías del script (0 ventas, FC<10%, coste>precio) al informe como preguntas | Son casi siempre error de datos del cliente, y preguntarlas produce mejor dato para la siguiente iteración |

| NUNCA | Porqué |
|---|---|
| Inventar un gramaje, un rendimiento o un precio de compra que el cliente no ha dado | Un número plausible en un informe de costes es peor que un hueco: se propaga a la decisión de retirar o subir precio |
| Recomendar subir precios cuando la desviación teórico-real supera los 5 puntos | Tapa un problema de control durante un mes y el dueño vuelve con el mismo agujero y menos confianza |
| Clasificar la matriz sin unidades vendidas reales | Sin eje de popularidad los cuatro cuadrantes son decorativos y la recomendación de retirada no tiene base |
| Retirar un perro sin comprobar si es ancla de cliente, comparte producto con una estrella o marca precio | Retirar el plato ancla arrastra la mesa entera que venía por él |
| Mezclar en el mismo informe la carta de sala y la de reparto | La comisión de plataforma convierte en pérdida platos rentables en sala: mezclarlos oculta las dos realidades |
| Presentar el food cost porcentual como criterio de decisión | El porcentaje no paga nóminas; el margen de contribución en euros sí |
| Corregir a ojo una anomalía del script en vez de preguntarla | Un coste por encima del precio de venta es casi siempre un error de unidades del cliente, y adivinarlo produce un informe elegante y falso |
| Dar por buena una cifra sectorial sin marcarla como referencia sin metodología publicada | Es la cifra huérfana que el cliente pregunta y no se puede defender |
| Acusar de sustracción a partir de una desviación | La desviación tiene media docena de causas antes que esa, y una acusación sin prueba destruye la relación y expone legalmente al cliente |

## Antipatrones

1. **Síntoma**: el informe da food cost por debajo del 15% en platos de pescado o carne y todo parece sano. **Causa raíz**: se calculó con el precio del albarán por los gramos de la receta, sin rendimiento ni merma. **Corrección**: recalcular con las dos capas; en la carta de prueba de esta skill el mismo plato pasa de 11,4% a 30,4% de food cost.

2. **Síntoma**: el dueño sube precios siguiendo el informe y a los dos meses el food cost real sigue igual. **Causa raíz**: se analizó la carta con una desviación teórico-real por encima de 5 puntos, es decir con un problema de control, no de precio. **Corrección**: parar el análisis de carta en el diagnóstico y atacar porcionado, mermas, roturas e invitaciones antes de tocar ningún precio.

3. **Síntoma**: la carta queda "limpia" tras el análisis y la caja baja. **Causa raíz**: se retiraron platos por porcentaje de food cost alto en vez de por margen en euros, y se retiró un ancla de cliente. **Corrección**: reordenar las decisiones por margen de contribución y aplicar el filtro de tres preguntas antes de retirar cualquier perro.

4. **Síntoma**: el informe recomienda subir el precio del café o del plato más conocido porque el margen es bajo. **Causa raíz**: no se pidió la lista de intocables al dueño y a sala. **Corrección**: preguntar por los marcadores de precio antes de generar el apartado de acciones; si no hay respuesta, ningún marcador se toca y se declara. `[DERIVADO, NO OBSERVADO EN CAMPO]`

5. **Síntoma**: aparecen platos con cero ventas clasificados como rompecabezas y el informe recomienda trabajar su venta. **Causa raíz**: el export del POS arrastra botones de platos retirados que siguen en el sistema. **Corrección**: el script marca `0 ventas: comprueba si es un botón muerto del POS`; esa bandera va al apartado 6 como pregunta y el plato no entra en las acciones hasta que el cliente confirme.

## Casos de prueba

Los cuatro casos están escritos con su entrada y su salida real en `cases/`. Todos son reproducibles ejecutando el script; ninguno tiene cifras narradas.

**Happy path** (`cases/case_01_happy_path.md`): carta completa de 9 platos con ventas, recetas, rendimientos e inventario (`assets/plantilla-datos.json`). Sale food cost teórico 32,35%, real 36,20%, desviación 3,85 puntos —banda de aviso—, y la matriz completa con dos estrellas, dos caballos, dos rompecabezas y tres perros, incluido un bogavante con 175,2% de food cost que pierde 20,50 € por unidad servida.

**Edge case** (`cases/case_02_edge_case.md`): carta sin rendimientos declarados, sin inventarios, con un plato de 0 ventas y un café de 900 unidades. El informe sale igual, marcado "sin contraste", y las banderas del script señalan las tres anomalías (`FC<10%`, `coste>precio`, `0 ventas`) en vez de esconderlas. Es el caso que enseña cuánto cambia el resultado por olvidar el rendimiento.

**Failure** (`cases/case_03_failure.md`): "¿cuánto me cuesta el arroz de marisco?", una línea, sin ventas, sin inventario, sin IVA declarado. Se entrega el escandallo del plato con coste 9,52 €, margen 28,66 € y food cost 24,93%, más el aviso de que con un solo plato el cuadrante no es concluyente y los tres supuestos declarados. No se pide más información antes de producir.

**Integration** (`cases/case_04_integration.md`): encadenado con `comparativa-proveedores`. La subida verificada del aceite (8,50 → 9,60 €/L, +12,9%) entra como nuevo precio de compra en el escandallo y se recalcula qué platos cambian de cuadrante por la compra, no por la receta.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
