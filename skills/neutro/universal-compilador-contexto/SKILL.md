---
name: universal-compilador-contexto
description: "Archivista y editor de contexto para cualquier proyecto u oficio. Lee una carpeta de trabajo completa (ordenador, Google Drive o ZIP adjunto) y el historial de chats del proyecto, y entrega en un ÚNICO ZIP la biblioteca de contexto (maestros por dominio + RESUMEN EJECUTIVO), el RESUMEN DE TODOS LOS CHATS con decisiones y pendientes, el RESUMEN DE TODO EL CONTEXTO en una página y el INVENTARIO con listado y ubicación de cada documento producido. Úsala SIEMPRE que se pida compilar, consolidar, unificar, actualizar o recompilar el contexto de un proyecto, cargar una carpeta al proyecto, sacar la versión vigente de cada tema, resumir los chats, saber qué documentos existen y dónde están, o preparar el paquete de contexto para socios, un equipo nuevo u otra cuenta — aunque no se nombre (pásame toda la carpeta al proyecto, qué hemos decidido en los chats, dame todo en un zip, pon orden en esta documentación). No la uses para producir entregables ni opinar sobre el proyecto; extrae y ordena lo que existe."
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso comercial sin derecho de redistribución. No interpreta el negocio, solo extrae y ordena. Ver LICENSE.txt.
compatibility: Requiere Python 3.9+, pdftotext, tesseract (OCR) y las librerías python-docx, python-pptx, openpyxl. Para el historial de chats usa las herramientas recent_chats / conversation_search / read_conversation de la sesión (parcial por diseño) o el ZIP del export oficial de datos (completo).
metadata:
  version: "1.1.0"
  author: "ZEUS"
  estado: ACORDADO
  auditoria: "17/20 (autoevaluación; desglose en references/casos-y-auditoria.md)"
  fecha: "2026-08-26"
---

# universal-compilador-contexto

## Qué hace

Convierte **una carpeta de trabajo completa, el historial de chats del proyecto y el conocimiento
ya cargado en él** en **un único ZIP `<PROYECTO>_CONTEXTO_<fecha>.zip` con la biblioteca por
dominios, el resumen ejecutivo, el resumen de chats, el resumen de contexto y el inventario de
documentos con su ubicación**, para **quien dirige el proyecto**, en **una sesión de 60 a 120
minutos para una carpeta de hasta 150 archivos**.

No opina sobre el proyecto ni corrige sus cifras: **extrae y ordena lo que existe**. Su trabajo
termina exactamente donde empieza el criterio del dueño, y por eso la salida más valiosa no es la
biblioteca sino las dos listas que la acompañan: los `[CONFLICTO]` entre documentos que se
contradicen y los huecos declarados. Esas dos listas **son la agenda de decisiones** de quien
dirige.

## Cuándo se dispara

- "pásame toda la carpeta del proyecto al proyecto de Claude"
- "qué hemos decidido en todos estos chats"
- "dame todo el contexto en un zip"
- "no sé cuál es la versión vigente de cada cosa"
- "actualiza la biblioteca con lo nuevo"
- "haz el censo de la carpeta, no sé ni qué tengo"
- "quiero un resumen de todo el proyecto en una página"
- "necesito ponerle al día a un socio que entra ahora"
- jerga del gremio: "contexto", "compilar", "biblioteca", "maestros", "censo", "taxonomía",
  "dominios", "inventario", "versión vigente", "conflicto", "hueco", "base de conocimiento",
  "export de chats"

## Quién lo ejecuta

Quien dirige el proyecto, o quien administre su base de conocimiento, con **60 a 120 minutos** de
atención para una carpeta de hasta 150 archivos. El tramo alto corresponde a la fase de lectura de
chats, que es donde hay trabajo humano irreducible: el script cita y cuenta, pero **la lectura de
qué significó cada decisión la escribe una persona**.

## Entrada

- **Obligatorio:** la carpeta de trabajo con todos sus archivos. Por defecto se busca en
  `/home/claude/fuente`, y el nombre del proyecto se toma del nombre de la carpeta si no se
  indica otro.
- **Recomendado:** el historial de chats. Hay dos rutas y **rinden cosas distintas**: la Ruta A
  usa las herramientas de la sesión y es **parcial por diseño**; la Ruta B usa el ZIP del export
  oficial y es completa.
- **Recomendado:** el conocimiento ya cargado en el proyecto, que se trata como **compilación
  anterior y no como fuente primaria**.
- **Recomendado:** sector, país, idioma y moneda, si la carpeta no los declara. **Nunca se
  asumen.**
- **Dato sucio típico:** las **versiones múltiples del mismo documento** —`propuesta.md`,
  `propuesta-v2.md`, `propuesta FINAL.md`, `propuesta FINAL buena.md`— sin fecha fiable ni marca
  de vigencia. No se elige en silencio: prevalece la que el material indique como vigente y **la
  divergencia queda abierta en `[CONFLICTO]`**. El segundo dato sucio es el PDF escaneado sin capa
  de texto, que exige OCR y cuyo resultado se marca como tal.

## Umbral que sostiene el producto

**La frontera entre decidido y propuesto.** Cifras, contratos, reparto y estructura son
`PROPUESTA A VALIDAR` **por defecto**, y solo un documento aprobado o un turno del propio usuario
las levanta a decisión. Nunca un turno del asistente: una propuesta de Claude en un chat **no es
una decisión del proyecto**, y promoverla es el fallo que convierte una compilación en una
falsificación educada.

El segundo umbral es de calidad de taxonomía, y tiene cifra: la estructura se deriva **del
material y no de una plantilla**, y se rehace hasta que **ningún dominio tenga menos de 2 fuentes**
y **"Anexos" no supere el 15 % de los archivos**. Una taxonomía impuesta deja archivos sin casa y
dominios vacíos, y ese es el síntoma que se mide.

El tercero es de alcance declarado: **la Ruta A de chats es parcial por diseño**. Usa las
herramientas de la sesión, que no garantizan cobertura completa del historial. Venderla como
completa es prometer lo que no se hizo, así que el método y su alcance se declaran siempre en la
entrega. La ruta completa exige el ZIP del
[export oficial de datos](https://support.claude.com/en/articles/9450526-export-your-claude-data),
cuyo enlace caduca.

Ambos umbrales son **criterio de oficio de la casa** `[A VALIDAR]`: no proceden de literatura ni
de estándar publicado.

## Procedimiento

1. **Entrada: la carpeta de trabajo → Acción: localizar la fuente, fijar los parámetros (proyecto,
   sector, país, idioma, moneda, ruta de chats) y hacer el censo completo de archivos con
   `scripts/censo_extraccion.py` → Salida: censo con recuento por tipo, duplicados y versiones
   múltiples detectadas → Si falta un parámetro: **no se asume ninguno** que la carpeta no
   declare; se pregunta o se marca como hueco.**

2. **Entrada: el censo → Acción: extracción total del texto de cada archivo a
   `EXTRACCIONES_FUENTE/`, aplicando OCR donde haga falta → Salida: el texto de todos los
   archivos legibles, y la lista de ilegibles → Si un archivo no se puede extraer: entra en la
   lista de huecos con su motivo, y **no se infiere su contenido por el nombre**.**

3. **Entrada: el historial de chats → Acción: digerirlos por la Ruta A (herramientas de sesión,
   parcial) o la Ruta B (ZIP del export, completa), declarando cuál se usó → Salida: borrador de
   `RESUMEN_CHATS.md` con citas y recuentos → Si se usa la Ruta A: se declara **parcial por
   diseño** en la propia entrega, nunca se presenta como completa.**

4. **Entrada: el borrador de chats → Acción: escribir la **lectura humana** de cada conversación:
   qué se decidió, qué quedó propuesto y qué sigue abierto, etiquetando `PROPUESTA A VALIDAR`
   todo lo que no tenga documento aprobado o turno del usuario detrás → Salida: `RESUMEN_CHATS.md`
   completo → Si la única fuente de un "se decidió X" es un turno del asistente: vuelve a
   `PROPUESTA A VALIDAR`.**

5. **Entrada: las extracciones → Acción: derivar la taxonomía del material, depurar duplicados y
   unificar versiones, abriendo `[CONFLICTO]` donde dos documentos vigentes se contradigan →
   Salida: biblioteca por dominios con sus maestros → Si algún dominio queda con menos de 2
   fuentes o "Anexos" supera el 15 % de los archivos: se rehace la taxonomía, no se entrega así.**

6. **Entrada: la biblioteca → Acción: montar el inventario de documentos con su ubicación de
   origen y empaquetar todo en un **ZIP único** con `scripts/empaquetar.py` → Salida:
   `<PROYECTO>_CONTEXTO_<fecha>.zip` → Si hay petición expresa de sueltos: es la única excepción;
   por defecto **no se entrega más de un ZIP ni se sueltan los `.md` fuera de él**.**

7. **Entrada: el ZIP montado → Acción: pasar el autocontrol —trazabilidad, conflictos abiertos,
   marcos no fusionados, confidencialidad, autonomía de fragmento— y verificar que no queda
   ninguna lectura pendiente de escribir → Salida: ZIP verificado o lista de correcciones →
   Si queda alguna lectura sin escribir: no se entrega, porque un resumen sin lectura es un
   índice.**

8. **Entrada: el ZIP verificado → Acción: entregar y cargar al proyecto, subiendo versión y
   **reemplazando** los compilados anteriores → Salida: contexto vigente cargado y versionado →
   Si quedan compilaciones viejas en el proyecto: se retiran, porque contexto acumulado
   contamina las respuestas.**

## Salida

```
<PROYECTO>_CONTEXTO_<fecha>.zip
 ├── RESUMEN_EJECUTIVO.md      <- una pagina, lo que hay que saber
 ├── RESUMEN_CONTEXTO.md       <- todo el contexto en una pagina
 ├── RESUMEN_CHATS.md          <- citas + LECTURA por chat, decidido vs propuesto
 ├── INVENTARIO.md             <- cada documento, su dominio y su ubicacion de origen
 ├── CONFLICTOS.md             <- documentos vigentes que se contradicen
 ├── HUECOS.md                 <- lo que no se pudo leer o no estaba
 ├── 00-09 dominios/           <- maestros derivados del material
 └── EXTRACCIONES_FUENTE/      <- texto extraido, para trazabilidad

## Supuestos de esta versión
[ruta de chats usada y su alcance, parametros asumidos, versiones elegidas,
 archivos ilegibles, dominios con pocas fuentes]
```

Los dos ficheros que más valen no son los maestros: **`CONFLICTOS.md` y `HUECOS.md` son la agenda
de decisiones del dueño.** Resolverlos en silencio sería decidir por él.

## Límites

- **No opina sobre el proyecto ni corrige sus cifras.** Extrae y ordena lo que existe; los
  conflictos y los huecos se devuelven, no se resuelven.
- **No modifica la carpeta original.** Todo lo nuevo vive en `CONTEXTO`.
- La **Ruta A de chats es parcial por diseño**: usa las herramientas de la sesión y no garantiza
  cobertura completa. La completa exige el ZIP del export oficial.
- El conocimiento ya cargado en el proyecto se trata como **compilación anterior**, no como fuente
  primaria: compilar sobre un resumen es copia de copia y hereda el error.
- No asume sector, país, idioma ni moneda que la carpeta no declare.
- Las credenciales y claves **no entran** en el paquete: se avisa y se dejan fuera.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Leer la fuente antes de escribir un maestro | Un maestro redactado desde un resumen previo es copia de copia: el error se hereda y además se firma |
| Declarar el método de chats y su alcance | La Ruta A es parcial por diseño, y venderla como completa es prometer lo que no se hizo |
| Etiquetar `PROPUESTA A VALIDAR` por defecto cifras, contratos, reparto y estructura | Solo un documento aprobado o un turno del usuario levanta algo a decisión |
| Dejar los conflictos a la vista, con la vigente en el cuerpo | Resolver una contradicción en silencio es decidir por el dueño |
| Marcar `[CONFIDENCIAL]` todo dato de tercero identificable y anonimizar casos | Sin autorización escrita en la carpeta, un caso con nombre es un problema de datos personales |
| Entregar aunque falte una capa, con los huecos declarados | Bloquear es el fallo más caro: media biblioteca útil vale más que ninguna |
| Versionar y reemplazar los compilados anteriores | Contexto viejo acumulado en el proyecto contamina todas las respuestas siguientes |
| Derivar la taxonomía del material y no de la plantilla | Una taxonomía impuesta deja archivos sin casa y dominios vacíos |
| Rehacer la taxonomía si un dominio no llega a 2 fuentes o "Anexos" supera el 15 % | Son los dos síntomas medibles de que la estructura no salió del material |
| Escribir la lectura humana de cada chat antes de empaquetar | El script cita y cuenta; qué significó cada decisión solo lo sabe quien estuvo |

| NUNCA | Porqué |
|---|---|
| Inventar un dato para rellenar un dominio | Un hueco declarado es información; un dato plausible es deuda que pagará otro |
| Fusionar marcos incompatibles | Son hipótesis distintas, no dos redacciones del mismo dato, y el promedio no existe en ninguna de las dos |
| Modificar la carpeta original | Todo lo nuevo vive en `CONTEXTO`; tocar el origen destruye la única referencia contra la que verificar |
| Promover una propuesta del asistente a decisión del proyecto | Es el fallo que convierte una compilación en una falsificación educada |
| Copiar párrafos con "según el documento X" | El buscador recupera fragmentos, y un fragmento pegado no se entiende solo fuera de su documento |
| Entregar más de un ZIP o soltar los `.md` fuera de él | Salvo petición expresa; si no, el contexto se dispersa y deja de haber una versión vigente |
| Opinar sobre el proyecto o corregir sus cifras | Conflictos y huecos son la lista de decisiones del dueño, y ahí termina el oficio |
| Asumir sector, país, idioma o moneda que la carpeta no declare | Un supuesto de moneda o de país se propaga a todos los maestros sin que nadie lo vea |
| Meter credenciales o claves en el paquete | Su valor es exclusivamente el acceso que conceden, y un paquete se copia una vez de más |

## Antipatrones

1. **Síntoma**: los maestros repiten rutas del proyecto y no citan archivos de la carpeta, o `RESUMEN_CHATS.md` son citas sin ninguna lectura escrita. **Causa raíz**: se saltó la extracción total y se redactó desde un resumen previo, o se entregó el borrador del script como si fuera el resumen. **Corrección**: repetir la extracción y reescribir desde `EXTRACCIONES_FUENTE/`, y escribir la lectura chat por chat antes de empaquetar.

2. **Síntoma**: nueve dominios de plantilla, tres de ellos vacíos y veinte archivos amontonados en "Anexos". **Causa raíz**: la taxonomía no se derivó del material, se impuso. **Corrección**: rehacer la fase de taxonomía hasta que ningún dominio tenga menos de 2 fuentes y "Anexos" no supere el 15 % de los archivos.

3. **Síntoma**: aparece una sola cifra donde los documentos de origen daban dos, procedentes de marcos distintos. **Causa raíz**: fusión indebida de hipótesis incompatibles. **Corrección**: separar las dos y abrir `[CONFLICTO]`; el promedio no existe en ninguno de los dos marcos.

4. **Síntoma**: un maestro afirma "se decidió X" y la única fuente es un turno del asistente en un chat. **Causa raíz**: atribución perdida al digerir la conversación. **Corrección**: devolverlo a `PROPUESTA A VALIDAR`; solo un documento aprobado o un turno del usuario levanta algo a decisión.

5. **Síntoma**: el índice declara "sin descartes, sin huecos" en una carpeta que tiene cuatro versiones del mismo documento. **Causa raíz**: el censo no se revisó y las versiones múltiples pasaron como archivos distintos. **Corrección**: rehacer el censo, listar las versiones y dejar la divergencia en `[CONFLICTO]` en lugar de elegir en silencio.

## Casos de prueba

Los cuatro casos están en `cases/`. El desglose completo y la rúbrica siguen en
[`references/casos-y-auditoria.md`](references/casos-y-auditoria.md).

**Happy path** (`cases/case_01_happy_path.md`): carpeta de 120 archivos con export de chats
completo. Taxonomía derivada en 7 dominios, todos con 2 o más fuentes.

**Edge case** (`cases/case_02_edge_case.md`): cuatro versiones del mismo documento sin fecha
fiable. No se elige en silencio: se abre `[CONFLICTO]` y decide el dueño.

**Failure** (`cases/case_03_failure.md`): sin acceso a los chats y con 18 PDF escaneados
ilegibles. El ZIP sale igual con los huecos declarados.

**Integration** (`cases/case_04_integration.md`): encadenado con `respaldo-proyecto-ia-cl`, que
produce el `chats.jsonl` y el `HUECOS.md` que este compilador consume.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
