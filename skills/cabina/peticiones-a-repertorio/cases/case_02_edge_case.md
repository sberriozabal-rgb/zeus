# Caso 2 · Edge case (transcripción de audio, mitad conversación)

## Entrada

La madre de la novia manda un audio de tres minutos. El DJ lo pasa por un transcriptor y pega
el resultado, sin puntuación y con el habla tal cual:

```
hola buenas mira te llamo por lo de la boda de mi hija que me ha dicho que te
mande yo las canciones de la parte de los mayores a ver quiero que pongas algo
de julio iglesias el de la vida sigue igual y tambien lo de los pecos y mi
marido dice que si puedes poner el que bailamos nosotros que es uno de nino
bravo pero no me acuerdo cual era el de un beso y una flor creo y luego lo del
paquito ese que le gusta a todo el mundo aunque mi hija dice que no pero yo creo
que si y oye tambien si puedes algo de rocio jurado que era la que le gustaba a
mi madre que en paz descanse y nada mas que ya hablamos vale un beso adios
```

## El reto

No hay lista. No hay números. No hay puntuación. Hay títulos aproximados, un título que la
propia persona no recuerda, un tema **explícitamente prohibido por la novia** que la madre
intenta colar, y bastante conversación.

## Salida esperada

```
CRUCE DE PETICIONES — Boda, bloque "mayores"
Peticiones detectadas: 5   Biblioteca: 8.412 tracks

TENGO (3)
  Nino Bravo - Un beso y una flor              0.91
  Los Pecos - [titulo mas probable]            0.88
  Rocio Jurado - [sin titulo concreto]         --  [ver DUDOSO]

DUDOSO (2)
  "julio iglesias el de la vida sigue igual"  -> La vida sigue igual   0.84
  "algo de rocio jurado"                      -> sin titulo: 14 candidatos en biblioteca

CONFLICTO DETECTADO (1)
  "paquito ese" -> Paquito el Chocolatero
  !! Este tema esta en el cubo PROHIBIDO de la lista de la novia.
     NO se resuelve aqui. Decide el contratante.

APARTADAS (6 lineas de conversacion)
```

## Los tres aciertos del caso

1. **"el de un beso y una flor creo"** se resuelve a 0.91 pese a la duda de la propia persona,
   porque el título está casi completo en la frase.
2. **"algo de rocío jurado"** no se resuelve. Hay 14 candidatos y elegir uno sería inventar
   una petición que nadie hizo. Sube como pregunta abierta: *"¿alguna en particular de Rocío
   Jurado, o elijo yo?"* — que además es la respuesta que la señora quiere oír.
3. **El conflicto de Paquito se declara y no se resuelve.** La madre lo pide, la novia lo
   prohibió. La skill no decide entre dos personas de la misma familia: marca el conflicto y lo
   devuelve a quien firma el contrato.

## Lo que NO se hace

No se descartan las peticiones por venir en prosa hablada. No se "corrige" a la señora. Y no
se cuela Paquito el Chocolatero porque lo pida alguien con autoridad aparente: **la lista de
prohibidos del contratante manda**, y el conflicto se declara por escrito.

## Supuestos declarados

> **Asumido**: el bloque es para la franja de invitados mayores, tal como dice el audio. "Los
> Pecos" se ha resuelto al título más probable de su repertorio presente en biblioteca (0.88);
> confírmalo. Seis líneas eran conversación y están en APARTADAS, revisadas: ninguna contenía
> petición.
