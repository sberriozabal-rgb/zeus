# Caso 1 · Happy path

## Encargo real que escribiría un chef

> "Te paso el salmón a la plancha con puré y espárragos, que es el plato que más
> vendo y el que peor sale cuando yo libro. Lo tengo apuntado: 4 raciones, 640 g
> de lomo de salmón, 800 g de patata, 120 g de mantequilla, 100 ml de nata, 12
> espárragos verdes, aceite y sal. Se hace a la plancha, piel abajo, y el puré es
> patata cocida, pasada y montada con la mantequilla y la nata. Estamos en
> Girona."

## Entrada

| Campo obligatorio | Estado | Valor aportado |
|---|---|---|
| Nombre del plato | CONFIRMADO | Salmón a la plancha con puré y espárragos |
| Rendimiento total | CONFIRMADO | 4 porciones |
| Tamaño de porción | AMBIGUO | Derivable del rendimiento |
| Ingredientes con cantidad | CONFIRMADO salvo aceite y sal | 640 g salmón · 800 g patata · 120 g mantequilla · 100 ml nata · 12 espárragos · aceite y sal sin cantidad |
| Procedimiento numerado | AMBIGUO | Descrito en prosa, sin orden ni tiempos |
| Temperaturas y tiempos | FALTA | — |
| Puntos críticos | FALTA | — |
| Mise en place | FALTA | — |
| Conservación y servicio | FALTA | — |
| Emplatado | FALTA | — |
| **País de operación** | CONFIRMADO | España (Girona) |

5 campos FALTA sobre 10 — pero cuatro de ellos (temperaturas, PCC, mise en place,
conservación) **los deriva la skill del procedimiento**, no del chef. Los campos
que quedan realmente sin dato son emplatado y las cantidades de aceite y sal.

## Salida esperada — la ficha completa

```markdown
# Salmón a la plancha con puré y espárragos

**Estado:** BORRADOR · **Versión:** v0.1 · **País de operación:** España
**Último pesaje real:** pendiente · **Escrita para:** line cook junior

## 1. Rendimiento
- Rendimiento total: 4 porciones · 1.660 g aprox. en crudo
- Porción individual: 160 g de salmón + 200 g de puré + 3 espárragos
- Tolerancia: ±10 % sobre peso de plato servido [TOLERANCIA POR DEFECTO — AJUSTAR SEGÚN PLATO]

## 2. Ingredientes
| Ingrediente | Cantidad | Unidad | Estado | Nota |
|---|---|---|---|---|
| Lomo de salmón sin espinas | 640 | g | CONFIRMADO | Compra en pieza; 160 g por ración ya porcionados |
| Patata para puré | 800 | g | CONFIRMADO | Peso en crudo, pelada |
| Mantequilla | 120 | g | CONFIRMADO | A temperatura de nevera |
| Nata 35 % MG | 100 | ml | CONFIRMADO | |
| Espárrago verde | 12 | ud | CONFIRMADO | 3 por ración |
| Aceite de oliva (plancha) | 12 | ml | ESTIMADO | [CANTIDAD ESTIMADA — VERIFICAR CON PESAJE] Punto de partida: 3 ml por ración |
| Sal | 6 | g | ESTIMADO | [CANTIDAD ESTIMADA — VERIFICAR CON PESAJE] Rango 5-8 g; partida 1,5 g por ración |

## 3. Mise en place
- Utensilios: plancha, cazo, pasapurés, varilla, espátula de pescado, **termómetro de sonda**, báscula de 1 g de precisión
- Preparación previa: salmón porcionado en 4 × 160 g y refrigerado ≤4 °C · patata pelada y troceada regular · espárragos limpios y despuntados

## 4. Procedimiento
| # | Acción | Tiempo | Temp. | Señal de que el paso terminó | PCC |
|---|---|---|---|---|---|
| 1 | Cocer la patata en agua con 3 g de sal desde frío | 18-22 min | hervor | La punta del cuchillo entra sin resistencia y sale limpia | |
| 2 | Escurrir y pasar por pasapurés en caliente | 3 min | — | Puré sin grumos visibles a contraluz | |
| 3 | Montar con mantequilla fría en dados y la nata templada | 4 min | — | Brilla y forma cinta al levantar la varilla; no se descuelga | |
| 4 | Blanquear espárragos en agua salada y cortar en agua con hielo | 2-3 min | hervor | Verde vivo, ceden al doblar sin romperse | |
| 5 | Calentar plancha con el aceite | 3 min | 200-220 °C | El aceite ondula, no humea | |
| 6 | Marcar el salmón piel abajo sin moverlo | 4-5 min | 200-220 °C | La piel se despega sola de la plancha al empujar con la espátula | |
| 7 | Voltear y terminar la cocción | 1-2 min | 200-220 °C | **Sonda en la parte más gruesa: 68 °C mantenidos 15 s** | ● |
| 8 | Regenerar puré y espárragos y montar el plato | 2 min | ≥65 °C | Puré a temperatura de pase medida con sonda | ● |

## 5. Puntos críticos de control
| Paso | Qué se controla | Umbral (temp + tiempo) | Verificación | Norma |
|---|---|---|---|---|
| 7 | Cocción del salmón | **68 °C durante 15 s** en el centro | Sonda en la parte más gruesa del lomo | AESAN-2021-004, categoría pescado |
| 8 | Mantenimiento en caliente del puré | **≥65 °C** mientras dure el servicio | Sonda en el recipiente de pase | **RD 3484/2000 art. 7** (norma reglamentaria; AESAN-2021-004 fija ≥63 °C, prevalece el RD ante inspección) |
| — | Conservación del salmón porcionado | ≤4 °C hasta el marcado | Registro de cámara del checklist de apertura | **RD 3484/2000 art. 7**: exige ≤8 °C para duración <24 h; la ficha aplica el umbral de >24 h (≤4 °C) por criterio de oficio con pescado crudo, **más estricto que el mínimo legal** |

## 6. Conservación y servicio
- Salmón porcionado: refrigerado a ≤4 °C, consumo en 24 h desde el porcionado. Las 24 h son el umbral del RD 3484/2000 art. 7 entre comida refrigerada de corta (≤8 °C) y larga duración (≤4 °C); al aplicar ya ≤4 °C, la ficha cumple ambos tramos
- Puré: caliente ≥65 °C en servicio (RD 3484/2000 art. 7); si se enfría, se regenera una sola vez a ≥74 °C/15 s (AESAN-2021-004, recalentamiento)
- Servicio: plato caliente, salmón recién marcado, no se marca por adelantado

## 7. Emplatado
[EMPLATADO PENDIENTE DE FOTO DE REFERENCIA]
- Vajilla: [pendiente de confirmar con el chef]
- Posición: puré en la base, salmón encima con la piel hacia arriba, espárragos en abanico apoyados
- Cantidades: 200 g de puré · 160 g de salmón · 3 espárragos
- Temperatura de servicio: plato ≥65 °C (RD 3484/2000 art. 7, comida preparada caliente)

## 8. Notas de escalado
No escalan linealmente: el tiempo de plancha (depende de la superficie disponible,
no del número de raciones) y el montado del puré (más volumen exige más tiempo de
varilla, no proporcional). Sí escalan: todos los gramajes de la sección 2.

## 9. Datos pendientes de verificar
- Aceite y sal — pesar en tres servicios reales y fijar la cifra
- Emplatado — foto de referencia del chef
- Vajilla — pieza concreta

## 10. Supuestos de esta ficha
- Porción de 160 g de salmón: derivada de 640 g / 4 porciones, no declarada por el chef
- Tolerancia ±10 %: valor por defecto de la casa, no normado
- Estado BORRADOR: no se ha pesado ni ejecutado ninguna vez con esta ficha delante
```

## El detalle que hace de esto un producto

El punto crítico del paso 7 sale a **68 °C durante 15 segundos**, no a 63 °C.

La v1.0.0 de esta skill habría escrito 63 °C, porque tomaba la tabla de una
fuente británica. Para un local en Girona la cifra defendible es la del informe
**AESAN-2021-004**: pescado 68 °C durante 15 s. Cinco grados y un tiempo que la
versión anterior no pedía. Si el mismo chef abriera en Monterrey, la ficha se
reescribiría a 63 °C (NOM-251 §7.3.1) — y eso es una reescritura, no una copia.

Ninguna receta de internet trae esa distinción. Es exactamente el peldaño entre
"documento bonito" y "documento que aguanta una inspección".

## Por qué es el caso central

Es el flujo esperado en una instalación real: el chef aporta gramaje y
procedimiento en prosa, y no aporta nada de lo que menos le importa y más pesa —
temperaturas, tiempos, conservación, emplatado. La skill deriva cuatro de los
cinco campos ausentes, marca los dos que no puede derivar, y entrega una ficha
que ya se puede colgar en la partida esta noche, en estado BORRADOR hasta el
primer pesaje.
