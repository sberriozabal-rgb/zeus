/**
 * Herramientas de solo lectura. Ninguna toca el disco.
 */

import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import * as path from "node:path";
import { z } from "zod";
import { CARPETA_DESCARGAS, CARPETA_SISTEMA, TAXONOMIA } from "../constantes.js";
import { huella, recorrer, type FichaFichero } from "../servicios/ficheros.js";
import { leerDiario } from "../servicios/registro.js";
import {
  baseDescargas,
  baseDocumentos,
  raicesPermitidas,
  resolverSeguro,
} from "../servicios/rutas.js";
import { extraerTexto } from "../servicios/texto.js";
import {
  campoDesplazamiento,
  campoFormato,
  campoLimite,
  error,
  explicar,
  humanizarBytes,
  paginar,
  respuesta,
} from "./comun.js";

const SOLO_LECTURA = {
  readOnlyHint: true,
  destructiveHint: false,
  idempotentHint: true,
  openWorldHint: false,
} as const;

export function registrarLectura(servidor: McpServer): void {
  // ---------------------------------------------------------------- raíces
  servidor.registerTool(
    "organizador_listar_raices",
    {
      title: "Listar raíces y taxonomía",
      description: `Muestra dónde puede trabajar este servidor y con qué criterio clasifica.

Llama a esta herramienta PRIMERO, antes que a ninguna otra: sin saber las raíces
no se puede construir una ruta válida, y toda ruta fuera de ellas se rechaza.

Args: ninguno.

Devuelve:
  {
    "raices": string[],            // rutas absolutas donde se puede operar
    "base_documentos": string|null,// dónde vive la taxonomía
    "base_descargas": string|null, // carpeta que se puede fusionar
    "taxonomia": string[],         // las once carpetas de destino
    "plataforma": string,          // 'darwin' en Mac
    "snapshot_disponible": boolean // si hay red de seguridad APFS
  }

Ejemplos:
  - Úsala cuando: empiezas una sesión de organización.
  - Úsala cuando: una herramienta te devolvió "Ruta fuera de las raíces permitidas".
  - No la uses cuando: ya conoces las raíces de esta misma conversación.`,
      inputSchema: {},
      outputSchema: {
        raices: z.array(z.string()),
        base_documentos: z.string().nullable(),
        base_descargas: z.string().nullable(),
        taxonomia: z.array(z.string()),
        plataforma: z.string(),
        snapshot_disponible: z.boolean(),
      },
      annotations: SOLO_LECTURA,
    },
    async () => {
      try {
        const raices = await raicesPermitidas();
        const docs = await baseDocumentos().catch(() => null);
        const desc = await baseDescargas();
        const datos = {
          raices,
          base_documentos: docs,
          base_descargas: desc,
          taxonomia: [...TAXONOMIA],
          plataforma: process.platform,
          snapshot_disponible: process.platform === "darwin",
        };

        const lineas = [
          "# Dónde puede trabajar el servidor",
          "",
          raices.length
            ? raices.map((r) => `- \`${r}\``).join("\n")
            : "- (ninguna: comprueba que existen ~/Documentos o ~/Documents)",
          "",
          `**Base de la taxonomía:** ${docs ? `\`${docs}\`` : "no encontrada"}`,
          `**Descargas fusionable:** ${desc ? `\`${desc}\`` : "no encontrada"}`,
          `**Plataforma:** ${process.platform}` +
            (process.platform === "darwin"
              ? " (hay snapshot APFS antes de cada operación destructiva)"
              : " — **sin snapshot APFS: no hay red de seguridad**"),
          "",
          "# Las once carpetas",
          "",
          ...TAXONOMIA.map((t) => `- ${t}`),
          "",
          `Las carpetas traídas de Descargas aterrizan intactas en \`${CARPETA_DESCARGAS}\`.`,
          `El registro y el diario de deshacer viven en \`${CARPETA_SISTEMA}\`.`,
        ];
        return respuesta(lineas.join("\n"), datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );

  // ----------------------------------------------------------- inventariar
  servidor.registerTool(
    "organizador_inventariar",
    {
      title: "Inventariar una carpeta",
      description: `Lista los ficheros de una carpeta con su tamaño, fecha y extensión, paginado.

Es el punto de partida de cualquier organización: da el mapa de lo que hay.
NO lee el contenido (para eso está organizador_leer_documento) y NO mueve nada.

Omite lo que nunca se toca: ocultos, node_modules, Library, paquetes de macOS
(.app, .pages, .key, .numbers…), descargas a medias y la carpeta 00 · SISTEMA.
No sigue enlaces simbólicos.

Args:
  - ruta (string): carpeta a inventariar, dentro de las raíces permitidas
  - profundidad (number, opcional): 1 = solo el primer nivel; por defecto, todo
  - con_huella (boolean): calcula el sha256 de cada fichero (lento, pero es lo
      que permite detectar duplicados exactos). Por defecto false
  - limite (number): máximo de ficheros a devolver, 1-200 (por defecto 50)
  - desplazamiento (number): cuántos saltar, para paginar (por defecto 0)
  - response_format ('markdown'|'json'): formato (por defecto 'markdown')

Devuelve:
  {
    "ruta": string,
    "total": number, "cuenta": number, "desplazamiento": number,
    "hay_mas": boolean, "siguiente_desplazamiento": number,
    "bytes_totales": number,
    "elementos": [{ "ruta","nombre","extension","bytes","modificado","sha256"? }]
  }

Ejemplos:
  - Úsala cuando: "¿qué hay en mi carpeta de Descargas?"
  - Úsala cuando: necesitas las rutas exactas para pasárselas a organizador_mover.
  - No la uses cuando: quieres saber de qué trata un documento (usa organizador_leer_documento).

Errores:
  - "Ruta fuera de las raíces permitidas" si la ruta se sale: mira organizador_listar_raices.
  - "no existe la ruta" si la carpeta no está.`,
      inputSchema: {
        ruta: z.string().min(1).describe("Carpeta a inventariar"),
        profundidad: z
          .number()
          .int()
          .min(1)
          .max(20)
          .optional()
          .describe("Niveles a recorrer. 1 = solo el primer nivel"),
        con_huella: z
          .boolean()
          .default(false)
          .describe("Calcular sha256 de cada fichero. Lento; necesario para duplicados"),
        limite: campoLimite,
        desplazamiento: campoDesplazamiento,
        response_format: campoFormato,
      },
      outputSchema: {
        ruta: z.string(),
        total: z.number(),
        cuenta: z.number(),
        desplazamiento: z.number(),
        hay_mas: z.boolean(),
        siguiente_desplazamiento: z.number().optional(),
        bytes_totales: z.number(),
        elementos: z.array(
          z.object({
            ruta: z.string(),
            nombre: z.string(),
            extension: z.string(),
            bytes: z.number(),
            modificado: z.string(),
            sha256: z.string().optional(),
          }),
        ),
      },
      annotations: SOLO_LECTURA,
    },
    async (args) => {
      try {
        const raiz = await resolverSeguro(args.ruta);
        const todos = await recorrer(raiz, { profundidad: args.profundidad });
        const bytesTotales = todos.reduce((s, f) => s + f.bytes, 0);
        const pagina = paginar(todos, args.limite, args.desplazamiento);

        let elementos: FichaFichero[] = pagina.elementos;
        if (args.con_huella) {
          elementos = await Promise.all(
            elementos.map(async (f) => ({
              ...f,
              sha256: await huella(f.ruta).catch(() => undefined),
            })),
          );
        }

        const datos = {
          ruta: raiz,
          total: pagina.total,
          cuenta: pagina.cuenta,
          desplazamiento: pagina.desplazamiento,
          hay_mas: pagina.hay_mas,
          ...(pagina.siguiente_desplazamiento !== undefined
            ? { siguiente_desplazamiento: pagina.siguiente_desplazamiento }
            : {}),
          bytes_totales: bytesTotales,
          elementos,
        };

        if (args.response_format === "json") {
          return respuesta(JSON.stringify(datos, null, 2), datos);
        }

        if (!elementos.length) {
          return respuesta(
            `# ${raiz}\n\nNo hay ficheros que organizar aquí (o todos están protegidos).`,
            datos,
          );
        }

        const lineas = [
          `# Inventario · ${raiz}`,
          "",
          `${pagina.total} ficheros · ${humanizarBytes(bytesTotales)} en total` +
            ` · mostrando ${pagina.cuenta} desde ${pagina.desplazamiento}`,
          "",
          "| Fichero | Tamaño | Modificado |",
          "|---|---|---|",
          ...elementos.map((f) => {
            const rel = path.relative(raiz, f.ruta) || f.nombre;
            return `| \`${rel}\` | ${humanizarBytes(f.bytes)} | ${f.modificado.slice(0, 10)} |`;
          }),
        ];
        if (pagina.hay_mas) {
          lineas.push(
            "",
            `Hay más: repite con \`desplazamiento=${pagina.siguiente_desplazamiento}\`.`,
          );
        }
        return respuesta(lineas.join("\n"), datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );

  // -------------------------------------------------------- leer documento
  servidor.registerTool(
    "organizador_leer_documento",
    {
      title: "Leer el contenido de un documento",
      description: `Extrae el texto de un documento para poder clasificarlo por lo que DICE, no por cómo se llama.

Esta es la herramienta que distingue organizar de adivinar. Un fichero llamado
'document.pdf' no dice nada; su primera página dice que es un informe urbanístico
de un local concreto. Léelo antes de decidir carpeta cuando el nombre sea genérico
(document.pdf, Libro1.xlsx, Untitled, Escaneo_001, IMG_1234, nombres con sólo cifras).

Formatos que lee:
  - Texto directo: .txt .md .csv .tsv .json .xml .yaml .html .log y código
  - PDF: mediante 'pdftotext' (5 primeras páginas). Requiere poppler instalado
  - Office moderno: .docx .xlsx .pptx (descomprime y limpia el XML)
  - Formatos de macOS: .doc .rtf .odt mediante 'textutil'

Args:
  - ruta (string): fichero a leer, dentro de las raíces permitidas
  - limite_caracteres (number): tope de texto devuelto, 200-25000 (por defecto 4000).
      Para clasificar suelen bastar 1500-4000: el encabezado ya delata el documento

Devuelve:
  {
    "ruta": string, "metodo": string,   // cómo se extrajo
    "bytes_original": number,
    "truncado": boolean, "caracteres": number,
    "texto": string
  }

Ejemplos:
  - Úsala cuando: el inventario muestra 'documento (1).pdf' y no sabes qué es.
  - Úsala cuando: dos ficheros tienen nombres parecidos y quieres ver si son lo mismo.
  - No la uses cuando: el nombre ya es inequívoco ('Factura Iberdrola 2024-03.pdf').
  - No la uses cuando: es una imagen o un vídeo: no tienen texto.

Errores:
  - "para leer PDF hace falta pdftotext": instala poppler o clasifica por nombre.
  - "no tiene texto extraíble": suele ser un PDF escaneado, solo imagen.`,
      inputSchema: {
        ruta: z.string().min(1).describe("Fichero cuyo contenido se quiere leer"),
        limite_caracteres: z
          .number()
          .int()
          .min(200)
          .max(25_000)
          .default(4_000)
          .describe("Tope de texto devuelto. 1500-4000 basta para clasificar"),
      },
      outputSchema: {
        ruta: z.string(),
        metodo: z.string(),
        bytes_original: z.number(),
        truncado: z.boolean(),
        caracteres: z.number(),
        texto: z.string(),
      },
      annotations: SOLO_LECTURA,
    },
    async (args) => {
      try {
        const ruta = await resolverSeguro(args.ruta);
        const extraido = await extraerTexto(ruta, args.limite_caracteres);
        const datos = {
          ruta,
          metodo: extraido.metodo,
          bytes_original: extraido.bytesOriginal,
          truncado: extraido.truncado,
          caracteres: extraido.texto.length,
          texto: extraido.texto,
        };
        const cabecera =
          `# ${path.basename(ruta)}\n\n` +
          `Extraído con ${extraido.metodo} · ${humanizarBytes(extraido.bytesOriginal)}` +
          (extraido.truncado ? " · **texto recortado**" : "") +
          "\n\n---\n\n";
        return respuesta(cabecera + extraido.texto, datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );

  // ----------------------------------------------------- buscar duplicados
  servidor.registerTool(
    "organizador_buscar_duplicados",
    {
      title: "Buscar duplicados exactos",
      description: `Agrupa los ficheros idénticos byte a byte bajo una carpeta.

Compara por sha256, no por nombre ni por tamaño: dos ficheros solo salen como
duplicados si su contenido es exactamente el mismo. Ignora los vacíos (0 bytes),
porque todos los ficheros vacíos son idénticos entre sí y eso no significa nada.

NO borra nada. Devuelve los grupos para que decidas, y el borrado lo hace
después organizador_borrar_duplicados, que vuelve a verificar la huella.

Dentro de cada grupo se propone conservar el de ruta más corta y fecha más
antigua (suele ser el original, no la copia).

Args:
  - ruta (string): carpeta donde buscar, dentro de las raíces permitidas
  - limite (number): máximo de grupos a devolver, 1-200 (por defecto 50)
  - desplazamiento (number): cuántos grupos saltar (por defecto 0)
  - response_format ('markdown'|'json'): formato (por defecto 'markdown')

Devuelve:
  {
    "ruta": string,
    "total": number,              // grupos de duplicados encontrados
    "cuenta": number, "desplazamiento": number, "hay_mas": boolean,
    "bytes_recuperables": number, // lo que se liberaría borrando los sobrantes
    "elementos": [{
      "sha256": string, "bytes": number,
      "conservar": string,        // ruta propuesta a mantener
      "sobrantes": string[]       // rutas idénticas a la anterior
    }]
  }

Ejemplos:
  - Úsala cuando: "¿cuánto espacio me sobra en Documentos?"
  - Úsala cuando: antes de fusionar Descargas, para saber qué va a colisionar.
  - No la uses cuando: buscas ficheros parecidos pero no idénticos: esto no los ve.`,
      inputSchema: {
        ruta: z.string().min(1).describe("Carpeta donde buscar duplicados"),
        limite: campoLimite,
        desplazamiento: campoDesplazamiento,
        response_format: campoFormato,
      },
      outputSchema: {
        ruta: z.string(),
        total: z.number(),
        cuenta: z.number(),
        desplazamiento: z.number(),
        hay_mas: z.boolean(),
        siguiente_desplazamiento: z.number().optional(),
        bytes_recuperables: z.number(),
        elementos: z.array(
          z.object({
            sha256: z.string(),
            bytes: z.number(),
            conservar: z.string(),
            sobrantes: z.array(z.string()),
          }),
        ),
      },
      annotations: SOLO_LECTURA,
    },
    async (args) => {
      try {
        const raiz = await resolverSeguro(args.ruta);
        const ficheros = (await recorrer(raiz)).filter((f) => f.bytes > 0);

        const porHuella = new Map<string, FichaFichero[]>();
        for (const f of ficheros) {
          const h = await huella(f.ruta).catch(() => null);
          if (!h) continue;
          const lista = porHuella.get(h);
          if (lista) lista.push(f);
          else porHuella.set(h, [f]);
        }

        const grupos = [...porHuella.entries()]
          .filter(([, lista]) => lista.length > 1)
          .map(([sha256, lista]) => {
            const ordenada = [...lista].sort(
              (a, b) =>
                a.ruta.split(path.sep).length - b.ruta.split(path.sep).length ||
                a.modificado.localeCompare(b.modificado) ||
                a.ruta.localeCompare(b.ruta),
            );
            const [conservar, ...sobrantes] = ordenada;
            return {
              sha256,
              bytes: conservar!.bytes,
              conservar: conservar!.ruta,
              sobrantes: sobrantes.map((f) => f.ruta),
            };
          })
          .sort((a, b) => b.bytes * b.sobrantes.length - a.bytes * a.sobrantes.length);

        const recuperables = grupos.reduce((s, g) => s + g.bytes * g.sobrantes.length, 0);
        const pagina = paginar(grupos, args.limite, args.desplazamiento);
        const datos = {
          ruta: raiz,
          total: pagina.total,
          cuenta: pagina.cuenta,
          desplazamiento: pagina.desplazamiento,
          hay_mas: pagina.hay_mas,
          ...(pagina.siguiente_desplazamiento !== undefined
            ? { siguiente_desplazamiento: pagina.siguiente_desplazamiento }
            : {}),
          bytes_recuperables: recuperables,
          elementos: pagina.elementos,
        };

        if (args.response_format === "json") {
          return respuesta(JSON.stringify(datos, null, 2), datos);
        }
        if (!grupos.length) {
          return respuesta(
            `# Duplicados · ${raiz}\n\nNinguno. Los ${ficheros.length} ficheros con contenido son todos distintos.`,
            datos,
          );
        }
        const lineas = [
          `# Duplicados · ${raiz}`,
          "",
          `${grupos.length} grupos · ${humanizarBytes(recuperables)} recuperables`,
          "",
        ];
        for (const g of pagina.elementos) {
          lineas.push(`### ${path.basename(g.conservar)} · ${humanizarBytes(g.bytes)}`);
          lineas.push(`- **Conservar:** \`${g.conservar}\``);
          for (const s of g.sobrantes) lineas.push(`- Sobra: \`${s}\``);
          lineas.push("");
        }
        return respuesta(lineas.join("\n"), datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );

  // ------------------------------------------------------------- registro
  servidor.registerTool(
    "organizador_ver_registro",
    {
      title: "Ver el registro de operaciones",
      description: `Muestra lo que el servidor ha hecho, de lo más reciente a lo más antiguo.

Cada operación destructiva queda anotada aquí antes de ejecutarse, con su
identificador. Esos identificadores son lo que consume organizador_deshacer.

Args:
  - limite (number): máximo de anotaciones, 1-200 (por defecto 50)
  - desplazamiento (number): cuántas saltar (por defecto 0)
  - solo_reversibles (boolean): solo movimientos aún deshacibles (por defecto false)
  - response_format ('markdown'|'json'): formato (por defecto 'markdown')

Devuelve:
  {
    "base": string, "total": number, "cuenta": number,
    "desplazamiento": number, "hay_mas": boolean,
    "elementos": [{ "id","ts","op","origen","destino"?,"motivo"?,"revertida"? }]
  }

Ejemplos:
  - Úsala cuando: "¿qué has movido?" o "deshaz lo último".
  - Úsala cuando: buscas dónde acabó un fichero tras una pasada.
  - No la uses cuando: quieres ver qué hay en una carpeta (usa organizador_inventariar).`,
      inputSchema: {
        limite: campoLimite,
        desplazamiento: campoDesplazamiento,
        solo_reversibles: z
          .boolean()
          .default(false)
          .describe("Solo movimientos que todavía se pueden deshacer"),
        response_format: campoFormato,
      },
      outputSchema: {
        base: z.string(),
        total: z.number(),
        cuenta: z.number(),
        desplazamiento: z.number(),
        hay_mas: z.boolean(),
        siguiente_desplazamiento: z.number().optional(),
        // Debe reflejar `Anotacion` entera: el SDK valida structuredContent
        // contra este esquema y rechaza cualquier propiedad no declarada.
        elementos: z.array(
          z.object({
            id: z.string(),
            ts: z.string(),
            op: z.string(),
            origen: z.string(),
            destino: z.string().optional(),
            sha256: z.string().optional(),
            bytes: z.number().optional(),
            motivo: z.string().optional(),
            revertida: z.boolean().optional(),
          }),
        ),
      },
      annotations: SOLO_LECTURA,
    },
    async (args) => {
      try {
        const base = await baseDocumentos();
        let anotaciones = (await leerDiario(base)).reverse();
        if (args.solo_reversibles) {
          anotaciones = anotaciones.filter(
            (a) => a.destino && a.op !== "borrar" && !a.revertida,
          );
        }
        const pagina = paginar(anotaciones, args.limite, args.desplazamiento);
        const datos = {
          base,
          total: pagina.total,
          cuenta: pagina.cuenta,
          desplazamiento: pagina.desplazamiento,
          hay_mas: pagina.hay_mas,
          ...(pagina.siguiente_desplazamiento !== undefined
            ? { siguiente_desplazamiento: pagina.siguiente_desplazamiento }
            : {}),
          elementos: pagina.elementos,
        };
        if (args.response_format === "json") {
          return respuesta(JSON.stringify(datos, null, 2), datos);
        }
        if (!pagina.elementos.length) {
          return respuesta("# Registro\n\nNo hay ninguna operación anotada todavía.", datos);
        }
        const lineas = [
          `# Registro · ${base}`,
          "",
          `${pagina.total} operaciones · mostrando ${pagina.cuenta}`,
          "",
          ...pagina.elementos.map((a) => {
            const marca = a.revertida ? " *(revertida)*" : "";
            const flecha = a.destino ? ` → \`${a.destino}\`` : "";
            return `- \`${a.ts.slice(0, 19).replace("T", " ")}\` **${a.op}** \`${a.origen}\`${flecha}${marca}  \n  _${a.id}_`;
          }),
        ];
        return respuesta(lineas.join("\n"), datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );
}
