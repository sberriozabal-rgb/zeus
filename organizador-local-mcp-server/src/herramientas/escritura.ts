/**
 * Herramientas que modifican el disco.
 *
 * Tres garantías en todas ellas:
 *   1. Snapshot APFS antes de la primera operación destructiva del proceso.
 *   2. Anotación en el diario ANTES de ejecutar, no después.
 *   3. Nada se borra sin volver a verificar el sha256 en el momento del borrado.
 */

import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import * as fs from "node:fs/promises";
import * as path from "node:path";
import { z } from "zod";
import { CARPETA_DESCARGAS, CARPETA_SISTEMA } from "../constantes.js";
import {
  destinoLibre,
  esDirectorioProtegido,
  esFicheroProtegido,
  esPaqueteDocumento,
  esPaqueteSistema,
  existe,
  huella,
  limpiarVacias,
  mover,
} from "../servicios/ficheros.js";
import {
  abrirSesion,
  anotar,
  leerDiario,
  reescribirDiario,
  snapshotAPFS,
} from "../servicios/registro.js";
import { baseDescargas, baseDocumentos, resolverSeguro } from "../servicios/rutas.js";
import {
  campoCarpeta,
  error,
  explicar,
  humanizarBytes,
  respuesta,
} from "./comun.js";

const MODIFICA = {
  readOnlyHint: false,
  destructiveHint: true,
  idempotentHint: false,
  openWorldHint: false,
} as const;

export function registrarEscritura(servidor: McpServer): void {
  // ----------------------------------------------------------------- mover
  servidor.registerTool(
    "organizador_mover",
    {
      title: "Mover y renombrar ficheros a la taxonomía",
      description: `Coloca uno o varios ficheros en su carpeta de la taxonomía, opcionalmente renombrándolos.

Acepta un lote entero: decide primero (leyendo con organizador_leer_documento
lo que haga falta) y aplica todo el plan de una vez. Cada movimiento se anota
en el diario antes de ejecutarse, así que organizador_deshacer puede revertirlo.

Si el destino ya está ocupado por un fichero DISTINTO, no se pisa: el que llega
recibe un sufijo ' · 2'. Si está ocupado por uno IDÉNTICO byte a byte, el
movimiento se omite y se informa, porque mover sobre un gemelo no aporta nada.

Args:
  - movimientos (array, 1-100): cada elemento
      { ruta: string,              // fichero a mover
        carpeta: string,           // una de las once de la taxonomía
        nombre_nuevo?: string,     // renombrado opcional (sin barras)
        subcarpeta?: string,       // p.ej. 'BARRY' dentro de 06 · Clientes
        motivo?: string }          // por qué va ahí; queda en el registro
  - crear_subcarpetas (boolean): crear la subcarpeta si no existe (por defecto true)

Devuelve:
  {
    "base": string, "snapshot": string,
    "movidos": number, "omitidos": number, "fallidos": number,
    "resultados": [{ "origen","destino"?,"estado","detalle"?,"id"? }]
  }
  estado es 'movido' | 'omitido' | 'fallido'.

Ejemplos:
  - Úsala cuando: ya sabes dónde va cada cosa y quieres aplicarlo de una pasada.
  - Úsala cuando: quieres renombrar 'document.pdf' a algo que se pueda buscar.
  - No la uses cuando: aún no has mirado el contenido y el nombre es genérico.
  - No la uses cuando: quieres eliminar copias (usa organizador_borrar_duplicados).

Errores:
  - "Ruta fuera de las raíces permitidas": mira organizador_listar_raices.
  - Un elemento que falle no aborta el lote: sale como 'fallido' con su motivo.`,
      inputSchema: {
        movimientos: z
          .array(
            z.object({
              ruta: z.string().min(1).describe("Fichero a mover"),
              carpeta: campoCarpeta,
              nombre_nuevo: z
                .string()
                .min(1)
                .max(255)
                .refine((n) => !n.includes("/") && !n.includes("\\") && n !== "." && n !== "..", {
                  message: "El nombre no puede contener barras ni ser '.' o '..'",
                })
                .optional()
                .describe("Nombre nuevo, si procede renombrar"),
              subcarpeta: z
                .string()
                .max(255)
                .refine((s) => !s.includes("..") && !path.isAbsolute(s), {
                  message: "La subcarpeta debe ser relativa y sin '..'",
                })
                .optional()
                .describe("Subcarpeta dentro de la carpeta de destino, p.ej. 'BARRY'"),
              motivo: z
                .string()
                .max(500)
                .optional()
                .describe("Por qué va ahí. Queda escrito en el registro"),
            }),
          )
          .min(1)
          .max(100)
          .describe("Lote de movimientos a aplicar"),
        crear_subcarpetas: z
          .boolean()
          .default(true)
          .describe("Crear la subcarpeta de destino si no existe"),
      },
      outputSchema: {
        base: z.string(),
        snapshot: z.string(),
        movidos: z.number(),
        omitidos: z.number(),
        fallidos: z.number(),
        resultados: z.array(
          z.object({
            origen: z.string(),
            destino: z.string().optional(),
            estado: z.enum(["movido", "omitido", "fallido"]),
            detalle: z.string().optional(),
            id: z.string().optional(),
          }),
        ),
      },
      annotations: MODIFICA,
    },
    async (args) => {
      try {
        const base = await baseDocumentos();
        const snap = await snapshotAPFS();
        await abrirSesion(base, `organizador_mover · ${args.movimientos.length} movimientos`);

        const resultados: Array<{
          origen: string;
          destino?: string;
          estado: "movido" | "omitido" | "fallido";
          detalle?: string;
          id?: string;
        }> = [];

        for (const m of args.movimientos) {
          try {
            const origen = await resolverSeguro(m.ruta);
            const st = await fs.stat(origen);
            if (!st.isFile()) {
              resultados.push({
                origen,
                estado: "fallido",
                detalle: "no es un fichero (las carpetas no se clasifican)",
              });
              continue;
            }
            if (esFicheroProtegido(path.basename(origen))) {
              resultados.push({
                origen,
                estado: "omitido",
                detalle: "protegido: oculto, descarga a medias o paquete de macOS",
              });
              continue;
            }

            const directorio = m.subcarpeta
              ? path.join(base, m.carpeta, m.subcarpeta)
              : path.join(base, m.carpeta);
            if (args.crear_subcarpetas) await fs.mkdir(directorio, { recursive: true });
            else if (!(await existe(directorio))) {
              resultados.push({
                origen,
                estado: "fallido",
                detalle: `no existe ${directorio} y crear_subcarpetas es false`,
              });
              continue;
            }

            const nombre = m.nombre_nuevo ?? path.basename(origen);
            const deseado = path.join(directorio, nombre);

            if (path.resolve(deseado) === path.resolve(origen)) {
              resultados.push({ origen, estado: "omitido", detalle: "ya está en su sitio" });
              continue;
            }
            if (await existe(deseado)) {
              const [a, b] = await Promise.all([huella(origen), huella(deseado)]);
              if (a === b) {
                resultados.push({
                  origen,
                  destino: deseado,
                  estado: "omitido",
                  detalle: "en el destino ya hay un fichero idéntico byte a byte",
                });
                continue;
              }
            }

            const destino = await destinoLibre(directorio, nombre);
            const anotacion = await anotar(base, {
              op: m.nombre_nuevo ? "renombrar" : "mover",
              origen,
              destino,
              bytes: st.size,
              motivo: m.motivo,
            });
            await mover(origen, destino);
            resultados.push({ origen, destino, estado: "movido", id: anotacion.id });
          } catch (e) {
            resultados.push({ origen: m.ruta, estado: "fallido", detalle: explicar(e) });
          }
        }

        const movidos = resultados.filter((r) => r.estado === "movido").length;
        const omitidos = resultados.filter((r) => r.estado === "omitido").length;
        const fallidos = resultados.filter((r) => r.estado === "fallido").length;
        const datos = {
          base,
          snapshot: snap.hecho ? `sí · ${snap.detalle}` : `no · ${snap.detalle}`,
          movidos,
          omitidos,
          fallidos,
          resultados,
        };

        const lineas = [
          `# Movimientos aplicados`,
          "",
          `**${movidos} movidos** · ${omitidos} omitidos · ${fallidos} fallidos`,
          `Snapshot APFS: ${datos.snapshot}`,
          "",
          ...resultados.map((r) => {
            const icono = r.estado === "movido" ? "✅" : r.estado === "omitido" ? "➖" : "❌";
            const destino = r.destino ? ` → \`${path.relative(base, r.destino)}\`` : "";
            const detalle = r.detalle ? ` — ${r.detalle}` : "";
            return `${icono} \`${path.basename(r.origen)}\`${destino}${detalle}`;
          }),
        ];
        return respuesta(lineas.join("\n"), datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );

  // ----------------------------------------------------- borrar duplicados
  servidor.registerTool(
    "organizador_borrar_duplicados",
    {
      title: "Borrar duplicados verificando la huella",
      description: `Borra ficheros SOLO si son idénticos byte a byte a un original que se conserva.

El borrado es directo, sin papelera ni cuarentena. La única red es el snapshot
APFS previo (unas 24 h) y el registro. Por eso esta herramienta vuelve a calcular
el sha256 de los dos ficheros en el momento del borrado: si el contenido cambió
desde que lo miraste con organizador_buscar_duplicados, NO borra y te lo dice.

Nunca borra el fichero indicado en 'conservar'. Nunca borra ficheros vacíos.

Args:
  - grupos (array, 1-100): cada elemento
      { conservar: string,      // el que se queda
        sobrantes: string[] }   // los que se borran si coinciden con el anterior
  - motivo (string, opcional): queda escrito en el registro

Devuelve:
  {
    "base": string, "snapshot": string,
    "borrados": number, "omitidos": number, "bytes_liberados": number,
    "resultados": [{ "ruta","estado","detalle"?,"bytes"? }]
  }
  estado es 'borrado' | 'omitido'.

Ejemplos:
  - Úsala cuando: organizador_buscar_duplicados te dio los grupos y los has revisado.
  - No la uses cuando: no has verificado que el 'conservar' es el que quieres guardar.
  - No la uses cuando: los ficheros son parecidos pero no idénticos: se omitirán todos.

Errores:
  - "la huella no coincide": el fichero cambió; vuelve a buscar duplicados.
  - Un sobrante que ya no exista sale como 'omitido', no como fallo.`,
      inputSchema: {
        grupos: z
          .array(
            z.object({
              conservar: z.string().min(1).describe("Fichero que NO se borra"),
              sobrantes: z
                .array(z.string().min(1))
                .min(1)
                .max(100)
                .describe("Ficheros a borrar si coinciden con 'conservar'"),
            }),
          )
          .min(1)
          .max(100)
          .describe("Grupos de duplicados a resolver"),
        motivo: z.string().max(500).optional().describe("Anotación para el registro"),
      },
      outputSchema: {
        base: z.string(),
        snapshot: z.string(),
        borrados: z.number(),
        omitidos: z.number(),
        bytes_liberados: z.number(),
        resultados: z.array(
          z.object({
            ruta: z.string(),
            estado: z.enum(["borrado", "omitido"]),
            detalle: z.string().optional(),
            bytes: z.number().optional(),
          }),
        ),
      },
      annotations: MODIFICA,
    },
    async (args) => {
      try {
        const base = await baseDocumentos();
        const snap = await snapshotAPFS();
        await abrirSesion(base, `organizador_borrar_duplicados · ${args.grupos.length} grupos`);

        const resultados: Array<{
          ruta: string;
          estado: "borrado" | "omitido";
          detalle?: string;
          bytes?: number;
        }> = [];
        let liberados = 0;

        for (const g of args.grupos) {
          let conservar: string;
          let huellaConservar: string;
          try {
            conservar = await resolverSeguro(g.conservar);
            const st = await fs.stat(conservar);
            if (!st.isFile() || st.size === 0) {
              for (const s of g.sobrantes) {
                resultados.push({
                  ruta: s,
                  estado: "omitido",
                  detalle: "el fichero a conservar no es un fichero con contenido",
                });
              }
              continue;
            }
            huellaConservar = await huella(conservar);
          } catch (e) {
            for (const s of g.sobrantes) {
              resultados.push({ ruta: s, estado: "omitido", detalle: explicar(e) });
            }
            continue;
          }

          for (const sobrante of g.sobrantes) {
            try {
              const ruta = await resolverSeguro(sobrante);
              if (path.resolve(ruta) === path.resolve(conservar)) {
                resultados.push({
                  ruta,
                  estado: "omitido",
                  detalle: "es el mismo fichero que se quiere conservar",
                });
                continue;
              }
              const st = await fs.stat(ruta);
              if (!st.isFile() || st.size === 0) {
                resultados.push({
                  ruta,
                  estado: "omitido",
                  detalle: "no es un fichero con contenido",
                });
                continue;
              }
              const h = await huella(ruta);
              if (h !== huellaConservar) {
                resultados.push({
                  ruta,
                  estado: "omitido",
                  detalle:
                    "la huella no coincide con la del fichero a conservar: NO es un duplicado exacto",
                });
                continue;
              }
              await anotar(base, {
                op: "borrar",
                origen: ruta,
                sha256: h,
                bytes: st.size,
                motivo: args.motivo ?? `duplicado exacto de ${conservar}`,
              });
              await fs.rm(ruta, { force: true });
              liberados += st.size;
              resultados.push({ ruta, estado: "borrado", bytes: st.size });
            } catch (e) {
              resultados.push({ ruta: sobrante, estado: "omitido", detalle: explicar(e) });
            }
          }
        }

        const borrados = resultados.filter((r) => r.estado === "borrado").length;
        const omitidos = resultados.filter((r) => r.estado === "omitido").length;
        const datos = {
          base,
          snapshot: snap.hecho ? `sí · ${snap.detalle}` : `no · ${snap.detalle}`,
          borrados,
          omitidos,
          bytes_liberados: liberados,
          resultados,
        };
        const lineas = [
          "# Duplicados borrados",
          "",
          `**${borrados} borrados** · ${humanizarBytes(liberados)} liberados · ${omitidos} omitidos`,
          `Snapshot APFS: ${datos.snapshot}`,
          "",
          ...resultados.map((r) =>
            r.estado === "borrado"
              ? `🗑️ \`${r.ruta}\` (${humanizarBytes(r.bytes ?? 0)})`
              : `➖ \`${r.ruta}\` — ${r.detalle}`,
          ),
        ];
        if (!snap.hecho) {
          lineas.push(
            "",
            "> **Sin snapshot APFS.** El borrado fue directo y no hay vuelta atrás " +
              "salvo tu respaldo habitual. Lo borrado queda listado en el registro.",
          );
        }
        return respuesta(lineas.join("\n"), datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );

  // ------------------------------------------------- fusionar descargas
  servidor.registerTool(
    "organizador_fusionar_descargas",
    {
      title: "Fusionar Descargas dentro de Documentos",
      description: `Vacía ~/Descargas dentro de ~/Documentos para que todo viva en un solo sitio.

Cómo reparte:
  - Ficheros sueltos → '99 · Sin clasificar', listos para que los clasifiques
    con organizador_leer_documento + organizador_mover.
  - Carpetas → '${CARPETA_DESCARGAS}', INTACTAS y sin aplanar. Un proyecto
    descomprimido pierde el sentido si le desmontas la estructura.
  - Descargas a medias (.download, .crdownload, .part, .aria2) → se quedan
    donde están: moverlas rompe la descarga en curso.
  - node_modules, Library, .git y paquetes de aplicación (.app, .framework,
    fototecas…) → se quedan donde están: no son documentos tuyos.
  - Paquetes-documento de macOS (.pages, .key, .numbers, .rtfd) → sí se mueven,
    enteros y sin abrirlos.

No borra ~/Descargas: el Dock la necesita. Solo queda vacía.
No borra duplicados: para eso están buscar_duplicados y borrar_duplicados después.
Las colisiones de nombre se resuelven con sufijo ' · 2', nunca pisando.

Args:
  - incluir_carpetas (boolean): mover también las carpetas (por defecto true)
  - simulacro (boolean): no toca nada, solo informa de lo que haría (por defecto false)

Devuelve:
  {
    "origen": string, "destino": string, "snapshot": string, "simulacro": boolean,
    "ficheros_movidos": number, "carpetas_movidas": number,
    "incompletas": number, "protegidos": number,
    "resultados": [{ "origen","destino","tipo","estado","motivo"? }]
  }

Ejemplos:
  - Úsala cuando: "junta Descargas con Documentos y organízalo".
  - Úsala con simulacro=true cuando: quieres ver el alcance antes de ejecutar.
  - No la uses cuando: hay una descarga grande en curso: espera a que termine.`,
      inputSchema: {
        incluir_carpetas: z
          .boolean()
          .default(true)
          .describe("Mover también las carpetas del primer nivel"),
        simulacro: z
          .boolean()
          .default(false)
          .describe("No tocar nada: solo informar de lo que se haría"),
      },
      outputSchema: {
        origen: z.string(),
        destino: z.string(),
        snapshot: z.string(),
        simulacro: z.boolean(),
        ficheros_movidos: z.number(),
        carpetas_movidas: z.number(),
        incompletas: z.number(),
        protegidos: z.number(),
        resultados: z.array(
          z.object({
            origen: z.string(),
            destino: z.string(),
            tipo: z.enum(["fichero", "carpeta"]),
            estado: z.enum(["movido", "simulado", "omitido"]),
            motivo: z.string().optional(),
          }),
        ),
      },
      annotations: { ...MODIFICA, idempotentHint: true },
    },
    async (args) => {
      try {
        const base = await baseDocumentos();
        const descargas = await baseDescargas();
        if (!descargas) {
          return error(
            "Error: no encuentro ~/Descargas ni ~/Downloads entre las raíces permitidas. " +
              "Mira organizador_listar_raices, o arranca el servidor con ORGANIZADOR_RAICES " +
              "incluyendo la carpeta de descargas.",
          );
        }

        const snap = args.simulacro
          ? { hecho: false, detalle: "simulacro: no se tocó nada" }
          : await snapshotAPFS();
        if (!args.simulacro) {
          await abrirSesion(base, `organizador_fusionar_descargas · desde ${descargas}`);
        }

        const destinoSueltos = path.join(base, "99 · Sin clasificar");
        const destinoCarpetas = path.join(base, CARPETA_DESCARGAS);
        if (!args.simulacro) {
          await fs.mkdir(destinoSueltos, { recursive: true });
          if (args.incluir_carpetas) await fs.mkdir(destinoCarpetas, { recursive: true });
        }

        const resultados: Array<{
          origen: string;
          destino: string;
          tipo: "fichero" | "carpeta";
          estado: "movido" | "simulado" | "omitido";
          motivo?: string;
        }> = [];
        let incompletas = 0;
        let protegidos = 0;

        const entradas = await fs.readdir(descargas, { withFileTypes: true });
        for (const e of entradas) {
          const origen = path.join(descargas, e.name);
          if (e.name.startsWith(".") || e.isSymbolicLink()) continue;

          // Un .pages es un directorio, pero es un documento: se mueve entero.
          // Un node_modules o un .app, no: se quedan donde están.
          const esDirectorio = e.isDirectory();
          const esDocumentoEmpaquetado = esDirectorio && esPaqueteDocumento(e.name);
          const esCarpetaReal = esDirectorio && !esPaqueteDocumento(e.name) && !esPaqueteSistema(e.name);

          if (esDirectorio && !esDocumentoEmpaquetado) {
            if (esPaqueteSistema(e.name) || esDirectorioProtegido(e.name)) {
              protegidos++;
              resultados.push({
                origen,
                destino: origen,
                tipo: "carpeta",
                estado: "omitido",
                motivo: esPaqueteSistema(e.name)
                  ? "aplicación o biblioteca de macOS: no es un documento"
                  : "directorio protegido (node_modules, Library, .git…)",
              });
              continue;
            }
            if (!args.incluir_carpetas) continue;
          }

          if (!esDirectorio && esFicheroProtegido(e.name)) {
            incompletas++;
            resultados.push({
              origen,
              destino: origen,
              tipo: "fichero",
              estado: "omitido",
              motivo: "descarga a medias: moverla la rompería",
            });
            continue;
          }

          const carpetaDestino = esCarpetaReal ? destinoCarpetas : destinoSueltos;
          const destino = args.simulacro
            ? path.join(carpetaDestino, e.name)
            : await destinoLibre(carpetaDestino, e.name);

          if (args.simulacro) {
            resultados.push({
              origen,
              destino,
              tipo: esCarpetaReal ? "carpeta" : "fichero",
              estado: "simulado",
            });
            continue;
          }

          await anotar(base, {
            op: "fusionar",
            origen,
            destino,
            motivo: esCarpetaReal ? "carpeta de Descargas, movida intacta" : "fichero de Descargas",
          });
          await mover(origen, destino);
          resultados.push({
            origen,
            destino,
            tipo: esCarpetaReal ? "carpeta" : "fichero",
            estado: "movido",
          });
        }

        if (!args.simulacro) {
          await limpiarVacias(descargas, [descargas]);
        }

        const ficheros = resultados.filter(
          (r) => r.tipo === "fichero" && r.estado !== "omitido",
        ).length;
        const carpetas = resultados.filter(
          (r) => r.tipo === "carpeta" && r.estado !== "omitido",
        ).length;
        const datos = {
          origen: descargas,
          destino: base,
          snapshot: snap.hecho ? `sí · ${snap.detalle}` : `no · ${snap.detalle}`,
          simulacro: args.simulacro,
          ficheros_movidos: ficheros,
          carpetas_movidas: carpetas,
          incompletas,
          protegidos,
          resultados,
        };

        const verbo = args.simulacro ? "se moverían" : "movidos";
        const lineas = [
          args.simulacro ? "# Fusión de Descargas (simulacro)" : "# Descargas fusionadas",
          "",
          `De \`${descargas}\` → \`${base}\``,
          "",
          `**${ficheros} ficheros** ${verbo} a \`99 · Sin clasificar\``,
          `**${carpetas} carpetas** ${verbo} intactas a \`${CARPETA_DESCARGAS}\``,
          `${incompletas} descargas a medias respetadas en su sitio`,
          `${protegidos} carpetas protegidas no tocadas (node_modules, apps…)`,
          `Snapshot APFS: ${datos.snapshot}`,
          "",
          ...resultados.slice(0, 60).map((r) => {
            const icono = r.estado === "omitido" ? "➖" : r.tipo === "carpeta" ? "📁" : "📄";
            return `${icono} \`${path.basename(r.origen)}\`` +
              (r.motivo ? ` — ${r.motivo}` : "");
          }),
        ];
        if (resultados.length > 60) {
          lineas.push("", `… y ${resultados.length - 60} más. Mira organizador_ver_registro.`);
        }
        if (!args.simulacro && ficheros > 0) {
          lineas.push(
            "",
            "**Siguiente paso:** inventaría `99 · Sin clasificar`, lee con " +
              "`organizador_leer_documento` lo que tenga nombre genérico, y aplica " +
              "`organizador_mover` con el plan completo.",
          );
        }
        return respuesta(lineas.join("\n"), datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );

  // -------------------------------------------------------------- deshacer
  servidor.registerTool(
    "organizador_deshacer",
    {
      title: "Deshacer movimientos del registro",
      description: `Devuelve a su sitio original los ficheros movidos, leyendo el diario de operaciones.

Revierte de lo más reciente a lo más antiguo, que es el único orden en que
deshacer una cadena de movimientos tiene sentido.

LO BORRADO NO SE PUEDE DESHACER desde aquí: el borrado es directo y sin
cuarentena. Para recuperar algo borrado, entra en Time Machine sobre la carpeta
afectada dentro de las ~24 h del snapshot APFS. Esta herramienta te dirá
exactamente qué operaciones eran borrados irrecuperables.

Si el origen volvió a estar ocupado por otro fichero, no lo pisa: devuelve el
fichero con sufijo ' · 2' y lo informa.

Args:
  - ids (string[], opcional): identificadores concretos de organizador_ver_registro.
      Si se omite, se deshacen las 'ultimas' operaciones reversibles
  - ultimas (number): cuántas deshacer si no das ids, 1-100 (por defecto 10)

Devuelve:
  {
    "base": string,
    "revertidos": number, "irrecuperables": number, "fallidos": number,
    "resultados": [{ "id","origen","destino"?,"estado","detalle"? }]
  }
  estado es 'revertido' | 'irrecuperable' | 'fallido' | 'ya_revertida'.

Ejemplos:
  - Úsala cuando: "deshaz lo último, lo has clasificado mal".
  - Úsala cuando: quieres revertir solo dos movimientos concretos, dando sus ids.
  - No la uses cuando: quieres recuperar algo borrado: ve a Time Machine.`,
      inputSchema: {
        ids: z
          .array(z.string().min(1))
          .max(100)
          .optional()
          .describe("Ids concretos a revertir; si se omite, se usan las últimas"),
        ultimas: z
          .number()
          .int()
          .min(1)
          .max(100)
          .default(10)
          .describe("Cuántas operaciones reversibles deshacer si no se dan ids"),
      },
      outputSchema: {
        base: z.string(),
        revertidos: z.number(),
        irrecuperables: z.number(),
        fallidos: z.number(),
        resultados: z.array(
          z.object({
            id: z.string(),
            origen: z.string(),
            destino: z.string().optional(),
            estado: z.enum(["revertido", "irrecuperable", "fallido", "ya_revertida"]),
            detalle: z.string().optional(),
          }),
        ),
      },
      annotations: { ...MODIFICA, destructiveHint: false },
    },
    async (args) => {
      try {
        const base = await baseDocumentos();
        const diario = await leerDiario(base);
        if (!diario.length) {
          return error(
            "Error: no hay ninguna operación anotada todavía, así que no hay nada que deshacer.",
          );
        }

        const porId = new Map(diario.map((a) => [a.id, a]));
        const elegidas = args.ids
          ? args.ids.map((id) => porId.get(id)).filter((a): a is NonNullable<typeof a> => !!a)
          : [...diario].reverse().filter((a) => !a.revertida).slice(0, args.ultimas);

        if (!elegidas.length) {
          return error(
            "Error: ninguna de esas operaciones está en el registro. " +
              "Usa organizador_ver_registro para ver los identificadores válidos.",
          );
        }

        await abrirSesion(base, `organizador_deshacer · ${elegidas.length} operaciones`);

        const resultados: Array<{
          id: string;
          origen: string;
          destino?: string;
          estado: "revertido" | "irrecuperable" | "fallido" | "ya_revertida";
          detalle?: string;
        }> = [];
        const revertidas = new Set<string>();

        // De lo más reciente a lo más antiguo: es el único orden sensato.
        for (const a of [...elegidas].sort((x, y) => y.ts.localeCompare(x.ts))) {
          if (a.revertida) {
            resultados.push({
              id: a.id,
              origen: a.origen,
              estado: "ya_revertida",
              detalle: "esta operación ya se deshizo antes",
            });
            continue;
          }
          if (a.op === "borrar" || !a.destino) {
            resultados.push({
              id: a.id,
              origen: a.origen,
              estado: "irrecuperable",
              detalle:
                "fue un borrado directo. Recupéralo desde Time Machine sobre la carpeta " +
                `\`${path.dirname(a.origen)}\` (snapshot APFS, ~24 h)`,
            });
            continue;
          }
          try {
            const actual = await resolverSeguro(a.destino);
            if (!(await existe(actual))) {
              resultados.push({
                id: a.id,
                origen: a.origen,
                destino: a.destino,
                estado: "fallido",
                detalle: "el fichero ya no está en el destino: se movió o se borró después",
              });
              continue;
            }
            const vuelta = await destinoLibre(path.dirname(a.origen), path.basename(a.origen));
            await mover(actual, vuelta);
            await anotar(base, {
              op: "deshacer",
              origen: actual,
              destino: vuelta,
              motivo: `revierte ${a.id}`,
            });
            revertidas.add(a.id);
            resultados.push({
              id: a.id,
              origen: vuelta,
              destino: a.destino,
              estado: "revertido",
              ...(vuelta !== a.origen
                ? { detalle: "el sitio original estaba ocupado: vuelve con sufijo" }
                : {}),
            });
          } catch (e) {
            resultados.push({
              id: a.id,
              origen: a.origen,
              destino: a.destino,
              estado: "fallido",
              detalle: explicar(e),
            });
          }
        }

        if (revertidas.size) {
          await reescribirDiario(
            base,
            diario.map((a) => (revertidas.has(a.id) ? { ...a, revertida: true } : a)),
          );
        }

        const revertidos = resultados.filter((r) => r.estado === "revertido").length;
        const irrecuperables = resultados.filter((r) => r.estado === "irrecuperable").length;
        const fallidos = resultados.filter((r) => r.estado === "fallido").length;
        const datos = { base, revertidos, irrecuperables, fallidos, resultados };

        const lineas = [
          "# Deshacer",
          "",
          `**${revertidos} revertidos** · ${irrecuperables} irrecuperables · ${fallidos} fallidos`,
          "",
          ...resultados.map((r) => {
            const icono =
              r.estado === "revertido"
                ? "↩️"
                : r.estado === "irrecuperable"
                  ? "🚫"
                  : r.estado === "ya_revertida"
                    ? "➖"
                    : "❌";
            return `${icono} \`${path.basename(r.origen)}\`` + (r.detalle ? ` — ${r.detalle}` : "");
          }),
        ];
        return respuesta(lineas.join("\n"), datos);
      } catch (e) {
        return error(explicar(e));
      }
    },
  );
}

// Reexportado para que index.ts pueda anunciar la carpeta de sistema.
export { CARPETA_SISTEMA };
