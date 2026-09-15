# Tarifa — CERRADA el 15-sep-2026

Todas las cifras están **ratificadas**. Ya no llevan `[A VALIDAR]`: el gate **G3 está levantado
en las 17 piezas**. Decisiones y su razón en [`DECISIONES.md`](DECISIONES.md).

## 1 · Hostelería — Motor B (instalación presencial)

| Producto | Contenido | Precio |
|---|---|---|
| **Instalación Esencial** | 3 skills | **2.500 €** |
| **Instalación Completa** | 6 skills | **4.900 €** |
| `productividad-personal-turno` suelta | 1 skill | **199 €** |

**Esencial** = `escandallo-ingenieria-menu` + `comparativa-proveedores` + `apertura-cierre-turno`.
El escandallo produce la cifra que abre la conversación; la comparativa produce el ahorro que el
dueño verifica esa misma tarde llamando al proveedor; el checklist es lo que hace que las otras
dos se sostengan tres semanas después.

**Completa** = las tres anteriores más `respuesta-resenas`, `productividad-personal-turno` y
`reporte-inteligencia-competencia`.

> ⚠️ **`receta-estandar` NO se factura todavía.** Su G4 está abajo por seguridad alimentaria.
> A 15-sep-2026 la casa ha hecho todo lo que podía —cifras ancladas al RD 3484/2000 y a AESAN,
> cláusula contractual redactada, discrepancia AESAN/RD detectada y aplicada— y **solo falta la
> revisión de un consultor de seguridad alimentaria** antes de cobrarse. El Completa se sirve con las otras seis al
> mismo precio, y cuando levante G4 entra sin coste para quien ya compró.

**No se cobra por Gumroad.** La instalación va por Stripe México (pesos) o transferencia: el ticket
alto justifica la comisión menor pese a no ser *merchant of record*.

> Regla de la casa, literal: *ante negociación se quita alcance, jamás se baja el precio del
> sistema completo.* Si el Completa baja a 3.500 € una vez, ya nunca vale 4.900 €.

## 2 · CABINA (DJ) — **TARIFA CERRADA** (15-sep-2026)

Precio ratificado por el dueño el 15-sep-2026. Estas cifras ya **no** llevan
`[A VALIDAR]`: el gate **G3 (precio)** está levantado en las seis piezas.

| Producto | Contenido | **Precio** | Múltiplo |
|---|---|---|---|
| Skill suelta | cualquiera de las 6 | **49 €** | 1x |
| **CABINA CORE** | 3 skills · `auditoria-de-biblioteca`, `postmortem-de-bolo`, `set-por-encargo` | **149 €** | 3,0x |
| **CABINA EVENTOS** | 2 skills · `peticiones-a-repertorio`, `presupuesto-y-contrato-evento` | **99 €** | 2,0x |
| **CABINA CARRERA** | 1 skill · `demo-a-sello` | **49 €** | 1x |
| **CABINA COMPLETA** | las 6 | **249 €** | 5,1x |

Pago único. Precio final al comprador; el IVA lo gestiona Gumroad como *merchant of
record*, que es la razón por la que se eligió como canal principal (decisión 8).

> ✅ **Primer producto de Gumroad decidido (15-sep-2026):** CABINA COMPLETA, las seis a 249.
> El informe FORJA v1.1.0 hablaba de «CABINA CORE a 249 USD»; queda derogado en eso. Esta
> tarifa se mantiene tal cual. `DECISIONES.md`, punto 9.

### Por qué estas cifras

**49 € la suelta.** Techo del tramo 30–49 € que convierte un 28 % mejor que el
sub-10 €, y suelo de la casa respetado. Ancla de oficio: un bolo de boda en
España está en el **escalón medio real de 1.000–1.500 €** (baremos con fuente en
`presupuesto-y-contrato-evento/references/baremos-precio.md`), así que una pieza
a 49 € es el **3–5 % de un solo bolo**. Comparable directo: Lexicon cuesta
199 USD vitalicio y *repara* bibliotecas; `auditoria-de-biblioteca` cuesta una
cuarta parte y hace lo que Lexicon no hace, que es priorizar por riesgo de
cabina. Ese límite está declarado en la propia skill.

**149 € CABINA CORE.** Exactamente 3,0x la suelta: el piso de la banda P2
(3–6x). Son las tres que usa cualquier DJ con biblioteca y bolos recurrentes.

**99 € CABINA EVENTOS.** Dos piezas, así que no es un P2 y la banda 3–6x no
aplica. Es el paquete con más valor protegido del catálogo: **una sola
cancelación sin cláusula de depósito cuesta 1.000–1.500 €**, y una hora extra
recuperada (75–250 €) paga el paquete varias veces.

**249 € CABINA COMPLETA.** 5,1x la suelta, dentro de la banda P2. Las seis
sueltas suman 294 €, así que aquí está el único incentivo de la tarifa: **45 € de
ahorro**. CORE y EVENTOS no llevan descuento a propósito, por la regla de la casa
de que ante negociación se quita alcance y jamás se baja el precio. Se compran
por coherencia de trabajo, no por ahorro.

Frase útil en venta: **CABINA COMPLETA cuesta lo que una hora extra que hoy no
estás cobrando.**

### Bloqueo levantado (15-sep-2026)

El bloqueo de G1 que existía al cerrar la tarifa —las seis puntuaban entre 0 y 2 sobre 20 por
falta de `cases/`, `CHANGELOG.md`, tabla NUNCA y antipatrones— **quedó resuelto el mismo
día**: envoltorio cerrado en las seis, validador en 20/20 mecánico (19/20 declarado). El
contenido de oficio no se tocó. **CABINA está lista para publicar en Gumroad** (hoja de alta en `venta/GUMROAD-ALTA.md`). Detalle en
[`ESTADO-GATES.md`](ESTADO-GATES.md#cabina-dj).

## 3 · Neutra / B2B — CERRADA

| Producto | Precio | Razón |
|---|---|---|
| `cobro-cartera-vencida` | **79 €** | El único por encima del tramo: entrega los mensajes redactados y un cuadro de mando, no solo análisis, y el comprador llega con el dolor ya medido en euros |
| `reporte-inteligencia` | **49 €** | Techo del tramo 30-49 € de mejor conversión |
| `respaldo-proyecto-ia-cl` | **49 €** | Ídem |
| `universal-compilador-contexto` | **49 €** | Ídem |
| **PACK CONTEXTO** | **89 €** | Las dos de contexto juntas. 98 € sueltas → 89 € |

No hay pack de las cuatro: `cobro-cartera-vencida` y `reporte-inteligencia` no comparten comprador
con las de contexto, y empaquetar lo que no se usa junto rebaja el precio sin subir la conversión.

`reporte-inteligencia-competencia` **no se lanza como suscripción todavía**: entra en la
Instalación Completa. La suscripción exige cadencia real que sostenerla, y con cero clientes eso
es una deuda que se paga todos los lunes. Se reabre con 3 instalaciones vivas.

## Canal de cobro

Decidido el 15-sep-2026 (decisión 8 de `DECISIONES.md`), tras rehacer la cuenta con el
procesamiento de tarjeta dentro:

- **Gumroad** como principal para catálogo: 10 % + 0,50 USD por venta directa `[según informe
  FORJA v1.1.0; confirmar en el desglose de la primera venta si incluye tarjeta]`, sin cuota
  fija, *merchant of record* (remite el IVA de cada país). Entrega por descarga del zip de
  `venta/empaquetar_gumroad.py`. Hoja de alta en `venta/GUMROAD-ALTA.md`.
- **myClaude** (92 % antes de Stripe) empata con Gumroad en unidades necesarias; se suma
  después, si acaso, por el tráfico que trae, no por margen. Sin exclusividad ni cuota.
- **Stripe México** para pesos e instalaciones: 3,6 % + 3,00 MXN, +0,5 % tarjeta
  internacional, +2 % conversión de divisa. **No es merchant of record.**
- **Polar** queda descartado: era *merchant of record* y entregaba por acceso revocable al
  repositorio, pero la decisión del 12-sep ya era Gumroad y la cuenta rehecha no da razón de
  margen para reabrirla. Configuración conservada en `venta/POLAR-CONFIGURACION.md`.

**Entrega por descarga es una desviación declarada de la doctrina** (*acceso revocable, nunca
adjunto*), asumida a cambio del IVA resuelto.

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
