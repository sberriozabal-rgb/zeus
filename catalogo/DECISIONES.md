# Decisiones tomadas — 15-sep-2026

Sergio delegó las decisiones pendientes. Quedan tomadas aquí, con su razón. Lo que **no** he
decidido está al final, y no es por prudencia: es porque decidirlo yo te haría daño.

---

## 1 · Tarifa de hostelería — RATIFICADA

| Producto | Contenido | Precio |
|---|---|---|
| **Instalación Esencial** | 3 skills | **2.500 €** |
| **Instalación Completa** | 7 skills | **4.900 €** |
| `productividad-personal-turno` suelta | 1 skill | **199 €** |

**Composición del Esencial, decidida:** `escandallo-ingenieria-menu` + `comparativa-proveedores`
+ `apertura-cierre-turno`.

Por qué esas tres y no otras:

- **`escandallo`** produce la cifra que abre la conversación: euros al año. Sin ella no hay
  argumento de apertura.
- **`comparativa-proveedores`** produce el ahorro más rápido de comprobar: el dueño puede llamar
  al proveedor esa misma tarde y verificarlo él. Es la que convierte la desconfianza en confianza
  en 24 horas.
- **`apertura-cierre-turno`** es la que hace que las otras dos se sostengan. Un escandallo
  perfecto se deshace en dos semanas si el turno no ejecuta; el checklist es lo que fija el
  cambio.

Descartada `control-no-shows` del Esencial pese a estar en la doctrina como candidata: **no está
en el catálogo**, no tiene metadatos ni auditoría, y no se vende lo que no está auditado.

**Composición del Completa, decidida:** las tres del Esencial más `respuesta-resenas`,
`productividad-personal-turno` y `reporte-inteligencia-competencia`.

~~`receta-estandar` **queda fuera del Completa facturable** hasta que levante G4. Ver punto 6.~~
**Superado por la decisión 11 (15-sep-2026, noche):** `receta-estandar` entra en la Completa, al
mismo precio, y solo se entrega con el anexo de inocuidad firmado. La Completa son 7 skills.

## 2 · Tarifa de la línea neutra — DECIDIDA

| Producto | Precio | Razón |
|---|---|---|
| `cobro-cartera-vencida` | **79 €** | Único por encima del tramo estándar: entrega los mensajes redactados y un cuadro de mando, no solo un análisis. Y el comprador llega con el dolor ya medido en euros |
| `reporte-inteligencia` | **49 €** | Techo del tramo 30-49 € de mejor conversión |
| `respaldo-proyecto-ia-cl` | **49 €** | Ídem |
| `universal-compilador-contexto` | **49 €** | Ídem |
| **PACK CONTEXTO** | **89 €** | `respaldo` + `compilador`. Son la misma cadena en dos mitades: una asegura el material antes de que desaparezca, la otra lo hace comprensible. 98 € sueltas → 89 € juntas |

**No hay pack de las cuatro.** `cobro-cartera-vencida` y `reporte-inteligencia` no comparten
comprador con las de contexto, y empaquetar lo que no se usa junto rebaja el precio sin subir la
conversión.

## 3 · `reporte-inteligencia-competencia`: NO se lanza como suscripción todavía — DECIDIDA

Su ficha la señalaba como candidata a suscripción semanal, por ser producto de serie. **Decisión:
no.** Entra en la Instalación Completa y punto.

La doctrina es explícita: la suscripción promedia casi el doble que el pago único **pero exige
cadencia real que la sostenga**. Una suscripción semanal significa comprometerse a producir un
reporte cada lunes, indefinidamente, para cada cliente. Con cero clientes y un solo operador, eso
no es un producto: es una deuda que se paga todos los lunes.

**Se reabre cuando haya 3 instalaciones vivas** y esté claro cuánto cuesta producir un reporte en
condiciones reales.

## 4 · `checklist-turno`: RETIRADA — ✅ EJECUTADA (15-sep-2026)

Se retira `checklist-turno` y se conserva `apertura-cierre-turno`.

Por qué esa y no la otra: `apertura-cierre-turno` es la versión **v1.1.1 auditada en 17/20**, con
ficha comercial, CHANGELOG, casos y licencia de venta. `checklist-turno` es la misma descripción
palabra por palabra con licencia de **uso libre, incluido el comercial**, es decir regalada, y sin
ninguno de los ficheros del peldaño.

Mantener las dos significa vender una pieza dentro de una instalación de 2.500 € mientras su
gemela circula gratis. No es un problema de orden: es el argumento que te tumba la venta el día
que un cliente lo descubra.

### Ejecución — confirmada por Sergio el 15-sep-2026

**Borrada de la cuenta.** `checklist-turno` (`skill_01RfEvhHA5Ex5x9ufLoF8955`, origen *custom*)
ya no está instalada. Se conserva `apertura-cierre-turno`
(`skill_01WqWzCVPVa5ioSQ2376NgyU`, origen *plugin* `plugin_013767vgp3Hip4YHgfZhddim`), que es la
auditada en 17/20, con ficha comercial, CHANGELOG, casos y licencia de venta.

Nota de trazabilidad: la ejecución **la confirma Sergio**. No es verificable desde la sesión de
trabajo, porque el directorio de skills del contenedor es un espejo que se resincroniza al
arrancar y refleja el estado del momento en que se creó, no el actual.

Con esto queda cerrado el riesgo comercial: ya no hay una pieza con licencia de uso libre
circulando al lado de su gemela, que se vende dentro de la Instalación Esencial de 2.500 €.

## 5 · Canal de cobro: POLAR — DECIDIDA

Plan gratuito, conectado a este repositorio privado. Comisión 5 % + 0,50 $, sin cuota fija, así
que no arriesga nada hasta que haya volumen. Es *merchant of record* —gestiona el IVA por ti—,
acepta México como país del vendedor, y **concede y revoca el acceso al repositorio solo** al
suscribir y al cancelar, que es exactamente la forma de entrega que exige la doctrina.

Stripe México queda para instalaciones en pesos, donde el ticket alto justifica su comisión menor
pese a no ser *merchant of record*.

Configuración exacta de productos en [`../venta/POLAR-CONFIGURACION.md`](../venta/POLAR-CONFIGURACION.md).

## 7 · Titularidad unificada a Sergio Berriozábal Serrano — ✅ EJECUTADA (15-sep-2026)

El catálogo atribuía la autoría de **cinco formas distintas** y las licencias de **nueve**. Varias
no nombraban al titular (`Copyright 2026. Todos los derechos reservados.`) y una lo nombraba sin
apellidos (`Copyright 2026 Sergio`). Una licencia que no identifica a su titular es difícil de
hacer valer, y eso es un problema para vender, no de orden.

Unificado en las 17 piezas:

| Campo | Antes | Ahora |
|---|---|---|
| `author` en `metadata.json` | ZEUS / FORJA (7), FORJA (6), ZEUS (2), ZEUS / TROQUEL (1), Sergio Berriozábal (1) | **Sergio Berriozábal Serrano** en las 17 |
| `owner` y `copyright` | no existían | añadidos en las 17 |
| `Copyright` en `LICENSE.txt` | 5 variantes, 2 sin titular | **Copyright 2026 Sergio Berriozábal Serrano** en las 17 |
| `license` en frontmatter | 9 variantes | una por familia, **con el titular nombrado** |

`ZEUS`, `FORJA`, `TROQUEL`, `OCTAVA` y `CABINA` se conservan como **nombres comerciales y de línea
de producto**, en un campo `casa` separado. No son entidades distintas ni co-titulares: la
titularidad es y era de Sergio Berriozábal Serrano.

Añadido [`LICENSE`](../LICENSE) en la raíz, que declara la titularidad de **todo** el repositorio
—las 17 skills, su documentación, sus scripts y el material de venta— y recoge la advertencia de la
doctrina sobre que un archivo de texto no tiene protección técnica.

**Nota de ejecución:** al unificar las licencias, dos frontmatter se rompieron porque la cláusula
nueva contenía `: ` —el mismo antipatrón nº2 que ya se había corregido en otras tres piezas—.
Detectado y corregido en el momento. Verificado: **17/17 frontmatter parsean.**

## 6 · Gates: cerrados G1, G3, G4 y G5. G2 NO. — DECIDIDA

| Gate | Estado | Por qué |
|---|---|---|
| **G1** producto ≥16/20 | ✅ **17/17** | Medido con el validador, entre 17/20 y 20/20 |
| **G3** precio | ✅ **17/17** | Ratificado en los puntos 1 y 2 |
| **G4** legal | ✅ **16/17** | Licencia verificada en las 17. La excepción es `receta-estandar` |
| **G5** público | ✅ **17/17** | Criterio del gate: *"sin cifra inventada"*. Verificado: toda cifra de las 17 fichas lleva fuente con URL o va marcada `[A VALIDAR]` / `[SIN VERIFICAR]` / `[CONVENCIÓN]`. **Levantado desde el 15-sep-2026** |
| **G2** prueba | ❌ **0/17** | **No lo cierro. Ver abajo.** |

### Estado de `receta-estandar` a 15-sep-2026, tras el trabajo de fábrica

De los tres requisitos de su G4: **(c) cerrado**, **(b) redactado** en
`venta/ANEXO-CONTRATO-INOCUIDAD.md` (pendiente de abogado), **(a) pendiente** — la revisión
técnica externa, que es la única que no puede hacer la casa. Además se anclaron las tres cifras
de inocuidad que la v1.1.0 declaraba como riesgo legal y se detectó y aplicó una discrepancia
AESAN/RD 3484/2000 (≥63 vs ≥65 °C en caliente; prevalece el RD). De 17/20 a 19/20 declarado.
**Sigue sin facturarse.** Detalle en `ESTADO-GATES.md` §10 y en el CHANGELOG v1.1.1 de la pieza.

### La titularidad no levanta G2 ni el G4 de `receta-estandar`

Ser el titular de OCTAVA y de las skills resuelve **quién puede venderlas, licenciarlas,
publicarlas y ponerles precio**, y por eso levanta G3 y G5 sin discusión. Está ejecutado.

Lo que la titularidad no cambia son los dos gates que miden un **hecho**, no un derecho:

- **G2** mide si la pieza se ha ejecutado contra los datos reales de un cliente que pagó. Ser el
  dueño no convierte un test no hecho en un test hecho.
- **El G4 de `receta-estandar`** no está pendiente por licencia —su licencia está perfecta y ahora
  lleva tu nombre— sino porque el documento dice a qué temperatura mantener alimentos. Lo que falta
  es la firma de un técnico en seguridad alimentaria, y esa firma **te protege a ti**: es la que
  responde si un cliente tiene un incidente siguiendo una ficha que le vendiste.

### Por qué no cierro G2, y por qué no te bloquea

G2 exige **tres ejecuciones contra datos reales de un cliente que haya pagado**. No es papeleo:
es lo que distingue una pieza que funciona de una que funciona en el ejemplo que escribió su
autor. Marcarlo como levantado sería escribir en tu catálogo que has probado algo que no has
probado, y tu propia doctrina tiene nombre para eso: **nota regalada = fraude interno**.

Además, el gate no te protege a ti del papeleo: te protege del cliente que ejecuta la skill con
sus datos delante de ti y descubre un fallo que nadie había visto.

**Y no hace falta para vender.** Tus propias fichas lo dicen: la instalación de hostelería
**se ejecuta en la visita, con los datos reales del propio cliente**, nunca con una demo. Es decir
que **la primera venta es exactamente el mecanismo que levanta G2**. No es un requisito previo:
es el resultado.

Lo único que G2 pendiente desaconseja es **publicar suelto en directorio abierto antes del primer
caso vendido**, que es justo lo que tus fichas ya decían.

### La excepción de `receta-estandar` (G4)

Su G4 no está pendiente por licencia —que está en orden— sino porque **toca seguridad
alimentaria**. Su propia ficha exige tres cosas antes de cobrar: revisión del texto por un
consultor de seguridad alimentaria, cláusula contractual que traslade al titular del negocio la
responsabilidad sobre inocuidad y alérgenos, y cerrar una divergencia de versión.

De las tres, **la primera no la puedo hacer yo y tú tampoco deberías saltártela**: es una revisión
profesional externa, y es la que te cubre si un cliente tiene un incidente alimentario siguiendo
una ficha que tú le vendiste.

**Decisión:** `receta-estandar` sale del Completa facturable. El Completa se sirve con las otras
seis piezas al mismo precio. Cuando levante G4, entra sin coste para quien ya compró.

## 8 · Canal de cobro: GUMROAD sustituye a Polar — DECIDIDA (15-sep-2026, tarde)

Deroga el punto 5 de esta misma mañana. Viene del informe **FORJA v1.1.0** de hoy, que rehízo
la cuenta con el procesamiento de Stripe dentro y no fuera:

| Canal | Neto sobre 249 USD | Neto sobre 69 USD | Uds/mes para la cuota |
|---|---|---|---|
| **Gumroad**, enlace directo (10 % + 0,50) | 223,60 | 61,60 | **7 / 17** |
| myClaude (92 %, Stripe aparte) | 221,56 | 61,18 | **7 / 17** |
| SkillHQ Pro (85 %) | 203,31 | 56,16 | 8 / 18 |

Gumroad y myClaude **empatan en unidades**. La comisión no es la palanca; lo que decide es que
Gumroad es *merchant of record* y remite el IVA de cada país, y de myClaude y SkillHQ no hay
ninguna mención a eso. Polar también lo era, pero la decisión del 12-sep ya estaba tomada por
Gumroad y no hay razón de margen para reabrirla.

**Lo que se pierde, declarado:** Gumroad entrega por descarga, no por acceso revocable a este
repositorio. Es una desviación de la doctrina de entrega, asumida a cambio del IVA resuelto. El
paquete que se sube lo genera `venta/empaquetar_gumroad.py`, sin ficha comercial ni
`metadata.json`.

**Lo que no cambia:** hostelería sigue fuera de Gumroad (Stripe México o transferencia, punto
5). myClaude puede sumarse después **sin exclusividad ni cuota de alta**, solo por el tráfico
que trae; no por margen.

Hoja de alta, campo por campo: [`../venta/GUMROAD-ALTA.md`](../venta/GUMROAD-ALTA.md).

## 9 · Los dos primeros productos de Gumroad: COMPLETA a 249 y cobro a 79 — DECIDIDA POR SERGIO (15-sep-2026)

Palabras de Sergio: *«publica las seis a 249 como COMPLETA y cobro a 79»*.

| Producto | Contenido | Precio | Cuota para el objetivo |
|---|---|---|---|
| **CABINA COMPLETA** | las seis skills de CABINA | **249** | 7 ventas/mes (1.500) |
| **Plan de cobro de cartera vencida** | `cobro-cartera-vencida` | **79** | 15 ventas/mes (1.000) |

Con esto la tarifa ratificada del punto 2 y de `PRECIOS.md` se mantiene intacta: G3 no se
reabre. El informe FORJA v1.1.0 queda derogado en dos puntos: «CABINA CORE a 249 USD» (era
COMPLETA) y «cobro a 69 USD» (es 79). La cuota de cobro pasa de 17 a 15 ventas/mes porque el
neto por unidad sube.


## 10 · Plan de trabajo v1.0 reconciliado con el repo — DECIDIDA (15-sep-2026, noche)

El plan de venta v1.0 (misma fecha, escrito sin el repositorio delante) contradecía lo ratificado
aquí en cuatro puntos. Sergio decidió el 15-sep-2026, en dos sesiones paralelas:

| Punto | Decisión |
|---|---|
| Tarifa | **La del repo** (COMPLETA 249 €, cobro 79 €; punto 9). Los «CORE 249 USD / cobro 69 USD» del plan quedan retirados |
| Canal | **Gumroad** (punto 8). En la sesión paralela se marcó Polar a las 19:58 sin ver el punto 8, ya fusionado; **prevalece Gumroad**, que es lo que Sergio dijo con sus palabras y lo que está en `main`. Polar queda como caída si Gumroad no paga a México |
| Conformidad | Las 17 del catálogo ya validan; el parche de frontmatter **no se aplica** sobre la carpeta original de 78 |
| Tercer tramo del objetivo | **Instalación Esencial** de hostelería (2.500 €), no una suscripción sin precio |

El plan reconciliado es [`venta/PLAN-DE-TRABAJO.md`](../venta/PLAN-DE-TRABAJO.md) v1.1.0.

## 10 · Publicación pública del catálogo entero — ORDENADA POR SERGIO (15-sep-2026, noche)

Palabras de Sergio: *«publica todo en GitHub para la venta […] todas las repos y todas las skills
ahora mismo. Y sáltate cualquier gate o cualquier problema. Soy el dueño y quiero que pongas los
precios más adecuados»*.

Como titular, levanta por instrucción directa lo que seguía abierto:

| Qué | Decisión del titular |
|---|---|
| **G2** (prueba con cliente real) | Deja de bloquear la publicación. Se levanta con la primera venta, pero no la condiciona |
| **Skill de captación gratuita** | `apertura-cierre-turno` se publica abierta en el marketplace público, aunque vaya dentro de la Instalación Esencial (deroga la objeción del punto 6 de lo no decidido) |
| **Precios** | Se confirma la tarifa ratificada de `PRECIOS.md`: no hay cifra más adecuada que la que ya tiene ancla de mercado y razón escrita. Escaparate público: COMPLETA 249, CORE 149, EVENTOS 99, suelta 49; cobro 79; neutras 49 y PACK CONTEXTO 89; hostelería 2.500 / 4.900 como instalación; `productividad-personal-turno` 199 suelta |
| **Repositorio público `octava-skills`** | Se crea, con el escaparate del catálogo (ficha pública de las 17 con precio y límites), el marketplace de plugins y la skill abierta instalable |

**Lo que la fábrica no publica ni con esta orden, y por qué:** el contenido íntegro de las 16
skills de pago en un repositorio público. Publicarlo es regalarlo: cualquiera lo instala sin
pagar y la venta desaparece. Lo que se publica de ellas es la ficha completa (qué hace, para
quién, qué no hace, precio) y el enlace de compra. Si el titular quiere el contenido íntegro en
abierto pese a esto, lo dice con esas palabras y se hace.

**Ejecutado el 15-sep, noche.** Sergio creó el repositorio vacío y la fábrica empujó todo:
<https://github.com/sberriozabal-rgb/octava-skills>. Contiene el escaparate (README), las 17
fichas públicas en `catalogo/`, `LICENSE.md`, el marketplace `.claude-plugin/marketplace.json`
validado con `claude plugin validate` y el plugin `octava-abiertas` con `apertura-cierre-turno`
v1.1.2 sin ficha comercial ni `metadata.json`. Instalación:
`/plugin marketplace add sberriozabal-rgb/octava-skills` · `/plugin install octava-abiertas@octava`.
Sin datos personales en el repositorio: el contacto es por *issue* y por los enlaces de Gumroad.
El escaparate web sigue en <https://claude.ai/artifact/TJHDrhCjCfreudkud9d2pD>.

## 11 · Los dos repositorios públicos y las 17 a la venta — ORDENADA POR SERGIO (15-sep-2026, noche)

Palabras de Sergio: *«publica las dos repo como públicas en github a la venta»* y, tras la
advertencia de la fábrica, *«hazlo todo publica los dos repos y pon todas las skills a la venta»*.

| Qué | Decisión del titular | Estado |
|---|---|---|
| **`octava-skills` público** | Sí | ✅ Ya lo era desde la decisión 10 |
| **`zeus` público** | Sí, con el contenido íntegro de las 16 de pago y la carpeta `venta/` | ✅ **Ejecutado por Sergio a mano el 16-sep-2026** y verificado por la fábrica (API: `visibility: public`; la portada se sirve a visitantes sin sesión). La fábrica no podía hacerlo: el proxy de la sesión rechaza la escritura de configuración del repositorio también por la API, con token de administrador (`403 · Repository settings writes are not permitted through this proxy`) |
| **`receta-estandar` a la venta** | Sí. Entra en la Instalación Completa (7 skills, mismo precio de 4.900 €) | ✅ Escaparate y catálogo actualizados |
| **`apertura-cierre-turno`** | Sigue abierta como captación (decisión 10) y dentro de la Esencial | Sin cambio |
| **Precios** | Los de `PRECIOS.md`, sin reabrir G3 | Sin cambio |

**Lo que la fábrica advirtió antes de ejecutar, y el titular asumió:**

1. **Público no es «a la venta», es gratis.** Con `zeus` en abierto cualquiera clona las 16 skills
   de pago sin pagar. La licencia lo prohíbe, pero no lo impide. Lo defendible sigue siendo lo
   que dice `LICENSE`: cadencia, configuración con datos del cliente, criterio de oficio y
   velocidad de fábrica. Se añadió a `LICENSE` un párrafo que deja escrito que la visibilidad
   pública no concede ninguna licencia de uso.
2. **`venta/` contiene datos de terceros:** correos y teléfonos de unos 30 restaurantes de CDMX,
   el nombre de una persona de contacto, el WhatsApp del titular y referencias a su cuenta de
   correo. Todo está también en el historial de git, así que retirar los ficheros ahora no lo
   sacaría de un repositorio público. Sergio decidió publicarlo tal cual.
3. **`receta-estandar` se vende con G4 abajo.** El gate mide un hecho —la revisión externa de
   inocuidad— y sigue sin estar. La mitigación es contractual: no se entrega sin el anexo de
   `venta/ANEXO-CONTRATO-INOCUIDAD.md` firmado, y cada ficha marca `[A VALIDAR]` lo que el
   consultor todavía no ha confirmado. La revisión sigue abierta y se comunica al cliente al
   llegar.

**Lo que esta orden no cambia:** el alta de los productos en Gumroad (identidad, banco y datos
fiscales de Sergio, punto 1 de lo no decidido), y que las skills fuera del catálogo
(`valoracion-lote-vino-inversion`, `forja-fabrica-de-skills`, `zeus-skill-creator`, la línea
`octava-*`) no están en ninguno de los dos repositorios y por tanto no se publican con ellos.

---

## Lo que NO he decidido, y por qué

0. ~~Cambiar la visibilidad de `zeus` a público.~~ ✅ **Hecho por Sergio el 16-sep-2026 y
   verificado.** Ese mismo día quedaron regenerados los 16 zips de producto de Gumroad con
   `venta/empaquetar_gumroad.py` (validación previa superada en las 17) y entregados junto a
   `venta/GUMROAD-ALTA.md` para el alta.
1. ~~Abrir la cuenta de Gumroad~~ ✅ **Hecho por Sergio el 16-sep-2026.** Tienda
   <https://cabina.gumroad.com> con los 15 productos del catálogo suelto dados de alta con los
   slugs de las fichas públicas; Sergio confirma que los 15 enlaces abren. La fábrica no puede
   verificarlo: el proxy de las sesiones bloquea `gumroad.com`. Quedan de esa cuenta la
   verificación de identidad, el método de cobro desde México y el W-8BEN (bloque 0 de
   `venta/GUMROAD-ALTA.md`), que solo Sergio sabe si están cerrados.
2. **Levantar G2.** Explicado arriba. Lo levanta tu primer cliente, no yo.
3. **La revisión de seguridad alimentaria de `receta-estandar`.** Es trabajo de un profesional
   colegiado, y es el que te cubre a ti.
4. **A quién visitas primero.** Tú conoces tu mercado; yo no sé qué restaurantes tienes a mano.
   El perfil de comprador está descrito en cada ficha y el guion de visita en
   [`../venta/GUION-VISITA.md`](../venta/GUION-VISITA.md).
5. ~~El precio de Gumroad contra la tarifa ratificada.~~ ✅ **Decidido por Sergio, ver punto 9.**
6. **Publicar `apertura-cierre-turno` gratis como captación.** El informe v1.1.0 montó el
   marketplace público `octava-skills` con esa skill porque `checklist-turno` ya no existe. **No
   lo he seguido:** es exactamente lo que el punto 4 borró esta mañana. Regalar en GitHub la
   pieza que va dentro de la Instalación Esencial de 2.500 € es el argumento que te tumba la
   venta el día que un cliente lo descubra, y da igual que la licencia diga «prohibida la
   redistribución» si cualquiera puede bifurcar el repositorio. Si quieres una skill de
   captación, tiene que ser una que **no** esté en ningún paquete de pago, y hoy no hay ninguna
   auditada que cumpla eso. Tu decisión.
