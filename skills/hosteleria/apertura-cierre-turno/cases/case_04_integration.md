# Caso 4 · Integration (encadenado con otras skills del sistema)

## Encargo real que escribiría un dueño

> "El escandallo me dice que la merluza pierde margen por porcionado y que la
> merma de la partida de frío se me ha ido a 8%. Y ahora tengo la ficha de
> receta estándar de los cuatro platos de esa partida. ¿Me metes todo esto en
> el checklist de apertura para que dejen de hacerlo a ojo?"

## Cómo se encadena

Tres skills del sistema instalable, en orden real de uso:

1. **`escandallo-ingenieria-menu`** ya calculó una desviación entre food cost
   teórico y real en "Merluza a la plancha", y la atribuyó a control de
   porcionado, no a precio de compra.
2. **`receta-estandar`** ya produjo la ficha de los cuatro platos de la partida
   de frío, cada una con gramaje por porción y tolerancia declarada (±10 % sobre
   peso de plato servido).
3. **`apertura-cierre-turno`** —esta skill— convierte esos dos hallazgos en
   tareas del checklist. **No recalcula nada.** Consume el umbral ya fijado por
   las otras dos y lo transforma en algo que alguien firma a las once de la
   mañana.

## Qué entrega este caso

Tres filas nuevas en el bloque de apertura, marcadas como **específicas del
local**, no de la plantilla base:

| # | Tarea | Responsable | Criterio de "hecho" | Origen |
|---|---|---|---|---|
| 11 | Verificar mise en place de partida de frío contra ficha de receta estándar | Cocina | Las cuatro fichas colgadas en la partida. Cada preparación pesada al menos una vez al montar, dentro de la tolerancia ±10 % declarada en la ficha | `receta-estandar` |
| 12 | Comprobar que la báscula de porcionado está encendida y tarada | Cocina | Tara a 0 verificada con el recipiente de servicio real, no vacía | `escandallo-ingenieria-menu` |
| 13 | Anotar merma de la partida de frío del día anterior antes de reponer | Cocina | Cifra en gramos anotada por preparación. Es el dato que alimenta el siguiente escandallo | `escandallo-ingenieria-menu` |

Y una fila en el **cierre**:

| # | Tarea | Responsable | Criterio de "hecho" | Origen |
|---|---|---|---|---|
| 9 | Registrar peso real servido de merluza en 3 platos al azar del servicio | Cocina | Tres cifras anotadas. Si dos de tres se salen de ±10 %, se abre incidencia con número | `receta-estandar` + `escandallo` |

## La regla que se respeta aquí, y es la que importa

El criterio de "hecho" de la tarea 11 **no dice "verificar que el porcionado sea
correcto"**. Dice ±10 %, que es el número que ya calculó `receta-estandar`. Esta
skill no inventa una tolerancia propia, no la redondea y no la mejora. Si mañana
el cliente cambia la tolerancia en la ficha de receta, el checklist queda
desactualizado y hay que regenerarlo — y eso se declara en la entrega, porque un
umbral copiado a mano en dos documentos distintos diverge en tres semanas.

## Cuándo NO aparecen estas filas

Solo se generan si el dueño aporta o referencia los informes previos **y** el
plato o la partida señalada existe en la operación del local. Si no hay informe
de escandallo, no hay fila 12: no se añade una tarea de báscula "por si acaso"
a un local que porciona a cucharón y nunca dijo tener un problema de coste.

## Por qué importa

Es lo que convierte siete skills en un sistema y no en una carpeta con siete
archivos. El checklist es la única de las siete que produce un documento que
alguien **firma cada día**: es el punto donde los hallazgos de las otras seis
dejan de ser un PDF que se leyó una vez y pasan a ser una tarea con dueño, hora
y cifra de corte. Sin esta pieza, el sistema diagnostica y no cambia nada.
