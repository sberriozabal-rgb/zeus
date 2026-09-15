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
  version: "1.0.0"
  sector: "hosteleria-restauracion"
  entregable: "informe-y-respuestas-resenas"
  enlaza_con: "escandallo-ingenieria-menu"
---

# Respuesta a reseñas y detección de patrones

Este es el trabajo que un dueño de restaurante hace a última hora, cansado, después del servicio, y que por eso sale mal: contestar reseñas con prisa, a la defensiva, o no contestarlas y dejar que se acumulen. Tu papel aquí no es escribir una respuesta bonita. Es escribir la respuesta que protege al negocio delante de quien lea esa reseña después —que no es el que la escribió, es el siguiente cliente que decide si reserva— y, sobre todo, decirle al dueño si las reseñas negativas están señalando un problema real que se repite, porque eso vale más que cualquier respuesta.

Entregas dos cosas en el mismo informe, porque son el mismo trabajo:

1. **Las respuestas** — una por cada reseña que se aporte, con el tono y la estructura correctos según si es positiva, negativa o mixta.
2. **El patrón** — si el mismo problema aparece en varias reseñas negativas (el mismo plato, el mismo tiempo de espera, el mismo miembro del personal, la misma franja), eso ya no es "un cliente difícil": es una señal operativa que el dueño puede arreglar el lunes.

## Lo primero: no contestes nada todavía

El error que arruina más reputaciones que la propia reseña mala es la respuesta improvisada. Antes de escribir una sola palabra, hay que clasificar la reseña, porque cada tipo se responde distinto y mezclarlas es lo que hace que una respuesta suene defensiva o genérica.

**Tres categorías, tres protocolos:**

- **Positiva (4-5 estrellas).** Se agradece, se es específico sobre algo que mencionó (no un genérico "gracias por tu visita"), y se invita a volver. Nunca se ignora: cada respuesta a una positiva es una oportunidad de que quien la lea después vea que el dueño está presente.
- **Negativa con motivo identificable (comida, servicio, tiempo, precio, limpieza).** Se reconoce el hecho concreto sin admitir culpa genérica ni discutir, se explica qué se va a revisar, y se ofrece un canal privado para resolverlo fuera de la vista pública. Nunca se explica en público el detalle interno (turno, empleado, proveedor): eso se habla puertas adentro.
- **Negativa sin motivo verificable, injusta, o de un competidor/troll.** Se responde con calma, sin acusar directamente pero dejando claro con hechos verificables (fecha, reserva, plato pedido si se puede verificar) que la reseña no encaja con el registro del local, y se invita a contacto privado. Nunca se entra en pelea pública: cada respuesta agresiva la lee el siguiente cliente potencial, no el que la escribió.

## Método

### 1. Clasifica cada reseña antes de tocar el teclado

Para cada reseña necesitas: puntuación (estrellas), texto, fecha, y si es posible, el motivo principal (comida / servicio / tiempo de espera / precio / limpieza / ambiente / otro). Si el cliente aporta un export con muchas reseñas y sin categorizar, el motivo se infiere del texto — y se declara como inferido, no como dato verificado.

### 2. Calcula el impacto antes de preocuparte por la estrella suelta

Una reseña de una estrella duele, pero lo que mueve el negocio es la tendencia, no el caso aislado. Con datos de `references/umbrales-resenas.md`:

**Una estrella adicional de media equivale a un +5-9% de ingresos, y el efecto solo existe en restaurantes independientes** (no en cadena). Esto convierte la gestión de reseñas de "cuidar el ego" a "cuidar la caja": medio punto de mejora en la media siguiendo un patrón de respuesta activa y corrección real puede valer más que una campaña de marketing.

El informe siempre traduce la tendencia de estrellas a un rango de impacto en ingresos, nunca solo el número de estrellas suelto.

### 3. Detecta el patrón, no el caso

Este es el oficio que no se copia. Una reseña negativa aislada es ruido; tres reseñas negativas en dos meses mencionando el mismo problema es una señal.

`scripts/resenas.py` agrupa las reseñas negativas por motivo inferido y cuenta repeticiones. **Umbral de alarma: 3 o más menciones del mismo motivo en un periodo de 60 días** activa la marca de "patrón operativo", no "clientes difíciles sueltos". Por debajo de ese umbral, se trata como ruido normal — perseguir cada queja aislada agota al dueño sin cambiar nada.

Cuando hay patrón, el informe lo dice sin adornos: "3 reseñas en 45 días mencionan tiempo de espera en la cena de fin de semana. Esto no es casualidad: revisa el turno de sábado noche antes de gastar en marketing para traer más gente a ese mismo cuello de botella."

### 4. Redacta con la estructura que protege, no la que más gusta

Cada respuesta negativa sigue esta estructura fija, en este orden, porque el orden importa: reconocer el hecho concreto → sin admitir una culpa genérica que pueda usarse en su contra → indicar qué se revisa → ofrecer canal privado → cerrar con una invitación a volver solo si tiene sentido con el tono de la reseña.

**Nunca copies y pegues la misma plantilla en dos respuestas negativas seguidas.** Los lectores lo notan, y una respuesta intercambiable no protege ante el siguiente cliente, que es para quien se escribe: cada una debe mencionar el detalle concreto de esa reseña. (Antes aquí se afirmaba que Google y TripAdvisor *penalizan* las respuestas idénticas. **Ninguna política publicada de las dos plataformas lo dice** — la regla de Google sobre contenido repetido está en contenido de usuario, no en respuestas del propietario. Retirado el 16-ago-2026 por ser afirmación sin fuente.)

### 5. Verifica antes de entregar

- ¿Cada respuesta menciona algo específico de la reseña, o es intercambiable con cualquier otra?
- ¿Alguna respuesta negativa admite culpa genérica de forma que pueda citarse como reconocimiento legal de responsabilidad? Si es así, reescribe: se reconoce el hecho ("la mesa esperó 40 minutos"), no la culpa abstracta ("fue nuestro error total").
- ¿El patrón detectado tiene al menos 3 menciones en 60 días, o se está sobredimensionando una queja aislada?
- ¿Se dio información interna sensible (nombre de empleado, proveedor, turno) en una respuesta pública? Eso se retira siempre.
- ¿El informe traduce la tendencia de estrellas a un rango de impacto en ingresos con la fuente declarada?

## Procedimiento

1. **Entrada: reseñas en cualquier formato (export, capturas, pegadas a mano) → Acción: normalizar cada una a puntuación, fecha, texto y plataforma → Salida: lista uniforme lista para clasificar → Si falta el dato: sin fecha, la reseña cuenta para el conteo pero NO para la ventana de 60 días del patrón, y se marca `[sin fecha]` en el informe.**

2. **Entrada: lista normalizada → Acción: clasificar cada reseña en positiva (4-5★) / negativa con motivo identificable / negativa sin motivo verificable → Salida: cada reseña con su categoría y su protocolo de respuesta asignado → Si falta el dato: el motivo se infiere del texto y se marca `[motivo inferido]`, nunca se presenta como categorización del cliente.**

3. **Entrada: reseñas negativas con motivo → Acción: ejecutar `scripts/resenas.py` para agrupar por motivo y contar repeticiones dentro de la ventana → Salida: tabla de patrones con nº de menciones y periodo → Si falta el dato: con menos de 5 reseñas totales no se declara ningún patrón; se dice que la muestra no da para distinguir patrón de ruido.**

4. **Entrada: tabla de patrones → Acción: aplicar el umbral de alarma (3 o más menciones del mismo motivo en 60 días) → Salida: patrones separados en "señal operativa" y "bajo umbral, no priorizar" → Si falta el dato: si las fechas son parciales, se declara la ventana real cubierta y se baja la confianza del patrón, no se extrapola.**

5. **Entrada: media de estrellas actual y objetivo → Acción: traducir la mejora a rango de ingresos con la elasticidad de Luca (HBS 12-016) → Salida: rango en % de ingresos, con la fuente y sus tres límites declarados → Si falta el dato: sin media actual no se calcula impacto; se cita la referencia como dato de mercado y se marca `[HUECO]` la cifra del local.**

6. **Entrada: cada reseña con su categoría → Acción: redactar la respuesta siguiendo la estructura fija de su protocolo, mencionando un detalle concreto e irrepetible de esa reseña → Salida: texto listo para publicar → Si falta el dato: si la reseña no da ningún detalle concreto (solo estrellas, sin texto), se redacta la respuesta corta de acuse y se marca que no admite personalización.**

7. **Entrada: respuestas redactadas → Acción: pasar el filtro de verificación de la sección 5 del Método (¿específica? ¿admite culpa genérica? ¿expone información interna?) → Salida: respuestas corregidas → Si una respuesta admite culpa genérica o nombra a un empleado, proveedor o turno, se reescribe antes de entregar, sin excepción.**

8. **Entrada: informe completo → Acción: añadir la sección de supuestos con qué motivos se infirieron y qué reseñas no se pudieron clasificar → Salida: informe entregable → Si falta el dato: se entrega igual con los huecos marcados; un patrón inventado en un informe de reputación es peor que un hueco declarado.**

## Formato del informe

Entrega siempre esta estructura:

```
# Reseñas y reputación — [Nombre del local]
[Periodo analizado] · [Nº de reseñas] · [Media de estrellas]

## 1. Diagnóstico en tres líneas
Media actual X,X estrellas · tendencia [subiendo/bajando/estable] · impacto estimado en ingresos si mejora Y puntos: Z%.

## 2. Respuestas listas para publicar
Una por reseña aportada, con la categoría (positiva/negativa con motivo/negativa injusta) y el texto completo.

## 3. Patrones detectados
Tabla: motivo · nº de menciones · periodo · ¿supera el umbral de alarma (3 en 60 días)?
Solo se listan los que superan el umbral; los que no, se mencionan como "bajo el umbral, no priorizar".

## 4. Acciones, por orden de impacto
Cada una: qué revisar operativamente · qué patrón la origina · qué se espera si se corrige.

## 5. Cómo conseguir más reseñas buenas
Recomendación breve: cuándo pedir la reseña (el momento del servicio en que más convierte), a quién no pedírsela (cliente con incidencia sin resolver).

## 6. Supuestos y huecos de dato
Qué motivo se infirió del texto en vez de venir categorizado, qué reseñas no se pudieron clasificar.
```

Cierra siempre con la cifra: **"cada estrella de mejora en la media puede representar un 5-9% de ingresos adicionales en un local independiente (HBS/Luca)"**. Es lo único que el dueño va a recordar.

## Límites

Esta skill no publica ninguna respuesta automáticamente: entrega el texto para que el dueño lo revise y lo publique él, o lo apruebe antes de que alguien de su equipo lo haga. No gestiona la eliminación de reseñas falsas ante la plataforma (Google/TripAdvisor tienen su propio proceso de disputa, ajeno a esta skill). No es asesoría legal: si una reseña contiene difamación clara o acusaciones falsas graves, se recomienda consultar con un profesional colegiado antes de responder o de iniciar una disputa formal. Trabaja con los datos que le den: si el export de reseñas está incompleto, el patrón detectado lo estará, y eso se dice en el informe en vez de rellenarse con una inferencia sin declarar — un patrón inventado en un informe de reputación es peor que un hueco declarado.

## Archivos de apoyo

- `references/umbrales-resenas.md` — la cifra de impacto de las estrellas en ingresos, el umbral de alarma de patrones, y las señales de alarma en los datos. Léelo cuando tengas que juzgar si una tendencia de reseñas es grave o priorizar un patrón.
- `scripts/resenas.py` — clasifica reseñas, detecta patrones por motivo y frecuencia, y calcula el impacto estimado de un cambio en la media de estrellas. Úsalo siempre para el cálculo del patrón. `python3 scripts/resenas.py datos.json`, `--ejemplo` para ver el formato de entrada, `--autotest` para comprobar la aritmética.
- `assets/plantillas-respuestas.md` — estructuras de respuesta por categoría (positiva, negativa con motivo, negativa injusta) listas para adaptar.

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

Ver carpeta `cases/`:

- `case_01_happy_path.md` — export completo de reseñas con fechas y motivos, patrón real detectado
- `case_02_edge_case.md` — reseña injusta o de competidor, sin motivo verificable
- `case_03_failure.md` — una captura suelta sin contexto ni histórico
- `case_04_integration.md` — encadenado con otra skill de la línea, el patrón de reseñas apunta a una causa operativa

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v1.1.0 — ver `CHANGELOG.md`.
