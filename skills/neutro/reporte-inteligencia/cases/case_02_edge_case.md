# Caso 2 · Edge case (dos locales propios a 900 m, panel solapado)

## Entrada

> "Reporte de mis dos locales. Están a 900 metros uno del otro, los dos en el mismo barrio."

## El problema

Con un radio de 2 km, los paneles de las dos unidades **se solapan en 4 de 6 competidores**. Si
se emite un solo reporte:

- Los cuatro solapados se cuentan dos veces en la mediana del panel.
- Los deltas de esos cuatro **se sumarían**, inflando cualquier movimiento del barrio.
- Las dos unidades propias competirían entre sí dentro de la misma tabla, y la peor arrastraría
  la lectura de la mejor.

## La salida correcta: dos reportes, no uno

```
REPORTE A — Unidad Chamberí        REPORTE B — Unidad Malasaña
  Panel propio de 6                  Panel propio de 6
  Solapados con B: 4 de 6            Solapados con A: 4 de 6
  Radio: 2 km                        Radio: 2 km
```

Cada uno con su panel, su tabla 7×8, su brecha y sus tres acciones. Y **una fila comparativa
adicional** entre las dos unidades propias, que es información que el dueño no tiene de ninguna
otra forma:

| Métrica | Chamberí | Malasaña | Delta |
|---|---|---|---|
| Nota media | 4,2 | 4,5 | −0,3 |
| Tasa de respuesta | 38 % | 74 % | −36 pp |
| Frescura | 9 % | 18 % | −9 pp |

## La declaración obligatoria

> **Solape de panel declarado.** Cuatro de los seis competidores aparecen en los dos reportes:
> [C1], [C2], [R1], [E1]. **Sus deltas no se suman.** Un movimiento de [R1] es un solo movimiento
> del barrio, no dos. Al leer los dos reportes juntos, cuenta cada competidor solapado una vez.

## Lo que el caso enseña

La comparación entre las dos unidades propias resulta más accionable que cualquiera de los dos
paneles: **Malasaña ya está haciendo bien lo que a Chamberí le falta**, y la corrección no exige
copiar a un competidor sino copiar al local de al lado, con el mismo dueño, el mismo producto y
la misma caja. La acción de 7 días de Chamberí sale de ahí.

## Lo que NO se hace

No se fusionan los dos paneles en uno de 8 o 10 competidores "para simplificar". La composición
3+2+1 es lo que garantiza que el panel incomode, y un panel de 10 diluye los dos cupos de
referencia hasta volverlos irrelevantes.
