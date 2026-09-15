#!/usr/bin/env node
/**
 * organizador-local-mcp-server
 *
 * Servidor MCP que organiza las carpetas LOCALES de un Mac (~/Documentos,
 * ~/Descargas) contra una taxonomía fija, dejando que el agente decida leyendo
 * el contenido de cada documento en vez de adivinar por el nombre.
 *
 * Transporte stdio: corre como subproceso del cliente MCP, en la misma máquina
 * donde están los ficheros. Un servidor remoto no serviría: el disco es local.
 *
 * Regla de la casa aplicada: borrado directo, sin cuarentena, con snapshot APFS
 * previo y registro completo de todo.
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { registrarEscritura } from "./herramientas/escritura.js";
import { registrarLectura } from "./herramientas/lectura.js";
import { raicesPermitidas } from "./servicios/rutas.js";

const VERSION = "1.0.0";

const AYUDA = `organizador-local-mcp-server v${VERSION}

Servidor MCP (stdio) para organizar carpetas locales contra una taxonomía fija.

Uso:
  organizador-local-mcp-server            arranca el servidor por stdio
  organizador-local-mcp-server --help     esta ayuda
  organizador-local-mcp-server --version  la versión

Variables de entorno:
  ORGANIZADOR_RAICES   Rutas separadas por ':' donde el servidor puede operar.
                       Por defecto: ~/Documentos, ~/Documents, ~/Descargas,
                       ~/Downloads (las que existan).

Configuración en Claude Desktop (claude_desktop_config.json):
  {
    "mcpServers": {
      "organizador-local": {
        "command": "node",
        "args": ["/ruta/absoluta/a/dist/index.js"],
        "env": { "ORGANIZADOR_RAICES": "/Users/tu-usuario/Documentos:/Users/tu-usuario/Descargas" }
      }
    }
  }

Configuración en Claude Code:
  claude mcp add organizador-local -- node /ruta/absoluta/a/dist/index.js

Herramientas:
  Lectura   organizador_listar_raices, organizador_inventariar,
            organizador_leer_documento, organizador_buscar_duplicados,
            organizador_ver_registro
  Escritura organizador_mover, organizador_borrar_duplicados,
            organizador_fusionar_descargas, organizador_deshacer
`;

async function principal(): Promise<void> {
  const argumentos = process.argv.slice(2);
  if (argumentos.includes("--help") || argumentos.includes("-h")) {
    process.stdout.write(AYUDA);
    return;
  }
  if (argumentos.includes("--version") || argumentos.includes("-v")) {
    process.stdout.write(`${VERSION}\n`);
    return;
  }

  const servidor = new McpServer({ name: "organizador-local-mcp-server", version: VERSION });
  registrarLectura(servidor);
  registrarEscritura(servidor);

  // En stdio, stdout es el canal del protocolo: cualquier traza va a stderr.
  const raices = await raicesPermitidas();
  if (raices.length === 0) {
    console.error(
      "AVISO: no se encontró ninguna raíz. Este servidor debe ejecutarse en la máquina " +
        "donde viven las carpetas. Comprueba ~/Documentos o define ORGANIZADOR_RAICES.",
    );
  } else {
    console.error(`organizador-local-mcp-server v${VERSION} · raíces: ${raices.join(", ")}`);
  }

  const transporte = new StdioServerTransport();
  await servidor.connect(transporte);
}

principal().catch((e: unknown) => {
  console.error("Error fatal del servidor:", e instanceof Error ? e.message : String(e));
  process.exit(1);
});
