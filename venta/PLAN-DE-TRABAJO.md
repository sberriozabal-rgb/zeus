# FORJA · Plan de trabajo de la venta del catálogo

**Versión** 1.1.0 · **Fecha** 15-sep-2026 · **Responsable** Sergio Berriozábal Serrano · OCTAVA
**Objetivo** 3.000 USD netos al mes en el canal en línea · **2.600 €** al cambio del 15-sep
(EUR/USD 1,1536, [Trading Economics](https://tradingeconomics.com/euro-area/currency)) ·
51.420 MXN al tipo de cambio del 15-sep (17,14)
**Estado** Fase 0 abierta. Ninguna de las tres fases siguientes puede arrancar hasta cerrarla.

> **Cambios respecto a la v1.0.0 (misma fecha).** La v1.0 se escribió sin el repositorio delante
> y se contradecía con él en cuatro puntos firmados el mismo día. Decidido por Sergio el
> 15-sep-2026, tras la reconciliación:
>
> | Punto | v1.0 decía | v1.1 (manda) |
> |---|---|---|
> | Tarifa | CABINA CORE 249 USD · cobro 69 USD | **La del repo**: CORE **149 €**, COMPLETA **249 €**, cobro **79 €** (`catalogo/PRECIOS.md`, ratificada 15-sep) |
> | Canal | Gumroad (10 % + 0,50) | **Polar** (5 % + 0,50 en plan gratuito, *merchant of record*, entrega por acceso al repo). `venta/POLAR-CONFIGURACION.md` |
> | Conformidad | "14 skills no validan" | **Las 17 del catálogo validan** la especificación (frontmatter y licencia verificados 15-sep). El parche de frontmatter es para la carpeta original de 78, no para el repo |
> | Tercer tramo | Suscripción sin precio | **Instalación Esencial** de hostelería (2.500 €), el único producto con cartera propia |
>
> Las fases 0.2, 1.2–1.4 y 2 de la v1.0 se conservan; sólo cambian el canal y las cifras.

---

## 0 · Dónde estamos, en una línea

El producto está terminado, el precio firmado y el canal decidido. **Lo que falta no es producto:
es que la tienda abra y que exista una sola cifra de cliente que respalde la promesa.**

| Frente | Estado |
|---|---|
| Producto (17 skills, 12 productos comprables) | Cerrado · 20/20 mecánico en las 17 |
| Precio | Firmado el 15-sep · G3 17/17 |
| Canal (Polar para catálogo · Stripe MX / transferencia para instalación) | Decidido en doctrina, confirmado el 15-sep |
| Textos de venta y licencia | Escritos (`venta/`, `LICENSE`, `LICENSE.txt` por skill) |
| Conformidad del catálogo | **Las 17 validan** |
| Tienda abierta | **No** |
| Prueba con cifra | **Ninguna** · G2 0/17 |

---

## 1 · Las cuatro fases

### Fase 0 · La puerta — día 1

Nada de lo que sigue tiene sentido hasta que esto esté hecho. Son cuarenta minutos.

| # | Acción | Quién | Tiempo | Criterio de salida |
|---|---|---|---|---|
| 0.1 | **No aplicar** el parche de frontmatter sobre la carpeta original. Si se quiere que la carpeta original coincida con el repo, se sustituyen las 17 carpetas originales por las de `skills/` | Sergio | 10 min | Una sola copia de cada skill vendible; la del repo |
| 0.2 | Crear la organización en Polar con datos fiscales, conectar GitHub a `sberriozabal-rgb/zeus` y **verificar identidad y método de cobro a México el mismo día** | Sergio | 30 min | Polar concede y revoca acceso al repo en una compra de prueba. Si no lo hace, no se publica nada |

> **Por qué la verificación va hoy y no cuando venda.** La revisión de cuenta nueva corre en
> paralelo. Si se deja para el final, ese tiempo se suma en vez de solaparse. Y el cobro a México
> vía Stripe Connect Express es el único punto del canal que no está confirmado (§5): si falla,
> se cae a Gumroad ese mismo día, con la aritmética de §2 rehecha al 10 % + 0,50.

### Fase 1 · Abrir el canal — días 2 a 4

| # | Acción | Quién | Tiempo | Criterio de salida |
|---|---|---|---|---|
| 1.1 | Alta en Polar de los 12 productos de `venta/POLAR-CONFIGURACION.md`, empezando por **CABINA CORE**, **CABINA COMPLETA** y **cobro-cartera-vencida** | Sergio | 45 min | Los tres enlaces directos responden |
| 1.2 | Comprarse el propio producto con cupón del 100 % | Sergio | 10 min | Ve el correo, la invitación al repo y la carpeta como los ve el comprador; al cancelar, pierde el acceso |
| 1.3 | Apuntar la comisión exacta del desglose de esa transacción | Sergio | 2 min | Se confirma si el 5 % + 0,50 incluye procesamiento y si aplica el 1,5 % de tarjeta internacional |
| 1.4 | Repositorio público `octava-skills` **sólo con las skills abiertas** (`[A DECIDIR: cuáles y con qué licencia]`, §5). Ninguna de las 17 de pago va ahí | Sergio | 15 min | `/plugin marketplace add sberriozabal-rgb/octava-skills` instala las abiertas y nada más |
| 1.5 | myClaude: **sólo** si confirma por escrito que actúa como *merchant of record* y entrega por acceso, no por zip (§5). Hasta entonces no se publica | Fábrica escribe · Sergio decide | 20 min | Respuesta escrita de myClaude en la carpeta |

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
| Repositorio público `octava-skills` con las abiertas | 0 | Captación. **Distribuye e instala, no vende** |
| Polar (página de producto propia) | 5 % + 0,50 | El canal de conversión del catálogo |
| Landing propia con botón de WhatsApp | 0 | El canal real de conversión de la casa, sobre todo para la instalación |
| Una publicación por semana sobre un problema real con su cifra | tiempo | Lista de correo, no aplausos. El 42 % de las ventas de producto digital viene del correo (`catalogo/PRECIOS.md`, anclas) |
| myClaude / directorios | 8 % + Stripe | Sólo tras cerrar el hueco de §5 |

> **La advertencia que conviene tener escrita.** CABINA vende a DJ y cobro de cartera vende a
> empresas: no comparten un solo comprador. La cartera de contactos de Sergio es de restaurantes,
> y a un restaurante no se le vende ninguno de los dos. **Por eso el tercer tramo es la instalación
> de hostelería y no una suscripción:** es el único producto para el que ya hay a quién llamar. Al
> DJ hay que ir a buscarlo donde está.

---

## 2 · La aritmética que gobierna el objetivo

Precios firmados, comisión de Polar en plan gratuito con el recargo de tarjeta internacional
incluido (5 % + 1,5 % + 0,50 USD ≈ 0,43 €). Fuente de las comisiones:
[polar.sh/docs/merchant-of-record/fees](https://polar.sh/docs/merchant-of-record/fees). La
comisión de retirada (2 USD el mes que hay pago + 0,25 % + 0,25 USD) es despreciable a este
volumen y no se descuenta por unidad.

| Producto | Precio | Neto por unidad (Polar) | Cuota/mes | Unidades/mes |
|---|---|---|---|---|
| CABINA CORE | 149 € | 138,9 € | 1.300 € | **10** (o 6 COMPLETA a 232,4 €) |
| Cobro de cartera vencida | 79 € | 73,4 € | 867 € | **12** |
| Instalación Esencial (transferencia, sin comisión) | 2.500 € | 2.500 € | 433 € | **una cada 6 meses** |

**22 ventas de catálogo al mes cubren 2.270 € netos, el 87 % del objetivo.** Los 433 € restantes
los cubre una Instalación Esencial cada seis meses; una sola instalación al año ya deja el
objetivo al 95 %. El hueco que la v1.0 dejaba sin precio (la suscripción) desaparece.

**Si Polar no paga a México y hay que caer a Gumroad** (10 % + 0,50, sin recargo internacional
declarado): CORE neto 133,7 €, cobro 70,7 €. Son 10 y 13 unidades: cambiar de canal cuesta una
venta más al mes, no ahorra ninguna. Lo que cambia es que Gumroad no concede ni revoca acceso al repositorio, y la
entrega pasa a ser por adjunto, que es lo que la doctrina prohíbe.

---

## 3 · El reloj del dinero

Que no se confunda lentitud administrativa con fracaso comercial.

| Hito | Cuándo |
|---|---|
| Venta hecha | día 0 |
| Retención antes de poder cobrarla | `[A VALIDAR — Polar, al configurar]` |
| Retirada a la cuenta (Stripe Connect Express) | `[A VALIDAR — Polar, al configurar]` |
| Revisión de cuenta nueva | en paralelo desde el día 1 (paso 0.2) |

**Entre la primera venta y el primer ingreso pueden pasar de dos a cuatro semanas.** Es el
calendario, no un problema. La instalación de hostelería no tiene este reloj: se cobra por
transferencia el día que se firma.

---

## 4 · Riesgos, con su señal de alarma

| Riesgo | Señal de que está pasando | Qué hacer |
|---|---|---|
| El tráfico no llega | La tienda abierta y sin visitas a los 14 días | No bajar precio. Ir a buscar al DJ donde está: foros, grupos, residentes conocidos |
| La promesa no convence sin cifra | Visitas sin compra | Acelerar la fase 2. Es el hueco, no el precio |
| CABINA COMPLETA a 249 € no aguanta en directorio | Cero ventas en directorios y sí en Polar | Confirmado: ese precio se defiende en página propia, no en estante. Ante negociación se quita alcance, jamás se baja el precio |
| Polar no paga a México | Stripe Connect Express rechaza la cuenta al configurar | Caer a Gumroad el mismo día con la aritmética de §2; aceptar entrega por adjunto como excepción documentada |
| Dos tarifas circulando | Alguien cita 249 USD por CORE o 69 USD por cobro | La v1.0 está retirada. Toda cifra sale de `catalogo/PRECIOS.md` |
| `receta-estandar` se vende antes de G4 | Aparece en un texto de la Completa como entregada | No se factura. Entra sin coste para quien ya compró cuando el consultor de inocuidad firme |

---

## 5 · Los huecos abiertos y quién los cierra

| Hueco | Responsable |
|---|---|
| **La prueba con cifra, en los tres productos** | Sergio · tres conversaciones |
| Si Polar (Stripe Connect Express) paga a México, y con qué retención | Sergio · paso 0.2 |
| Si el 5 % + 0,50 de Polar incluye el procesamiento y cuándo aplica el 1,5 % internacional | Sergio · paso 1.3 |
| Qué dos skills se abren en `octava-skills` y con qué licencia | Sergio · antes del paso 1.4 |
| Si myClaude y SkillHQ actúan como *merchant of record* y entregan por acceso | La fábrica, escribiéndoles |
| Cómo se entra en el directorio `claudemarketplaces.com` | La fábrica |
| Revisión externa de inocuidad de `receta-estandar` (único G4 abajo) | Sergio · consultor |
| Revisión del abogado de `venta/ANEXO-CONTRATO-INOCUIDAD.md` | Sergio · abogado |
| Tipo de cambio para facturar en pesos | El día que se factura |

Cerrados respecto a la v1.0: conformidad de las 17 (validan), licencia de las 17 (declarada),
precio del tercer tramo (Instalación Esencial), usuario de myClaude (no se publica hasta cerrar
el hueco de arriba).

---

## 6 · La regla que no se toca

**No se fabrica una skill nueva hasta que estas tres estén vendidas a alguien que pagó.** El
catálogo tiene 17 piezas listas y ninguna venta; el problema no se arregla con la 18.

---

## Documentos de esta carpeta

| Archivo | Qué es |
|---|---|
| `venta/PLAN-DE-TRABAJO.md` | Este documento. El plan operativo, v1.1 |
| `venta/POLAR-CONFIGURACION.md` | Los 12 productos y sus textos, listos para copiar en Polar |
| `venta/GUION-VISITA.md` · `venta/MENSAJES.md` | La visita de hostelería y los correos de la fase 2 |
| `venta/ANEXO-CONTRATO-INOCUIDAD.md` | Cláusula de `receta-estandar`, pendiente de abogado |
| `catalogo/PRECIOS.md` · `catalogo/DECISIONES.md` · `catalogo/ESTADO-GATES.md` | La tarifa, sus razones y la matriz de gates |

La v1.0 de este plan, el informe `FORJA_Estado_Canales_y_GitHub_v1_1`, el `.pptx` de ocho láminas y
los dos zips (`OCTAVA-repo-github-v1.0.0`, `myclaude-cobro-cartera-vencida-v1.1.0`) quedan en la
carpeta del proyecto como histórico. **No se sube ninguno de los dos zips a un repositorio público
sin comprobar antes que no contienen skills de pago.**
