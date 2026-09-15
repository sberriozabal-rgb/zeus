# Caso 1 · Happy path

## Encargo real que escribiría un dueño

> "Te paso un export de las últimas reseñas de Google de los últimos dos meses. Contéstame las que tienen menos de 3 estrellas y dime si hay algo que se repite."

## Entrada

7 reseñas de ejemplo (`scripts/resenas.py --ejemplo`): mezcla de positivas (5, 4 estrellas), negativas con motivo (tiempo de espera repetido 3 veces, precio 1 vez), y una mixta de 3 estrellas.

## Salida esperada

1. Media actual: 2,57 estrellas.
2. Patrón detectado: "tiempo_espera" con 3 menciones en 35 días (05-06 a 10-07), supera el umbral — se marca como patrón operativo, no como clientes difíciles sueltos.
3. "precio" con solo 1 mención — bajo el umbral, no se prioriza.
4. Respuestas redactadas para las 5 reseñas negativas/mixtas (4 negativas con motivo + 1 mixta), cada una con detalle específico de su texto, sin plantilla repetida.
5. Escenario de impacto: con una mejora de 0,5 estrellas en la media, el rango de referencia de mercado es +2,5% a +4,5% en ingresos (Luca/HBS), declarado explícitamente como escenario, no promesa.

## Por qué es el caso central

Cubre el flujo completo: reseñas mixtas, un patrón real que supera el umbral y uno que no, y el cálculo de impacto con su fuente — el camino esperado en la mayoría de instalaciones reales.
