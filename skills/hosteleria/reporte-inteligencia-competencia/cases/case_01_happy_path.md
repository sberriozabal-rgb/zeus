# Caso 1 · Happy path (seis competidores aportados, tres plataformas)

## Entrada

> "Somos [Marca], en Lavapiés, Madrid. Mis competidores son estos seis: [C1] a [C6].
> Quiero saber cómo voy contra ellos."

Los seis aportados por el dueño, con ficha en Google, TripAdvisor y un agregador de delivery.

## Captura (paso 3) — con fecha de consulta

```
LOCAL      CALIF.  RESENAS  RESENA MAS NUEVA  RESPONDE
[Marca]     4.1      68       hace 19 dias      parcial (35%)
[C1]        4.6     240       hace 2 dias       si (100%)
[C2]        4.3     112       hace 5 dias       si (88%)
[C3]        4.4      95       hace 3 dias       parcial (60%)
[C4]        3.9     310       hace 1 dia        no (0%)
[C5]        4.7     180       hace 4 dias       si (95%)
[C6]        4.2      54       hace 11 dias      parcial (40%)
Consultado: [fecha] 11:20 · Google + TripAdvisor + [agregador]
```

## Semáforo (pasos 4 y 5) — contra la MEDIANA, no la media

```
                     Marca      Mediana comp.   Brecha   Estado
Calificacion (*)      4.1          4.35          -0.25   AMBAR
Volumen resenas        68           137           -69     AMBAR
Recencia (dias)        19             3.5        -15.5    ROJO
Tasa de respuesta     35%            74%          -39pp   ROJO
```

**Nota de atípico:** [C4] tiene 310 reseñas con 3,9★. Con media, el volumen mediano habría salido
disparado y la brecha de la marca habría parecido peor de lo que es. Por eso mediana.

## Lo que hacen bien ellos (paso 6, ≥3 menciones)

- **Responden a todas las reseñas en menos de 24 h** — [C1], [C5] · Google · [fechas]
- **Mencionan el nombre del camarero en la respuesta** — [C1] · Google · [fechas]
- **Publican el plato del día a diario** — [C2], [C5] · [agregador] · [fechas]

## Lo que hacemos peor

- **"Pedimos la cuenta y tardaron media hora"** — Google · [fecha] · 4 menciones
- **"No contestan a las reseñas"** — TripAdvisor · [fecha] · 3 menciones

La segunda es literalmente la métrica en rojo del semáforo: **el cliente lo está diciendo en voz
alta y la tabla lo confirma**. Esa coincidencia es la que convierte un número en una acción.

## Tres acciones para esta semana

1. **Responder** las 44 reseñas sin respuesta, empezando por las de 1-2★ — responsable: encargado — para: **viernes**
2. **Fijar** rutina diaria de respuesta al cerrar caja — responsable: encargado — para: **lunes**
3. **Pedir** reseña al cliente satisfecho al cobrar, sin incentivo — responsable: jefe de sala — para: **desde el martes**

Ninguna cuesta dinero. Las tres atacan las dos métricas en rojo.

## Supuestos de esta versión

> Panel completo: los seis aportados por el dueño, ninguno inferido. Tres plataformas cubiertas
> en los siete locales. Sin divergencias entre fuentes en este corte. Umbrales de comportamiento
> `[CONTEXTO EE. UU. — A VALIDAR ES/MX]`.

## Por qué es el caso central

De una captura de 40 minutos salen **tres acciones de coste cero con día de entrega**, y la razón
por la que son esas tres es una tabla de cuatro filas que el dueño puede recomprobar él mismo
abriendo las fichas.
