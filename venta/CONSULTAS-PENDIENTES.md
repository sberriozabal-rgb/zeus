# Consultas pendientes a terceros — listas para enviar

Tres huecos del informe FORJA v1.1.0 que se cierran escribiendo. Los textos están en los
borradores de Gmail de `sergio@redcontramar.com` (asunto idéntico al de aquí) y copiados abajo.
**Falta el destinatario en los tres:** los dominios `myclaude.sh`, `skillhq.dev` y
`claudemarketplaces.com` están bloqueados desde la sesión de trabajo y no pude sacar la
dirección de contacto. Se toma del pie de página o del formulario de cada web al enviar.

Van en inglés porque los tres son productos internacionales; SkillHQ cobra en euros pero
publica en inglés.

| # | A quién | Hueco que cierra | Qué cambia según la respuesta |
|---|---|---|---|
| 1 | myClaude | ¿*Merchant of record*? ¿Paga a México? | Si el IVA europeo es del creador, myClaude entra solo si el tráfico lo justifica |
| 2 | SkillHQ | Lo mismo, más si 249 es un precio que su tienda admite | Si no hay evidencia de venta por encima de 50 €, CABINA COMPLETA no va a SkillHQ; el de cobro sí cabría |
| 3 | claudemarketplaces.com | Cómo se entra en el directorio (`/submit` da 404) | Solo importa si se publica el marketplace gratuito, que está parado (decisión pendiente 6) |

---

## 1 · myClaude

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
