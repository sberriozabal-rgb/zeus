# CASOS DE PRUEBA · respaldo-proyecto-ia-cl v2.0.0

Los cinco casos con entrada concreta, salida esperada y **la trampa que cada uno
comprueba**. Los casos 01–04 usan datos sintéticos; el caso 05 se ejecutó de
verdad contra un export simulado el 2026-08-16 y su salida es la observada, no
la esperada.

---

## case_01_happy_path · proyecto Pro con export completo

**Entrada.** Proyecto "Método de peritación", plan Pro, con acceso de edición:
22 documentos de texto, 4 adjuntos (3 PDF de 2–8 MB y 1 xlsx), instrucciones de
1 800 palabras, 2 skills propias, y el ZIP del export oficial descargado en
plazo, **con campo de proyecto** en las conversaciones: 61 chats en la cuenta,
14 del proyecto. Destino: cuenta personal de un socio.

**Comandos.**

```
python3 scripts/respaldo.py --preparar respaldo-mp --proyecto "Metodo de peritacion"
# pegar L1, copiar L2, colocar .skill
python3 scripts/respaldo.py --ingerir export.zip --carpeta respaldo-mp --proyecto "Metodo de peritacion"
python3 scripts/respaldo.py --recolectar ~/Descargas --carpeta respaldo-mp --desde 2026-01-01
# P5-P7 a mano: clasificar, redactar, lecturas, prueba de humo
python3 scripts/respaldo.py --auto respaldo-mp --proyecto "Metodo de peritacion"
```

**Salida esperada.**

```
respaldo-respaldo-mp-2026-08-16.zip
{"cifrado":"AES-256","huecos":[],
 "metodo_seleccion":"campo de proyecto del export [FIABLE]",
 "chats_incluidos":14,"chats_descartados":47}
ACTA-respaldo-mp-2026-08-16.json -> "resultado":"SELLADO Y VERIFICADO"
```

Dentro: RESTAURAR-TODO.md con L1 íntegra y el resumen de los 14 chats, cada uno
con su `LECTURA DE UNA PERSONA` escrita. Los 47 chats ajenos aparecen listados
como descartados en RESUMEN-CHATS.md, no en el paquete.

**La trampa que comprueba.** Que el filtro por campo de proyecto separa 14 de
61 sin arrastrar ninguno ajeno, y que el resumen entra en el maestro. Si el
paquete trae 61 transcripciones, el filtro no funcionó y el respaldo multiplica
su volumen con datos personales de otros contextos (regla NUNCA-6 de v1, ahora
absorbida por el filtro).

---

## case_02_edge_case · export SIN campo de proyecto

**Entrada.** El mismo proyecto, pero el export entrega conversaciones sin campo
de proyecto utilizable (formato antiguo o cambiado). 61 chats, 14 del proyecto,
y dos de ellos ni siquiera nombran el proyecto en el texto.

**Salida esperada.**

```
"metodo_seleccion":"coincidencia de texto [INDICIO, NO PRUEBA] - el export no
 trae campo de proyecto utilizable; revisa la seleccion a mano"
AVISO: la seleccion es un indicio, no una prueba. Revisala antes de sellar.
```

El operador revisa el índice de RESUMEN-CHATS.md contra la tabla de descartados,
añade a mano los 2 chats que el texto no capturó y anota en HUECOS.md:
`[SELECCION MANUAL: 2 chats añadidos tras filtro INDICIO]`.

**La trampa que comprueba.** Que la skill no disfraza un indicio de prueba
(regla NUNCA-7). Un sellado directo tras un filtro `[INDICIO]` sin revisión es
fallo del operador, y el AVISO impreso es lo que el auditor busca en el acta.

---

## case_03_failure · sin export: encargo de una línea

**Entrada.** "Respáldame el proyecto" — sin export solicitado, y al pedirlo el
enlace del correo ya había caducado (24 h). Nada más de contexto.

**Salida esperada.** No se rinde ni se bloquea: entrega el respaldo de L1–L4
completo con `--auto` sin `--export`, y en el maestro y HUECOS.md:

```
| chat | historial completo | [NO EXPORTABLE: export no descargado en plazo] |
  Acción: volver a solicitar el export en Ajustes -> Privacidad y re-sellar
  con --ingerir cuando llegue. Plazo: 24 h desde el correo.
```

El paquete se declara **PARCIAL**, y RESTAURAR-TODO.md lleva en la sección 6 el
hueco con la instrucción de re-sellado.

**La trampa que comprueba.** El caso failure entrega algo útil: lo irremplazable
(L1) queda a salvo hoy, y el camino para completar L5 mañana queda escrito. Un
respaldo que se aborta porque falta una capa es peor que un parcial declarado.

---

## case_04_integration · chats.jsonl como entrada de otra skill

**Entrada.** El `05-chats/chats.jsonl` de un respaldo sellado, consumido por una
skill de cartera/auditoría que necesita saber qué decisiones de precio hay
documentadas.

**Salida esperada.** Cada línea del jsonl es un objeto autónomo:

```json
{"n":1,"titulo":"Precios FORJA","creado":"2026-07-02T09:00:00",
 "n_mensajes":2,"senales":{"decisiones":[{"rol":"assistant",
 "cita":"Decidimos 2.500 EUR + 190 EUR/mes..."}],
 "cifras":["2.500 EUR","190 EUR/mes"],"pendientes":[...]}}
```

La skill consumidora filtra `senales.decisiones` sin abrir ninguna
transcripción. El contrato: metadatos y señales viajan en el jsonl; el texto
íntegro solo en `transcripciones/`, que es C2 y no sale del paquete.

**La trampa que comprueba.** Que la integración no obliga a repartir las
transcripciones completas. Si la skill consumidora necesita el texto íntegro,
debe pedir el paquete y su clave por los dos canales, como cualquiera.

---

## case_05_datos_sucios · ejecutado en real el 2026-08-16

**Entrada.** Export simulado con las suciedades vistas en exports reales: chat
sin campo de proyecto, mensajes con `content` en bloques y con `parts`, chat
vacío, mensajes sin fecha, **una clave API pegada en medio de una conversación**,
y una carpeta de descargas con un duplicado exacto bajo otro nombre y un archivo
de 2020.

**Salida observada (literal).**

```
Volcado reconocido: data-2026/conversations.json -> 3 conversaciones.
"chats_incluidos": 1, "chats_descartados": 2   (el vacío se omite solo)
"recolectados": 2, "duplicados": 1, "omitidos": 1
== ESCANEO ==  C3 (secreto): 2
  [C3] 05-chats/RESUMEN-CHATS.md:37  clave OpenAI/Anthropic
  [C3] 05-chats/transcripciones/001-precios-forja.md:16  clave OpenAI/Anthropic
AUTO DETENIDO: hay secretos. Rotalos y redactalos antes de sellar.
```

Tras sustituir por `[REDACTADO:credencial - rotada 2026-08-16]` y relanzar:

```
"resultado": "SELLADO Y VERIFICADO"
== VERIFICACION ==  OK: 9   ALTERADOS: 0   AUSENTES: 0
Archivo maestro RESTAURAR-TODO.md: presente
```

**La trampa que comprueba.** Tres a la vez. Que el secreto citado dentro de un
chat detiene el sellado (antipatrón 5 aplicado a L5); que el marcador
`[REDACTADO:...]` ya no re-dispara el patrón y el segundo sellado pasa (gotcha
G-1 de v1.0.0, corregido); y que el duplicado se descarta por SHA-256
conservando la copia que citan las instrucciones, no la primera alfabética.
