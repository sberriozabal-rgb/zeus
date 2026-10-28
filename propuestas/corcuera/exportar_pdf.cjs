// Exporta las láminas de Corcuera a PDF (una por página, a tamaño real) y, con --png, a PNG.
// Uso: node exportar_pdf.cjs [--png]
// Requiere Playwright con Chromium. Las fuentes se cargan de Google Fonts: hace falta red.
const { chromium } = require('playwright');
const { pathToFileURL } = require('node:url');
const { join } = require('node:path');
const { mkdirSync } = require('node:fs');

const aqui = __dirname;
const base = 'corcuera-propuesta-bar-lobby';
const html = pathToFileURL(join(aqui, `${base}.html`)).href;

(async () => {
const navegador = await chromium.launch();
const pagina = await navegador.newPage({ viewport: { width: 1632, height: 1200 } });
await pagina.goto(html, { waitUntil: 'networkidle' });
await pagina.evaluate(() => document.fonts.ready);

await pagina.pdf({ path: join(aqui, `${base}.pdf`), preferCSSPageSize: true, printBackground: true });
console.log(`PDF: ${base}.pdf`);

if (process.argv.includes('--png')) {
  const destino = join(aqui, 'laminas');
  mkdirSync(destino, { recursive: true });
  const laminas = await pagina.$$('.lamina');
  for (const [i, lamina] of laminas.entries()) {
    await lamina.screenshot({ path: join(destino, `lamina-${i + 1}.png`) });
  }
  console.log(`PNG: ${laminas.length} láminas en laminas/`);
}

await navegador.close();
})();
