# CHANGELOG — auditoria-de-biblioteca

Formato: `[versión] — fecha`. Tipo de cambio y motivo, siempre.
MAYOR cambia el protocolo · MENOR añade capacidad sin romper nada · PARCHE corrige
referencias, ejemplos o redacción.

## [1.1.0] — 2026-09-15

**Alineación con el ADN de la casa y cierre del envoltorio de venta.** La auditoría
mecánica del 15-sep-2026 (`validar_skill.py`) dio **0/20** sobre la v1.0.0: la skill
tenía buen contenido de oficio pero no cumplía la estructura de serie ni tenía los
ficheros que exige el peldaño P1. No era un problema de criterio, era de envoltorio.

Añadido:

- Estructura de 13 secciones del ADN: `Qué hace`, `Cuándo se dispara`, `Quién lo
  ejecuta`, `Entrada`, `Umbral que sostiene el producto`, `Procedimiento`, `Salida`,
  `Límites`, `Reglas`, `Antipatrones`, `Casos de prueba`, `Ficha comercial`, `Versión`.
- Procedimiento reescrito en 6 pasos atómicos con el molde
  Entrada → Acción → Salida → Si falta el dato.
- Tabla de reglas ampliada a 10 SIEMPRE y 9 NUNCA con su porqué.
- 5 antipatrones con síntoma, causa raíz y corrección.
- Los 4 casos de prueba en `cases/`, con entrada y salida reales.
- `references/FUENTES.md` con las fuentes externas, su fecha de consulta y sus límites.
- `README.md`, `LICENSE.txt`, `metadata.json` y ficha comercial `ANEXO-A`.
- Viñeta obligatoria de **dato sucio típico** en `Entrada`: el XML exportado desde otra
  máquina, que es el fallo que produce el falso 100% de rutas rotas.

Corregido:

- `description` del frontmatter pasada a escalar de bloque `>-`. Como escalar plano
  contenía `: ` y **no era YAML válido**, lo que podía impedir que la skill cargase en
  el entorno del comprador. El texto es idéntico carácter a carácter.

Precio fijado en esta versión: **49 €** pago único. Ver `ANEXO-A-ficha-comercial.md`.

## [1.0.0] — 2026-08-XX

Creación inicial. Diagnóstico de `collection.xml` de rekordbox con 10 categorías de
hallazgo, índice de salud 0-100, priorización por riesgo en cabina y límite honesto
declarado frente a Lexicon. Solo lectura por diseño.
