# ZEUS

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
| **Hostelería** | 7 | B · instalación presencial | 4.900 € completa / 2.500 € esencial `[A VALIDAR]` |
| **CABINA** (DJ) | 6 | A · catálogo | sin fijar |
| **Neutra / B2B** | 4 | A · catálogo | sin fijar |

- [`catalogo/PRECIOS.md`](catalogo/PRECIOS.md) — tarifa propuesta con anclas de mercado y canal de cobro.
- [`catalogo/ESTADO-GATES.md`](catalogo/ESTADO-GATES.md) — matriz G1–G5 y riesgos abiertos.
- [`catalogo/PENDIENTE-FIRMA.md`](catalogo/PENDIENTE-FIRMA.md) — las 4 decisiones que desbloquean el cobro.

## Estructura

```
skills/
├── hosteleria/   7 skills · sistema instalable Motor B
├── cabina/       6 skills · 3 paquetes (CORE, EVENTOS, CARRERA)
└── neutro/       4 skills · B2B sin oficio específico
catalogo/         tarifa, gates y decisiones pendientes
```

Cada skill conserva su `SKILL.md`, sus `references/`, `assets/`, `scripts/`,
`cases/`, su `metadata.json` y su ficha comercial `ANEXO-A` donde existe.

## Estado

Las 17 están en estado `ACORDADO` con licencia que permite la venta. Ninguna
tiene el gate **G3 (precio)** levantado con firma, y **G2 (prueba contra datos
reales de cliente)** está abajo en todo el catálogo. Nada de esto impide vender
una instalación presencial —se ejecuta con los datos del propio cliente, que es
como está diseñado el Motor B—, pero sí desaconseja publicar suelto en
directorio antes del primer caso vendido.

No se ha subido lo que no está en condiciones: `valoracion-lote-vino-inversion`
(BORRADOR), `checklist-turno` (duplicado con licencia incompatible),
`forja-fabrica-de-skills` y `zeus-skill-creator` (internos), y la línea
`octava-*` (sistema operativo de OCTAVA, no catálogo). Motivos en
[`CATALOGO.md`](CATALOGO.md#lo-que-no-se-ha-subido-y-por-qué).
