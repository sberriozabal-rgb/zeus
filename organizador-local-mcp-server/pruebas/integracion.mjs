/**
 * Prueba de integración: arranca el servidor por stdio y lo conduce con el
 * cliente MCP real, como haría Claude Desktop.
 */
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import * as path from "node:path";
import { fileURLToPath } from "node:url";
import { crearFixture, arbol } from "./fixture.mjs";

const aqui = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.join(aqui, ".arenero", "mac");

let fallos = 0;
const ok = (c, m) => { console.log(`${c ? "  ✅" : "  ❌"} ${m}`); if (!c) fallos++; };
const datos = (r) => r.structuredContent;
const texto = (r) => r.content?.map((c) => c.text).join("\n") ?? "";

const { docs, desc } = await crearFixture(RAIZ);

const transporte = new StdioClientTransport({
  command: "node",
  args: [path.join(aqui, "..", "dist", "index.js")],
  env: { ...process.env, ORGANIZADOR_RAICES: `${docs}:${desc}` },
  stderr: "ignore",
});
const cliente = new Client({ name: "prueba", version: "1.0.0" });
await cliente.connect(transporte);

console.log("\n── Herramientas expuestas");
const { tools } = await cliente.listTools();
ok(tools.length === 9, `9 herramientas registradas (hay ${tools.length})`);
ok(tools.every((t) => t.description && t.description.length > 200), "todas con descripción extensa");
ok(tools.every((t) => t.annotations), "todas con anotaciones");
ok(tools.every((t) => t.name.startsWith("organizador_")), "todas con prefijo de servicio");
const soloLectura = tools.filter((t) => t.annotations?.readOnlyHint).map((t) => t.name);
ok(soloLectura.length === 5, `5 de solo lectura (hay ${soloLectura.length})`);

console.log("\n── Raíces");
let r = await cliente.callTool({ name: "organizador_listar_raices", arguments: {} });
ok(datos(r).raices.length === 2, "dos raíces declaradas");
ok(datos(r).taxonomia.length === 11, "once carpetas en la taxonomía");
ok(datos(r).base_documentos === docs, "base de Documentos correcta");

console.log("\n── Seguridad de rutas");
r = await cliente.callTool({ name: "organizador_inventariar", arguments: { ruta: "/etc" } });
ok(r.isError === true, "rechaza una ruta fuera de las raíces");
r = await cliente.callTool({ name: "organizador_inventariar", arguments: { ruta: `${desc}/../../../etc` } });
ok(r.isError === true, "rechaza el escape por '..'");
ok(texto(r).includes("organizador_listar_raices"), "el error sugiere qué hacer");

console.log("\n── Inventario");
r = await cliente.callTool({ name: "organizador_inventariar", arguments: { ruta: desc } });
const nombres = datos(r).elementos.map((e) => e.nombre);
ok(!nombres.includes("pelicula.mp4.download"), "omite la descarga a medias");
ok(!nombres.some((n) => n === "index.js"), "no entra en node_modules");
ok(nombres.includes("README.md"), "sí recorre carpetas normales");

console.log("\n── Lectura de contenido");
r = await cliente.callTool({ name: "organizador_leer_documento", arguments: { ruta: path.join(desc, "documento.md") } });
ok(datos(r).texto.includes("Passatge de Rates"), "extrae el texto del documento");
r = await cliente.callTool({ name: "organizador_leer_documento", arguments: { ruta: path.join(desc, "captura.png") } });
ok(r.isError === true && texto(r).includes("No sé extraer"), "explica que no sabe leer un .png");

console.log("\n── Fusión de Descargas (simulacro)");
r = await cliente.callTool({ name: "organizador_fusionar_descargas", arguments: { simulacro: true } });
ok(datos(r).simulacro === true, "marca que fue simulacro");
const antesFusion = (await arbol(desc)).length;
ok(antesFusion === 11, `el simulacro no movió nada (${antesFusion} ficheros siguen en Descargas)`);

console.log("\n── Fusión de Descargas (real)");
r = await cliente.callTool({ name: "organizador_fusionar_descargas", arguments: {} });
ok(datos(r).carpetas_movidas === 1, `1 carpeta movida intacta (${datos(r).carpetas_movidas})`);
ok(datos(r).protegidos === 2, `2 protegidos no tocados: node_modules e Instalador.app (${datos(r).protegidos})`);
ok(datos(r).ficheros_movidos === 6, `6 sueltos, contando Propuesta.pages entera (${datos(r).ficheros_movidos})`);
ok(datos(r).incompletas === 1, "1 descarga a medias respetada");
const restanteDesc = await arbol(desc);
ok(restanteDesc.includes("pelicula.mp4.download"), "la descarga a medias sigue en Descargas");
ok(restanteDesc.some((f) => f.includes("node_modules")), "node_modules no se tocó");
ok(restanteDesc.some((f) => f.includes("Instalador.app")), "la app no se movió");
const tras = await arbol(docs);
ok(tras.some((f) => f.includes("Carpetas de Descargas/proyecto-web/src/app.js")), "el proyecto conserva su estructura");
ok(tras.some((f) => f.includes("Propuesta.pages/index.xml")), "el .pages sí se movió, entero y sin abrirlo");

console.log("\n── Duplicados");
r = await cliente.callTool({ name: "organizador_buscar_duplicados", arguments: { ruta: docs } });
ok(datos(r).total === 1, `1 grupo de duplicados (${datos(r).total})`);
const grupo = datos(r).elementos[0];
ok(grupo.sobrantes.length === 1, "con un sobrante");
r = await cliente.callTool({
  name: "organizador_borrar_duplicados",
  arguments: { grupos: [{ conservar: grupo.conservar, sobrantes: grupo.sobrantes }] },
});
ok(datos(r).borrados === 1, "borra el duplicado exacto");

console.log("\n── Borrado protegido: no borra lo que no coincide");
r = await cliente.callTool({
  name: "organizador_borrar_duplicados",
  arguments: { grupos: [{ conservar: path.join(docs, "99 · Sin clasificar", "documento.md"), sobrantes: [path.join(docs, "99 · Sin clasificar", "Xcode_15.dmg")] }] },
});
ok(datos(r).borrados === 0 && datos(r).omitidos === 1, "se niega a borrar un fichero distinto");
ok(JSON.stringify(datos(r)).includes("huella no coincide"), "y dice exactamente por qué");

console.log("\n── Mover a la taxonomía");
r = await cliente.callTool({
  name: "organizador_mover",
  arguments: {
    movimientos: [
      { ruta: path.join(docs, "99 · Sin clasificar", "documento.md"),
        carpeta: "06 · Clientes y proyectos anteriores",
        subcarpeta: "BARRY",
        nombre_nuevo: "2022 · Informe urbanístic · Ptge Ratés.md",
        motivo: "el contenido cita Passatge de Rates y el expedient T1068" },
      { ruta: path.join(docs, "99 · Sin clasificar", "captura.png"), carpeta: "09 · Fotos y medios" },
    ],
  },
});
ok(datos(r).movidos === 2, `2 movidos (${datos(r).movidos})`);
const idMovimiento = datos(r).resultados[0].id;
const trasMover = await arbol(docs);
ok(trasMover.some((f) => f.includes("BARRY/2022 · Informe urbanístic · Ptge Ratés.md")), "renombra y coloca en la subcarpeta");

console.log("\n── Registro");
r = await cliente.callTool({ name: "organizador_ver_registro", arguments: { limite: 100 } });
ok(datos(r).total >= 9, `el registro tiene todas las operaciones (${datos(r).total})`);
ok(JSON.stringify(datos(r)).includes("Passatge de Rates"), "guarda el motivo razonado");

console.log("\n── Deshacer");
r = await cliente.callTool({ name: "organizador_deshacer", arguments: { ids: [idMovimiento] } });
ok(datos(r).revertidos === 1, "revierte el movimiento");
const trasDeshacer = await arbol(docs);
ok(trasDeshacer.some((f) => f.endsWith("99 · Sin clasificar/documento.md")), "el fichero volvió con su nombre original");
r = await cliente.callTool({ name: "organizador_deshacer", arguments: { ids: [idMovimiento] } });
ok(datos(r).resultados[0].estado === "ya_revertida", "no revierte dos veces lo mismo");

console.log("\n── Deshacer un borrado: debe declararse irrecuperable");
r = await cliente.callTool({ name: "organizador_ver_registro", arguments: { limite: 100 } });
const borrado = datos(r).elementos.find((a) => a.op === "borrar");
r = await cliente.callTool({ name: "organizador_deshacer", arguments: { ids: [borrado.id] } });
ok(datos(r).irrecuperables === 1, "declara el borrado irrecuperable");
ok(JSON.stringify(datos(r)).includes("Time Machine"), "y dirige a Time Machine");

await cliente.close();
console.log(fallos === 0 ? "\n🟢 TODAS LAS COMPROBACIONES PASAN\n" : `\n🔴 ${fallos} COMPROBACIONES FALLAN\n`);
process.exit(fallos === 0 ? 0 : 1);
