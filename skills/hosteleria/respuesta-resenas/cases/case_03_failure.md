# Caso 3 · Failure (encargo de una línea, sin contexto)

## Encargo real que escribiría un dueño

> "me pusieron 1 estrella, ayúdame a responder"

Sin fecha, sin motivo, sin más contexto que el texto pegado en el chat.

## Entrada mínima construible

```json
{"resenas": [{"estrellas": 1, "texto": "pesimo"}]}
```

## Salida esperada — lo que se entrega igual, sin rendirse

El motor no se detiene a pedir el export completo. Con una sola reseña:

- Calcula la media (1,0 — trivial con un solo dato, pero correcta).
- Clasifica la reseña como `negativa_sin_motivo_declarado` (sin motivo explícito ni suficiente texto para inferirlo).
- No puede evaluar patrón (una sola reseña nunca supera el umbral de 3) y lo dice sin alarmismo — no es una alarma, es matemáticamente imposible detectar un patrón con un dato.
- Declara el hueco de fecha en `errores_datos`.
- Entrega igualmente una respuesta lista para usar de la categoría "negativa injusta / sin motivo verificable" (plantilla 3 de `assets/plantillas-respuestas.md`), porque con el texto "pésimo" sin más detalle, no hay hecho concreto que reconocer — se pide al cliente que aporte más contexto en el canal privado.

## Por qué es el caso decisivo

El antipatrón "caso failure cobarde" aquí sería responder "necesito más información, mándame el resto de las reseñas" y detenerse. Este motor entrega una respuesta usable inmediatamente (el dueño la puede publicar hoy) y señala, sin bloquear el trabajo, qué haría el análisis más completo si hay más datos disponibles.
