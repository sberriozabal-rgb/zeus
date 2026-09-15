---
name: comparativa-proveedores
description: >-
  Compara los precios de tus proveedores de restaurante, detecta qué productos han subido
  y cuánto, dice qué proveedor tiene hoy cada cosa más barata, y calcula cuánto margen te
  comen esas subidas en los platos de tu carta. Úsala siempre que aparezcan albaranes,
  facturas de proveedor, un export de compras o una lista de precios, o cuando alguien
  pregunte cuánto le ha subido un producto, qué proveedor le sale mejor, si le están
  clavando, por qué le sube la comida sin tocar la carta, o si compensa cambiar de
  proveedor; y cuando pida una comparativa de compras, un control de precios de proveedor
  o revisar los albaranes del mes. Aplica también con frases del oficio como "el aceite se
  ha puesto imposible", "me está subiendo todo el proveedor", "este me está clavando",
  "cuánto me ha subido el pescado", "quién me lo tiene más barato" o "me sube la comida y
  no sé por qué". No la uses para calcular el escandallo de un plato desde cero (eso es
  escandallo-ingenieria-menu) ni para carta de vinos con rotación de bodega.
license: Proprietary. Copyright 2026. All rights reserved.
compatibility: Requiere Python 3.9+ para ejecutar scripts/proveedores.py. Sin dependencias externas.
metadata:
  version: "1.1.0"
  sector: "hosteleria-restauracion"
  entregable: "informe-control-compras"
  enlaza_con: "escandallo-ingenieria-menu"
---

# Comparativa de proveedores y control de precios de compra

## Qué hace

Convierte un montón de albaranes y facturas de varios proveedores en dos entregables que
van en el mismo informe porque son el mismo trabajo: **la alerta de subidas** —qué producto
subió, cuánto, desde cuándo, y quién lo tiene hoy más barato— y **el impacto en la carta**
—qué platos se comen esa subida y cuánto margen pierden al mes. Cierra en tres o cuatro
acciones de compra, cada una con su euro anual al lado.

Esto no es restar precios. Antes de restar hay que desactivar tres trampas que hacen que la
mayoría de las comparativas de compras digan lo contrario de la verdad: unidades sin
normalizar (una garrafa de 5 L a 42,50 € es **8,50 €/L**, más barata que el litro suelto a
8,90 €, aunque el número grande asuste), IVA mezclado entre una lista de precios y un
albarán, y dos productos que no son el mismo producto. Y hay una cuarta capa que solo se ve
si se compara por unidad base: el formato encubierto, mismo precio de caja con menos gramos
dentro. En España el 54% de los consumidores dice haber notado esa práctica y el Gobierno
tramita obligar a declararla en el punto de venta (Ipsos y Ley de Consumo Sostenible, ver
`references/FUENTES.md`): al restaurante nadie se lo avisa en el albarán.

## Cuándo se dispara

- "cuánto me ha subido el aceite / el pescado / la harina"
- "este me está clavando"
- "quién me lo tiene más barato"
- "me sube la comida y no he tocado la carta"
- "me está subiendo todo el proveedor"
- "el aceite se ha puesto imposible"
- "¿compensa cambiarme de proveedor?"
- "mírame los albaranes del mes"
- "te paso las facturas de los tres proveedores"
- "me han dicho que hay otro más barato pero no sé si es lo mismo"
- "el de siempre me ha cambiado el formato de la caja"
- "necesito una comparativa de compras para negociar"
- jerga del gremio: "albarán", "escandallo de compra", "precio de lista", "precio pactado",
  "portes", "mínimo de pedido", "rappel", "lonja", "base imponible", "€/kg", "garrafa",
  "saco", "caja de X kilos", "producto de temporada"

## Quién lo ejecuta

El dueño o el gerente de compras de un local independiente, o el jefe de cocina que hace
los pedidos. El momento real es el que nadie tiene: cruzar cincuenta líneas de albarán entre
tres proveedores, cada semana, a mano. Por eso no se hace nunca y por eso el proveedor sube
de céntimo en céntimo sin que nadie lo vea. Se ejecuta fuera de servicio, con 30 a 60
minutos y la carpeta de albaranes o el export del programa de compras delante. La presión es
la misma que en toda la línea: quien lee el informe conoce sus albaranes mejor que quien lo
escribe, y una comparación mal normalizada le hace cambiar de proveedor para peor. Por eso
todo cálculo pasa por `scripts/proveedores.py` y toda línea que no se pueda normalizar se
descarta declarándolo, nunca se adivina.

## Las tres trampas que se desactivan antes de restar nada

**1 · Unidad distinta.** El proveedor A factura el aceite por garrafa de 5 L y el B por
litro suelto. 42,50 € la garrafa **no** es más caro que 8,90 € el litro: son 8,50 €/L contra
8,90 €/L y gana el A. Comparar precio de línea sin llevar todo a unidad base (€/kg, €/L,
€/ud) es la forma número uno de tomar la decisión de compra al revés. Ninguna línea se
compara hasta estar en la misma base.

**2 · IVA mezclado.** Los albaranes vienen sin IVA; las listas de precios a veces lo llevan
incluido. Un queso a 20,90 €/kg con 10% incluido son **19,00 €/kg** de base imponible:
comparado contra un albarán sin IVA, la diferencia que aparece es puro artefacto. Todo se
compara sobre base imponible. Los tipos vigentes de España y México están en
`references/familias-y-volatilidad.md` §3, con su fuente en `references/FUENTES.md`.

**3 · Producto que no es el mismo.** Aceite de oliva virgen extra no es aceite de orujo.
Merluza del Cantábrico no es merluza austral congelada. Cuando la diferencia entre dos
proveedores supera el 40-50%, la primera hipótesis no es "me están clavando": es que no son
el mismo producto. Recomendar el cambio sin verificarlo hace que el cliente reciba producto
peor en la primera entrega y no vuelva a fiarse del informe.

Y una cuarta que no es trampa del dato sino del proveedor: **el formato encubierto**. Mismo
precio de caja, menos gramos dentro. El precio de línea no cambia, el €/kg sí. Solo se ve
comparando por base, y es la subida que más agradece un dueño porque es la que él no puede
ver.

## Entrada

Lo que el usuario aporta, en cualquier combinación, y lo que se hace si falta:

- **Líneas de albarán o factura** con seis datos: producto, familia, proveedor, unidad de
  compra (y el formato real si es caja, garrafa o saco), precio y fecha. Es lo único
  imprescindible. Si falta el formato de una unidad de agregación, esa línea **se descarta y
  se declara** en el apartado 7: un peso supuesto contamina el €/kg de todo el producto.
- **Dos fechas del mismo producto y proveedor** — sin dos fechas no hay alerta de subidas.
  Si solo hay un periodo, se entrega la comparativa entre proveedores y se dice por escrito
  que la alerta de subidas queda pendiente del segundo periodo.
- **Dos proveedores del mismo producto** — sin dos proveedores no hay comparativa. Si solo
  hay uno, se entrega la alerta de subidas y se dice que la comparativa no aplica.
- **Consumo mensual por producto** (kg, L o unidades al mes) — es lo que convierte un
  porcentaje en euros. Si falta, el análisis funciona pero **el impacto sale 0 €**, que no
  significa que no cueste: significa que falta el dato. El informe lo declara con esas
  palabras y ordena por porcentaje, avisando de que ese orden no es el de prioridad real.
- **Tipo de IVA de cada línea y si el precio lo lleva incluido** — si no consta, se asume
  precio de albarán sin IVA (que es lo habitual) y se declara. Si hay sospecha de mezcla, la
  línea se marca "IVA por confirmar" en vez de descontarse a ojo: descontar un 10% donde
  tocaba 4% mueve la comparación casi seis puntos.
- **Carta o salida de `escandallo-ingenieria-menu`** (opcional) — sin ella no hay apartado 5
  (impacto en la carta) y se dice; con ella, cada subida se cruza con los platos que usan
  ese producto.
- **Dato sucio típico**: el mismo producto llamado de tres formas distintas por tres
  proveedores ("AOVE 5L", "Aceite O.V.E. garrafa", "Oliva virgen extra"), unidades de
  agregación sin peso ("1 caja"), y el mismo producto facturado una vez en kilos y otra en
  unidades. La skill agrupa por producto **a criterio, revisando el emparejamiento a ojo
  antes de fiarse de la máquina**, y las dos incoherencias que no puede resolver las expulsa
  con nombre y motivo: `Línea 2: Unidad 'caja' no es base (kg/L/ud) y falta 'formato'` ·
  `Línea 4: 'Queso curado' aparece en base 'ud' y antes en 'kg'`. Ninguna línea desaparece
  en silencio, y el informe dice cuántas se descartaron y cuántas entraron.

## Umbral que sostiene el producto

**Umbral de alerta: +8% entre dos fechas del mismo producto y proveedor.** El razonamiento
que lo defiende ante un cliente: la inflación general en España se situó en el **3,6% anual
en julio de 2026** (INE, nota de prensa del 13-ago-2026). Una subida del 8% en un producto
concreto es más del doble de la inflación general, y por tanto ya no es "todo sube": es una
decisión de ese proveedor sobre ese producto. El corte exacto en 8 es **criterio de oficio,
marcado `[A VALIDAR]`**, y es calibrable por cliente: quien compra en lonja necesita un
umbral más alto para que "alerta" siga significando algo.

**La distinción que decide la acción: estacional contra estructural.** No es lo mismo una
subida que se corrige sola que una que no vuelve a bajar, y confundirlas hace que el dueño
persiga un fantasma. Las dos referencias que lo sostienen:

- **Fruta y verdura se mueven por cosecha.** El propio INE atribuye la bajada mensual del
  0,7% de los precios de alimentos en julio de 2026 al descenso de frutas y hortalizas. Una
  merluza que pasa de 11 a 13,50 €/kg en agosto no es un proveedor que clava: es agosto.
- **El aceite de oliva sube por cosecha, pero cuando cae, cae de golpe.** Los precios en
  origen de la campaña 2024/25 cayeron un **49,4% en virgen extra** frente a la campaña
  anterior (Observatorio de Precios y Mercados de la Junta de Andalucía, dic-2025). Es la
  familia que obliga a revisar contrato en los dos sentidos: quien firmó precio fijo en el
  pico lo pagó un año entero.

Las subidas de familias volátiles se marcan estacionales y **no cuentan en el total de
sobrecoste evitable**. La lista de familias volátiles está en
`references/familias-y-volatilidad.md` §1 y es un parámetro del motor (`volatiles`), no una
constante escondida en el código.

**El formato encubierto es la cifra que un aficionado no busca.** Mismo precio de línea,
menos gramos: solo aparece comparando €/base. En España el **54% de los consumidores** dice
haber notado reduflación en sus compras (estudio Ipsos citado en la tramitación de la Ley de
Consumo Sostenible, jun-2025), la OCU la denunció en febrero de 2025 como práctica extendida
durante tres años de subidas, y la reforma en tramitación obligará a informarlo **de forma
visible en el punto de venta durante no menos de 90 días**. Nada de eso protege a un
restaurante: al albarán de un mayorista no llega esa etiqueta.

**Umbrales de decisión en euros** (criterio de oficio, `[A VALIDAR]`, calibrables por
cliente en la instalación): una subida con impacto **> 300 €/año** merece entrar a negociar;
un ahorro por cambio de proveedor **> 500 €/año** merece pedir oferta formal. Por debajo se
anota y no se prioriza, porque el tiempo del dueño también cuesta. Y una diferencia
**> 40-50%** entre dos proveedores del mismo producto se trata como sospecha de que no es el
mismo producto, no como hallazgo.

## Procedimiento

1. **Entrada: albaranes, facturas o export de compras → Acción: levantar cada línea con producto, familia, proveedor, unidad, formato real, precio y fecha, y añadir consumo mensual si existe → Salida: fichero de líneas listo para el motor → Si falta el formato de una caja o un saco: la línea se descarta y se anota para el apartado 7, nunca se supone el peso.**

2. **Entrada: nombres de producto de cada proveedor → Acción: agrupar el mismo producto aunque cada uno lo llame distinto, revisando el emparejamiento a ojo → Salida: lista de productos unificados → Si dos nombres no son claramente el mismo producto: se dejan separados y se pregunta, porque agruparlos falsea la comparativa entera.**

3. **Entrada: líneas agrupadas → Acción: ejecutar `python3 scripts/proveedores.py datos.json` para normalizar a unidad base y a base imponible → Salida: €/kg, €/L o €/ud sin IVA por línea, más la lista `errores_datos` de lo que no se pudo normalizar → Si falta el tipo de IVA: se asume precio de albarán sin IVA y se declara; si hay sospecha de mezcla, la línea se marca "IVA por confirmar".**

4. **Entrada: precios por base con fecha → Acción: detectar subidas del mismo proveedor entre la primera y la última fecha del periodo, contra el umbral del 8% → Salida: alertas con precio antes, precio ahora, % y fechas → Si solo hay una fecha por producto y proveedor: no hay alerta posible y se dice, en vez de comparar contra otro proveedor y llamarlo subida.**

5. **Entrada: familia de cada producto → Acción: marcar como estacional toda subida de familia volátil según `references/familias-y-volatilidad.md` → Salida: cada subida etiquetada estacional o estructural, y el total de sobrecoste evitable contando solo las estructurales → Si la familia no consta: se clasifica por el nombre del producto y se declara el criterio usado.**

6. **Entrada: precios por base de distintos proveedores en la fecha más reciente → Acción: identificar quién tiene hoy cada producto más barato y calcular la diferencia → Salida: tabla de comparativa con ahorro mensual y anual → Si la diferencia supera el 40-50%: se emite como sospecha de producto distinto, no como ahorro, y se pide verificar calidad, calibre y origen antes de cambiar.**

7. **Entrada: histórico de precio por base del mismo formato → Acción: buscar formato encubierto (precio de línea estable con €/base al alza) y revisar a mano portes, precio de lista contra pactado y mínimo de pedido → Salida: apartado 4 del informe, o la frase "no se detectaron subidas encubiertas en este periodo" → Si no hay dos periodos del mismo formato: no se puede detectar y se dice.**

8. **Entrada: variación por base y consumo mensual → Acción: multiplicar variación por volumen para obtener impacto en euros y ordenar todo de mayor a menor impacto anual → Salida: subidas y ahorros ordenados por euros → Si falta el consumo: el impacto sale 0 €, se declara que es un hueco de dato y no un coste cero, y se ordena por porcentaje avisando de que no es el orden de prioridad.**

9. **Entrada: carta o salida de `escandallo-ingenieria-menu` → Acción: cruzar cada subida con los platos que usan ese producto y calcular sobrecoste por ración, por mes y margen perdido → Salida: apartado 5 con los platos que pasan de sanos a tocados por la compra, no por la receta → Si no hay datos de carta: el apartado no aparece y se ofrece como siguiente paso.**

10. **Entrada: todo lo anterior → Acción: pasar las cinco verificaciones (misma base por producto, ningún precio por base absurdo, ninguna subida superior al 100% sin verificar, estacionales separadas de estructurales, cada acción con cifra anual) y redactar tres o cuatro acciones → Salida: informe cerrado con "ahorro y sobrecoste evitable estimado: X €/año" → Si una acción no acaba en cifra: no es una acción, es una observación, y se saca del apartado 6.**

## Salida

```markdown
# Control de compras — [Nombre del local]
[Periodo comparado] · [Nº de proveedores] · [Nº de productos cruzados] · [Nº de líneas válidas / descartadas]

## 1. Diagnóstico en tres líneas
Sobrecoste estructural detectado: **X €/año**. Ahorro posible por cambio de proveedor: **Y €/año**.
De lo que ha subido, [importe] es estacional (se corrige solo) y [importe] es estructural (aquí está la pelea).

## 2. Las subidas que más te cuestan
| Producto | Proveedor | Antes → Ahora (€/base) | % | €/año | ¿Estacional? |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

## 3. Quién te lo tiene más barato hoy
| Producto | Más barato (prov · precio) | Más caro (prov · precio) | Ahorro €/año |
|---|---|---|---|
| ... | ... | ... | ... |

## 4. Trucos detectados
Formatos encubiertos, portes, precio de lista sin aplicar, mínimo de pedido.
Si no hay ninguno: "No se detectaron subidas encubiertas en este periodo."

## 5. Impacto en tu carta
Solo si hay datos de carta o escandallo.
| Plato | Ventas/mes | Sobrecoste €/ración | €/mes | €/año | Margen perdido |
|---|---|---|---|---|---|

## 6. Acciones, por orden de impacto
1. **[Qué hacer]** — vale X €/año. Antes de ejecutar, comprueba [calidad · calibre · plazo · servicio].

## 7. Supuestos y huecos de dato
- Líneas descartadas y por qué (con el mensaje literal del motor).
- Qué se asumió (IVA, familia, consumo).
- Qué falta por medir para la siguiente vuelta.

**Ahorro y sobrecoste evitable estimado: X €/año.**
```

Longitud máxima: 2 páginas más las tablas. Si se pasa, es que hay que partir el informe por
familias (bebida y limpieza aparte de alimentación), no alargarlo.

## Límites

- El proveedor más barato no es siempre el mejor: calidad, calibre, plazo de entrega,
  servicio y crédito comercial valen dinero que no está en el precio por kilo. El informe
  señala dónde mirar; la decisión la firma el dueño con su criterio de producto.
- No renegocia por el cliente, no pide ofertas, no cambia pedidos en ningún sistema.
- No es asesoría fiscal ni contable. Los tipos de IVA que aplica son referencia verificada
  (ver `references/FUENTES.md`) y el tipo real de cada línea lo confirma el asesor.
- No detecta fraude ni lo afirma. Un formato encubierto o un porte intermitente es un
  hallazgo para preguntar al comercial, no una acusación.
- No sustituye el escandallo: calcula el impacto de una subida sobre un plato ya escandallado,
  no el coste del plato desde cero. Eso es `escandallo-ingenieria-menu`.
- Sin consumo mensual no hay priorización por euros, y sin priorización por euros el informe
  es una lista de porcentajes. Se declara antes de entregarlo, no después.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Llevar toda línea a unidad base (€/kg, €/L, €/ud) antes de comparar dos precios | Una garrafa de 5 L a 42,50 € son 8,50 €/L y gana al litro suelto de 8,90 €: sin normalizar, la recomendación de compra sale invertida |
| Comparar sobre base imponible y decir qué tipo de IVA se aplicó a cada línea | Un queso a 20,90 € con 10% incluido son 19,00 € netos; cruzarlo contra un albarán sin IVA inventa una diferencia que no existe |
| Ejecutar el cálculo con `scripts/proveedores.py`, nunca a mano | Cincuenta líneas cruzadas a mano producen un error aritmético delante de quien conoce sus albaranes, y ahí acaba la instalación |
| Separar subidas estacionales de estructurales antes de sumar el sobrecoste evitable | Perseguir al proveedor de pescado en agosto quema la relación comercial y no ahorra un euro |
| Ordenar subidas y ahorros por impacto anual en euros, no por porcentaje | Un perejil que sube el 40% con 2 € de compra al mes es ruido; un aceite que sube el 8% con 600 € al mes es el trabajo |
| Declarar cada línea descartada con el motivo literal del motor | Una línea que desaparece sin explicación se lee como cálculo incompleto y tumba la credibilidad del resto del informe |
| Revisar a ojo el emparejamiento de nombres de producto antes de fiarse del agrupamiento | "AOVE 5L" y "Oliva virgen extra" son el mismo producto; "virgen extra" y "orujo" no, y agruparlos falsea toda la comparativa |
| Tratar una diferencia superior al 40-50% entre proveedores como sospecha de producto distinto | Recomendar el cambio sin verificar calidad y calibre entrega producto peor en la primera compra |
| Decir "falta el dato de consumo" cuando el impacto sale 0 € | El motor devuelve 0 € por hueco de dato, y un 0 € sin explicar se lee como "no cuesta nada" |
| Revisar a mano portes, precio pactado y mínimo de pedido, que el motor no ve | Son coste real que no está en la línea de producto y cambian qué proveedor es más barato de verdad |
| Cerrar cada acción con su cifra anual y qué comprobar antes de ejecutarla | Una acción sin euros no se ejecuta, y una sin verificación previa hace cambiar de proveedor a ciegas |

| NUNCA | Porqué |
|---|---|
| Suponer el peso de una caja, un saco o una garrafa cuando no consta | Un peso inventado contamina el €/kg de ese producto y de toda comparación en la que entre |
| Llamar subida a la diferencia entre dos proveedores distintos | Una subida es el mismo producto y el mismo proveedor en dos fechas; lo otro es comparativa, y confundirlos produce alarmas falsas |
| Contar las subidas estacionales en el total de sobrecoste evitable | Infla la cifra del titular con dinero que se corrige solo, y el dueño lo descubre en el cambio de temporada |
| Recomendar un cambio de proveedor sin decir qué hay que verificar antes (calidad, calibre, plazo, servicio) | El precio por kilo no incluye lo que de verdad rompe un servicio: que no llegue el pedido del viernes |
| Acusar a un proveedor de mala fe por un formato encubierto o un porte | Es un hallazgo para preguntar, no una prueba, y una acusación cierra la puerta a la renegociación que sí ahorra dinero |
| Descontar un IVA que no se sabe con certeza | Descontar 10% donde tocaba 4% mueve la comparación casi seis puntos: se marca "IVA por confirmar" |
| Entregar una tabla de precios como informe | Un informe de compras que no acaba en tres acciones con euros no se lee dos veces |
| Presentar los umbrales de fábrica (8%, 300 €, 500 €) como norma del sector | Son criterio de oficio calibrable; el valor de la instalación es ajustarlos a los datos de ESE negocio |
| Dar por buena una subida superior al 100% sin verificarla | Casi siempre es unidad o formato mal metido, y publicarla destruye la confianza en todo el resto del informe |

## Antipatrones

1. **Síntoma**: el informe recomienda cambiar a un proveedor cuyo precio de línea es más bajo, y al mes siguiente el coste del local sube. **Causa raíz**: se comparó precio de línea sin normalizar formatos (garrafa contra litro, caja contra kilo). **Corrección**: ninguna comparación sale del motor sin `precio_por_base`; el informe imprime siempre la base usada junto al precio.

2. **Síntoma**: el titular del informe promete un ahorro de varios miles de euros y el dueño no lo ve en la cuenta. **Causa raíz**: se contaron las subidas estacionales (pescado, fruta, verdura) dentro del sobrecoste evitable. **Corrección**: el total del apartado 1 suma solo estructurales; las estacionales aparecen en su propia línea con la etiqueta y la fecha de revisión.

3. **Síntoma**: el impacto anual de todas las subidas sale 0 € y el informe parece decir que nada cuesta. **Causa raíz**: no se aportó consumo mensual y el motor multiplica por cero. **Corrección**: cuando `consumo_mes_base` es 0, el informe escribe "impacto no calculable: falta el consumo mensual de este producto" en vez de imprimir 0 €, y pide ese dato como primer paso de la siguiente vuelta.

4. **Síntoma**: aparece un producto con una subida del 300% que nadie recuerda haber pagado. **Causa raíz**: el mismo producto llegó facturado una vez por kilo y otra por unidad, o con un formato distinto sin declarar. **Corrección**: el motor expulsa la línea con el mensaje `aparece en base 'ud' y antes en 'kg'`; ese mensaje va literal al apartado 7 y el producto no entra en el análisis hasta que el cliente confirme la unidad.

5. **Síntoma**: el dueño enseña el informe a su comercial de siempre y la relación se enfría sin haber ahorrado nada. **Causa raíz**: el informe se redactó como acusación ("te está clavando") en vez de como hallazgo con cifra. **Corrección**: cada hallazgo se escribe como pregunta verificable con su euro al lado —"el €/kg de esta referencia ha subido un 11% con el mismo precio de caja: ¿ha cambiado el formato?"—, que es lo que abre una renegociación en vez de cerrarla. `[DERIVADO, NO OBSERVADO EN CAMPO]`

## Casos de prueba

Los cuatro están escritos con su entrada y su salida real en `cases/`, ejecutados contra el
motor. Ninguna cifra está narrada.

**Happy path** (`cases/case_01_happy_path.md`): tres proveedores, dos periodos, consumo
declarado y carta aportada. Detecta el aceite +12,9% (estructural, 792 €/año), la merluza
+22,7% marcada estacional, el cambio a Mayorista B que ahorra 504 €/año, y el sobrecoste de
1.152 €/año que la merluza mete en un solo plato de la carta.

**Edge case** (`cases/case_02_edge_case.md`): una caja sin peso declarado, un queso con IVA
incluido y el mismo producto facturado en kilos y en unidades. Se descartan dos líneas con
su motivo literal, entran tres, y el informe sale con el aviso "2 línea(s) descartadas por
datos incoherentes" en vez de con un número redondo y falso.

**Failure** (`cases/case_03_failure.md`): "cuánto me ha subido el aceite", dos albaranes
pegados, sin consumo, sin segundo proveedor. Se entrega la subida real (8,50 → 9,80 €/L,
+15,3%) y se declara por qué el impacto en euros sale 0 y qué dato lo convierte en euros.

**Integration** (`cases/case_04_integration.md`): encadenado con
`escandallo-ingenieria-menu`. Las dos subidas verificadas entran como nuevo precio de compra
en la carta ya escandallada, y aparece el hallazgo que ninguna de las dos skills ve sola: la
desviación teórico-real **baja** de 3,85 a 2,88 puntos sin que la cocina haya mejorado nada.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
