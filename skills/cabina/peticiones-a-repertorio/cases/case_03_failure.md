# Caso 3 · Failure (sin export de biblioteca)

## Entrada

El cliente manda la lista. El DJ no sabe exportar su biblioteca, o la tiene en un ordenador al
que ahora no llega.

```
1. Perfect - Ed Sheeran (primer baile)
2. Despacito
3. Bailando
...
26 peticiones. Nada de reggaeton. No poner Paquito el Chocolatero.
```

Sin `collection.xml`. Sin CSV. Sin biblioteca.

## Lo que se pierde

**Todo el cruce.** Sin biblioteca no se puede saber qué tiene y qué le falta, que es la mitad
del valor del informe. No se disimula: se dice en la primera línea.

## Salida real — lo que se entrega igual, sin rendirse

```
CRUCE DE PETICIONES — Boda, 14-jun
>> PENDIENTE DE BIBLIOTECA: no se aporto export.
>> El reparto TENGO / NO TENGO no se ha podido calcular.

PETICIONES PARSEADAS (26)
   1. Ed Sheeran - Perfect                    [MOMENTO: primer baile]
   2. Despacito                               [2+ versiones probables]
   3. Enrique Iglesias - Bailando
   ...

PROHIBIDO (2)  -- esto SI es definitivo, no depende de la biblioteca
  Paquito el Chocolatero
  Reggaeton (genero completo)

MOMENTOS CRITICOS DETECTADOS (1)
  primer baile -> Ed Sheeran - Perfect

AMBIGUEDADES DE VERSION A RESOLVER (3)
  "Despacito"        -> original / ft. Bieber
  "Bailando"         -> version espanol / ft. Sean Paul
  "la del anuncio"   -> sin candidato

APARTADAS (4 lineas de conversacion)
```

## Lo que sí queda cerrado y es entregable hoy

- **La lista de prohibidos es definitiva.** No depende de la biblioteca en absoluto, y es la
  parte que genera conflicto. Ya se puede poner por escrito.
- **Los momentos críticos están identificados.** El primer baile es Perfect: eso se compra sí
  o sí, con biblioteca o sin ella.
- **Las ambigüedades de versión están listadas** y se pueden preguntar al cliente ya, en
  paralelo, sin esperar al export.
- **El documento de confirmación se puede enviar** con los bloques de prohibidos y de
  preguntas. Solo falta el bloque "Confirmado".

## Los supuestos declarados y la instrucción que cierra el hueco

> **Asumido**: sin export de biblioteca, ninguna petición se ha marcado como disponible. Las
> 26 están parseadas y clasificadas por momento y por ambigüedad de versión, pero **no sé qué
> tienes**.
>
> **Para cerrar el hueco, 2 minutos:**
> - **rekordbox**: `File > Export Collection in xml format`.
> - **Serato / Engine DJ / VirtualDJ / Lexicon**: exporta un CSV con al menos las columnas
>   `artist` y `title`.
>
> Mándame ese fichero y te devuelvo el reparto completo con la lista de compra priorizada y
> presupuestada.

## Lo que NO se hace

No se responde "necesito tu biblioteca" y se cierra. El DJ se lleva la lista de prohibidos
lista para enviar —que es la parte que le evita el conflicto—, los momentos críticos
localizados y tres preguntas de versión que puede mandar al cliente esta misma tarde. El
trabajo avanza en paralelo mientras resuelve el export.

Tampoco se adivina qué puede tener en biblioteca "un DJ de bodas típico". Sería inventar el
dato central del informe.
