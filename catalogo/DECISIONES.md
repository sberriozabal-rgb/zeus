# Decisiones tomadas — 15-sep-2026

Sergio delegó las decisiones pendientes. Quedan tomadas aquí, con su razón. Lo que **no** he
decidido está al final, y no es por prudencia: es porque decidirlo yo te haría daño.

---

## 1 · Tarifa de hostelería — RATIFICADA

| Producto | Contenido | Precio |
|---|---|---|
| **Instalación Esencial** | 3 skills | **2.500 €** |
| **Instalación Completa** | 6 skills | **4.900 €** |
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

`receta-estandar` **queda fuera del Completa facturable** hasta que levante G4. Ver punto 6.

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

---

## Lo que NO he decidido, y por qué

1. **Abrir la cuenta de Gumroad** (antes Polar, ver punto 8). Requiere tu identidad, tu cuenta
   bancaria y tus datos fiscales. Te dejo la hoja de alta de cada producto lista para pegar.
   Verifica identidad el mismo día.
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
