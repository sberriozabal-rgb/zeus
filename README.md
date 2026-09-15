# ZEUS

**Titular de todos los derechos: Sergio Berriozábal Serrano.** Copyright © 2026.
Ver [`LICENSE`](LICENSE). `ZEUS`, `FORJA`, `TROQUEL`, `OCTAVA` y `CABINA` son nombres
comerciales del titular, no entidades distintas.

Repositorio privado de skills de ZEUS / FORJA: activos ejecutables para
hostelería y restauración, DJ y cabina, gestión y finanzas, más los códigos de
Google Script y los contextos de la casa.

**Este repositorio es privado y es el canal de entrega del catálogo.** La
doctrina de la casa exige entregar por *acceso revocable a repositorio privado,
nunca por adjunto*: el adjunto no se recupera al cancelar, el acceso sí.

## Catálogo de venta

→ **[`CATALOGO.md`](CATALOGO.md)** — 17 skills cargadas, en tres líneas.

| Línea | Skills | Motor | Precio |
|---|---|---|---|
| **Hostelería** | 7 | B · instalación presencial | **4.900 €** completa / **2.500 €** esencial ✅ |
| **CABINA** (DJ) | 6 | A · catálogo | **49 € suelta / 249 € completa** ✅ cerrado |
| **Neutra / B2B** | 4 | A · catálogo | **49–79 €** · pack 89 € ✅ |

- [`catalogo/PRECIOS.md`](catalogo/PRECIOS.md) — tarifa propuesta con anclas de mercado y canal de cobro.
- [`catalogo/ESTADO-GATES.md`](catalogo/ESTADO-GATES.md) — matriz G1–G5 y riesgos abiertos.
- [`catalogo/DECISIONES.md`](catalogo/DECISIONES.md) — **las decisiones tomadas**, con su razón.
- [`venta/`](venta/) — kit de venta: **hoja de alta en Gumroad** (`GUMROAD-ALTA.md`), empaquetador
  de productos (`empaquetar_gumroad.py`), guion de visita y mensajes listos.

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
levantados.** La única excepción de G4 es `receta-estandar`, por seguridad alimentaria.

**G2 (prueba contra datos reales de cliente) sigue abajo en las 17, y es correcto que lo esté.**
No se cierra por decisión: lo levanta el primer cliente que ejecuta una skill con sus datos. Y no
bloquea la venta — la instalación de hostelería se ejecuta precisamente así, en la visita y con los
datos del propio cliente.

No se han subido: `valoracion-lote-vino-inversion` (BORRADOR, 16/20), `checklist-turno`
(**retirada y borrada de la cuenta**, duplicado con licencia de uso libre), `forja-fabrica-de-skills` y
`zeus-skill-creator` (internos), y la línea `octava-*`. Motivos en
[`CATALOGO.md`](CATALOGO.md#lo-que-no-se-ha-subido-y-por-qué).
