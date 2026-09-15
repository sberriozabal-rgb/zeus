# Caso 2 · Edge case (cuatro versiones del mismo documento, sin fecha fiable)

## Situación

En la carpeta aparecen:

```
propuesta-cliente.md              modificado: 2026-07-03
propuesta-cliente-v2.md           modificado: 2026-07-19
propuesta-cliente FINAL.md        modificado: 2026-07-11
propuesta-cliente FINAL buena.md  modificado: 2026-08-02
```

Las cuatro difieren en **el precio, el alcance y el plazo**. La fecha del sistema no es fiable:
copiar un archivo la reescribe, y aquí hay indicios de que eso pasó.

## La tentación, y por qué es el peor error posible

Elegir "FINAL buena" porque es la más reciente y el nombre lo sugiere. Es exactamente el
antipatrón del promedio aplicado a versiones: **se decide por el dueño, en silencio, y todos los
maestros heredan esa decisión sin que nadie sepa que se tomó.**

Si la elección es errónea, el precio equivocado se propaga a la biblioteca entera, al resumen
ejecutivo y a la base de conocimiento del proyecto. Y no queda rastro de que hubiera alternativa.

## Lo que se hace

Se busca **marca de vigencia en el contenido**, no en el nombre ni en la fecha del sistema:
referencias internas a otros documentos fechados, número de versión declarado dentro del texto,
mención en un chat con fecha. Aquí aparece una pista parcial —un chat del 20-jul cita el alcance
de `v2`— pero **no cubre el precio**.

Resultado: **se declara conflicto y no se elige.**

```markdown
## CONFLICTOS.md

### [CONFLICTO 1] · Propuesta de cliente — 4 versiones, sin vigente identificable

| Archivo | Precio | Alcance | Plazo | Indicio de vigencia |
|---|---|---|---|---|
| propuesta-cliente.md | 3.800 € | 3 fases | 8 sem | ninguno |
| propuesta-cliente-v2.md | 4.900 € | 4 fases | 10 sem | citado en chat del 20-jul (solo alcance) |
| propuesta-cliente FINAL.md | 4.900 € | 3 fases | 8 sem | el nombre, que no es prueba |
| propuesta-cliente FINAL buena.md | 5.400 € | 4 fases | 12 sem | mtime mas reciente, no fiable |

**En el cuerpo de los maestros prevalece `v2`**, por ser la unica con indicio externo
(chat fechado), y va marcada `[CONFLICTO — vigencia no confirmada]`.

**Decision pendiente del dueno:** cual es la propuesta vigente. Afecta a precio,
alcance y plazo en los dominios 02, 03 y 05.
```

## Y en el índice también

La entrada aparece **dos veces**: en `CONFLICTOS.md` y en el índice de los tres dominios
afectados. Quien abra el maestro de precios ve el marcador ahí mismo, no enterrado en un anexo.

## Por qué es el caso decisivo

Es el escenario que distingue un compilador honesto de uno cómodo. La versión cómoda entrega una
biblioteca limpia, sin conflictos, con un precio que puede estar mal. La honesta entrega una
biblioteca con **una decisión pendiente claramente escrita**, que es exactamente lo que el dueño
necesita ver.

Resolver en silencio es decidir por él.
