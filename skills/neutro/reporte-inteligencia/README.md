# reporte-inteligencia

Skill de la **línea neutra** (B2B, cualquier sector). Agent Skills, estándar abierto.

Convierte **el nombre de una marca y su plaza** en un **reporte semanal de inteligencia
competitiva**: panel congelado de 6 competidores, tabla de brecha en 8 métricas de reputación
digital pública, qué hacen bien ellos, qué hacemos mal, oportunidades de la plaza y **3 acciones
de 7 días con dueño y métrica de verificación**. Cada cifra va con su cita y su fecha.

Agnóstica de sector: hostelería, retail, clínicas, hoteles, servicios, SaaS, ecommerce. La
vertical de restauración, con umbrales propios del oficio, es `reporte-inteligencia-competencia`.

## Instalación

1. Copia la carpeta `reporte-inteligencia/` entera, sin renombrarla, al directorio de skills de
   tu cliente: en Claude Code, `.claude/skills/` del proyecto o `~/.claude/skills/` para tenerla
   en todos.
2. Abre una sesión nueva. La skill se activa sola cuando la conversación encaja con su
   descripción ("compárame con los seis de mi zona", "el informe de esta semana", "quién nos
   come terreno"); también puedes nombrarla.

## Cómo se usa

Da el nombre de la marca. Si es ambiguo, la skill hace **una** pregunta (ciudad o dirección) y
nunca más de dos. Antes de medir declara el **modo de captura**:

| Modo | Qué alcanza | Tiempo aproximado |
|---|---|---|
| BÚSQUEDA | 2 de las 8 métricas · la línea base queda **ABIERTA** | ~1 h 15 min |
| PLATAFORMA | las 8 métricas · cierra la línea base | 6–8 h |

El producto es la **serie semanal**: el panel de competidores se congela 13 semanas para que los
deltas signifiquen algo. Un corte aislado no tiene brecha anterior contra la que compararse.

## Qué hay dentro

- `SKILL.md` — procedimiento, reglas SIEMPRE / NUNCA, antipatrones y límites.
- `assets/plantilla-reporte.md` — la plantilla de las 10 secciones del reporte.
- `references/metricas-y-umbrales.md` — las 8 métricas, sus umbrales y el alcance por modo.
- `references/fuentes-por-sector.md` — dónde se mira en cada sector.
- `references/FUENTES.md` — cada cifra con su fuente, su fecha y su límite.
- `cases/` — los 4 casos de prueba (feliz, borde, fallo, integración).
- `CHANGELOG.md` · `LICENSE.txt`.

## Lo que esta skill NO hace

- **El modo BÚSQUEDA no cierra una línea base**, y el reporte lo declara en cabecera.
- No usa datos obtenidos saltándose términos de uso ni muros de acceso.
- No identifica ni nombra a ningún reseñador: analiza patrones, no personas.
- **No recomienda solicitar, comprar, incentivar ni suprimir reseñas**, propias ni ajenas.
- No responde reseñas (eso es `respuesta-resenas`) ni es *due diligence*.

Las cifras de comportamiento del consumidor proceden de paneles de EE. UU.: la dirección es
extrapolable, las cifras exactas no, y así se marcan.

## Licencia

Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso comercial en tu propia actividad,
sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. Ver `LICENSE.txt`.
