# CHANGELOG — reporte-inteligencia

## 1.1.0 — 16-ago-2026 · parche de modo de captura

Origen: primera ejecución real de la skill (Semana 0, taquería de CDMX, 2026-08-16). El dry-run destapó un supuesto no declarado del protocolo.

### Añadido
- **P2·bis · Declarar el MODO DE CAPTURA**, paso bloqueante. Distingue modo BÚSQUEDA (alcanza métricas 1 y 2) de modo PLATAFORMA (alcanza 1 a 8) y prohíbe mezclarlos en una misma serie.
- Regla **SIEMPRE 9**: declarar el modo de captura en la cabecera.
- Regla **NUNCA 8**: no declarar cerrada una línea base levantada en modo BÚSQUEDA.
- **Antipatrón 6 · La línea base de escaparate**, marcado `[OBSERVADO]`. Primer antipatrón de esta skill procedente de uso real y no de derivación.
- Sección **1·bis** en `references/metricas-y-umbrales.md`: tabla de alcance métrica por métrica y por modo.
- Marcas de fuente `[FUENTE SIN FECHA]` y `[FUENTE INTERESADA]`; regla de reportar ambas fuentes cuando se contradicen.
- Campos `Modo de captura` y `Estado de línea base` en la cabecera y en el bloque HANDOFF de `assets/plantilla-reporte.md`.

### Corregido
- **Estimación de tiempo de la DEFINICIÓN OPERATIVA.** Decía 45 minutos; medía solo la redacción y omitía la captura. Sustituida por un desglose por fase y por modo: ~1 h 15 min en modo BÚSQUEDA, 6–8 h en modo PLATAFORMA. Segundo fallo de estimación temporal en esta skill; la causa localizada es haber cronometrado el entregable en vez del levantamiento.

### Pendiente
- Reauditar con la rúbrica de 20 puntos (nota vigente 18/20, anterior al parche).
- Convertir los antipatrones 1 a 5 de `[DERIVADO]` a `[OBSERVADO]`: requiere 3 reportes reales más.
- Discrepancia de registro: el inventario apuntaba v1.2.0 / 19-20 para esta skill; en disco estaba 1.0.1 / 18-20. Conciliar antes de empaquetar para venta.

## 1.0.1 — 16-ago-2026 · auditoría del segundo lote

### Corregido
- `LICENSE.txt` añadido: había campo `license` pero no el archivo.
