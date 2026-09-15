# Caso 4 · Integration (alimenta a `universal-compilador-contexto`)

## Situación

El respaldo está sellado y verificado. Meses después, el usuario quiere **entender** lo que hay
dentro: qué se decidió, qué versión de cada documento es la vigente y qué quedó pendiente. Eso no
lo hace esta skill —que ordena y cifra, no interpreta— sino
`universal-compilador-contexto`.

## Dónde se tocan exactamente

Esta skill produce en la capa 6 un `chats.jsonl` normalizado: una conversación por línea, con
fecha, título y mensajes. Ese fichero es **una de las fuentes de ingesta** del compilador, junto
con los documentos de `02-conocimiento/`.

```
respaldo-proyecto-ia-cl                universal-compilador-contexto
  06-chats/chats.jsonl        ----->     ingesta de historial
  02-conocimiento/*.md        ----->     censo documental
  HUECOS.md                   ----->     huecos declarados que NO debe inventar
```

## Por qué el handoff funciona en este orden y no al revés

El compilador **necesita el export ya descargado**, y descargarlo a tiempo es precisamente el
paso 1 de esta skill. Intentarlo al revés —compilar primero y respaldar después— choca con el
enlace caducado del caso 3.

## Lo que viaja y no es obvio: `HUECOS.md`

Es la pieza que más valor aporta al encadenado. El compilador produce un resumen de todo el
contexto, y sin `HUECOS.md` **no sabría distinguir entre "no se decidió nada sobre X" y "la capa
que hablaba de X no viajó"**. Con él, el resumen final puede decir:

> *No hay constancia de decisión sobre [tema]. Nota: el historial de chats de este proyecto
> no está en el respaldo (enlace de export caducado, ver `HUECOS.md`), así que la ausencia no
> prueba que no se decidiera.*

Esa distinción entre **ausencia de dato** y **ausencia de decisión** es exactamente lo que
separa un compilador honesto de uno que rellena.

## El límite de clase que se respeta al encadenar

Los chats son **C2 por defecto**. Si el compilador va a producir un resumen que se comparte con
terceros, ese resumen **hereda la clase del material del que sale**: no se puede bajar a C0
porque el formato de salida sea más corto. La redacción de C2 se aplica igual al resumen.

Y los C3 no llegan nunca al compilador, porque no llegaron al paquete: se rotaron en origen.

## Qué demuestra el caso

Que el respaldo no es un archivo muerto. Produce la materia prima ordenada, clasificada y con sus
huecos declarados, que es justo lo que otra skill necesita para trabajar sin inventar.
