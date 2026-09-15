# Anexo A — Ficha comercial

| Campo | Valor |
|---|---|
| Nombre técnico | `reporte-inteligencia-competencia` |
| Nombre comercial | Radar semanal de competencia |
| Peldaño | P1 · SKILL |
| Línea / Paquete | Hostelería · vertical de `reporte-inteligencia` |
| Comprador nombrado | Dueño de restaurante independiente en España o México, con ficha activa en Google y **competencia identificable en su zona** que pueda nombrar. Decide y paga el dueño. |
| Quien NO es comprador | El local sin competencia local identificable, y quien quiera un informe único: **el producto es la serie semanal**, y un corte aislado no tiene brecha anterior contra la que compararse ni acciones que verificar. Tampoco un grupo o cadena: la elasticidad de nota que sostiene el argumento está medida solo en independientes. |
| Trabajo que quita | Mirar a ojo las fichas de los de al lado cada cierto tiempo, sacar impresiones sin fecha ni cita, y no poder distinguir si algo ha cambiado de verdad o es la memoria del que mira. |
| Umbral que aporta | Los **cuatro cortes de decisión con fuente**: 4,5★ (el 31 % solo usa negocios por encima), 20 reseñas (el 47 % evita los que tienen menos), 14 días de recencia (el 32 % solo se fía de las últimas dos semanas) y 100 % de tasa de respuesta (más del 80 % cree que hay que responder a todas). Más la **regla del 5.0** —la diana es 4,5-4,8, porque un 5,0 clavado se lee como falso— y el uso de **mediana y no media**, que es lo que impide que un competidor con 5,0 y 6 reseñas dispare una falsa alarma. |
| Límite declarado | Solo fuentes públicas, sin paneles privados ni datos personales. **No responde reseñas**: eso es `respuesta-resenas`. No es *due diligence* ni asesoría legal o financiera. Y los umbrales de comportamiento son de panel estadounidense: `[CONTEXTO EE. UU. — A VALIDAR para ES/MX]`, **no se usan como promesa de venta sin esa etiqueta**. |
| Precio propuesto | No se vende suelta en su forma actual. Candidata a **suscripción semanal** dentro de la línea de hostelería, por ser un producto de serie y no de corte único. `[A VALIDAR — pendiente de ratificación por escrito de Sergio]` |
| Razón del precio | Es la única pieza de la línea cuyo valor está en la cadencia, no en el entregable: un corte vale poco y doce cortes valen mucho. La doctrina de la casa dice que la suscripción promedia casi el doble que el pago único, **pero exige cadencia real que la sostenga**, y eso es una decisión de operación, no de producto. |
| Canal | Dentro del sistema instalable de hostelería (Motor B), o suscripción por Polar si se decide el modelo de serie. |
| Motor | B · Instalación |
| Frase de anuncio | «Cada lunes: cómo vas contra los seis de tu zona, qué hacen ellos que tú no, y tres cosas para esta semana.» |
| Estado / Versión | ACORDADO / v1.1.0 |
| Auditoría | **19/20** (`validar_skill.py`, 15-sep-2026). El validador devuelve 20/20 mecánico; **no se firma el 20** porque el punto 19 exige URLs verificadas y no se han reconfirmado una a una. Antes de esta revisión medía **1/20** y no declaraba nota en su ficha, porque no tenía ficha. |
| Gates | G1 [x] G2 [ ] G3 [ ] G4 [x] G5 [ ] |

## Notas de gates

- **G1 (producto)** levantado el 15-sep-2026: 19/20 desde **1/20** medido. La nota baja era de
  estructura: los cuatro cortes con fuente, los 8 pasos, la plantilla de una página y el pie legal
  ya estaban. Lo que faltaba era el envoltorio y **todos** los ficheros del peldaño: no tenía
  `README`, ni `CHANGELOG`, ni `LICENSE`, ni `metadata.json`, ni `cases/`, ni `references/`.
- **G2 (prueba)** pendiente: los cuatro casos son de fabricación.
- **G3 (precio)** pendiente, y aquí hay además una **decisión de modelo sin tomar**: corte suelto
  o suscripción semanal. Es la única pieza del catálogo cuyo valor depende de la cadencia.
- **G4 (legal)** en orden y con dos salvaguardas propias: el **pie legal literal** en toda
  entrega (fuentes públicas, no *due diligence*, no asesoría) y la regla de **detener la ficha de
  un competidor** con el que el cliente tenga relación contractual o personal.
- **G5 (público)** pendiente.

## Solape comercial declarado

Esta pieza es la **vertical de hostelería de `reporte-inteligencia`**: mismo panel de seis, misma
lógica de mediana y brecha, cuatro métricas en vez de ocho y salida de una página en vez de diez
secciones. **No se venden las dos al mismo comprador.** A un restaurante se le vende esta; a
cualquier otro sector, la neutra.
