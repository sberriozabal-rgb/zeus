# Changelog — respuesta-resenas

## [1.2.0] — 2026-09-15

**Resuelto el desajuste de versión que arrastraba esta pieza, y cerrada la estructura de
serie.** La auditoría del 15-sep-2026 (`validar_skill.py`) destapó que la skill puntuaba
**8/20** mientras su ficha declaraba 19/20.

### Qué pasó de verdad

El diagnóstico inicial fue que el trabajo de la v1.1.0 no se había hecho. **Era incorrecto y
queda corregido aquí.** Las cuatro piezas que la ficha decía haber fabricado el 16-ago-2026 sí
estaban en el fichero y sí pasan la rúbrica:

| Pieza declarada el 16-ago | ¿Estaba? | Punto de la rúbrica |
|---|---|---|
| Procedimiento en pasos atómicos con rama "si falta el dato" | Sí, 8 pasos | 07 ✔ |
| Tabla de reglas SIEMPRE | Sí, 11 reglas | 10 ✔ |
| Tabla de reglas NUNCA | Sí, 10 reglas | 11 ✔ |
| Sección de antipatrones | Sí, 5 con molde completo | 12 ✔ |

Lo que falló fue otra cosa, y eran tres problemas distintos:

1. **Desajuste de versión dentro del propio fichero.** El frontmatter decía
   `version: "1.0.0"`, la sección `## Versión` del mismo `SKILL.md` decía `v1.1.0`,
   `metadata.json` decía `1.1.0`, y este CHANGELOG **no tenía entrada de 1.1.0**: solo la
   1.0.0 y un «Roadmap v1.1». Cuatro sitios, tres respuestas distintas.
2. **Estructura anterior al ADN de la casa.** El fichero usaba `## Método`,
   `## Formato del informe` y `## Lo primero: no contestes nada todavía` en lugar de las 13
   secciones de serie, así que fallaba 12 puntos de rúbrica **por nomenclatura**, no por
   contenido ausente.
3. **`## Casos de prueba` listaba los ficheros pero no los rotulaba** como Happy path / Edge
   case / Failure / Integration, de modo que los cuatro casos existían en `cases/` y aun así
   los puntos 13-16 caían.

### Qué se ha hecho

- Reestructurado a las **13 secciones del ADN**: `Qué hace`, `Cuándo se dispara`, `Quién lo
  ejecuta`, `Entrada`, `Umbral que sostiene el producto`, `Procedimiento`, `Salida`, `Límites`,
  `Reglas`, `Antipatrones`, `Casos de prueba`, `Ficha comercial`, `Versión`.
- **Procedimiento, Reglas y Antipatrones se conservan verbatim.** Ya pasaban; tocarlos habría
  sido rehacer trabajo bueno.
- `## Cuándo se dispara` con 9 disparadores más la viñeta de jerga del gremio.
- `## Entrada` dato a dato, con la viñeta obligatoria de **dato sucio típico**: el export sin
  categorizar y con fechas parciales, y la captura suelta sin histórico.
- `## Umbral que sostiene el producto` reúne por primera vez los tres umbrales en un sitio: el
  de patrón (3 menciones en 60 días, **criterio de oficio `[A VALIDAR]`**, sin contraste de
  hipótesis), el de muestra mínima (5 reseñas), el de impacto (Luca, HBS 12-016, con sus tres
  límites) y el legal (incentivos y *review gating*, con las políticas de Google y Tripadvisor
  y el art. 27.8 de la Ley 3/1991).
- `## Límites` pasa de párrafo corrido a seis viñetas, e incorpora explícitamente que **no
  aplica a cadenas ni a grupos con marca consolidada**, porque el efecto de ingresos por
  estrella está medido solo en independientes.
- `## Salida` con la plantilla en bloque de código y la sección `Supuestos de esta versión`.
- `## Casos de prueba` rotulado con los cuatro nombres de serie.
- Versión unificada en **1.2.0** en los cuatro sitios.

### Por qué 1.2.0 y no 1.1.0

La 1.1.0 llegó a declararse en `metadata.json`, en la ficha comercial y en la sección de
versión del propio `SKILL.md`, pero nunca tuvo entrada en este CHANGELOG. **Ese número está
quemado**: cualquiera que viera "1.1.0" estaba viendo un fichero que puntuaba 8/20. Reutilizarlo
mantendría la ambigüedad. Se salta a 1.2.0 y queda escrito por qué.

### Nota de auditoría

El validador devuelve **19/20**. El punto que falla es el 19, de criterio: *"que las URLs estén
verificadas, no solo presentes"*. Las ocho URLs de `references/` no se han reverificado una a
una en esta pasada. **La nota declarada es 19/20 y no se redondea al alza**, que es la regla que
esta misma pieza incumplió y por la que ha hecho falta esta versión.

## 1.0.0 — 2026-08-11

Creación inicial.

- Clasificación de reseñas en 4 categorías (positiva, negativa con motivo, negativa injusta/sin motivo, mixta) con plantilla de respuesta específica por categoría.
- Detección de patrones operativos: motivo repetido ≥3 veces en 60 días, con fuente y umbral declarados en `references/umbrales-resenas.md`.
- Traducción de tendencia de estrellas a rango de impacto en ingresos (+5% a +9% por +1 estrella, Luca/HBS, solo en independientes), siempre presentado como escenario de referencia, nunca como promesa — cumple el gate de la doctrina "no se promete resultado económico".
- Script determinista `scripts/resenas.py` con 6 comprobaciones aritméticas en `--autotest`, todas en verde.
- Corrección de antipatrón "caso failure cobarde" descubierta en la prueba del caso edge: cuando una mención de un motivo repetido carece de fecha, el sistema ya no la descarta en silencio del cálculo de patrón — declara explícitamente `posible_patron_oculto_por_fecha_faltante` para que el hueco de dato no oculte una señal operativa real.
- Plantillas de respuesta (`assets/plantillas-respuestas.md`) para las 4 categorías, más una variante para cuando el problema señalado ya se corrigió.
- Auditoría interna: 19/20. Pendiente para v1.1: referencias externas adicionales sobre cadencia óptima de solicitud de reseñas (hoy marcada [SIN VERIFICAR]).

## Roadmap v1.1

- Verificar con fuente fechada la cadencia óptima de solicitud de reseñas (hoy es criterio de oficio sin cifra de mercado).
- Explorar el cruce automático (no solo cualitativo) con `escandallo-ingenieria-menu`: si el nombre de un plato aparece tanto en una reseña negativa como en la lista de platos con desviación de food cost, marcarlo automáticamente como prioridad alta.
