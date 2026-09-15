/**
 * Recorrido del disco, huellas y movimientos seguros.
 */

import { createHash } from "node:crypto";
import { createReadStream } from "node:fs";
import * as fs from "node:fs/promises";
import * as path from "node:path";
import {
  CARPETA_SISTEMA,
  DIRECTORIOS_PROTEGIDOS,
  EXTENSIONES_INCOMPLETAS,
  EXTENSIONES_PAQUETE,
  EXTENSIONES_PAQUETE_DOCUMENTO,
  EXTENSIONES_PAQUETE_SISTEMA,
} from "../constantes.js";

export interface FichaFichero {
  ruta: string;
  nombre: string;
  extension: string;
  bytes: number;
  modificado: string;
  /** sha256 completo. Solo se calcula cuando hace falta: es caro. */
  sha256?: string;
}

/** ¿Es un paquete de macOS? Es un directorio, pero se trata como una unidad. */
export function esPaquete(nombre: string): boolean {
  const n = nombre.toLowerCase();
  return EXTENSIONES_PAQUETE.some((e) => n.endsWith(e));
}

/** ¿Es un paquete que el usuario entiende como un documento suyo? */
export function esPaqueteDocumento(nombre: string): boolean {
  const n = nombre.toLowerCase();
  return EXTENSIONES_PAQUETE_DOCUMENTO.some((e) => n.endsWith(e));
}

/** ¿Es una app o una biblioteca? Eso no se clasifica. */
export function esPaqueteSistema(nombre: string): boolean {
  const n = nombre.toLowerCase();
  return EXTENSIONES_PAQUETE_SISTEMA.some((e) => n.endsWith(e));
}

/** ¿Es una descarga a medias? Moverla la rompe. */
export function esIncompleto(nombre: string): boolean {
  const n = nombre.toLowerCase();
  return EXTENSIONES_INCOMPLETAS.some((e) => n.endsWith(e));
}

/** ¿Es un directorio en el que no se entra? */
export function esDirectorioProtegido(nombre: string): boolean {
  return DIRECTORIOS_PROTEGIDOS.has(nombre) || nombre.startsWith(".") || esPaquete(nombre);
}

/** ¿Es un fichero que no se toca? */
export function esFicheroProtegido(nombre: string): boolean {
  return nombre.startsWith(".") || esIncompleto(nombre) || esPaquete(nombre);
}

export interface OpcionesRecorrido {
  /** Profundidad máxima. 1 = solo el primer nivel. Por defecto, sin límite. */
  profundidad?: number;
  /** Rutas absolutas cuyo subárbol se omite entero. */
  omitir?: string[];
}

/**
 * Recorre un directorio devolviendo los ficheros no protegidos.
 *
 * No sigue enlaces simbólicos: un enlace a `/` convertiría el recorrido en
 * un paseo por todo el disco.
 */
export async function recorrer(
  raiz: string,
  opciones: OpcionesRecorrido = {},
): Promise<FichaFichero[]> {
  const { profundidad = Number.POSITIVE_INFINITY, omitir = [] } = opciones;
  const omitirSet = new Set(omitir.map((o) => path.resolve(o)));
  const salida: FichaFichero[] = [];

  async function paso(dir: string, nivel: number): Promise<void> {
    if (nivel > profundidad) return;
    if (omitirSet.has(path.resolve(dir))) return;

    let entradas;
    try {
      entradas = await fs.readdir(dir, { withFileTypes: true });
    } catch {
      return; // Sin permiso o desaparecida: se ignora en silencio.
    }

    for (const e of entradas) {
      const completa = path.join(dir, e.name);
      if (e.isSymbolicLink()) continue;

      if (e.isDirectory()) {
        if (esDirectorioProtegido(e.name)) continue;
        await paso(completa, nivel + 1);
        continue;
      }
      if (!e.isFile()) continue;
      if (esFicheroProtegido(e.name)) continue;

      try {
        const st = await fs.stat(completa);
        salida.push({
          ruta: completa,
          nombre: e.name,
          extension: path.extname(e.name).toLowerCase(),
          bytes: st.size,
          modificado: st.mtime.toISOString(),
        });
      } catch {
        // Desapareció entre readdir y stat.
      }
    }
  }

  await paso(raiz, 1);
  salida.sort((a, b) => a.ruta.localeCompare(b.ruta));
  return salida;
}

/** sha256 de un fichero, por streaming: no carga el fichero en memoria. */
export async function huella(ruta: string): Promise<string> {
  return new Promise((resolver, rechazar) => {
    const hash = createHash("sha256");
    const flujo = createReadStream(ruta);
    flujo.on("error", rechazar);
    flujo.on("data", (trozo) => hash.update(trozo));
    flujo.on("end", () => resolver(hash.digest("hex")));
  });
}

/** ¿Existe? */
export async function existe(ruta: string): Promise<boolean> {
  try {
    await fs.access(ruta);
    return true;
  } catch {
    return false;
  }
}

/**
 * Un destino libre dentro de `directorio` para el nombre dado.
 * Si está ocupado, añade ` · 2`, ` · 3`… antes de la extensión.
 */
export async function destinoLibre(directorio: string, nombre: string): Promise<string> {
  let candidato = path.join(directorio, nombre);
  if (!(await existe(candidato))) return candidato;

  const ext = path.extname(nombre);
  const tronco = ext ? nombre.slice(0, -ext.length) : nombre;
  for (let i = 2; ; i++) {
    candidato = path.join(directorio, `${tronco} · ${i}${ext}`);
    if (!(await existe(candidato))) return candidato;
  }
}

/**
 * Mueve respetando límites de volumen.
 *
 * `fs.rename` falla con EXDEV entre volúmenes distintos (un disco externo, por
 * ejemplo). En ese caso se copia y se borra el origen.
 */
export async function mover(origen: string, destino: string): Promise<void> {
  await fs.mkdir(path.dirname(destino), { recursive: true });
  try {
    await fs.rename(origen, destino);
  } catch (error) {
    const codigo = (error as NodeJS.ErrnoException).code;
    if (codigo !== "EXDEV") throw error;
    await fs.cp(origen, destino, { recursive: true, force: false, errorOnExist: true });
    await fs.rm(origen, { recursive: true, force: true });
  }
}

/** Borra las carpetas vacías bajo `raiz`, en cascada. Nunca borra `raiz`. */
export async function limpiarVacias(raiz: string, proteger: string[] = []): Promise<string[]> {
  const protegidas = new Set([path.resolve(raiz), ...proteger.map((p) => path.resolve(p))]);
  const borradas: string[] = [];

  async function paso(dir: string): Promise<boolean> {
    if (path.basename(dir) === CARPETA_SISTEMA) return false;
    let entradas;
    try {
      entradas = await fs.readdir(dir, { withFileTypes: true });
    } catch {
      return false;
    }
    let vacio = true;
    for (const e of entradas) {
      const completa = path.join(dir, e.name);
      if (e.isDirectory() && !e.isSymbolicLink() && !esPaquete(e.name)) {
        const seFue = await paso(completa);
        if (!seFue) vacio = false;
      } else {
        vacio = false;
      }
    }
    if (vacio && !protegidas.has(path.resolve(dir))) {
      try {
        await fs.rmdir(dir);
        borradas.push(dir);
        return true;
      } catch {
        return false;
      }
    }
    return false;
  }

  await paso(raiz);
  return borradas;
}
