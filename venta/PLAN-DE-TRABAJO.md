# FORJA · Plan de trabajo de la venta del catálogo

**Versión** 1.1.0 · **Fecha** 15-sep-2026 · **Responsable** Sergio Berriozábal Serrano · OCTAVA
**Objetivo** 3.000 USD netos al mes en el canal en línea · **2.600 €** al cambio del 15-sep
(EUR/USD 1,1536, [Trading Economics](https://tradingeconomics.com/euro-area/currency)) ·
51.420 MXN al tipo de cambio del 15-sep (17,14)
**Estado** Fase 0 abierta. Ninguna de las tres fases siguientes puede arrancar hasta cerrarla.

> **Cambios respecto a la v1.0.0 (misma fecha).** La v1.0 se escribió sin el repositorio delante
> y se contradecía con él en cuatro puntos. Decidido por Sergio el 15-sep-2026
> (`catalogo/DECISIONES.md`, puntos 8, 9 y 10):
>
> | Punto | v1.0 decía | v1.1 (manda) |
> |---|---|---|
> | Tarifa | CABINA CORE 249 USD · cobro 69 USD | **La del repo**: los dos primeros productos son **CABINA COMPLETA 249** (las seis) y **cobro 79**; CORE sigue a 149 € en la tarifa. Punto 9, con palabras de Sergio |
> | Canal | Gumroad | **Gumroad** se confirma (punto 8). Polar, que era la doctrina, queda como caída si Gumroad no paga a México |
> | Conformidad | "14 skills no validan" | **Las 17 del catálogo validan** la especificación (frontmatter y licencia verificados dos veces el 15-sep). El parche de frontmatter es para la carpeta original de 78, no para el repo |
> | Tercer tramo | Suscripción sin precio | **Instalación Esencial** de hostelería (2.500 €), el único producto con cartera propia |
>
> Las fases 0.2, 1.2–1.4 y 2 de la v1.0 se conservan; cambian las cifras y desaparece la skill
> gratuita del marketplace (punto 6 de los pendientes de `DECISIONES.md`).

---

## 0 · Dónde estamos, en una línea

El producto está terminado, el precio firmado y el canal decidido. **Lo que falta no es producto:
es que la tienda abra y que exista una sola cifra de cliente que respalde la promesa.**

| Frente | Estado |
|---|---|
| Producto (17 skills, 12 productos comprables) | Cerrado · 20/20 mecánico en las 17 |
| Precio | Firmado el 15-sep · G3 17/17 |
| Canal (Gumroad para catálogo · Stripe MX / transferencia para instalación) | Decidido el 12-sep, confirmado el 15-sep |
| Textos de venta y licencia | Escritos: `venta/GUMROAD-ALTA.md` (dos productos, campo por campo), `LICENSE`, `LICENSE.txt` por skill |
| Paquetes | `venta/empaquetar_gumroad.py` genera el zip de cada producto sin ficha ni `metadata.json` |
| Conformidad del catálogo | **Las 17 validan** |
| Tienda abierta | **No** |
| Prueba con cifra | **Ninguna** · G2 0/17 |

---

## 1 · Las cuatro fases

### Fase 0 · La puerta — día 1

Nada de lo que sigue tiene sentido hasta que esto esté hecho. Son cuarenta minutos.

| # | Acción | Quién | Tiempo | Criterio de salida |
|---|---|---|---|---|
| 0.1 | **No aplicar** el parche de frontmatter sobre la carpeta original. Si se quiere que la carpeta original coincida con el repo, se sustituyen las 17 carpetas originales por las de `skills/` | Sergio | 10 min | Una sola copia de cada skill vendible: la del repo |
| 0.2 | Abrir la cuenta de Gumroad (`venta/GUMROAD-ALTA.md`, bloque 0), **verificar identidad y configurar el método de cobro desde México el mismo día**, W-8BEN incluido | Sergio | 30 min | Umbral de pago en 10 USD, no en 100. Método de cobro a México confirmado; si sólo aparece PayPal, ver §4 |

> **Por qué la verificación va hoy y no cuando venda.** La revisión de cuenta nueva corre entre una
> y tres semanas en paralelo `[según informe FORJA v1.1.0; sin segunda comprobación, el proxy de
> las sesiones bloquea gumroad.com]`. Si se deja para el final, esas semanas se suman en vez de
> solaparse.

### Fase 1 · Abrir el canal — días 2 a 4

| # | Acción | Quién | Tiempo | Criterio de salida |
|---|---|---|---|---|
| 1.1 | `python3 venta/empaquetar_gumroad.py cabina-completa` y `... cobro-cartera-vencida` | Sergio | 2 min | Dos zips en `dist/`, sin ficha comercial ni `metadata.json` dentro |
| 1.2 | Alta de **CABINA COMPLETA (249)** y **cobro-cartera-vencida (79)** con la hoja `venta/GUMROAD-ALTA.md`, bloques 1 y 2. Precio en EUR si Gumroad lo admite; si sólo USD, la cifra se mantiene y se anota | Sergio | 30 min | Los dos enlaces directos responden, buscador interno apagado |
| 1.3 | Comprarse el propio producto con descuento del 100 % | Sergio | 10 min | Ve el correo, el enlace y el zip como los ve el comprador |
| 1.4 | Apuntar la comisión exacta del desglose de esa transacción | Sergio | 2 min | Se cierra el hueco de si el 10 % + 0,50 incluye el procesamiento de tarjeta |
| 1.5 | ~~Repositorio público `octava-skills`~~ ✅ **Publicado el 15-sep por orden del titular** (decisión 10): <https://github.com/sberriozabal-rgb/octava-skills>, con las 17 fichas, el marketplace validado y `apertura-cierre-turno` abierta | Hecho | — | Los enlaces de compra de las fichas apuntan a Gumroad: el paso 1.2 los pone en marcha |
| 1.6 | myClaude: **sólo** tras confirmar por escrito que actúa como *merchant of record* o asumir el IVA europeo. Sin exclusividad ni cuota de alta | Fábrica escribe · Sergio decide | 20 min | Respuesta escrita de myClaude en la carpeta |

### Fase 2 · La prueba — días 5 a 20

**Ésta es la fase que decide si el negocio existe.** Las anteriores son administrativas. Es el
gate G2 de la casa, y es el único que sigue en 0/17.

| # | Acción | Quién | Criterio de salida |
|---|---|---|---|
| 2.1 | Un DJ con biblioteca real (2.000 tracks o más, un año de uso) ejecuta `auditoria-de-biblioteca` | Sergio consigue al DJ | Declaración escrita: tracks marcados y en qué categoría, tiempo que dedicaba antes a revisar, fallos en cabina en tres meses |
| 2.2 | Una empresa con cartera vencida ejecuta `cobro-cartera-vencida` | Sergio consigue la empresa | Declaración escrita: importe recuperado, semanas transcurridas, horas semanales que dedicaba antes |
| 2.3 | Un restaurante de la cartera propia ejecuta la **Instalación Esencial** (escandallo + proveedores + turno) | Sergio · `venta/GUION-VISITA.md` | La cifra del escandallo y el ahorro de la comparativa, verificados por el dueño esa tarde |
| 2.4 | Reescribir el bloque 3 de cada ficha con la cifra y su origen; quitar el condicional | Fábrica | La promesa deja de ir en condicional y el precio sube de fuente 3 a fuente 2 o 1 |

**El trato en 2.1 y 2.2:** gratis a cambio del permiso escrito para publicar la cifra. Los correos
están en `venta/MENSAJES.md`, sin enviar. **En 2.3 no:** la instalación se cobra desde la primera,
porque es el producto con precio de servicio y la doctrina prohíbe regalarlo.

### Fase 3 · El tráfico — desde el día 6, en paralelo

| Vía | Coste | Qué aporta |
|---|---|---|
| Gumroad, enlace directo (sin buscador interno) | 10 % + 0,50 | El canal de conversión del catálogo |
| Landing propia con botón de WhatsApp | 0 | El canal real de conversión de la casa, sobre todo para la instalación |
| Una publicación por semana sobre un problema real con su cifra | tiempo | Lista de correo, no aplausos. El 42 % de las ventas de producto digital viene del correo (`catalogo/PRECIOS.md`, anclas) |
| myClaude / directorios | 8 % + Stripe | Tráfico, no margen: empata con Gumroad en unidades. Sólo tras cerrar el hueco del IVA (§5) |
| Repositorio público `octava-skills` | 0 | Sólo si aparece una skill de captación que no sea de pago. **Distribuye e instala, no vende** |

> **La advertencia que conviene tener escrita.** CABINA vende a DJ y cobro de cartera vende a
> empresas: no comparten un solo comprador. La cartera de contactos de Sergio es de restaurantes,
> y a un restaurante no se le vende ninguno de los dos. **Por eso el tercer tramo es la instalación
> de hostelería y no una suscripción:** es el único producto para el que ya hay a quién llamar. Al
> DJ hay que ir a buscarlo donde está.

---

## 2 · La aritmética que gobierna el objetivo

Precios firmados y comisión real de Gumroad, **verificada el 15-sep-2026**: el 10 % + 0,50 USD
**no incluye** el procesamiento de tarjeta, que va aparte (≈ 2,9 % + 0,30 USD); coste efectivo
≈ 12,9 % + 0,80 USD por venta directa ([Swell](https://www.swell.is/content/gumroad-pricing),
[Checkout Page](https://checkoutpage.com/blog/how-gumroad-pricing-works-and-a-cheaper-alternative),
[InsightRaider](https://insightraider.com/en/answers/how-much-does-gumroad-cost-per-month)). Las ventas
por el buscador interno (Discover) pagan un 30 % plano: por eso se apaga. Las cuotas son las de la
decisión 9.

| Producto | Precio | Neto por unidad, cobrando en EUR | Neto si Gumroad sólo admite USD | Cuota/mes |
|---|---|---|---|---|
| CABINA COMPLETA | 249 | 216,2 € | 187,3 € (216,1 USD) | **7** |
| Cobro de cartera vencida | 79 | 68,1 € | 59,0 € (68,1 USD) | **15** |
| Instalación Esencial (transferencia, sin comisión) | 2.500 € | 2.500 € | — | **una cada 6 meses** |

**22 ventas al mes entre los dos productos cubren 2.535 € netos (97 %) si Gumroad cobra en euros;
2.196 € (84 %) si sólo admite dólares.** En los dos casos una Instalación Esencial cada seis meses
(417 €/mes) cierra el objetivo. Gumroad muestra precios en EUR pero procesa en USD al cambio del
momento ([Gumroad Help](https://gumroad.com/help/article/149-adding-a-product)): la cifra en euros
es la que ve el comprador; lo que entra en cuenta es dólares.

**Cambiar de canal no ahorra ni una venta:** Polar (5 % + 1,5 % internacional + 0,50) daría 232,4 €
y 73,4 € netos, unos 240 € más al mes con las mismas 22 unidades, y entregaría por acceso revocable
al repositorio. Se decidió Gumroad por el IVA resuelto y por no reabrir una decisión ya tomada dos
veces; Polar es la caída si Gumroad no paga a México. **A 15-sep no hay confirmación de que Polar
pague a México** (su lista de países no se pudo leer desde aquí); de Gumroad sí la hay (§3).

---

## 3 · El reloj del dinero

Que no se confunda lentitud administrativa con fracaso comercial. **Verificado el 15-sep-2026**
([Gumroad Help — Getting paid](https://help.gumroad.com/article/13-getting-paid),
[InsightRaider](https://insightraider.com/en/answers/when-does-gumroad-pay-out)).

| Hito | Cuándo |
|---|---|
| Venta hecha | día 0 |
| Retención antes de poder cobrarla | 7 días |
| Los pagos salen los viernes, por ventas hasta el viernes anterior | el viernes siguiente |
| Mínimo para que salga el pago | 10 USD acumulados; si no, pasa a la semana siguiente |
| Verificación de identidad (KYC de Stripe) | la pide tras cierto volumen; hacerla el día 1 para que no frene el primer pago |
| **Cobro a México** | **Transferencia a banco local mexicano, soportada** ([Gumroad: local bank account support](https://gumroad.gumroad.com/p/local-bank-account-support-in-more-countries)). PayPal ya no es método de pago de Gumroad desde oct-2024. Lo que no hay en México es la conexión directa de Stripe, que no afecta al cobro |

**Entre la primera venta y el primer ingreso pasan de dos a tres semanas.** Es el calendario, no
un problema. La instalación de hostelería no tiene este reloj: se cobra por transferencia el día
que se firma.

---

## 4 · Riesgos, con su señal de alarma

| Riesgo | Señal de que está pasando | Qué hacer |
|---|---|---|
| El tráfico no llega | La tienda abierta y sin visitas a los 14 días | No bajar precio. Ir a buscar al DJ donde está: foros, grupos, residentes conocidos |
| La promesa no convence sin cifra | Visitas sin compra | Acelerar la fase 2. Es el hueco, no el precio |
| CABINA COMPLETA a 249 no aguanta en directorios | Cero ventas en myClaude y sí en el enlace directo | Confirmado: ese precio se defiende en página propia, no en estante. Ante negociación se quita alcance, jamás se baja el precio |
| Gumroad no paga a México por transferencia | El alta de cobro no ofrece banco mexicano (contra lo que dice su blog) | Caer a Polar con `venta/POLAR-CONFIGURACION.md`, previa confirmación de que Polar sí paga a México |
| La tienda se llama CABINA y el producto de cobro vive ahí | Un director financiero pregunta qué es CABINA | Asumido el 12-sep. Casi nadie llega por la portada |
| Dos tarifas circulando | Alguien cita «CORE 249 USD» o «cobro 69 USD» | La v1.0 está retirada. Toda cifra sale de `catalogo/PRECIOS.md` |
| El zip se comparte | Un comprador lo pasa a diez colegas | Desviación asumida de la doctrina (decisión 8). La licencia lo prohíbe; el remedio real es la fase 2: la cifra de cliente no se copia con el zip |
| `receta-estandar` se vende antes de G4 | Un cliente sigue una ficha con un binomio `[A VALIDAR]` sin validar | Decisión 11: se vende dentro de la Completa. Mitigación: no se entrega sin el anexo de inocuidad firmado, y la revisión del consultor sigue abierta y se comunica al cliente en cuanto llegue |

---

## 5 · Los huecos abiertos y quién los cierra

| Hueco | Responsable |
|---|---|
| **La prueba con cifra, en los tres productos** | Sergio · tres conversaciones. Estado del pipeline real en [`PIPELINE.md`](PIPELINE.md) |
| ~~Si el 10 % + 0,50 incluye el procesamiento~~ **No lo incluye** (verificado 15-sep, §2). El paso 1.4 sólo confirma la cifra exacta | Sergio · paso 1.4 |
| ~~Qué método de cobro ofrece Gumroad desde México~~ **Banco local** (verificado 15-sep, §3). El paso 0.2 lo comprueba en el alta | Sergio · paso 0.2 |
| ~~Si Gumroad admite precio en EUR~~ **Muestra EUR, cobra en USD** (verificado 15-sep, §2) | — |
| Si Polar paga a México (sólo importa si Gumroad falla) | La fábrica, cuando el proxy deje leer polar.sh |
| Si myClaude y SkillHQ actúan como *merchant of record* o el IVA europeo es del vendedor | **Correos redactados** (15-sep): en borradores de Gmail y en [`CONSULTAS-PENDIENTES.md`](CONSULTAS-PENDIENTES.md). Falta el destinatario, que Sergio toma de cada web al enviar |
| Cómo se entra en el directorio `claudemarketplaces.com` | **Correo redactado** (15-sep), mismo sitio. Sólo se envía si se decide publicar el marketplace gratuito |
| Si existe una skill de captación que no sea de pago (hoy no) | Sergio |
| Revisión externa de inocuidad de `receta-estandar` (único G4 abajo) | Sergio · consultor |
| Revisión del abogado de `venta/ANEXO-CONTRATO-INOCUIDAD.md` | Sergio · abogado |
| Tipo de cambio para facturar en pesos | El día que se factura |

Cerrados respecto a la v1.0: conformidad de las 17 (validan), licencia de las 17 (declarada),
precio del tercer tramo (Instalación Esencial), precio de la suscripción (no hay suscripción),
qué producto de CABINA sale primero (COMPLETA, no CORE), skill gratuita del marketplace (no).

---

## 6 · La regla que no se toca

**No se fabrica una skill nueva hasta que estas tres estén vendidas a alguien que pagó.** El
catálogo tiene 17 piezas listas y ninguna venta; el problema no se arregla con la 18.

---

## Documentos de esta carpeta

| Archivo | Qué es |
|---|---|
| `venta/LISTA-DE-VENTA.md` | La lista maestra: hecho / pendiente / de quién, producto a producto |
| `venta/PLAN-DE-TRABAJO.md` | Este documento. El plan operativo, v1.1 |
| `venta/PIPELINE.md` | El pipeline real: la campaña del 7-sep prospecto a prospecto, con la acción siguiente de cada uno |
| `venta/GUMROAD-ALTA.md` | La cuenta, los 15 productos campo por campo (descripción, tags, portada), la política de devolución |
| `venta/portadas/` · `venta/generar_portadas.py` | Cover y thumbnail de cada producto de Gumroad, generadas desde la hoja de alta |
| `venta/OFERTA-HOSTELERIA.md` | Ficha de producto de las instalaciones Esencial y Completa |
| `venta/empaquetar_gumroad.py` | Genera en `dist/` el zip de cada producto sin material de fábrica |
| `venta/POLAR-CONFIGURACION.md` | Histórico; es la caída si Gumroad no paga a México |
| `venta/GUION-VISITA.md` · `venta/MENSAJES.md` | La visita de hostelería y los correos de la fase 2 |
| `venta/ANEXO-CONTRATO-INOCUIDAD.md` | Cláusula de `receta-estandar`, pendiente de abogado |
| `catalogo/PRECIOS.md` · `catalogo/DECISIONES.md` · `catalogo/ESTADO-GATES.md` | La tarifa, sus razones y la matriz de gates |

La v1.0 de este plan, el informe `FORJA_Estado_Canales_y_GitHub_v1_1`, el `.pptx` de ocho láminas y
los dos zips (`OCTAVA-repo-github-v1.0.0`, `myclaude-cobro-cartera-vencida-v1.1.0`) quedan en la
carpeta del proyecto como histórico. **`OCTAVA-repo-github-v1.0.0.zip` no se sube a ningún
repositorio público: lleva `apertura-cierre-turno`, que es de pago.**
