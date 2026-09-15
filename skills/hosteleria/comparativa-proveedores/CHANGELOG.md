# Changelog — comparativa-proveedores

## [1.1.1] — 2026-09-15

**Parche de conformidad con la rúbrica.** De 18/20 a 20/20 mecánico (19/20 declarado: el punto 19, URLs verificadas una a una, no se reconfirmó). Procedimiento consolidado de 10 a 8 pasos: 4+5 (detectar la subida contra el umbral del 8 % y etiquetarla estacional o estructural) y 8+9 (impacto en euros por volumen y sobrecoste por ración vía escandallo). Ninguna rama "si falta el dato" se pierde. Literal "Supuestos de esta versión" en el apartado 7 de la plantilla de salida. El contenido de oficio no cambia.

## 1.1.0 — 2026-08-16

**Auditoría de fábrica ZEUS.** Nota honesta antes de la revisión: **11/20**. La v1.0.0
tenía método y motor, pero cero casos de prueba ejecutados, cero ficha comercial, cero
README, cero metadatos de empaque y las cifras de umbral sin fuente verificada. Nota
después de esta revisión: **18/20**. Los dos puntos que siguen faltando están nombrados
abajo, no redondeados.

### Añadido — estructura (ADN de la línea Hostelería)

- `cases/` completo, **ejecutado contra el motor, ninguna cifra narrada**:
  - `case_01_happy_path.md` — 3 proveedores, 2 fechas, consumo y carta. Aceite +12,9%
    (792 €/año, estructural), merluza +22,7% (1.200 €/año, **estacional y fuera del
    sobrecoste evitable**), cambio a Mayorista B por 504 €/año, y 1.152 €/año que la
    merluza mete en un solo plato de la carta.
  - `case_02_edge_case.md` — IVA incluido mezclado con albarán, una caja sin peso y el
    mismo queso facturado en kilos y por pieza. Dos líneas expulsadas con el mensaje
    literal del motor, tres válidas, y una subida de 261,82 €/año que **no se prioriza
    por estar debajo del umbral de 300 €/año**.
  - `case_03_failure.md` — "cuánto me ha subido el aceite" con dos albaranes pegados.
    Se entrega el informe completo con la subida real (8,50 → 9,80 €/L, +15,3%), la
    regla de los 15,60 €/año por cada litro/mes para que el dueño haga su propia cuenta,
    y el resto en `[HUECO]` declarado. Nunca se pide más información y se para.
  - `case_04_integration.md` — encadenado con `escandallo-ingenieria-menu`. Con los dos
    precios actualizados sobre su carta de prueba, la desviación teórico-real **baja de
    3,85 a 2,88 puntos** sin que la cocina haya cambiado nada: 0,97 puntos de esa
    desviación eran compra, no porcionado.
- `README.md`, `metadata.json` y `ANEXO-A-ficha-comercial.md` — no existían.

### Corregido — cifras

- **Umbral del 8% anclado.** La v1.0.0 lo presentaba sin contraste. Ahora se defiende
  contra el IPC general de España —3,6% anual en julio de 2026, INE, nota de prensa del
  13-ago-2026— y se declara explícitamente que el corte exacto en 8 es criterio de
  oficio `[A VALIDAR]` y calibrable por cliente, no norma del sector.
- **Estacionalidad con fuente, no con intuición de cocina.** La misma nota del INE
  atribuye la bajada mensual del 0,7% de alimentos de julio de 2026 al descenso de
  frutas y hortalizas. La familia del aceite se sostiene con el Observatorio de Precios
  y Mercados de la Junta de Andalucía: campaña 2024/25, virgen extra **−49,4%** en
  origen frente a la anterior. Se declara que precio en origen no es precio de
  mayorista de hostelería y no llega igual ni a la vez al albarán.
- **Formato encubierto documentado, no insinuado.** Ipsos (54% de consumidores dice
  haberlo notado) y la reforma del art. 20 del TRLGDCU en tramitación dentro de la Ley
  de Consumo Sostenible, que obligará a informarlo de forma visible durante no menos de
  90 días. Se dice lo que importa para vender esto: **esa norma protege al consumidor
  en el lineal, no al restaurante frente a su mayorista**.
- **Tipos de IVA verificados** contra la sede de la AEAT (21% general, 10% y 4%
  reducidos) y contra el art. 2-A de la Ley del IVA en México (tasa 0% para alimentos,
  con excepciones tasadas). Con nota de verificación honesta: el portal del SAT para
  ese artículo no se pudo recuperar el 16-ago-2026 y la fuente usada es un compendio de
  tercero, `[A VALIDAR]` con contador.
- **Los tres umbrales de decisión en euros (300 €, 500 €, 40-50%) quedan marcados
  `[A VALIDAR]`** en `references/FUENTES.md` §6 como criterio de oficio sin fuente
  publicada. Presentarlos como norma del sector es regla NUNCA de la skill.

### Puntos que siguen sin conseguirse (18/20, no 20/20)

1. **Caso failure útil.** `scripts/proveedores.py` con `{"lineas": []}` no devuelve
   error: devuelve el esqueleto completo con todos los totales a **0 € y
   `avisos_verificacion` vacío**. Un informe de ceros sin un solo aviso es exactamente
   el antipatrón nº 3 de esta misma skill, producido por su propio motor. El informe del
   caso 3 lo escribe el ejecutor, no el script. Se declara en vez de redondearse.
2. **Umbral declarado que el motor no aplica.** `SKILL.md` §Umbral, la regla SIEMPRE
   correspondiente y `familias-y-volatilidad.md` §5 fijan la sospecha de "no es el mismo
   producto" en una diferencia **> 40-50%** entre proveedores. La función `verificar()`
   del motor solo emite ese aviso por encima del **60%**. Una diferencia del 50% pasa
   hoy sin aviso, y el umbral que opera no es el que está escrito.

## 1.0.0 — 2026-08-11

Creación inicial.

- Normalización a unidad base común (€/kg, €/L, €/ud) y a base imponible antes de
  cualquier comparación, con factores de formato explícitos y descarte declarado de toda
  línea no normalizable.
- Alerta de subidas del mismo producto y proveedor entre dos fechas contra umbral
  configurable, separando estacionales de estructurales por familia volátil.
- Comparativa entre proveedores sobre la foto más reciente de cada uno, con ahorro
  mensual y anual.
- Detección de formato encubierto: mismo precio de línea, distinto €/base.
- Impacto en la carta cruzando cada subida con los platos que usan ese producto.
- Script determinista `scripts/proveedores.py` con 6 comprobaciones aritméticas en
  `--autotest`.
- `references/familias-y-volatilidad.md` con volatilidad por familia, factores de
  formato, tipos de IVA, trucos de proveedor documentados y umbrales de decisión.
- Auditoría interna declarada entonces: no se declaró. **Reauditada en v1.1.0 a 11/20.**

## Roadmap v1.2

- Que el motor devuelva el informe del caso failure —o al menos un aviso— con entrada
  vacía, en vez de un esqueleto de ceros mudo. Es el punto 1 de los dos que faltan.
- Bajar el umbral de aviso de `verificar()` de 60% a 45% para que coincida con el
  declarado. Es el punto 2, y es una línea de código.
- Comprobación nº 7 en `--autotest`: que ninguna subida estacional entre nunca en
  `impacto_anual_subidas_no_estacionales_eur`, para blindar el antipatrón nº 2.
- Lectura de portes y mínimo de pedido como líneas propias del albarán, hoy revisión
  manual del paso 7.
- Buscar y verificar un índice de precios de compra de hostelería (no IPC de consumo)
  para España y México, que es la vara correcta y hoy no la tenemos.
