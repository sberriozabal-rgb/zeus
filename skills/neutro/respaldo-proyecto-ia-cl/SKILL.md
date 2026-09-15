---
name: respaldo-proyecto-ia-cl
description: Convierte un Proyecto de Claude — instrucciones, conocimiento, adjuntos y descargas, skills y el historial de chats resumido — en un paquete cifrado, verificable y reconstruible en otra cuenta, con un archivo maestro RESTAURAR-TODO.md con las instrucciones íntegras y los pasos de restauración. Digiere el export oficial de datos para transcribir y resumir los chats del proyecto, y barre carpetas de descargas deduplicando por SHA-256. Úsala cuando el usuario quiera respaldar, exportar, migrar, clonar o poner a salvo un proyecto; cuando diga "haz copia de seguridad del proyecto", "guarda las descargas y los chats", "resume todos los chats", "si pierdo la cuenta lo pierdo todo" o "cómo saco todo esto de aquí". También para auditar un respaldo existente o preparar la entrega a un tercero sin exponer datos sensibles. Sirve a Free, Pro, Max, Team y Enterprise, con las diferencias declaradas en la matriz.
license: Proprietary
compatibility: Requiere Python 3.9+ y el paquete pyzipper para el cifrado AES-256. Sin pyzipper el paquete se entrega sin cifrar y así se declara. La ingesta de chats requiere el ZIP del export oficial (Ajustes → Privacidad → Exportar datos).
metadata:
  author: ZEUS
  version: "2.0.0"
  estado: ACORDADO
  auditoria: "18/20 (autoevaluación)"
---

# RESPALDO DE PROYECTO CLAUDE

## ROL

Eres el responsable de custodia de un Proyecto de Claude. Tu producto no es una
explicación: es un **paquete** que otra persona, en otra cuenta, en otro mes,
puede abrir y usar para reconstruir el proyecto sin ti delante.

---

## DEFINICIÓN OPERATIVA

Convierte **el contenido de un Proyecto de Claude (instrucciones, base de
conocimiento, descargas y adjuntos, skills asociadas y el historial de chats del
export oficial)** en **un paquete cifrado AES-256 con archivo maestro
RESTAURAR-TODO.md, resumen de chats, checksums SHA-256 y guion de reconstrucción**,
para **quien administra el proyecto**, en **30–60 minutos por proyecto de hasta
100 documentos una vez recibido el export**.

---

## LO PRIMERO QUE HAY QUE SABER, Y NO ES OPCIONAL

Anthropic **no soporta migrar datos entre cuentas personales**. Cita literal del
Centro de Ayuda: *"Exported data can't be imported into another personal Claude
account, and we don't support migrating data between personal accounts."*
(support.claude.com, art. 9450526).

Consecuencia operativa: **no existe un botón de migración y esta skill no lo
inventa.** Lo que produce es un paquete de **reconstrucción manual**: contenido
íntegro, ordenado y verificable, más el guion para volver a crearlo a mano en la
cuenta destino. Quien prometa otra cosa está vendiendo humo.

Segunda consecuencia: **el respaldo hay que hacerlo mientras se tiene acceso.**
Un proyecto al que ya perdiste el acceso no se respalda; se pierde.

Tercera, nueva en v2: **el historial de chats solo viaja por el export oficial.**
Ninguna sesión de trabajo puede leer los demás chats de la cuenta; lo que sí
puede es digerir el ZIP que la plataforma entrega en Ajustes → Privacidad →
Exportar datos. Ese ZIP llega por correo y **su enlace caduca a las 24 horas**:
se descarga en el momento, no mañana.

---

## PROTOCOLO · 12 pasos (P0–P11)

Los pasos con comando los ejecuta `scripts/respaldo.py`; el modo `--auto` los
encadena. Los pasos sin comando son de criterio y los firma una persona.

### P0 · Pedir el export oficial
**Entrada:** acceso a la cuenta. **Acción:** Ajustes → Privacidad → Exportar
datos, y descargar el ZIP del correo **antes de 24 horas**. **Salida:** el ZIP
del export, guardado fuera de la carpeta de trabajo.

**Si falta el dato:** sin export no hay L5 automática. El respaldo continúa y el
historial se declara `[NO EXPORTABLE: export no solicitado]` en HUECOS.md.
Nunca se aborta el respaldo por esta capa.

---

### P1 · Inventariar el perímetro
**Entrada:** acceso al proyecto. **Acción:** listar las cinco capas y contar
elementos. **Salida:** tabla `capa · nº elementos · accesible sí/no`.

| Capa | Qué es | Se recupera |
|---|---|---|
| L1 · Instrucciones | El texto de "Instrucciones del proyecto" | Copiar/pegar |
| L2 · Conocimiento | Docs de texto creados en el proyecto | Copiar/pegar o descarga |
| L3 · Adjuntos | PDF, imágenes, xlsx, binarios subidos o descargados | Descarga + barrido local (P4) |
| L4 · Skills | Skills asociadas o invocadas por el proyecto | Archivo `.skill` propio |
| L5 · Chats | Conversaciones del proyecto | **Export oficial, digerido en P3** |

**Si falta el dato:** una capa no accesible se declara `[NO EXPORTABLE]` con el
motivo y se sigue.

---

### P2 · Preparar el árbol
`python3 scripts/respaldo.py --preparar <carpeta> --proyecto "<nombre>"`

Crea la estructura canónica vacía. L1 se pega a mano en `01-instrucciones/`
**antes que nada**: es lo único irremplazable. Si el proceso se interrumpe, lo
que ya está a salvo es lo que más pesa.

```
respaldo-<proyecto>-<AAAA-MM-DD>/
├── RESTAURAR-TODO.md      # archivo maestro, generado en P8
├── MANIFIESTO.md · HUECOS.md · CHECKSUMS.txt
├── 01-instrucciones/  02-conocimiento/  03-adjuntos/  04-skills/
└── 05-chats/
    ├── RESUMEN-CHATS.md   # generado en P3
    ├── chats.jsonl        # una línea por chat, para encadenar con otra skill
    └── transcripciones/   # un .md por chat
```

---

### P3 · Ingerir los chats del export
`python3 scripts/respaldo.py --ingerir <export>.zip --carpeta <carpeta> --proyecto "<nombre>"`

Acepta el ZIP, la carpeta descomprimida o un `.json` suelto, y **no depende del
nombre del archivo**: reconoce el volcado por su estructura, porque el formato
del export ha cambiado antes y volverá a cambiar. Filtra los chats del proyecto,
escribe una transcripción por chat y genera `RESUMEN-CHATS.md` con índice,
temas por frecuencia, citas candidatas a decisión, cifras y pendientes.

Dos honestidades del filtro y del resumen, no negociables:

1. **El método de selección se declara.** Si el export trae campo de proyecto,
   el filtro es `[FIABLE]`. Si no lo trae, se cae a coincidencia de texto y se
   marca `[INDICIO, NO PRUEBA]`: la selección se revisa a mano antes de sellar.
2. **El resumen automático es un borrador que cita, cuenta y ordena. No
   interpreta.** Cada chat termina con la línea `LECTURA DE UNA PERSONA:
   [pendiente de escribir]`, y P7 obliga a rellenarla. Un índice de citas que se
   entrega como resumen ejecutivo es el antipatrón 6.

**Si falta el dato:** un chat sin mensajes se omite; un export sin conversaciones
detiene solo este paso, con el motivo probable (enlace caducado, archivo
equivocado) impreso.

---

### P4 · Recolectar las descargas
`python3 scripts/respaldo.py --recolectar <carpeta-descargas> [...] --carpeta <carpeta> --desde AAAA-MM-DD`

Barre una o varias carpetas locales (Descargas, Escritorio, la carpeta del
cliente), **deduplica por SHA-256** —dos archivos con el mismo contenido son
uno, aunque uno se llame "copia de"— y de cada grupo de duplicados conserva la
copia cuyo nombre citan L1/L2. Renombra a nombre neutro (`003-propuesta.pdf`) y
escribe `INDICE-ADJUNTOS.md` con tres tablas: la correspondencia
neutro↔original, **lo citado que no apareció** (antipatrón 4, va a HUECOS.md) y
**lo recolectado que nadie cita** (se decide pieza a pieza: entra o se descarta).

**Si falta el dato:** sin corte `--desde`, se barre todo; un archivo de más de
512 MB o de 0 bytes se omite y se cuenta.

---

### P5 · Clasificar sensibilidad — 4 clases excluyentes

| Clase | Criterio verificable | Destino |
|---|---|---|
| **C0 · PÚBLICO** | Podría publicarse hoy sin consecuencia | Entra sin cambios |
| **C1 · INTERNO** | Método propio; su fuga da ventaja a un competidor | Entra cifrado |
| **C2 · CONFIDENCIAL** | Nombra a un tercero identificable, precios o contratos | Entra cifrado **y redactado** |
| **C3 · SECRETO** | Da acceso: clave API, token, contraseña, credencial | **NO ENTRA. Se rota.** |

Se lee de C3 hacia C0 y se para en la primera que se cumpla. Un archivo con una
clave API es C3 aunque el otro 99 % sea público — **se parte el archivo, no se
rebaja la clase**. Clase desconocida = C2, nunca C0. **Las transcripciones de
chats son C2 por defecto**: son donde vive el dato personal que nadie recuerda
haber escrito.

---

### P6 · Redactar y escanear
`python3 scripts/respaldo.py --escanear <carpeta>`

Sustituir cada dato identificable de los C2 por `[REDACTADO:tipo]` y anotar la
correspondencia en `DICCIONARIO.md`, **que no viaja en el paquete**: es el único
archivo que revierte la redacción. Después, escanear. El script detecta patrones
de credencial y dato personal; **propone, y la clasificación la firma una
persona**. Desde v2.0.0 el marcador `[REDACTADO:...]` ya no vuelve a disparar el
patrón de contraseñas (gotcha G-1): redactar cierra el hallazgo.

**Si falta el dato:** un patrón dudoso se redacta. Redactar de más cuesta una
consulta al diccionario; redactar de menos cuesta una filtración.

---

### P7 · Escribir la lectura humana y la prueba de humo

Dos escrituras que ninguna máquina hace por ti:

1. **La lectura de cada chat.** Sobre el borrador de P3, en cada
   `LECTURA DE UNA PERSONA:`, dos o tres frases: qué se decidió de verdad, qué
   quedó abierto, qué cifra hay que defender.
2. **La prueba de humo.** Una pregunta cuya respuesta correcta solo es posible
   si el proyecto se reconstruyó bien, con su respuesta y el archivo donde vive
   el dato. Se escribe **en el origen**: quien reconstruye no sabe qué debería
   salir.

**Criterio de paso:** cero líneas `[pendiente de escribir]` y prueba de humo con
respuesta.

---

### P8 · Generar el archivo maestro
`python3 scripts/respaldo.py --restaurar-todo <carpeta> --proyecto "<nombre>"`

Escribe `RESTAURAR-TODO.md`: **un solo archivo con las instrucciones L1
íntegras para pegar, el índice y extracto de L2, el inventario de adjuntos y
skills, el resumen de chats completo, los 10 pasos de restauración en orden, la
prueba de humo, los huecos declarados y el acta de reconstrucción**. Quien lo
abre sabe qué había en el proyecto sin abrir nada más; las carpetas del paquete
aportan los binarios.

El maestro **no contiene la huella SHA-256 del paquete** y lo dice: un archivo
no puede contener la huella del contenedor que lo contiene. La huella viaja por
el canal B y la comprueba P10.

---

### P9 · Sellar
`python3 scripts/respaldo.py --empaquetar <carpeta>`

Checksums SHA-256 de todo, y ZIP anidado: interno sin cifrar dentro de externo
cifrado AES-256. Dos decisiones técnicas no negociables:

1. **AES-256, nunca el cifrado ZIP heredado** — roto por ataque de texto
   conocido desde 1994 (Biham y Kocher).
2. **Doble ZIP**, porque el formato ZIP no cifra los nombres de archivo: el
   directorio central va en claro y un nombre como `contrato-cliente-X.pdf`
   filtra al cliente sin contraseña.

**La contraseña no se pasa como argumento**: variable `RESPALDO_PASSWORD` o
consola. El sellado **se detiene ante cualquier hallazgo C3** y avisa si falta
el archivo maestro. Sin `pyzipper`, no cifra en silencio: se detiene, dice qué
falta y ofrece continuar marcando `[SIN CIFRAR]` en el nombre.

---

### P10 · Probar la restauración en frío
`python3 scripts/respaldo.py --verificar <paquete>.zip`

En una carpeta vacía y distinta: extraer, comprobar cada checksum, comprobar que
`RESTAURAR-TODO.md` está presente, y abrir tres archivos de tres carpetas
distintas. **Un respaldo no probado no es un respaldo: es un archivo.** Si un
checksum no cuadra, se rehace el paquete completo; no se parchea.

---

### P11 · Entregar y custodiar la clave

Paquete y contraseña por **dos canales distintos**. Canal A (paquete): correo,
nube, disco. Canal B (contraseña + huella SHA-256): mensajería cifrada extremo a
extremo, llamada o gestor de contraseñas. Nunca los dos por el mismo medio, ni
siquiera en dos correos seguidos. Sin segundo canal, se entrega el paquete y se
retiene la contraseña: el paquete cifrado sin clave es inofensivo.

---

### MODO AUTO — el encadenado
`python3 scripts/respaldo.py --auto <carpeta> --export <export>.zip --descargas ~/Descargas --proyecto "<nombre>"`

Encadena P2 → P3 → P4 → escaneo → P8 → P9 → P10 y escribe un
`ACTA-<carpeta>-<fecha>.json` con el resultado de cada paso. Se detiene solo
ante C3. Lo que NO automatiza, porque no debe: pegar L1 (P2), clasificar (P5),
redactar (P6), la lectura humana y la prueba de humo (P7) y la entrega (P11).
El uso honesto de `--auto` es: primera pasada para tener el árbol y el borrador,
P5–P7 a mano, segunda pasada `--auto` para sellar y verificar.

---

## REGLAS

### SIEMPRE

1. **Respalda mientras tienes acceso.** El respaldo es una operación del presente; el que se aplaza no existe.
2. **Pide el export y descárgalo antes de 24 horas.** Es la única vía al historial de chats y su enlace caduca; un export no descargado es una capa perdida.
3. **Cifra con AES-256 y anida el ZIP.** Los nombres de archivo son datos y el formato ZIP los deja en claro.
4. **Separa paquete y clave en dos canales.** Un canal comprometido no debe bastar para abrirlo.
5. **Prueba la restauración antes de borrar el origen.** Un respaldo no verificado tiene la misma fiabilidad que no tenerlo, con la desventaja de que tranquiliza.
6. **Declara los huecos en `HUECOS.md`.** Quien reconstruye necesita saber qué le falta; descubrirlo a mitad es peor que saberlo de entrada.
7. **Escribe la lectura humana sobre el borrador de chats.** El script cita y cuenta; qué significa cada decisión solo lo sabe quien estuvo en la conversación.
8. **Escribe la prueba de humo en el origen.** Quien reconstruye no sabe qué debería salir; el autor sí.
9. **Ante la duda de clase, sube la clase, no la bajes.** El coste de proteger de más es una consulta; el de proteger de menos es irreversible.

### NUNCA

1. **Nunca metas un secreto (C3) en el respaldo.** Una clave API respaldada es una clave API filtrada en cuanto el paquete se copia una vez de más. **Se rota, no se respalda.**
2. **Nunca envíes la contraseña junto al paquete.** Anula el cifrado por completo y da falsa sensación de seguridad, que es peor que no cifrar.
3. **Nunca uses el cifrado ZIP heredado.** Roto por ataque de texto conocido desde 1994; la contraseña larga no lo arregla.
4. **Nunca pases la contraseña como argumento en la línea de comandos.** Queda en el historial del shell y en la lista de procesos del sistema.
5. **Nunca incluyas `DICCIONARIO.md` dentro del paquete redactado.** Revierte toda la redacción y convierte el trabajo de P6 en teatro.
6. **Nunca entregues el borrador automático como resumen ejecutivo.** Cita y cuenta, no interpreta; sin la lectura de P7 es un índice, y venderlo como resumen es prometer lo que el producto no hace.
7. **Nunca des por buena una selección de chats `[INDICIO]` sin revisarla.** La coincidencia de texto arrastra chats ajenos y deja fuera chats del proyecto; el campo de proyecto del export es prueba, el texto no.
8. **Nunca declares el respaldo completo si `HUECOS.md` no está vacío.** Se declara "completo salvo N elementos declarados".
9. **Nunca borres el proyecto origen en la misma sesión en que lo respaldas.** La verificación de P10 y el borrado deben estar separados por al menos un día y por una persona que confirme.

---

## MATRIZ DE APLICABILIDAD

| Contexto | Aplica | Ajuste |
|---|---|---|
| Proyecto personal (Free/Pro/Max) → otra cuenta personal | ✅ Sí | Caso central. No hay ruta nativa; reconstrucción manual con RESTAURAR-TODO.md. |
| Cuenta personal → organización Team/Enterprise | ⚠️ Parcial | Anthropic documenta un traslado propio de cuenta personal a organización (art. 9267400). **Compruébalo antes**: si aplica, es preferible a la reconstrucción manual. |
| Dentro de una misma organización Team/Enterprise | ⚠️ Parcial | Puede bastar con permisos de proyecto compartido. Usa esta skill solo si además necesitas copia fuera de la plataforma. |
| Export sin campo de proyecto en los chats | ⚠️ Parcial | El filtro cae a coincidencia de texto `[INDICIO, NO PRUEBA]`. Revisión manual obligatoria antes de sellar. |
| Proyecto con >100 documentos o en modo RAG | ✅ Sí | Trocea por carpetas de L2 y sella un paquete por lote. El manifiesto raíz indexa los lotes. |
| Proyecto con adjuntos que ya no tienes en local | ⚠️ Parcial | Lo que ni el barrido de P4 ni la descarga alcanzan va a `HUECOS.md` con su procedencia. |
| Entrega de un proyecto a un cliente externo | ✅ Sí | Obligatorio P6 completo con revisión de segunda persona. Las transcripciones de chats normalmente NO viajan a un tercero: se entrega solo el resumen leído y aprobado. |
| Cumplimiento de retención o requerimiento legal | ⚠️ Parcial | Copia técnica, **no prueba con validez legal**. La cadena de custodia probatoria exige sellado por tercero. Consúltalo con abogado. |
| **Aquí NO aplica** | ❌ | Recuperar un proyecto al que ya se perdió el acceso, y decidir si se borra el origen. Lo primero es soporte; lo segundo lo firma una persona. |

---

## ANTIPATRONES

### 1 · El respaldo que lleva la llave dentro
**Síntoma observable:** el correo de entrega contiene el `.zip` y, más abajo, la contraseña — o la contraseña está en un `.txt` dentro del propio paquete.
**Causa raíz:** se trató el cifrado como formalidad de proceso, no como control de acceso.
**Corrección:** paquete por canal A, contraseña y huella SHA-256 por canal B. Si no hay canal B, se retiene la contraseña.

### 2 · El nombre de archivo que delata
**Síntoma observable:** al listar el ZIP cifrado **sin introducir contraseña** se leen rutas como `03-adjuntos/propuesta-Cliente-Sanchez-450000.pdf`.
**Causa raíz:** se asumió que cifrar el ZIP cifra también el índice. No lo hace: el directorio central va en claro.
**Corrección:** ZIP anidado y nombres neutros; la correspondencia vive en `INDICE-ADJUNTOS.md`, dentro del cifrado.

### 3 · El respaldo que nadie abrió nunca
**Síntoma observable:** MANIFIESTO sin línea de verificación fechada, o fechada en el mismo minuto exacto que la creación del paquete.
**Causa raíz:** se confundió "el comando terminó sin error" con "el paquete se puede restaurar".
**Corrección:** P10 en carpeta vacía distinta, tres archivos de tres carpetas, línea fechada y firmada.

### 4 · La instrucción que apunta a un archivo que no viajó
**Síntoma observable:** las instrucciones reconstruidas citan `CATALOGO.md` y en `02-conocimiento/` no existe.
**Causa raíz:** capas respaldadas por separado sin comprobar referencias cruzadas.
**Corrección:** P4 y P9 lo comprueban solos: lo citado que no aparece se imprime y va a `HUECOS.md`.

### 5 · El secreto respaldado en vez de rotado
**Síntoma observable:** una cadena tipo `sk-`, `ghp_`, `AKIA` o `Bearer ` en cualquier archivo del paquete — **incluidas las transcripciones de chats**, donde las claves se pegan sin pensar.
**Causa raíz:** se aplicó "esto también forma parte del proyecto" a algo cuyo valor es exclusivamente el acceso que concede.
**Corrección:** rotarlo en origen y dejar `[REDACTADO:credencial — rotada AAAA-MM-DD]`. El sellado se detiene solo; desde v2.0.0 el marcador ya no re-dispara el patrón.

### 6 · El borrador que se vendió como resumen
**Síntoma observable:** RESUMEN-CHATS.md con líneas `LECTURA DE UNA PERSONA: [pendiente de escribir]` dentro de un paquete sellado.
**Causa raíz:** se confundió extraer citas con entender la conversación; la máquina hizo su mitad y nadie hizo la otra.
**Corrección:** P7 antes de P9. El autocontrol lo comprueba: cero `[pendiente de escribir]` en un paquete que se declara COMPLETO.

---

## CASOS DE PRUEBA

Los cinco casos, con entrada real y salida esperada, en
[`references/casos.md`](references/casos.md):

- `case_01_happy_path` — proyecto Pro, export con campo de proyecto, 22 docs, 4 adjuntos, 2 skills
- `case_02_edge_case` — export sin campo de proyecto: filtro `[INDICIO]`, revisión manual
- `case_03_failure` — sin export solicitado y enlace caducado: L5 a HUECOS, el resto viaja
- `case_04_integration` — encadenado: `chats.jsonl` como entrada de una skill de auditoría
- `case_05_datos_sucios` — export con chat vacío, mensajes sin fecha, secreto pegado en un chat y descargas duplicadas

---

## AUTOCONTROL

Antes de dar el respaldo por bueno:

- [ ] ¿`--escanear` devolvió cero hallazgos C3, o los que devolvió están rotados y redactados?
- [ ] ¿El método de selección de chats fue `[FIABLE]`, o siendo `[INDICIO]` se revisó a mano?
- [ ] ¿Queda alguna línea `LECTURA DE UNA PERSONA: [pendiente de escribir]`?
- [ ] ¿RESTAURAR-TODO.md existe, lleva las instrucciones L1 íntegras y la prueba de humo con respuesta?
- [ ] ¿La contraseña viajó por un canal distinto al del paquete?
- [ ] ¿Existe línea de verificación fechada, posterior a la creación?
- [ ] ¿Toda ruta citada en L1 existe en el árbol, o está en `HUECOS.md`?
- [ ] ¿`DICCIONARIO.md` está **fuera** del paquete?
- [ ] ¿El nombre del paquete y de sus carpetas está limpio de nombres propios?
- [ ] ¿Algún ejemplo de estas reglas contiene un dato que estas mismas reglas obligarían a marcar?

---

## CONTRATO DE INTERFAZ

**Entrada:** carpeta de trabajo con las cinco capas, y opcionalmente el ZIP del
export oficial y carpetas locales de descargas. Parámetros: `proyecto`, `desde`,
`salida`.

**Salida:** JSON por modo. `--auto` emite además `ACTA-<carpeta>-<fecha>.json`
con el resultado de cada paso. `--empaquetar` emite `paquete`, `ruta`, `sha256`,
`cifrado`, `n_archivos`, `por_clase{}`, `huecos[]`, `hallazgos_escaneo[]`.
`--ingerir` deja `05-chats/chats.jsonl` — una línea por chat con metadatos y
señales, sin transcripción — consumible por cualquier skill de registro,
auditoría o cartera.

**Dependencias:** ninguna obligatoria. `pyzipper` es opcional y su ausencia se
declara, no se oculta.

---

## REFERENCIAS

Verificadas y con su estatus declarado, en
[`references/fuentes.md`](references/fuentes.md).

**Esta skill no publica ningún umbral de seguridad propio.** El único parámetro
numérico que fija es la longitud mínima de contraseña recomendada, marcada
`[CRITERIO DEL AUTOR]` en `references/fuentes.md` con su justificación.

---

**v2.0.0 · 2026-08-16 · Estado: ACORDADO · Autoevaluación 18/20 · Ver `CHANGELOG.md`**
