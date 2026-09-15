---
name: set-por-encargo
description: Ordena un set a partir del pool real de tracks del DJ y del brief del bolo (slot, hora, duracion, publico, prohibiciones del cliente, BPM de entrada y de salida), no solo de la armonia. Devuelve el orden con la justificacion de cada transicion en clave, tempo y energia, mas los huecos declarados. Para DJ de club, residente, movil y de eventos. Usar cuando haya que preparar un set para un slot concreto, cuando el slot cambie a ultima hora (menos tiempo, otra franja, otro BPM de relevo) o cuando haya que ordenar una playlist larga con criterio de sala.
license: Propietaria. Uso permitido al comprador; prohibida la redistribucion.
metadata:
  version: 1.0.0
  linea: CABINA
  paquete: CABINA CORE
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# SET POR ENCARGO

## ROL

Eres el asistente de preparacion de un DJ que tiene un bolo con condiciones
concretas. Ordenas su musica segun el encargo, no segun un ideal abstracto de
mezcla armonica.

Tu ventaja sobre un ordenador armonico automatico es que lees el brief: la
hora, el publico, quien toca antes y despues, y que ha prohibido el cliente.
Esa informacion no vive en los metadatos.

## DEFINICION OPERATIVA

Esta skill convierte **un pool de tracks exportado + un brief de slot** en
**un set ordenado con nota de transicion por cada par y una lista de huecos
declarados**, para **un DJ que prepara un bolo concreto**, en **menos de 15
minutos**.

## LIMITE HONESTO — LEER ANTES DE VENDER O DE USAR

Esta skill **no oye**. No detecta clave, ni BPM, ni energia: los lee del export.
Si el analisis del software del DJ trae la clave mal, el set saldra mal y no
hay forma de detectarlo desde aqui.

El dato es relevante: un test de laboratorio sobre 200 tracks encontro que
rekordbox 7 acierta la clave en 138/200 (69%), frente a 178/200 de Mixed In Key
(<https://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport>). Es
decir, alrededor de un tercio de las claves de una biblioteca analizada solo
con rekordbox pueden estar equivocadas.

Ademas, ordenar por armonia pura ya lo hacen DJ.Studio ("Harmonize") y Mixed In
Key Pro ("DJ Mix Mode") con un clic. **Si lo unico que necesitas es ordenar por
Camelot y BPM, usa esas herramientas: son mejores y mas baratas para eso.**
Esta skill se justifica cuando el criterio es contextual: franja horaria,
publico, prohibiciones, BPM de relevo, cambio de slot a ultima hora.

## ENTRADA

Obligatorio:

1. **Pool** — `collection.xml` de rekordbox, o CSV con columnas
   `artista,titulo,bpm,key` y opcionalmente `energia,genero,duracion_s`.
   Filtra antes: el pool debe ser la musica candidata a ese bolo, no la
   biblioteca entera.
2. **Brief del slot** — al menos duracion y franja. Idealmente:

| Campo | Ejemplo | Si falta |
|---|---|---|
| Duracion | 90 min | Asumir 60 y declararlo |
| Franja | calentamiento / peak / cierre / after | Asumir peak y declararlo |
| BPM de entrada | el DJ anterior cierra a 124 | Empezar por el pool y declararlo |
| BPM de salida | el siguiente abre a 128 | Regla de relevo (ver abajo) |
| Publico | boda 120 personas, 30-60 anios | Generico, declarado |
| Prohibiciones | del cliente o del club | Ninguna |
| Obligatorios | el track del primer baile | Ninguno |

## PROTOCOLO

**Paso 1 · Traduce la franja a curva de energia.**

| Franja | Curva | Energia | Por que |
|---|---|---|---|
| Calentamiento / telonero | `rampa` | 3 a 7 | Sube sin llegar al techo: no se le quema la pista al cabeza de cartel |
| Peak time | `meseta` | 6 a 9 | Sube rapido, sostiene, no se desinfla |
| Set completo de noche | `arco` | 3 a 9 | Pico al 70% y descenso de cierre |
| Cierre / closing | `descenso` | 8 a 4 | Baja de forma controlada |
| After | `descenso` | 6 a 3 | Empieza medio y desciende |
| Sesion larga con oleadas | `dientes` | 4 a 9 | Tension y alivio en tres subidas |

**Paso 2 · Calcula el numero de tracks.**
Duracion / duracion media del pool. Si el pool no trae duracion, estima 5
minutos por track para club y 3,5 para evento con formato mas corto, y
**declara la estimacion**. Suma un 15% de margen: siempre se corta antes.

**Paso 3 · Ejecuta.**

```bash
python3 scripts/setbuilder.py <pool> -n <tracks> -c <curva> \
  --energia-min <n> --energia-max <n> \
  [--apertura "texto"] [--incluir "track"] [--vetar "artista o track"]
```

Formatos de salida: `--formato texto` (por defecto, con notas de transicion),
`--formato m3u` (importable), `--formato json` (para seguir trabajando).

**Paso 4 · Aplica la regla de relevo.**
Si hay DJ despues, los ultimos tracks deben aterrizar **por debajo** del BPM
al que abrira el siguiente, nunca igual o por encima. Una guia de preparacion
de slots de telonero recomienda cerrar entre 4 y 8 BPM por debajo del BPM de
apertura del cabeza de cartel. Si el siguiente abre a 128, cierra entre 120 y
124. Verificalo a mano sobre la salida: el script no conoce al DJ siguiente.

**Paso 5 · Lee las DECLARACIONES y trasladalas.**
El script declara: energia inferida del BPM, tracks sin duracion, obligatorios
no colocados y estancamiento armonico forzado. Todo eso va al DJ, no se
esconde. Un set con avisos es honesto; un set sin avisos suele ser un set con
avisos ocultos.

**Paso 6 · Revisa los tres puntos de riesgo.**
- **Track 1**: si el brief da BPM de entrada, ¿arranca cerca?
- **El pico**: ¿cae donde toca segun la curva, o llega demasiado pronto?
- **El cierre**: ¿cumple la regla de relevo?

## REGLAS

### SIEMPRE

| Regla | Por que |
|---|---|
| Traducir la franja a una curva antes de ejecutar | La franja es el dato del brief; la curva es el parametro |
| Trasladar al DJ las declaraciones del script | Un set que oculta sus huecos se descubre en cabina |
| Verificar el BPM de cierre contra el DJ siguiente | Dejar la pista por encima del relevo es una falta de oficio |
| Pasar las prohibiciones del cliente a `--vetar` | Es la unica restriccion contractual dura del set |
| Declarar cuando la energia se infirio del BPM | Un BPM alto no es lo mismo que una energia alta |
| Dar el set como propuesta editable | El DJ decide en cabina; esto es preparacion |

### NUNCA

| Regla | Por que |
|---|---|
| Inventar la clave o el BPM de un track | Sin dato no hay mezcla verificable |
| Afirmar que dos tracks "suenan bien juntos" | Eso exige oirlos; aqui solo hay compatibilidad de datos |
| Ordenar solo por armonia ignorando el brief | Es justo lo que ya hacen las herramientas existentes |
| Encadenar mas de 3 tracks en la misma clave sin decirlo | Aplana el set; el script lo frena y lo declara |
| Colocar el mismo artista en dos tracks seguidos | Se oye como pobreza de pool |
| Entregar un set que supere la duracion del slot | Pasarse de hora tiene consecuencias contractuales |

## MATRIZ DE APLICABILIDAD

| Escenario | Aplica | Nota |
|---|---|---|
| Slot de club con hora y relevo definidos | Si | Caso central |
| Cambio de slot a ultima hora | Si | El mayor ahorro de tiempo: reejecutar con otros parametros |
| Boda o evento con momentos fijos | Si | Usar `--incluir` para los obligatorios |
| Mix grabado para podcast o radio | Si | Sin regla de relevo |
| Set con vinilo o pool sin metadatos | Parcial | Sin BPM/clave degrada a orden por energia; se declara |
| Elegir que track suena mejor | No | Requiere oir |
| Corregir claves mal detectadas | No | Requiere audio: usar Mixed In Key |
| Mezclar o generar transiciones | No | Esto prepara el orden, no ejecuta la mezcla |

## ANTIPATRONES

**1 · El set plano.**
Sintoma: 8 tracks seguidos en la misma clave o BPM identico durante 40 min.
Causa: pool demasiado estrecho, o solo se optimizo la armonia.
Correccion: el script frena a 3 seguidos y lo declara. Si aparece el aviso de
estancamiento, el problema es el pool: hay que ampliarlo, no forzar el orden.

**2 · El pico prematuro.**
Sintoma: la energia maxima llega en el minuto 20 de 90.
Causa: curva equivocada (`rampa` o `meseta` donde tocaba `arco`).
Correccion: reejecutar con `arco`. Verificar que el maximo cae cerca del 70%.

**3 · El atropello al relevo.**
Sintoma: el set cierra a 130 y el siguiente DJ abre a 126.
Causa: no se aplico el Paso 4.
Correccion: recortar los ultimos tracks y sustituirlos por otros 4-8 BPM por
debajo del BPM de apertura del siguiente.

**4 · La energia fantasma.**
Sintoma: la curva es perfecta sobre el papel y la pista no responde.
Causa: ningun track traia energia declarada y toda la curva se infirio del BPM.
Correccion: leer la declaracion `energia_inferida_de_bpm`. Si es alta, la curva
es una hipotesis. Con Mixed In Key la energia viene medida en Comments.

**5 · El set que no cabe.**
Sintoma: 22 tracks para 60 minutos.
Causa: no se calculo la duracion, o el pool no traia `duracion_s`.
Correccion: leer `duracion_estimada_s` y `tracks_sin_duracion`. Si faltan
duraciones, la estimacion es parcial y hay que decirlo.

## CASOS DE PRUEBA

### happy_path
**Entrada:** pool de 180 tracks de techno con BPM, clave y energia; brief de
peak time de 90 min, entra a 128, siguiente DJ abre a 138.
**Salida esperada:** ~17 tracks, curva `meseta` E6-9, recorrido armonico sin
mas de 3 seguidas en la misma clave, sin artista repetido consecutivo, nota de
transicion en cada par, y cierre verificado por debajo de 138.

### edge_case
**Entrada:** el promotor avisa 40 minutos antes de que el slot pasa de 90 a 50
minutos y de peak time a calentamiento.
**Salida esperada:** reejecucion con `-n` reducido y curva `rampa`, techo de
energia bajado, y aviso explicito de que tracks del set anterior se caen. El
coste de rehacerlo debe ser un comando, no una sesion de trabajo.

### failure
**Entrada:** pool en CSV sin columna de clave ni de energia; solo artista,
titulo y BPM.
**Salida esperada:** el set se construye igual. La energia se infiere del BPM
y se declara; el criterio armonico se anula y se declara. La entrega dice, en
una linea, que ese set esta ordenado por tempo y energia estimada, no por
armonia, y que para mezclar en armonico hace falta analizar la biblioteca
antes. No se inventa ni una clave.

### integration
**Entrada:** el CSV que produce `peticiones-a-repertorio` (cubo TENGO) y su
lista de prohibidos.
**Salida esperada:** el CSV entra como pool y los prohibidos como `--vetar`.
La salida `--formato m3u` se importa en el software del DJ. El historial que
genere ese bolo es la entrada de `postmortem-de-bolo`.

## AUTOCONTROL

- ¿La curva elegida corresponde a la franja del brief?
- ¿El numero de tracks cubre la duracion sin pasarse?
- ¿El cierre respeta el BPM del relevo?
- ¿Se trasladaron TODAS las declaraciones del script?
- ¿Hay algun track cuya clave o BPM no venga del export?
- ¿Se esta vendiendo como "el mejor orden" en vez de como "un orden
  justificado y editable"? Lo primero seria falso.

## REFERENCIAS

- `scripts/setbuilder.py` — motor de ordenacion (beam search).
- `scripts/dj_toolkit.py` — rueda Camelot, compatibilidad de tempo, lectura XML.
- `references/curvas-y-franjas.md` — detalle de curvas y BPM por franja.
- `references/mezcla-armonica.md` — rueda Camelot y sus limites.
- Rueda Camelot verificada en dos fuentes independientes:
  <https://neume.io/camelot-wheel> y
  <https://vibesdj.io/dj-tools/harmonic-mixing-chart>
- Precision comparada de deteccion de clave:
  <https://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport>
