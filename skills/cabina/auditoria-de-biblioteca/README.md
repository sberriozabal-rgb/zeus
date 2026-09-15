# auditoria-de-biblioteca

Skill de la línea **CABINA**, paquete **CABINA CORE** (Agent Skills, estándar abierto).

Diagnostica una biblioteca de DJ exportada de rekordbox y devuelve un parte de reparación
priorizado por riesgo real en cabina, no por volumen de hallazgos. Solo lectura: nunca
escribe en la base de datos del DJ.

## Qué entrega

Un parte con índice de salud 0-100, los hallazgos por categoría traducidos a consecuencia
concreta ("312 que no podrás sincronizar", no "312 sin beatgrid"), un top-3 de acciones para
el próximo bolo con nombre y apellido, y un bloque de mantenimiento aparte con la estimación
de trabajo separada entre lo que se arregla en lote y lo que exige oír el audio.

## Instalación

Copia esta carpeta completa (o el `.skill` empaquetado) en el directorio de skills del agente
que la va a ejecutar, o instálala desde el repositorio privado si tienes acceso vigente.

## Uso

```bash
python3 scripts/dj_toolkit.py audit <collection.xml>
python3 scripts/dj_toolkit.py audit <collection.xml> --comprobar-rutas   # solo en tu máquina
python3 scripts/dj_toolkit.py audit <collection.xml> --json              # datos crudos
```

Exporta el XML desde rekordbox con `File > Export Collection in xml format`.

**`--comprobar-rutas` solo tiene sentido en la máquina donde vive la música.** Desde otra,
todas las rutas salen rotas y el parte de rutas es basura; la skill lo detecta y lo declara.

## Lo que esta skill no hace

Diagnostica, no repara. Si lo que quieres es reparación automática en lote, compra
[Lexicon](https://www.lexicondj.com/pricing) (199 USD vitalicio): limpia géneros, encuentra
duplicados sin romper playlists y remapea rutas. Esta skill hace lo que Lexicon no hace, que
es leer el estado con criterio de bolo y decir qué se arregla primero.

## Ficheros

- `SKILL.md` — la skill.
- `references/hallazgos.md` — catálogo de las 10 categorías: qué detecta, por qué importa en
  cabina, cómo se arregla y si el arreglo necesita oír el audio.
- `references/FUENTES.md` — fuentes externas con fecha de consulta y límites declarados.
- `scripts/dj_toolkit.py` — el motor del diagnóstico.
- `cases/` — los 4 casos de prueba.
- `ANEXO-A-ficha-comercial.md` — comprador, precio, canal y gates.

## Licencia

Propietaria. Uso permitido al comprador; prohibida la redistribución. Ver `LICENSE.txt`.
