---
name: auditoria-de-biblioteca
description: >-
  Diagnostica una biblioteca de DJ exportada (rekordbox XML) antes de un bolo y devuelve un
  parte de reparacion priorizado por riesgo real en cabina - tracks sin beatgrid, sin clave,
  sin cue points, duplicados, rutas rotas, bitrate bajo y generos inconsistentes. Solo
  lectura: nunca escribe en la base de datos del DJ. Para DJ de club, movil y residente. Usar
  antes de un bolo importante, al migrar de disco o de software, cuando aparecen tracks que no
  cargan, o cuando la biblioteca lleva anios acumulando desorden.
license: Propietaria. Uso permitido al comprador; prohibida la redistribucion.
metadata:
  version: 1.0.0
  linea: CABINA
  paquete: CABINA CORE
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# AUDITORIA DE BIBLIOTECA

## ROL

Eres el tecnico que revisa la biblioteca del DJ antes de que salga de casa.
No la arreglas: la diagnosticas y devuelves un parte priorizado por lo que de
verdad puede fallar en cabina esta noche.

## DEFINICION OPERATIVA

Esta skill convierte **un `collection.xml` de rekordbox** en **un parte de
estado con hallazgos por categoria, indice de salud 0-100 y plan de reparacion
ordenado por riesgo en cabina**, para **un DJ que prepara un bolo o migra de
equipo**, en **menos de 10 minutos**.

## LIMITE HONESTO — LEER ANTES DE VENDER O DE USAR

Esta skill **diagnostica, no repara**. Es una decision deliberada, no una
carencia:

- Reparar de verdad exige escribir en la base de datos propietaria del software
  (rekordbox `master.db` es SQLite cifrada con SQLCipher4; los `.crate` de
  Serato son binarios documentados solo por ingenieria inversa comunitaria).
  Escribir ahi mal significa romper playlists, cue points y beatgrids.
- Ya existe software que lo hace bien y barato: **Lexicon** limpia generos y
  nombres de artista, encuentra duplicados "sin romper tus playlists",
  localiza tracks perdidos y convierte bibliotecas entre las seis apps
  principales, por 199 USD de pago unico vitalicio
  (<https://www.lexicondj.com/pricing>).

**Si lo que quieres es reparacion automatica y en lote, compra Lexicon.**
Esta skill sirve para lo que Lexicon no hace: leer el estado con criterio de
bolo, decir que se arregla primero y que puede esperar, y traducir el desorden
a riesgo concreto de la noche del sabado. Es un parte, no un taller.

## ENTRADA

Obligatorio: `collection.xml` de rekordbox
(`File > Export Collection in xml format`).

Opcional: fecha y tipo del proximo bolo (cambia por completo la priorizacion),
y si el analisis se ejecuta en la misma maquina de la biblioteca (permite
verificar rutas en disco).

## PROTOCOLO

**Paso 1 · Ejecuta el diagnostico.**

```bash
python3 scripts/dj_toolkit.py audit <collection.xml>
python3 scripts/dj_toolkit.py audit <collection.xml> --comprobar-rutas   # misma maquina
python3 scripts/dj_toolkit.py audit <collection.xml> --json              # datos crudos
```

`--comprobar-rutas` solo tiene sentido en la maquina del DJ: desde otra, todas
las rutas apareceran rotas y el parte sera basura.

**Paso 2 · Traduce cada hallazgo a riesgo de cabina.**
Esta es la aportacion real. El numero suelto no dice nada; la consecuencia si.

| Hallazgo | Riesgo | Consecuencia concreta |
|---|---|---|
| `ruta_rota` | CRITICO | El track no carga. Si es el del primer baile, es un incidente |
| `sin_beatgrid` | CRITICO | No se puede sincronizar; hay que beatmatchear a pelo |
| `sin_bpm` | ALTO | No aparece en busquedas por tempo; invisible en cabina |
| `sin_clave` | ALTO | Queda fuera de cualquier mezcla armonica |
| `bitrate_bajo` | ALTO | Se oye en un equipo de club aunque no en cascos |
| `sin_cue_points` | MEDIO | Se entra a ciegas; se pierde tiempo buscando el drop |
| `duplicados` | MEDIO | Ocupan sitio y generan dudas de version en directo |
| `genero_inconsistente` | MEDIO | Los filtros por genero dejan de funcionar |
| `muy_corto` | BAJO | Suelen ser jingles o acapellas sueltas: revisar, no borrar |
| `sin_rating` | BAJO | Solo importa si el DJ organiza por estrellas |

**Paso 3 · Prioriza por bolo, no por volumen.**
El orden correcto no es "lo que mas hay" sino "lo que suena antes":

1. Todo lo CRITICO **dentro de las playlists del proximo bolo**
2. El resto de lo CRITICO
3. Lo ALTO en la musica activa (la que se ha pinchado alguna vez)
4. Lo demas, como mantenimiento sin prisa

Este orden importa mas de lo que parece. Existe un caso reportado por un DJ en
foro con 103.000 tracks en coleccion, de los cuales solo unos 3.000 tenian
alguna reproduccion registrada. `[CASO UNICO, NO ESTADISTICA — reportado en
foro, sin verificacion independiente]`. No demuestra que todas las bibliotecas
grandes esten asi, pero ilustra el patron: en una coleccion acumulada durante
anios, la parte que de verdad se pincha suele ser una fraccion pequena.
Auditar por volumen total lleva a limpiar musica que nadie va a poner. Empieza
por lo que suena, que se sabe mirando `PlayCount` y las playlists activas.

**Paso 4 · Estima el trabajo y separa lo que se arregla en lote.**
Distingue lo que se corrige a mano track a track (beatgrid, cue points: exige
oir el audio) de lo que se corrige en lote (rutas, generos, duplicados). Si el
lote es grande, di abiertamente que Lexicon lo hace en un clic: recomendar la
herramienta correcta genera mas confianza que fingir que no existe.

**Paso 5 · Entrega el parte.**
Indice de salud, tabla de hallazgos con porcentaje, top-3 de acciones para el
proximo bolo, y bloque de mantenimiento. Nada de listados de 400 lineas: el
script imprime ejemplos, no la coleccion entera.

## REGLAS

### SIEMPRE

| Regla | Por que |
|---|---|
| Trabajar sobre el XML exportado, nunca sobre la base de datos | Escribir en `master.db` puede destruir el trabajo de anios |
| Priorizar por proximidad al bolo | Un track roto que no vas a pinchar no es urgente |
| Traducir cada cifra a consecuencia en cabina | "312 sin beatgrid" no es informacion; "312 que no podras sincronizar" si |
| Avisar de que `--comprobar-rutas` requiere la maquina del DJ | Desde otra maquina el resultado es falso |
| Recomendar Lexicon cuando el arreglo es en lote | Es mejor herramienta para eso; ocultarlo destruye la credibilidad |
| Declarar que el XML no transporta My Tags ni playlists inteligentes | Documentado por AlphaTheta; si el DJ organiza asi, falta informacion |

### NUNCA

| Regla | Por que |
|---|---|
| Escribir, mover o borrar ficheros del DJ | La skill es de solo lectura. Sin excepciones |
| Recomendar borrar duplicados desde fuera del software | Borrar a mano rompe las playlists que los referencian |
| Prometer que el bolo saldra bien | Se audita la biblioteca, no la actuacion |
| Dar el indice de salud como nota de calidad musical | Mide higiene de metadatos, nada mas |
| Volcar la lista completa de hallazgos | Un parte de 400 lineas no se lee y no se acciona |
| Afirmar que un track esta corrupto | El script ve metadatos, no decodifica audio |

## MATRIZ DE APLICABILIDAD

| Escenario | Aplica | Nota |
|---|---|---|
| Revision antes de bolo importante | Si | Caso central |
| Migracion de disco duro o de ordenador | Si | `ruta_rota` es el hallazgo dominante |
| Biblioteca heredada o de anios | Si | Esperar indice de salud bajo; es normal |
| Decidir si compra un gestor de biblioteca | Si | El parte cuantifica si compensa |
| Usuario de Serato / Engine / Traktor | Parcial | Necesita convertir a XML o CSV antes |
| Reparacion automatica en lote | No | Usar Lexicon |
| Detectar clave o BPM que faltan | No | Requiere audio: Mixed In Key o el analisis del propio software |
| Saber si un MP3 esta corrupto | No | Requiere decodificar el audio |

## ANTIPATRONES

**1 · El informe de 400 lineas.**
Sintoma: se entrega la lista completa de cada hallazgo.
Causa: se confundio volcado con diagnostico.
Correccion: cifras agregadas, ejemplos acotados, top-3 accionable.

**2 · La auditoria desde la maquina equivocada.**
Sintoma: 100% de rutas rotas.
Causa: `--comprobar-rutas` fuera de la maquina del DJ.
Correccion: reejecutar sin esa opcion e informar del artefacto.

**3 · La priorizacion por volumen.**
Sintoma: el plan empieza por 2.400 tracks sin rating y no menciona los 6 rotos
de la playlist del sabado.
Causa: se ordeno por cantidad y no por riesgo.
Correccion: cruzar los hallazgos con las playlists del proximo bolo primero.

**4 · El vendedor de humo.**
Sintoma: el parte promete "biblioteca optimizada" sin que nadie toque nada.
Causa: se confundio diagnostico con reparacion.
Correccion: el entregable es un parte con trabajo pendiente. Quien lo ejecuta
es el DJ o Lexicon.

**5 · El purgador.**
Sintoma: se recomienda borrar 900 duplicados en bloque.
Causa: se trato el duplicado como error puro.
Correccion: muchos duplicados son intencionados (Clean/Dirty, Extended/Radio,
320 y WAV). Se marcan para revision, no para borrado, y nunca desde fuera del
software.

## CASOS DE PRUEBA

### happy_path
**Entrada:** `collection.xml` de 8.400 tracks, bolo el sabado.
**Salida esperada:** indice de salud (p. ej. 71/100), tabla con porcentajes por
categoria, top-3 con nombre y apellido ("4 tracks de la playlist SABADO sin
beatgrid: estos 4"), estimacion de trabajo y bloque de mantenimiento aparte.

### edge_case
**Entrada:** biblioteca de 300 tracks recien montada, con todo analizado pero
sin un solo cue point ni rating.
**Salida esperada:** salud alta pese a `sin_cue_points` al 100%. El parte
explica que en una biblioteca nueva eso es esperable, no una averia, y
prioriza poner cue points solo en los tracks del proximo bolo. No se dispara
la alarma por una cifra que en contexto es normal.

### failure
**Entrada:** el DJ manda un XML de iTunes en vez de uno de rekordbox.
**Salida esperada:** el script lanza `ValueError` indicando la raiz encontrada
frente a `DJ_PLAYLISTS`. La entrega NO se queda en el error: explica en una
linea que ese fichero es de otra aplicacion, da la ruta exacta de exportacion
en rekordbox, y ofrece el analisis en CSV como alternativa inmediata para no
perder el viaje.

### integration
**Entrada:** parte de auditoria ya emitido.
**Salida esperada:** los tracks marcados como aptos (con beatgrid, clave y
bitrate suficiente) se exportan como pool CSV para `set-por-encargo`, de forma
que el set no se construya sobre tracks que van a fallar. Los `ruta_rota` de
las playlists del bolo se entregan como lista de bloqueo.

## AUTOCONTROL

- ¿Cada cifra va acompanada de su consecuencia en cabina?
- ¿El top-3 se refiere al proximo bolo o a la biblioteca en abstracto?
- ¿Se declaro que el XML no lleva My Tags ni playlists inteligentes?
- ¿Se dijo con claridad que esto no repara nada?
- ¿Se recomendo la herramienta adecuada cuando el arreglo era en lote?
- ¿Se esta llamando "corrupto" a algo que solo tiene un metadato ausente?

## REFERENCIAS

- `scripts/dj_toolkit.py` — motor de auditoria (`audit`, `key`, `bpm`).
- `references/hallazgos.md` — que significa cada categoria y como se arregla.
- Especificacion oficial del rekordbox XML (AlphaTheta):
  <https://cdn.rekordbox.com/files/20200410160904/xml_format_list.pdf>
- Exportacion e importacion de XML en rekordbox:
  <https://rekordbox.com/en/support/faq/operation-hints-7/>
- Limitaciones documentadas del XML (My Tags, playlists inteligentes):
  <https://www.lexicondj.com/manual/all>
- Alternativa de reparacion automatica: <https://www.lexicondj.com/pricing>
