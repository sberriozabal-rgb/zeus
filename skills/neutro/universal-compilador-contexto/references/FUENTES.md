# Fuentes externas — universal-compilador-contexto

Esta skill es un procedimiento de compilación, no un artefacto de mercado: sus umbrales son
criterio de oficio y así se declaran. Las fuentes externas que sí tiene son **de plataforma y de
dependencia técnica**, y determinan qué puede y qué no puede hacer.

## 1 · Límite de la ingesta de chats

**Export de datos de Claude.** Es la única vía a un historial **completo** de conversaciones. Su
enlace **caduca**, y sin él la ingesta cae a la Ruta A, que es parcial por diseño.
<https://support.claude.com/en/articles/9450526-export-your-claude-data>
Consultado: 2026-08-26, revalidado 2026-09-15.

Consecuencia operativa: **la Ruta A se declara siempre como parcial**. Presentarla como completa
es prometer una cobertura que la propia plataforma no garantiza por esa vía.

## 2 · Dependencias de extracción

La calidad de la compilación depende de qué se puede leer. Estas son las herramientas que
sostienen la fase de extracción total, y su ausencia se declara como hueco, no se disimula:

| Dependencia | Para qué | Fuente |
|---|---|---|
| **Poppler / pdftotext** | Texto de PDF con capa de texto | <https://poppler.freedesktop.org/> |
| **Tesseract OCR** | PDF escaneado sin capa de texto | <https://github.com/tesseract-ocr/tesseract> |
| **python-docx** | Documentos `.docx` | <https://python-docx.readthedocs.io/> |
| **openpyxl** | Hojas `.xlsx` | <https://openpyxl.readthedocs.io/> |

Un PDF escaneado procesado con OCR **se marca como tal** en el inventario: su texto es una
transcripción automática y puede contener errores que no existen en el original.

## 3 · Especificación del artefacto

**Agent Skills**, estándar abierto. Define el frontmatter y el empaquetado de las skills que la
compilación inventaría en la capa correspondiente.
<https://agentskills.io/specification> · Consultado: 2026-09-15.

## Umbrales SIN fuente externa — criterio de oficio de la casa

`[A VALIDAR]` en los tres casos. No proceden de literatura ni de estándar publicado:

| Umbral | Valor | Qué controla |
|---|---|---|
| Fuentes mínimas por dominio | **2** | Que la taxonomía salga del material y no de una plantilla |
| Tope de "Anexos" | **15 %** de los archivos | Que no haya un cajón de sastre disfrazado de dominio |
| Decidido vs propuesto | `PROPUESTA A VALIDAR` **por defecto** | Que una propuesta del asistente no se convierta en decisión del proyecto |

El tercero no es un número pero es el umbral que más importa: **solo un documento aprobado o un
turno del usuario levanta algo a decisión**.
