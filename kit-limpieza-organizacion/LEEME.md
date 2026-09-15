# Kit de limpieza y organización · complemento

Piezas nuevas que se suman al **KIT DE LIMPIEZA Y ORGANIZACIÓN · OCTAVA SOG v1.0**
que ya vive en Drive.

## `organizador_documentos_y_descargas_mac_v1.2.sh`

Fusiona `~/Descargas` dentro de `~/Documentos` y organiza el conjunto contra la
misma taxonomía que usa Google Drive (`01 · … 10 · …` + `99 · Sin clasificar`),
de modo que el Mac y Drive quedan con la misma forma.

**Uso:** copiar el contenido entero y pegarlo en Terminal. Nada que instalar.

### Qué hace, en orden

| Fase | Qué |
|---|---|
| 0 | Fusiona `~/Descargas` → `~/Documentos` |
| 1 | Borra duplicados **byte a byte idénticos** |
| 2 | Manda versiones marcadas (`copia`, `(2)`) a `10 · Respaldos y volcados` |
| 3 | Clasifica en las once carpetas |
| 4 | Elimina carpetas vacías en cascada |

### Decisiones de la fase 0

- Los **ficheros sueltos** de Descargas entran en `99 · Sin clasificar` y siguen
  el circuito normal: se deduplican y se clasifican como todo lo demás.
- Las **carpetas** entran **intactas** en `99 · Sin clasificar/Carpetas de Descargas`
  y no se aplanan. Un proyecto descomprimido pierde el sentido si lo desmontas,
  así que esas quedan fuera de la clasificación automática, para tu revisión.
- Las **descargas a medias** (`.download`, `.crdownload`, `.part`, `.aria2`) se
  quedan donde están: moverlas rompe la descarga.
- `~/Descargas` **no se borra**, solo queda vacía — el Dock la necesita.

### Seguridad

- **Snapshot APFS** automático antes de tocar nada (vuelta atrás ~24 h por Time Machine).
- **LOG completo** en `Documentos/00 · SISTEMA/LOG.md`: cada borrado, movimiento
  y renombrado, con origen y destino.
- **Protegidos**: carpetas ocultas, `node_modules`, `Library` y paquetes de macOS
  (`.app`, `.pages`, `.key`, `.numbers`, `.rtfd`, `.photoslibrary`, `.logicx`…).
- Solo se borra lo **idéntico byte a byte** y con contenido (>0 bytes).
- **Idempotente**: una segunda pasada sobre carpetas ya limpias no toca nada.
- Colisiones de nombre con contenido distinto se conservan con sufijo `· A-VALIDAR-n`.

### Simulacro

En la cabecera del script, `SIMULACRO=1` hace una pasada en seco: no mueve ni
borra nada, solo escribe en el LOG lo que haría. Por defecto va a `0`, que es la
regla de la casa (borrado directo, ACORDADO 2026-08-08).

## `REGISTRO-drive-99-sin-clasificar-2026-09-15.md`

Registro de la pasada de organización sobre `99 · Sin clasificar` de Google Drive:
25 ficheros de entrada, 24 clasificados leyendo su contenido, 1 pendiente.
Incluye nombre original, nombre nuevo y el porqué de cada movimiento.

## Verificación automática

Dos scripts, que el CI del repositorio ejecuta en cada push sobre **macOS**
—la plataforma donde el organizador se va a pegar de verdad— y que también
puedes lanzar tú:

| Script | Qué comprueba |
|---|---|
| `verificar-sintaxis.sh` | Sintaxis del envoltorio **y del cuerpo**. `bash -n` sobre el fichero solo valida el envoltorio: el cuerpo va dentro de un heredoc entrecomillado y el intérprete no lo mira. Hay que extraerlo y validarlo aparte |
| `probar.sh` | Prueba funcional: ejecuta el script real con `HOME` apuntando a un árbol desechable y comprueba 19 cosas — que el duplicado se borra, que la colisión con contenido distinto se conserva marcada, que `node_modules` y las apps no se arrastran, que un `.pages` sí se mueve entero, que la descarga a medias no se toca, que `~/Descargas` queda vacía pero existe, y que una segunda pasada no cambia nada |

Probar el script solo en Linux daría confianza falsa: usa `stat -f` y `tmutil`,
que son de macOS. Por eso ese trabajo del CI corre en `macos-latest`.
