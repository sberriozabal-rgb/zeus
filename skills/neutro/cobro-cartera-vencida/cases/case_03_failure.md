# CASO 03 · FAILURE (falta información crítica)
`[DATOS DE EJEMPLO — NO REALES]`

**Escenario:** listado incompleto — sin fechas de vencimiento y sin cifra de ventas del periodo. Prueba de que la skill **entrega algo útil igualmente** en vez de rendirse. Fecha de hoy: 2026-08-11.

## ENTRADA (deliberadamente rota)

Texto pegado de un correo, sin estructura:

```
Nos deben:
- Cliente Ronda: como 30 mil, factura de hace tiempo
- Óvalo SA: 12.500, la de mayo
- (una línea ilegible) ... 4.000 ...
- Cliente Norte: 8.900, creo que de junio
```

- No hay fechas de vencimiento.
- No hay cifra de ventas del periodo (no se puede calcular DSO).
- Una línea sin cliente identificable.

## SALIDA ESPERADA — cómo se defiende la skill

**NO responde "faltan datos, mándame más".** Entrega:

1. **Tabla normalizada de lo procesable (P1):**
   - Ronda: importe ~30.000 `[IMPORTE APROXIMADO]`, sin vencimiento → `[PLAZO ASUMIDO 30D]` desde la fecha de emisión si se recupera; mientras, marcada como no clasificable en tramo.
   - Óvalo SA: 12.500, "la de mayo" → asume vencimiento 2026-05-31 `[FECHA INFERIDA]` → T2 (72 d).
   - Norte: 8.900, "de junio" → asume 2026-06-30 `[FECHA INFERIDA]` → T2 (42 d).

2. **LÍNEAS NO PROCESABLES:** la línea ilegible de 4.000 (sin cliente) → listada aparte, fuera del cálculo.

3. **Cuadro de mando parcial:**
   - Total vencido procesable: ~51.400
   - DSO: `[NO CALCULABLE — falta cifra de ventas del periodo]`
   - Importe en riesgo: `[NO DETERMINABLE — faltan fechas de vencimiento confirmadas]`

4. **Acciones que sí se pueden dar:**
   - Óvalo y Norte → A2 reclamación formal (T2), con mensaje redactado.
   - Ronda → primero **recuperar la fecha de la factura**: tarea pendiente concreta, no un escalón.

5. **TAREAS PENDIENTES entregadas como lista accionable:**
   - [ ] Confirmar fecha de vencimiento de las 3 facturas.
   - [ ] Identificar el cliente de la línea de 4.000.
   - [ ] Aportar ventas del trimestre para calcular DSO.

**Qué demuestra este caso:** el criterio de paso de la FASE 5 — el caso failure no termina
en "pide más datos" a secas. Entrega la parte procesable con supuestos etiquetados, aísla
lo no procesable, y convierte lo que falta en una lista de tareas de 3 puntos, no en un muro.
