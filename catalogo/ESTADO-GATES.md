# Matriz de gates y riesgos abiertos

Los cinco gates de la casa: **G1** producto (≥16/20) · **G2** prueba (3 casos
reales, uno sucio) · **G3** precio (comprador nombrado + cifra firmada) ·
**G4** legal (licencia verificada) · **G5** público (sin cifra inventada).

## Hostelería

| Skill | G1 | G2 | G3 | G4 | G5 | Nota |
|---|:--:|:--:|:--:|:--:|:--:|---|
| `escandallo-ingenieria-menu` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 |
| `respuesta-resenas` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 · v1.2.0 reestructurada |
| `apertura-cierre-turno` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 · v1.1.2 atribución cerrada |
| `comparativa-proveedores` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 |
| `receta-estandar` | ✅ | ❌ | ✅ | ❌ | ✅ | 19/20 · **G4 abajo solo por (a): revisión técnica externa** |
| `productividad-personal-turno` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 |
| `reporte-inteligencia-competencia` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 · dentro de la Completa, sin suscripción hasta 3 instalaciones vivas |

G3 y G5 levantados en las siete el 15-sep-2026 (`DECISIONES.md` §6). G2 lo levanta la
primera instalación vendida.

## CABINA (DJ)

Ficha comercial escrita para las seis y **envoltorio cerrado el 15-sep-2026**. Nota medida con
el validador de la casa (`validar_skill.py`), no estimada.

| Skill | Antes | Ahora | G1 | G2 | G3 | G4 | G5 |
|---|---|---|:--:|:--:|:--:|:--:|:--:|
| `auditoria-de-biblioteca` | 0/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ✅ |
| `postmortem-de-bolo` | 1/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ✅ |
| `presupuesto-y-contrato-evento` | 1/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ✅ |
| `set-por-encargo` | 2/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ✅ |
| `peticiones-a-repertorio` | 2/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ✅ |
| `demo-a-sello` | 2/20 | **19/20** | ✅ | ❌ | ✅ | ✅ | ✅ |

**Por qué 19 y no 20.** El validador devuelve **20/20 mecánico** en las seis. No se firma el 20:
el punto 19 es de criterio —*"que las URLs estén verificadas, no solo presentes"*— y en esta
pasada no se han reverificado una a una. Es el mismo criterio con el que la casa corrigió a la
baja el 20/20 de `escandallo-ingenieria-menu`. **No se redondea al alza.**

**Qué se cerró en cada una:** estructura de 13 secciones del ADN, procedimiento en 6 pasos
atómicos con el molde Entrada → Acción → Salida → Si falta el dato, 10 reglas SIEMPRE y 9 NUNCA
con su porqué, 5 antipatrones con síntoma/causa/corrección, los 4 casos de prueba con entrada y
salida reales, y los ficheros del peldaño P1: `CHANGELOG.md`, `README.md`, `LICENSE.txt`,
`metadata.json` y `references/FUENTES.md` donde faltaba.

**El contenido de oficio no se tocó.** Las notas de 0-2/20 nunca midieron la calidad del
oficio: medían conformidad de formato. Las tablas de riesgo por hallazgo, las seis curvas de
energía, los cuatro cubos con sus umbrales, las seis cláusulas críticas y los plazos de Beatport
y Spotify ya estaban y son el producto. Lo que faltaba era la forma que la casa exige para poder
cobrar.

**G3 levantado** el 15-sep-2026: 49 € suelta, 149 € CORE, 99 € EVENTOS, 249 € COMPLETA.
**G4 en orden**: licencia de comprador redactada en las seis, y `presupuesto-y-contrato-evento`
lleva además aviso legal no negociable de que no es asesoramiento jurídico.

**G2 sigue abajo, y solo lo levanta el primer comprador.** Los 4 casos de cada skill son de
fabricación: ninguna se ha ejecutado contra los datos reales de alguien que haya pagado.

**Calibración del validador:** contra las skills de hostelería devuelve 17-19/20, coincidiendo
con sus notas declaradas. Es fiable.


## Neutra / B2B

| Skill | G1 | G2 | G3 | G4 | G5 | Nota |
|---|:--:|:--:|:--:|:--:|:--:|---|
| `cobro-cartera-vencida` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 · 79 € · la mejor posicionada para venta suelta |
| `reporte-inteligencia` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 · 49 € · reauditada tras v1.1.0, ahora v1.2.0 |
| `respaldo-proyecto-ia-cl` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 · 49 € / 89 € en PACK CONTEXTO · medida con el validador, ya no autoevaluación |
| `universal-compilador-contexto` | ✅ | ❌ | ✅ | ✅ | ✅ | 19/20 · 49 € / 89 € en PACK CONTEXTO · ídem |

Las cuatro cerraron envoltorio y ficha comercial el 15-sep-2026. G2 lo levanta el primer comprador por Gumroad.

---

## Riesgos abiertos

### 1 · ~~`checklist-turno` duplica a `apertura-cierre-turno`~~ ✅ RESUELTO (15-sep-2026)

Las dos skills tienen **la misma descripción palabra por palabra** y el mismo
producto. Las licencias se contradicen:

- `apertura-cierre-turno` → *"uso comercial sin derecho de redistribución"* (se vende)
- `checklist-turno` → *"uso libre, incluido el comercial, con atribución"* (regalada)

Vender una pieza de la Instalación Completa mientras su gemela circula con
licencia de uso libre es un problema comercial real, no una cuestión de orden.
**Retirada `checklist-turno`, se conserva `apertura-cierre-turno`** (la auditada, con ficha y
licencia de venta). Decisión en [`DECISIONES.md`](DECISIONES.md).

✅ **Ejecutado el 15-sep-2026**, confirmado por Sergio: `checklist-turno`
(`skill_01RfEvhHA5Ex5x9ufLoF8955`) borrada de la cuenta. Ya no hay una pieza con licencia de uso
libre circulando al lado de la que se vende. **Riesgo cerrado.**

### 2 · Ninguna pieza ha pasado G2: cero ejecuciones contra datos reales de cliente

Es el gate que falla en todo el catálogo de hostelería. Las fichas lo declaran
sin adornos: *"los 4 casos son de fabricación. Falta ejecutarla contra 3 exports
reales de un cliente real, uno con datos sucios."* Un 19/20 en una pieza que
nunca se ha ejecutado con los datos de un cliente es nota de fábrica, no de
campo. Esto no impide vender una instalación presencial —se ejecuta en la visita
con los datos del propio cliente, que es precisamente cómo está diseñado el
Motor B—, pero sí desaconseja publicar en directorio.

### 3 · ~~Atribución en corrección centralizada en `apertura-cierre-turno`~~ ✅ CERRADA (15-sep-2026, v1.1.2)

Las cuatro cifras de rotación que sostenían el producto estaban "en corrección centralizada" desde
el 15-ago-2026, con el aviso de **no usarlas en material de venta**. Quedan ancladas a autor, año
y URL:

| Cifra | Autor | Fuente |
|---|---|---|
| Rotación España **63,8 %** | **Synergie España** | *La situación del empleo en el sector Hospitality en España 2026* |
| Sustitución **2.800–5.000 €** | **Linkers** | análisis de la consultora, abr-2026 |
| Rotación México **80–120 %** | **CANIRAC** | vía La Jornada, 21-feb-2024 |
| Vacante México **2–3× salario** | **CANIRAC** | misma fuente |

**Ya se pueden usar en argumentario**, con una condición que no es opcional: siempre con el nombre
de quien las publica. Ninguna de las tres fuentes publica tamaño de muestra ni metodología —dos son
empresas del sector y una es la cámara patronal—, así que van marcadas
`[SIN TAMAÑO DE MUESTRA PUBLICADO]` y **nunca como dato oficial**. No son INE.

**Y de paso, tres defectos que el validador destapó al revisarla**, en una de las tres piezas del
Esencial de 2.500 €:

1. **`allowed-tools: []` rompía el empaquetado** — la spec exige cadena separada por espacios, no
   lista, y el validador lo marca como error duro de subida. Mismo tipo de defecto que el
   frontmatter YAML inválido de otras tres piezas: no se ve hasta que falla en casa del comprador.
2. Los pasos 6 y 7 sin rama "si falta el dato": solo 5 de 7 cumplían el molde.
3. 7 reglas NUNCA donde la rúbrica pide 8.

La pieza pasa de **17/20 a 19/20 declarado** (20/20 mecánico).

### 4 · Sobre la protección del archivo

De la doctrina, literal: *"No existe protección técnica de un archivo de texto, y
esta skill nunca la promete. Una skill es texto plano: no hay DRM, ni firma, ni
ofuscación posible. Cualquier comprador puede copiarla y pasársela a diez
colegas. Lo defendible es la cadencia de actualización, el acceso revocable, la
configuración con datos del cliente, el criterio de oficio y la velocidad de la
fábrica. Quien venda protección del archivo, miente."*

Por eso la entrega va por acceso revocable a este repositorio privado y no por
adjunto.


### 5 · ~~`respuesta-resenas` envía la v1.0.0~~ ✅ RESUELTO (15-sep-2026, v1.2.0)

**Corrección del diagnóstico inicial.** Se dijo que el trabajo de la v1.1.0 no se había hecho.
**Era incorrecto.** Las cuatro piezas que la ficha declaraba haber fabricado el 16-ago —
procedimiento atómico, tabla SIEMPRE, tabla NUNCA y antipatrones — **sí estaban en el fichero y
sí pasaban la rúbrica** (puntos 07, 10, 11 y 12).

Lo que fallaba era otra cosa, y eran tres problemas:

1. **La versión decía tres cosas distintas en cuatro sitios.** Frontmatter `1.0.0`, sección
   `## Versión` del mismo fichero `v1.1.0`, `metadata.json` `1.1.0`, y el CHANGELOG sin ninguna
   entrada de 1.1.0.
2. **Estructura anterior al ADN.** Usaba `## Método` y `## Formato del informe` en vez de las 13
   secciones de serie, así que caía en 12 puntos **por nomenclatura**, no por contenido ausente.
3. **`## Casos de prueba` no rotulaba** los cuatro casos como Happy path / Edge case / Failure /
   Integration, de modo que existían en `cases/` y aun así los puntos 13-16 caían.

**Resuelto en v1.2.0**: reestructurada al ADN conservando verbatim procedimiento, reglas y
antipatrones; versión unificada en los cuatro sitios. De **8/20 a 19/20** (20/20 mecánico, menos
el punto 19 de criterio). Se salta a 1.2.0 porque **el número 1.1.0 está quemado**: quien lo vio
estaba viendo un fichero de 8/20.


### 6 · Frontmatter YAML inválido en 3 skills — **corregido el 15-sep-2026**

`auditoria-de-biblioteca`, `presupuesto-y-contrato-evento` y
`reporte-inteligencia` tenían la `description` como escalar plano conteniendo
`: ` (dos puntos y espacio), que **no es YAML válido**. Ejemplo:
`description: ... Solo lectura: nunca escribe en la base de datos del DJ.`

Es el antipatrón nº 2 de la doctrina, literal: *"la skill entregada al cliente da
error al cargarse en su entorno, o no aparece en su lista de capacidades"*.
Vender un activo que puede no cargar en casa del comprador es la peor primera
impresión posible, y el fallo no se ve hasta que está entregado.

**Corregido** pasando las tres a escalar de bloque `>-`, que es el formato que ya
usaban las skills de hostelería. El texto es idéntico carácter a carácter —solo
cambia el envoltorio—. Verificado: **17/17 frontmatter del catálogo parsean
correctamente.**

Conviene añadir esta comprobación al empaquetado, que es lo que la propia
doctrina manda: *"ejecutar el validador antes de empaquetar, sin excepción"*.

### 7 · Frontmatter YAML: los seis de CABINA revalidados

Tras la reescritura, los seis `SKILL.md` de CABINA vuelven a parsear correctamente y sus
`metadata` mantienen todos los valores como cadena, conforme a la especificación. **17/17 del
catálogo válidos.**

### 8 · ~~Cinco skills más con el mismo problema de envoltorio~~ ✅ CERRADO (15-sep-2026)

Las cinco pasan el umbral. Medido con `validar_skill.py`, no estimado.

| Skill | Línea | Antes | Ahora | Versión |
|---|---|---|---|---|
| `cobro-cartera-vencida` | Neutra | declaraba 19/20 · medía **1/20** | **19/20** | 1.2.0 |
| `reporte-inteligencia` | Neutra | declaraba 18/20 · medía **2/20** | **19/20** | 1.2.0 |
| `respaldo-proyecto-ia-cl` | Neutra | declaraba 18/20 · medía **3/20** | **19/20** | 2.1.0 |
| `universal-compilador-contexto` | Neutra | declaraba 17/20 · medía **1/20** | **19/20** | 1.1.0 |
| `reporte-inteligencia-competencia` | Hostelería | sin nota · medía **1/20** | **19/20** | 1.1.0 |

Mismo trabajo que en CABINA: 13 secciones del ADN, pasos atómicos con el molde de la serie,
reglas en tabla con su porqué, 5 antipatrones, los 4 casos de prueba y los ficheros del peldaño.
**El contenido de oficio no se tocó en ninguna.**

Lo que faltaba, pieza por pieza:

- **`reporte-inteligencia-competencia`** era la más desnuda del catálogo: tenía un `SKILL.md`
  bueno **y nada más**. Ni README, ni CHANGELOG, ni LICENSE, ni metadata, ni cases, ni
  references.
- **`cobro-cartera-vencida`** tenía las reglas como listas numeradas en vez de tablas, los
  antipatrones con los dos puntos dentro de la negrita, y sus tres fuentes europeas viviendo en
  el `SKILL.md` en lugar de en `references/`, de modo que el recuento de URLs daba cero.
- **`respaldo-proyecto-ia-cl`** y **`universal-compilador-contexto`** tenían 12 y 6 fases con el
  molde correcto pero repartido en viñetas, y 6 antipatrones donde la rúbrica pide 5.

**Estado del catálogo: 17 de 17 por encima del umbral.** Las 17 están en 20/20 mecánico, y
las fichas declaran 19/20 en las revisadas porque el punto 19 —URLs verificadas una a una— no se
ha confirmado en esta pasada. No se redondea al alza.

### 9 · Solape comercial entre las dos piezas de inteligencia — **declarado**

`reporte-inteligencia-competencia` es la **vertical de hostelería** de `reporte-inteligencia`:
mismo panel de seis, misma lógica de mediana y brecha, cuatro métricas en vez de ocho, salida de
una página en vez de diez secciones. **No son duplicados**, como lo eran `checklist-turno` y
`apertura-cierre-turno`, pero **no se venden las dos al mismo comprador**: a un restaurante se le
vende la vertical, a cualquier otro sector la neutra. Queda declarado en las dos fichas.

En cambio `respaldo-proyecto-ia-cl` y `universal-compilador-contexto` **sí se venden juntas**: son
la misma cadena en dos mitades y el `chats.jsonl` y el `HUECOS.md` de la primera son entradas
directas de la segunda.

### 10 · `receta-estandar`: discrepancia AESAN / RD 3484/2000 en mantenimiento en caliente — **detectada y aplicada, pendiente de confirmar por el consultor**

Al anclar las tres cifras de inocuidad que la v1.1.0 declaraba como riesgo legal, apareció que
**dentro de España las dos fuentes oficiales no coinciden**: el informe AESAN-2021-004 fija el
mantenimiento en caliente en **≥63 °C** y el Real Decreto 3484/2000, art. 7, en **≥65 °C**. El
RD es norma reglamentaria; AESAN es opinión científica. Ante inspección prevalece el RD.

**Se ha aplicado la cifra reglamentaria** (dirección conservadora: más estricta) en los casos
españoles, y la discrepancia está declarada en `temperaturas_haccp.md`, en el `SKILL.md`, en
`FUENTES.md` (fuente 7, nueva, con URL del BOE) y en la cláusula 6 del anexo contractual. **Los
binomios de cocinado no se han tocado**: siguen siendo de AESAN y el RD no los regula.

Lo mismo con el **4 °C, que significa cosas distintas en cada país**: en España es conservación
de más de 24 h (RD art. 7); en México es recepción de pescado fresco (NOM-251 §7.4.2), y la
conservación es ≤7 °C (§7.3.3). Una ficha que ponga "≤4 °C" sin decir cuál de las dos es no
sirve en ninguno de los dos. Declarado en la tabla de discrepancias.

**Estado del G4 de `receta-estandar` tras esto:** de los tres requisitos de su ficha, **(c)**
divergencia de versión → cerrado; **(b)** cláusula contractual → redactada en
`venta/ANEXO-CONTRATO-INOCUIDAD.md`, pendiente de revisión jurídica; **(a)** revisión técnica
externa → **pendiente, y es la única que no puede hacer la casa**. La pieza pasa de 17/20 a
19/20 declarado y **sigue sin facturarse** hasta que (a) esté hecha.