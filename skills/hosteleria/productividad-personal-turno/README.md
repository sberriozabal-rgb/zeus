# Productividad de personal por turno  ·  `productividad-personal-turno`  v1.1.1

Sabes en qué franjas pagas plantilla sin venta y en cuáles pierdes venta por falta de mano.

## Qué es
Una Agent Skill conforme a la especificación abierta (agentskills.io). No es un documento
para leer: es un procedimiento que un motor compatible ejecuta cuando detecta el disparo.

## Para quién
Dueño o encargado de restaurante independiente de 1-3 locales, ES/MX. Decide el dueño.

## Instalación
1. Descomprime el paquete `.skill` (es un zip) o copia la carpeta completa.
2. Colócala en el directorio de skills de tu entorno, sin renombrar la carpeta:
   debe llamarse exactamente `productividad-personal-turno`.
3. Reinicia la sesión. La skill se activa sola cuando aparece uno de sus disparos;
   no hay que invocarla por su nombre.

## Cómo se usa
Pídelo con tus palabras. Ejemplos de frases que la activan están en la sección
"Cuándo se dispara" de `SKILL.md`. Si le faltan datos, no se bloquea: produce con los
valores por defecto más defendibles y declara al final qué asumió.

## Qué hay dentro
- `ANEXO-A-ficha-comercial.md`
- `CHANGELOG.md`
- `LICENSE.txt`
- `SKILL.md`
- `assets/ejemplo-28-dias.csv`
- `assets/plantilla-turnos.csv`
- `cases/case_01_happy_path.md`
- `cases/case_02_edge_case.md`
- `cases/case_03_failure.md`
- `cases/case_04_integration.md`
- `metadata.json`
- `references/coste-hora-por-pais.md`
- `references/umbrales-productividad.md`
- `scripts/productividad_turno.py`

## Antes de usarlo en un cliente
Toda cifra marcada `[A VALIDAR]` es criterio de oficio sin fuente publicada: se sustituye
por la medición real del cliente antes de ponerla en un informe que se cobra.

## Límites
Este activo no es asesoría legal, fiscal, laboral ni sanitaria. Ver la sección "Límites"
de `SKILL.md` y el aviso de `LICENSE.txt`.
