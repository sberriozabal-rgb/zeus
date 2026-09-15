# Caso 4 · Integration (consume la salida de `respaldo-proyecto-ia-cl`)

## Situación

El usuario ya ejecutó `respaldo-proyecto-ia-cl` y tiene el paquete cifrado con su proyecto dentro.
Ahora quiere **entender** lo que hay ahí: qué se decidió, cuál es la versión vigente de cada cosa
y qué quedó abierto.

Ese es exactamente el trabajo de esta skill, y el encadenado resuelve el problema logístico que
tiene en solitario: **conseguir los chats**.

## Qué aporta cada una

| `respaldo-proyecto-ia-cl` produce | `universal-compilador-contexto` lo usa como |
|---|---|
| `06-chats/chats.jsonl` normalizado | fuente de la fase de ingesta de chats (Ruta B, completa) |
| `02-conocimiento/` | material del censo y de la extracción total |
| `03-adjuntos/` + `INDICE-ADJUNTOS.md` | archivos con su nombre real recuperable |
| `HUECOS.md` | **huecos heredados que NO debe inventar** |

## Por qué el orden importa y no es reversible

El respaldo se hace **mientras hay acceso** y su primer paso es solicitar el export antes de que
caduque el enlace. Si se intenta compilar primero, se llega al export tarde y la ingesta de chats
cae a la Ruta A, **parcial por diseño**.

Encadenado en este orden, la compilación arranca con cobertura completa de chats sin tener que
gestionar plazos.

## La pieza que más valor aporta al encadenado: el `HUECOS.md` heredado

Es lo que permite que el resumen final distinga **ausencia de dato** de **ausencia de decisión**:

> *No consta ninguna decisión sobre el reparto societario. **Nota:** el historial de chats de
> este proyecto no viajó en el respaldo (enlace de export caducado, ver `HUECOS.md` heredado),
> así que esta ausencia no prueba que no se decidiera.*

Sin ese fichero, el compilador escribiría *"no se decidió nada sobre el reparto"*, que es una
afirmación **falsa** presentada con toda la autoridad de una biblioteca ordenada.

## La clase de sensibilidad viaja con el material

Los chats llegan marcados **C2 por defecto** desde el respaldo. El resumen que produce esta skill
**hereda esa clase**: no baja a C0 porque el formato de salida sea más corto. Si el resumen se va
a compartir con un socio o con un tercero, se le aplica la misma redacción de C2.

Y los **C3 no llegan nunca**: se rotaron en origen y no entraron en el paquete.

## El límite compartido que ninguna de las dos cruza

Ninguna interpreta el negocio. El respaldo ordena y cifra; el compilador extrae y estructura. Las
dos devuelven **conflictos y huecos** al dueño en vez de resolverlos, y las dos etiquetan
`PROPUESTA A VALIDAR` lo que no tiene un documento aprobado detrás.

## Qué demuestra el caso

Que las dos piezas son **la misma cadena en dos mitades**: una asegura el material antes de que
desaparezca, la otra lo hace comprensible. Y que el fichero más humilde del respaldo —la lista de
lo que no viajó— es el que impide que la compilación mienta por omisión.
