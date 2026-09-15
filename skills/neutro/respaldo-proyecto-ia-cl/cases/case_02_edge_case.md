# Caso 2 · Edge case (export sin campo de proyecto)

## Situación

El export llega, pero **no trae el campo que identifica a qué proyecto pertenece cada chat**.
Hay 340 conversaciones en la cuenta y entre ellas están las del proyecto, mezcladas con todo lo
demás.

## La única vía disponible, y su trampa

Filtrar por **coincidencia de texto**: buscar en las conversaciones los términos propios del
proyecto (nombre del cliente, nombre del método, títulos de documentos de la base de
conocimiento).

Funciona a medias, y las dos mitades fallan en direcciones opuestas:

```
FILTRO POR TEXTO -> 58 chats candidatos   [INDICIO]

Revision manual (obligatoria):
  - 3 arrastrados que NO son del proyecto
      * 2 mencionan al cliente pero en una conversacion personal
      * 1 cita el nombre del metodo en una consulta general
  - 1 del proyecto que el filtro NO cogio
      * hablaba del tema sin nombrar nunca al cliente ni al metodo

Seleccion final: 56 chats  (58 - 3 + 1)
```

## La regla que evita el desastre silencioso

> **El campo de proyecto es prueba; el texto es indicio.** Una selección `[INDICIO]` **nunca se
> da por buena sin revisarla**.

Los dos errores tienen coste distinto y ninguno es aceptable:

- **Arrastrar un chat ajeno** mete conversación personal —que es C2 por defecto— en un paquete
  que quizá se entregue a otra persona. Es una fuga de datos personales por descuido de filtro.
- **Dejar fuera un chat propio** pierde para siempre una conversación que sí era del proyecto,
  y nadie se entera hasta que hace falta.

## Lo que se declara en el paquete

```markdown
## HUECOS.md
Ninguno.

## Supuestos de esta versión
Seleccion de chats por COINCIDENCIA DE TEXTO [INDICIO], no por campo de proyecto:
el export no lo incluia. 58 candidatos -> revision manual -> 56 seleccionados
(3 descartados por ser ajenos, 1 anadido a mano que el filtro no cogio).
La seleccion NO es exhaustiva por construccion: puede quedar fuera algun chat
que no mencione ningun termino del proyecto.
```

Esa última frase es la importante: **se declara que el método tiene un límite estructural**, no
se presenta el resultado como completo.

## Por qué es el caso decisivo

Es el escenario en que un respaldo automático parecería haber funcionado perfectamente —58 chats
recuperados, ningún error— y habría metido tres conversaciones personales en un paquete ajeno y
perdido una propia. **La revisión manual no es una recomendación: es parte del procedimiento.**
