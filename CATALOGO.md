# Catálogo de venta — ZEUS / FORJA

Estado a 15-sep-2026. **17 skills cargadas** en `skills/`, todas en estado
`ACORDADO` con licencia que permite la venta. Este repositorio es privado: es el
canal de entrega que exige la doctrina de la casa —*acceso revocable a
repositorio privado, nunca por adjunto*—, no un escaparate público.

> **Estado de venta.** Gates **G1, G3 y G5 levantados en las 17** y **G4 en 16/17**
> (`receta-estandar` espera revisión externa de inocuidad). Tarifa ratificada el
> 15-sep-2026 y titularidad unificada en Sergio Berriozábal Serrano. Lo único que ninguna
> pieza tiene aún es **G2**: tres ejecuciones con cliente real, que solo levanta la primera
> venta. Razón de cada decisión en [`catalogo/DECISIONES.md`](catalogo/DECISIONES.md);
> [`catalogo/PENDIENTE-FIRMA.md`](catalogo/PENDIENTE-FIRMA.md) queda como histórico.

---

## Línea 1 · HOSTELERÍA — Motor B (instalación presencial)

Producto de ticket alto. Las fichas prohíben la venta suelta de estas piezas y
la publicación en directorio hasta que el sistema completo tenga el primer caso
vendido. Se venden como instalación.

| # | Skill | Ver. | Auditoría | Estado |
|---|---|---|---|---|
| 1 | `escandallo-ingenieria-menu` | **1.1.1** | **19/20** ✅ | ACORDADO |
| 2 | `respuesta-resenas` | **1.2.0** | **19/20** ✅ reestructurada | ACORDADO |
| 3 | `apertura-cierre-turno` | **1.1.2** | **19/20** ✅ atribución cerrada | ACORDADO |
| 4 | `comparativa-proveedores` | **1.1.1** | **19/20** ✅ | ACORDADO |
| 5 | `receta-estandar` | **1.1.1** | **19/20** ✅ cifras de inocuidad ancladas · G4 solo espera revisión externa | ACORDADO |
| 6 | `productividad-personal-turno` | **1.1.1** | **19/20** ✅ | ACORDADO |
| 7 | `reporte-inteligencia-competencia` | **1.1.0** | **19/20** ✅ | ACORDADO |

**Auditoría:** las 7 en **20/20 mecánico** (19/20 declarado), muy por encima del 16 que exige P1.

**Precio ratificado (15-sep-2026):** Instalación Completa **4.900 €** (6 skills) · Instalación
Esencial **2.500 €** (3 skills). `productividad-personal-turno` es la única con precio suelto:
**199 €** pago único. `receta-estandar` no se factura hasta levantar G4; entra en la Completa
sin coste para quien ya compró. Razón de cada cifra en [`catalogo/PRECIOS.md`](catalogo/PRECIOS.md).

## Línea 2 · CABINA — DJ (3 paquetes cerrados)

Seis piezas, tres paquetes, licencia de comprador limpia (*uso permitido al
comprador; prohibida la redistribución*). **Tarifa cerrada el 15-sep-2026** y
ficha comercial escrita para las seis.

| Paquete | Skills | **Precio** | Auditoría |
|---|---|---|---|
| **CABINA CORE** | `auditoria-de-biblioteca`, `postmortem-de-bolo`, `set-por-encargo` | **149 €** | 19/20 las tres |
| **CABINA EVENTOS** | `peticiones-a-repertorio`, `presupuesto-y-contrato-evento` | **99 €** | 19/20 las dos |
| **CABINA CARRERA** | `demo-a-sello` | **49 €** | 19/20 |
| **CABINA COMPLETA** | las seis | **249 €** | — |

Suelta: **49 €** cualquiera de las seis. Tarifa y razón de cada cifra en
[`catalogo/PRECIOS.md`](catalogo/PRECIOS.md#2--cabina-dj--tarifa-cerrada-15-sep-2026).

> ✅ **Lista para publicar.** G1 y G3 levantados en las seis el 15-sep-2026: auditoría
> **19/20** (el validador da 20/20 mecánico; no se firma el 20 porque las URLs no se han
> reverificado una a una) y precio cerrado. Venían de 0-2/20 por falta de envoltorio, no de
> oficio. Queda G2, que solo lo levanta el primer comprador.

## Línea 3 · NEUTRA / B2B

Piezas que no dependen de un oficio concreto. Vendibles sueltas por catálogo
(Motor A) sin tocar la estrategia de hostelería.

| Skill | Ver. | Auditoría | Estado |
|---|---|---|---|
| `cobro-cartera-vencida` | **1.2.0** | **19/20** ✅ | ACORDADO |
| `reporte-inteligencia` | **1.2.0** | **19/20** ✅ | ACORDADO |
| `respaldo-proyecto-ia-cl` | **2.1.0** | **19/20** ✅ | ACORDADO |
| `universal-compilador-contexto` | **1.1.0** | **19/20** ✅ | ACORDADO |

✅ **Las cuatro cerraron envoltorio el 15-sep-2026** y están en 19/20. `cobro-cartera-vencida`
es la mejor candidata a primer producto suelto de catálogo: sector agnóstico, dolor con cifra
directa (DSO, importe en riesgo) y comprador que ya sabe que tiene el problema.

`respaldo-proyecto-ia-cl` y `universal-compilador-contexto` son **la misma cadena en dos
mitades** y se venden bien juntas: una asegura el material antes de que desaparezca, la otra
lo hace comprensible.

---

## Lo que NO se ha subido, y por qué

| Activo | Motivo |
|---|---|
| `valoracion-lote-vino-inversion` | Estado **BORRADOR**, 16/20, cuatro de cinco gates abajo. La doctrina dice que por debajo de ACORDADO no sale de la fábrica. |
| `checklist-turno` | ✅ **RETIRADA Y BORRADA de la cuenta el 15-sep-2026.** Era duplicado de `apertura-cierre-turno` con licencia de uso libre. Se conserva `apertura-cierre-turno`, que es la auditada y con licencia de venta. Ver [`catalogo/DECISIONES.md`](catalogo/DECISIONES.md). |
| `forja-fabrica-de-skills` | Su propia ficha: *"No se vende. Activo interno."* |
| `zeus-skill-creator` | Interno. Si se licencia: 490–990 €/año por puesto `[A VALIDAR]`. |
| Línea `octava-*` (17 skills) | Sin metadatos de estado ni ficha comercial. Es el sistema operativo de OCTAVA, no catálogo de venta. |
| Resto de la biblioteca | Sin `estado`, sin auditoría o con licencia de uso personal. |

## Documentos

- [`catalogo/PRECIOS.md`](catalogo/PRECIOS.md) — tarifa propuesta, con la razón de cada cifra y su anclaje de mercado.
- [`catalogo/ESTADO-GATES.md`](catalogo/ESTADO-GATES.md) — matriz G1–G5 pieza por pieza y los tres riesgos abiertos.
- [`catalogo/PENDIENTE-FIRMA.md`](catalogo/PENDIENTE-FIRMA.md) — las 4 decisiones que desbloquean el cobro.
