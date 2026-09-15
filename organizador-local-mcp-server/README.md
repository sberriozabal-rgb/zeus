# organizador-local-mcp-server

Servidor MCP que deja a Claude organizar las carpetas **locales** de tu Mac
(`~/Documentos`, `~/Descargas`) clasificando cada documento **por lo que dice**,
no por cómo se llama.

La diferencia con un script de reglas es esa: un script ve `document.pdf` y no
puede hacer nada con él. Este servidor deja que el agente lo abra, lea que es un
informe urbanístico de un local concreto, y lo coloque y lo renombre en
consecuencia.

Corre por **stdio**, como subproceso de tu cliente MCP, en la misma máquina donde
están los ficheros. Un servidor remoto no serviría: el disco es local.

## Instalación

```bash
npm install
npm run build
```

### Claude Desktop

En `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "organizador-local": {
      "command": "node",
      "args": ["/ruta/absoluta/a/organizador-local-mcp-server/dist/index.js"],
      "env": {
        "ORGANIZADOR_RAICES": "/Users/TU_USUARIO/Documentos:/Users/TU_USUARIO/Descargas"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add organizador-local \
  --env ORGANIZADOR_RAICES=$HOME/Documentos:$HOME/Descargas \
  -- node /ruta/absoluta/a/organizador-local-mcp-server/dist/index.js
```

En macOS, la primera vez el sistema pedirá dar acceso a **Archivos y carpetas**
al cliente MCP (Ajustes › Privacidad y seguridad). Sin eso, todo devuelve
`EACCES`.

## La taxonomía

Las once carpetas son deliberadamente las mismas que las de Google Drive del
usuario, para que un documento se busque igual en los dos sitios:

| Carpeta | Qué va |
|---|---|
| `01 · OCTAVA · Negocio y campaña` | Plan, campañas, diagnósticos, prospectos |
| `02 · OCTAVA · Marca y piezas` | Manual de marca, isotipos, tipografías |
| `03 · OCTAVA · IA, prompts y skills` | Prompts, agentes, skills, Apps Script |
| `04 · Método operativo de restauración` | Escandallos, APPCC, inventarios, turnos |
| `05 · Archivo de calidad · Hotel Diagonal Barcelona` | El archivo histórico del hotel |
| `06 · Clientes y proyectos anteriores` | Un subdirectorio por cliente |
| `07 · Personal · Administración y finanzas` | Facturas, recibos, banco, impuestos |
| `08 · Personal · Identidad, carrera y salud` | DNI, CV, médico |
| `09 · Fotos y medios` | Imagen, vídeo, audio |
| `10 · Respaldos y volcados` | Archivos comprimidos, exports, versiones archivadas |
| `99 · Sin clasificar` | La bandeja de entrada: lo que aún no se ha decidido |

El registro y el diario de vuelta atrás viven en `00 · SISTEMA`, que nunca se
clasifica. Las carpetas traídas de Descargas aterrizan intactas en
`99 · Sin clasificar/Carpetas de Descargas`.

## Herramientas

### Solo lectura

| Herramienta | Qué hace |
|---|---|
| `organizador_listar_raices` | Dónde puede trabajar y con qué criterio. **Llámala primero.** |
| `organizador_inventariar` | Lista ficheros con tamaño y fecha, paginado |
| `organizador_leer_documento` | Extrae el texto para poder clasificar por contenido |
| `organizador_buscar_duplicados` | Agrupa los idénticos byte a byte |
| `organizador_ver_registro` | Qué se ha hecho, con los ids para deshacer |

### Modifican el disco

| Herramienta | Qué hace |
|---|---|
| `organizador_mover` | Aplica un lote de movimientos y renombrados |
| `organizador_borrar_duplicados` | Borra solo lo verificado idéntico |
| `organizador_fusionar_descargas` | Vacía Descargas dentro de Documentos |
| `organizador_deshacer` | Revierte movimientos usando el diario |

## Ejemplos

**1. Organizar lo que llegó de Descargas**

```
"Junta Descargas con Documentos y organiza lo que entre."
```

El agente encadena: `fusionar_descargas` (con `simulacro: true` primero si
quiere ver el alcance) → `inventariar` de `99 · Sin clasificar` →
`leer_documento` de todo lo que tenga nombre genérico → `mover` con el plan
completo y un motivo razonado por fichero.

**2. Averiguar qué es un fichero sin nombre**

```
"¿Qué es 'documento.pdf'? Ponlo donde toque."
```

`leer_documento` devuelve el texto; el agente decide carpeta, subcarpeta y un
nombre que se pueda buscar dentro de seis meses, y lo aplica con `mover`.

**3. Recuperar espacio sin riesgo**

```
"¿Cuánto espacio me sobra en Documentos?"
```

`buscar_duplicados` agrupa y propone cuál conservar. `borrar_duplicados` vuelve
a calcular el sha256 de los dos ficheros **en el momento de borrar**: si el
contenido cambió desde que lo miraste, no borra y lo dice.

**4. Arrepentirse**

```
"Deshaz lo último, has clasificado mal esas facturas."
```

`ver_registro` da los ids, `deshacer` los revierte de lo más reciente a lo más
antiguo. Lo borrado no vuelve desde aquí, y la herramienta lo dice sin rodeos:
hay que ir a Time Machine.

## Seguridad

- **Raíces cerradas.** Toda ruta pasa por una comprobación que resuelve enlaces
  simbólicos y verifica que sigue cayendo dentro de una raíz declarada. Un `..`
  en un parámetro no llega a `/etc`.
- **Nunca se entra en** carpetas ocultas, `node_modules`, `Library`, `.git`, ni
  en paquetes de macOS. Los paquetes-documento (`.pages`, `.key`, `.numbers`,
  `.rtfd`) sí se mueven, pero enteros: lo que los rompe es sacarles las piezas.
- **Las descargas a medias** (`.download`, `.crdownload`, `.part`, `.aria2`) se
  quedan donde están.
- **Snapshot APFS** antes de la primera operación destructiva del proceso. Si no
  está disponible (no es macOS, o Time Machine no está configurado), la respuesta
  lo dice en vez de callárselo.
- **Se anota antes de ejecutar**, no después: si algo falla a mitad, el registro
  ya tiene la operación.
- **No se borra sin verificar la huella** en el momento del borrado.
- **No se pisa nada**: un destino ocupado por contenido distinto recibe sufijo
  ` · 2`; ocupado por contenido idéntico, se omite el movimiento.

### Lo que este servidor no protege

El borrado es directo, sin papelera ni cuarentena — es la regla de la casa,
acordada. La red es el snapshot APFS (~24 h) y el registro. Fuera de esa
ventana, la vuelta atrás es tu respaldo normal de Time Machine.

## Pruebas

```bash
npm test              # 38 comprobaciones contra un cliente MCP real
npm run eval:preparar # fixture determinista de la evaluación
npm run eval:resolver # resuelve las 10 preguntas y enseña las respuestas
```

La prueba de integración arranca el servidor por stdio y lo conduce con el
cliente del SDK, igual que haría Claude Desktop: cubre seguridad de rutas,
protecciones, fusión, duplicados, movimientos, registro y deshacer.

`eval:resolver` no solo imprime las respuestas: las contrasta con las
publicadas en `evaluacion.xml` y **sale con error si alguna deja de coincidir**.
Así la evaluación no se queda afirmando cosas que ya no son ciertas.

El CI del repositorio (`.github/workflows/ci.yml`) ejecuta compilación, pruebas
y evaluación en **ubuntu-latest y macos-latest** en cada push.

Las preguntas de `pruebas/evaluacion/evaluacion.xml` están pensadas para que
ninguna se resuelva leyendo nombres de fichero: hay que abrir los documentos.
