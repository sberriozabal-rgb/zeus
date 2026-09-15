# Caso 2 · Edge case

## Encargo real que escribiría un dueño

> "Aquí van cuatro reseñas de limpieza que me han caído, algunas las apunté a mano y no tengo la fecha de una."

## Entrada

```json
{"resenas": [
  {"estrellas": 2, "fecha": "2026-05-01", "motivo": "limpieza", "texto": "mesa sucia"},
  {"texto": "sin estrellas puesto por error de captura"},
  {"estrellas": 1, "motivo": "limpieza", "texto": "otra vez sucio, sin fecha capturada"},
  {"estrellas": 2, "fecha": "2026-05-20", "motivo": "limpieza", "texto": "tercera vez"}
]}
```

La segunda reseña no tiene `estrellas` (dato sucio real). La tercera no tiene `fecha`.

## Salida esperada

El motor descarta la reseña 1 (sin estrellas) del cálculo de media y lo declara en `errores_datos`. Sigue con las tres reseñas de "limpieza" válidas.

**El hallazgo clave de este caso**: con las dos reseñas que sí tienen fecha (05-01 y 05-20), la ventana de 60 días solo cuenta 2 menciones — por debajo del umbral de 3. Un motor ingenuo diría "no es patrón, es ruido". Este motor detecta que hay una tercera mención del mismo motivo sin fecha, y en vez de ocultar esa ambigüedad, la declara explícitamente: `posible_patron_oculto_por_fecha_faltante: true`, con el aviso "pide las fechas exactas antes de descartarlo como ruido". No decide en silencio.

## Por qué importa

Es la misma disciplina que `control-no-shows` aplicó con el ticket medio ausente: un hueco de dato no se rellena con un valor cómodo (aquí, "no es patrón") cuando esa conclusión podría estar equivocada precisamente por el hueco. Se declara la incertidumbre, no se resuelve a favor de la respuesta más simple.
