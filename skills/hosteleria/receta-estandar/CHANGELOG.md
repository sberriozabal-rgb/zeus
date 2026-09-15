# CHANGELOG — receta-estandar

Formato de versión: `[nombre]_v[MAYOR].[MENOR].[PARCHE]` según el estándar
ZEUS de versionado (ver ZEUS_02_INSTRUCCIONES, sección 4).

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
