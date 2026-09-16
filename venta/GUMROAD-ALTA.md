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
| **Cover / Thumbnail** | `venta/portadas/cabina-completa-portada.png` (1280×720) · `venta/portadas/cabina-completa-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
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
| **Cover / Thumbnail** | `venta/portadas/cobro-cartera-vencida-portada.png` (1280×720) · `venta/portadas/cobro-cartera-vencida-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
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
| 1 | Abrir Gumroad y verificar identidad | ✅ **Tienda abierta el 16-sep-2026** en <https://cabina.gumroad.com>. La verificación de identidad, el cobro desde México y el W-8BEN los confirma Sergio; desde la fábrica no se ve |
| 2 | Repositorio `octava-skills` con la skill gratuita | ✅ **Publicado** (decisión 10): <https://github.com/sberriozabal-rgb/octava-skills>. Sus fichas enlazan a `cabina.gumroad.com/l/<slug>`: usa exactamente esos slugs al dar de alta cada producto |
| 3 | Alta de los dos productos | ✅ **Los 15 del catálogo suelto dados de alta el 16-sep-2026** con los zips de `empaquetar_gumroad.py` y los slugs de las fichas públicas. Sergio confirma que los 15 enlaces abren |
| 4 | `myclaude publish` | Sergio · con el paquete del informe; desde aquí `myclaude.sh` no responde. Antes, la consulta sobre IVA de `CONSULTAS-PENDIENTES.md` |
| 5–7 | Las dos conversaciones de prueba | Sergio · es el hueco que importa |

---

## 6 · Alta del resto del catálogo

Los dos productos de arriba van primero. Estos trece se dan de alta después, con el mismo
formulario, la misma política de devolución (bloque 3) y las mismas tres reglas (bloque 4).
Los `slug` son **exactamente** los que enlazan las fichas públicas de
<https://github.com/sberriozabal-rgb/octava-skills>: si cambias uno, cambia también la ficha.
Cada zip lo genera `empaquetar_gumroad.py` con el nombre del `slug`.

Generado el 15-sep-2026 desde los `SKILL.md` y las fichas comerciales. Cada descripción sigue la
plantilla de la casa: frase de anuncio, qué hace, qué NO hace, requisitos, licencia.

### CABINA CORE · 149

| Campo | Valor |
|---|---|
| **Name** | CABINA CORE — 3 skills de cabina para DJ |
| **URL** | `cabina-core` |
| **Price** | 149 |
| **Content** | `dist/cabina-core.zip` → `python3 venta/empaquetar_gumroad.py cabina-core` |
| **Cover / Thumbnail** | `venta/portadas/cabina-core-portada.png` (1280×720) · `venta/portadas/cabina-core-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Las tres que usa cualquier DJ con biblioteca y bolos recurrentes: qué va a fallar, qué pasó, y el set para el slot que te den. |
| **Tags** | dj, rekordbox, serato, biblioteca, set, claude, skills, cabina |

**Description (pegar entera)**

> **Las tres que usa cualquier DJ con biblioteca y bolos recurrentes: qué va a fallar, qué pasó, y el set para el slot que te den.**
>
> Tres skills para Claude que trabajan sobre tus exports de rekordbox o Serato, sin tocar tu biblioteca: la auditoría que prioriza por riesgo de cabina, el parte de bolo con la hora exacta y el set reordenado para el slot que te toque.
>
> **Qué llevas**
>
> - **Auditoría de biblioteca** — Te digo qué tracks te van a fallar en el próximo bolo, y en qué orden arreglarlos.
> - **Parte de bolo** — Qué se cortó pronto, qué se sostuvo y dónde saltó el tempo. Con la hora exacta, no con lo que recuerdes.
> - **Set por encargo** — Te cambian el slot a las siete de la tarde y a las ocho tienes el set reordenado, con el por qué de cada transición.
>
> **Qué NO hace**
>
> - **Diagnostica, no repara.** Es decisión deliberada: reparar exige escribir en la base de datos propietaria (rekordbox `master.db` es SQLite cifrada con SQLCipher4; los `.crate` de Serato son binarios documentados solo por ingeniería inversa comunitaria) y hacerlo mal rompe playlists, cue points y beatgrids.
> - No detecta clave ni BPM que falten: eso exige decodificar el audio. Lo hace el análisis del propio software o Mixed In Key.
> - No sabe si un MP3 está corrupto. Ve metadatos, no decodifica.
> - No transporta My Tags ni playlists inteligentes: el XML de rekordbox no los incluye, está documentado por AlphaTheta (<https://rekordbox.com/>), y si el DJ organiza así le falta información en el parte.
>
> **Requisitos**
>
> - **Obligatorio:** `collection.xml` de rekordbox, exportado con `File > Export Collection in xml format`.
> - **Recomendado:** fecha y tipo del próximo bolo. Cambia por completo la priorización: sin ella el parte ordena por riesgo genérico, con ella ordena por lo que suena antes.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### CABINA EVENTOS · 99

| Campo | Valor |
|---|---|
| **Name** | CABINA EVENTOS — 2 skills para el DJ de eventos |
| **URL** | `cabina-eventos` |
| **Price** | 99 |
| **Content** | `dist/cabina-eventos.zip` → `python3 venta/empaquetar_gumroad.py cabina-eventos` |
| **Cover / Thumbnail** | `venta/portadas/cabina-eventos-portada.png` (1280×720) · `venta/portadas/cabina-eventos-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Las dos piezas del bolo de evento: qué pides al repertorio y qué firmas antes de tocar. |
| **Tags** | dj, bodas, eventos, contrato, presupuesto, claude, skills, cabina |

**Description (pegar entera)**

> **Las dos piezas del bolo de evento: qué pides al repertorio y qué firmas antes de tocar.**
>
> Dos skills para Claude para el DJ de bodas y eventos: la lista del cliente cruzada contra tu biblioteca con el documento ya escrito, y el presupuesto desglosado con las seis cláusulas que se pagan cuando faltan.
>
> **Qué llevas**
>
> - **Peticiones a repertorio** — Qué tengo, qué hay que comprar, qué está en una versión que no sirve y qué me han pedido que no ponga. Con el documento para el cliente ya escrito.
> - **Presupuesto y contrato de evento** — Las seis cláusulas que se pagan cuando faltan, y el presupuesto desglosado para que negociar no sea bajar el margen.
>
> **Qué NO hace**
>
> - **No es asesoramiento jurídico.** Produce borradores de práctica sectorial, y la validez de cada cláusula depende de la jurisdicción. El uso recurrente exige revisión de abogado.
> - No es asesoramiento fiscal. Los impuestos se indican de forma explícita en el presupuesto, pero el tipo aplicable lo confirma el asesor del DJ.
> - Los baremos son **contexto de mercado, no tarifa recomendada**. Sirven para saber si estás fuera de precio; el precio lo fija el DJ con su coste y su agenda.
> - **No se aplica el baremo de un país a otro** sin declararlo como referencia importada. El dato de The Knot es de EE. UU. y no vale para España sin ese aviso.
>
> **Requisitos**
>
> - **Obligatorio · Lista del cliente**, pegada tal cual. Vale WhatsApp con marcas de hora, email, lista numerada, prosa continua o transcripción de audio. **No se pide que la limpien: limpiarla es el trabajo.**
> - **Obligatorio · Export de biblioteca**: `collection.xml` de rekordbox, o CSV con al menos `artist` y `title` (Lexicon, Serato, Engine DJ y VirtualDJ exportan CSV).
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Auditoría de biblioteca · 49

| Campo | Valor |
|---|---|
| **Name** | Auditoría de biblioteca — skill para Claude |
| **URL** | `auditoria-de-biblioteca` |
| **Price** | 49 |
| **Content** | `dist/auditoria-de-biblioteca.zip` → `python3 venta/empaquetar_gumroad.py auditoria-de-biblioteca` |
| **Cover / Thumbnail** | `venta/portadas/auditoria-de-biblioteca-portada.png` (1280×720) · `venta/portadas/auditoria-de-biblioteca-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Te digo qué tracks te van a fallar en el próximo bolo, y en qué orden arreglarlos. |
| **Tags** | dj, rekordbox, biblioteca, beatgrid, cue points, claude, skills |

**Description (pegar entera)**

> **Te digo qué tracks te van a fallar en el próximo bolo, y en qué orden arreglarlos.**
>
> Convierte **un `collection.xml` exportado de rekordbox** en **un parte de estado con los hallazgos agrupados por categoría, un índice de salud de 0 a 100 y un plan de reparación ordenado por riesgo real en cabina**, para **un DJ de club, móvil o residente que prepara un bolo o migra de equipo**, en **menos de 10 minutos de atención**.
>
> **Qué NO hace**
>
> - **Diagnostica, no repara.** Es decisión deliberada: reparar exige escribir en la base de datos propietaria (rekordbox `master.db` es SQLite cifrada con SQLCipher4; los `.crate` de Serato son binarios documentados solo por ingeniería inversa comunitaria) y hacerlo mal rompe playlists, cue points y beatgrids.
> - No detecta clave ni BPM que falten: eso exige decodificar el audio. Lo hace el análisis del propio software o Mixed In Key.
> - No sabe si un MP3 está corrupto. Ve metadatos, no decodifica.
> - No transporta My Tags ni playlists inteligentes: el XML de rekordbox no los incluye, está documentado por AlphaTheta (<https://rekordbox.com/>), y si el DJ organiza así le falta información en el parte.
>
> **Requisitos**
>
> - **Obligatorio:** `collection.xml` de rekordbox, exportado con `File > Export Collection in xml format`.
> - **Recomendado:** fecha y tipo del próximo bolo. Cambia por completo la priorización: sin ella el parte ordena por riesgo genérico, con ella ordena por lo que suena antes.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Parte de bolo · 49

| Campo | Valor |
|---|---|
| **Name** | Parte de bolo — skill para Claude |
| **URL** | `postmortem-de-bolo` |
| **Price** | 49 |
| **Content** | `dist/postmortem-de-bolo.zip` → `python3 venta/empaquetar_gumroad.py postmortem-de-bolo` |
| **Cover / Thumbnail** | `venta/portadas/postmortem-de-bolo-portada.png` (1280×720) · `venta/portadas/postmortem-de-bolo-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Qué se cortó pronto, qué se sostuvo y dónde saltó el tempo. Con la hora exacta, no con lo que recuerdes. |
| **Tags** | dj, rekordbox, serato, historial, bolo, claude, skills |

**Description (pegar entera)**

> **Qué se cortó pronto, qué se sostuvo y dónde saltó el tempo. Con la hora exacta, no con lo que recuerdes.**
>
> Convierte **un export de historial de sesión (rekordbox o Serato) más el relato del DJ sobre la sala** en **un parte de aprendizaje con los hechos verificables separados de las hipótesis, y de una a tres decisiones concretas para el próximo bolo**, para **un DJ residente, móvil o de club que repite tipo de evento o sala**, en **menos de 20 minutos de atención**.
>
> **Qué NO hace**
>
> - **El fichero no sabe si había gente.** No hay forma de saber cuánta gente había ni cómo respondió: eso lo aporta el DJ o no existe en el parte.
> - No evalúa técnica de mezcla ni calidad de la selección musical: eso exigiría oír la grabación, y esta skill no oye.
> - Sin historial exportado no hay análisis. Un set grabado en audio no sirve de entrada.
> - Sin horas en el export, el parte pierde tiempo en el aire, curva de tempo y localización de momentos, que es aproximadamente la mitad de su valor.
>
> **Requisitos**
>
> - **Obligatorio:** historial exportado en CSV o TSV, con al menos título y hora. En rekordbox está en la pestaña Historial, botón derecho sobre la sesión, exportar. En Serato, en History, botón Export (csv o txt). Cualquier CSV con `title,artist,start time` vale.
> - **Muy recomendable:** el relato de la sala, que se obtiene con las cinco preguntas de `references/preguntas-de-sala.md`: a qué hora se llenó y se vació, si hubo algún momento de pérdida, cuál fue el mejor momento, qué sorprendió, y en qué condiciones se tocó.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Set por encargo · 49

| Campo | Valor |
|---|---|
| **Name** | Set por encargo — skill para Claude |
| **URL** | `set-por-encargo` |
| **Price** | 49 |
| **Content** | `dist/set-por-encargo.zip` → `python3 venta/empaquetar_gumroad.py set-por-encargo` |
| **Cover / Thumbnail** | `venta/portadas/set-por-encargo-portada.png` (1280×720) · `venta/portadas/set-por-encargo-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Te cambian el slot a las siete de la tarde y a las ocho tienes el set reordenado, con el por qué de cada transición. |
| **Tags** | dj, set, tracklist, rekordbox, armonía, claude, skills |

**Description (pegar entera)**

> **Te cambian el slot a las siete de la tarde y a las ocho tienes el set reordenado, con el por qué de cada transición.**
>
> Convierte **un pool de tracks exportado más el brief del slot** en **un set ordenado con nota de transición para cada par y una lista de huecos declarados**, para **un DJ de club, residente, móvil o de eventos que prepara un bolo concreto**, en **menos de 15 minutos de atención**.
>
> **Qué NO hace**
>
> - **No oye.** Lee clave, BPM y energía del export; no los detecta. Si el análisis de origen trae la clave mal, el set saldrá mal y no hay forma de detectarlo desde aquí.
> - No corrige claves mal detectadas: eso exige audio y es trabajo de Mixed In Key.
> - No decide qué track suena mejor. Calcula compatibilidad de datos, que no es lo mismo que compatibilidad musical.
> - No mezcla ni genera transiciones: prepara el orden, no ejecuta nada en cabina.
>
> **Requisitos**
>
> - **Obligatorio · Pool**: `collection.xml` de rekordbox, o CSV con columnas `artista,titulo,bpm,key` y opcionalmente `energia,genero,duracion_s`. **Hay que filtrarlo antes**: el pool es la música candidata a ese bolo, no la biblioteca entera.
> - **Obligatorio · Brief del slot**: al menos duración y franja. Idealmente también BPM de entrada y de salida, público, prohibiciones del cliente y tracks obligatorios.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Peticiones a repertorio · 49

| Campo | Valor |
|---|---|
| **Name** | Peticiones a repertorio — skill para Claude |
| **URL** | `peticiones-a-repertorio` |
| **Price** | 49 |
| **Content** | `dist/peticiones-a-repertorio.zip` → `python3 venta/empaquetar_gumroad.py peticiones-a-repertorio` |
| **Cover / Thumbnail** | `venta/portadas/peticiones-a-repertorio-portada.png` (1280×720) · `venta/portadas/peticiones-a-repertorio-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Qué tengo, qué hay que comprar, qué está en una versión que no sirve y qué me han pedido que no ponga. Con el documento para el cliente ya escrito. |
| **Tags** | dj, bodas, eventos, repertorio, peticiones, claude, skills |

**Description (pegar entera)**

> **Qué tengo, qué hay que comprar, qué está en una versión que no sirve y qué me han pedido que no ponga. Con el documento para el cliente ya escrito.**
>
> Convierte **una lista de peticiones en lenguaje natural más un export de la biblioteca del DJ** en **un informe de cuatro cubos (TENGO / NO TENGO / DUDOSO / PROHIBIDO) con lista de compra priorizada y documento de confirmación redactado para el cliente**, para **un DJ móvil que prepara un evento contratado**, en **menos de 10 minutos de trabajo asistido**.
>
> **Qué NO hace**
>
> - **No oye.** No elige qué versión suena mejor: propone por contexto de evento y la decisión la firma una persona.
> - No consulta tiendas digitales ni verifica disponibilidad comercial: genera la lista de compra, no compra ni comprueba que el track esté a la venta.
> - No sirve para peticiones que llegan **durante** el evento. Esto es preparación, no tiempo real.
> - Sin biblioteca exportable solo entrega parseo, prohibidos y agrupación, y lo declara. Es aproximadamente medio informe.
>
> **Requisitos**
>
> - **Obligatorio · Lista del cliente**, pegada tal cual. Vale WhatsApp con marcas de hora, email, lista numerada, prosa continua o transcripción de audio. **No se pide que la limpien: limpiarla es el trabajo.**
> - **Obligatorio · Export de biblioteca**: `collection.xml` de rekordbox, o CSV con al menos `artist` y `title` (Lexicon, Serato, Engine DJ y VirtualDJ exportan CSV).
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Presupuesto y contrato de evento · 49

| Campo | Valor |
|---|---|
| **Name** | Presupuesto y contrato de evento — skill para Claude |
| **URL** | `presupuesto-y-contrato-evento` |
| **Price** | 49 |
| **Content** | `dist/presupuesto-y-contrato-evento.zip` → `python3 venta/empaquetar_gumroad.py presupuesto-y-contrato-evento` |
| **Cover / Thumbnail** | `venta/portadas/presupuesto-y-contrato-evento-portada.png` (1280×720) · `venta/portadas/presupuesto-y-contrato-evento-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Las seis cláusulas que se pagan cuando faltan, y el presupuesto desglosado para que negociar no sea bajar el margen. |
| **Tags** | dj, bodas, eventos, contrato, presupuesto, rider, claude, skills |

**Description (pegar entera)**

> **Las seis cláusulas que se pagan cuando faltan, y el presupuesto desglosado para que negociar no sea bajar el margen.**
>
> Convierte **una consulta de cliente de evento (fecha, lugar, tipo, horario, extras)** en **presupuesto desglosado por conceptos, contrato con las cláusulas marcadas por nivel de riesgo y rider técnico del espacio concreto**, para **un DJ móvil o de eventos que responde a un lead sin manager ni agencia**, en **menos de 30 minutos de atención**.
>
> **Qué NO hace**
>
> - **No es asesoramiento jurídico.** Produce borradores de práctica sectorial, y la validez de cada cláusula depende de la jurisdicción. El uso recurrente exige revisión de abogado.
> - No es asesoramiento fiscal. Los impuestos se indican de forma explícita en el presupuesto, pero el tipo aplicable lo confirma el asesor del DJ.
> - Los baremos son **contexto de mercado, no tarifa recomendada**. Sirven para saber si estás fuera de precio; el precio lo fija el DJ con su coste y su agenda.
> - **No se aplica el baremo de un país a otro** sin declararlo como referencia importada. El dato de The Knot es de EE. UU. y no vale para España sin ese aviso.
>
> **Requisitos**
>
> - **Mínimo imprescindible:** fecha, tipo de evento, ciudad o lugar, y duración. Con eso ya se produce.
> - **Recomendado:** número de invitados (determina el equipo y el precio), espacio y si es interior o exterior (exterior obliga a plan B de lluvia y más potencia), hora de inicio y fin (define horas extra y recargo nocturno).
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Demo a sello · 49

| Campo | Valor |
|---|---|
| **Name** | Demo a sello — skill para Claude |
| **URL** | `demo-a-sello` |
| **Price** | 49 |
| **Content** | `dist/demo-a-sello.zip` → `python3 venta/empaquetar_gumroad.py demo-a-sello` |
| **Cover / Thumbnail** | `venta/portadas/demo-a-sello-portada.png` (1280×720) · `venta/portadas/demo-a-sello-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | El canal que pide cada sello, la frase que lo distingue de los otros cien envíos, y la fecha correcta para que Beatport y Spotify lleguen a tiempo. |
| **Tags** | dj, productor, demo, sello, beatport, spotify, claude, skills |

**Description (pegar entera)**

> **El canal que pide cada sello, la frase que lo distingue de los otros cien envíos, y la fecha correcta para que Beatport y Spotify lleguen a tiempo.**
>
> Convierte **un track terminado más los datos del artista** en **una lista priorizada de sellos con su canal exacto, un texto de envío por sello, el clip de 20 segundos seleccionado y un calendario de envío coordinado con los plazos de tienda**, para **un productor o DJ que manda demos sin manager**, en **menos de 45 minutos de atención**.
>
> **Qué NO hace**
>
> - **No compra una firma.** Ordena el envío y elimina los descartes automáticos, que son de forma. El criterio artístico del sello no se puede gestionar desde aquí.
> - No garantiza respuesta, escucha ni publicación. **El silencio es la respuesta por defecto** y así se declara antes de enviar nada.
> - No produce ni masteriza. Si el track no está terminado, la skill se detiene en el paso 1.
> - La lista de canales es **una foto de agosto de 2026**: los sellos cambian de política y el canal se verifica en su web antes de cada envío.
>
> **Requisitos**
>
> - **Obligatorio:** track terminado y **masterizado**. Los sellos solo aceptan trabajo terminado; si no lo está y aun así se envía, se declara.
> - **Obligatorio:** género, BPM y clave.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### PACK CONTEXTO · 89

| Campo | Valor |
|---|---|
| **Name** | PACK CONTEXTO — 2 skills para Claude |
| **URL** | `pack-contexto` |
| **Price** | 89 |
| **Content** | `dist/pack-contexto.zip` → `python3 venta/empaquetar_gumroad.py pack-contexto` |
| **Cover / Thumbnail** | `venta/portadas/pack-contexto-portada.png` (1280×720) · `venta/portadas/pack-contexto-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Saca tu proyecto de IA a un paquete cifrado y conviértelo en una biblioteca ordenada con la lista de lo que aún no has decidido. |
| **Tags** | claude, proyecto, respaldo, backup, contexto, documentación, skills |

**Description (pegar entera)**

> **Saca tu proyecto de IA a un paquete cifrado y conviértelo en una biblioteca ordenada con la lista de lo que aún no has decidido.**
>
> Las dos mitades de la misma cadena: el respaldo asegura el material antes de que desaparezca; el compilador lo hace comprensible, ordenado por temas y con la versión vigente marcada.
>
> **Qué llevas**
>
> - **Respaldo cifrado de proyecto de IA** — Te llevas tu proyecto entero cifrado, con el guion para rehacerlo y la lista de lo que no cabía. Probado en frío antes de que borres nada.
> - **Compilador de contexto de proyecto** — Todo lo que hay en tu carpeta, ordenado por temas, con la versión vigente marcada y la lista de lo que aún no has decidido.
>
> **Qué NO hace**
>
> - **No migra nada.** Anthropic no soporta migrar datos entre cuentas personales, y esta skill no inventa un botón que no existe: produce un paquete de **reconstrucción manual**.
> - **No respalda secretos.** Las credenciales son C3 y **se rotan, no se respaldan**.
> - El borrador automático de chats **cita y cuenta, no interpreta**. Sin la lectura humana es un índice, y venderlo como resumen es prometer lo que el producto no hace.
> - Sin el export oficial no hay historial de chats, y esa capa entera va a `HUECOS.md`. El resto del respaldo sí se hace.
>
> **Requisitos**
>
> - **Obligatorio:** acceso vigente al proyecto. El respaldo es una operación del presente: el que se aplaza no existe.
> - **Obligatorio:** el **export oficial** de los datos de Claude, solicitado y descargado **antes de 24 horas**, porque su enlace caduca. Es la única vía al historial de chats.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Reporte semanal de inteligencia competitiva · 49

| Campo | Valor |
|---|---|
| **Name** | Reporte semanal de inteligencia competitiva — skill para Claude |
| **URL** | `reporte-inteligencia` |
| **Price** | 49 |
| **Content** | `dist/reporte-inteligencia.zip` → `python3 venta/empaquetar_gumroad.py reporte-inteligencia` |
| **Cover / Thumbnail** | `venta/portadas/reporte-inteligencia-portada.png` (1280×720) · `venta/portadas/reporte-inteligencia-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Seis competidores, ocho métricas y tres acciones para esta semana. Con la cita y la fecha de cada cosa, para que puedas comprobarlo. |
| **Tags** | competencia, reputación, reseñas, benchmark, pyme, claude, skills |

**Description (pegar entera)**

> **Seis competidores, ocho métricas y tres acciones para esta semana. Con la cita y la fecha de cada cosa, para que puedas comprobarlo.**
>
> Convierte **el nombre de una marca y su plaza** en **un reporte semanal de 10 secciones con panel congelado de 6 competidores, tabla de brecha en 8 métricas y 3 acciones de 7 días con dueño y métrica de verificación**, para **quien dirige marca, operación o el negocio entero**.
>
> **Qué NO hace**
>
> - **El modo BÚSQUEDA no cierra una línea base.** Alcanza 2 de 8 métricas y se emite siempre con `ESTADO_LINEA_BASE: ABIERTA`.
> - No usa datos obtenidos saltándose términos de uso ni muros de acceso: el reporte se sostiene sobre lo que cualquiera puede ver.
> - No identifica ni nombra a ningún reseñador. Analiza patrones, no personas.
> - **No recomienda solicitar, comprar, incentivar ni suprimir reseñas**, ni propias ni del competidor: está prohibido por norma en EE. UU. y por política de plataforma en todos los mercados.
>
> **Requisitos**
>
> - **Obligatorio:** el nombre de la marca. Nada más es obligatorio.
> - **Recomendado:** ciudad o dirección. Es la **única** pregunta que se hace si el nombre es ambiguo, y nunca se hacen más de dos.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Respaldo cifrado de proyecto de IA · 49

| Campo | Valor |
|---|---|
| **Name** | Respaldo cifrado de proyecto de IA — skill para Claude |
| **URL** | `respaldo-proyecto-ia-cl` |
| **Price** | 49 |
| **Content** | `dist/respaldo-proyecto-ia-cl.zip` → `python3 venta/empaquetar_gumroad.py respaldo-proyecto-ia-cl` |
| **Cover / Thumbnail** | `venta/portadas/respaldo-proyecto-ia-cl-portada.png` (1280×720) · `venta/portadas/respaldo-proyecto-ia-cl-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Te llevas tu proyecto entero cifrado, con el guion para rehacerlo y la lista de lo que no cabía. Probado en frío antes de que borres nada. |
| **Tags** | claude, proyecto, respaldo, backup, cifrado, skills |

**Description (pegar entera)**

> **Te llevas tu proyecto entero cifrado, con el guion para rehacerlo y la lista de lo que no cabía. Probado en frío antes de que borres nada.**
>
> Convierte **el contenido de un Proyecto de Claude —instrucciones, base de conocimiento, descargas y adjuntos, skills asociadas y el historial de chats del export oficial—** en **un paquete cifrado AES-256 con archivo maestro `RESTAURAR-TODO.md`, resumen de chats, checksums SHA-256 y guion de reconstrucción**, para **quien administra el proyecto**, en **30 a 60 minutos por proyecto de hasta 100 documentos**, una vez recibido el export.
>
> **Qué NO hace**
>
> - **No migra nada.** Anthropic no soporta migrar datos entre cuentas personales, y esta skill no inventa un botón que no existe: produce un paquete de **reconstrucción manual**.
> - **No respalda secretos.** Las credenciales son C3 y **se rotan, no se respaldan**.
> - El borrador automático de chats **cita y cuenta, no interpreta**. Sin la lectura humana es un índice, y venderlo como resumen es prometer lo que el producto no hace.
> - Sin el export oficial no hay historial de chats, y esa capa entera va a `HUECOS.md`. El resto del respaldo sí se hace.
>
> **Requisitos**
>
> - **Obligatorio:** acceso vigente al proyecto. El respaldo es una operación del presente: el que se aplaza no existe.
> - **Obligatorio:** el **export oficial** de los datos de Claude, solicitado y descargado **antes de 24 horas**, porque su enlace caduca. Es la única vía al historial de chats.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Compilador de contexto de proyecto · 49

| Campo | Valor |
|---|---|
| **Name** | Compilador de contexto de proyecto — skill para Claude |
| **URL** | `universal-compilador-contexto` |
| **Price** | 49 |
| **Content** | `dist/universal-compilador-contexto.zip` → `python3 venta/empaquetar_gumroad.py universal-compilador-contexto` |
| **Cover / Thumbnail** | `venta/portadas/universal-compilador-contexto-portada.png` (1280×720) · `venta/portadas/universal-compilador-contexto-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Todo lo que hay en tu carpeta, ordenado por temas, con la versión vigente marcada y la lista de lo que aún no has decidido. |
| **Tags** | claude, proyecto, contexto, documentación, biblioteca, skills |

**Description (pegar entera)**

> **Todo lo que hay en tu carpeta, ordenado por temas, con la versión vigente marcada y la lista de lo que aún no has decidido.**
>
> Convierte **una carpeta de trabajo completa, el historial de chats del proyecto y el conocimiento ya cargado en él** en **un único ZIP `<PROYECTO>_CONTEXTO_<fecha>.zip` con la biblioteca por dominios, el resumen ejecutivo, el resumen de chats, el resumen de contexto y el inventario de documentos con su ubicación**, para **quien dirige el proyecto**, en **una sesión de 60 a 120 minutos para una carpeta de hasta 150 archivos**.
>
> **Qué NO hace**
>
> - **No opina sobre el proyecto ni corrige sus cifras.** Extrae y ordena lo que existe; los conflictos y los huecos se devuelven, no se resuelven.
> - **No modifica la carpeta original.** Todo lo nuevo vive en `CONTEXTO`.
> - La **Ruta A de chats es parcial por diseño**: usa las herramientas de la sesión y no garantiza cobertura completa. La completa exige el ZIP del export oficial.
> - El conocimiento ya cargado en el proyecto se trata como **compilación anterior**, no como fuente primaria: compilar sobre un resumen es copia de copia y hereda el error.
>
> **Requisitos**
>
> - **Obligatorio:** la carpeta de trabajo con todos sus archivos. Por defecto se busca en `/home/claude/fuente`, y el nombre del proyecto se toma del nombre de la carpeta si no se indica otro.
> - **Recomendado:** el historial de chats. Hay dos rutas y **rinden cosas distintas**: la Ruta A usa las herramientas de la sesión y es **parcial por diseño**; la Ruta B usa el ZIP del export oficial y es completa.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

### Productividad de personal por turno · 199

| Campo | Valor |
|---|---|
| **Name** | Productividad de personal por turno — skill para Claude |
| **URL** | `productividad-personal-turno` |
| **Price** | 199 |
| **Content** | `dist/productividad-personal-turno.zip` → `python3 venta/empaquetar_gumroad.py productividad-personal-turno` |
| **Cover / Thumbnail** | `venta/portadas/productividad-personal-turno-portada.png` (1280×720) · `venta/portadas/productividad-personal-turno-miniatura.png` (600×600) → `python3 venta/generar_portadas.py` |
| **Summary** | Sabes en qué franjas pagas plantilla sin venta y en cuáles pierdes venta por falta de mano. |
| **Tags** | restaurante, hostelería, personal, turnos, tpv, productividad, claude, skills |

**Description (pegar entera)**

> **Sabes en qué franjas pagas plantilla sin venta y en cuáles pierdes venta por falta de mano.**
>
> Convierte el export de ventas por franja horaria y el parte de horas del mismo periodo en un informe de dos páginas para el dueño o el encargado, en unos 20 minutos: ventas por hora trabajada y coste de personal sobre venta sin IVA de cada franja y de cada día de la semana, los euros de exceso del periodo, qué parte de ese exceso es de horas fijas que no se pueden tocar, y una propuesta de escalonar entradas y salidas con las horas concretas que recupera.
>
> **Qué NO hace**
>
> - **No calcula el cuadrante legal ni sustituye a asesoría laboral.** No interpreta convenio colectivo, no valida jornada máxima, descansos entre jornadas, festivos, horas complementarias ni registro horario. Toda modificación de jornada, horario o turno se valida con **asesoría laboral o graduado social (España)** o con **abogado laboral (México)** y, donde exista, con la representación legal de los trabajadores. Este informe prepara la decisión; no la autoriza.
> - No calcula nóminas, finiquitos, indemnizaciones ni cotizaciones. Los factores de coste hora son de gestión, no de nómina.
> - No propone despidos ni evalúa a personas. Trabaja con franjas y puestos. Si el encargo pide señalar a alguien, queda fuera de alcance y se dice.
> - No sustituye conocer el local: sin saber qué se hace en cada franja, los porcentajes engañan y el informe lo declara en vez de rellenar el hueco.
>
> **Requisitos**
>
> - **Ventas por franja horaria, sin IVA** (export del TPV: fecha, franja, importe) — es el dato obligatorio. Si el export viene con IVA, se pide el tipo aplicado y se descuenta antes de calcular nada; si no se conoce, se calcula igual y se marca en la cabecera del informe que los porcentajes de coste están inflados por el IVA incluido.
> - **Horas trabajadas de esa misma franja** (fichajes, parte de horas o cuadrante ejecutado) — dato obligatorio. Sin ventas y horas del mismo periodo no hay productividad: hay facturación, que es otra cosa, y el activo se detiene y lo dice.
>
> **Licencia**
>
> Uso comercial permitido en tu actividad, sin límite de ejecuciones. Prohibida la redistribución, reventa o publicación. `LICENSE.txt` dentro.
>
> Copyright 2026 Sergio Berriozábal Serrano.

---

## 7 · Portadas y miniaturas

Gumroad pide una imagen por producto: la **cover** (la enseña en la página del producto, 1280×720)
y la **thumbnail** (la enseña en la tienda y en Discover, cuadrada, 600×600). Sin ellas el
producto se publica igual, pero en la tienda aparece como una caja gris.

Las quince parejas están hechas y en `venta/portadas/`, generadas desde la misma tabla de nombre,
resumen y precio de esta hoja con `python3 venta/generar_portadas.py` (necesita Pillow:
`pip install pillow`). Tipografía del sistema, fondo liso, sin fotos de stock ni marcas ajenas:
línea de producto arriba, nombre, frase de anuncio, precio y "skills para Claude · estándar abierto
Agent Skills". Si cambia un precio o una frase, se cambia aquí y se vuelve a ejecutar el script.

Las de las instalaciones de hostelería no existen porque no se venden por Gumroad
(`OFERTA-HOSTELERIA.md`).
