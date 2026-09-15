# Origen de esta skill

**Skill de terceros. No es propiedad de la casa y no forma parte del catálogo de venta.**

| Campo | Valor |
|---|---|
| Nombre | `omnivoice` (skill oficial de VoiceStudio) |
| Repositorio | https://github.com/debpalash/VoiceStudio |
| Commit descargado | `4e55180f700e2ce1b39195ec7377b9b3da8e20b2` (2026-09-14) |
| Ruta upstream | `.claude/skills/omnivoice/` (paquete Claude con `references/` y `scripts/`) |
| Copia canónica upstream | `skills/omnivoice/SKILL.md` → guardada aquí en `references/skill-canonica-api-openai.md` |
| Autor y copyright | Palash Debnath y colaboradores de VoiceStudio |
| Licencia | AGPL-3.0-only (texto completo en `LICENSE-UPSTREAM.txt`, resumen en `LICENSE-NOTICE-UPSTREAM.md`) |
| Fecha de descarga | 2026-09-15 |
| Estado de prueba | **Probada el 15-sep-2026**: audio en español generado por REST y por MCP contra VoiceStudio 0.5.2. Detalle en `PRUEBA-2026-09-15.md` |

## Qué hace

Genera voz local (TTS), clona voces a partir de un clip de 3-10 s, diseña voces por
descripción y transcribe audio (STT) a través del backend de VoiceStudio en
`http://localhost:3900`. Todo corre en la máquina del usuario, sin API key ni coste.

Requiere tener VoiceStudio instalado y arrancado. Instalación y arranque en
`references/mcp-setup.md` y en los scripts de `scripts/`.

## Reglas de la casa para esta pieza

- **No se vende ni se empaqueta en ningún paquete de ZEUS / FORJA.** Es AGPL y de
  autor ajeno; se usa como herramienta interna (locuciones, demos, doblaje).
- No se modifica el contenido upstream. Si hace falta adaptar algo, se crea una skill
  propia que la invoque, no se edita esta.
- Para actualizarla: `npx skills add debpalash/VoiceStudio` o volver a copiar
  `.claude/skills/omnivoice/` del repositorio upstream y actualizar el commit de esta ficha.

## Dónde está instalada

- `.claude/skills/omnivoice/` — copia real; Claude Code la carga al abrir este repositorio.
- `skills/externas/omnivoice` — enlace simbólico a la anterior, para que figure en el inventario.
