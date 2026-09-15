# Caso 4 · Integration (encadenado con otra skill)

## Encargo real que escribiría un dueño

> "Ya vi que mi merluza está sangrando margen [con escandallo-ingenieria-menu]. Ahora resulta que también me están cayendo reseñas quejándose de la merluza. ¿Tiene esto relación?"

## Cómo se encadena

1. `escandallo-ingenieria-menu` ya identificó que "Merluza a la plancha" tiene una desviación entre food cost teórico y real de más de 5 puntos — señal de problema de control (porcionado, mermas), no solo de precio.
2. `respuesta-resenas` procesa el export de reseñas y detecta que 3 reseñas negativas en los últimos 45 días mencionan específicamente ese plato ("la merluza estaba pasada", "poca cantidad", "no como la primera vez que vine") — supera el umbral de patrón.
3. El punto de conexión (`metadata.enlaza_con: escandallo-ingenieria-menu`) es cualitativo: cuando ambos informes señalan el mismo plato desde ángulos distintos (cifras internas de coste vs. percepción pública), el hallazgo se refuerza mutuamente y sube de prioridad.

## Qué entrega este caso

Una sección de cierre añadida al informe estándar de `respuesta-resenas`:

```
## 7. Relación con tu análisis de carta
Tu informe de ingeniería de menú marcó "Merluza a la plancha" con una
desviación de food cost de 6,2 puntos — señal de problema de control,
no de receta. Las reseñas confirman el síntoma desde fuera: 3 quejas
en 45 días mencionan textualmente ese plato ("pasada", "poca cantidad",
"no es como antes"). Esto ya no es una coincidencia entre dos informes
distintos: es el mismo problema visto desde dos ángulos. Prioridad alta.
```

## Formato de entrega en la integración

Mismo formato de salida que el caso estándar, con la sección 7 añadida solo cuando el dueño aporta o referencia un informe previo de `escandallo-ingenieria-menu` Y el motivo detectado en las reseñas coincide con un plato nombrado en ese informe. Si no coincide, la sección no aparece.

## Por qué importa

Es la tercera pieza que demuestra que el sistema instalable no es una colección de seis análisis sueltos: comparte el mismo lenguaje de cifras y puede citar hallazgos de sus hermanas sin inventar nada — la diferencia entre "paquete" y "sistema" que exige la Escalera de Producto de TROQUEL.
