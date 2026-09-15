# FUENTES · respaldo-proyecto-ia-cl v2.0.0

Cada fuente está anclada a la afirmación concreta que sostiene. Una fuente que no
sostiene ninguna línea del SKILL.md se elimina, no se decora.

---

## A · Qué permite y qué no permite la plataforma

### A1 · No hay migración entre cuentas personales `[VERIFICADO · CITA LITERAL]`
Centro de Ayuda de Claude, *Export your Claude data*, art. 9450526.
<https://support.claude.com/en/articles/9450526-export-your-claude-data>

> "Exported data can't be imported into another personal Claude account, and we
> don't support migrating data between personal accounts."

**Sostiene:** el bloque "LO PRIMERO QUE HAY QUE SABER" y toda la razón de ser del
paso P9 (reconstrucción manual en lugar de importación).

### A2 · Qué contiene la exportación nativa `[VERIFICADO · CITA LITERAL]`
Mismo artículo.

> "Data exports include conversation data and the user data for your account."

> "The download link will expire 24 hours after delivery."

**Sostiene:** que la exportación nativa **no es sustituto de esta skill**. El
artículo no declara que la base de conocimiento de los proyectos ni los adjuntos
viajen en ese volcado, y el enlace caduca en 24 h.
**Hueco declarado:** no se ha localizado documentación oficial que enumere el
contenido exacto del volcado archivo por archivo. Lo que esta skill afirma sobre
la exportación nativa se limita a lo citado arriba.

### A3 · Composición de un Proyecto `[VERIFICADO]`
Centro de Ayuda, *How can I create and manage projects?*, art. 9519177.
<https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>

Un proyecto se compone de base de conocimiento, instrucciones, chats y —en Team y
Enterprise— miembros y permisos. Declara además: *"Free users can create a maximum
of five projects"* y que al acercarse al límite de contexto se activa modo RAG.

**Sostiene:** las capas L1–L5 de P1 y la fila de ">100 documentos o modo RAG" de la
matriz de aplicabilidad.
**No sostiene:** el artículo **no documenta** copiar, duplicar ni transferir un
proyecto. Esa ausencia está declarada como tal en la matriz, no rellenada.

### A4 · Traslado de cuenta personal a organización `[LOCALIZADA, NO APLICADA]`
Centro de Ayuda, *Move your personal Claude account to a Team or Enterprise
organization*, art. 9267400.
<https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization>

**Sostiene:** la fila "Cuenta personal → organización" de la matriz, marcada
⚠️ Parcial con la instrucción de comprobarlo antes de reconstruir a mano.
**Estatus honesto:** el procedimiento existe y está documentado; esta skill **no lo
ha ejecutado ni verificado paso a paso**. Por eso la matriz dice "compruébalo
antes", no "hazlo así".

### A5 · Exportación de organización `[VERIFICADO · CITA LITERAL]`
Centro de Ayuda, *Export your organization's data*, art. 13346720.
<https://support.claude.com/en/articles/13346720-export-your-organization-s-data>

> "Organization data exports are only available to Team and Enterprise plan
> Primary Owners."

> "Messages, files, and projects deleted from your account, either manually by
> individual users or via enterprise retention settings, will not be included in
> data exports initiated after the deletion."

**Sostiene:** la regla SIEMPRE-1 ("respalda mientras tienes acceso") y la fila
"Aquí NO aplica" de la matriz. Lo borrado no vuelve.

### A6 · Caducidad del enlace del export `[VERIFICADO · CITA LITERAL]`
Mismo artículo que A1/A2 (art. 9450526), re-verificado el 2026-08-16.

> "The download link will expire 24 hours after delivery."

**Sostiene:** el paso P0, la regla SIEMPRE-2 de v2 y el case_03_failure: un
export no descargado en plazo es una capa perdida hasta volver a solicitarlo.

**Hueco declarado que la v2 hereda de la v1:** Anthropic **no publica** la
estructura interna del ZIP del export (nombres de archivo, esquema JSON). Por
eso `--ingerir` identifica el volcado por su estructura y acepta tres formas de
mensaje (`text` plano, `content` en bloques, `parts`), todas observadas en
exports reales pero ninguna garantizada por documentación oficial. Si el
formato cambia otra vez, el modo degradado es: `--ingerir` no reconoce nada,
lo dice, y L5 va a HUECOS.md — nunca inventa conversaciones.

---

## B · Por qué AES-256 y no el cifrado ZIP heredado

### B1 · El cifrado ZIP clásico está roto `[FICHA BIBLIOGRÁFICA VERIFICADA · TEXTO COMPLETO NO LEÍDO]`
Biham, E. y Kocher, P. (1994). *A Known Plaintext Attack on the PKZIP Stream
Cipher*. Fast Software Encryption.

**Sostiene:** la regla NUNCA-3 y la decisión técnica 1 de P6. Un solo archivo
cuyo contenido el atacante conozca —una plantilla, un encabezado, un logotipo—
basta para recuperar el estado interno del cifrador y abrir el resto del paquete.
La longitud de la contraseña **no** mitiga este ataque.

### B2 · Ataques con texto conocido reducido `[FICHA BIBLIOGRÁFICA VERIFICADA · TEXTO COMPLETO NO LEÍDO]`
Stay, M. (2001). *ZIP Attacks with Reduced Known Plaintext*. Fast Software
Encryption.

**Sostiene:** que el requisito de texto conocido del ataque B1 es menor de lo que
la intuición sugiere. Refuerza NUNCA-3.

### B3 · El esquema WinZip AES tuvo defectos propios `[PDF LOCALIZADO EN SERVIDOR DEL AUTOR · NO LEÍDO ÍNTEGRO]`
Kohno, T. (2004). *Attacking and Repairing the WinZip Encryption Scheme*.
ACM CCS. <https://homes.cs.washington.edu/~yoshi/papers/WinZip/winzip.pdf>

**Sostiene el DEBATE, no la recomendación.** Es la fuente que impide vender
AES-256 en ZIP como solución perfecta: los defectos que documenta están en el
*esquema* (uso de metadatos, mezcla de métodos de cifrado en un mismo archivo),
no en el algoritmo AES. Ver la sección DEBATE más abajo.

### B4 · El formato ZIP no cifra los nombres de archivo `[VERIFICADO EN ESTE ENTORNO]`
Comprobación directa ejecutada el 2026-08-15 con `pyzipper` 0.3.x y AES-256:

- ZIP cifrado **sin anidar** → `zipfile.ZipFile(...).namelist()` devuelve
  `['03-adjuntos/propuesta-Cliente-Sanchez-450000.pdf']` **sin introducir la contraseña**.
- ZIP cifrado **anidado** por `scripts/respaldo.py` → `namelist()` devuelve
  `['contenido.zip']`, y leerlo sin contraseña falla con
  `RuntimeError: File 'contenido.zip' is encrypted, password required`.

**Sostiene:** el antipatrón 2, la regla SIEMPRE-2 y la decisión técnica 2 de P6.
Es la única afirmación de este documento verificada por ejecución propia y no por
lectura. **Limitación:** comprobado con `pyzipper`; no se ha comprobado el
comportamiento de 7-Zip, WinZip ni Keka sobre el mismo archivo.

---

## C · Parámetro numérico propio

### C1 · Longitud mínima de contraseña: 20 caracteres `[CRITERIO DEL AUTOR]`
El script avisa por debajo de 20 caracteres. **No es una norma ni procede de
ninguna fuente citada aquí.** El razonamiento, que el lector puede rechazar: la
contraseña de un respaldo se escribe una vez, se guarda en un gestor y no se teclea
a diario, así que el coste de que sea larga es cercano a cero, mientras que el
paquete puede quedar accesible a un atacante durante años y sin límite de intentos.

**Esta skill no publica ningún otro umbral de seguridad.** No fija tiempos de
retención, ni caducidad de contraseña, ni algoritmos de derivación de clave: eso
depende de la política de cada organización y no se inventa aquí.

---

## DEBATE ABIERTO · ¿es suficiente un ZIP cifrado con AES-256?

**A favor.** No requiere instalar nada en el lado del receptor: 7-Zip, WinZip,
Keka y el explorador de la mayoría de sistemas abren AES-256 en ZIP. Para un
respaldo que viaja entre dos personas, la fricción cero es lo que hace que el
control se use de verdad en lugar de saltarse.

**En contra.** Kohno (B3) documentó defectos en el esquema, no en el algoritmo; el
formato deja metadatos en claro (B4); y un ZIP con contraseña no ofrece
autenticación del remitente: quien reciba el paquete no puede probar quién lo
generó. Para eso hacen falta herramientas de cifrado con firma —GnuPG, age— que
cifran el archivo entero, nombres incluidos, y permiten firmar.

**Resolución de diseño de esta versión:** AES-256 en ZIP **con anidado
obligatorio**, porque el anidado cierra el hueco de metadatos que es el más
explotable de los tres, y porque el receptor típico de este paquete es una persona
que no va a instalar GnuPG para abrirlo. La firma del remitente se sustituye por
un control de menor coste y menor garantía: la huella SHA-256 entregada por un
canal distinto (P8). **Es un control más débil que una firma criptográfica y así
se declara.** Quien necesite no repudio debe usar GnuPG o age, y esta skill no lo
cubre tampoco en v2.0.0.

---

## RECUENTO HONESTO DE ESTE DOCUMENTO

| Estatus | Cuántas | Cuáles |
|---|---|---|
| Verificada con cita literal del original | 4 | A1, A2, A3, A5 |
| Localizada, documentada, **no ejecutada** | 1 | A4 |
| Ficha bibliográfica verificada, **texto completo no leído** | 3 | B1, B2, B3 |
| Verificada por ejecución propia en este entorno | 1 | B4 |
| Criterio del autor, sin fuente | 1 | C1 |

**7 fuentes externas distintas.** La debilidad conocida de este documento: las
tres referencias criptográficas (B1–B3) se citan por ficha, no por lectura del
texto completo. Sostienen una recomendación —usa AES, no ZipCrypto— que es
consenso amplio del campo, pero quien quiera discutir los detalles del ataque debe
ir al original. Sigue en el roadmap.

---

**Actualizado 2026-08-16 · respaldo-proyecto-ia-cl v2.0.0.**
