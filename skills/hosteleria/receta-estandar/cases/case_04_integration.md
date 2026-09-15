# Caso 4 · Integration (la ficha alimenta al escandallo)

## Encargo real que escribiría un dueño

> "Ya tengo la ficha del salmón firmada y pesada. Ahora quiero el escandallo de
> la carta. Me dijo el asesor que con las recetas ya hechas el escandallo sale
> solo. ¿Es verdad o me va a volver a salir que el salmón me deja un margen
> buenísimo, que es lo que decía la hoja de Excel del año pasado y luego no
> aparecía por ningún lado?"

## Entrada

La ficha del caso 1, ya con el pesaje hecho: **`Salmón a la plancha con puré y
espárragos`, ACORDADA, v1.0, España (Girona), último pesaje 24-ago-2026.**

Y una pregunta que la ficha del caso 1 **no** contestaba y que el chef contesta
ahora, en la misma sesión, porque es la que hace falta aguas abajo:

| Dato nuevo | Valor declarado por el chef | Marca |
|---|---|---|
| Forma de compra del salmón | Lomo con piel y espinas, en pieza | CONFIRMADO |
| Rendimiento tras limpieza | 78 % (desespinado y perfilado en cocina) | `[A VALIDAR — medido por el chef en 3 piezas, no por esta skill]` |
| Merma de plancha | 12 % de pérdida de peso en cocción | `[A VALIDAR — medido por el chef]` |

## El hueco que cierra la integración

`escandallo-ingenieria-menu` no calcula solo con la ficha tal como salió del caso
1, y este es el punto entero del caso.

La ficha declara **160 g de lomo de salmón por ración**. Ese es el peso **neto,
limpio, listo para la plancha**. El albarán del proveedor no habla de eso: habla
de kilos de pieza con piel y espinas. Un escandallo que multiplica los 160 g de la
ficha por el precio del albarán está mal por construcción, y sale bajo — que es
exactamente la razón por la que el margen del año pasado no aparecía en la caja.

Con el rendimiento declarado, la aritmética cambia de sitio:

```
Peso en la ficha (neto, a la plancha)   : 160 g / ración
Rendimiento tras limpieza declarado     : 78 %
Peso de COMPRA que hay que escandallar  : 160 / 0,78 = 205,1 g / ración
                                          640 / 0,78 = 820,5 g / 4 raciones

Efecto sobre el coste de materia prima del ingrediente principal: +28,2 %
```

**Ese +28,2 % es la cifra que la integración pone encima de la mesa y que ninguna
de las dos skills tiene sola.** La ficha sabe cuánto salmón se cocina; el
escandallo sabe cuánto cuesta el kilo; nadie sabía cuánto salmón hay que comprar
para cocinar ese. El precio por kilo **no aparece en este caso a propósito**: sale
del albarán del cliente y lo pone `escandallo-ingenieria-menu`, no esta skill.

Y hay una segunda transferencia, la que hace ejecutable la tolerancia:

```
Peso neto crudo por ración              : 160 g
Merma de plancha declarada              : 12 %
Peso de plato servido                   : 140,8 g
Tolerancia ±10 % sobre plato servido    : 126,7 g – 154,9 g
```

La tolerancia de la ficha está declarada sobre **peso de plato servido**, no sobre
crudo. Sin la merma de cocción, esa banda no se puede pesar en el pase, que es el
único sitio donde se comprueba. Con ella, el jefe de partida pesa tres platos al
azar y sabe en dos segundos si está dentro.

## Lo que se entrega — el contrato, con la costura declarada

```json
{
  "plato": "Salmón a la plancha con puré y espárragos",
  "pais_operacion": "ES",
  "rendimiento_total": {"porciones": 4, "peso_g": 1660},
  "porcion_individual_g": 160,
  "tolerancia_porcion_pct": 10,
  "ingredientes": [
    {"nombre": "lomo de salmón sin espinas", "cantidad": 640, "unidad": "g", "marca": "CONFIRMADO",
     "unidad_compra": "pieza con piel y espinas", "rendimiento_limpieza_pct": 78,
     "peso_compra_g": 820.5, "merma_coccion_pct": 12},
    {"nombre": "patata para puré", "cantidad": 800, "unidad": "g", "marca": "CONFIRMADO",
     "unidad_compra": "kg, sin pelar", "rendimiento_limpieza_pct": 82, "peso_compra_g": 975.6}
  ],
  "puntos_criticos_haccp": [
    {"paso": 7, "temp_min_c": 68, "tiempo_min_s": 15, "metodo_verificacion": "sonda",
     "norma": "AESAN-2021-004, categoría pescado"}
  ],
  "estado": "ACORDADO"
}
```

> **Costura declarada en la entrega, no en un cajón:** los campos
> `unidad_compra`, `rendimiento_limpieza_pct`, `peso_compra_g` y
> `merma_coccion_pct` **no están en el contrato JSON de `SKILL.md § Salida`**. Ahí
> la unidad de compra vive en la columna *Nota* de la tabla de ingredientes, que
> es texto libre y ningún consumidor puede leer. Mientras el contrato no incorpore
> esos cuatro campos, la transferencia hacia el escandallo se hace a mano y es
> exactamente donde se pierde el 28,2 %. `[carencia detectada — extensión de
> contrato para una versión MENOR, no se decide desde un caso]`

## Reglas de la integración

- **Esta skill no calcula el coste. Nunca.** Entrega gramaje de receta, gramaje de
  compra y merma. El precio del kilo, los costes indirectos, el food cost objetivo
  y el PVP son de `escandallo-ingenieria-menu`, con la estructura real del
  negocio. Duplicar el cálculo aquí garantiza que las dos cifras diverjan.
- **El rendimiento de limpieza y la merma de cocción los mide el chef en su
  cocina, no los estima la skill.** Son datos de local: cambian con el proveedor,
  con la pieza y con quién la limpia. Sin ellos, el campo va a `[PENDIENTE]` y el
  escandallo se entrega declarando que trabaja con peso neto, no con peso de
  compra. Nunca se rellenan con una tabla de rendimientos de manual.
- **En sentido contrario**: si el escandallo concluye que hay que bajar el salmón
  a 140 g y subir el puré, **no se toca el escandallo: se reescribe la ficha**, se
  vuelve a pesar y la ficha baja a BORRADOR hasta ese pesaje. Cada skill manda en
  su cifra, y la cifra de gramaje es de esta.
- **Una ficha escalada con `scripts/escalar_receta.py` no alimenta al escandallo.**
  El script devuelve la ficha a `estado: BORRADOR` a propósito, y una ficha
  BORRADOR es una hipótesis. El escandallo de un catering de 80 se hace con la
  ficha reverificada, no con la multiplicada.
- **Hacia `apertura-cierre-turno`**: los bloques 3 (mise en place) y 6
  (conservación y servicio) de la ficha se transfieren tal cual como tareas de
  checklist con su criterio de "hecho" — *salmón porcionado en 4 × 160 g y
  refrigerado*, *puré de pase con sonda ≥63 °C*. El punto crítico de mantenimiento
  en caliente deja de ser una línea de una ficha plastificada y pasa a ser una
  tarea firmada de la lista de apertura. La tolerancia ±10 % **no se copia** en el
  checklist: se referencia. Un umbral vive en un solo sitio.

## Por qué importa

Porque es la demostración de que la línea es un sistema y no tres documentos
vendidos juntos. Ninguna de las dos skills puede sola responder a la pregunta del
dueño: la ficha no sabe lo que cuesta el kilo y el escandallo no sabe cuánto se
tira al limpiar. Sumadas, dan el número que explica por qué el margen del Excel
del año pasado nunca apareció en la caja — **un 28,2 % más de materia prima en el
ingrediente principal del plato que más vende**, que es lo mismo que le pasaba a
la merluza del caso de `escandallo-ingenieria-menu` al aplicarle rendimiento y
merma.

Y demuestra el límite en la misma página: la integración **transporta un dato que
el chef midió**, no lo inventa, y **no recalcula lo que le toca a la otra skill**.

## Supuestos declarados en la entrega

- Rendimiento de limpieza 78 % y merma de plancha 12 %: declarados por el chef
  sobre tres piezas, no medidos por la casa ni tomados de tabla de manual. Se
  revisan al cambiar de proveedor o de calibre de pieza. `[A VALIDAR]`
- Rendimiento de la patata 82 %: mismo origen y misma marca. `[A VALIDAR]`
- No se aporta ningún precio de compra: no es dato de esta skill.
- La ficha se da por ACORDADA porque consta pesaje real el 24-ago-2026. Sin esa
  fecha en la cabecera, esta integración no se ejecuta: un escandallo construido
  sobre una ficha nunca pesada es una hipótesis con dos decimales.
