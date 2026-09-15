/**
 * Fixture determinista para la evaluación.
 *
 * Solo usa formatos que el servidor lee sin binarios externos (.md .txt .csv
 * .json .html), para que la evaluación corra igual en cualquier máquina sin
 * depender de que poppler o textutil estén instalados.
 */
import * as fs from "node:fs/promises";
import * as path from "node:path";
import { fileURLToPath } from "node:url";

const aqui = path.dirname(fileURLToPath(import.meta.url));
export const RAIZ = path.join(aqui, ".arenero");
export const DOCS = path.join(RAIZ, "Documentos");
export const DESC = path.join(RAIZ, "Descargas");

const INFORME_VENTAS = `empresa,periodo,base,cuota,total,operaciones
FIMARABA RESTAURACION SL,2016-Q2,148411.69,14841.37,163253.06,639
`;

const FACTURA_SANOFI = `FACTURA SIMPLIFICADA T-4964
Restaurante Ikea - Portal de Castilla 27, 01007 Vitoria-Gasteiz
FIMARABA RESTAURACION SL - NIF B-01545185
Cliente: SANOFI AVENTIS S.A. - A-08163586
Fecha: 24/11/2017 13:45
Comensales: 8
Concepto: MENU x 8 a 60,00 EUR
Base imponible: 436,36 EUR
IVA 10%: 43,64 EUR
TOTAL: 480,00 EUR
`;

const INFORME_URBANISTICO = `# Informe urbanistic previ

Ajuntament de Barcelona - Districte de Sant Marti
Expedient: T1068
Emplacament: Passatge de Rates 11-15, 08018 Barcelona
Activitat sol.licitada: BOTIGA DE PLATS PREPARATS
Data de presentacio: 31/03/2022

Es sol.licita un nou certificat urbanistic previ a la tramitacio de la
comunicacio per a la instal.lacio de l'activitat.
`;

const ALTA_FIBRA = `Boletin digital de instalacion
Codigo: 7434516
Cliente: BELCEBU BCN SL
NIF/CIF: B-67595736
Direccion: Passatge de Rates 13 (local 2), 08018 Barcelona
Servicio: Pack Internet Fibra 1Gb + linea
Velocidad contratada: 1000/1000
Fecha de instalacion: 16/06/2023
`;

const ACTA = `# Notas de la reunion

Repasamos el estado del local de Passatge de Rates 11-15.
Pendiente: cerrar el tema del certificado urbanistico antes de fin de mes.
`;

/** Relleno determinista: mismo contenido siempre, para que los tamaños no bailen. */
const relleno = (n) => "x".repeat(n);

export async function preparar() {
  await fs.rm(RAIZ, { recursive: true, force: true });
  const sinClasificar = path.join(DOCS, "99 · Sin clasificar");
  const finanzas = path.join(DOCS, "07 · Personal · Administración y finanzas");
  await fs.mkdir(sinClasificar, { recursive: true });
  await fs.mkdir(finanzas, { recursive: true });
  await fs.mkdir(DESC, { recursive: true });

  // --- Documentos con nombre genérico: solo el contenido los delata ---
  await fs.writeFile(path.join(sinClasificar, "documento.md"), INFORME_URBANISTICO);
  await fs.writeFile(path.join(sinClasificar, "sin-titulo.txt"), FACTURA_SANOFI);
  await fs.writeFile(path.join(sinClasificar, "Libro1.csv"), INFORME_VENTAS);
  await fs.writeFile(path.join(sinClasificar, "adjunto-3.txt"), ALTA_FIBRA);
  await fs.writeFile(path.join(sinClasificar, "notas.md"), ACTA);
  // El más pesado de la carpeta, a propósito.
  await fs.writeFile(path.join(sinClasificar, "volcado.json"), JSON.stringify({ relleno: relleno(40_000) }));

  // --- Duplicados exactos: dos grupos ---
  await fs.writeFile(path.join(finanzas, "recibo luz.txt"), "RECIBO IBERDROLA 181,20 EUR\n");
  await fs.writeFile(path.join(sinClasificar, "recibo luz copia.txt"), "RECIBO IBERDROLA 181,20 EUR\n");
  await fs.writeFile(path.join(finanzas, "recibo gas.txt"), "RECIBO EDP NATURGAS 399,91 EUR\n");
  await fs.writeFile(path.join(sinClasificar, "recibo gas (1).txt"), "RECIBO EDP NATURGAS 399,91 EUR\n");

  // --- Descargas ---
  await fs.writeFile(path.join(DESC, "pelicula.mp4.download"), relleno(500));
  await fs.writeFile(path.join(DESC, "manual.txt"), "Manual de usuario.\n");
  await fs.mkdir(path.join(DESC, "node_modules", "left-pad"), { recursive: true });
  await fs.writeFile(path.join(DESC, "node_modules", "left-pad", "index.js"), "module.exports=0");
  await fs.mkdir(path.join(DESC, "Instalador.app", "Contents"), { recursive: true });
  await fs.writeFile(path.join(DESC, "Instalador.app", "Contents", "Info.plist"), "<plist/>");
  await fs.mkdir(path.join(DESC, "fotos-viaje"), { recursive: true });
  await fs.writeFile(path.join(DESC, "fotos-viaje", "IMG_001.jpg"), relleno(120));

  return { DOCS, DESC };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  await preparar();
  console.log(`Fixture listo en ${RAIZ}`);
}
