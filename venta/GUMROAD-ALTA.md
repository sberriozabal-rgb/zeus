# Hoja de alta en Gumroad — lista para pegar

**Canal decidido el 15-sep-2026** (FORJA v1.1.0, decisión 8 de
[`../catalogo/DECISIONES.md`](../catalogo/DECISIONES.md)). Sustituye a
[`POLAR-CONFIGURACION.md`](POLAR-CONFIGURACION.md), que se conserva como historial.

Dos productos primero, el resto cuando esos dos tengan un comprador. Cada bloque es lo que va
en cada campo del formulario de Gumroad, en el orden en que lo pide. Lo que va entre
`[corchetes]` lo rellenas tú.

> **Comprobado el 15-sep-2026 por búsqueda (el proxy bloquea gumroad.com, no las búsquedas).**
> La comisión es 10 % + 0,50 USD **más** el procesamiento de tarjeta (≈ 2,9 % + 0,30): coste
> efectivo ≈ 12,9 % + 0,80 por venta directa; 30 % plano si la venta entra por Discover. Pagos
> los viernes, retención de 7 días, mínimo 10 USD. México cobra por **transferencia a banco
> local**. El precio se puede mostrar en EUR, pero se procesa en USD. Fuentes y cifras netas en
> `PLAN-DE-TRABAJO.md` §2 y §3. El 404 de `cabina.gumroad.com/l/cabina-core` sigue sin segunda
> comprobación: el subdominio se reserva en el alta.

---

## 0 · La cuenta, antes de crear ningún producto

| Paso | Qué | Por qué |
|---|---|---|
| 1 | Crear la cuenta con el correo de la casa y **verificar identidad el mismo día** | Según el informe, el umbral de pago cae de 100 a 10 USD verificado |
| 2 | Configurar el método de cobro **desde México** | Hueco abierto: qué método ofrece Gumroad a un vendedor mexicano. Se cierra aquí, no antes |
| 3 | Rellenar los datos fiscales que pida (W-8BEN para no residentes en EE. UU.) | Sin esto retiene impuesto en origen |
| 4 | **Apuntar el desglose de la primera venta** (o de una compra de prueba propia a 1 USD) | Es lo que cierra el hueco de si el 10 % + 0,50 incluye o no el procesamiento de tarjeta |
| 5 | Subdominio de la tienda: `cabina` para CABINA, o uno solo para todo el catálogo | El informe daba por hecho `cabina.gumroad.com`; si no está reservado, resérvalo hoy |

**Entrega.** Gumroad entrega por descarga, no por acceso a repositorio. Eso es una desviación
declarada de la doctrina (*acceso revocable, nunca adjunto*) y está asumida en la decisión 8: a
cambio Gumroad actúa como *merchant of record* y remite el IVA por ti. El fichero que subes lo
genera `empaquetar_gumroad.py` (abajo), **sin** la ficha comercial ni el `metadata.json`, que
son de fábrica.

**Moneda.** La tarifa está en euros. Si Gumroad te deja fijar el precio en EUR, ponlo en EUR;
si solo admite USD, la cifra se mantiene (249 y 79) y se anota en la ficha del producto que se
publicó en dólares. No se convierte al cambio: el número es el precio.

---

## 1 · Producto: CABINA COMPLETA · 249

**Decidido por Sergio el 15-sep-2026:** las seis skills a 249 con el nombre CABINA COMPLETA.
Coincide con la tarifa ratificada de `PRECIOS.md`; no se reabre G3. El informe v1.1.0 decía
«CABINA CORE a 249 USD»: queda derogado en ese punto, la cuota de 7 ventas/mes no cambia.

### Campos

| Campo de Gumroad | Valor |
|---|---|
| **Name** | CABINA COMPLETA — 6 skills de cabina para DJ |
| **URL** | `cabina-completa` |
| **Price** | 249 · en EUR si Gumroad lo admite; si solo USD, 249 USD |
| **Type** | Digital product · pago único |
| **Content** | `dist/cabina-completa.zip` → `python3 venta/empaquetar_gumroad.py cabina-completa` |
| **Summary** (una línea) | Te digo qué tracks te van a fallar en el próximo bolo, en qué orden arreglarlos, y qué pasó de verdad en el último. |
| **Tags** | dj, rekordbox, serato, claude, skills, cabina, eventos |
| **Refund policy** | *Ver bloque 3* |
| **Quantity / PWYW** | Sin límite · sin «paga lo que quieras» |

### Description (pegar entera)

> **Te digo qué tracks te van a fallar en el próximo bolo, y en qué orden arreglarlos.**
>
> Seis skills para Claude, escritas por un DJ para el trabajo que se repite antes y después de
> cada bolo. Se instalan en Claude Code o en cualquier cliente que siga el estándar abierto
> Agent Skills, y trabajan sobre tus propios exports: no tocan tu biblioteca.
>
> **Qué llevas**
>
> - **Auditoría de biblioteca** — lee tu `collection.xml` de rekordbox y devuelve un parte
>   priorizado por riesgo real en cabina: rutas rotas y tracks sin beatgrid primero, lo cosmético
>   al final, y el Top 3 para el bolo de la fecha que le des. Solo lectura, siempre.
> - **Parte de bolo** — cruza el historial exportado de la sesión con lo que pasó en la sala y te
>   dice qué se cortó pronto, qué se sostuvo y dónde saltó el tempo. Con la hora exacta, no con
>   lo que recuerdes.
> - **Set por encargo** — te cambian el slot a las siete y a las ocho tienes el set reordenado
>   para esa franja, ese BPM de relevo y esas prohibiciones del cliente, con el porqué de cada
>   transición.
> - **Peticiones a repertorio** — cruza la lista del cliente contra tu biblioteca: qué tienes,
>   qué hay que comprar, qué está en una versión que no sirve, qué te han pedido que no pongas.
>   Con el documento para el cliente ya escrito.
> - **Presupuesto y contrato de evento** — el presupuesto desglosado y las seis cláusulas que se
>   pagan cuando faltan (depósito, cancelación, horas extra, rider, comida, imprevistos).
> - **Demo a sello** — el canal que pide cada sello, el texto breve con el encaje en su catálogo,
>   el clip de 20 segundos y la fecha de envío coordinada con los plazos de Beatport y Spotify.
>
> **Qué NO hace, para que no lo compres por lo que no es**
>
> - No repara la biblioteca. Diagnostica y prioriza; escribir en la base de datos de rekordbox o
>   en los `.crate` de Serato puede destruir playlists y cue points, y por eso no lo hace. Para
>   reparar en lote está Lexicon, y es mejor en eso.
> - No oye. Lee clave, BPM y energía del export; si tu software analizó mal una clave, desde
>   aquí no se detecta.
> - El parte de bolo no sabe si había gente: eso lo aportas tú o no está en el parte.
> - Con Serato, Engine o Traktor funciona tras exportar a XML o CSV.
> - El contrato no es asesoría jurídica: te da las cláusulas y su razón, la revisión legal es
>   tuya.
>
> **Requisitos**
>
> Claude Code (o cliente compatible con Agent Skills) y Python 3 para los scripts, sin librerías
> externas. Export XML de rekordbox para la auditoría y el set; CSV del historial para el parte.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de bolos ni de clientes. Prohibida la
> redistribución, reventa o publicación. Cada skill lleva su `LICENSE.txt`.
>
> Copyright 2026 Sergio Berriozábal Serrano.

---

## 2 · Producto: Plan de cobro de cartera vencida · 79

**Decidido por Sergio el 15-sep-2026: 79.** Es la tarifa ratificada. El informe v1.1.0 decía
69 USD y calculaba 17 ventas/mes sobre esa cifra; a 79 la cuota de 1.000/mes baja a **15
ventas/mes** con el neto de Gumroad (79 − 7,90 − 0,50 = 70,60).

### Campos

| Campo de Gumroad | Valor |
|---|---|
| **Name** | Plan de cobro de cartera vencida — skill para Claude |
| **URL** | `cobro-cartera-vencida` |
| **Price** | 79 · en EUR si Gumroad lo admite; si solo USD, 79 USD |
| **Type** | Digital product · pago único |
| **Content** | `dist/cobro-cartera-vencida.zip` → `python3 venta/empaquetar_gumroad.py cobro-cartera-vencida` |
| **Summary** (una línea) | A quién reclamar primero, qué escribirle exactamente, y en qué fecha subes el tono si no paga. |
| **Tags** | cobros, facturas, cuentas por cobrar, pyme, b2b, claude, skills |
| **Refund policy** | *Ver bloque 3* |
| **Quantity / PWYW** | Sin límite · sin «paga lo que quieras» |

### Description (pegar entera)

> **A quién reclamar primero, qué escribirle exactamente, y en qué fecha subes el tono si no
> paga.**
>
> Le pasas tu listado de facturas vencidas —hoja de cálculo, export del ERP, foto o texto
> pegado, sin limpiarlo antes— y te devuelve un plan de cobro con una acción fechada por
> factura, el mensaje ya redactado para cada cliente y un cuadro de mando de cuatro cifras.
>
> **Qué entrega**
>
> - **La prioridad por cruce, no por antigüedad.** Una factura parada 90 días porque falta una
>   orden de compra no necesita una llamada del responsable: necesita que se reemita el
>   documento. La acción sale del cruce entre cuántos días lleva vencida y por qué no se ha
>   pagado (disputa, error documental, tesorería o silencio).
> - **El texto de cada mensaje**, listo para enviar, en el tono que toca a cada escalón.
> - **El calendario de escalado con fechas**: si en la fecha de revisión no hay pago ni acuerdo
>   escrito, sube un escalón. Es lo que impide el recordatorio infinito.
> - **El cuadro de mando**: DSO, importe en riesgo, cliente crítico y coste del cobro.
> - Anexo para México contra texto legal (interés moratorio, prescripción, CFDI). Para el resto
>   de jurisdicciones aplica el criterio general y los plazos que le indiques; los anexos de
>   España y Colombia no están todavía.
>
> **Qué NO hace**
>
> - **No es asesoría jurídica.** Marca el punto exacto en que el expediente debe pasar a un
>   profesional; a partir de ahí, no sigue.
> - **No sirve para cobrar a consumidores particulares.** El cobro a personas físicas tiene
>   normativa de protección al consumidor con límites de frecuencia y contenido que este
>   protocolo no contempla. Solo B2B.
> - No valora carteras para venta, no lleva concurso de acreedores ni cierre fiscal.
> - Con más de 2.000 líneas describe el criterio para programarlo en tu sistema de cobro; no lo
>   ejecuta línea a línea.
>
> **Requisitos**
>
> Claude Code o cualquier cliente compatible con el estándar abierto Agent Skills. Sin
> dependencias. Cuanto más completo el listado (fecha de emisión, último contacto, ventas del
> periodo), más afinado el plan; con cliente, importe y vencimiento ya funciona.
>
> **Licencia**
>
> Uso en tu propio negocio o en el de tus clientes de consultoría. Prohibida la redistribución
> o reventa. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

---

## 3 · Política de devolución (la misma en los dos)

> Es un producto digital de texto y scripts: se descarga entero en la primera compra. Por eso
> no hay devolución por «no era lo que esperaba»: la sección **Qué NO hace** está arriba para
> que lo sepas antes. Sí devuelvo el importe íntegro si el fichero no se descarga, está
> corrupto o una skill no se activa en Claude Code siguiendo el LEEME, dentro de los 14 días
> siguientes a la compra. Escríbeme respondiendo al correo de Gumroad.

---

## 4 · Las tres reglas de todo texto de producto

Son las mismas de la doctrina y **no se negocian**:

1. **Ninguna cifra sin su fuente.** Por eso la descripción de CABINA no cita el 69 % de acierto
   de clave de rekordbox ni la de cobro las 9,85 horas semanales: en la página de venta irían
   sin su límite pegado. Están en las skills, con URL.
2. **Ninguna promesa de resultado.** Ni «recuperarás tu cartera», ni «te firmará el sello».
3. **No decir que están probadas** hasta que G2 esté levantado. Los casos son de fabricación.

---

## 5 · Lo que queda de la lista de siete días, y de quién es

| Día | Pendiente | Estado a 15-sep |
|---|---|---|
| 1 | Parche de frontmatter en las 14 skills rotas | **En este repositorio no aplica: 17/17 parsean y 17/17 declaran licencia**, incluidas `auditoria-de-biblioteca` y `presupuesto-y-contrato-evento`. Las 14 rotas están en la biblioteca de 78 de la cuenta, no aquí. Si esa biblioteca tiene copia distinta de estas dos, la buena es ésta |
| 1 | Abrir Gumroad y verificar identidad | Sergio · bloque 0 |
| 2 | Repositorio `octava-skills` con la skill gratuita | ✅ **Publicado** (decisión 10): <https://github.com/sberriozabal-rgb/octava-skills>. Sus fichas enlazan a `cabina.gumroad.com/l/<slug>`: usa exactamente esos slugs al dar de alta cada producto |
| 3 | Alta de los dos productos | Sergio · bloques 1 y 2, con `cabina-completa.zip` y `cobro-cartera-vencida.zip` de `empaquetar_gumroad.py`. Precios decididos: 249 y 79 |
| 4 | `myclaude publish` | Sergio · con el paquete del informe; desde aquí `myclaude.sh` no responde. Antes, la consulta sobre IVA de `CONSULTAS-PENDIENTES.md` |
| 5–7 | Las dos conversaciones de prueba | Sergio · es el hueco que importa |
