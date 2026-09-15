# Tarifa propuesta

Toda cifra de este documento está `[A VALIDAR]` hasta ratificación por escrito.
Las que ya estaban escritas en una ficha comercial se transcriben tal cual; las
que faltaban se proponen aplicando las anclas de mercado de la propia doctrina
de la casa (`forja-fabrica-de-skills`), citadas abajo con su fuente.

## 1 · Hostelería — Motor B (instalación)

| Producto | Contenido | Precio en ficha |
|---|---|---|
| **Instalación Completa** | 6 skills del sistema | **4.900 €** `[A VALIDAR]` |
| **Instalación Esencial** | 3 skills | **2.500 €** `[A VALIDAR]` |
| `productividad-personal-turno` suelta | 1 skill | **149–249 €** pago único `[A VALIDAR]` |

Las fichas coinciden en que el paquete Esencial de 3 se arma con
`escandallo-ingenieria-menu` (produce la cifra que abre la conversación: euros
al año) más dos de entre `comparativa-proveedores` (el ahorro más fácil de
comprobar: el dueño llama al proveedor esa misma tarde), `apertura-cierre-turno`
y `control-no-shows`. **La composición exacta está sin cerrar** y es una de las
decisiones pendientes de firma.

> Regla de la casa, literal: *ante negociación se quita alcance, jamás se baja el
> precio del sistema completo.*

## 2 · CABINA (DJ) — propuesta nueva

No existía precio. Se propone aplicando la escalera P0–P5 de la casa: son P1
sueltos (suelo 30 $) agrupables en P2 (*3–6 veces el precio de una skill
suelta*).

| Producto | Contenido | Propuesta |
|---|---|---|
| Skill suelta | cualquiera de las 6 | **39–49 €** `[A VALIDAR]` |
| **CABINA CORE** | 3 skills | **119–149 €** `[A VALIDAR]` |
| **CABINA EVENTOS** | 2 skills | **89–119 €** `[A VALIDAR]` |
| **CABINA CARRERA** | 1 skill | **39–49 €** `[A VALIDAR]` |
| **CABINA COMPLETA** | 6 skills | **249–299 €** `[A VALIDAR]` |

Razón del rango: el tramo 30–49 $ convierte un 28 % mejor que el sub-10 $, y los
productos por debajo de 10 $ son ~35 % del catálogo pero capturan el 0,8 % del
ingreso. `presupuesto-y-contrato-evento` es la que más arriba puede ir del rango:
lo que evita —depósito, cancelación, horas extra, limitador de sonido— se mide en
bolos perdidos, no en comodidad.

## 3 · Neutra / B2B — propuesta nueva

| Skill | Propuesta |
|---|---|
| `cobro-cartera-vencida` | **49–79 €** `[A VALIDAR]` — 19/20, sector neutro, dolor con cifra directa (DSO, importe en riesgo) |
| `reporte-inteligencia` | **39–49 €** `[A VALIDAR]` — reauditar tras v1.1.0 antes de publicar |
| `respaldo-proyecto-ia-cl` | **39–49 €** `[A VALIDAR]` |
| `universal-compilador-contexto` | **39–49 €** `[A VALIDAR]` |

## Canal de cobro

La doctrina ya lo tiene decidido y no hace falta reabrirlo:

- **Polar** como principal: es *merchant of record*, acepta México como país del
  vendedor, y concede y revoca acceso a repositorio privado de GitHub al
  suscribir y al cancelar. Comisión 5 % + 0,50 $ en plan gratuito; 3,8 % + 0,40 $
  en plan de 20 $/mes; +1,5 % en tarjeta internacional; 15 $ por disputa.
- **Stripe México** para pesos e instalaciones: 3,6 % + 3,00 MXN, +0,5 % tarjeta
  internacional, +2 % conversión de divisa. **No es merchant of record.**
- Entrega **siempre por acceso revocable** a este repositorio privado, nunca por
  adjunto. El adjunto no se recupera al cancelar.

Empezar por el plan gratuito de Polar: comisión más alta pero sin cuota fija, no
arriesga nada hasta que haya volumen. `scripts/punto_equilibrio.py` de
`forja-fabrica-de-skills` calcula a partir de cuántas transacciones compensa
saltar al plan de 20 $/mes.

## Anclas de mercado (fuentes de la doctrina)

- 44 % de los productos digitales factura **exactamente 0 $**; mediana 72 $/mes;
  menos del 5 % supera 1.000 $/mes y el 1 % superior se lleva el 99,5 % del
  ingreso. *(InsightRaider, State of Gumroad 2026, n=146.271, ene–abr 2026.)*
  → **Publicar no es vender.**
- Rango 30–49 $ convierte **28 % mejor** que sub-10 $. *(Misma fuente.)*
- Suscripción promedia 4.053 $/mes frente a 2.047 $/mes del pago único; solo el
  11 % de los productos genera algún ingreso. *(Whop Trends, n=195.236,
  24-feb-2026.)*
- **42 % de las ventas viene del correo**, por delante de redes (23 %) y directo
  (18 %). *(InsightRaider.)* → Sin lista propia no hay negocio.
- La pyme mediana gasta **~30 $/mes en IA en total**; solo el 16 % supera
  150 $/mes. *(JPMorganChase Institute, n>4,6 M pymes, 2019–2025, publicado
  14-abr-2026.)* → Una suscripción de catálogo compite contra un presupuesto
  total de 30 $/mes, no contra cero.

Consecuencia que la propia doctrina extrae: **5.000 $/mes son 173 suscriptores a
29 $/mes, o dos instalaciones de 2.500 €.** La diferencia de esfuerzo comercial
es de dos órdenes de magnitud. El dinero empieza por el servicio y escala por el
producto, nunca al revés.
