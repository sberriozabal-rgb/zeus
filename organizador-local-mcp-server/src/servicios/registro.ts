/**
 * Registro y vuelta atrás.
 *
 * Dos escrituras por operación:
 *   - LOG.md      — para el humano, en prosa.
 *   - diario.jsonl — para la máquina, una línea por operación, que es lo que
 *                    permite deshacer sin adivinar.
 *
 * La regla de la casa es borrado directo sin cuarentena, así que el diario y
 * el snapshot APFS son toda la red que hay. Por eso se escriben SIEMPRE, y
 * antes de tocar nada.
 */

import { randomUUID } from "node:crypto";
import * as fs from "node:fs/promises";
import * as path from "node:path";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { CARPETA_SISTEMA, FICHERO_DIARIO, FICHERO_LOG } from "../constantes.js";

const ejecutar = promisify(execFile);

export type TipoOperacion = "mover" | "borrar" | "renombrar" | "fusionar" | "deshacer";

export interface Anotacion {
  id: string;
  ts: string;
  op: TipoOperacion;
  origen: string;
  destino?: string;
  sha256?: string;
  bytes?: number;
  motivo?: string;
  /** Marcada cuando un `deshacer` ya revirtió esta operación. */
  revertida?: boolean;
}

/** Ruta de la carpeta de sistema dentro de una base. */
export function carpetaSistema(base: string): string {
  return path.join(base, CARPETA_SISTEMA);
}

async function asegurarSistema(base: string): Promise<string> {
  const dir = carpetaSistema(base);
  await fs.mkdir(dir, { recursive: true });
  return dir;
}

/** Escribe una anotación en los dos ficheros. Devuelve la anotación completa. */
export async function anotar(
  base: string,
  entrada: Omit<Anotacion, "id" | "ts">,
): Promise<Anotacion> {
  const dir = await asegurarSistema(base);
  const anotacion: Anotacion = {
    id: randomUUID(),
    ts: new Date().toISOString(),
    ...entrada,
  };

  await fs.appendFile(
    path.join(dir, FICHERO_DIARIO),
    JSON.stringify(anotacion) + "\n",
    "utf8",
  );

  const sello = anotacion.ts.replace("T", " ").slice(0, 19);
  const cuerpo =
    anotacion.op === "borrar"
      ? `BORRADO · \`${anotacion.origen}\`${anotacion.motivo ? ` · ${anotacion.motivo}` : ""}`
      : `${anotacion.op.toUpperCase()} · \`${anotacion.origen}\` → \`${anotacion.destino}\`` +
        (anotacion.motivo ? ` · ${anotacion.motivo}` : "");
  await fs.appendFile(
    path.join(dir, FICHERO_LOG),
    `- [${sello}] ${cuerpo}\n`,
    "utf8",
  );

  return anotacion;
}

/** Cabecera de sesión en el LOG, para separar pasadas. */
export async function abrirSesion(base: string, titulo: string): Promise<void> {
  const dir = await asegurarSistema(base);
  const sello = new Date().toISOString().replace("T", " ").slice(0, 19);
  await fs.appendFile(
    path.join(dir, FICHERO_LOG),
    `\n### [${sello}] ${titulo}\n\n`,
    "utf8",
  );
}

/** Lee el diario entero. Devuelve [] si aún no existe. */
export async function leerDiario(base: string): Promise<Anotacion[]> {
  try {
    const bruto = await fs.readFile(path.join(carpetaSistema(base), FICHERO_DIARIO), "utf8");
    const salida: Anotacion[] = [];
    for (const linea of bruto.split("\n")) {
      if (!linea.trim()) continue;
      try {
        salida.push(JSON.parse(linea) as Anotacion);
      } catch {
        // Una línea corrupta no invalida el resto del diario.
      }
    }
    return salida;
  } catch {
    return [];
  }
}

/** Reescribe el diario. Se usa para marcar operaciones como revertidas. */
export async function reescribirDiario(base: string, anotaciones: Anotacion[]): Promise<void> {
  const dir = await asegurarSistema(base);
  const cuerpo = anotaciones.map((a) => JSON.stringify(a)).join("\n") + "\n";
  await fs.writeFile(path.join(dir, FICHERO_DIARIO), cuerpo, "utf8");
}

export interface ResultadoSnapshot {
  hecho: boolean;
  detalle: string;
}

/**
 * El intento de esta sesión, con su resultado. Se recuerda tanto el éxito como
 * el fracaso: si Time Machine no está configurado, `tmutil` va a fallar igual
 * la segunda vez y la quinta, y cada intento cuesta hasta un minuto de espera.
 * Un intento por proceso, que es lo que dice la documentación de esta función.
 */
let intento: ResultadoSnapshot | null = null;

/**
 * Snapshot APFS antes de la primera operación destructiva del proceso.
 *
 * Solo existe en macOS. En cualquier otro sitio devuelve el motivo, y quien
 * llama decide: las herramientas lo muestran en la respuesta para que quede
 * claro si hay red de seguridad o no.
 */
export async function snapshotAPFS(): Promise<ResultadoSnapshot> {
  if (intento) {
    return intento.hecho
      ? { hecho: true, detalle: "ya se hizo uno en esta sesión" }
      : intento;
  }
  if (process.platform !== "darwin") {
    intento = { hecho: false, detalle: "no es macOS: no hay snapshot APFS disponible" };
    return intento;
  }
  try {
    const { stdout } = await ejecutar("tmutil", ["localsnapshot"], { timeout: 60_000 });
    intento = { hecho: true, detalle: stdout.trim() || "snapshot creado" };
  } catch (error) {
    intento = {
      hecho: false,
      detalle:
        `no se pudo crear (${error instanceof Error ? error.message : String(error)}). ` +
        "Suele ser que Time Machine no está configurado. No se reintentará en esta sesión.",
    };
  }
  return intento;
}
