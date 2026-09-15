# Métricas, fórmulas y umbrales

**Cuándo se lee:** en P2, antes de calcular cualquier métrica, y en P9 para el semáforo de alertas.

---

## 1 · Definiciones exactas

| # | Métrica | Fórmula | Ventana | Nota |
|---|---|---|---|---|
| 1 | Nota media global | La que publica la plataforma | Toda la vida del perfil | Si hay varias plataformas, se reporta cada una por separado y **nunca se promedian entre sí**: las escalas y los sesgos de muestra no son comparables |
| 2 | Volumen | Nº total de reseñas por plataforma | Toda la vida | — |
| 3 | Velocidad | (reseñas nuevas de las últimas 4 semanas) ÷ 4 | 28 días | Se compara con la velocidad del panel, no consigo misma |
| 4 | Nota reciente | Media aritmética de las últimas 20 reseñas | Últimas 20 | Es el indicador adelantado: se mueve meses antes que la métrica 1 |
| 5 | % 1–2★ | (reseñas de 1 o 2 estrellas ÷ 50) × 100 | Últimas 50 | Si hay menos de 50, se declara el N real |
| 6 | Tasa de respuesta | (reseñas con respuesta del propietario ÷ 50) × 100 | Últimas 50 | Se cuenta la respuesta visible públicamente |
| 7 | Tiempo mediano de respuesta | Mediana de (fecha respuesta − fecha reseña) | Últimas 20 respondidas | **Mediana, no media**: una respuesta a los 8 meses destroza la media |
| 8 | Frescura | (reseñas de los últimos 30 días ÷ volumen total) × 100 | 30 días | Indicador de "negocio vivo" |

**Derivada:** *desviación reciente* = métrica 4 − métrica 1. Negativa significa que el negocio está peor de lo que su nota global aparenta.

---

## 1·bis · Alcance por modo de captura `[v1.1.0]`

Qué métrica se puede obtener con cada modo declarado en P2·bis. No hay atajos: las métricas 3 a 8 exigen abrir el listado de reseñas fechado.

| Métrica | Modo BÚSQUEDA | Modo PLATAFORMA | Por qué |
|---|---|---|---|
| 1 · Nota global | ⚠️ Parcial | ✅ | El buscador la expone, pero casi nunca con fecha de captura |
| 2 · Volumen | ⚠️ Parcial | ✅ | Idem; agregadores distintos dan cifras distintas del mismo local |
| 3 · Velocidad | ❌ | ✅ | Exige contar reseñas fechadas de 28 días |
| 4 · Nota reciente | ❌ | ✅ | Exige listado ordenado por fecha |
| 5 · % 1–2★ | ❌ | ✅ | Exige filtro por estrellas |
| 6 · Tasa de respuesta | ❌ | ✅ | Exige ver las respuestas del propietario |
| 7 · T. mediano de respuesta | ❌ | ✅ | Exige fecha de reseña y fecha de respuesta |
| 8 · Frescura | ❌ | ✅ | Exige conteo fechado |

**Consecuencia:** la métrica 4 —el indicador adelantado, el que detecta la deriva de 3 a 6 meses antes— es inalcanzable en modo BÚSQUEDA. Un reporte sin métrica 4 **no tiene poder predictivo**, solo descriptivo.

**Marcas de fuente nuevas en v1.1.0:**
- `[FUENTE SIN FECHA]` — el dato existe pero no se sabe de cuándo. No entra en medianas.
- `[FUENTE INTERESADA]` — la cifra procede de la web o el material del propio negocio evaluado. Se reporta, nunca se usa sola.
- Ante dos fuentes que se contradicen: **se reportan ambas.** La discrepancia es el dato, no un problema a resolver eligiendo.

---

## 2 · Reglas de cálculo

- **Mediana del panel, no media** (regla SIEMPRE 8). Con 6 competidores, la mediana es el promedio de los valores 3.º y 4.º ordenados.
- **Un competidor con menos de 10 reseñas totales** se marca `[MUESTRA INSUFICIENTE]` y **se excluye del cálculo de las medianas**, pero permanece en el reporte con sus datos cualitativos.
- **Redondeo:** notas a un decimal, porcentajes a entero, tiempos a la hora entera si superan las 24 h.
- **Multiplataforma:** el reporte usa una plataforma **ancla** por sector (ver `fuentes-por-sector.md`) para la serie temporal, y las demás como contexto. Cambiar de ancla rompe la serie igual que cambiar el panel.

---

## 3 · Umbrales de alerta `[CONVENCIÓN]`

Estos cortes son convenciones de la skill, calibradas para que salten pocas veces y por algo real. No proceden de una fuente externa.

| Alerta | Disparador | Acción que fuerza |
|---|---|---|
| 🔴 **Deriva de calidad** | Desviación reciente ≤ −0,3 | Entra obligatoriamente en la sección 6 (fallos propios) |
| 🔴 **Racha negativa** | ≥ 3 reseñas de 1–2★ en 7 días | Genera una de las 3 acciones de la semana |
| 🔴 **Silencio** | Tasa de respuesta < 50 % | Acción de 7 días, coste cero |
| 🟠 **Rezago de panel** | Peor que la mediana en ≥ 3 de las 8 métricas | Se declara en el resumen ejecutivo |
| 🟠 **Perfil apagado** | Frescura < 5 % o velocidad < 0,5/semana | Se contrasta con la velocidad del panel antes de alarmar |
| 🟠 **Lentitud** | Tiempo mediano de respuesta > 72 h | Acción de 7 días |
| 🟡 **Competidor acelerando** | Un competidor duplica su velocidad respecto a la media del panel durante 3 semanas seguidas | Pasa a vigilancia; se busca la causa en sus reseñas de P3 |

**Falsa alarma más común:** un pico de velocidad en un competidor coincidiendo con una fecha señalada de la plaza (fiesta local, evento, temporada). Antes de reportar aceleración, comprobar si el pico es simultáneo en varios competidores: si lo es, es la plaza, no él.

---

## 4 · Ejes de clasificación cualitativa (P3)

| Eje | Qué recoge | Ejemplos de queja |
|---|---|---|
| Producto | Lo que se entrega | Calidad, cantidad, temperatura, acabado, defecto |
| Servicio y tiempos | El trato y la espera | Espera, trato, error en el pedido, seguimiento |
| Precio-valor | La relación entre lo pagado y lo recibido | "Caro para lo que es", cargos sorpresa |
| Entorno y limpieza | El sitio | Ruido, aseos, temperatura, accesibilidad |
| Canal digital | Todo lo previo y posterior a la visita | Reserva, pedido, entrega, web, respuesta online |

Una reseña puede tocar varios ejes: se cuenta en todos los que menciona explícitamente, nunca en los que se infieren.
