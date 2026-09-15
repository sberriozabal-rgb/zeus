---
name: respaldo-proyecto-ia-cl
description: Convierte un Proyecto de Claude — instrucciones, conocimiento, adjuntos y descargas, skills y el historial de chats resumido — en un paquete cifrado, verificable y reconstruible en otra cuenta, con un archivo maestro RESTAURAR-TODO.md con las instrucciones íntegras y los pasos de restauración. Digiere el export oficial de datos para transcribir y resumir los chats del proyecto, y barre carpetas de descargas deduplicando por SHA-256. Úsala cuando el usuario quiera respaldar, exportar, migrar, clonar o poner a salvo un proyecto; cuando diga "haz copia de seguridad del proyecto", "guarda las descargas y los chats", "resume todos los chats", "si pierdo la cuenta lo pierdo todo" o "cómo saco todo esto de aquí". También para auditar un respaldo existente o preparar la entrega a un tercero sin exponer datos sensibles. Sirve a Free, Pro, Max, Team y Enterprise, con las diferencias declaradas en la matriz.
license: Proprietary
compatibility: Requiere Python 3.9+ y el paquete pyzipper para el cifrado AES-256. Sin pyzipper el paquete se entrega sin cifrar y así se declara. La ingesta de chats requiere el ZIP del export oficial (Ajustes → Privacidad → Exportar datos).
metadata:
  author: ZEUS
  version: "2.1.0"
  estado: ACORDADO
  auditoria: "18/20 (autoevaluación)"
---

# respaldo-proyecto-ia-cl

## Qué hace

Convierte **el contenido de un Proyecto de Claude —instrucciones, base de conocimiento,
descargas y adjuntos, skills asociadas y el historial de chats del export oficial—** en **un
paquete cifrado AES-256 con archivo maestro `RESTAURAR-TODO.md`, resumen de chats, checksums
SHA-256 y guion de reconstrucción**, para **quien administra el proyecto**, en **30 a 60 minutos
por proyecto de hasta 100 documentos**, una vez recibido el export.

Lo primero, y no es opcional: **Anthropic no soporta migrar datos entre cuentas personales.**
Cita literal del Centro de Ayuda: *"Exported data can't be imported into another personal Claude
account, and we don't support migrating data between personal accounts."* Consecuencia operativa:
**no existe un botón de migración y esta skill no lo inventa.** Lo que produce es un paquete de
reconstrucción **manual**, con el contenido ordenado y el guion para rehacerlo a mano.

## Cuándo se dispara

- "quiero hacer copia de seguridad de mi proyecto de Claude"
- "me voy a cambiar de cuenta, ¿cómo me llevo todo?"
- "¿puedo migrar un proyecto a otra cuenta?"
- "quiero guardar el historial de chats antes de borrar el proyecto"
- "necesito el contenido del proyecto fuera de la plataforma"
- "¿cómo exporto mis datos de Claude?"
- "quiero entregarle el proyecto a otra persona"
- "voy a cerrar la cuenta y no quiero perder lo que hay dentro"
- jerga del gremio: "export", "proyecto", "base de conocimiento", "instrucciones del proyecto",
  "adjuntos", "respaldo", "backup", "cifrado", "AES-256", "checksum", "restauración en frío",
  "rotar la clave", "redactado", "huecos"

## Quién lo ejecuta

Quien administra el proyecto, con **30 a 60 minutos** de atención por proyecto de hasta 100
documentos, **contados desde que llega el export**. El export no es inmediato: se solicita, llega
por correo y **su enlace caduca**, así que hay una ventana previa de espera que no depende de
quien ejecuta.

## Entrada

- **Obligatorio:** acceso vigente al proyecto. El respaldo es una operación del presente: el que
  se aplaza no existe.
- **Obligatorio:** el **export oficial** de los datos de Claude, solicitado y descargado **antes
  de 24 horas**, porque su enlace caduca. Es la única vía al historial de chats.
- **Recomendado:** la lista de skills asociadas al proyecto y de descargas generadas en él, que
  no siempre viajan en el export.
- **Recomendado:** un segundo canal de comunicación con quien vaya a custodiar el paquete, para
  separar paquete y contraseña.
- **Dato sucio típico:** el export **sin campo de proyecto**, que obliga a seleccionar los chats
  por coincidencia de texto. Esa selección va marcada `[INDICIO]` y **hay que revisarla a mano**:
  la coincidencia arrastra chats ajenos y deja fuera chats del proyecto. El campo de proyecto es
  prueba; el texto no. El segundo dato sucio es el **secreto pegado dentro de un chat** —una
  clave API que alguien copió sin pensar—, que dispara la parada del sellado.

## Umbral que sostiene el producto

**Las cuatro clases de sensibilidad, excluyentes y leídas de C3 hacia C0**, parando en la primera
que se cumpla:

| Clase | Criterio verificable | Destino |
|---|---|---|
| **C0 · PÚBLICO** | Podría publicarse hoy sin consecuencia | Entra sin cambios |
| **C1 · INTERNO** | Método propio; su fuga da ventaja a un competidor | Entra cifrado |
| **C2 · CONFIDENCIAL** | Nombra a un tercero identificable, precios o contratos | Entra cifrado **y redactado** |
| **C3 · SECRETO** | Da acceso: clave API, token, contraseña, credencial | **NO ENTRA. Se rota.** |

Un archivo con una clave API es **C3 aunque el otro 99 % sea público**: se parte el archivo, no
se rebaja la clase. **Clase desconocida = C2, nunca C0.** Y **las transcripciones de chats son C2
por defecto**, porque son donde vive el dato personal que nadie recuerda haber escrito.

El segundo umbral es técnico y tiene fuente: **el cifrado ZIP heredado está roto por ataque de
texto conocido desde 1994** (<https://homes.cs.washington.edu/~yoshi/papers/WinZip/winzip.pdf>),
y una contraseña larga no lo arregla. De ahí AES-256 y **ZIP anidado**: el directorio central de
un ZIP va **en claro**, así que los nombres de archivo se leen sin contraseña y los nombres de
archivo son datos.

El tercero es de proceso: **la restauración se prueba en frío antes de borrar el origen**, en
carpeta vacía distinta, con tres archivos de tres carpetas y una línea fechada y firmada en el
manifiesto. Un respaldo no verificado tiene la misma fiabilidad que no tenerlo, **con la
desventaja de que tranquiliza**.

Límites de plataforma, documentados: el export de datos personales
(<https://support.claude.com/en/articles/9450526-export-your-claude-data>), el de organización
(<https://support.claude.com/en/articles/13346720-export-your-organization-s-data>) y el paso de
cuenta personal a Team o Enterprise
(<https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization>).

## Procedimiento

1. **Entrada: el proyecto con acceso vigente → Acción: solicitar el export oficial de datos y
   descargarlo antes de que caduque el enlace, mientras se inventaria el perímetro (instrucciones,
   base de conocimiento, adjuntos, descargas y skills asociadas) → Salida: export en mano e
   inventario del perímetro → Si el enlace caduca o no se solicitó: la capa de historial de chats
   va entera a `HUECOS.md` y **el resto del respaldo se hace igual**.**

2. **Entrada: el inventario → Acción: preparar el árbol de carpetas del paquete e ingerir los
   chats del export, filtrando por el campo de proyecto → Salida: árbol poblado con las capas
   disponibles → Si el export no trae campo de proyecto: se filtra por coincidencia de texto,
   la selección se marca `[INDICIO]` y **se revisa a mano antes de seguir**.**

3. **Entrada: el árbol poblado → Acción: recolectar las descargas y los adjuntos, comprobando las
   referencias cruzadas entre lo que citan las instrucciones y lo que existe en disco → Salida:
   capas completas con su listado → Si algo citado no aparece: se imprime y va a `HUECOS.md`, no
   se da por presente.**

4. **Entrada: todo el contenido recolectado → Acción: clasificar cada elemento en C0-C3 leyendo de
   C3 hacia C0 → Salida: cada archivo con su clase y su destino → Si la clase es dudosa: se asigna
   **C2, nunca C0**; ante la duda se sube la clase, porque el coste de proteger de más es una
   consulta y el de proteger de menos es irreversible.**

5. **Entrada: los archivos clasificados → Acción: redactar los C2 sustituyendo el dato por su
   marcador, y escanear todo el paquete en busca de patrones de credencial (`sk-`, `ghp_`,
   `AKIA`, `Bearer `), **incluidas las transcripciones de chats** → Salida: contenido redactado y
   libre de secretos → Si aparece un secreto: **se rota en origen** y se deja
   `[REDACTADO:credencial — rotada AAAA-MM-DD]`; el sellado se detiene solo.**

6. **Entrada: el borrador automático de chats → Acción: escribir la **lectura humana** de qué
   significó cada decisión, y la prueba de humo que verificará la reconstrucción → Salida:
   `RESUMEN-CHATS.md` completo y prueba de humo escrita → Si queda algún
   `[pendiente de escribir]`: el paquete **no puede declararse COMPLETO**; el script cita y
   cuenta, pero solo quien estuvo en la conversación sabe qué significa.**

7. **Entrada: el paquete montado → Acción: generar `RESTAURAR-TODO.md`, calcular los checksums
   SHA-256 y sellar con AES-256 en **ZIP anidado** con nombres neutros → Salida: paquete cifrado
   con su manifiesto → Si `DICCIONARIO.md` está dentro del paquete redactado: se saca, porque
   revierte toda la redacción y convierte el paso 5 en teatro.**

8. **Entrada: el paquete sellado → Acción: probar la restauración **en frío**, en carpeta vacía
   distinta, abriendo tres archivos de tres carpetas, y firmar la línea fechada del manifiesto;
   después entregar el paquete por un canal y la contraseña con su huella SHA-256 por otro →
   Salida: paquete verificado y entregado con custodia separada → Si no hay segundo canal: **se
   retiene la contraseña**, nunca se manda junto al paquete.**

## Salida

```
paquete-[proyecto]-[fecha].zip          <- ZIP exterior, AES-256
 └── contenido.zip                      <- ZIP anidado (oculta el indice)
      ├── RESTAURAR-TODO.md             <- archivo maestro y guion de reconstruccion
      ├── MANIFIESTO.md                 <- inventario + checksums SHA-256 + linea de
      │                                    verificacion FECHADA Y FIRMADA
      ├── HUECOS.md                     <- lo que NO viajo, y por que
      ├── RESUMEN-CHATS.md              <- borrador automatico + LECTURA DE UNA PERSONA
      ├── INDICE-ADJUNTOS.md            <- correspondencia nombre neutro <-> nombre real
      ├── 01-instrucciones/
      ├── 02-conocimiento/
      ├── 03-adjuntos/
      ├── 04-descargas/
      ├── 05-skills/
      └── 06-chats/  (C2 por defecto)

## Supuestos de esta versión
[capas no disponibles, seleccion [INDICIO] sin revisar, clases dudosas subidas a C2,
 credenciales rotadas con su fecha]
```

Estado del paquete: **COMPLETO** solo si `HUECOS.md` está vacío y no queda ningún
`[pendiente de escribir]`. En caso contrario se declara *"completo salvo N elementos
declarados"*.

## Límites

- **No migra nada.** Anthropic no soporta migrar datos entre cuentas personales, y esta skill no
  inventa un botón que no existe: produce un paquete de **reconstrucción manual**.
- **No respalda secretos.** Las credenciales son C3 y **se rotan, no se respaldan**.
- El borrador automático de chats **cita y cuenta, no interpreta**. Sin la lectura humana es un
  índice, y venderlo como resumen es prometer lo que el producto no hace.
- Sin el export oficial no hay historial de chats, y esa capa entera va a `HUECOS.md`. El resto
  del respaldo sí se hace.
- Sin `pyzipper` el paquete se entrega **sin cifrar**, y así se declara. No se disimula.
- No sustituye una política de retención ni un cumplimiento normativo: es un respaldo operativo,
  no un archivo legal.

## Reglas

| SIEMPRE | Porqué |
|---|---|
| Respaldar mientras se tiene acceso | El respaldo es una operación del presente; el que se aplaza no existe |
| Pedir el export y descargarlo antes de 24 horas | Es la única vía al historial de chats y su enlace caduca; un export no descargado es una capa perdida |
| Cifrar con AES-256 y anidar el ZIP | Los nombres de archivo son datos, y el directorio central de un ZIP va en claro |
| Separar paquete y clave en dos canales | Un canal comprometido no debe bastar para abrirlo |
| Probar la restauración antes de borrar el origen | Un respaldo no verificado tiene la misma fiabilidad que no tenerlo, con la desventaja de que tranquiliza |
| Declarar los huecos en `HUECOS.md` | Quien reconstruye necesita saber qué le falta; descubrirlo a mitad es peor que saberlo de entrada |
| Escribir la lectura humana sobre el borrador de chats | El script cita y cuenta; qué significó cada decisión solo lo sabe quien estuvo en la conversación |
| Escribir la prueba de humo en el origen | Quien reconstruye no sabe qué debería salir; el autor sí |
| Subir la clase ante la duda, nunca bajarla | El coste de proteger de más es una consulta; el de proteger de menos es irreversible |
| Declarar cuando el paquete va sin cifrar por falta de `pyzipper` | Un paquete que se cree cifrado y no lo está es peor que uno que se sabe en claro |

| NUNCA | Porqué |
|---|---|
| Meter un secreto (C3) en el respaldo | Una clave API respaldada es una clave API filtrada en cuanto el paquete se copia una vez de más. **Se rota, no se respalda** |
| Enviar la contraseña junto al paquete | Anula el cifrado por completo y da falsa sensación de seguridad, que es peor que no cifrar |
| Usar el cifrado ZIP heredado | Roto por ataque de texto conocido desde 1994; la contraseña larga no lo arregla |
| Pasar la contraseña como argumento en la línea de comandos | Queda en el historial del shell y en la lista de procesos del sistema |
| Incluir `DICCIONARIO.md` dentro del paquete redactado | Revierte toda la redacción y convierte el trabajo de redactado en teatro |
| Entregar el borrador automático como resumen ejecutivo | Cita y cuenta, no interpreta; venderlo como resumen es prometer lo que el producto no hace |
| Dar por buena una selección de chats `[INDICIO]` sin revisarla | La coincidencia de texto arrastra chats ajenos y deja fuera chats del proyecto |
| Declarar el respaldo completo con `HUECOS.md` no vacío | Se declara "completo salvo N elementos declarados", que es una frase distinta |
| Borrar el proyecto origen en la misma sesión en que se respalda | La verificación y el borrado deben estar separados por al menos un día y por una persona que confirme |

## Antipatrones

1. **Síntoma**: el correo de entrega contiene el `.zip` y, más abajo, la contraseña — o la contraseña está en un `.txt` dentro del propio paquete. **Causa raíz**: se trató el cifrado como formalidad de proceso, no como control de acceso. **Corrección**: paquete por canal A, contraseña y huella SHA-256 por canal B; si no hay canal B, se retiene la contraseña.

2. **Síntoma**: al listar el ZIP cifrado **sin introducir contraseña** se leen rutas como `03-adjuntos/propuesta-Cliente-Sanchez-450000.pdf`. **Causa raíz**: se asumió que cifrar el ZIP cifra también el índice, y no lo hace: el directorio central va en claro. **Corrección**: ZIP anidado y nombres neutros; la correspondencia vive en `INDICE-ADJUNTOS.md`, dentro del cifrado.

3. **Síntoma**: el manifiesto no tiene línea de verificación fechada —o la tiene fechada en el mismo minuto exacto que la creación del paquete— y, al restaurar meses después, las instrucciones citan `CATALOGO.md` que no está en `02-conocimiento/`. **Causa raíz**: se confundió "el comando terminó sin error" con "el paquete se puede restaurar", y las capas se respaldaron por separado sin comprobar referencias cruzadas. **Corrección**: restauración en frío en carpeta vacía distinta, tres archivos de tres carpetas, línea fechada y firmada; y la comprobación de referencias cruzadas manda lo citado y ausente a `HUECOS.md`.

4. **Síntoma**: una cadena tipo `sk-`, `ghp_`, `AKIA` o `Bearer ` aparece en cualquier archivo del paquete, **incluidas las transcripciones de chats**, donde las claves se pegan sin pensar. **Causa raíz**: se aplicó "esto también forma parte del proyecto" a algo cuyo valor es exclusivamente el acceso que concede. **Corrección**: rotarlo en origen y dejar `[REDACTADO:credencial — rotada AAAA-MM-DD]`; el sellado se detiene solo.

5. **Síntoma**: `RESUMEN-CHATS.md` contiene líneas `LECTURA DE UNA PERSONA: [pendiente de escribir]` dentro de un paquete ya sellado y declarado completo. **Causa raíz**: se confundió extraer citas con entender la conversación: la máquina hizo su mitad y nadie hizo la otra. **Corrección**: la lectura humana va antes del sellado, y el autocontrol comprueba que haya **cero** `[pendiente de escribir]` en un paquete declarado COMPLETO.

## Casos de prueba

Los cuatro casos están en `cases/`. El quinto, de datos sucios, sigue en
[`references/casos.md`](references/casos.md) junto al detalle de los demás.

**Happy path** (`cases/case_01_happy_path.md`): proyecto Pro con export que trae campo de
proyecto, 22 documentos, 4 adjuntos y 2 skills. Paquete COMPLETO con `HUECOS.md` vacío.

**Edge case** (`cases/case_02_edge_case.md`): export **sin** campo de proyecto. El filtro por
coincidencia de texto se marca `[INDICIO]` y se revisa a mano: arrastra tres chats ajenos y deja
fuera uno propio.

**Failure** (`cases/case_03_failure.md`): el export no se solicitó a tiempo y el enlace caducó. La
capa de chats entera va a `HUECOS.md` y **las otras cinco capas se respaldan igual**.

**Integration** (`cases/case_04_integration.md`): encadenado con
`universal-compilador-contexto`, que consume el `chats.jsonl` de este respaldo como una de sus
fuentes de ingesta.

## Ficha comercial

Ver `ANEXO-A-ficha-comercial.md`.

## Versión

v2.1.0 — ver `CHANGELOG.md`.
