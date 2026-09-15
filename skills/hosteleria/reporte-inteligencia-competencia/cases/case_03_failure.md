# Caso 3 · Failure (sin competidores aportados y solo ficha de Google)

## Entrada

> "Hazme el reporte de competencia de mi bar."

Sin nombres de competidores. Al buscar, el local solo tiene ficha en Google: no aparece en
TripAdvisor, no está en TheFork, no tiene agregador de delivery ni Instagram con actividad.

## Lo que NO se hace

No se responde "necesito que me digas contra quién quieres compararte". Se piden **una vez**, y
si no llegan, se produce igual.

Y sobre todo: **no se adivinan los competidores**. Rellenar el panel con los seis bares más
cercanos en el mapa es la regla NUNCA de esta skill, porque proximidad geográfica no es
competencia: el bar de menús de obra a 80 metros no compite con una coctelería.

## Salida real — el reporte se emite con lo que hay

```
REPORTE DE INTELIGENCIA — [Marca] · Semana del [fecha]
>> PANEL INCOMPLETO: el dueno no aporto competidores.
>> Se trabaja con 3 localizados por categoria y rango de ticket, NO por cercania.
>> [COMPETIDOR NO APORTADO] x3

SEMAFORO (marca vs. mediana de 3 competidores)
                     Marca      Mediana comp.   Brecha   Estado
Calificacion (*)      4.0          4.4           -0.4     AMBAR
Volumen resenas        31          128           -97      AMBAR
Recencia (dias)        26            4           -22      ROJO
Tasa de respuesta      0%           67%          -67pp    ROJO

COBERTURA DE FUENTES
Google         .... ficha activa
TripAdvisor    .... [SIN DATO PUBLICO] — sin ficha
TheFork        .... [SIN DATO PUBLICO] — sin ficha
Agregador      .... [SIN DATO PUBLICO] — sin presencia
```

## El hallazgo que sale precisamente de lo que falta

> **Estás en una sola de las seis fuentes que consulta tu cliente.** El consumidor mira **seis
> plataformas de media** y Google ya solo pesa un 71 %, cayendo desde el 83 %. Ahora mismo, al
> 29 % que no empieza por Google **no existes**.
>
> Esto no es un hueco del reporte: es el hallazgo principal del corte. `[SIN DATO PÚBLICO]` en
> tres de cuatro fuentes **es** el diagnóstico.

## Tres acciones, y las dos primeras son gratis

1. **Crear** ficha en TripAdvisor y completarla — responsable: dueño — para: **jueves**
2. **Responder** las 31 reseñas de Google, empezando por las de 1-2★ — responsable: dueño — para: **domingo**
3. **Mandar** por WhatsApp la lista de seis competidores reales para el próximo corte — responsable: dueño — para: **lunes**

La tercera cierra el hueco del panel para la semana siguiente, y es trabajo de dos minutos del
dueño, no del analista.

## Los supuestos declarados

> **Asumido**: sin competidores aportados, se han localizado **3** por categoría y rango de
> ticket dentro del radio, no por cercanía. Van marcados `[COMPETIDOR NO APORTADO]` y **el panel
> no se da por válido**: la mediana de tres es orientativa y la brecha puede moverse bastante
> cuando llegue el panel real.
>
> Tres de las cuatro fuentes están en `[SIN DATO PÚBLICO]` porque el local no tiene ficha, no
> porque no se hayan consultado. **No se ha estimado ninguna métrica.**
>
> Umbrales de comportamiento `[CONTEXTO EE. UU. — A VALIDAR ES/MX]`.

## Por qué es el caso decisivo

El dueño pidió saber cómo va contra su competencia y se lleva algo que no esperaba y vale más:
que su problema no es la competencia, es que **solo existe en una plataforma de seis**. Y dos
acciones gratis que puede hacer este fin de semana.
