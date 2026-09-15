# Caso 4 · Integration (encadenado con `respuesta-resenas`)

## Situación

El reporte del caso 1 cerró con la tasa de respuesta en **rojo (35 % frente al 74 % de la
mediana)** y con una queja propia repetida 3 veces: *"no contestan a las reseñas"*.

La acción 1 era responder las 44 reseñas pendientes. **Eso no lo hace esta skill**: lo hace
`respuesta-resenas`, y aquí se define cómo se le pasa el trabajo.

## El límite que se respeta

Esta skill **nunca responde reseñas**. Es una regla NUNCA explícita: mezclarlo rompe el límite
del artefacto. Produce la evidencia y la prioridad; la redacción y la firma son de la otra pieza
y del dueño.

## Qué se le pasa exactamente

```markdown
## HANDOFF -> respuesta-resenas

### Prioridad de respuesta (de la brecha del semaforo)
Tasa de respuesta: 35% propia vs 74% mediana del panel -> ROJO
Pendientes: 44 resenas sin respuesta, de las cuales 9 son de 1-2*

### Quejas propias detectadas, con frecuencia y ancla
| Tema | Menciones | Plataforma | Fechas |
|---|---|---|---|
| "tardaron media hora en traer la cuenta" | 4 | Google | [fechas] |
| "no contestan a las resenas" | 3 | TripAdvisor | [fechas] |

### Lo que hacen los competidores que funciona
- [C1] y [C5] responden a todas en menos de 24 h
- [C1] menciona el nombre del camarero en la respuesta
```

## Por qué encaja con el umbral de la otra skill

`respuesta-resenas` declara patrón con **3 o más menciones del mismo motivo en 60 días**. Los dos
temas de este handoff llegan con **4 y 3 menciones** ya contadas y ancladas a plataforma y fecha:
**el umbral de patrón viene resuelto**, y la otra skill puede confirmarlo con su propio conteo sin
partir de cero.

## La verificación cruzada de la semana siguiente

Aquí está lo que hace útil el encadenado: la acción que ejecuta `respuesta-resenas` **es la
métrica que mide este reporte**. No hace falta preguntar a nadie si se hizo.

| Métrica | Corte actual | Objetivo | Se verifica |
|---|---|---|---|
| Tasa de respuesta | 35 % 🔴 | ≥ 70 % | próximo corte semanal |
| Queja "no contestan" | 3 menciones | 0 nuevas | próximo corte semanal |

Si en el corte siguiente la tasa sigue en 35 %, la acción no se hizo. El semáforo no admite
excusas porque mide desde fuera, exactamente igual que lo ve un cliente.

## La otra dirección del encadenado

`respuesta-resenas` traduce la tendencia de estrellas a rango de ingresos con la elasticidad de
Luca (+5-9 % por estrella, **solo en independientes**). Este reporte aporta el dato que aquella
necesita para hacerlo bien: la **posición contra la mediana del panel**, que es lo que dice si
media estrella de mejora te mete o no en el set de elección del 31 % que solo usa negocios de
4,5★+.
