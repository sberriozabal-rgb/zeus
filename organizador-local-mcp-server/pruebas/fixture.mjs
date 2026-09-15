import * as fs from "node:fs/promises";
import * as path from "node:path";

export async function crearFixture(raiz) {
  await fs.rm(raiz, { recursive: true, force: true });
  const docs = path.join(raiz, "Documentos");
  const desc = path.join(raiz, "Descargas");
  await fs.mkdir(docs, { recursive: true });
  await fs.mkdir(desc, { recursive: true });

  // Documentos de partida
  await fs.writeFile(path.join(docs, "factura luz enero.pdf"), "RECIBO IBERDROLA 181,20 EUR");
  await fs.mkdir(path.join(docs, "vieja", "anidada"), { recursive: true });
  await fs.writeFile(path.join(docs, "vieja", "anidada", "nomina marzo.txt"), "NOMINA MARZO");

  // Descargas
  await fs.writeFile(path.join(desc, "factura luz enero.pdf"), "RECIBO IBERDROLA 181,20 EUR"); // dup exacto
  await fs.writeFile(path.join(desc, "DNI Sergio.pdf"), "OTRO CONTENIDO");
  await fs.writeFile(
    path.join(desc, "documento.md"),
    "# Informe urbanistic previ\n\nAjuntament de Barcelona. Passatge de Rates 11-15.\nBotiga de plats preparats. Expedient T1068.\n",
  );
  await fs.writeFile(path.join(desc, "Xcode_15.dmg"), "BINARIO FALSO");
  await fs.writeFile(path.join(desc, "captura.png"), "PNG FALSO");
  await fs.writeFile(path.join(desc, "pelicula.mp4.download"), "A MEDIAS");
  await fs.mkdir(path.join(desc, "proyecto-web", "src"), { recursive: true });
  await fs.writeFile(path.join(desc, "proyecto-web", "README.md"), "# proyecto");
  await fs.writeFile(path.join(desc, "proyecto-web", "src", "app.js"), "console.log(1)");
  await fs.mkdir(path.join(desc, "node_modules", "lodash"), { recursive: true });
  await fs.writeFile(path.join(desc, "node_modules", "lodash", "index.js"), "module.exports={}");
  // Paquete-documento: es un directorio, pero es un documento del usuario.
  await fs.mkdir(path.join(desc, "Propuesta.pages"), { recursive: true });
  await fs.writeFile(path.join(desc, "Propuesta.pages", "index.xml"), "<doc/>");
  // Paquete-aplicación: no es un documento, no se toca.
  await fs.mkdir(path.join(desc, "Instalador.app", "Contents"), { recursive: true });
  await fs.writeFile(path.join(desc, "Instalador.app", "Contents", "Info.plist"), "<plist/>");

  return { docs, desc };
}

export async function arbol(raiz) {
  const salida = [];
  async function paso(dir) {
    let entradas;
    try { entradas = await fs.readdir(dir, { withFileTypes: true }); } catch { return; }
    for (const e of entradas.sort((a, b) => a.name.localeCompare(b.name))) {
      const c = path.join(dir, e.name);
      if (e.isDirectory()) await paso(c);
      else salida.push(path.relative(raiz, c));
    }
  }
  await paso(raiz);
  return salida.sort();
}
