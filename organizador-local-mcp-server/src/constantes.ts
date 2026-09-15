/**
 * Constantes compartidas del servidor.
 *
 * La taxonomía es deliberadamente la misma que la de Google Drive del usuario,
 * para que el Mac y Drive queden con la misma forma y un documento se busque
 * igual en los dos sitios.
 */

/** Tope de caracteres por respuesta, para no ahogar el contexto del agente. */
export const LIMITE_CARACTERES = 25_000;

/** Las once carpetas de la taxonomía, en orden. */
export const TAXONOMIA = [
  "01 · OCTAVA · Negocio y campaña",
  "02 · OCTAVA · Marca y piezas",
  "03 · OCTAVA · IA, prompts y skills",
  "04 · Método operativo de restauración",
  "05 · Archivo de calidad · Hotel Diagonal Barcelona",
  "06 · Clientes y proyectos anteriores",
  "07 · Personal · Administración y finanzas",
  "08 · Personal · Identidad, carrera y salud",
  "09 · Fotos y medios",
  "10 · Respaldos y volcados",
  "99 · Sin clasificar",
] as const;

export type Carpeta = (typeof TAXONOMIA)[number];

/** Carpeta de sistema: guarda el LOG y el diario de deshacer. Nunca se clasifica. */
export const CARPETA_SISTEMA = "00 · SISTEMA";

/** Subcarpeta donde aterrizan intactas las carpetas traídas de Descargas. */
export const CARPETA_DESCARGAS = "99 · Sin clasificar/Carpetas de Descargas";

export const FICHERO_LOG = "LOG.md";
export const FICHERO_DIARIO = "diario.jsonl";

/**
 * Nombres que nunca se tocan. Romper un paquete de macOS rompe el documento,
 * y tocar node_modules o Library rompe proyectos e instalaciones.
 */
export const DIRECTORIOS_PROTEGIDOS = new Set([
  "node_modules",
  "Library",
  ".git",
  CARPETA_SISTEMA,
]);

/**
 * Paquetes de macOS que son DOCUMENTOS: por dentro son un directorio, pero
 * para el usuario son un fichero. Se pueden mover enteros sin romperlos;
 * lo que los rompe es entrar dentro y sacarles las piezas.
 */
export const EXTENSIONES_PAQUETE_DOCUMENTO = [".pages", ".key", ".numbers", ".rtfd"];

/**
 * Paquetes que son aplicaciones o bibliotecas, no documentos. No se clasifican
 * ni se mueven: una app vive donde la instalaste, y una fototeca pesa demasiado
 * para andar paseándola.
 */
export const EXTENSIONES_PAQUETE_SISTEMA = [
  ".app", ".framework", ".bundle", ".sparsebundle",
  ".photoslibrary", ".fcpbundle", ".logicx", ".band",
];

/** Todos los paquetes: en ninguno se entra a recorrer. */
export const EXTENSIONES_PAQUETE = [
  ...EXTENSIONES_PAQUETE_DOCUMENTO,
  ...EXTENSIONES_PAQUETE_SISTEMA,
];

/** Descargas a medias: moverlas rompe la descarga. */
export const EXTENSIONES_INCOMPLETAS = [
  ".download", ".crdownload", ".part", ".aria2", ".tmp", ".partial",
];

/** Extensiones cuyo texto se puede leer directamente. */
export const EXTENSIONES_TEXTO = [
  ".txt", ".md", ".markdown", ".csv", ".tsv", ".json", ".xml", ".yaml", ".yml",
  ".html", ".htm", ".log", ".sh", ".js", ".ts", ".py", ".gs", ".css", ".sql",
];

/** Extensiones de paquete OOXML: el texto vive en XML dentro del zip. */
export const EXTENSIONES_OOXML = [".docx", ".xlsx", ".pptx"];

/** Extensiones que macOS sabe convertir con `textutil`. */
export const EXTENSIONES_TEXTUTIL = [".doc", ".rtf", ".odt", ".wordml", ".webarchive"];
