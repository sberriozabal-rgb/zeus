# Caso 2 · Edge case (dos plataformas divergen sobre el mismo local)

## Situación

Al capturar la ficha de la marca propia:

```
FUENTE          CALIFICACION   RESENAS   CONSULTADO
Google              4.1          68       [fecha] 11:20
TripAdvisor         3.4          52       [fecha] 11:26
```

**0,7 estrellas de diferencia** sobre el mismo restaurante, el mismo día, con volúmenes
parecidos. No es un decimal de redondeo: es una divergencia real.

## Lo que NO se hace

**No se promedia en silencio.** Un "3,75" en la tabla sería un número que no existe en ninguna
parte, que el dueño no puede recomprobar en ninguna ficha, y que además **escondería el único
hallazgo interesante del corte**.

Tampoco se elige la fuente que más conviene. Quedarse con Google porque es la nota más alta es la
versión cobarde del mismo error.

## Lo que se hace: reportar ambas, y convertir la divergencia en el hallazgo

```
SEMAFORO (marca vs. mediana de 6 competidores)
                     Marca            Mediana comp.   Brecha    Estado
Calificacion (*)     4.1 G / 3.4 TA       4.35        -0.25/-0.95  AMBAR/ROJO
                     >> DIVERGENCIA DE FUENTES: 0.7* entre Google y TripAdvisor
```

Y arriba del todo, como hallazgo principal:

> **Hallazgo del corte: tu nota depende de dónde te miren.** En Google estás en 4,1 y en
> TripAdvisor en 3,4. Son 0,7 estrellas de diferencia sobre el mismo restaurante. Dado que el
> consumidor consulta **seis fuentes de media**, el que te descubra por TripAdvisor te ve por
> debajo del corte de 4,0, que es donde el 31 % deja de considerarte.

## Por qué la divergencia es información y no un problema de medición

Se comprueban las dos fichas y aparece el motivo, que es accionable:

- En Google se responde al 35 % de las reseñas; **en TripAdvisor al 0 %**.
- Las reseñas de TripAdvisor son de media **más antiguas** (la más nueva, de hace 40 días) y
  concentran quejas de una etapa anterior del local.

La divergencia no es ruido: es **una plataforma abandonada**. Y eso no se habría visto nunca si
las dos notas se hubieran promediado.

## Las tres acciones que salen de aquí

1. **Reclamar y actualizar** la ficha de TripAdvisor — responsable: dueño — para: **miércoles**
2. **Responder** las reseñas de TripAdvisor empezando por las más recientes — responsable: encargado — para: **viernes**
3. **Pedir** reseña en TripAdvisor específicamente al cliente satisfecho de fin de semana — responsable: jefe de sala — para: **desde el sábado**

## Supuestos de esta versión

> Divergencia declarada y **no promediada**. La brecha se reporta contra las dos notas. La
> mediana de competidores se calcula sobre Google, que es la fuente donde los siete tienen ficha
> activa; los tres competidores con ficha de TripAdvisor se anotan aparte y **no entran en esa
> mediana** por muestra desigual.
