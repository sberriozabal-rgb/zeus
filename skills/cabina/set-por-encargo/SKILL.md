---
name: set-por-encargo
description: Ordena un set a partir del pool real de tracks del DJ y del brief del bolo (slot, hora, duracion, publico, prohibiciones del cliente, BPM de entrada y de salida), no solo de la armonia. Devuelve el orden con la justificacion de cada transicion en clave, tempo y energia, mas los huecos declarados. Para DJ de club, residente, movil y de eventos. Usar cuando haya que preparar un set para un slot concreto, cuando el slot cambie a ultima hora (menos tiempo, otra franja, otro BPM de relevo) o cuando haya que ordenar una playlist larga con criterio de sala.
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso permitido al comprador; prohibida la redistribución. Ver LICENSE.txt.
metadata:
  version: "1.1.0"
  linea: CABINA
  paquete: CABINA CORE
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# set-por-encargo

## Qué hace

Convierte **un pool de tracks exportado más el brief del slot** en **un set ordenado con nota
de transición para cada par y una lista de huecos declarados**, para **un DJ de club,
residente, móvil o de eventos que prepara un bolo concreto**, en **menos de 15 minutos de
atención**.

La ventaja sobre un ordenador armónico automático es que lee el brief: la hora, el público,
quién toca antes y después, y qué ha prohibido el cliente. Esa información no vive en los
metadatos y es la que decide el set de verdad. Ordenar por Camelot y BPM lo hace cualquier
herramienta con un clic; ordenar sabiendo que eres el telonero y que el cabeza de cartel abre
a 128 es otra cosa.

## Cuándo se dispara

- "me han cambiado el slot, ahora tengo 60 minutos en vez de 90"
- "tengo que preparar el set de la boda del sábado"
- "el DJ de antes cierra a 124, ¿por dónde entro?"
- "tengo una playlist de 300 tracks y no sé por dónde empezar a ordenarla"
- "los novios han prohibido reggaetón, ¿cómo lo monto?"
- "soy telonero y no quiero quemarle la pista al cabeza de cartel"
- "necesito que el primer baile caiga en un sitio concreto"
- "me han pasado de peak time a cierre y hay que rehacerlo"
- jerga del gremio: "slot", "relevo", "curva de energía", "peak time", "telonero",
  "Camelot", "rueda armónica", "BPM de entrada", "closing", "after", "pool", "warm up",
  "primer baile", "vetar"

## Quién lo ejecuta

El propio DJ preparando el bolo, con **10 a 15 minutos** de atención: filtrar el pool,
rellenar el brief y revisar los tres puntos de riesgo de la salida. Si el slot cambia a última
hora, la reejecución son **menos de 2 minutos**, que es donde está el mayor ahorro real.

## Entrada

- **Obligatorio · Pool**: `collection.xml` de rekordbox, o CSV con columnas
  `artista,titulo,bpm,key` y opcionalmente `energia,genero,duracion_s`. **Hay que filtrarlo
  antes**: el pool es la música candidata a ese bolo, no la biblioteca entera.
- **Obligatorio · Brief del slot**: al menos duración y franja. Idealmente también BPM de
  entrada y de salida, público, prohibiciones del cliente y tracks obligatorios.
- **Recomendado:** quién toca antes y quién después, con su BPM de cierre y de apertura. Es
  lo que activa la regla de relevo.
- **Opcional:** tracks a vetar por decisión del club o del cliente, y el momento fijo al que
  debe caer un obligatorio (el primer baile, la entrada de los novios).
- **Dato sucio típico:** el pool sin columna de energía, muy habitual en exports de rekordbox.
  El motor la infiere del BPM y **lo declara**, porque un BPM alto no es lo mismo que una
  energía alta: un drum & bass de 174 puede ser atmosférico y un house de 120 puede reventar
  la sala. El segundo dato sucio es el pool sin `duracion_s`, que obliga a estimar el número
  de tracks y también se declara.

## Umbral que sostiene el producto

**Las seis curvas de energía por franja**, que traducen un dato del brief (la franja) en un
parámetro ejecutable (la curva), con su rango y su razón de oficio. Son criterio de la casa
`[A VALIDAR]`, no literatura publicada, y están en `references/curvas-y-franjas.md`.

El segundo umbral sí tiene fuente y es el de relevo: una guía de preparación de slots de
telonero recomienda **cerrar entre 4 y 8 BPM por debajo** del BPM de apertura del cabeza de
cartel. Si el siguiente abre a 128, se cierra entre 120 y 124.

El tercero es el límite de precisión que condiciona todo lo demás: **rekordbox 7 acierta la
clave en 138/200 tracks (69%) frente a 178/200 de Mixed In Key**
(<https://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport>). Alrededor de un
tercio de las claves de una biblioteca analizada solo con rekordbox pueden estar mal, y desde
aquí **no hay forma de detectarlo**. Las distancias armónicas se calculan sobre la rueda
Camelot (<https://neume.io/camelot-wheel>).

## Procedimiento

1. **Entrada: la franja del brief → Acción: traducirla a curva de energía con la tabla de seis
   franjas y fijar el rango mínimo y máximo → Salida: curva y rango como parámetros →
   Si falta la franja: asumir `peak` con meseta 6-9 y declarar el supuesto en la primera línea
   de la entrega.**

2. **Entrada: duración del slot y duración media del pool → Acción: calcular el número de
   tracks y sumar un 15% de margen, porque siempre se corta antes → Salida: número de tracks a
   generar → Si el pool no trae duración: estimar 5 minutos por track en club y 3,5 en evento
   de formato corto, y declarar la estimación.**

3. **Entrada: pool, curva, número de tracks y restricciones → Acción: ejecutar
   `python3 scripts/setbuilder.py <pool> -n <tracks> -c <curva> --energia-min <n>
   --energia-max <n> [--incluir] [--vetar]` → Salida: el set ordenado con nota de transición
   por par → Si un obligatorio no se puede colocar sin romper la curva: el motor lo declara
   y no lo fuerza en silencio.**

4. **Entrada: el set generado y el BPM de apertura del DJ siguiente → Acción: aplicar la regla
   de relevo comprobando a mano que los últimos tracks aterrizan entre 4 y 8 BPM por debajo →
   Salida: cierre verificado o corregido → Si no hay DJ después: se omite la regla y se cierra
   según la curva, declarándolo.**

5. **Entrada: las DECLARACIONES que imprime el motor → Acción: trasladarlas íntegras al DJ
   (energía inferida del BPM, tracks sin duración, obligatorios no colocados, estancamiento
   armónico frenado) → Salida: el set acompañado de sus huecos → Si no hay ninguna
   declaración: se dice explícitamente que no la hay, en vez de callar.**

6. **Entrada: el set completo → Acción: revisar los tres puntos de riesgo —que el track 1
   arranque cerca del BPM de entrada, que el pico caiga donde marca la curva y no antes, y que
   el cierre cumpla el relevo— → Salida: set entregable como propuesta editable → Si alguno
   falla: se reejecuta con parámetros corregidos antes de entregar.**

## Salida

```
SET — [sala / evento], [fecha]
Slot: [duracion] · Franja: [franja] · Curva: [curva] (energia [min]-[max])
BPM entrada: [n]  ->  BPM salida: [n]   Relevo: [n] (cierra 4-8 por debajo)

 #  BPM  KEY  EN  TRACK                          TRANSICION
 1  124  8A   3   Artista - Titulo               entrada cerca del relevo (124)
 2  125  8A   4   Artista - Titulo               misma clave, +1 BPM
 3  126  9A   5   Artista - Titulo               +1 paso Camelot, +1 BPM
...

DECLARACIONES
 - Energia inferida del BPM en 14 de 22 tracks (el pool no trae columna)
 - 3 tracks sin duracion: numero de tracks estimado a 5 min/track
 - Obligatorio "[track]" no colocado: rompia la curva en el minuto 40

## Supuestos de esta versión
[franja asumida, duraciones estimadas, y el aviso de precision de clave]
```

Las seis curvas del paso 1:

| Franja | Curva | Energía | Por qué |
|---|---|---|---|
| Calentamiento / telonero | `rampa` | 3 a 7 | Sube sin llegar al techo: no se le quema la pista al cabeza de cartel |
| Peak time | `meseta` | 6 a 9 | Sube rápido, sostiene, no se desinfla |
| Set completo de noche | `arco` | 3 a 9 | Pico al 70% y descenso de cierre |
| Cierre / closing | `descenso` | 8 a 4 | Baja de forma controlada |
| After | `descenso` | 6 a 3 | Empieza medio y desciende |
| Sesión larga con oleadas | `dientes` | 4 a 9 | Tensión y alivio en tres subidas |

## Límites

- **No oye.** Lee clave, BPM y energía del export; no los detecta. Si el análisis de origen
  trae la clave mal, el set saldrá mal y no hay forma de detectarlo desde aquí.
- No corrige claves mal detectadas: eso exige audio y es trabajo de Mixed In Key.
- No decide qué track suena mejor. Calcula compatibilidad de datos, que no es lo mismo que
  compatibilidad musical.
- No mezcla ni genera transiciones: prepara el orden, no ejecuta nada en cabina.
- Con pool sin BPM ni clave degrada a orden por energía, y lo declara. Con vinilo o pool sin
  metadatos el valor cae mucho.
- Ordenar por armonía pura ya lo hacen DJ.Studio ("Harmonize") y Mixed In Key Pro ("DJ Mix
  Mode") con un clic. **Si lo único que necesitas es ordenar por Camelot y BPM, usa esas: son
  mejores y más baratas para eso.** Esta skill se justifica cuando el criterio es contextual.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Traducir la franja a una curva antes de ejecutar nada | La franja es el dato que da el cliente; la curva es el parámetro que entiende el motor |
| Trasladar al DJ todas las declaraciones del motor | Un set que oculta sus huecos los descubre en cabina, que es el peor sitio |
| Verificar a mano el BPM de cierre contra el DJ siguiente | El motor no conoce al relevo; dejar la pista por encima es una falta de oficio |
| Pasar las prohibiciones del cliente a `--vetar` | Es la única restricción contractual dura del set y su incumplimiento tiene consecuencias |
| Declarar cuando la energía se infirió del BPM | Un BPM alto no es una energía alta: un DnB de 174 puede ser atmosférico |
| Entregar el set como propuesta editable, nunca como orden cerrado | El DJ decide en cabina; esto es preparación, no dirección |
| Filtrar el pool antes de ejecutar | Con la biblioteca entera el motor elige entre ruido y el set pierde criterio |
| Sumar un 15% de margen al número de tracks | Siempre se corta antes: es mejor sobrar que quedarse sin música a falta de diez minutos |
| Revisar los tres puntos de riesgo antes de entregar | Track 1, pico y cierre concentran casi todos los fallos de un set preparado |
| Declarar la estimación cuando el pool no trae duración | El número de tracks cambia el set entero, y es un supuesto que el DJ debe poder corregir |

| NUNCA | Porqué |
|---|---|
| Inventar la clave o el BPM de un track | Sin dato no hay mezcla verificable, y un dato inventado se propaga a todas las transiciones |
| Afirmar que dos tracks "suenan bien juntos" | Eso exige oírlos; aquí solo hay compatibilidad de datos, que es otra cosa |
| Ordenar solo por armonía ignorando el brief | Es exactamente lo que ya hacen las herramientas existentes, mejor y más barato |
| Encadenar más de 3 tracks en la misma clave sin decirlo | Aplana el set; el motor lo frena a 3 y lo declara como estancamiento |
| Colocar el mismo artista en dos tracks seguidos | Se oye como pobreza de pool aunque los dos tracks sean buenos |
| Entregar un set que supere la duración del slot | Pasarse de hora tiene consecuencias contractuales, sobre todo con limitador de sonido |
| Forzar un obligatorio rompiendo la curva sin avisar | El DJ prefiere saber que su track no encaja a descubrir el bajón en directo |
| Dar por buena la clave del export sin el aviso de precisión | Un tercio de las claves analizadas solo con rekordbox pueden estar mal |
| Cerrar por encima del BPM de apertura del relevo | Obliga al siguiente DJ a bajar en frío delante de la pista, y se nota |

## Antipatrones

1. **Síntoma**: 8 tracks seguidos en la misma clave, o BPM idéntico durante 40 minutos.
   **Causa raíz**: pool demasiado estrecho, o se optimizó solo la armonía. **Corrección**: el
   motor frena a 3 seguidos y lo declara; si aparece el aviso de estancamiento el problema es
   el pool y hay que ampliarlo, no forzar el orden.

2. **Síntoma**: la energía máxima llega en el minuto 20 de 90. **Causa raíz**: curva
   equivocada, `rampa` o `meseta` donde tocaba `arco`. **Corrección**: reejecutar con `arco` y
   verificar que el máximo cae cerca del 70% del slot.

3. **Síntoma**: el set cierra a 130 y el DJ siguiente abre a 126. **Causa raíz**: no se aplicó
   la regla de relevo del paso 4. **Corrección**: recortar los dos últimos tracks y aterrizar
   entre 4 y 8 BPM por debajo de 126, es decir entre 118 y 122.

4. **Síntoma**: el track del primer baile aparece en mitad del set, entre dos temas de peak.
   **Causa raíz**: se pasó como `--incluir` sin posición fija y el motor lo colocó donde
   encajaba armónicamente. **Corrección**: los obligatorios con momento fijo se colocan
   primero y el set se construye alrededor; si rompen la curva, se declara y decide el DJ.

5. **Síntoma**: el set es perfecto sobre el papel y en cabina suena deslavazado. **Causa raíz**: se confió en claves de un export analizado solo con rekordbox, con ~31% de error
   esperable. **Corrección**: tratar las transiciones armónicas como propuesta, no como
   garantía, y comprobar de oído las del pico antes del bolo.

## Casos de prueba

Los cuatro casos están en `cases/`, con entrada y salida reales.

**Happy path** (`cases/case_01_happy_path.md`): slot de telonero de 90 minutos, relevo que abre
a 128, pool de 180 tracks con clave y BPM. Sale curva `rampa` 3-7 y cierre a 122.

**Edge case** (`cases/case_02_edge_case.md`): cambio de slot a última hora, de 90 a 50 minutos
y de peak a cierre, a una hora del bolo. Reejecución completa en menos de dos minutos.

**Failure** (`cases/case_03_failure.md`): pool sin clave y sin energía, solo artista, título y
BPM. Se entrega un set ordenado por BPM y energía inferida, con el hueco declarado.

**Integration** (`cases/case_04_integration.md`): encadenado con `postmortem-de-bolo`. Las
decisiones del parte del mes anterior entran como parámetros de este set.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
