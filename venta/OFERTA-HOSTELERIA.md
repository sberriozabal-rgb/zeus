# Oferta de hostelería — ficha de producto de las instalaciones

Lo que el dueño de un restaurante lee, oye o recibe cuando se le ofrece la instalación. Es la
ficha que faltaba: la hoja de Gumroad (`GUMROAD-ALTA.md`) cubre el catálogo suelto, y las
instalaciones no se venden por Gumroad. Sigue la plantilla de la casa —frase de anuncio, qué hace,
qué NO hace, requisitos, licencia— y las tres reglas del bloque 4 de la hoja de Gumroad: ninguna
cifra sin fuente, ninguna promesa de resultado, y no decir que están probadas hasta que G2 esté
levantado.

**Tarifa ratificada el 15-sep-2026** (`../catalogo/PRECIOS.md`). Composición de la Completa según
la decisión 11 (`../catalogo/DECISIONES.md`): 7 skills, `receta-estandar` dentro con anexo firmado.

| Producto | Skills | Precio | Cómo se cobra |
|---|---|---|---|
| **Instalación Esencial** | 3 | **2.500 €** | Stripe México (pesos) o transferencia |
| **Instalación Completa** | 7 | **4.900 €** | Stripe México (pesos) o transferencia |
| **Productividad de personal por turno**, suelta | 1 | **199 €** | Gumroad (`productividad-personal-turno`) |

Precio sin impuestos. En México se factura en pesos al tipo de cambio del día de la factura. Ante
negociación se quita alcance, jamás se baja el precio: si la Completa baja a 3.500 € una vez, ya
nunca vale 4.900 €.

---

## 1 · Instalación Esencial · 2.500 €

> **Te digo qué plato de tu carta te está comiendo el margen, qué proveedor te ha subido de
> verdad, y dejo montado el checklist para que el turno lo sostenga.**
>
> Tres herramientas instaladas en tu local, ejecutadas con tus datos delante de ti y con tu
> equipo formado para usarlas. No es un informe que se lee y se guarda: es un sistema que se
> queda funcionando en tu ordenador y que tu encargado puede volver a ejecutar cada mes.
>
> **Qué llevas**
>
> - **Escandallo e ingeniería de menú** — el coste real de cada plato de tu carta con el
>   rendimiento de limpieza y la merma de cocción aplicados, que es lo que hace que el coste del
>   albarán no sea el coste del plato. Cada plato clasificado en la matriz de popularidad y
>   margen (Kasavana y Smith, 1982) para decir qué proteger, qué abaratar, qué reposicionar y
>   qué retirar. La cifra sale en euros o pesos al año, no en porcentajes.
> - **Comparativa de proveedores** — tus albaranes y facturas de los últimos meses,
>   normalizados a la misma unidad: qué producto te ha subido, cuánto, desde cuándo, qué parte
>   de esa subida se corrige sola con la temporada, y qué proveedor te lo tiene hoy más barato.
>   Lo compruebas esa misma tarde llamando al proveedor.
> - **Apertura, cambio y cierre de turno** — los checklists de tu local, no una lista genérica:
>   cada tarea con su responsable por puesto, su momento exacto y su criterio de "hecho", más el
>   parte de incidencias. Es lo que hace que las otras dos se sostengan tres semanas después.
>
> **Qué NO hace, para que no lo compres por lo que no es**
>
> - No es asesoría contable, fiscal ni laboral, y no sustituye a tu gestor. Tu gestor te dice
>   cuánto ganaste el mes pasado; esto te dice qué plato te está comiendo el margen y cuánto
>   cuesta arreglarlo. Son dos trabajos distintos.
> - No cambia de proveedor por ti ni negocia con él. Te da el dato con la unidad igualada; la
>   llamada la haces tú.
> - No funciona con proveedor único obligado por contrato o central de compras: sin dos
>   proveedores del mismo producto no hay comparativa. Tampoco si tiras los albaranes y solo
>   guardas el resumen del banco.
> - No es un plan de higiene certificado (APPCC/HACCP) ni lo sustituye.
> - No promete ningún resultado. Lo que ves en la visita es tu carta y tus facturas pasando por
>   el sistema; lo que hagas con la cifra es tuyo.
>
> **Requisitos**
>
> - Un ordenador del local con Claude Code (o un cliente compatible con el estándar abierto
>   Agent Skills) y Python 3. La instalación lo deja configurado.
> - Export de ventas por producto del último mes (del TPV) y las últimas facturas o albaranes de
>   los proveedores principales. Si no los tienes a mano, se sacan en la visita.
> - Una persona del local —el dueño, el encargado o el jefe de cocina— que ejecute con nosotros
>   la primera vez y firme la formación.
>
> **Qué incluye la instalación**
>
> - Visita de instalación en el local: las tres skills configuradas con tus datos y ejecutadas
>   delante de ti.
> - Formación de la persona que las va a usar, con el ejemplo hecho sobre tu carta y tus facturas.
> - Los tres informes de la primera ejecución, en tu poder aunque no sigas con nosotros.
> - Licencia de uso en tu local, sin límite de ejecuciones.
>
> **Licencia**
>
> Uso en tu propia organización, en los locales que operes, sin límite de ejecuciones. Prohibida
> la redistribución, reventa o publicación. Cada skill lleva su `LICENSE.txt`.
>
> Copyright 2026 Sergio Berriozábal Serrano.

**Ficha comercial de cada pieza:** `../skills/hosteleria/<skill>/ANEXO-A-ficha-comercial.md`.
**Comprador nombrado:** restaurante independiente o grupo pequeño, España o México, plantilla de
8 a 30 personas, carta de 20 a 60 referencias, que compra a dos o más proveedores del mismo
producto y guarda los albaranes. Decide el dueño; en grupo pequeño, el gerente con el jefe de
cocina delante.

---

## 2 · Instalación Completa · 4.900 €

> **El sistema de operación de tu local, montado con tus datos: margen, compras, turno,
> reseñas, plantilla, competencia y recetas.**
>
> Las tres piezas de la Esencial más cuatro que trabajan sobre lo que pasa fuera de la cocina y
> alrededor de ella. Siete herramientas instaladas en tu local, ejecutadas con tus datos delante
> de ti y con tu equipo formado para volver a ejecutarlas sin nosotros.
>
> **Qué llevas**
>
> - **Escandallo e ingeniería de menú**, **comparativa de proveedores** y **apertura, cambio y
>   cierre de turno** — las tres de la Esencial, descritas arriba.
> - **Respuesta a reseñas** — tu export de reseñas de Google o TripAdvisor convertido en dos
>   cosas: las respuestas listas para publicar, una por reseña y con el tono de cada categoría, y
>   el patrón operativo: si el mismo problema aparece tres o más veces en sesenta días, eso ya no
>   es un cliente difícil, es algo que puedes arreglar el lunes.
> - **Productividad de personal por turno** — ventas por hora trabajada y coste de personal
>   sobre venta sin IVA, franja a franja y día a día: en qué franjas pagas plantilla sin venta y
>   en cuáles pierdes venta por falta de mano, cuánto de ese exceso es de horas fijas que no se
>   pueden tocar, y una propuesta de escalonar entradas y salidas con las horas que recupera.
> - **Radar semanal de competencia** — cada semana, cómo vas contra seis competidores de tu
>   zona en nota, volumen, recencia y tasa de respuesta, qué hacen ellos que tú no, y tres cosas
>   para esta semana con responsable y día. Con la cita y la fecha de cada dato.
> - **Receta estándar** — la forma de cocinar cada plato que hoy vive en la cabeza de un
>   cocinero, convertida en una ficha que cualquier cocinero del turno puede ejecutar: gramaje,
>   pasos numerados con señal de terminado, puntos críticos con el binomio tiempo-temperatura de
>   la norma de tu país (RD 3484/2000 y AESAN en España, NOM-251-SSA1-2009 en México) y criterio
>   de emplatado verificable. Se entrega con el anexo de seguridad alimentaria firmado.
>
> **Qué NO hace, para que no lo compres por lo que no es**
>
> - Todo lo que no hace la Esencial (arriba).
> - No publica ninguna respuesta a reseñas: te deja el texto, lo publicas tú. No gestiona la
>   retirada de reseñas falsas ante la plataforma ni es asesoría legal ante difamación.
> - No calcula cuadrantes legales ni sustituye a la asesoría laboral: no interpreta convenio,
>   jornada máxima, descansos ni registro horario. No propone despidos ni evalúa a personas;
>   trabaja con franjas y puestos. Toda modificación de turno se valida con asesoría laboral o
>   graduado social (España) o abogado laboral (México).
> - El radar usa solo fuentes públicas, no nombra a ningún reseñador y nunca recomienda
>   solicitar, comprar, incentivar ni suprimir reseñas. No es *due diligence*.
> - **Receta estándar no es un plan de higiene ni lo certifica.** Documenta la receta con las
>   temperaturas de la norma; validar cada binomio en tu cocina, con tu equipo, y declarar los
>   alérgenos es obligación tuya como operador. La revisión externa de un técnico en seguridad
>   alimentaria sigue abierta: lo que ese técnico todavía no ha confirmado va marcado en la ficha
>   como `[A VALIDAR]`, no escondido, y se te comunica en cuanto llegue.
> - No promete ningún resultado. Si mencionamos el efecto de las reseñas en los ingresos, va con
>   sus tres límites: es Yelp, es Estados Unidos, es ingresos y no margen, y solo se midió en
>   independientes (Michael Luca, HBS Working Paper 12-016).
>
> **Requisitos**
>
> - Los de la Esencial, más: export de reseñas de Google o TripAdvisor; ventas por franja
>   horaria sin IVA y el parte de horas del mismo periodo; el nombre de seis competidores de tu
>   zona (si no los tienes, los localizamos); y, para las recetas, el jefe de cocina fuera de
>   servicio para la primera ficha.
> - Ficha activa en Google con volumen suficiente para que un patrón signifique algo. Si eres
>   una cadena o un grupo con marca consolidada, el argumento de las reseñas no te aplica y te lo
>   decimos antes de vender.
>
> **Qué incluye la instalación**
>
> - Todo lo de la Esencial, con las siete skills.
> - Anexo de seguridad alimentaria al contrato (`ANEXO-CONTRATO-INOCUIDAD.md`), firmado antes de
>   entregar `receta-estandar`.
> - El radar de competencia se deja configurado con tu panel de seis competidores; la serie
>   semanal la ejecuta tu equipo. No es una suscripción.
>
> **Licencia**
>
> Uso en tu propia organización, en los locales que operes, sin límite de ejecuciones. Prohibida
> la redistribución, reventa o publicación. Cada skill lleva su `LICENSE.txt`.
>
> Copyright 2026 Sergio Berriozábal Serrano.

---

## 3 · Productividad de personal por turno, suelta · 199 €

Es la única pieza de hostelería con precio suelto, y se vende por Gumroad: ficha completa en
`GUMROAD-ALTA.md`, bloque 6 (`productividad-personal-turno`). El comprador se instala la skill
él mismo; no hay visita. Si un cliente de instalación la pide después de la Esencial, entra como
ampliación al mismo precio, y se le instala en la siguiente visita.

---

## 4 · Cómo se vende, en orden

1. **El Diagnóstico Exprés** abre la puerta: 90 minutos en el local y una página con tres
   hallazgos al día siguiente, sin coste. Landing en `landing/octava-diagnostico-expres.html`;
   correos en `MENSAJES.md`; pipeline real en `PIPELINE.md`.
2. **La visita de venta** de 45 minutos ejecuta el escandallo y la comparativa con los datos del
   dueño. Guion en `GUION-VISITA.md`. La oferta se enseña una vez, con las dos opciones, y luego
   silencio.
3. **La instalación** se factura por Stripe México en pesos o por transferencia, nunca por
   Gumroad (`../catalogo/PRECIOS.md`, canal de cobro). Con la Completa se firma antes el anexo de
   inocuidad, que todavía debe revisar un abogado.
4. **El primer cliente levanta G2**: se anota qué se ejecutó con datos reales y qué falló. Tres
   de esos y la línea entera sale de "casos de fabricación".

## 5 · Lo que no se dice en ningún material de hostelería

- Que las skills están probadas. G2 está abajo; se dice *"lo estás viendo ejecutarse con tus
  datos ahora mismo"*, que es cierto y es más fuerte.
- Ninguna cifra de mercado sin su autor y su límite pegados: la rotación del 63,8 % es del
  informe de Synergie España 2026, no "datos oficiales"; los 2.800–5.000 € por sustituir a una
  persona son de un análisis de Linkers; el +5–9 % de ingresos por estrella es de Michael Luca, HBS Working Paper 12-016 (Yelp,
  EE. UU., independientes, ingresos y no margen).
- Que `receta-estandar` sustituye el APPCC, o que las fichas están revisadas por un técnico:
  no lo están todavía.
- Un precio distinto de los de `../catalogo/PRECIOS.md`.
