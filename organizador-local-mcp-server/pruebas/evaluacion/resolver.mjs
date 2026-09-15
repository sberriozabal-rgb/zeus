/**
 * Resuelve las preguntas de la evaluación contra el servidor real y las
 * contrasta con las respuestas publicadas en evaluacion.xml.
 *
 * Sale con código distinto de cero si alguna deja de coincidir: así, si el
 * fixture o el comportamiento del servidor cambian, la evaluación no se queda
 * publicando respuestas que ya no son ciertas.
 */
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import * as fs from "node:fs/promises";
import * as path from "node:path";
import { fileURLToPath } from "node:url";
import { preparar, DOCS, DESC } from "./preparar.mjs";

const aqui = path.dirname(fileURLToPath(import.meta.url));
await preparar();

const cliente = new Client({ name: "eval", version: "1.0.0" });
await cliente.connect(
  new StdioClientTransport({
    command: "node",
    args: [path.join(aqui, "..", "..", "dist", "index.js")],
    env: { ...process.env, ORGANIZADOR_RAICES: `${DOCS}:${DESC}` },
    stderr: "ignore",
  }),
);

const llamar = async (name, args = {}) =>
  (await cliente.callTool({ name, arguments: args })).structuredContent;
const sinClasificar = path.join(DOCS, "99 · Sin clasificar");
const leer = async (f) =>
  (await llamar("organizador_leer_documento", { ruta: path.join(sinClasificar, f) })).texto;

const inv = await llamar("organizador_inventariar", { ruta: sinClasificar, limite: 200 });
const dups = await llamar("organizador_buscar_duplicados", { ruta: DOCS });
const invDesc = await llamar("organizador_inventariar", { ruta: DESC, limite: 200 });
const fusion = await llamar("organizador_fusionar_descargas", { simulacro: true });

const urbanistico = await leer("documento.md");
const fibra = await leer("adjunto-3.txt");
const ventas = await leer("Libro1.csv");
const sanofi = await leer("sin-titulo.txt");
const mayor = inv.elementos.reduce((a, b) => (b.bytes > a.bytes ? b : a));

/** En el mismo orden que los <qa_pair> de evaluacion.xml. */
const resueltas = [
  urbanistico.match(/Expedient:\s*(\S+)/)[1],
  fibra.match(/NIF\/CIF:\s*(\S+)/)[1],
  ventas.trim().split("\n")[1].split(",")[4],
  sanofi.match(/Comensales:\s*(\d+)/)[1],
  String(dups.total),
  String(dups.bytes_recuperables),
  mayor.nombre,
  urbanistico.match(/Passatge de Rates [\d-]+/)[0],
  String(invDesc.total),
  String(fusion.protegidos),
];

const xml = await fs.readFile(path.join(aqui, "evaluacion.xml"), "utf8");
const publicadas = [...xml.matchAll(/<answer>([\s\S]*?)<\/answer>/g)].map((m) => m[1].trim());
const preguntas = [...xml.matchAll(/<question>([\s\S]*?)<\/question>/g)].map((m) => m[1].trim());

let fallos = 0;
if (publicadas.length !== resueltas.length) {
  console.error(
    `❌ evaluacion.xml tiene ${publicadas.length} respuestas y el resolutor calcula ${resueltas.length}`,
  );
  fallos++;
}

console.log("\nEvaluación · respuesta calcuada contra respuesta publicada\n");
for (let i = 0; i < Math.min(publicadas.length, resueltas.length); i++) {
  const coincide = resueltas[i] === publicadas[i];
  if (!coincide) fallos++;
  console.log(`${coincide ? "✅" : "❌"} ${i + 1}. ${preguntas[i].slice(0, 72)}…`);
  console.log(`      calculada: ${resueltas[i]}`);
  if (!coincide) console.log(`      publicada: ${publicadas[i]}`);
}

await cliente.close();
console.log(
  fallos === 0
    ? "\n🟢 Las 10 respuestas publicadas siguen siendo ciertas\n"
    : `\n🔴 ${fallos} respuestas ya no coinciden con evaluacion.xml\n`,
);
process.exit(fallos === 0 ? 0 : 1);
