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

## 4 · `checklist-turno`: RETIRADA — DECIDIDA

Se retira `checklist-turno` y se conserva `apertura-cierre-turno`.

Por qué esa y no la otra: `apertura-cierre-turno` es la versión **v1.1.1 auditada en 17/20**, con
ficha comercial, CHANGELOG, casos y licencia de venta. `checklist-turno` es la misma descripción
palabra por palabra con licencia de **uso libre, incluido el comercial**, es decir regalada, y sin
ninguno de los ficheros del peldaño.

Mantener las dos significa vender una pieza dentro de una instalación de 2.500 € mientras su
gemela circula gratis. No es un problema de orden: es el argumento que te tumba la venta el día
que un cliente lo descubra.

### Cómo borrarla, sin equivocarse de skill

⚠️ **Esta acción solo puede hacerla Sergio.** `checklist-turno` no vive en este repositorio ni en
el contenedor de trabajo: el directorio de skills de la sesión es **un espejo que se resincroniza
desde la cuenta de Claude al arrancar**. Borrar la copia local no elimina nada — vuelve en la
sesión siguiente, con la skill intacta en la cuenta y igual de distribuible.

El riesgo de borrar la equivocada es real, porque **las dos tienen la misma descripción palabra
por palabra**. Se distinguen por el origen y por el identificador:

| | `checklist-turno` — **se borra** | `apertura-cierre-turno` — **se conserva** |
|---|---|---|
| `skillId` | `skill_01RfEvhHA5Ex5x9ufLoF8955` | `skill_01WqWzCVPVa5ioSQ2376NgyU` |
| Origen | **custom** — subida directamente a la cuenta | **plugin** — `plugin_013767vgp3Hip4YHgfZhddim` |
| Creada | 2026-08-11 | 2026-09-05 |
| Licencia | *"uso libre, incluido el comercial"* ❌ | *"uso comercial sin derecho de redistribución"* ✅ |
| Auditoría | sin ficha ni nota | 17/20, ficha, CHANGELOG, casos |

**La señal fiable en la interfaz es el origen:** `apertura-cierre-turno` viene de un plugin y
debería mostrar esa marca; `checklist-turno` es una skill personalizada, sin plugin detrás. Se
borra la personalizada, desde la gestión de skills de la cuenta en claude.ai.

**Hasta que eso ocurra, esta decisión está documentada pero no ejecutada**, y la pieza sigue
circulando con licencia de uso libre mientras su gemela se vende dentro de una instalación de
2.500 €.

## 5 · Canal de cobro: POLAR — DECIDIDA

Plan gratuito, conectado a este repositorio privado. Comisión 5 % + 0,50 $, sin cuota fija, así
que no arriesga nada hasta que haya volumen. Es *merchant of record* —gestiona el IVA por ti—,
acepta México como país del vendedor, y **concede y revoca el acceso al repositorio solo** al
suscribir y al cancelar, que es exactamente la forma de entrega que exige la doctrina.

Stripe México queda para instalaciones en pesos, donde el ticket alto justifica su comisión menor
pese a no ser *merchant of record*.

Configuración exacta de productos en [`../venta/POLAR-CONFIGURACION.md`](../venta/POLAR-CONFIGURACION.md).

## 6 · Gates: cerrados G3, G4 y G5. G2 NO. — DECIDIDA

| Gate | Estado | Por qué |
|---|---|---|
| **G1** producto ≥16/20 | ✅ **17/17** | Medido con el validador, entre 17/20 y 20/20 |
| **G3** precio | ✅ **17/17** | Ratificado en los puntos 1 y 2 |
| **G4** legal | ✅ **16/17** | Licencia verificada en las 17. La excepción es `receta-estandar` |
| **G5** público | ✅ **17/17** | Criterio del gate: *"sin cifra inventada"*. Verificado: toda cifra de las 17 fichas lleva fuente con URL o va marcada `[A VALIDAR]` / `[SIN VERIFICAR]` / `[CONVENCIÓN]` |
| **G2** prueba | ❌ **0/17** | **No lo cierro. Ver abajo.** |

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

---

## Lo que NO he decidido, y por qué

1. **Abrir la cuenta de Polar.** Requiere tu identidad, tu cuenta bancaria y tus datos fiscales.
   Te dejo la configuración exacta de cada producto lista para copiar.
2. **Levantar G2.** Explicado arriba. Lo levanta tu primer cliente, no yo.
3. **La revisión de seguridad alimentaria de `receta-estandar`.** Es trabajo de un profesional
   colegiado, y es el que te cubre a ti.
4. **A quién visitas primero.** Tú conoces tu mercado; yo no sé qué restaurantes tienes a mano.
   El perfil de comprador está descrito en cada ficha y el guion de visita en
   [`../venta/GUION-VISITA.md`](../venta/GUION-VISITA.md).
