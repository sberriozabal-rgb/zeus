# Caso 4 · Integration (alimenta a `set-por-encargo`)

## Situación

El cruce del caso 1 está cerrado: 19 TENGO, 3 DUDOSO resueltos por el cliente y 5 compras
hechas. Ahora hay que **montar el set del evento**, y eso lo hace `set-por-encargo`.

## Por qué se encadenan

`set-por-encargo` necesita dos cosas que este cruce produce exactamente:

1. **Un pool filtrado**, no la biblioteca entera. La regla de aquella skill es explícita: con
   la biblioteca completa el motor elige entre ruido y el set pierde criterio. El cubo TENGO
   más las compras aprobadas **es** ese pool.
2. **Las prohibiciones y los obligatorios** como parámetros duros, que son restricción
   contractual y no preferencia.

## Traducción cubo → parámetro

| Del cruce | A `set-por-encargo` |
|---|---|
| Cubo TENGO (19) + compras (5) | pool de entrada, 24 tracks confirmados |
| Cubo PROHIBIDO: Paquito, reggaetón | `--vetar "Paquito el Chocolatero"` + veto de género |
| Momento crítico: primer baile = Perfect | `--incluir "Perfect"` con posición fija |
| Tipo de evento: boda, abuela presente | versiones Clean ya resueltas en el cruce |

## Entrada encadenada

```bash
python3 ../set-por-encargo/scripts/setbuilder.py pool_boda.csv -n 46 -c arco \
  --energia-min 3 --energia-max 9 \
  --incluir "Ed Sheeran - Perfect" \
  --vetar "Paquito el Chocolatero"
```

## El hueco que aparece en el cruce de las dos skills

El pool confirmado son 24 tracks. Un banquete y baile de boda de 4 horas necesita alrededor de
46. **Faltan 22 tracks que el cliente no ha pedido y que el DJ pone de su criterio**, y esa es
una conclusión útil que ninguna de las dos skills da por separado:

> Tus invitados han pedido 24 temas. El set necesita 46. Los otros 22 los eliges tú, y son
> los que sostienen la pista entre petición y petición. Conviene que estén en la misma franja
> de energía y en claves compatibles con los confirmados.

## Verificación cruzada de versiones

Un detalle que solo se ve al encadenar: si el cruce resolvió "Despacito" a la versión original
y el pool de `set-por-encargo` trae las dos, el motor puede elegir la de Bieber por
compatibilidad armónica y **romper lo que se confirmó por escrito al cliente**. Por eso el pool
que se pasa lleva solo la versión confirmada, no las dos.

## Qué demuestra el caso

Que el cruce no es un trámite administrativo: produce el pool y las restricciones duras del
set, y además detecta cuánta música tiene que aportar el DJ de su propio criterio. La otra
integración natural es con `auditoria-de-biblioteca`, que dice si los 24 confirmados tienen
clave y BPM analizados — sin eso, `set-por-encargo` no puede ordenarlos armónicamente.
