# CHANGELOG — escandallo-ingenieria-menu

Formato: `[versión] — fecha`. Tipo de cambio y motivo, siempre.
MAYOR cambia el protocolo (quien usaba la anterior debe releer) · MENOR añade capacidad sin
romper nada · PARCHE corrige referencias, ejemplos o redacción.

## [1.1.1] — 2026-09-15

**Parche de conformidad con la rúbrica.** De 18/20 a 20/20 mecánico (19/20 declarado: el punto 19, URLs verificadas una a una, no se reconfirmó). Procedimiento consolidado de 10 a 8 pasos: 3+4 (coste de ingrediente con rendimiento y merma, más las capas que no están en la receta) y 9+10 (las cinco verificaciones y el cierre con la cifra anual). Ninguna rama "si falta el dato" se pierde. Literal "Supuestos de esta versión" en el apartado 6 de la plantilla de salida. El contenido de oficio no cambia.

## [1.1.0] — 2026-08-16

**Auditoría honesta y alineación con el ADN de la línea Hostelería.** La auditoría mecánica
del 15-ago-2026 detectó que esta skill se declaraba en 18/20 sin tener carpeta `cases/`,
sin CHANGELOG, sin ficha comercial, sin README, sin metadata.json y sin sección de
antipatrones. La re-auditoría punto por punto contra la rúbrica de 20 dio **7/20 real**.
Esta versión cierra esas carencias. No cambia ningún criterio de cálculo: el motor
`scripts/escandallo.py` produce exactamente los mismos números que en v1.0.0 salvo la
corrección de redacción del punto siguiente.

### Añadido
- `SKILL.md` reescrito a la estructura de la línea (misma que `apertura-cierre-turno`):
  **Qué hace · Cuándo se dispara · Quién lo ejecuta · Entrada · Umbral · Procedimiento ·
  Salida · Límites · Reglas · Antipatrones · Casos · Ficha comercial · Versión**.
  El método de oficio anterior no se ha perdido: la matriz, el orden de ataque por
  cuadrante, los tres platos intocables y las tres capas de coste están ahora en
  "Las cuatro decisiones de oficio" y repartidos por los 10 pasos del procedimiento.
- Sección **`## Cuándo se dispara`** con 12 frases reales del oficio y línea de jerga
  (escandallo, prime cost, gramaje, rendimiento, merma, TPV). Antes el disparo solo vivía
  en el `description` del frontmatter.
- Sección **`## Quién lo ejecuta`**: dueño o gerente fuera de servicio, 45-90 minutos,
  presión de credibilidad ante quien conoce sus propios números.
- Sección **`## Entrada`** con siete datos y qué se hace si falta cada uno, más el bullet
  obligatorio **Dato sucio típico** (export del POS con platos retirados, botones que
  agrupan varios platos, IVA mezclado).
- Sección **`## Reglas`**: 11 filas SIEMPRE y 9 filas NUNCA, todas verificables leyendo el
  informe que sale.
- Sección **`## Antipatrones`**: los 5 fallos más probables con síntoma observable, causa
  raíz y corrección. Uno marcado `[DERIVADO, NO OBSERVADO EN CAMPO]`.
- `cases/case_01_happy_path.md`, `case_02_edge_case.md`, `case_03_failure.md`,
  `case_04_integration.md` — los cuatro **ejecutados contra el motor**, con la salida real
  pegada. Ninguna cifra narrada.
- `references/FUENTES.md` — fuentes externas verificadas el 16-ago-2026 con URL y la
  afirmación concreta que sostiene cada una, más la tabla de lo que queda `[A VALIDAR]`.
- `ANEXO-A-ficha-comercial.md`, `README.md`, `metadata.json`, este `CHANGELOG.md`.

### Corregido
- `scripts/escandallo.py`: el aviso de desviación imprimía literalmente "3-5 puntos" para
  cualquier desviación superior a 2, de modo que una desviación de 2,87 se anunciaba como
  "3-5 puntos". Ahora dice "más de 2 y hasta 5 puntos". Solo cambia el texto; el corte
  numérico (>2 y >5) es el mismo y ningún resultado se altera.
- El umbral de popularidad del 70% se atribuía a Kasavana-Smith sin cita. Ahora tiene
  cita primaria (1982) y fuente secundaria consultable verificada.

### Marcado `[A VALIDAR]` (antes se presentaba como dato firme)
- El corte de **desviación > 5 puntos = problema de control**: es criterio de oficio. Las
  fuentes disponibles hablan de 1 punto (Restaurant365) y de 1-2 puntos medidos en cinco
  locales durante 12 meses (Chefs Resources), y ninguna publica el corte superior.
- Los rangos de **food cost y prime cost por tipología** de
  `references/rendimientos-y-umbrales.md`: proceden de guías sectoriales sin metodología
  publicada.
- La **comisión de plataformas de reparto (25-30%)**: solo hay blogs comerciales. La skill
  ya no la usa para calcular; excluye el reparto del informe estándar y pide el contrato.

## [1.0.0] — 2026-08-11
Primera versión: método de escandallo con rendimiento, merma y costes ocultos; matriz de
Kasavana-Smith; formato de informe; `references/rendimientos-y-umbrales.md`;
`assets/plantilla-datos.json`; `scripts/escandallo.py`.
