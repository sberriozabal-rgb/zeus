# CHANGELOG — universal-compilador-contexto

## [1.1.0] — 2026-09-15

**Cierre del envoltorio de venta.** La auditoría mecánica del 15-sep-2026 (`validar_skill.py`)
dio **1/20** frente al **17/20 (autoevaluación)** que declaraba el frontmatter. La autoevaluación
iba honestamente marcada como tal, pero una nota que el validador no reproduce no sirve para
vender.

Añadido:

- Estructura de **13 secciones del ADN**, con las seis fases F0-F5 reescritas como **8 pasos
  atómicos** con el molde en línea Entrada → Acción → Salida → Si falta el dato.
- Reglas convertidas de lista numerada a tabla: **10 SIEMPRE y 9 NUNCA** con su porqué.
- Antipatrones de 6 a **5 con el molde de serie**, fusionando "la copia de la copia" y "el
  resumen que es un índice": los dos son el mismo fallo —se entregó un derivado en lugar de leer
  la fuente— visto en dos artefactos distintos.
- Los **4 casos de prueba** en `cases/`, con entrada y salida reales.
  `references/casos-y-auditoria.md` conserva el desglose y la rúbrica.
- `references/FUENTES.md`, que esta skill **no tenía**: límite de la ingesta de chats con la
  documentación de la plataforma, las cuatro dependencias de extracción con su fuente, y la tabla
  de los tres umbrales que son criterio de oficio `[A VALIDAR]`.
- Viñeta de **dato sucio típico** en `Entrada`: las versiones múltiples del mismo documento sin
  fecha fiable, y el PDF escaneado sin capa de texto.
- `ANEXO-A-ficha-comercial.md`, `LICENSE.txt` y `metadata.json`.

**El contenido de oficio no se ha tocado**: la frontera decidido ≠ propuesto, los dos umbrales
medibles de taxonomía (≥2 fuentes por dominio, "Anexos" ≤ 15 %), la regla de no fusionar marcos
incompatibles y la de no modificar la carpeta original están exactamente como estaban.

Declarado por primera vez en ficha:

- Que `CONFLICTOS.md` y `HUECOS.md` **son la agenda de decisiones del dueño**, y no un apéndice:
  es la salida que más valor aporta y la que justifica el precio.
- La relación con `respaldo-proyecto-ia-cl`: **misma cadena en dos mitades**, se venden juntas y
  no compiten.

Resultado: **19/20** declarado (20/20 mecánico, menos el punto 19 de criterio).

## [1.0.0] — 2026-08-26

Creación inicial. Seis fases F0-F5, taxonomía derivada del material, frontera decidido/propuesto,
manejo de conflictos y huecos, ZIP único con biblioteca por dominios, resumen ejecutivo, resumen
de chats, resumen de contexto e inventario con ubicación. Autoevaluación declarada: 17/20.
