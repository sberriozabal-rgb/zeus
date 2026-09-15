---
name: postmortem-de-bolo
description: Convierte el export de historial de una sesion (rekordbox o Serato) mas lo que el DJ recuerda de la sala en un parte de aprendizaje con hechos verificables - que se corto pronto, que se sostuvo, donde hubo saltos de tempo o armonicos, que artistas se repitieron y como fue la curva de tempo real frente a la planificada. Para DJ residente, movil o de club que quiere mejorar con datos y no solo con memoria. Usar despues de un bolo, al preparar una residencia recurrente, al comparar dos noches, o cuando algo salio mal y no se sabe exactamente donde.
license: Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Uso permitido al comprador; prohibida la redistribución. Ver LICENSE.txt.
metadata:
  version: "1.1.0"
  linea: CABINA
  paquete: CABINA CORE
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# postmortem-de-bolo

## Qué hace

Convierte **un export de historial de sesión (rekordbox o Serato) más el relato del DJ sobre
la sala** en **un parte de aprendizaje con los hechos verificables separados de las hipótesis,
y de una a tres decisiones concretas para el próximo bolo**, para **un DJ residente, móvil o
de club que repite tipo de evento o sala**, en **menos de 20 minutos de atención**.

El dato ya está ahí: todos los softwares exportan historial y casi nadie lo lee. Lo que esta
skill aporta no es leerlo, sino cruzarlo con la memoria de la noche y marcar con precisión
dónde acaba el hecho y dónde empieza la interpretación. El historial dice qué sonó y cuándo,
con precisión de segundo. El DJ dice cómo respondió la sala. Ninguna de las dos fuentes sirve
sola, y confundirlas es el error que convierte un postmortem en una superstición.

## Cuándo se dispara

- "el sábado se me cayó la pista y no sé en qué momento"
- "quiero preparar la residencia del mes que viene mirando lo que pasó"
- "¿por qué funcionó mejor una noche que otra?"
- "creo que repetí artistas sin darme cuenta"
- "noté que la perdía sobre la una y media pero no sé qué puse"
- "quiero comparar las dos últimas bodas"
- "el cierre salió redondo, ¿qué hice distinto?"
- "me dijeron que hubo un bajón y no lo vi venir"
- jerga del gremio: "historial", "history", "curva de tempo", "peak time", "se cayó la
  pista", "salto armónico", "Camelot", "track cortado", "tiempo en el aire", "relevo",
  "sesión", "residencia", "set planificado"

## Quién lo ejecuta

El propio DJ, al día siguiente del bolo o en los días posteriores, con **15 a 20 minutos** de
atención: exportar el historial, responder a las cinco preguntas de sala y leer el parte. Se
puede hacer acompañado, y funciona mejor así, pero no lo exige.

## Entrada

- **Obligatorio:** historial exportado en CSV o TSV, con al menos título y hora. En rekordbox
  está en la pestaña Historial, botón derecho sobre la sesión, exportar. En Serato, en
  History, botón Export (csv o txt). Cualquier CSV con `title,artist,start time` vale.
- **Muy recomendable:** el relato de la sala, que se obtiene con las cinco preguntas de
  `references/preguntas-de-sala.md`: a qué hora se llenó y se vació, si hubo algún momento de
  pérdida, cuál fue el mejor momento, qué sorprendió, y en qué condiciones se tocó.
- **Opcional:** el set planificado, para contrastar plan contra ejecución. El punto donde el
  DJ abandona el plan suele ser el punto donde algo cambió en la sala.
- **Opcional:** el historial de una sesión equivalente anterior, para comparar.
- **Dato sucio típico:** el historial que cruza la medianoche y reinicia las horas de 23:58 a
  00:03, lo que produce duraciones negativas. El script lo detecta y suma 24 h cuando la
  diferencia sale negativa, y declara cuántos cruces hubo. El segundo dato sucio habitual es
  el export sin columna de hora, que reduce el parte a secuencia y repeticiones: se entrega
  igual y se declara que el alcance es aproximadamente la mitad.

## Umbral que sostiene el producto

**La frontera de tres cajas entre HECHO, RELATO e HIPÓTESIS.** Es el umbral de método, no de
cifra, y es lo que separa esta skill de una charla de bar: cada afirmación del parte lleva su
origen marcado, y una hipótesis jamás se escribe como hecho.

Los umbrales numéricos que usa el motor son **criterio de oficio de la casa, sin fuente
externa** `[A VALIDAR]`: track cortado pronto por debajo de **120 segundos** en el aire,
track sostenido por encima de **420 segundos**, salto de tempo relevante a partir de **5 BPM**,
y salto armónico relevante a partir de **3 pasos** en la rueda Camelot. Son configurables con
`--corto` y `--largo` precisamente porque no son leyes: un DJ de techno y uno de bodas no
comparten esas fronteras.

Sobre la clave, un aviso que viaja con el dato: la que trae el historial es la que calculó el
software, y su acierto no es total —hay un test de 200 tracks que da 69% a rekordbox 7 frente
a 89% de Mixed In Key (<https://www.mixedinkey.com/>)—, así que un salto armónico detectado
se trata como pregunta, no como sentencia.

**Advertencia honesta que va en el producto:** la investigación de campo no localizó ninguna
herramienta comercial que haga diagnóstico posterior a la sesión. No haber encontrado la
herramienta no prueba que no exista.

## Procedimiento

1. **Entrada: el historial exportado → Acción: ejecutar `python3 scripts/historial.py
   <historial.csv>` para extraer tiempo real en el aire, curva de tempo por tramos de 15
   minutos, tracks cortados y sostenidos, saltos de tempo y armónicos, y repeticiones →
   Salida: la tabla de hechos del fichero → Si el historial no trae horas: se extraen solo
   secuencia y repeticiones, y el parte declara en su primera línea que su alcance es
   aproximadamente la mitad del habitual.**

2. **Entrada: la tabla de hechos → Acción: preguntar al DJ las cinco preguntas de sala de
   `references/preguntas-de-sala.md` antes de interpretar nada → Salida: el relato de la
   noche, con horas aproximadas → Si el DJ no aporta relato: no se entrega un postmortem, se
   entrega una descripción, y se dice con esa palabra.**

3. **Entrada: hechos y relato → Acción: clasificar cada afirmación en una de las tres cajas
   (HECHO del fichero, RELATO del DJ, HIPÓTESIS del cruce) y etiquetarla de forma visible →
   Salida: el cuerpo del parte con cada línea marcada → Si una afirmación no encaja en
   ninguna caja: se elimina, porque es opinión.**

4. **Entrada: cada momento que el DJ menciona → Acción: cruzar el reloj y mirar qué sonaba
   exactamente entonces y qué ocurrió en esos minutos → Salida: los momentos vagos
   convertidos en puntos concretos con hora y track → Si el recuerdo del DJ es impreciso: se
   abre una ventana de ±10 minutos y se declara la ventana en vez de forzar un instante.**

5. **Entrada: el set planificado, si existe → Acción: contrastar qué se respetó, qué se saltó
   y en qué momento empezó la improvisación → Salida: el punto de abandono del plan, que
   suele coincidir con un cambio en la sala → Si no hay set planificado: se omite el apartado
   y se sugiere guardarlo la próxima vez.**

6. **Entrada: todo lo anterior → Acción: cerrar con entre una y tres decisiones, cada una con
   su acción concreta y su forma de comprobación en el próximo bolo → Salida: el parte
   completo → Si salen más de tres decisiones: se eligen las tres de mayor impacto, porque
   una lista de doce se aplica cero veces.**

## Salida

```markdown
# Parte de bolo — [Sala / evento], [fecha]
[N tracks] · [duración] · [condiciones: aforo, hora, DJ anterior]

## Hechos del fichero
[tabla: track · hora · tiempo en el aire · BPM · clave]
Curva de tempo por tramos de 15 min: [...]

## Lo que cuenta el DJ
[RELATO, con sus horas aproximadas]

## El cruce del reloj
[HIPÓTESIS marcadas: "a la 01:28 hubo un salto de +8 BPM y 6 pasos de clave,
 y el DJ sitúa ahí la pérdida. Podría estar relacionado — contrastar."]

## Decisiones para el próximo (máximo 3)
1. [acción concreta] — se comprueba: [cómo]

## Supuestos de esta versión
[qué campos faltaban, qué ventanas se abrieron, qué no se pudo cruzar]
```

Las tres cajas que sostienen el paso 3:

| Caja | Origen | Cómo se escribe |
|---|---|---|
| HECHO | Sale del fichero | "El track X estuvo 1:50 en el aire" |
| RELATO | Lo dice el DJ | "El DJ recuerda que la pista se vació sobre la 01:20" |
| HIPÓTESIS | Cruce de ambos | "Podría ser que… — contrastar la próxima vez" |

## Límites

- **El fichero no sabe si había gente.** No hay forma de saber cuánta gente había ni cómo
  respondió: eso lo aporta el DJ o no existe en el parte.
- No evalúa técnica de mezcla ni calidad de la selección musical: eso exigiría oír la
  grabación, y esta skill no oye.
- Sin historial exportado no hay análisis. Un set grabado en audio no sirve de entrada.
- Sin horas en el export, el parte pierde tiempo en el aire, curva de tempo y localización de
  momentos, que es aproximadamente la mitad de su valor.
- No compara sesiones con condiciones distintas. Un martes y un sábado no son comparables, y
  forzar la comparación produce conclusiones falsas.
- La clave que analiza es la que calculó el software del DJ, con su margen de error conocido.
  Un salto armónico detectado es una pregunta, no una sentencia.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Separar HECHO, RELATO e HIPÓTESIS de forma visible en cada línea | Es toda la utilidad del ejercicio; sin esa frontera el parte es una superstición con tablas |
| Preguntar por la sala antes de concluir nada | El fichero no registra al público, y sin relato no hay postmortem sino descripción |
| Cruzar cada momento recordado con la hora exacta del fichero | Convierte "sobre la una y media" en "a la 01:28", que es donde aparece el valor |
| Cerrar con entre una y tres decisiones comprobables | Un parte sin decisión es entretenimiento, y más de tres no se aplican |
| Declarar qué campos faltaban en el historial | El DJ debe saber qué parte del análisis no se pudo hacer y por qué |
| Tratar el track cortado pronto como pregunta, no como fallo | Puede ser un error de lectura de sala o un ajuste deliberado y bueno |
| Abrir una ventana temporal cuando el recuerdo es impreciso | Forzar un instante exacto sobre un recuerdo vago fabrica una causa que no existe |
| Corregir el cruce de medianoche sumando 24 h y declarar cuántos hubo | Sin la corrección aparecen duraciones negativas que invalidan la curva entera |
| Contrastar el plan con lo ejecutado cuando exista el set planificado | El punto de abandono del plan suele ser el punto donde cambió la sala |
| Reescribir como preguntas cualquier apartado que suene a lista de errores | Un parte que suena a expediente se lee una vez y no se vuelve a pedir |

| NUNCA | Porqué |
|---|---|
| Afirmar que un track "vació la pista" | El fichero no registra a la gente. Es hipótesis, y presentarla como hecho es el fallo central del oficio |
| Juzgar la calidad de la selección musical | No es el objeto de la skill y además no se oyó la sesión |
| Deducir el éxito por el número de tracks pinchados | Más tracks no es mejor: puede ser inseguridad o pista que no arranca |
| Tratar un salto de BPM como error automático | Un salto de 8 BPM puede ser el mejor momento de la noche; se pregunta qué pasó ahí |
| Comparar dos noches con condiciones distintas | Aforo, hora, sala, público y DJ anterior cambian el resultado más que cualquier decisión de track |
| Inventar la hora de un track que no la trae | Sin marca temporal no hay dato, y una hora estimada contamina la curva entera |
| Presentar una hipótesis sin su etiqueta | En cuanto una hipótesis pierde la etiqueta se convierte en creencia, y el DJ la arrastra bolos |
| Entregar más de tres decisiones | Es la diferencia entre un parte que se aplica y una lista que se archiva |
| Concluir sobre el público a partir del tiempo en el aire | El tiempo en el aire es una decisión del DJ, no una medición de la pista |

## Antipatrones

1. **Síntoma**: el parte afirma que "este track vació la pista". **Causa raíz**: se convirtió
   un tiempo corto en el aire en una conclusión sobre el público. **Corrección**: el hecho es
   que estuvo 1:50 en el aire; la causa la aporta el DJ, y si no la aporta queda como
   hipótesis etiquetada.

2. **Síntoma**: un informe extenso y correcto que el DJ lee y no le dice nada que no supiera.
   **Causa raíz**: se analizó el fichero sin preguntar por la noche. **Corrección**: sin
   relato no hay postmortem; se para y se hacen las cinco preguntas de sala antes de escribir
   una línea de interpretación.

3. **Síntoma**: el parte cierra con una lista de doce mejoras. **Causa raíz**: se confundió
   exhaustividad con utilidad. **Corrección**: máximo tres decisiones, elegidas por impacto.
   Si hay doce, se aplican cero.

4. **Síntoma**: "el sábado funcionó mejor que el martes". **Causa raíz**: se comparó sin
   controlar aforo, hora, sala ni público. **Corrección**: comparar solo sesiones
   equivalentes y declarar explícitamente qué variables no se controlaron.

5. **Síntoma**: el parte entero suena a expediente disciplinario. **Causa raíz**: se leyó cada
   anomalía del fichero como un fallo. **Corrección**: reescribir las anomalías como
   preguntas abiertas —"a la 01:28 hay un salto de 8 BPM, ¿qué pasó ahí?"— porque puede haber
   sido el mejor momento de la noche.

## Casos de prueba

Los cuatro casos están en `cases/`, con entrada y salida reales.

**Happy path** (`cases/case_01_happy_path.md`): historial de 42 tracks con horas, BPM y clave,
más el relato completo. El cruce del reloj localiza qué sonaba en el momento de pérdida que
el DJ recuerda y cierra con dos decisiones comprobables.

**Edge case** (`cases/case_02_edge_case.md`): sesión que cruza la medianoche con las horas
reiniciadas. Se detecta el cruce, se corrige sumando 24 h y se declara, en vez de producir
duraciones negativas.

**Failure** (`cases/case_03_failure.md`): export sin horas, sin BPM y sin clave. Se entrega lo
que el orden sí permite —secuencia, artistas repetidos, contraste con el plan— con los
supuestos declarados y la instrucción de cómo exportar con horas la próxima vez.

**Integration** (`cases/case_04_integration.md`): encadenado con `set-por-encargo`. Las
decisiones del parte se traducen a parámetros del siguiente set de la serie: tracks a vetar,
tracks a asegurar, y curva de energía ajustada con lo aprendido.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
