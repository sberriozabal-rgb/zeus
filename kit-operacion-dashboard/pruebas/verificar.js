// Comprobación automática de los criterios de aceptación con Playwright (Chromium).
// Uso: node pruebas/verificar.js <Kit_de_operacion.xlsx> [carpeta para capturas]
// Crea en una carpeta temporal dos copias modificadas del Excel (venta de alimentos a 4.000.000
// y un plato nuevo) con Python + openpyxl, sirve la página en localhost y compara cifras.
const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const os = require('os');
const path = require('path');
const { execFileSync } = require('child_process');

const raiz = path.resolve(__dirname, '..');
const excel = path.resolve(process.argv[2] || path.join(raiz, 'Kit_de_operacion.xlsx'));
const capturas = path.resolve(process.argv[3] || path.join(os.tmpdir(), 'kit-capturas'));
fs.mkdirSync(capturas, { recursive: true });

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'kit-'));
const excel4M = path.join(tmp, 'Kit_venta_4M.xlsx');
const excelPlato = path.join(tmp, 'Kit_plato_nuevo.xlsx');
execFileSync('python3', ['-I', '-c', `
import openpyxl, sys
src, a, b = sys.argv[1:4]
wb = openpyxl.load_workbook(src); wb['04 Estado de resultados']['B5'] = 4000000; wb.save(a)
wb = openpyxl.load_workbook(src); ws = wb['03 Ingeniería de menú']
ws['A20'] = 'Tiradito de pescado'; ws['B20'] = 300; ws['D20'] = 310; ws['E20'] = 80; wb.save(b)
`, excel, excel4M, excelPlato]);

const tipos = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.md': 'text/markdown' };
const servidor = http.createServer((req, res) => {
  const ruta = path.join(raiz, decodeURIComponent(req.url.split('?')[0]).replace(/^\/$/, '/index.html'));
  if (!ruta.startsWith(raiz) || !fs.existsSync(ruta)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': tipos[path.extname(ruta)] || 'application/octet-stream' });
  fs.createReadStream(ruta).pipe(res);
});

let fallos = 0;
function comprobar(nombre, ok, detalle) {
  console.log((ok ? 'OK   ' : 'FALLA') + '  ' + nombre + (detalle ? '  → ' + detalle : ''));
  if (!ok) fallos++;
}
const texto = (page, sel) => page.$eval(sel, (e) => e.innerText.replace(/\s+/g, ' ').trim());

(async () => {
  await new Promise((r) => servidor.listen(0, r));
  const url = 'http://127.0.0.1:' + servidor.address().port + '/';
  const navegador = await chromium.launch();
  const contexto = await navegador.newContext({ viewport: { width: 1200, height: 900 } });
  const page = await contexto.newPage();
  const errores = [];
  page.on('console', (m) => { if (m.type() === 'error') errores.push(m.text()); });
  page.on('pageerror', (e) => errores.push('pageerror: ' + e.message));
  await page.goto(url);
  await page.waitForFunction(() => window.KIT && document.querySelector('#menu canvas'));

  // 1. Datos precargados = resultados esperados
  const cinco = await texto(page, '#cinco');
  const punto = await texto(page, '#punto');
  const res = await texto(page, '#resultados');
  const menu = await texto(page, '#menu');
  const fugas = await texto(page, '#fugas');
  const reservas = await texto(page, '#reservas');
  const pase = await texto(page, '#pase');
  comprobar('Etiqueta «Ejemplo» visible', await page.isVisible('#etiqueta-ejemplo'));
  comprobar('Prime cost 2,850,000 · 57.0 %', /Prime cost \$2,850,000 57\.0 %/.test(res), res.slice(0, 400));
  comprobar('Utilidad de operación 900,000 · 18.0 %', /Utilidad de operación \$900,000 18\.0 %/.test(res));
  comprobar('Utilidad neta 600,000 · 12.0 %', /Utilidad neta \$600,000 12\.0 %/.test(res));
  comprobar('Un punto de prime cost = $50,000', /prime cost son \$50,000/.test(punto), punto);
  comprobar('Un punto de food cost = $35,000', /food cost son \$35,000/.test(punto));
  comprobar('Umbral de popularidad 5.83 %', /Umbral de popularidad 5\.83 %/.test(menu));
  comprobar('Margen medio ponderado $161.85', /Margen medio ponderado \$161\.85/.test(menu));
  const cats = await page.evaluate(() => {
    const r = KIT.calcMenu(KIT.estado().datos.menu), o = {};
    r.platos.forEach((p) => { (o[p.categoria] = o[p.categoria] || []).push(p.plato); });
    return o;
  });
  comprobar('Estrellas: Pulpo, Camarones, Ribeye', JSON.stringify(cats['Estrella']) === JSON.stringify(['Pulpo a la brasa', 'Camarones al ajillo', 'Ribeye 350 g']), JSON.stringify(cats['Estrella']));
  comprobar('Rompecabezas: Pechuga, Pasta, Risotto', JSON.stringify(cats['Rompecabezas']) === JSON.stringify(['Pechuga rellena', 'Pasta del día', 'Risotto de hongos']));
  comprobar('Caballos de batalla: los otros seis', (cats['Caballo de batalla'] || []).length === 6);
  comprobar('Ningún Perro', !cats['Perro'] && /Perros · 0/.test(menu));
  comprobar('Fuga diez referencias: $2,986 semana, $12,928 mes, 3.68 %', /\$12,928 al mes \$2,986 a la semana · 3\.68 % del costo teórico/.test(fugas), fugas.slice(0, 200));
  comprobar('Fuga barra: $16,589 semana, $71,832 mes', /\$71,832 al mes \$16,589 a la semana/.test(fugas));
  comprobar('Nota de la misma botella', /Son la misma botella contada dos veces/.test(fugas));
  comprobar('Enero: 57,600 / 19,200 / 38,400', /Enero 400 48 12\.0 % \$57,600 \$19,200 \$38,400/.test(reservas), reservas.slice(0, 300));
  comprobar('Pase 21–23 Pulpo 26.5 / 27', /21–23 Pulpo a la brasa 26\.5 27\.0/.test(pase));
  comprobar('Pase 21–23 Ribeye 23.5 / 25', /21–23 Ribeye 350 g 23\.5 25\.0/.test(pase));
  comprobar('Pase 21–23 Hamburguesa 23.5 / 24', /21–23 Hamburguesa de la casa 23\.5 24\.0/.test(pase));
  comprobar('Pase 13–15 Pulpo 20.5 / 22', /13–15 Pulpo a la brasa 20\.5 22\.0/.test(pase));
  comprobar('Cinco números de S-4 (31.9 %, 21.8 %, 29.5 %, 58.4 %, $487)', /31\.9 %/.test(cinco) && /21\.8 %/.test(cinco) && /29\.5 %/.test(cinco) && /58\.4 %/.test(cinco) && /\$487/.test(cinco), cinco);
  await page.screenshot({ path: path.join(capturas, 'ejemplo-escritorio.png'), fullPage: true });

  // 2. Cargar el Excel sin modificar = mismos números que el ejemplo
  await page.setInputFiles('#archivo', excel);
  await page.waitForFunction(() => KIT.estado().fuente === 'archivo');
  const iguales = await page.evaluate(() => {
    const a = KIT.estado().datos, b = KIT.EJEMPLO, dif = [];
    (function cmp(x, y, ruta) {
      if (typeof x === 'number' || typeof y === 'number') { if (!(Math.abs(x - y) < 1e-9)) dif.push(ruta + ': ' + x + ' ≠ ' + y); return; }
      if (x && y && typeof x === 'object') { new Set(Object.keys(x).concat(Object.keys(y))).forEach((k) => { if (!(x[k] == null && y[k] == null)) cmp(x[k], y[k], ruta + '.' + k); }); return; }
      if (x !== y) dif.push(ruta + ': ' + JSON.stringify(x) + ' ≠ ' + JSON.stringify(y));
    })(a, b, 'datos');
    return dif;
  });
  comprobar('Excel sin modificar = datos precargados', iguales.length === 0, iguales.slice(0, 6).join(' | '));
  comprobar('Al cargar se quita «Ejemplo» y sale archivo y hora', !(await page.isVisible('#etiqueta-ejemplo')) && /Kit_de_operacion\.xlsx · cargado el/.test(await texto(page, '#fuente')), await texto(page, '#fuente'));
  comprobar('Mismo texto de resultados tras cargar', (await texto(page, '#resultados')) === res && (await texto(page, '#fugas')) === fugas && (await texto(page, '#menu')) === menu);

  // 3. Venta de alimentos a 4.000.000
  await page.setInputFiles('#archivo', excel4M);
  await page.waitForFunction(() => KIT.estado().archivo === 'Kit_venta_4M.xlsx');
  const res4 = await texto(page, '#resultados'), punto4 = await texto(page, '#punto');
  comprobar('4M: prime cost 3,000,000 · 54.5 %', /Prime cost \$3,000,000 54\.5 %/.test(res4), res4.slice(0, 400));
  comprobar('4M: utilidad de operación 1,250,000 · 22.7 %', /Utilidad de operación \$1,250,000 22\.7 %/.test(res4));
  comprobar('4M: utilidad neta 950,000 · 17.3 %', /Utilidad neta \$950,000 17\.3 %/.test(res4));
  comprobar('4M: punto de prime cost $55,000 y de food cost $40,000', /\$55,000/.test(punto4) && /\$40,000/.test(punto4), punto4);

  // 4. Plato nuevo en la pestaña 03
  await page.setInputFiles('#archivo', excelPlato);
  await page.waitForFunction(() => KIT.estado().archivo === 'Kit_plato_nuevo.xlsx');
  const nuevo = await page.evaluate(() => {
    const r = KIT.calcMenu(KIT.estado().datos.menu);
    return { n: r.platos.length, umbral: r.umbral, medio: r.margenMedio, p: r.platos.find((p) => p.plato === 'Tiradito de pescado') };
  });
  comprobar('Plato nuevo leído (13 platos)', nuevo.n === 13 && !!nuevo.p, JSON.stringify(nuevo));
  comprobar('Tiradito → Rompecabezas (mezcla 1.88 % < 5.38 %, margen 230 ≥ 163.13)', nuevo.p && nuevo.p.categoria === 'Rompecabezas' && /Rompecabezas · 4/.test(await texto(page, '#menu')));

  // 6. Sin conexión tras la primera carga: recargar sin red muestra lo último guardado
  await page.setInputFiles('#archivo', excel);
  await page.waitForFunction(() => KIT.estado().archivo === 'Kit_de_operacion.xlsx');
  await page.check('#wins input[data-i="0"]');
  const contextoOff = contexto; // misma sesión de navegador = mismo localStorage
  await contextoOff.route(/^https?:\/\/(?!127\.0\.0\.1)/, (r) => r.abort());
  await page.reload();
  await page.waitForFunction(() => window.KIT);
  comprobar('Tras recargar sin red: sigue el Excel cargado', (await page.evaluate(() => KIT.estado().fuente)) === 'archivo' && !(await page.isVisible('#etiqueta-ejemplo')));
  comprobar('Tras recargar sin red: gráficos pintados (librerías locales)', await page.evaluate(() => !!window.Chart && !!window.XLSX && document.querySelectorAll('canvas').length >= 8));
  comprobar('Quick win guardado y «Toca ahora» en el 2', await page.evaluate(() => document.querySelector('#wins input[data-i="0"]').checked && document.querySelector('#wins li.toca input').getAttribute('data-i') === '1'));

  // 5. 400 px de ancho, claro y oscuro
  for (const esquema of ['light', 'dark']) {
    const ctx = await navegador.newContext({ viewport: { width: 400, height: 860 }, colorScheme: esquema, deviceScaleFactor: 2 });
    await ctx.route(/^https?:\/\/(?!127\.0\.0\.1)/, (r) => r.abort());
    const p = await ctx.newPage();
    p.on('console', (m) => { if (m.type() === 'error') errores.push('[' + esquema + '] ' + m.text()); });
    p.on('pageerror', (e) => errores.push('[' + esquema + '] pageerror: ' + e.message));
    await p.goto(url);
    await p.waitForFunction(() => window.KIT && document.querySelector('#menu canvas'));
    await p.waitForTimeout(300);
    const ancho = await p.evaluate(() => ({ doc: document.documentElement.scrollWidth, body: document.body.scrollWidth }));
    comprobar('400 px ' + esquema + ': sin scroll horizontal', ancho.doc <= 400 && ancho.body <= 400, JSON.stringify(ancho));
    const fondo = await p.evaluate(() => getComputedStyle(document.body).backgroundColor);
    comprobar('400 px ' + esquema + ': fondo del tema', esquema === 'dark' ? fondo === 'rgb(20, 26, 29)' : fondo === 'rgb(247, 244, 238)', fondo);
    await p.screenshot({ path: path.join(capturas, 'movil-' + esquema + '.png'), fullPage: true });
    await ctx.close();
  }

  // 7. Consola: se ignoran solo los fallos de red de CDN y Google Fonts (no hay red en la prueba)
  const propios = errores.filter((e) => !/ERR_FAILED|ERR_INTERNET_DISCONNECTED|ERR_NAME_NOT_RESOLVED|ERR_CONNECTION|Failed to load resource/.test(e));
  comprobar('Ningún error propio en la consola', propios.length === 0, propios.join(' | '));
  console.log('Errores de red ignorados: ' + (errores.length - propios.length));
  console.log('Capturas en ' + capturas);

  await navegador.close();
  servidor.close();
  console.log(fallos ? '\n' + fallos + ' comprobaciones fallaron.' : '\nTodo en orden.');
  process.exit(fallos ? 1 : 0);
})().catch((e) => { console.error(e); servidor.close(); process.exit(2); });
