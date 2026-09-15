/**
 * Seguridad de rutas.
 *
 * El servidor solo opera dentro de unas raíces declaradas. Toda ruta que
 * entra por una herramienta pasa por `resolverSeguro`, que la normaliza,
 * resuelve enlaces simbólicos y comprueba que sigue cayendo dentro de una
 * raíz. Sin esto, un `../` en un parámetro llega a cualquier punto del disco.
 */

import * as fs from "node:fs/promises";
import * as os from "node:os";
import * as path from "node:path";

/** Error de ruta fuera de las raíces permitidas. */
export class RutaNoPermitida extends Error {
  constructor(ruta: string, raices: string[]) {
    super(
      `Ruta fuera de las raíces permitidas: ${ruta}\n` +
        `Raíces configuradas: ${raices.join(", ")}\n` +
        `Sugerencia: usa organizador_listar_raices para ver dónde puede trabajar ` +
        `el servidor, o arranca el servidor con ORGANIZADOR_RAICES apuntando a la ` +
        `carpeta que necesitas.`,
    );
    this.name = "RutaNoPermitida";
  }
}

let raicesCache: string[] | null = null;

/** Expande `~` al home del usuario. */
function expandirTilde(p: string): string {
  if (p === "~") return os.homedir();
  if (p.startsWith("~/")) return path.join(os.homedir(), p.slice(2));
  return p;
}

/**
 * Raíces permitidas. Se leen de ORGANIZADOR_RAICES (separadas por `:`).
 * Si no está definida, se usan las carpetas habituales del usuario que existan.
 */
export async function raicesPermitidas(): Promise<string[]> {
  if (raicesCache) return raicesCache;

  const declaradas = process.env.ORGANIZADOR_RAICES;
  const candidatas = declaradas
    ? declaradas.split(":").filter(Boolean).map(expandirTilde)
    : [
        path.join(os.homedir(), "Documentos"),
        path.join(os.homedir(), "Documents"),
        path.join(os.homedir(), "Descargas"),
        path.join(os.homedir(), "Downloads"),
      ];

  const existentes: string[] = [];
  for (const c of candidatas) {
    try {
      const real = await fs.realpath(path.resolve(c));
      const st = await fs.stat(real);
      if (st.isDirectory()) existentes.push(real);
    } catch {
      // Una raíz candidata que no existe simplemente no se ofrece.
    }
  }
  raicesCache = existentes;
  return existentes;
}

/** Solo para pruebas: olvida las raíces memorizadas. */
export function olvidarRaices(): void {
  raicesCache = null;
}

/** ¿`hijo` cae dentro de `padre`? Compara por segmentos, no por prefijo de cadena. */
export function estaDentro(padre: string, hijo: string): boolean {
  const rel = path.relative(padre, hijo);
  return rel === "" || (!rel.startsWith("..") && !path.isAbsolute(rel));
}

/**
 * Resuelve una ruta y garantiza que cae dentro de una raíz permitida.
 *
 * Resuelve enlaces simbólicos del ancestro existente más profundo, de modo que
 * un enlace que apunte fuera de las raíces queda rechazado aunque el nombre
 * parezca inocente.
 */
export async function resolverSeguro(entrada: string): Promise<string> {
  const raices = await raicesPermitidas();
  if (raices.length === 0) {
    throw new Error(
      "No hay ninguna raíz disponible. Este servidor solo funciona en la máquina " +
        "donde viven las carpetas (tu Mac). Comprueba que existe ~/Documentos o " +
        "~/Documents, o define ORGANIZADOR_RAICES.",
    );
  }

  const absoluta = path.resolve(expandirTilde(entrada));

  // Resolver el ancestro existente más profundo, para neutralizar symlinks.
  let existente = absoluta;
  const cola: string[] = [];
  for (;;) {
    try {
      existente = await fs.realpath(existente);
      break;
    } catch {
      const padre = path.dirname(existente);
      if (padre === existente) throw new RutaNoPermitida(entrada, raices);
      cola.unshift(path.basename(existente));
      existente = padre;
    }
  }
  const resuelta = cola.length ? path.join(existente, ...cola) : existente;

  if (!raices.some((r) => estaDentro(r, resuelta))) {
    throw new RutaNoPermitida(entrada, raices);
  }
  return resuelta;
}

/** Devuelve la raíz que contiene la ruta dada. */
export async function raizDe(ruta: string): Promise<string> {
  const raices = await raicesPermitidas();
  const dentro = raices.filter((r) => estaDentro(r, ruta));
  if (dentro.length === 0) throw new RutaNoPermitida(ruta, raices);
  // La más específica, por si una raíz anida dentro de otra.
  return dentro.sort((a, b) => b.length - a.length)[0]!;
}

/**
 * La base de organización: la carpeta de Documentos entre las raíces.
 * Es donde vive la taxonomía y donde aterriza todo lo que se fusiona.
 */
export async function baseDocumentos(): Promise<string> {
  const raices = await raicesPermitidas();
  const docs = raices.find((r) => /Documentos|Documents/i.test(path.basename(r)));
  if (!docs) {
    throw new Error(
      "No encuentro una carpeta de Documentos entre las raíces permitidas " +
        `(${raices.join(", ")}). La taxonomía se construye dentro de Documentos, ` +
        "así que necesito una.",
    );
  }
  return docs;
}

/** La carpeta de Descargas entre las raíces, si la hay. */
export async function baseDescargas(): Promise<string | null> {
  const raices = await raicesPermitidas();
  return raices.find((r) => /Descargas|Downloads/i.test(path.basename(r))) ?? null;
}
