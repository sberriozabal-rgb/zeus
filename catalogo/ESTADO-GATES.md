# Matriz de gates y riesgos abiertos

Los cinco gates de la casa: **G1** producto (≥16/20) · **G2** prueba (3 casos
reales, uno sucio) · **G3** precio (comprador nombrado + cifra firmada) ·
**G4** legal (licencia verificada) · **G5** público (sin cifra inventada).

## Hostelería

| Skill | G1 | G2 | G3 | G4 | G5 | Nota |
|---|:--:|:--:|:--:|:--:|:--:|---|
| `escandallo-ingenieria-menu` | ✅ | ❌ | ⚠️ | ✅ | ❌ | 19/20 |
| `respuesta-resenas` | ✅ | ❌ | ⚠️ | ✅ | ❌ | 19/20 |
| `apertura-cierre-turno` | ✅ | ❌ | ⚠️ | ✅ | ❌ | 19/20 |
| `comparativa-proveedores` | ✅ | ❌ | ⚠️ | ✅ | ❌ | 18/20 |
| `receta-estandar` | ✅ | ❌ | ⚠️ | ❌ | ❌ | 18/20 · **G4 abajo** |
| `productividad-personal-turno` | ❌ | ❌ | ❌ | ❌ | ❌ | ficha con los 5 gates sin marcar |
| `reporte-inteligencia-competencia` | — | — | — | — | — | sin ficha comercial |

⚠️ = G3 marcado en la ficha con comprador nombrado y canal, pero **la cifra sigue
`[A VALIDAR]` a la espera de firma**.

## CABINA (DJ)

Ficha comercial escrita para las seis y **envoltorio cerrado el 15-sep-2026**. Nota medida con
el validador de la casa (`validar_skill.py`), no estimada.

| Skill | Antes | Ahora | G1 | G2 | G3 | G4 | G5 |
|---|---|---|:--:|:--:|:--:|:--:|:--:|
| `auditoria-de-biblioteca` | 0/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ❌ |
| `postmortem-de-bolo` | 1/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ❌ |
| `presupuesto-y-contrato-evento` | 1/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ❌ |
| `set-por-encargo` | 2/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ❌ |
| `peticiones-a-repertorio` | 2/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ❌ |
| `demo-a-sello` | 2/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ❌ |

**Por qué 19 y no 20.** El validador devuelve **20/20 mecánico** en las seis. No se firma el 20:
el punto 19 es de criterio —*"que las URLs estén verificadas, no solo presentes"*— y en esta
pasada no se han reverificado una a una. Es el mismo criterio con el que la casa corrigió a la
baja el 20/20 de `escandallo-ingenieria-menu`. **No se redondea al alza.**

**Qué se cerró en cada una:** estructura de 13 secciones del ADN, procedimiento en 6 pasos
atómicos con el molde Entrada → Acción → Salida → Si falta el dato, 10 reglas SIEMPRE y 9 NUNCA
con su porqué, 5 antipatrones con síntoma/causa/corrección, los 4 casos de prueba con entrada y
salida reales, y los ficheros del peldaño P1: `CHANGELOG.md`, `README.md`, `LICENSE.txt`,
`metadata.json` y `references/FUENTES.md` donde faltaba.

**El contenido de oficio no se tocó.** Las notas de 0-2/20 nunca midieron la calidad del
oficio: medían conformidad de formato. Las tablas de riesgo por hallazgo, las seis curvas de
energía, los cuatro cubos con sus umbrales, las seis cláusulas críticas y los plazos de Beatport
y Spotify ya estaban y son el producto. Lo que faltaba era la forma que la casa exige para poder
cobrar.

**G3 levantado** el 15-sep-2026: 49 € suelta, 149 € CORE, 99 € EVENTOS, 249 € COMPLETA.
**G4 en orden**: licencia de comprador redactada en las seis, y `presupuesto-y-contrato-evento`
lleva además aviso legal no negociable de que no es asesoramiento jurídico.

**G2 sigue abajo, y solo lo levanta el primer comprador.** Los 4 casos de cada skill son de
fabricación: ninguna se ha ejecutado contra los datos reales de alguien que haya pagado.

**Calibración del validador:** contra las skills de hostelería devuelve 17-19/20, coincidiendo
con sus notas declaradas. Es fiable.


## Neutra / B2B

| Skill | Nota declarada | Ficha | Observación |
|---|---|---|---|
| `cobro-cartera-vencida` | 19/20 | no | La mejor posicionada del catálogo para venta suelta |
| `reporte-inteligencia` | 18/20 | no | *"pendiente de reauditoría tras v1.1.0"* — reauditar antes de publicar |
| `respaldo-proyecto-ia-cl` | 18/20 *(autoevaluación)* | no | Auditoría propia, no externa |
| `universal-compilador-contexto` | 17/20 *(autoevaluación)* | no | Auditoría propia, no externa |

---

## Riesgos abiertos

### 1 · `checklist-turno` duplica a `apertura-cierre-turno` con licencia incompatible

Las dos skills tienen **la misma descripción palabra por palabra** y el mismo
producto. Las licencias se contradicen:

- `apertura-cierre-turno` → *"uso comercial sin derecho de redistribución"* (se vende)
- `checklist-turno` → *"uso libre, incluido el comercial, con atribución"* (regalada)

Vender una pieza de la Instalación Completa mientras su gemela circula con
licencia de uso libre es un problema comercial real, no una cuestión de orden.
**Hay que retirar una de las dos antes de cobrar la primera instalación.**
`checklist-turno` no se ha subido a este catálogo por ese motivo.

### 2 · Ninguna pieza ha pasado G2: cero ejecuciones contra datos reales de cliente

Es el gate que falla en todo el catálogo de hostelería. Las fichas lo declaran
sin adornos: *"los 4 casos son de fabricación. Falta ejecutarla contra 3 exports
reales de un cliente real, uno con datos sucios."* Un 19/20 en una pieza que
nunca se ha ejecutado con los datos de un cliente es nota de fábrica, no de
campo. Esto no impide vender una instalación presencial —se ejecuta en la visita
con los datos del propio cliente, que es precisamente cómo está diseñado el
Motor B—, pero sí desaconseja publicar en directorio.

### 3 · Atribución en corrección centralizada en `apertura-cierre-turno`

Su `metadata.json` dice: *"EN CORRECCION CENTRALIZADA — atribucion en revision
por la casa (15-ago-2026). **No usar en material de venta hasta cierre.**"*
La cifra de rotación que sostiene el producto no se ha revalidado. Antes de meter
esta pieza en un argumentario hay que cerrar esa atribución.

**Precedente a tener presente:** la v1.0.0 de `respuesta-resenas` afirmaba que
Google y TripAdvisor *"penalizan"* las respuestas idénticas. Ninguna política
publicada de las dos plataformas dice eso. Se retiró el 16-ago-2026. Si esa frase
llegó a algún material de venta ya enviado, hay que corregirla también ahí.

### 4 · Sobre la protección del archivo

De la doctrina, literal: *"No existe protección técnica de un archivo de texto, y
esta skill nunca la promete. Una skill es texto plano: no hay DRM, ni firma, ni
ofuscación posible. Cualquier comprador puede copiarla y pasársela a diez
colegas. Lo defendible es la cadencia de actualización, el acceso revocable, la
configuración con datos del cliente, el criterio de oficio y la velocidad de la
fábrica. Quien venda protección del archivo, miente."*

Por eso la entrega va por acceso revocable a este repositorio privado y no por
adjunto.


### 5 · `respuesta-resenas` envía la v1.0.0 mientras declara la v1.1.0

Hallazgo del validador, 15-sep-2026. La pieza puntúa **8/20**, no el 19/20 que
declara su ficha. La causa no es la rúbrica: es un **desajuste de versión**.

- `SKILL.md` frontmatter → `version: "1.0.0"`
- `metadata.json` → `"version": "1.1.0"`, `"fecha_revision": "2026-08-16"`
- `CHANGELOG.md` → **solo tiene entrada 1.0.0**, más un «Roadmap v1.1»

La ficha describe con detalle cuatro piezas del ADN que *"se fabricaron el
16-ago-2026"* —pasos atómicos con rama «si falta el dato», tabla de reglas
SIEMPRE, tabla NUNCA y antipatrones— y dice que por eso la nota subió de 16 a
19/20. **El fichero que se entrega no las lleva todas**, y el CHANGELOG no
registra ninguna v1.1.0.

Es exactamente el fallo que la propia ficha de esta skill se corrigió una vez y
que la doctrina llama *nota regalada = fraude interno*. Hay que decidir qué es
verdad: o la v1.1.0 existe y no se guardó, o la ficha describe un trabajo que no
se llegó a hacer. Hasta resolverlo, esta pieza **no debe ir en material de venta
con la etiqueta 19/20**.

Nota de calibración: las otras cinco de hostelería validan en 17–19/20, en línea
con lo declarado. El problema es de esta pieza, no del catálogo.

### 6 · Frontmatter YAML inválido en 3 skills — **corregido el 15-sep-2026**

`auditoria-de-biblioteca`, `presupuesto-y-contrato-evento` y
`reporte-inteligencia` tenían la `description` como escalar plano conteniendo
`: ` (dos puntos y espacio), que **no es YAML válido**. Ejemplo:
`description: ... Solo lectura: nunca escribe en la base de datos del DJ.`

Es el antipatrón nº 2 de la doctrina, literal: *"la skill entregada al cliente da
error al cargarse en su entorno, o no aparece en su lista de capacidades"*.
Vender un activo que puede no cargar en casa del comprador es la peor primera
impresión posible, y el fallo no se ve hasta que está entregado.

**Corregido** pasando las tres a escalar de bloque `>-`, que es el formato que ya
usaban las skills de hostelería. El texto es idéntico carácter a carácter —solo
cambia el envoltorio—. Verificado: **17/17 frontmatter del catálogo parsean
correctamente.**

Conviene añadir esta comprobación al empaquetado, que es lo que la propia
doctrina manda: *"ejecutar el validador antes de empaquetar, sin excepción"*.

### 7 · Frontmatter YAML: los seis de CABINA revalidados

Tras la reescritura, los seis `SKILL.md` de CABINA vuelven a parsear correctamente y sus
`metadata` mantienen todos los valores como cadena, conforme a la especificación. **17/17 del
catálogo válidos.**