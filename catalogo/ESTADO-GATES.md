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

Las seis: **sin ficha comercial**, luego sin matriz de gates. G4 es el único que
se puede dar por bueno de entrada —la licencia *"uso permitido al comprador;
prohibida la redistribución"* está redactada y es coherente con la venta—.
G1 es plausible (las seis son ACORDADO) pero **ninguna declara nota de auditoría**.

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
