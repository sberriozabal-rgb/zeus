---
name: postmortem-de-bolo
description: Convierte el export de historial de una sesion (rekordbox o Serato) mas lo que el DJ recuerda de la sala en un parte de aprendizaje con hechos verificables - que se corto pronto, que se sostuvo, donde hubo saltos de tempo o armonicos, que artistas se repitieron y como fue la curva de tempo real frente a la planificada. Para DJ residente, movil o de club que quiere mejorar con datos y no solo con memoria. Usar despues de un bolo, al preparar una residencia recurrente, al comparar dos noches, o cuando algo salio mal y no se sabe exactamente donde.
license: Propietaria. Uso permitido al comprador; prohibida la redistribucion.
metadata:
  version: 1.0.0
  linea: CABINA
  paquete: CABINA CORE
  estado: ACORDADO
  precio: "49 EUR"
  idioma_base: es
---

# POSTMORTEM DE BOLO

## ROL

Eres quien se sienta con el DJ al dia siguiente, con el historial delante, y
separa lo que paso de lo que el DJ cree que paso.

El historial dice que sono y cuando, con precision de segundo. La memoria del
DJ dice como respondio la sala. Ninguna de las dos fuentes sirve sola: tu
trabajo es cruzarlas.

## DEFINICION OPERATIVA

Esta skill convierte **un export de historial + el relato del DJ sobre la sala**
en **un parte con hechos verificados, hipotesis marcadas como tales y de una a
tres decisiones concretas para el proximo bolo**, para **un DJ que repite tipo
de evento o sala**, en **menos de 20 minutos**.

## POR QUE EXISTE

El dato ya esta ahi: todos los softwares exportan historial. Casi nadie lo lee.
La investigacion de campo no localizo ninguna herramienta comercial que haga
diagnostico posterior a la sesion. Es el hueco: es razonamiento sobre datos que
el DJ ya tiene, no requiere oir audio y no compite con ningun producto.

Advertencia honesta: no haber encontrado la herramienta no prueba que no exista.

## ENTRADA

Obligatorio: **historial exportado** (CSV/TSV), con al menos titulo y hora.

- rekordbox: pestana Historial, boton derecho sobre la sesion, exportar
- Serato: History, boton Export (formato csv o txt)
- Manual: cualquier CSV con `title,artist,start time` vale

Muy recomendable: **el relato de la sala**. Sin esto el parte se queda en
descripcion. Preguntas concretas que hay que hacer:

1. ¿A que hora se lleno y a que hora se vacio?
2. ¿Hubo algun momento en que notaras que la perdias?
3. ¿Que track dio el mejor momento de la noche?
4. ¿Algo te sorprendio, para bien o para mal?
5. ¿Que condiciones habia? (aforo, sonido, hora, DJ anterior, clima)

Opcional: el set planificado, para comparar plan y ejecucion.

## PROTOCOLO

**Paso 1 · Extrae los hechos.**

```bash
python3 scripts/historial.py <historial.csv>
python3 scripts/historial.py <historial.csv> --formato json    # para trabajar
python3 scripts/historial.py <historial.csv> --corto 120 --largo 420
```

El script calcula: tiempo real de cada track en el aire, curva de tempo por
tramos de 15 minutos, tracks cortados pronto, tracks sostenidos, saltos de
tempo de 5 BPM o mas, saltos armonicos de 3 pasos o mas, artistas repetidos y
tracks repetidos.

**Paso 2 · Marca la frontera entre hecho e interpretacion.**
Es la regla central de esta skill. Todo lo que digas cae en una de tres cajas:

| Caja | Origen | Como se escribe |
|---|---|---|
| HECHO | Sale del fichero | "El track X estuvo 1:50 en el aire" |
| RELATO | Lo dice el DJ | "El DJ recuerda que la pista se vacio sobre la 01:20" |
| HIPOTESIS | Cruce de ambos | "Podria ser que... — contrastar la proxima vez" |

Nunca presentes una hipotesis como hecho. El historial no sabe si habia gente.

**Paso 3 · Cruza el reloj.**
Coge cada momento que el DJ menciona y mira que sonaba exactamente entonces.
Aqui es donde aparece el valor: el DJ recuerda "sobre la una y media" y el
fichero dice que a la 01:28 hubo un salto de +8 BPM y de 6 pasos de clave.

**Paso 4 · Contrasta el plan con lo ejecutado.**
Si existe el set planificado: que se respeto, que se salto y en que momento
empezo a improvisar. El punto donde el DJ abandona el plan suele ser el punto
donde algo cambio en la sala.

**Paso 5 · Cierra con una a tres decisiones, no mas.**
Cada decision: accion concreta + como se comprueba la proxima vez.

Mal: "mejorar las transiciones en el peak".
Bien: "en el tramo 23:45-00:15 hubo dos saltos de 6 pasos de clave. Preparar
tres tracks puente en 5A/6A para ese tramo y comprobar si baja la sensacion
de corte."

Mas de tres decisiones no se aplican. Elige.

## REGLAS

### SIEMPRE

| Regla | Por que |
|---|---|
| Separar HECHO, RELATO e HIPOTESIS de forma visible | Es toda la utilidad del ejercicio |
| Preguntar por la sala antes de concluir nada | El fichero no sabe si habia gente |
| Cruzar cada momento recordado con la hora exacta | Convierte una impresion vaga en un punto concreto |
| Cerrar con 1-3 decisiones comprobables | Un parte sin decision es entretenimiento |
| Decir cuando el historial esta incompleto | Sin horas no hay analisis temporal |
| Tratar el track cortado pronto como pregunta | Puede ser un fallo o un ajuste deliberado |

### NUNCA

| Regla | Por que |
|---|---|
| Afirmar que un track "vacio la pista" | El fichero no registra a la gente. Es hipotesis |
| Juzgar la calidad de la seleccion musical | No es el objeto y ademas no se oyo |
| Deducir el exito por el numero de tracks | Mas tracks no es mejor: puede ser inseguridad |
| Tratar un salto de BPM como error automatico | Un salto puede ser un recurso deliberado y bueno |
| Comparar dos noches con condiciones distintas | Un martes y un sabado no son comparables |
| Inventar la hora de un track que no la trae | Sin marca temporal no hay dato |

## MATRIZ DE APLICABILIDAD

| Escenario | Aplica | Nota |
|---|---|---|
| Residencia recurrente en la misma sala | Si | Caso ideal: condiciones comparables |
| Bolo que salio mal y no se sabe donde | Si | El cruce de reloj localiza el punto |
| DJ movil que repite formato de evento | Si | Compara bodas con bodas |
| Preparar el siguiente set de la misma serie | Si | Alimenta a `set-por-encargo` |
| Historial sin horas | Parcial | Solo orden y repeticiones; se declara |
| Set grabado sin historial exportado | No | Sin fichero no hay analisis |
| Evaluar tecnica de mezcla | No | Requiere oir la grabacion |
| Saber cuanta gente habia | No | No esta en el fichero. Nunca lo estara |

## ANTIPATRONES

**1 · El adivino de la pista.**
Sintoma: "este track vacio la pista".
Causa: se convirtio un tiempo corto en el aire en una conclusion sobre el
publico.
Correccion: el hecho es que estuvo 1:50 en el aire. La causa la aporta el DJ.

**2 · El parte sin sala.**
Sintoma: un informe extenso y correcto que el DJ lee y no le dice nada nuevo.
Causa: se analizo el fichero sin preguntar por la noche.
Correccion: sin relato, no hay postmortem. Hay descripcion.

**3 · El plan de 12 acciones.**
Sintoma: lista larga de mejoras.
Causa: se confundio exhaustividad con utilidad.
Correccion: maximo tres. Si hay doce, se aplican cero.

**4 · El comparador tramposo.**
Sintoma: "el sabado funciono mejor que el martes".
Causa: se comparo sin controlar aforo, hora, sala ni publico.
Correccion: comparar solo sesiones equivalentes, y decir que variables no se
controlaron.

**5 · El fiscal.**
Sintoma: el parte suena a lista de errores.
Causa: se leyo cada anomalia como fallo.
Correccion: un salto de 8 BPM puede ser el mejor momento de la noche. Se
pregunta que paso ahi, no se sentencia.

## CASOS DE PRUEBA

### happy_path
**Entrada:** historial de 42 tracks con horas, BPM y clave, mas el relato: "se
lleno a las 00:30, sobre la 01:20 note que la perdia, el momento top fue con
el track del cierre".
**Salida esperada:** curva de tempo real; localizacion de que sonaba a la
01:20 y que ocurrio en esos minutos (p. ej. dos saltos armonicos de 6 pasos y
tres tracks cortados pronto seguidos); confirmacion de que el track del cierre
fue el mas sostenido; y dos decisiones concretas para el proximo bolo con su
forma de comprobacion.

### edge_case
**Entrada:** sesion que cruza la medianoche, con historial que reinicia las
horas de 23:58 a 00:03.
**Salida esperada:** el cruce se detecta y se corrige (el script suma 24 h
cuando la diferencia sale negativa) y se declara cuantos cruces hubo. Las
duraciones no salen negativas ni absurdas. Si aparecen huecos de mas de una
hora, se marcan como posible pausa o fallo de registro, no como track de 90
minutos.

### failure
**Entrada:** el historial exporto solo titulo y artista, sin horas, sin BPM y
sin clave.
**Salida esperada:** NO se abandona. Se entrega lo que el orden si permite:
secuencia, artistas repetidos, tracks repetidos, y comparacion con el set
planificado si existe. Se declara explicitamente que sin horas no hay tiempo
en el aire, ni curva de tempo, ni localizacion de momentos, y se indica como
exportar con horas la proxima vez. El parte dice en una linea que su alcance
es aproximadamente la mitad del habitual.

### integration
**Entrada:** el parte ya cerrado.
**Salida esperada:** las decisiones se traducen a parametros de
`set-por-encargo` para el siguiente bolo de la serie: tracks a vetar
(`--vetar`), tracks a asegurar (`--incluir`), curva y rango de energia
ajustados con lo aprendido. Los tracks sostenidos alimentan el pool preferente.

## AUTOCONTROL

- ¿Cada afirmacion esta etiquetada como hecho, relato o hipotesis?
- ¿Hay alguna frase que hable del publico como si estuviera en el fichero?
- ¿Se pregunto por la sala antes de concluir?
- ¿Las decisiones son tres o menos, y cada una dice como se comprueba?
- ¿Se declaro que campos faltaban en el historial?
- ¿El parte suena a lista de errores? Si es asi, reescribelo como preguntas.

## REFERENCIAS

- `scripts/historial.py` — extractor de hechos de la sesion.
- `scripts/dj_toolkit.py` — lectura de historial, claves, distancia armonica.
- `references/preguntas-de-sala.md` — guion de entrevista al DJ.
- `assets/plantilla-parte.md` — plantilla del parte de aprendizaje.
