# Caso 4 · Integration (recibe de `postmortem-de-bolo`)

## Situación

Residencia mensual. El bolo anterior se analizó con `postmortem-de-bolo` y el parte cerró con
dos decisiones. Este caso muestra cómo entran en el set de este mes.

## Las decisiones del parte anterior

1. Retrasar el pico de tempo unos 20 min: el mes pasado se llegó a 131,5 BPM a la 01:15, solo
   45 minutos después de llenarse, y el DJ notó pérdida ahí.
2. Preparar tres tracks puente en 5A/6A para el tramo 01:15–01:45, que concentró dos saltos
   armónicos de 6 pasos.

## Traducción a parámetros

| Decisión | Parámetro |
|---|---|
| Retrasar el pico | curva `arco` con pico al **75%** del slot (por defecto 70%) |
| Tres puentes 5A/6A | `--incluir` los tres, con restricción de 2 pasos máx. en ese tramo |
| El cierre fue el más sostenido (7:12) | entra como obligatorio de cierre |
| Tres tracks cortados < 90 s | `--vetar` los tres para este slot |
| El DJ anterior cerró a 124 | `--bpm-entrada 124` |

## Ejecución

```bash
python3 scripts/setbuilder.py pool.csv -n 48 -c arco \
  --energia-min 3 --energia-max 9 --pico 0.75 \
  --bpm-entrada 124 \
  --incluir "Puente 5A" --incluir "Puente 6A" --incluir "Puente 5A bis" \
  --incluir "Cierre sostenido" \
  --vetar "Track corto 1" --vetar "Track corto 2" --vetar "Track corto 3"
```

## Verificación cruzada

El parte del mes que viene comprobará si funcionó, y las dos decisiones nacieron con su forma
de comprobación:

- Decisión 1 → ¿la curva llega al máximo **después de la 01:30**?
- Decisión 2 → ¿cuántos saltos armónicos ≥3 pasos hay en el tramo 01:15–01:45? Objetivo: cero.

## La otra integración

Los tres tracks puente en 5A/6A **solo se pueden buscar si la biblioteca tiene la clave
analizada**. Ahí conecta con `auditoria-de-biblioteca`: sus hallazgos `sin_clave` son
exactamente el pool que esta skill no puede usar. En el cruce documentado en aquel caso, 58 de
420 tracks candidatos (13,8%) quedaban fuera del set armónico por un metadato que falta.

## Qué demuestra el caso

Que las tres skills de CABINA CORE forman un ciclo: la auditoría limpia el pool, el set se
construye sobre él, el parte mide qué pasó, y sus decisiones vuelven al set siguiente como
parámetros. Ninguna de las tres cierra el bucle sola.
