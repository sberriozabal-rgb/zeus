---
name: auditoria-de-biblioteca
description: >-
  Diagnostica una biblioteca de DJ exportada (rekordbox XML) antes de un bolo y devuelve un
  parte de reparacion priorizado por riesgo real en cabina - tracks sin beatgrid, sin clave,
  sin cue points, duplicados, rutas rotas, bitrate bajo y generos inconsistentes. Solo
  lectura: nunca escribe en la base de datos del DJ. Para DJ de club, movil y residente. Usar
  antes de un bolo importante, al migrar de disco o de software, cuando aparecen tracks que no
  cargan, o cuando la biblioteca lleva anios acumulando desorden.
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso permitido al comprador; prohibida la redistribución. Ver LICENSE.txt.
metadata:
  version: "1.1.0"
  linea: CABINA
  paquete: CABINA CORE
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# auditoria-de-biblioteca

## Qué hace

Convierte **un `collection.xml` exportado de rekordbox** en **un parte de estado con los
hallazgos agrupados por categoría, un índice de salud de 0 a 100 y un plan de reparación
ordenado por riesgo real en cabina**, para **un DJ de club, móvil o residente que prepara un
bolo o migra de equipo**, en **menos de 10 minutos de atención**.

No es un limpiador de bibliotecas. Es el técnico que revisa el material antes de que salgas
de casa y te dice qué se arregla primero, qué puede esperar y qué no vas a poder arreglar a
tiempo. La aportación no es contar defectos —eso lo hace cualquier script— sino traducir
cada cifra a la consecuencia concreta de la noche del sábado, y ordenar el trabajo por
proximidad al bolo en lugar de por volumen.

## Cuándo se dispara

- "se me quedó un track sin cargar en medio del set"
- "he cambiado de disco duro y ahora me salen exclamaciones por todos lados"
- "voy a pasar de Serato a rekordbox y no sé cómo está la colección"
- "tengo un bolo importante el sábado y quiero revisar la música antes"
- "llevo diez años metiendo música y aquello es un cementerio"
- "¿me compro Lexicon o no me hace falta?"
- "no me aparecen tracks cuando filtro por BPM"
- "¿cuántos duplicados tengo realmente?"
- jerga del gremio: "beatgrid", "cue points", "rutas rotas", "track not found", "collection
  xml", "analizar la biblioteca", "Camelot", "bitrate", "My Tags", "playlist inteligente",
  "relocalizar", "colección", "crate"

## Quién lo ejecuta

El propio DJ, sin intermediarios, con **10 a 15 minutos** de atención disponible: el tiempo
de exportar el XML, lanzar el script y leer el parte. La reparación posterior no está en ese
tiempo y se estima aparte, porque puede ir de veinte minutos a varias tardes.

## Entrada

- **Obligatorio:** `collection.xml` de rekordbox, exportado con
  `File > Export Collection in xml format`.
- **Recomendado:** fecha y tipo del próximo bolo. Cambia por completo la priorización: sin
  ella el parte ordena por riesgo genérico, con ella ordena por lo que suena antes.
- **Recomendado:** si el análisis se ejecuta en la misma máquina donde vive la biblioteca,
  porque solo ahí tiene sentido comprobar rutas en disco.
- **Opcional:** nombre de las playlists del bolo, para cruzar los hallazgos contra ellas.
- **Dato sucio típico:** el XML exportado desde otra máquina, o una copia antigua del
  fichero. Se detecta porque las rutas apuntan a un volumen que no existe y el porcentaje de
  `ruta_rota` se dispara al 100%. Cuando eso ocurre no se entrega el parte de rutas: se
  declara el artefacto y se reejecuta sin `--comprobar-rutas`.

## Umbral que sostiene el producto

**La proporción de biblioteca que de verdad se pincha.** Auditar por volumen total lleva a
limpiar música que nadie va a poner nunca. Hay un caso reportado por un DJ en foro con
103.000 tracks en colección de los cuales solo unos 3.000 tenían alguna reproducción
registrada `[CASO ÚNICO, NO ESTADÍSTICA — reportado en foro, sin verificación
independiente]`. No demuestra nada sobre el conjunto del oficio, pero marca el criterio: se
empieza por lo que suena, que se sabe mirando `PlayCount` y las playlists activas.

El segundo umbral es de precisión y sí tiene fuente: un test de laboratorio sobre 200 tracks
dio **69% de acierto de clave a rekordbox 7 frente a 89% de Mixed In Key**
(<https://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport>). Por eso `sin_clave`
se marca como ALTO pero la clave *presente* nunca se da por buena sin avisar.

El tercer umbral es de decisión de compra: **199 USD de pago único vitalicio** es lo que
cuesta Lexicon (<https://www.lexicondj.com/pricing>), que sí repara en lote. El parte
cuantifica si compensa.

## Procedimiento

1. **Entrada: el `collection.xml` y la fecha del bolo → Acción: ejecutar
   `python3 scripts/dj_toolkit.py audit <collection.xml>`, añadiendo `--comprobar-rutas` solo
   si se está en la máquina del DJ → Salida: conteo bruto de hallazgos por categoría e índice
   de salud → Si falta la fecha del bolo: se ejecuta igual y el parte se ordena por riesgo
   genérico, declarando que la priorización no está cruzada con playlists.**

2. **Entrada: el conteo bruto → Acción: traducir cada hallazgo a su consecuencia en cabina
   con la tabla de riesgo de abajo → Salida: cada categoría con su nivel CRÍTICO/ALTO/MEDIO/
   BAJO y la frase de consecuencia → Si aparece una categoría que no está en la tabla: se
   reporta como observación sin nivel asignado y no se prioriza.**

3. **Entrada: hallazgos con nivel → Acción: cruzarlos contra las playlists del próximo bolo y
   contra `PlayCount` para separar música activa de archivo → Salida: los hallazgos partidos
   en cuatro bloques de prioridad → Si no hay playlists del bolo identificadas: se usa
   `PlayCount > 0` como sustituto de "música activa" y se declara el sustituto.**

4. **Entrada: los bloques priorizados → Acción: separar lo que se arregla en lote (rutas,
   géneros, duplicados) de lo que exige oír el audio track a track (beatgrid, cue points) →
   Salida: estimación de trabajo en dos columnas, lote y manual → Si el lote es grande: se
   dice abiertamente que Lexicon lo hace en un clic por 199 USD, con su URL.**

5. **Entrada: todo lo anterior → Acción: montar el parte con índice de salud, tabla de
   hallazgos con porcentaje, top-3 de acciones para el próximo bolo y bloque de mantenimiento
   aparte → Salida: el parte completo, con ejemplos acotados y nunca el volcado entero →
   Si el número de hallazgos de una categoría supera los 20: se imprimen 5 ejemplos y el
   recuento, jamás la lista completa.**

6. **Entrada: el parte montado → Acción: pasar las tres verificaciones (que ninguna
   recomendación implique escribir en la base de datos, que el porcentaje de rutas rotas no
   sea un artefacto de máquina equivocada, y que cada cifra lleve su consecuencia) → Salida:
   parte verificado → Si alguna verificación falla: se corrige antes de entregar y se anota
   en los supuestos.**

## Salida

```markdown
# Parte de biblioteca — [Nombre del DJ]
[Fecha] · [N tracks] · Próximo bolo: [fecha y tipo]

## Índice de salud: [N]/100

## Hallazgos
| Categoría | N | % | Riesgo | Consecuencia en cabina |
|---|---|---|---|---|

## Top 3 para el bolo del [fecha]
1. [acción con nombre y apellido: "4 tracks de la playlist SABADO sin beatgrid: estos 4"]

## Mantenimiento sin prisa
[lo que puede esperar, con estimación de trabajo]

## Supuestos de esta versión
[qué se asumió, qué no se pudo comprobar y por qué]
```

La tabla de traducción que sostiene el paso 2:

| Hallazgo | Riesgo | Consecuencia concreta |
|---|---|---|
| `ruta_rota` | CRÍTICO | El track no carga. Si es el del primer baile, es un incidente |
| `sin_beatgrid` | CRÍTICO | No se puede sincronizar; hay que beatmatchear a pelo |
| `sin_bpm` | ALTO | No aparece en búsquedas por tempo; invisible en cabina |
| `sin_clave` | ALTO | Queda fuera de cualquier mezcla armónica |
| `bitrate_bajo` | ALTO | Se oye en un equipo de club aunque no en cascos |
| `sin_cue_points` | MEDIO | Se entra a ciegas; se pierde tiempo buscando el drop |
| `duplicados` | MEDIO | Ocupan sitio y generan dudas de versión en directo |
| `genero_inconsistente` | MEDIO | Los filtros por género dejan de funcionar |
| `muy_corto` | BAJO | Suelen ser jingles o acapellas sueltas: revisar, no borrar |
| `sin_rating` | BAJO | Solo importa si el DJ organiza por estrellas |

## Límites

- **Diagnostica, no repara.** Es decisión deliberada: reparar exige escribir en la base de
  datos propietaria (rekordbox `master.db` es SQLite cifrada con SQLCipher4; los `.crate` de
  Serato son binarios documentados solo por ingeniería inversa comunitaria) y hacerlo mal
  rompe playlists, cue points y beatgrids.
- No detecta clave ni BPM que falten: eso exige decodificar el audio. Lo hace el análisis del
  propio software o Mixed In Key.
- No sabe si un MP3 está corrupto. Ve metadatos, no decodifica.
- No transporta My Tags ni playlists inteligentes: el XML de rekordbox no los incluye, está
  documentado por AlphaTheta (<https://rekordbox.com/>), y si el DJ organiza así le falta
  información en el parte.
- Con Serato, Engine o Traktor solo funciona tras convertir a XML o CSV
  (<https://serato.com/>).
- El índice de salud mide higiene de metadatos. No es una nota de calidad musical ni predice
  cómo saldrá la noche.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Trabajar sobre el XML exportado, nunca sobre la base de datos | Escribir en `master.db` puede destruir el trabajo de años y no hay deshacer |
| Priorizar por proximidad al bolo, no por volumen | Un track roto que no vas a pinchar el sábado no es urgente, y el que sí vas a pinchar es un incidente |
| Traducir cada cifra a consecuencia en cabina | "312 sin beatgrid" no es información; "312 que no podrás sincronizar" sí |
| Avisar de que `--comprobar-rutas` requiere la máquina del DJ | Desde otra máquina todas las rutas salen rotas y el parte entero es basura |
| Recomendar Lexicon cuando el arreglo es en lote | Es mejor herramienta para eso; ocultarlo para parecer imprescindible destruye la credibilidad |
| Declarar que el XML no transporta My Tags ni playlists inteligentes | Está documentado por AlphaTheta; si el DJ organiza así, el parte tiene un hueco y debe saberlo |
| Separar el trabajo de lote del que exige oír el audio | Son dos tipos de tarea con coste de tiempo distinto; mezclarlos hace inútil la estimación |
| Acotar los ejemplos a cinco por categoría y dar el recuento | Un parte de 400 líneas no se lee, y lo que no se lee no se acciona |
| Cruzar los hallazgos con `PlayCount` cuando no hay playlists del bolo | Es el mejor sustituto disponible para separar música viva de archivo muerto |
| Declarar en los supuestos todo lo que no se pudo comprobar | El DJ tiene que saber qué parte del parte es medición y qué parte es inferencia |

| NUNCA | Porqué |
|---|---|
| Escribir, mover o borrar ficheros del DJ | La skill es de solo lectura. Sin excepciones y sin "solo esta vez" |
| Recomendar borrar duplicados desde fuera del software | Borrar a mano rompe las playlists que los referencian, y el DJ lo descubre en cabina |
| Tratar todo duplicado como error | Muchos son intencionados: Clean/Dirty, Extended/Radio, 320 y WAV. Se marcan para revisión, nunca para borrado |
| Prometer que el bolo saldrá bien | Se audita la biblioteca, no la actuación. Prometer resultado es vender humo |
| Dar el índice de salud como nota de calidad musical | Mide higiene de metadatos y nada más; leerlo como juicio artístico es un malentendido caro |
| Volcar la lista completa de hallazgos | Confunde volcado con diagnóstico y convierte el entregable en ruido |
| Afirmar que un track está corrupto | El script ve metadatos, no decodifica audio. No puede saberlo |
| Dar por buena una clave presente sin advertir de su precisión | rekordbox 7 acierta el 69% según el test citado: una clave presente no es una clave correcta |
| Entregar el parte de rutas cuando se ejecutó desde otra máquina | El 100% de rutas rotas es un artefacto, y presentarlo como hallazgo es un error que se ve a la legua |

## Antipatrones

1. **Síntoma**: se entrega la lista completa de cada hallazgo, 400 líneas. **Causa raíz**: se
   confundió volcado con diagnóstico. **Corrección**: cifras agregadas, cinco ejemplos por
   categoría como máximo, y un top-3 accionable con nombre y apellido.

2. **Síntoma**: el parte dice 100% de rutas rotas y el DJ entra en pánico. **Causa raíz**: se
   ejecutó `--comprobar-rutas` fuera de la máquina del DJ. **Corrección**: reejecutar sin esa
   opción, informar del artefacto y no incluir rutas en el plan hasta poder comprobarlas.

3. **Síntoma**: el plan empieza por 2.400 tracks sin rating y no menciona los 6 rotos de la
   playlist del sábado. **Causa raíz**: se ordenó por cantidad en vez de por riesgo y
   proximidad al bolo. **Corrección**: cruzar los hallazgos con las playlists del próximo
   bolo antes de ordenar nada.

4. **Síntoma**: el parte promete "biblioteca optimizada" sin que nadie haya tocado nada.
   **Causa raíz**: se confundió diagnóstico con reparación. **Corrección**: el entregable es
   un parte con trabajo pendiente; quien lo ejecuta es el DJ o Lexicon, y eso se dice.

5. **Síntoma**: se recomienda borrar 900 duplicados en bloque. **Causa raíz**: se trató el
   duplicado como error puro sin mirar por qué existe. **Corrección**: marcar para revisión
   distinguiendo versiones deliberadas (Clean/Dirty, Extended/Radio, 320/WAV) del duplicado
   accidental, y nunca borrar desde fuera del software.

## Casos de prueba

Los cuatro casos están en `cases/`, con entrada real y salida esperada.

**Happy path** (`cases/case_01_happy_path.md`): colección de 8.400 tracks, bolo el sábado,
playlists identificadas. Sale índice de salud 71/100 y un top-3 que empieza por los 4 tracks
de la playlist del bolo sin beatgrid.

**Edge case** (`cases/case_02_edge_case.md`): biblioteca de 300 tracks recién montada, todo
analizado pero sin un solo cue point ni rating. Salud alta pese a `sin_cue_points` al 100%:
el caso que enseña que un porcentaje alto no es automáticamente un problema.

**Failure** (`cases/case_03_failure.md`): XML exportado desde otra máquina, 100% de rutas
rotas. Se entrega el parte de todo lo demás con los supuestos declarados, en vez de rendirse.

**Integration** (`cases/case_04_integration.md`): encadenado con `set-por-encargo`. Los
tracks sin clave que detecta esta auditoría son exactamente los que quedan fuera del set
armónico, y se cuantifica cuánto pool pierde el DJ por ese hueco.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
