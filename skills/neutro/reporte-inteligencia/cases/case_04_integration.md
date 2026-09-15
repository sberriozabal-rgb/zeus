# Caso 4 · Integration (encadenado con `respuesta-resenas`)

## Situación

El reporte de la semana 1 está emitido. Entre los cinco fallos propios, dos son de servicio y
uno de producto, todos sostenidos por citas de reseñas. La pregunta inmediata del dueño es:

> "Vale, ¿y ahora qué les contesto a esos?"

Eso lo hace `respuesta-resenas`, y este caso define cómo se le pasa el trabajo sin que se pierda
nada por el camino.

## El bloque HANDOFF

El reporte cierra con un bloque en tabla, sin prosa, listo para consumir por otra skill:

```markdown
## HANDOFF

### Fallos propios (5) — lista plana
| # | Fallo (en palabras del cliente) | Eje | Frecuencia | Cita de apoyo |
|---|---|---|---|---|
| 1 | "tardan 40 minutos en traer la comida" | Servicio | 11 menciones / 50 | [fecha, plataforma] |
| 2 | "el camarero no volvió a pasar" | Servicio | 7 / 50 | [fecha, plataforma] |
| 3 | "la carne llegó fría" | Producto | 5 / 50 | [fecha, plataforma] |
| 4 | "no cogen el teléfono para reservar" | Acceso | 4 / 50 | [fecha, plataforma] |
| 5 | "caro para lo que es" | Precio | 3 / 50 | [fecha, plataforma] |

### Acciones de 7 días (3)
| Acción | Dueño | Métrica de verificación + fecha |
|---|---|---|

### Panel congelado
| Competidor | Perfil | Fecha de descongelación |
|---|---|---|
```

## Por qué encaja exactamente con `respuesta-resenas`

Aquella skill declara patrón con **3 o más menciones del mismo motivo en 60 días**. Este reporte
ya entrega la frecuencia contada y la cita con fecha, así que los cinco fallos llegan **con el
umbral de patrón ya resuelto**: los cinco lo superan.

Lo que hace `respuesta-resenas` con eso:

- Redacta la respuesta pública de cada reseña, mencionando el detalle concreto de cada una.
- Confirma o desmiente el patrón con su propio conteo sobre la ventana de 60 días.
- Traduce la tendencia de estrellas a rango de ingresos con la elasticidad de Luca.

## La verificación cruzada que solo aparece al encadenar

El reporte mide la **tasa de respuesta del propietario** como métrica 6 y el **tiempo mediano de
respuesta** como métrica 7, y la brecha del caso 1 las situaba en 5.º y 6.º de 7. Al ejecutar
`respuesta-resenas` sobre los fallos de este handoff, **las dos métricas se mueven directamente**:
responder las 50 reseñas pendientes es a la vez la acción de aquella skill y la métrica de
verificación de esta.

El reporte de la semana siguiente lo comprueba sin preguntar a nadie: tasa de respuesta ≥ 70 % y
tiempo mediano < 24 h, o no se hizo.

## El límite que se respeta al encadenar

El reporte **no** propone las respuestas. Produce la evidencia con fuente y fecha; la redacción
es de la otra skill, y la firma del dueño. Y ninguna de las dos recomienda jamás solicitar,
comprar, incentivar ni suprimir reseñas: está prohibido por norma y por política de plataforma.
