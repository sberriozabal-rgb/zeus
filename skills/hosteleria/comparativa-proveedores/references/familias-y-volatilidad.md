# Familias, volatilidad, IVA y formatos

Referencia de apoyo para `comparativa-proveedores`. Léela cuando tengas que juzgar si una subida es normal, decidir si dos precios son comparables, o normalizar una unidad rara.

Índice:
1. Volatilidad de precio por familia
2. Formatos de compra y sus factores
3. Tipos de IVA aplicables
4. Trucos de proveedor documentados
5. Umbrales de decisión

---

## 1. Volatilidad de precio por familia

La **volatilidad** es cuánto se mueve el precio de un producto por causas ajenas al proveedor: temporada, lonja, cosecha, clima. Una subida dentro del rango volátil normal **no es abuso del proveedor**: es mercado. El análisis la marca como estacional y no la cuenta como sobrecoste evitable, porque perseguir al proveedor por una subida de temporada hace perder el tiempo al dueño.

| Familia | Volatilidad | Lectura |
|---|---|---|
| Pescado y marisco fresco | **Muy alta** | Cambia por lonja y día. Una subida del 20–30% en temporada baja es normal. No se renegocia: se cambia el plato del día o se sube el precio del plato. |
| Verdura y fruta de hoja/temporada | **Alta** | Sigue la cosecha. El tomate de invierno cuesta el doble que el de agosto. |
| Aceite de oliva | **Alta pero estructural** | Sube por cosecha, pero cuando sube no vuelve solo. Sí se renegocia y se compara. |
| Huevo | **Media** | Sensible a costes de pienso y sanidad avícola. |
| Carne (vacuno, cerdo, ave) | **Media** | Tendencia estructural más que estacional. Comparable y negociable. |
| Lácteos y quesos | **Media-baja** | Contratos más estables. |
| Secos, harinas, legumbre, pasta, arroz | **Baja** | Precio estable. Cualquier subida clara es estructural y negociable. |
| Bebida, refresco, cerveza, agua | **Baja** | Tarifa de fabricante. Se negocia por volumen, no por temporada. |
| Limpieza, papel, desechables | **Baja** | Negociable por volumen. |

**Regla operativa**: las familias marcadas "muy alta" y "alta de temporada" entran en la lista `volatiles` del script y sus subidas se separan. Las de volatilidad baja o estructural son las que de verdad se pueden atacar renegociando o cambiando de proveedor.

---

## 2. Formatos de compra y sus factores

El proveedor factura por su formato de venta; tú decides por unidad base. Estos son los formatos habituales y a qué base se llevan. **Siempre pide el peso/volumen real del formato**: una "caja" no es una unidad de medida.

| Formato típico | Base | Cómo normalizar |
|---|---|---|
| Garrafa de aceite 5 L | L | precio ÷ 5 |
| Garrafa 10 L | L | precio ÷ 10 |
| Saco de harina 25 kg | kg | precio ÷ 25 |
| Saco de patata 20/25 kg | kg | precio ÷ peso real |
| Caja de fruta/verdura | kg | precio ÷ kg reales de la caja (varía) |
| Caja de pescado | kg | precio ÷ kg reales (ojo al hielo: pesa el neto) |
| Bandeja/estuche de carne | kg | precio ÷ kg de la bandeja |
| Docena de huevos | ud | precio ÷ 12 |
| Barril de cerveza 30 L | L | precio ÷ 30 |
| Pack/retractilado de X unidades | ud | precio ÷ X |
| Cuñas o piezas de queso | kg | precio ÷ kg de la pieza |

**Errores clásicos de normalización:**
- El pescado se factura por peso **con hielo o sin él**: usa el neto escurrido, o el rendimiento saldrá falso.
- La caja de fruta no trae siempre los mismos kilos: no asumas un peso fijo entre semanas.
- El mejillón y productos con concha: el precio por kg bruto no dice nada del coste real de la carne (ver `escandallo-ingenieria-menu` para rendimientos).

---

## 3. Tipos de IVA aplicables

Se compara **sobre base imponible, sin IVA**. Estos son los tipos vigentes para alimentación; el script descuenta el IVA si el precio viene con él.

**España (verificado 10-ago-2026, a validar con asesor):**
- Alimentos básicos (pan, leche, huevos, frutas, verduras, legumbres, cereales): **4%** superreducido. *Nota: hubo rebajas temporales al 0–5% en 2023–2024 sobre básicos y aceite/pasta; comprobar el tipo vigente en la fecha del albarán antes de descontar.*
- Resto de alimentos y bebidas sin alcohol: **10%** reducido.
- Bebidas alcohólicas y refrescos con azúcar añadido: **21%** general.

**México (verificado 10-ago-2026, a validar con contador):**
- La mayoría de alimentos no procesados: **tasa 0%** (no confundir con exento).
- Alimentos preparados para consumo, y ciertos productos: **16%** general.

Cuando no sepas con certeza el tipo, **no lo adivines**: pregunta o marca la línea como "IVA por confirmar" en el informe. Descontar un 10% donde tocaba 4% mueve la comparación casi seis puntos.

---

## 4. Trucos de proveedor documentados

No para acusar a nadie, sino para que el dueño mire donde no suele mirar. Todos son prácticas reales del sector, no invención.

**Reducción de formato (shrinkflation).** Mismo precio de caja, menos gramos dentro. El precio de línea no cambia, el €/kg sí. El script lo detecta y lo marca; es la subida que más agradece un dueño porque no la puede ver en el albarán.

**Portes intermitentes.** El transporte aparece en unas facturas y no en otras, o se factura aparte para que la línea de producto "parezca" barata. Súmalo al coste real.

**Precio de lista vs. precio pactado.** Se acuerda un descuento por volumen y "se olvida" de aplicarse en algunas líneas. Cruza el precio facturado con el pactado si lo tienes.

**Mínimo de pedido.** Un producto barato por kg puede salir caro si el mínimo de pedido te obliga a comprar más del que gastas antes de que caduque. El coste real incluye la merma por caducidad.

**Escalado silencioso.** Subidas pequeñas y frecuentes (1–2% cada pocas semanas) que individualmente no disparan ninguna alarma pero suman dos o tres puntos al trimestre. Por eso el análisis compara el primer precio del periodo con el último, no albarán contra albarán.

---

## 5. Umbrales de decisión

Rangos de referencia para calibrar el análisis. Sirven para juzgar, no para sentenciar.

| Señal | Umbral orientativo | Acción |
|---|---|---|
| Subida entre dos fechas (familia estable) | **≥ 8%** | Alerta: renegociar o comparar. |
| Subida entre dos fechas (familia volátil) | ≥ 8% | Marcar estacional, revisar en el cambio de temporada. |
| Diferencia entre dos proveedores, mismo producto | > 40–50% | Sospecha de que **no es el mismo producto**: verificar calidad/calibre antes de recomendar cambio. |
| Impacto de una subida | **> 300 €/año** | Merece entrar a negociar. Por debajo, anotar pero no priorizar. |
| Ahorro por cambio de proveedor | **> 500 €/año** | Merece pedir oferta formal y considerar el cambio, valorando servicio y plazo. |

Estos umbrales son orientativos y calibrables por cliente: un grupo con central de compras negocia distinto que un local de barrio. El valor de la instalación está precisamente en ajustar estos números a los datos de ESE negocio, no en dejar los de fábrica.
