# Caso 1 · Happy path (carpeta de 120 archivos, export completo)

## Entrada

- Carpeta de trabajo con **120 archivos**: 64 `.md`, 28 `.pdf`, 18 `.docx`, 6 `.xlsx`, 4 `.pptx`.
- **Export oficial de chats descargado** → Ruta B, cobertura completa.
- Parámetros declarados por el usuario: proyecto, sector, país (ES), idioma (es), moneda (EUR).

## Censo (paso 1)

```
CENSO — 120 archivos
  .md     64      .pdf    28  (24 con capa de texto, 4 escaneados -> OCR)
  .docx   18      .xlsx    6      .pptx    4
  Duplicados exactos por hash: 3
  Versiones multiples detectadas: 2 grupos (5 archivos)
  Ilegibles: 0
```

## Taxonomía derivada (paso 5)

Se deriva **del material**, contando de qué habla cada archivo, no de una plantilla:

| Dominio | Fuentes | ¿Cumple ≥2? |
|---|---|---|
| 00 · Identidad y marca | 9 | ✔ |
| 01 · Mercado y competencia | 14 | ✔ |
| 02 · Producto y método | 31 | ✔ |
| 03 · Comercial y precios | 18 | ✔ |
| 04 · Operación | 22 | ✔ |
| 05 · Finanzas | 11 | ✔ |
| 06 · Legal y contratos | 7 | ✔ |
| **Anexos** | **8** | **6,7 % de 120** ✔ (tope: 15 %) |

Siete dominios, **ninguno por debajo de 2 fuentes**, y "Anexos" muy por debajo del tope. La
taxonomía no se rehace.

## Lo que sale del ZIP

```
PROYECTO_CONTEXTO_2026-09-15.zip
  RESUMEN_EJECUTIVO.md    RESUMEN_CONTEXTO.md    RESUMEN_CHATS.md
  INVENTARIO.md           CONFLICTOS.md          HUECOS.md
  00-06 dominios/         EXTRACCIONES_FUENTE/
```

## Los dos ficheros que de verdad usa el dueño

**`CONFLICTOS.md` — 2 entradas.** Los dos grupos de versiones múltiples:

> **[CONFLICTO 1]** El precio del paquete aparece como 4.900 € en `propuesta-FINAL.md`
> (fecha 12-ago) y como 5.400 € en `propuesta-v3.md` (fecha 19-ago). El más reciente no es el
> que se llama FINAL. **Decide el dueño.**

**`HUECOS.md` — vacío.** Los 4 PDF escaneados se procesaron con OCR y su texto está marcado como
transcripción automática en el inventario.

## Trazabilidad

`INVENTARIO.md` da, por cada uno de los 120 archivos, su dominio asignado y **su ubicación de
origen en la carpeta**. Cualquier afirmación de un maestro se puede rastrear hasta el archivo del
que salió, y de ahí al fichero real.

## Supuestos de esta versión

> Ruta B (export oficial): cobertura completa de chats. Parámetros declarados por el usuario, no
> asumidos. 4 PDF procesados con OCR y marcados como transcripción automática. 3 duplicados
> exactos depurados por hash, listados en el inventario. Dos grupos de versiones múltiples
> **no resueltos**: están en `CONFLICTOS.md`.

## Por qué es el caso central

Muestra el criterio que separa esto de descomprimir una carpeta: la taxonomía **se mide** contra
dos umbrales, las versiones contradictorias **no se resuelven en silencio**, y todo lo que se
afirma se puede rastrear hasta el archivo de origen.
