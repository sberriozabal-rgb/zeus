/**
 * Piezas compartidas por las herramientas: formato de respuesta, paginación,
 * troceado por límite de caracteres y traducción de errores a mensajes útiles.
 */

import { z } from "zod";
import { LIMITE_CARACTERES, TAXONOMIA } from "../constantes.js";
import { RutaNoPermitida } from "../servicios/rutas.js";

export const FORMATOS = ["markdown", "json"] as const;
export type Formato = (typeof FORMATOS)[number];

/** Fragmentos de esquema que se repiten en varias herramientas. */
export const campoFormato = z
  .enum(FORMATOS)
  .default("markdown")
  .describe("Formato de salida: 'markdown' para leerlo, 'json' para procesarlo");

export const campoLimite = z
  .number()
  .int()
  .min(1)
  .max(200)
  .default(50)
  .describe("Número máximo de elementos a devolver (1-200)");

export const campoDesplazamiento = z
  .number()
  .int()
  .min(0)
  .default(0)
  .describe("Cuántos elementos saltar, para paginar");

export const campoCarpeta = z
  .enum(TAXONOMIA)
  .describe(
    "Carpeta de destino dentro de la taxonomía. Usa organizador_listar_raices " +
      "para ver las once con su criterio.",
  );

export interface Pagina<T> {
  total: number;
  cuenta: number;
  desplazamiento: number;
  hay_mas: boolean;
  siguiente_desplazamiento?: number;
  elementos: T[];
}

/** Aplica paginación a una lista ya resuelta. */
export function paginar<T>(todos: T[], limite: number, desplazamiento: number): Pagina<T> {
  const elementos = todos.slice(desplazamiento, desplazamiento + limite);
  const consumidos = desplazamiento + elementos.length;
  const hayMas = consumidos < todos.length;
  return {
    total: todos.length,
    cuenta: elementos.length,
    desplazamiento,
    hay_mas: hayMas,
    ...(hayMas ? { siguiente_desplazamiento: consumidos } : {}),
    elementos,
  };
}

/** Bytes en algo que un humano lee de un vistazo. */
export function humanizarBytes(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  const unidades = ["KB", "MB", "GB", "TB"];
  let valor = bytes / 1024;
  let i = 0;
  while (valor >= 1024 && i < unidades.length - 1) {
    valor /= 1024;
    i++;
  }
  return `${valor.toFixed(valor < 10 ? 1 : 0)} ${unidades[i]}`;
}

/**
 * Respuesta de herramienta.
 *
 * Cuando hay `outputSchema`, el SDK valida `structuredContent`, así que el
 * objeto estructurado y el texto salen siempre del mismo dato.
 */
export function respuesta(texto: string, estructurado: Record<string, unknown>) {
  const recortado =
    texto.length > LIMITE_CARACTERES
      ? texto.slice(0, LIMITE_CARACTERES) +
        `\n\n… respuesta recortada en ${LIMITE_CARACTERES} caracteres. ` +
        "Usa 'limite' y 'desplazamiento' para ver el resto por partes."
      : texto;
  return {
    content: [{ type: "text" as const, text: recortado }],
    structuredContent: estructurado,
  };
}

/** Respuesta de error: explica qué pasó y qué hacer a continuación. */
export function error(mensaje: string) {
  return {
    isError: true,
    content: [{ type: "text" as const, text: mensaje }],
  };
}

/** Traduce una excepción a un mensaje accionable. */
export function explicar(e: unknown): string {
  if (e instanceof RutaNoPermitida) return `Error: ${e.message}`;
  if (e instanceof z.ZodError) {
    const detalles = e.issues.map((i) => `  - ${i.path.join(".") || "(raíz)"}: ${i.message}`);
    return `Error: parámetros inválidos.\n${detalles.join("\n")}`;
  }
  const err = e as NodeJS.ErrnoException;
  switch (err?.code) {
    case "ENOENT":
      return (
        `Error: no existe la ruta (${err.path ?? "?"}). ` +
        "Comprueba con organizador_inventariar que sigue ahí: puede haberse movido en una pasada anterior."
      );
    case "EACCES":
    case "EPERM":
      return (
        `Error: sin permiso sobre ${err.path ?? "la ruta"}. ` +
        "En macOS, concede a tu cliente MCP acceso a Archivos y carpetas en " +
        "Ajustes › Privacidad y seguridad."
      );
    case "ENOSPC":
      return "Error: no queda espacio en el disco. Libera espacio y repite.";
    case "EXDEV":
      return "Error: el origen y el destino están en volúmenes distintos y la copia falló.";
    default:
      return `Error: ${e instanceof Error ? e.message : String(e)}`;
  }
}
