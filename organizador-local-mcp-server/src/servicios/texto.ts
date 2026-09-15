/**
 * Extracción de texto.
 *
 * Es la pieza que separa este servidor de un script de reglas: permite al
 * agente leer el CONTENIDO y decidir, en vez de adivinar por el nombre.
 * Un `document.pdf` no dice nada; su primera página, todo.
 *
 * No se añade ninguna dependencia de terceros: se usa lo que macOS ya trae
 * (`textutil`, `mdimport`) y lo que suele estar (`pdftotext`, `unzip`), y si
 * no está, se dice con claridad en vez de fallar en silencio.
 */

import { execFile } from "node:child_process";
import * as fs from "node:fs/promises";
import * as path from "node:path";
import { promisify } from "node:util";
import {
  EXTENSIONES_OOXML,
  EXTENSIONES_TEXTO,
  EXTENSIONES_TEXTUTIL,
  LIMITE_CARACTERES,
} from "../constantes.js";

const ejecutar = promisify(execFile);

export interface TextoExtraido {
  texto: string;
  metodo: string;
  truncado: boolean;
  bytesOriginal: number;
}

/** ¿Está disponible el binario? */
async function hayBinario(nombre: string): Promise<boolean> {
  try {
    await ejecutar("which", [nombre], { timeout: 5_000 });
    return true;
  } catch {
    return false;
  }
}

/** Colapsa espacios y líneas en blanco: el ruido no ayuda a clasificar. */
function compactar(bruto: string): string {
  return bruto
    .replace(/\r\n?/g, "\n")
    .replace(/[ \t ]+/g, " ")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

/** Quita etiquetas XML/HTML dejando el texto, con separación entre nodos. */
function quitarEtiquetas(xml: string): string {
  return xml
    .replace(/<(w:p|w:br|w:tab|a:p|text:p|tr|\/tr|\/p|br)\b[^>]*>/gi, "\n")
    .replace(/<[^>]+>/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/&#(\d+);/g, (_, n: string) => String.fromCharCode(Number(n)));
}

/** Piezas internas de cada formato OOXML donde vive el texto. */
const PIEZAS_OOXML: Record<string, string[]> = {
  ".docx": ["word/document.xml"],
  ".pptx": ["ppt/slides/slide1.xml", "ppt/slides/slide2.xml", "ppt/slides/slide3.xml"],
  ".xlsx": ["xl/sharedStrings.xml", "xl/worksheets/sheet1.xml"],
};

async function desdeOoxml(ruta: string, ext: string): Promise<string> {
  if (!(await hayBinario("unzip"))) {
    throw new Error("hace falta `unzip` para leer este formato y no está disponible");
  }
  const trozos: string[] = [];
  for (const pieza of PIEZAS_OOXML[ext] ?? []) {
    try {
      const { stdout } = await ejecutar("unzip", ["-p", ruta, pieza], {
        timeout: 30_000,
        maxBuffer: 32 * 1024 * 1024,
      });
      if (stdout.trim()) trozos.push(quitarEtiquetas(stdout));
    } catch {
      // La pieza puede no existir (un .pptx de una sola diapositiva, por ejemplo).
    }
  }
  if (!trozos.length) throw new Error("el paquete no contenía texto legible");
  return trozos.join("\n\n");
}

/**
 * Extrae el texto de un fichero.
 *
 * Devuelve siempre algo útil o un error explicativo: nunca una cadena vacía
 * sin decir por qué.
 */
export async function extraerTexto(
  ruta: string,
  limite: number = LIMITE_CARACTERES,
): Promise<TextoExtraido> {
  const st = await fs.stat(ruta);
  if (!st.isFile()) throw new Error(`No es un fichero: ${ruta}`);

  const ext = path.extname(ruta).toLowerCase();
  let bruto: string;
  let metodo: string;

  if (EXTENSIONES_TEXTO.includes(ext)) {
    // Solo se lee el principio: para clasificar basta, y un log de 2 GB no cabe.
    const manejador = await fs.open(ruta, "r");
    try {
      const buffer = Buffer.alloc(Math.min(st.size, limite * 4));
      const { bytesRead } = await manejador.read(buffer, 0, buffer.length, 0);
      bruto = buffer.subarray(0, bytesRead).toString("utf8");
    } finally {
      await manejador.close();
    }
    metodo = "lectura directa";
  } else if (ext === ".pdf") {
    if (!(await hayBinario("pdftotext"))) {
      throw new Error(
        "para leer PDF hace falta `pdftotext`, que no está instalado. " +
          "En macOS: `brew install poppler`. " +
          "Mientras tanto, usa organizador_inventariar y clasifica por nombre y fecha.",
      );
    }
    const { stdout } = await ejecutar("pdftotext", ["-l", "5", "-q", ruta, "-"], {
      timeout: 60_000,
      maxBuffer: 32 * 1024 * 1024,
    });
    bruto = stdout;
    metodo = "pdftotext (5 primeras páginas)";
  } else if (EXTENSIONES_OOXML.includes(ext)) {
    bruto = await desdeOoxml(ruta, ext);
    metodo = `unzip + XML (${ext})`;
  } else if (EXTENSIONES_TEXTUTIL.includes(ext)) {
    if (process.platform !== "darwin" || !(await hayBinario("textutil"))) {
      throw new Error(
        `\`${ext}\` necesita \`textutil\`, que solo existe en macOS. ` +
          "Convierte el fichero a PDF o a texto y vuelve a intentarlo.",
      );
    }
    const { stdout } = await ejecutar(
      "textutil",
      ["-convert", "txt", "-stdout", ruta],
      { timeout: 60_000, maxBuffer: 32 * 1024 * 1024 },
    );
    bruto = stdout;
    metodo = "textutil";
  } else {
    throw new Error(
      `No sé extraer texto de \`${ext || "(sin extensión)"}\`. ` +
        `Formatos que sí leo: ${[...EXTENSIONES_TEXTO, ".pdf", ...EXTENSIONES_OOXML, ...EXTENSIONES_TEXTUTIL].join(", ")}. ` +
        "Para el resto, clasifica por nombre, tamaño y fecha con organizador_inventariar.",
    );
  }

  const limpio = compactar(bruto);
  if (!limpio) {
    throw new Error(
      "El fichero se abrió pero no tiene texto extraíble. " +
        "Puede ser un PDF escaneado (solo imagen) o un documento vacío.",
    );
  }

  const truncado = limpio.length > limite;
  return {
    texto: truncado ? limpio.slice(0, limite) : limpio,
    metodo,
    truncado,
    bytesOriginal: st.size,
  };
}
