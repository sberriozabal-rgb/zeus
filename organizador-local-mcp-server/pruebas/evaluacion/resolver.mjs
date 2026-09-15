/** Resuelve cada pregunta de la evaluación usando el servidor, y enseña la respuesta. */
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import * as path from "node:path";
import { fileURLToPath } from "node:url";
import { preparar, DOCS, DESC } from "./preparar.mjs";

const aqui = path.dirname(fileURLToPath(import.meta.url));
await preparar();

const cliente = new Client({ name: "eval", version: "1.0.0" });
await cliente.connect(new StdioClientTransport({
  command: "node",
  args: [path.join(aqui, "..", "..", "dist", "index.js")],
  env: { ...process.env, ORGANIZADOR_RAICES: `${DOCS}:${DESC}` },
  stderr: "ignore",
}));
const llamar = async (name, args = {}) => (await cliente.callTool({ name, arguments: args })).structuredContent;
const sinClasificar = path.join(DOCS, "99 · Sin clasificar");

const inv = await llamar("organizador_inventariar", { ruta: sinClasificar, limite: 200 });
const dupsDocs = await llamar("organizador_buscar_duplicados", { ruta: DOCS });
const invDesc = await llamar("organizador_inventariar", { ruta: DESC, limite: 200 });
const leer = async (f) => (await llamar("organizador_leer_documento", { ruta: path.join(sinClasificar, f) })).texto;

const urbanistico = await leer("documento.md");
const fibra = await leer("adjunto-3.txt");
const ventas = await leer("Libro1.csv");
const sanofi = await leer("sin-titulo.txt");

const mayor = inv.elementos.reduce((a, b) => (b.bytes > a.bytes ? b : a));
const fusion = await llamar("organizador_fusionar_descargas", { simulacro: true });

const R = [
  ["1. Expedient del trámite urbanístico", urbanistico.match(/Expedient:\s*(\S+)/)[1]],
  ["2. NIF del alta de fibra", fibra.match(/NIF\/CIF:\s*(\S+)/)[1]],
  ["3. Total facturado en el informe de ventas", ventas.trim().split("\n")[1].split(",")[4]],
  ["4. Comensales de la factura T-4964", sanofi.match(/Comensales:\s*(\d+)/)[1]],
  ["5. Grupos de duplicados exactos en Documentos", String(dupsDocs.total)],
  ["6. Bytes recuperables borrando los sobrantes", String(dupsDocs.bytes_recuperables)],
  ["7. Fichero más grande de 99 · Sin clasificar", mayor.nombre],
  ["8. Dirección citada por dos documentos distintos",
    urbanistico.match(/Passatge de Rates [\d-]+/)[0]],
  ["9. Ficheros que el inventario ve en Descargas (sin protegidos)", String(invDesc.total)],
  ["10. Carpetas protegidas que la fusión no tocaría", String(fusion.protegidos ?? 0)],
];
for (const [p, r] of R) console.log(`${p}\n   → ${r}\n`);

// Comprobaciones de estabilidad: las respuestas no deben depender del orden.
console.log("Duplicados detectados:");
for (const g of dupsDocs.elementos) {
  console.log(`   ${path.basename(g.conservar)} ← ${g.sobrantes.map((s) => path.basename(s)).join(", ")} (${g.bytes} B)`);
}
console.log(`\nInventario de Descargas: ${invDesc.elementos.map((e) => e.nombre).join(", ")}`);
console.log(`Simulacro de fusión: ${fusion.ficheros_movidos} ficheros, ${fusion.carpetas_movidas} carpetas, ${fusion.protegidos} protegidos, ${fusion.incompletas} incompletas`);
await cliente.close();
