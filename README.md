# ZEUS

**Titular de todos los derechos: Sergio Berriozábal Serrano.** Copyright © 2026.
Ver [`LICENSE`](LICENSE). `ZEUS`, `FORJA`, `TROQUEL`, `OCTAVA` y `CABINA` son nombres
comerciales del titular, no entidades distintas.

Repositorio de skills de ZEUS / FORJA: activos ejecutables para
hostelería y restauración, DJ y cabina, gestión y finanzas, más los códigos de
Google Script y los contextos de la casa.

**Este repositorio es público por decisión del titular (decisión 11) y es la fuente de verdad
del catálogo.** Que el contenido sea visible no lo hace de uso libre: la licencia de cada skill
prohíbe la redistribución y la publicación, y el uso comercial solo lo concede la compra. La
doctrina de la casa prefiere entregar por *acceso revocable a repositorio privado, nunca por
adjunto*; desde el 15-sep-2026 el catálogo suelto (CABINA y línea neutra) se vende en
**Gumroad**, que entrega por descarga. Es una desviación declarada, asumida a cambio de que Gumroad remita el IVA como
*merchant of record* (decisión 8 en [`catalogo/DECISIONES.md`](catalogo/DECISIONES.md)). Las
instalaciones de hostelería siguen entregándose en la visita.

## Escaparate público

→ **<https://github.com/sberriozabal-rgb/octava-skills>** — fichas públicas de las 17 con precio y
límites, marketplace de plugins y la skill abierta instalable. Generado desde este repositorio
(decisión 10). Escaparate web: <https://sberriozabal-rgb.github.io/octava-skills/>.

## Comprar

Las **17 skills están a la venta**. Catálogo suelto (CABINA y B2B) en la tienda de Gumroad
enlazada en cada ficha del escaparate; instalaciones de hostelería por
[formulario](https://github.com/sberriozabal-rgb/octava-skills/issues/new?template=instalacion.yml)
y visita presencial. La tienda es <https://cabina.gumroad.com>, abierta el 16-sep-2026 con los
15 productos del catálogo suelto. Si un enlace fallara,
[pide el producto aquí](https://github.com/sberriozabal-rgb/octava-skills/issues/new?template=comprar.yml).

## Catálogo de venta

→ **[`CATALOGO.md`](CATALOGO.md)** — 17 skills cargadas, en tres líneas.

| Línea | Skills | Motor | Precio |
|---|---|---|---|
| **Hostelería** | 7 | B · instalación presencial | **4.900 €** completa (7 skills) / **2.500 €** esencial (3) ✅ |
| **CABINA** (DJ) | 6 | A · catálogo | **49 € suelta / 249 € completa** ✅ cerrado |
| **Neutra / B2B** | 4 | A · catálogo | **49–79 €** · pack 89 € ✅ |

- [`catalogo/PRECIOS.md`](catalogo/PRECIOS.md) — tarifa propuesta con anclas de mercado y canal de cobro.
- [`catalogo/ESTADO-GATES.md`](catalogo/ESTADO-GATES.md) — matriz G1–G5 y riesgos abiertos.
- [`catalogo/DECISIONES.md`](catalogo/DECISIONES.md) — **las decisiones tomadas**, con su razón.
- [`venta/LISTA-DE-VENTA.md`](venta/LISTA-DE-VENTA.md) — **empieza aquí**: lo que está hecho, lo
  que solo puede hacer el titular y en qué orden, producto a producto.
- [`venta/`](venta/) — kit de venta: **hoja de alta en Gumroad** (`GUMROAD-ALTA.md`, los 15
  productos con descripción, tags y portada), **portadas** (`portadas/`, `generar_portadas.py`),
  **oferta de hostelería** (`OFERTA-HOSTELERIA.md`, las instalaciones descritas), empaquetador
  de productos con validación previa (`empaquetar_gumroad.py`), consultas pendientes a terceros
  (`CONSULTAS-PENDIENTES.md`), guion de visita, mensajes listos y **locuciones**
  generadas en local (`venta/locuciones/`).

## Estructura

```
skills/
├── hosteleria/   7 skills · sistema instalable Motor B
├── cabina/       6 skills · 3 paquetes (CORE, EVENTOS, CARRERA)
├── neutro/       4 skills · B2B sin oficio específico
└── externas/     skills de terceros para uso interno · fuera del catálogo
catalogo/         tarifa, gates y decisiones pendientes
.claude/skills/   copia real de las skills externas; Claude Code las carga al abrir el repo
```

Las skills externas (hoy `omnivoice`, de VoiceStudio, AGPL-3.0) tienen autor y licencia
ajenos: **no se venden ni se empaquetan**. Ficha de origen en su `ORIGEN.md`.

Cada skill conserva su `SKILL.md`, sus `references/`, `assets/`, `scripts/`,
`cases/`, su `metadata.json` y su ficha comercial `ANEXO-A` donde existe.

## Estado

Las 17 están en `ACORDADO`, con licencia de venta y **todas por encima del umbral de 16/20** que
exige el peldaño P1 (medido, no estimado). **Gates G1 (17/17), G3 (17/17), G4 (16/17) y G5 (17/17)
levantados.** La única excepción de G4 es `receta-estandar`, por seguridad alimentaria: sigue
abajo como hecho (la revisión externa no está), pero **desde la decisión 11 no bloquea la venta**;
entra en la Completa con el anexo de inocuidad firmado.

**G2 (prueba contra datos reales de cliente) sigue abajo en las 17, y es correcto que lo esté.**
No se cierra por decisión: lo levanta el primer cliente que ejecuta una skill con sus datos. Y no
bloquea la venta — la instalación de hostelería se ejecuta precisamente así, en la visita y con los
datos del propio cliente.

No se han subido: `valoracion-lote-vino-inversion` (BORRADOR, 16/20), `checklist-turno`
(**retirada y borrada de la cuenta**, duplicado con licencia de uso libre), `forja-fabrica-de-skills` y
`zeus-skill-creator` (internos), y la línea `octava-*`. Motivos en
[`CATALOGO.md`](CATALOGO.md#lo-que-no-se-ha-subido-y-por-qué).
