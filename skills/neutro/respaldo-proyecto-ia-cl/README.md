# respaldo-proyecto-ia-cl

Skill de la **línea neutra** (Agent Skills, estándar abierto).

Convierte el contenido de un Proyecto de Claude en un **paquete cifrado AES-256** con archivo
maestro de reconstrucción, resumen de chats, checksums SHA-256 y lista de huecos declarados.

## Lo primero, y no es opcional

**Anthropic no soporta migrar datos entre cuentas personales.** Cita literal del Centro de Ayuda:

> *"Exported data can't be imported into another personal Claude account, and we don't support
> migrating data between personal accounts."*

**No existe un botón de migración y esta skill no lo inventa.** Lo que produce es un paquete de
**reconstrucción manual**: el contenido ordenado, clasificado y con el guion para rehacerlo.

## Las cuatro clases, leídas de C3 hacia C0

| Clase | Criterio | Destino |
|---|---|---|
| **C0 · PÚBLICO** | Podría publicarse hoy sin consecuencia | Entra sin cambios |
| **C1 · INTERNO** | Método propio; su fuga da ventaja a un competidor | Entra cifrado |
| **C2 · CONFIDENCIAL** | Nombra a un tercero identificable, precios o contratos | Cifrado **y redactado** |
| **C3 · SECRETO** | Da acceso: clave, token, credencial | **NO ENTRA. Se rota.** |

Dos reglas duras: un archivo con una clave API es **C3 aunque el otro 99 % sea público** —se
parte el archivo, no se rebaja la clase—, y **clase desconocida = C2, nunca C0**. Las
transcripciones de chats son **C2 por defecto**: es donde vive el dato personal que nadie recuerda
haber escrito.

## Por qué ZIP anidado y no un ZIP con contraseña

El **directorio central de un ZIP va en claro**: los nombres de archivo se leen sin introducir la
contraseña, y los nombres de archivo son datos. Por eso el paquete es un ZIP cifrado que contiene
otro ZIP, con nombres neutros dentro y la correspondencia en `INDICE-ADJUNTOS.md`.

Y por eso nunca se usa el cifrado ZIP heredado: está
[roto por ataque de texto conocido desde 1994](https://homes.cs.washington.edu/~yoshi/papers/WinZip/winzip.pdf),
y una contraseña larga no lo arregla.

## La regla que hace que el respaldo sirva

**Probar la restauración en frío antes de borrar el origen**, en carpeta vacía distinta, abriendo
tres archivos de tres carpetas, con línea fechada y firmada en el manifiesto — **y en un día
distinto al del sellado**.

Un respaldo no verificado tiene la misma fiabilidad que no tenerlo, **con la desventaja de que
tranquiliza**.

## Requisitos

Python 3.9+ y `pyzipper` para el cifrado AES-256. **Sin `pyzipper` el paquete se entrega sin
cifrar, y así se declara** — no se disimula.

Para el historial de chats hace falta el ZIP del
[export oficial](https://support.claude.com/en/articles/9450526-export-your-claude-data).
**Su enlace caduca: descárgalo en menos de 24 horas.**

## Ficheros

- `references/casos.md` — los cinco casos con detalle, incluido el de datos sucios.
- `references/fuentes.md` — fuentes y límites de plataforma documentados.
- `cases/` — los 4 casos de prueba principales.
- `scripts/` — ingesta, sellado y verificación.

## Licencia

Propietaria. Ver `LICENSE.txt`.
