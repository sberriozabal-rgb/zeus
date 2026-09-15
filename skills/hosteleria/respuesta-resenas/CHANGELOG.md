# Changelog — respuesta-resenas

## 1.0.0 — 2026-08-11

Creación inicial.

- Clasificación de reseñas en 4 categorías (positiva, negativa con motivo, negativa injusta/sin motivo, mixta) con plantilla de respuesta específica por categoría.
- Detección de patrones operativos: motivo repetido ≥3 veces en 60 días, con fuente y umbral declarados en `references/umbrales-resenas.md`.
- Traducción de tendencia de estrellas a rango de impacto en ingresos (+5% a +9% por +1 estrella, Luca/HBS, solo en independientes), siempre presentado como escenario de referencia, nunca como promesa — cumple el gate de la doctrina "no se promete resultado económico".
- Script determinista `scripts/resenas.py` con 6 comprobaciones aritméticas en `--autotest`, todas en verde.
- Corrección de antipatrón "caso failure cobarde" descubierta en la prueba del caso edge: cuando una mención de un motivo repetido carece de fecha, el sistema ya no la descarta en silencio del cálculo de patrón — declara explícitamente `posible_patron_oculto_por_fecha_faltante` para que el hueco de dato no oculte una señal operativa real.
- Plantillas de respuesta (`assets/plantillas-respuestas.md`) para las 4 categorías, más una variante para cuando el problema señalado ya se corrigió.
- Auditoría interna: 19/20. Pendiente para v1.1: referencias externas adicionales sobre cadencia óptima de solicitud de reseñas (hoy marcada [SIN VERIFICAR]).

## Roadmap v1.1

- Verificar con fuente fechada la cadencia óptima de solicitud de reseñas (hoy es criterio de oficio sin cifra de mercado).
- Explorar el cruce automático (no solo cualitativo) con `escandallo-ingenieria-menu`: si el nombre de un plato aparece tanto en una reseña negativa como en la lista de platos con desviación de food cost, marcarlo automáticamente como prioridad alta.
