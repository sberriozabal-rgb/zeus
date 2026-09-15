# Como exportar la biblioteca desde cada software

El objetivo es obtener un fichero que `cruzar.py` pueda leer: un
`collection.xml` de rekordbox, o un CSV con al menos `artist` y `title`.

## rekordbox (recomendado)

`File > Export Collection in xml format`

Fuente: FAQ oficial de rekordbox
<https://rekordbox.com/en/support/faq/operation-hints-7/>

Exportacion automatica programada, util para no repetir el paso antes de cada
evento: `Preferences > Advanced > Others > XML Auto Export` (destino Dropbox).

**Limitacion documentada:** el XML NO exporta My Tags ni playlists
inteligentes. Si el DJ organiza el repertorio de eventos con My Tags, esa
informacion no llega al cruce y hay que decirlo.

## Serato

No exporta XML. Dos rutas:

1. Exportar el crate a CSV desde herramientas de terceros (Lexicon exporta a
   CSV, M3U8, HTML y PDF: <https://www.lexicondj.com/pricing>).
2. Trabajar sobre un CSV manual con las columnas `artist,title`.

Los `.crate` son binarios y su formato es ingenieria inversa de la comunidad,
no especificacion oficial de Serato
(<https://github.com/mixxxdj/mixxx/wiki/Serato-Database-Format>). Esta skill
NO los lee: pedir siempre un CSV.

## Engine DJ (Denon)

Base de datos SQLite. Igual que Serato: exportar a CSV con herramienta externa.

## Traktor

`collection.nml` (XML propio). Esta skill no lo parsea de forma nativa:
convertir a CSV antes.

## CSV minimo aceptable

```csv
artist,title
Bad Bunny,Tití Me Preguntó
Karol G,Provenza
```

Columnas opcionales que mejoran el informe si estan presentes:
`mix`, `bpm`, `key`, `genre`, `location`.

El separador puede ser coma, punto y coma, tabulador o barra vertical: el
script lo detecta solo. La codificacion debe ser UTF-8.

## Comprobacion rapida

```bash
python3 scripts/cruzar.py biblioteca.csv peticiones.txt
```

La primera linea del informe dice cuantos tracks se leyeron. Si dice 0, el
fichero no es legible o las columnas no se llaman como se espera.
