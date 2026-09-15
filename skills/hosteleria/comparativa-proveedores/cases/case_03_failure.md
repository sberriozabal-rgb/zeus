# Caso 3 · Failure (encargo de una línea, sin contexto)

## Encargo real que escribiría un dueño

> "cuánto me ha subido el aceite"

Y pegados debajo, sin más, dos albaranes del mismo proveedor:

```json
{"lineas": [
  {"producto": "Aceite oliva virgen extra", "proveedor": "Distribuidora A",
   "unidad": "garrafa", "formato": {"valor": 5, "base": "L"}, "precio": 42.50,
   "fecha": "2026-03-12"},
  {"producto": "Aceite oliva virgen extra", "proveedor": "Distribuidora A",
   "unidad": "garrafa", "formato": {"valor": 5, "base": "L"}, "precio": 49.00,
   "fecha": "2026-08-10"}
]}
```

Sin consumo mensual, sin segundo proveedor, sin carta, sin nombre del local.

## Qué NO se hace

No se responde "necesito el consumo mensual y los albaranes de tus otros proveedores para poder calcularlo". El dueño ya sabe que le faltan datos: lo que ha preguntado es cuánto le ha subido el aceite, y esa pregunta **tiene respuesta exacta con lo que ha mandado**. Se entrega producto ahora.

Nota técnica: `scripts/proveedores.py` con `{"lineas": []}` **no devuelve error**: devuelve el esqueleto completo con todos los totales a 0 y `avisos_verificacion` vacío. **Eso es la salida del motor, no la salida de la skill**, y además es el peor comportamiento posible del motor —un informe de ceros sin un solo aviso es exactamente el antipatrón nº 3 de esta misma skill—. La skill nunca traslada ese cero: entrega el informe de abajo y, con entrada vacía de verdad, entrega el mismo informe con la sección 2 completa en `[HUECO]`. Queda anotado en el CHANGELOG como el defecto que impide el 20/20.

## Salida esperada — lo que se entrega igual

```markdown
# Control de compras — [tu local]
12-03-2026 → 10-08-2026 · 1 proveedor · 1 producto · 2 líneas válidas / 0 descartadas

## 1. Diagnóstico en tres líneas
Tu aceite de oliva virgen extra ha subido un **15,3%** en cinco meses con el mismo
proveedor: de **8,50 €/L a 9,80 €/L** de base imponible (garrafa de 5 L, de 42,50 €
a 49,00 €). Es **más de cuatro veces la inflación general** de España, que en
julio de 2026 estaba en el 3,6% anual (INE). Esto ya no es "es que todo sube": es una
decisión de ese proveedor sobre ese producto.
Sobrecoste estructural en euros: **[HUECO — falta tu consumo mensual de aceite]**.

## 2. Las subidas que más te cuestan
| Producto | Proveedor | Antes → Ahora (€/L) | % | €/año | ¿Estacional? |
|---|---|---|---|---|---|
| Aceite oliva virgen extra | Distribuidora A | 8,50 → 9,80 | +15,3% | [HUECO] | No |

El motor imprime **0 €** en esa casilla. **Ese 0 € no significa que no te cueste
nada**: significa que no has aportado cuántos litros gastas al mes. Con el aviso
literal del motor: *"impacto NO calculable en euros — falta el consumo mensual
(kg/L/ud al mes). El 0 € que aparece es un hueco de dato, no un coste cero: no lo
presentes como tal."*
Para que te hagas la cuenta tú mismo mientras tanto: **cada litro que compras al mes
son 15,60 € más al año**. Si gastas 60 L/mes, son 936 €/año. Si gastas 20, son 312 €.
Multiplica tus litros por 15,60 y tienes tu cifra.

## 3. Quién te lo tiene más barato hoy
[HUECO — hace falta el albarán o la tarifa de un segundo proveedor del mismo producto]
Sin dos proveedores no hay comparativa. Lo que sí se puede decir del oficio: si te
ofrecen un aceite a más de un 40-50% por debajo de 9,80 €/L, la primera hipótesis no
es que hayas encontrado un chollo, es que **no es el mismo aceite** (virgen extra no
es virgen, y virgen no es orujo). Antes de cambiar: acidez, origen y cosecha.

## 4. Trucos detectados
No hay formato encubierto en este periodo: el precio de línea **sí** cambió (42,50 →
49,00 €) y la garrafa siguió siendo de 5 L. Si algún día ves la misma garrafa al mismo
precio pero con menos litros dentro, eso es la subida que no aparece en el albarán, y
solo se ve comparando €/L.

## 5. Impacto en tu carta
[HUECO — sin escandallo ni carta no se puede cruzar]
Regla rápida mientras tanto: en un plato que lleve un chorro de acabado de unos 25 ml, esta
subida son 0,03 € por ración. En una fritura amortizada o un confitado, es mucho más.
Los platos que hay que mirar son los de aceite como ingrediente, no como acabado.

## 6. Acciones, por orden de impacto
1. **Sacar tu consumo mensual de aceite** — un dato, el de un mes normal. Sin él, todo
   lo de arriba es un porcentaje y no un euro. Coste: 10 minutos con las facturas.
2. **Pedir tarifa a un segundo proveedor de virgen extra**, con acidez y origen por
   escrito. Vale la pena si el ahorro supera los 500 €/año, y con 60 L/mes basta una
   diferencia de 0,70 €/L para superarlo.
3. **Preguntar a tu comercial por esta subida, con el número delante y sin acusar**:
   "el litro me ha pasado de 8,50 a 9,80 en cinco meses, un 15,3%. ¿A qué responde?"
   Esa pregunta abre una renegociación; "me estás clavando" la cierra.
4. **Volver a mirarlo en la próxima cosecha.** El aceite es la familia que sube por
   cosecha y cae de golpe: en la campaña 2024/25 los precios en origen del virgen
   extra cayeron un 49,4% frente a la anterior (Observatorio de Precios y Mercados de
   la Junta de Andalucía). Precio en origen no es precio de mayorista y no baja igual
   ni a la vez, pero quien firma precio fijo en el pico lo paga un año entero.

## 7. Supuestos y huecos de dato
- Se asume que los dos precios son **de albarán y sin IVA**, que es lo habitual. Si
  alguno era precio de tarifa con IVA incluido, la comparación cambia y hay que
  rehacerla: dilo.
- Se asume que la garrafa siguió siendo de 5 L en las dos fechas. Si cambió el
  formato, la subida real es otra.
- Consumo mensual: HUECO. No se ha estimado con un consumo medio de sector porque el
  tuyo lo cambia entero.
- Segundo proveedor: HUECO. La comparativa no aplica con uno solo.
- Carta y escandallo: HUECO. El apartado 5 se ofrece como siguiente paso.

**Ahorro y sobrecoste evitable estimado: [HUECO — es tu consumo mensual multiplicado
por 1,30 €/L].**
```

**Una sola pregunta al final**, no cuatro: *"¿Cuántos litros de aceite gastas en un mes normal? Con ese número te devuelvo la cifra en euros, y si me pasas el albarán de otro proveedor, quién te lo tiene más barato."*

## Por qué es el caso decisivo

Todo lo que no depende de los datos que faltan —la subida exacta con su base normalizada, la comparación contra el IPC, la regla de los 15,60 €/año por litro/mes, el umbral del 40-50% para no cambiar a ciegas, la frase literal para el comercial y la advertencia de la cosecha— se entrega completo y es ejecutable esta misma semana. El único hueco es el euro anual, y se dice por qué está vacío en vez de rellenarlo con un consumo de sector inventado. El dueño sale con una subida cuantificada, una cuenta que puede hacer él mismo en treinta segundos y una tarea concreta para tener su cifra.
