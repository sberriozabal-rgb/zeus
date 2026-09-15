# Caso 2 · Edge case (datos sucios)

## Encargo real que escribiría un dueño

> "Te mando lo que tengo. El queso me ha subido, creo. Del tomate solo apunté 'una caja', y de la pieza de queso entera no sé si va por kilos o por pieza, va como me lo factura él."

## Entrada — el export sucio real

```json
{
  "umbral_alerta_pct": 8.0,
  "lineas": [
    {"producto": "Queso curado", "familia": "lacteo", "proveedor": "Quesos D",
     "unidad": "kg", "precio": 20.90, "iva_pct": 10, "precio_lleva_iva": true,
     "fecha": "2026-04-05", "consumo_mes_base": 12},
    {"producto": "Queso curado", "familia": "lacteo", "proveedor": "Quesos D",
     "unidad": "kg", "precio": 22.90, "iva_pct": 10, "precio_lleva_iva": true,
     "fecha": "2026-08-07", "consumo_mes_base": 12},
    {"producto": "Tomate pera", "familia": "verdura", "proveedor": "Frutas E",
     "unidad": "caja", "precio": 14.40, "fecha": "2026-08-07", "consumo_mes_base": 90},
    {"producto": "Aceite oliva virgen extra", "familia": "seco", "proveedor": "Distribuidora A",
     "unidad": "garrafa", "formato": {"valor": 5, "base": "L"}, "precio": 48.00,
     "fecha": "2026-08-01", "consumo_mes_base": 60},
    {"producto": "Queso curado", "familia": "lacteo", "proveedor": "Quesos D",
     "unidad": "ud", "precio": 62.00, "fecha": "2026-08-07"}
  ]
}
```

Tres suciedades distintas, todas vistas en carpetas de albaranes reales: **precio de lista con IVA incluido** mezclado con precios de albarán, una **caja sin peso declarado**, y el **mismo producto facturado una vez en kilos y otra por pieza**.

## Salida esperada — qué hace y qué se niega a hacer

Cifras reales del motor:

- **El IVA se descuenta y se dice.** 20,90 €/kg con 10% incluido son **19,00 €/kg** de base imponible; 22,90 € son **20,82 €/kg**. El porcentaje de subida no cambia —el IVA es proporcional y sale **+9,6%** de las dos maneras—, pero **los euros sí**: el impacto se calcula sobre 1,82 €/kg de diferencia neta, no sobre los 2,00 €/kg del precio con IVA. Y sobre todo: cruzar esos 22,90 € contra el albarán sin IVA de otro quesero habría inventado una diferencia de casi dos euros por kilo que no existe. Es el motivo por el que la base imponible no es una formalidad contable, es la condición para que la comparación signifique algo.

- **Impacto: 21,82 €/mes → 261,82 €/año.** Estructural (lácteo no es familia volátil), pero **por debajo del umbral de 300 €/año**: se anota y **no se prioriza**. El informe lo dice con esas palabras. Que una subida supere el umbral de alerta del 8% no la convierte en trabajo del dueño.

- **Dos líneas expulsadas, con el mensaje literal del motor**, que va tal cual al apartado 7 del informe:
  - `Línea 2: Unidad 'caja' no es base (kg/L/ud) y falta 'formato' con {valor, base}. No se puede comparar sin normalizar.`
  - `Línea 4: 'Queso curado' aparece en base 'ud' y antes en 'kg'. Revisa la unidad.`
  
  La caja de tomate **no se estima en 10 kg** porque las cajas suelen traer 10 kg: un peso supuesto contamina el €/kg de ese producto y de toda comparación en la que entre. Y la pieza de 62,00 € no se convierte a kilos dividiendo por un peso de pieza inventado: se pregunta.

- **`avisos_verificacion` con una sola línea**: `2 línea(s) descartadas por datos incoherentes: no entran en el análisis.` El informe abre declarando **3 líneas válidas de 5**, no un número redondo.

- **El aceite entra pero no produce nada, y también se dice**: una sola fecha y un solo proveedor. Sin dos fechas no hay alerta; sin dos proveedores no hay comparativa. Aparece en el apartado 7 como "pendiente del segundo periodo", no desaparece.

- `comparativa_proveedores`: vacío. `productos_analizados`: 2. El tomate nunca llegó a existir como producto porque su única línea murió en la normalización.

## Por qué importa

Es el antipatrón nº 4 de la skill desactivado antes de producirse: el mismo producto en dos bases distintas habría dado una "subida" del 197% (62,00 € contra 20,82 €) que ningún dueño recuerda haber pagado, y que habría destruido la confianza en todo el resto del informe. Y es la disciplina de la casa aplicada dos veces: **ningún dato ausente se resuelve con el valor cómodo**. Ni un peso de caja estándar, ni un peso de pieza medio. Se declara y se pregunta.

## Comprobación

Guardar el JSON de arriba y ejecutar `python3 scripts/proveedores.py datos.json`. Deben aparecer las 2 líneas literales de `errores_datos`, `lineas_validas: 3` y el aviso de líneas descartadas.
