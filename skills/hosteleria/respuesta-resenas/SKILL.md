---
name: respuesta-resenas
description: >-
  Redacta respuestas a reseñas de Google/TripAdvisor con el criterio de un dueño de
  restaurante, no de un bot genérico, y detecta patrones repetidos en las reseñas
  negativas que señalan un problema operativo real (no solo un cliente difícil). Úsala
  siempre que aparezca una reseña, un export de reseñas de Google o TripAdvisor, una
  captura de una opinión negativa, o cuando alguien pregunte cómo responder a una reseña
  mala, por qué le están bajando las estrellas, qué hacer con un cliente que se quejó en
  internet, cómo conseguir más reseñas buenas, o pida un análisis de las últimas
  opiniones. Aplica también con frases del oficio como "me pusieron una reseña de una
  estrella", "cómo respondo a esto sin quedar mal", "llevo tres quejas seguidas por lo
  mismo", "cómo consigo que la gente reseñe" o "esta reseña es injusta". No la uses para
  gestionar publicidad en redes ni para diseñar la carta de respuesta a una reclamación
  formal por escrito de un cliente (eso es un asunto legal, no de reputación).
license: Proprietary. Copyright 2026. All rights reserved.
compatibility: Requiere Python 3.9+ para ejecutar scripts/resenas.py. Sin dependencias externas.
metadata:
  version: "1.2.0"
  sector: "hosteleria-restauracion"
  entregable: "informe-y-respuestas-resenas"
  enlaza_con: "escandallo-ingenieria-menu"
---

# Respuesta a reseñas y detección de patrones

## Qué hace

Convierte **un conjunto de reseñas en cualquier formato (export de Google o TripAdvisor,
capturas, pegadas a mano)** en **un informe con la respuesta redactada para cada una y los
patrones operativos que se repiten en las negativas**, para **el dueño o encargado de un
restaurante independiente**, en **menos de 30 minutos de atención**.

Este es el trabajo que un dueño hace a última hora, cansado, después del servicio, y que por
eso sale mal: contestar con prisa, a la defensiva, o no contestar y dejar que se acumulen. El
papel de la skill no es escribir una respuesta bonita, sino escribir **la que protege al negocio
delante de quien lea esa reseña después** —que no es quien la escribió, es el siguiente cliente
que decide si reserva— y, sobre todo, decirle al dueño si las negativas están señalando un
problema real que se repite. Eso vale más que cualquier respuesta: una reseña negativa aislada
es ruido; el mismo motivo tres veces en dos meses es una señal operativa que se arregla el lunes.

## Cuándo se dispara

- "me pusieron una reseña de una estrella"
- "cómo respondo a esto sin quedar mal"
- "llevo tres quejas seguidas por lo mismo"
- "esta reseña es injusta, seguro que es de la competencia"
- "por qué me están bajando las estrellas"
- "cómo consigo que la gente me reseñe"
- "¿le ofrezco algo para que la quite?"
- "quiero que alguien mire las últimas opiniones"
- "un cliente se quejó en internet y no sé qué hacer"
- jerga del gremio: "reseña", "estrella", "valoración", "opinión", "Google", "TripAdvisor",
  "ficha de Google", "media", "reputación", "troll", "reseña falsa", "responder reseñas"

## Quién lo ejecuta

El dueño o el encargado, con **20 a 30 minutos** de atención para una tanda de reseñas de un
mes. No requiere conocimiento técnico: el único paso que exige criterio propio es decidir qué
patrón se ataca primero, y el informe ya llega ordenado por impacto.

## Entrada

- **Obligatorio:** las reseñas, en el formato que sea. Export de Google o TripAdvisor, capturas
  de pantalla, o pegadas a mano. No hace falta limpiarlas antes.
- **Recomendado:** la fecha de cada reseña. Sin fecha, la reseña cuenta para el total pero
  **no entra en la ventana de 60 días** que define el patrón, y se marca `[sin fecha]`.
- **Recomendado:** la media de estrellas actual del local, que es lo único que permite traducir
  la tendencia a un rango de ingresos.
- **Recomendado:** el motivo principal de cada negativa (comida, servicio, tiempo de espera,
  precio, limpieza, ambiente) si viene categorizado. Si no, se infiere del texto.
- **Dato sucio típico:** el export sin categorizar y con fechas parciales. El motivo se deduce
  del texto y se marca **siempre** `[motivo inferido]`, nunca se presenta como categorización
  del cliente, porque el dueño va a tomar una decisión operativa con eso y tiene que saber si
  está leyendo un dato o una lectura. El segundo dato sucio es la captura suelta sin histórico:
  se responde igual, pero no se declara ningún patrón.

## Umbral que sostiene el producto

**Tres menciones del mismo motivo en una ventana de 60 días.** Por debajo de ese umbral se
trata como ruido normal y se dice explícitamente "bajo el umbral, no priorizar": perseguir cada
queja aislada agota al dueño sin cambiar nada. Por encima, deja de ser "clientes difíciles" y
pasa a ser señal operativa. El umbral es **criterio de oficio de la casa `[A VALIDAR]`**, sin
contraste de hipótesis detrás, y así está declarado en `references/umbrales-resenas.md`.

Regla de muestra mínima: **con menos de 5 reseñas totales no se declara ningún patrón**. Se dice
que la muestra no da para distinguir patrón de ruido.

El segundo umbral sí tiene fuente, y es el que convierte esto de cuidar el ego a cuidar la caja:
**una estrella adicional de media equivale a un +5% a +9% de ingresos**, según Luca, *Reviews,
Reputation and Revenue: The Case of Yelp.com*, HBS Working Paper 12-016
(<https://www.hbs.edu/faculty/Pages/item.aspx?num=41233>). **Se cita siempre con sus tres
límites pegados: es Yelp, es EE. UU. (3.582 restaurantes de Seattle, 2003-2009), y es ingresos,
no margen.** Y **solo existe en restaurantes independientes**, no en cadena: por eso un grupo
con marca consolidada no es comprador de esta pieza.

El tercer umbral es legal y es el que evita un problema caro: está prohibido incentivar reseñas
o filtrarlas (*review gating*). Lo dicen las políticas publicadas de Google
(<https://support.google.com/contributionpolicy/answer/7400114>) y Tripadvisor
(<https://www.tripadvisor.com/Trust-lvBd3L1aU38Y.html>), y en España cae en el art. 27.8 de la
Ley 3/1991 tras el RDL 24/2021, con sanciones del art. 49 TRLGDCU
(<https://www.iberley.es/legislacion/articulo-49-ley-defensa-consumidores-usuarios>).

## Procedimiento

1. **Entrada: reseñas en cualquier formato (export, capturas, pegadas a mano) → Acción: normalizar cada una a puntuación, fecha, texto y plataforma → Salida: lista uniforme lista para clasificar → Si falta el dato: sin fecha, la reseña cuenta para el conteo pero NO para la ventana de 60 días del patrón, y se marca `[sin fecha]` en el informe.**

2. **Entrada: lista normalizada → Acción: clasificar cada reseña en positiva (4-5★) / negativa con motivo identificable / negativa sin motivo verificable → Salida: cada reseña con su categoría y su protocolo de respuesta asignado → Si falta el dato: el motivo se infiere del texto y se marca `[motivo inferido]`, nunca se presenta como categorización del cliente.**

3. **Entrada: reseñas negativas con motivo → Acción: ejecutar `scripts/resenas.py` para agrupar por motivo y contar repeticiones dentro de la ventana → Salida: tabla de patrones con nº de menciones y periodo → Si falta el dato: con menos de 5 reseñas totales no se declara ningún patrón; se dice que la muestra no da para distinguir patrón de ruido.**

4. **Entrada: tabla de patrones → Acción: aplicar el umbral de alarma (3 o más menciones del mismo motivo en 60 días) → Salida: patrones separados en "señal operativa" y "bajo umbral, no priorizar" → Si falta el dato: si las fechas son parciales, se declara la ventana real cubierta y se baja la confianza del patrón, no se extrapola.**

5. **Entrada: media de estrellas actual y objetivo → Acción: traducir la mejora a rango de ingresos con la elasticidad de Luca (HBS 12-016) → Salida: rango en % de ingresos, con la fuente y sus tres límites declarados → Si falta el dato: sin media actual no se calcula impacto; se cita la referencia como dato de mercado y se marca `[HUECO]` la cifra del local.**

6. **Entrada: cada reseña con su categoría → Acción: redactar la respuesta siguiendo la estructura fija de su protocolo, mencionando un detalle concreto e irrepetible de esa reseña → Salida: texto listo para publicar → Si falta el dato: si la reseña no da ningún detalle concreto (solo estrellas, sin texto), se redacta la respuesta corta de acuse y se marca que no admite personalización.**

7. **Entrada: respuestas redactadas → Acción: pasar el filtro de verificación de la sección 5 del Método (¿específica? ¿admite culpa genérica? ¿expone información interna?) → Salida: respuestas corregidas → Si una respuesta admite culpa genérica o nombra a un empleado, proveedor o turno, se reescribe antes de entregar, sin excepción.**

8. **Entrada: informe completo → Acción: añadir la sección de supuestos con qué motivos se infirieron y qué reseñas no se pudieron clasificar → Salida: informe entregable → Si falta el dato: se entrega igual con los huecos marcados; un patrón inventado en un informe de reputación es peor que un hueco declarado.**

## Salida

```
# Reseñas y reputación — [Nombre del local]
[Periodo analizado] · [Nº de reseñas] · [Media de estrellas]

## 1. Diagnóstico en tres líneas
Media actual X,X estrellas · tendencia [subiendo/bajando/estable] · impacto estimado
en ingresos si mejora Y puntos: Z%.

## 2. Respuestas listas para publicar
Una por reseña aportada, con su categoría (positiva / negativa con motivo / negativa
injusta) y el texto completo.

## 3. Patrones detectados
Tabla: motivo · nº de menciones · periodo · ¿supera el umbral (3 en 60 días)?
Solo se listan los que lo superan; el resto, como "bajo el umbral, no priorizar".

## 4. Acciones, por orden de impacto
Cada una: qué revisar operativamente · qué patrón la origina · qué se espera si se corrige.

## 5. Cómo conseguir más reseñas buenas
Cuándo pedirla, a quién no pedírsela, y el límite legal de incentivos con su política citada.

## Supuestos de esta versión
Qué motivo se infirió del texto en vez de venir categorizado, qué reseñas no se pudieron
clasificar, qué ventana real cubren las fechas disponibles.
```

Las tres categorías que deciden el protocolo de respuesta, y que se asignan **antes** de
escribir una sola palabra:

| Categoría | Qué se hace | Qué nunca se hace |
|---|---|---|
| **Positiva (4-5★)** | Agradecer siendo específico sobre algo que mencionó, e invitar a volver | Ignorarla, o responder un genérico "gracias por tu visita" |
| **Negativa con motivo** | Reconocer el hecho concreto, decir qué se revisa, ofrecer canal privado | Admitir culpa genérica, o explicar en público el detalle interno |
| **Negativa sin motivo verificable** | Responder con calma y hechos verificables, invitar a contacto privado | Entrar en pelea pública o acusar de reseña falsa |

Cierra siempre con la cifra, que es lo único que el dueño va a recordar: **"cada estrella de
mejora en la media puede representar un 5-9% de ingresos adicionales en un local
independiente"**, con sus tres límites pegados.

## Límites

- **No publica ninguna respuesta.** Entrega el texto para que lo revise y lo publique el dueño,
  o lo apruebe antes de que lo haga alguien de su equipo. La firma es suya.
- No gestiona la eliminación de reseñas falsas ante la plataforma: Google y TripAdvisor tienen
  su propio proceso de disputa, ajeno a esta skill.
- **No es asesoría legal.** Ante difamación clara, acusación de intoxicación alimentaria o
  mención de abogado, la skill se detiene y deriva a un profesional colegiado: ahí deja de ser
  reputación y pasa a ser prueba.
- No inventa patrones para rellenar. Si el export está incompleto, el patrón detectado también
  lo estará, y eso se dice: un patrón inventado en un informe de reputación es peor que un hueco
  declarado.
- La elasticidad de Luca **no es la cifra de ese local**. Es una media de 3.582 restaurantes de
  Seattle entre 2003 y 2009, en Yelp y sobre ingresos: referencia de mercado, no su caja.
- **No aplica a cadenas ni a grupos con marca consolidada.** El efecto de ingresos por estrella
  está medido solo en independientes, así que el argumento central no les sirve.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Clasificar la reseña antes de redactar una sola palabra | Cada categoría tiene un protocolo distinto; mezclarlos es lo que hace que la respuesta suene defensiva o intercambiable |
| Mencionar un detalle concreto e irrepetible de esa reseña | Una respuesta que sirve para cualquier reseña no protege ante el siguiente cliente, que es para quien se escribe |
| Reconocer el hecho ("la mesa esperó 40 minutos"), nunca la culpa abstracta | Una admisión genérica de responsabilidad puede citarse en una reclamación formal; el hecho concreto no |
| Ofrecer canal privado en toda respuesta negativa | Saca la conversación de la vista pública sin parecer que se esconde nada |
| Exigir 3 menciones del mismo motivo en 60 días antes de declarar patrón | Por debajo de ese umbral se persigue ruido, y el dueño se agota sin cambiar nada |
| Declarar `[motivo inferido]` cuando el motivo se dedujo del texto | El dueño va a tomar una decisión operativa con eso: tiene que saber si es dato o lectura |
| Traducir la tendencia de estrellas a rango de ingresos con la fuente declarada | Convierte la gestión de reseñas de cuidar el ego a cuidar la caja, que es lo que paga |
| Declarar los tres límites de la cifra de Luca al citarla | Es Yelp, es EE. UU. y es sobre ingresos, no margen. Sin esos tres límites la cifra se usa mal |
| Responder también a las positivas | Cada respuesta a una positiva la lee el siguiente cliente y ve a un dueño presente |
| Entregar el informe con huecos marcados antes que rellenarlos | Un patrón inventado en un informe de reputación es peor que un hueco declarado |
| Ejecutar el conteo de patrones con el script, nunca a ojo | Un patrón contado a mano se sesga hacia la queja que más molestó al dueño |

| NUNCA | Porqué |
|---|---|
| Publicar la respuesta automáticamente | La firma es del dueño; la skill entrega texto, no publica |
| Nombrar a un empleado, un proveedor o un turno concreto en público | Expone a una persona y convierte un problema de reputación en un problema laboral |
| Entrar en discusión pública con una reseña injusta | Cada respuesta agresiva la lee el siguiente cliente potencial, no quien la escribió |
| Copiar y pegar la misma plantilla en dos respuestas negativas seguidas | Los lectores lo notan y anula el efecto de haber respondido |
| Ofrecer descuento, invitación o compensación a cambio de una reseña o de retirarla | Lo prohíben expresamente Google y Tripadvisor, y en España cae en el art. 27.8 de la Ley 3/1991 tras el RDL 24/2021 |
| Pedir reseña solo a los clientes contentos (*review gating*) | Google lo prohíbe con esas palabras: "discourage or prohibit negative reviews, or selectively solicit positive reviews" |
| Declarar patrón con menos de 3 menciones o fuera de la ventana de 60 días | Convierte ruido en diagnóstico y manda al dueño a arreglar lo que no está roto |
| Responder a una acusación de intoxicación alimentaria o a una amenaza legal sin abogado | Deja de ser reputación y pasa a ser prueba; lo firma un profesional colegiado |
| Presentar la elasticidad de Luca como cifra del local | Es una media de 3.582 restaurantes de Seattle entre 2003 y 2009: es referencia de mercado, no la caja de ese dueño |
| Afirmar que una plataforma penaliza algo sin la política publicada que lo diga | Es una cifra huérfana en forma de afirmación, y erosiona la confianza que sostiene el negocio |

## Antipatrones

1. **Síntoma**: las cinco respuestas del informe se pueden intercambiar entre sí sin que ninguna deje de tener sentido. **Causa raíz**: se redactó desde la plantilla en vez de desde la reseña, saltándose el paso 6 del procedimiento. **Corrección**: por cada respuesta, subrayar la palabra que solo pertenece a esa reseña; si no hay ninguna, reescribir.

2. **Síntoma**: la respuesta dice "sentimos muchísimo el error que cometimos" ante una reclamación por intoxicación. **Causa raíz**: se confundió empatía con admisión de responsabilidad. **Corrección**: reconocer el hecho verificable y derivar a canal privado; ante mención de daño a la salud o de abogado, la skill se detiene y deriva a profesional colegiado.

3. **Síntoma**: el informe declara "patrón de tiempo de espera" con dos menciones separadas cinco meses. **Causa raíz**: el umbral de 3 en 60 días se aplicó a ojo en vez de con el script. **Corrección**: ejecutar `scripts/resenas.py`, y si la ventana real no llega, listarlo como "bajo el umbral, no priorizar".

4. **Síntoma**: el dueño empieza a ofrecer un postre gratis a cambio de reseña, y la cuenta recibe un aviso de la plataforma. **Causa raíz**: la skill recomendó "cómo conseguir más reseñas buenas" sin declarar el límite de incentivos. **Corrección**: la sección 5 del informe cita siempre la política vigente y separa lo permitido (pedir reseña de una experiencia real) de lo prohibido (incentivar o filtrar). `[DERIVADO, NO OBSERVADO EN CAMPO]`

5. **Síntoma**: el informe cierra con "+5-9% de ingresos" sin decir de dónde sale, y el dueño lo repite ante su socio como si fuera su cifra. **Causa raíz**: se citó la conclusión de Luca sin sus tres límites. **Corrección**: cada mención de la elasticidad lleva pegado Yelp / EE. UU. 2003-2009 / ingresos-no-margen, o no se menciona.

## Casos de prueba

Los cuatro casos están en `cases/`, con entrada y salida reales.

**Happy path** (`cases/case_01_happy_path.md`): export completo de reseñas con fechas y motivos.
Se detecta un patrón real que supera el umbral de 3 en 60 días y se traduce a acción operativa.

**Edge case** (`cases/case_02_edge_case.md`): reseña injusta o de competidor, sin motivo
verificable. Se responde con hechos verificables y sin entrar en pelea pública.

**Failure** (`cases/case_03_failure.md`): una captura suelta, sin contexto ni histórico. Se
entrega la respuesta redactada con sus supuestos declarados, y se dice explícitamente que con
una sola reseña no se puede declarar ningún patrón.

**Integration** (`cases/case_04_integration.md`): encadenado con `escandallo-ingenieria-menu`.
El patrón de reseñas apunta a una causa operativa y se cruza con los platos que ya están
señalados por desviación de food cost.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.2.0 — ver `CHANGELOG.md`.
