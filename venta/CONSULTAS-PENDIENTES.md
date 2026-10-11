# Consultas pendientes a terceros — listas para enviar

Tres huecos del informe FORJA v1.1.0 que se cierran escribiendo. Los textos están en los
borradores de Gmail de `sergio@redcontramar.com` (asunto idéntico al de aquí) y copiados abajo.
## Estado a 2-oct-2026 — lo que contestaron y lo que cambia

Leído en el correo de la casa el 2-oct-2026. Los tres hilos están en Gmail con el asunto de abajo.

| Consulta | Qué pasó | Lo que cambia |
|---|---|---|
| **myClaude** | **No se puede contactar por correo.** Dos envíos el 17-sep (`hello@myclaude.sh` desde esta sesión, `hi@myclaude.sh` desde otra) y los dos **rebotaron** el 20-sep: el servidor de correo del dominio no acepta conexiones (`4.4.1 timed out` en 76.76.21.21 y 216.198.79.1 durante 72 horas). No es una dirección equivocada: el dominio no recibe correo | myClaude sigue sin respuesta sobre IVA y pago a México. Única vía que queda: una *issue* en su GitHub (<https://github.com/myclaude-sh>, piden «friction reports» por ahí) o un mensaje en X (`@myclaude_sh`). **Mientras no conteste, no entra** (plan §1, paso 1.6) |
| **SkillHQ** | **Contestó Mirek (SkillHQ Support) el 22-sep.** Tres respuestas claras, abajo | Cierra el hueco. SkillHQ **no sirve para el catálogo a la tarifa de la casa**: tope de 50 € por producto, sin pago a México por Stripe. Detalle en «Lo que SkillHQ dijo» |
| **claudemarketplaces** | No enviada (retenida hasta la decisión pendiente 6) | Sin cambio |

### Lo que SkillHQ dijo, punto por punto (22-sep-2026)

1. **IVA.** Depende del nivel de vendedor. En **Starter**, SkillHQ es *merchant of record*: cobra,
   calcula y remite el IVA europeo y emite la factura al comprador; el vendedor declara el ingreso
   en México. En **Pro**, el vendedor es el *merchant of record* y asume IVA y facturación.
2. **Pago a México.** Su Stripe Connect **no paga a México** (los pagos transfronterizos de una
   plataforma del EEE no incluyen cuentas mexicanas; citan la documentación de Stripe). Un vendedor
   Starter en México cobra por **PayPal verificado, en euros**; PayPal convierte a pesos con su
   comisión.
3. **Precio.** Rango admitido: **2 a 50 € por producto**. Un producto de 249 € **no se admite**, y
   no tienen evidencia de ventas a ese precio. Sugieren publicar las skills sueltas dentro del rango.

**Lo que eso significa contra la tarifa de `catalogo/PRECIOS.md`:** caben las seis de CABINA sueltas
a 49 € y las tres neutras a 49 €; **no caben** CABINA COMPLETA (249), CORE (149), EVENTOS (99),
cobro de cartera (79), PACK CONTEXTO (89) ni `productividad-personal-turno` (199). Y lo que entre
cobra por PayPal con una conversión encima. SkillHQ es, como mucho, un escaparate de piezas
sueltas de 49 €, no un canal para el catálogo.

### Lo que salió de la casa el 25-sep, y hay que saber

En el mismo hilo, dos respuestas a Mirek firmadas por Sergio (01:50 y 02:31 UTC) y generadas por
otra sesión de Claude Code (llevan su pie). Dicen: nivel Starter y cobro por PayPal en euros
confirmados; se ofrecen **dos skills de hostelería** (`escandallo-ingenieria-menu` y
`respuesta-resenas`) como *private beta listings* **a 12–18 € cada una**, descritas como
«production-tested in Madrid»; y se pregunta por el alta KYC desde México. SkillHQ **no ha
contestado** a 2-oct.

Tres cosas que conviene mirar antes de seguir por ahí, porque chocan con lo escrito:

1. **Precio.** `PRECIOS.md` no vende hostelería suelta salvo `productividad-personal-turno` a 199 €;
   el escandallo y las reseñas van dentro de la instalación de 2.500 / 4.900 €. Ofrecerlas a 12–18 €
   es una tarifa nueva que no está decidida en `DECISIONES.md`, y la regla es «se quita alcance,
   jamás se baja el precio».
2. **«Probadas».** La regla 1 de `GUMROAD-ALTA.md` §4 y la 1 de `LISTA-DE-VENTA.md` §6: no decir
   «probadas» hasta levantar G2, que sigue en 0/17.
3. **Entrega.** Los dos correos no llevan adjunto. El contenido de las dos `.skill` fue **dentro del
   cuerpo del mensaje**, como texto en base64 (37 KB y 84 KB) junto con marcado de herramienta
   (`<parameter name="attachments">`). Es decir: SkillHQ recibió dos correos ilegibles que contienen
   las dos skills enteras, decodificables, antes de ningún alta. Es entrega por adjunto a un tercero
   sin contrato, la desviación que la doctrina prohíbe, y además se ve mal. Si se sigue con SkillHQ,
   conviene un correo corto de Sergio, escrito a mano, que pida disculpas por los dos mensajes
   malformados, retire los ficheros y deje el precio en el rango de la casa.

Lo de abajo es el texto original de las tres consultas, tal como se enviaron.

Van en inglés porque los tres son productos internacionales; SkillHQ cobra en euros pero
publica en inglés.

| # | A quién | Hueco que cierra | Qué cambia según la respuesta |
|---|---|---|---|
| 1 | myClaude | ¿*Merchant of record*? ¿Paga a México? | Si el IVA europeo es del creador, myClaude entra solo si el tráfico lo justifica |
| 2 | SkillHQ | Lo mismo, más si 249 es un precio que su tienda admite | Si no hay evidencia de venta por encima de 50 €, CABINA COMPLETA no va a SkillHQ; el de cobro sí cabría |
| 3 | claudemarketplaces.com | Cómo se entra en el directorio (`/submit` da 404) | Solo importa si se publica el marketplace gratuito, que está parado (decisión pendiente 6) |

---

## 1 · myClaude

**Para:** `hello@myclaude.sh` · enviada 17-sep · **rebotada el 20-sep** (servidor de correo inalcanzable)
**Asunto:** Seller from Mexico: merchant of record, EU VAT and payouts

> Hello,
>
> I am preparing to publish two paid skills on myClaude and I have three questions before I run
> `myclaude publish`. I read the monetization, pricing and vault.yaml docs; none of them covers
> these points.
>
> 1. **Merchant of record.** When a buyer in the EU purchases a skill, who is the seller of
>    record for VAT purposes: myClaude, or the creator? In other words, does myClaude collect
>    and remit VAT / sales tax on my behalf, or is that my obligation?
> 2. **Payouts to Mexico.** Your docs say Stripe Connect Express pays out to "35+ countries"
>    without listing them. Is Mexico among them, and in which currency would I receive payouts?
> 3. **Fees.** I understand the split is 92 / 8 and that Stripe processing is deducted from the
>    creator's side. Is there any other fee (payout, currency conversion, chargeback) I should
>    account for?
>
> Thank you,
> Sergio Berriozábal Serrano

## 2 · SkillHQ

**Para:** `support@skillhq.dev` · enviada 17-sep · **respondida el 22-sep**
**Asunto:** Seller from Mexico: VAT handling, payouts and price range

> Hello,
>
> I am considering listing two paid Claude skills on SkillHQ and I have three questions before
> registering as a seller.
>
> 1. **VAT.** For a buyer in the EU, does SkillHQ act as merchant of record and remit VAT, or is
>    the seller responsible for it?
> 2. **Payouts to Mexico.** Does your Stripe setup pay out to a seller based in Mexico? In which
>    currency?
> 3. **Price range.** The products I see listed go from 2 to 50 €. One of mine is a six-skill
>    pack priced at 249. Is there a maximum price, and do you have any evidence of products in
>    that range selling on the platform? I would rather know before listing.
>
> Thank you,
> Sergio Berriozábal Serrano

## 3 · claudemarketplaces.com

**Para:** `hi@claudemarketplaces.com` · **no enviada** (decisión pendiente 6)
**Asunto:** How to get a marketplace listed

> Hello,
>
> I maintain a Claude Code plugin marketplace on GitHub (a `marketplace.json` validated with
> `claude plugin validate`). I would like it listed in your directory. Your `/submit` page
> returns a 404 and I could not find a submission procedure on the site.
>
> Could you tell me how listings are added: a GitHub topic, a pull request, a form, or an email
> to you with the repository URL?
>
> Thank you,
> Sergio Berriozábal Serrano

---

## Lo que ya NO hace falta preguntar

Verificado por búsqueda el 15-sep-2026 (`PLAN-DE-TRABAJO.md` §2 y §3): el 10 % + 0,50 de
Gumroad **no** incluye el procesamiento de tarjeta (coste efectivo ≈ 12,9 % + 0,80 por venta
directa), Gumroad paga a México por **transferencia a banco local**, y muestra precios en EUR
pero cobra en USD. El paso 1.4 del plan confirma la cifra exacta en el desglose de la primera
venta.
