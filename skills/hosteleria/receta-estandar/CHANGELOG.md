# CHANGELOG — receta-estandar

Formato de versión: `[nombre]_v[MAYOR].[MENOR].[PARCHE]` según el estándar
ZEUS de versionado (ver ZEUS_02_INSTRUCCIONES, sección 4).

## v1.1.1 — 2026-09-15

**Cierra el "Pendiente declarado" de la v1.1.0 y deja la pieza lista para la revisión técnica
externa.** Sube de 17/20 a 19/20 declarado (20/20 mecánico).

### Para el consultor de seguridad alimentaria — cada cifra tocada, con su fuente

Esta versión **cambia cifras de inocuidad**. Todas en dirección conservadora o de anclaje, y
todas listadas aquí para que la revisión externa (requisito (a) del G4) las confirme o corrija:

| Dónde | Antes | Ahora | Fuente |
|---|---|---|---|
| `case_01` conservación del salmón porcionado | ≤4 °C, "práctica de oficio; ver nota de región" (**la nota no existía**) | ≤4 °C anclado: el RD exige ≤8 °C para <24 h; la ficha aplica el umbral de >24 h por criterio con pescado crudo, **más estricto que el mínimo** | RD 3484/2000 art. 7 |
| `case_01` vida útil del porcionado | "24 h", sin fuente | 24 h, que es el umbral del RD entre comida refrigerada de corta y larga duración | RD 3484/2000 art. 7 |
| `case_01` mantenimiento en caliente del puré (paso 8, PCC 8, sección 6) | ≥63 °C (AESAN) | **≥65 °C** | RD 3484/2000 art. 7 — norma reglamentaria; AESAN-2021-004 es opinión científica y fija 63. Prevalece el RD ante inspección |
| `case_01` temperatura de servicio del plato | ≥63 °C | ≥65 °C | ídem |
| `case_04` puré de pase | ≥63 °C | ≥65 °C | ídem |
| `case_01` regeneración del puré | sin binomio | ≥74 °C/15 s | AESAN-2021-004, recalentamiento |
| `scripts/escalar_receta.py --ejemplo` (salsa de tomate) | `temp_min_c: 74`, sin tiempo, sin norma, sin país | `70 °C / 120 s`, norma AESAN vegetales, `pais_operacion: ES` | AESAN-2021-004, categoría vegetales: 70 °C durante 2 min. **74 °C era la cifra de aves/rellenos, no de una salsa de tomate** |
| `scripts/escalar_receta.py --ejemplo` conservación | "≤4 °C, 3 días", sin fuente | igual, anclado: >24 h → ≤4 °C | RD 3484/2000 art. 7 |

**La discrepancia AESAN / RD 3484/2000 en mantenimiento en caliente es el hallazgo de esta
versión.** Dentro de España las dos fuentes oficiales no coinciden (63 frente a 65 °C). Se ha
aplicado la reglamentaria y se ha declarado la discrepancia en `temperaturas_haccp.md`, en la
sección `Umbral` del `SKILL.md`, en `FUENTES.md` (fuente 7, nueva) y en la cláusula 6 del anexo
contractual. **El consultor debe confirmar el criterio.**

**No se ha tocado ningún binomio de cocinado** (pescado 68/15 s, aves 74/1 s, etc.): siguen
siendo de AESAN y el RD no los regula.

### Añadido
- `references/FUENTES.md` fuente 7: Real Decreto 3484/2000, art. 7, con URL del BOE, cifras
  verificadas y qué sostiene y qué no.
- `references/temperaturas_haccp.md` tabla A-bis con las cuatro cifras del RD, y dos filas
  nuevas en "Dónde discrepan": mantenimiento en caliente AESAN/RD, y **el 4 °C que significa
  cosas distintas en cada país** (conservación >24 h en España; recepción de pescado en México).
- `venta/ANEXO-CONTRATO-INOCUIDAD.md`: cláusula contractual que traslada al titular la
  inocuidad, la validación de cada binomio y los alérgenos. Es el requisito (b) del G4.
  **Pendiente de revisión jurídica.**
- Pie de ficha "Supuestos de esta versión" en `## Salida`.

### Corregido
- Tres defectos de estructura de la rúbrica: URLs inline en `## Umbral`, supuestos en
  `## Salida`, y el antipatrón 3 con `**Causa raíz**` partido en dos líneas.
- Referencia colgante "ver nota de región" en `case_01`: eliminada, sustituida por el anclaje.
- Versión unificada en frontmatter, `metadata.json`, ficha y CHANGELOG.

### Sigue pendiente, y no lo puede hacer la casa
- **(a) Revisión técnica externa** de `## Límites`, de la declaración de no-APPCC y de las tablas
  de `temperaturas_haccp.md`, incluida la discrepancia AESAN/RD.
- Revisión jurídica del anexo contractual, en particular las cláusulas 3 (alérgenos) y 5
  (exclusión de responsabilidad).
- El campo de unidad de compra / rendimiento / merma en el contrato JSON: sigue en v1.2.0.

**Hasta que (a) esté hecha, `receta-estandar` no se factura.** G4 sigue abajo a propósito.

## v1.1.0 — 2026-08-16

### Añadido
- `cases/case_04_integration.md` — encadenamiento con `escandallo-ingenieria-menu`: la ficha
  aporta gramaje exacto y merma de limpieza declarada, que es la entrada que el escandallo
  necesita para calcular el coste real del plato.
- `README.md`, `LICENSE.txt`, `metadata.json` y `ANEXO-A-ficha-comercial.md`.

### Cambiado
- Las tablas de temperatura y tiempo pasan de referencia británica (FSA UK) a **AESAN-2021-004
  (España) y NOM-251-SSA1-2009 (México)**, con el apartado citado en cada fila. Es el cambio de
  más valor de esta versión: ancla la seguridad alimentaria a la norma del mercado donde se vende.
- `metadata.contrato_salida_hacia` nombraba tres skills inexistentes (`escandallo-costos`,
  `ingenieria-menu`, `checklist-operativo`). Corregido a las reales.

### Pendiente declarado
- Tres cifras de inocuidad viven en `cases/case_01_happy_path.md` y en el `--ejemplo` de
  `scripts/escalar_receta.py` **sin ancla de norma y sin marca `[A VALIDAR]`**: refrigeración
  ≤4 °C, vida útil de 24 h desde el porcionado, y un punto crítico a 74 °C sin `tiempo_min_s`.
  En NOM-251 el 4 °C es de recepción (§7.4.2); el de conservación es ≤7 °C (§7.3.3). Son riesgo
  legal en una skill de seguridad alimentaria y se corrigen antes de cobrar por ella.
- El contrato JSON de `SKILL.md § Salida` no tiene campo para unidad de compra, rendimiento de
  limpieza ni merma de cocción: viven en texto libre en la columna *Nota*. Sin ese campo el
  escandallo sale bajo por construcción. Entra en v1.2.0.

## v1.0.0 — 2026-08-11

**Tipo:** CREAR (primera versión).

**Motivo:** segunda skill de la cola de producción del vertical Gastronomía
(REGISTRO_ZEUS.md, sección 6), fabricada como excepción declarada a la regla
anti-deriva — `escandallo-costos` (nº1 de la cola) todavía no tiene uso real
documentado en OCTAVA al momento de esta entrega. Excepción autorizada
directamente por Sergio.

**Contenido:**
- `SKILL.md` — protocolo de 8 pasos, 8 SIEMPRE / 8 NUNCA, 5 antipatrones,
  matriz de aplicabilidad, 4 casos de prueba, contrato de interfaz JSON hacia
  `escandallo-costos`, `ingenieria-menu` y `checklist-operativo`.
- `references/temperaturas_haccp.md` — tabla de temperaturas mínimas de
  seguridad, fuente FoodDocs/Food Standards Agency UK, con aviso explícito de
  que son cifras de normativa británica a contrastar por país.
- `references/equivalencias_cocina.md` — tabla de conversión de unidades
  caseras a gramaje, marcada como práctica sectorial no normada.
- `scripts/escalar_receta.py` — escala cantidades de ingredientes por factor o
  por número de porciones destino, sin tocar tiempos ni temperaturas
  (corrige el antipatrón "la escala rota"). Probado con `--ejemplo`.

**Auditoría de entrega:** 17/20 — ver informe de auditoría adjunto en el
registro del proyecto (`REGISTRO_ARTEFACTOS.md`, entrada 006).

**Roadmap v1.1.0 (qué falta, declarado, no prometido):**
- Sustituir la tabla de equivalencias de cocina por una fuente única citable
  con URL (hoy es conocimiento de oficio declarado como tal, no una
  publicación específica verificada) — sube el criterio 12 de la rúbrica.
- Añadir declaración explícita de techo de escalabilidad del script
  (¿se degrada la precisión de redondeo o el sentido físico de la receta por
  encima de qué factor de multiplicación?) — sube el criterio 16.
- Reemplazar los 4 casos sintéticos por fichas reales de recetas
  estandarizadas en un restaurante en producción, con pesaje documentado —
  mismo patrón de mejora que el resto del catálogo ZEUS (ver
  REGISTRO_ARTEFACTOS.md, sección "Patrones que se repiten").
- Anexo regional de temperaturas HACCP para México (NOM-251-SSA1) en vez de
  depender solo de la referencia británica — candidato a ADAPTAR con
  `zeus-skill-localizer`.
- Validar contra `zeus-skill-auditor` cuando esa pieza esté disponible en el
  mismo entorno de trabajo, para una segunda lectura independiente de esta
  autoauditoría.
