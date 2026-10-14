# Lanzamiento: los textos listos para pegar, canal por canal

**Estado a 14-oct-2026.** Un mes después de abrir la tienda: 15 productos en Gumroad, el
repositorio público con una estrella y cero pedidos, y ~130 correos en frío a restaurantes con
una respuesta (negativa). La estrategia de canales (`CANALES-DISTRIBUCION.md`) está escrita desde
el 17-sep y **ningún post ha salido**. Nadie compra lo que no ve.

## El cambio de orden que importa

El comprador de una skill es **alguien que ya usa Claude Code**. Un DJ que además usa Claude es
una intersección pequeña; un restaurante que use Claude, más pequeña aún. Por eso el orden de
empuje es el contrario al del catálogo:

| Orden | Producto | Dónde está su comprador | Por qué primero |
|---|---|---|---|
| 1 | **PACK CONTEXTO** (89 €) y sus dos sueltas | r/ClaudeAI, r/ClaudeCode, X, Discord de Claude | El comprador **ya está en Claude** y tiene meses de proyecto que teme perder. Es el único producto cuyo dolor vive dentro de la herramienta |
| 2 | **Cobro de cartera vencida** (79 €) | LinkedIn en español, grupos de pymes y contadores | Dolor con cifra, sector agnóstico, el comprador sabe cuánto tiene vencido |
| 3 | **CABINA** (49–249 €) | r/DJs, r/Beatmatch, grupos de DJ en español, DJ TechTools | Nicho real, pero hay que enseñarles primero qué es una skill |
| 4 | Instalación de hostelería | Visita, WhatsApp, carta en mano | El correo en frío está agotado: 130 envíos, 0 visitas |

**La skill gratuita es el anzuelo en todos los canales**: dos líneas para instalarla y ver cómo
trabaja una pieza de la serie.

## Tres reglas que no se tocan

1. **Decir que es tuyo.** Todas las comunidades aceptan «I built…» y castigan el anuncio
   disfrazado. Un post, una vez, y se contesta a quien comente.
2. **Ninguna promesa ni cifra sin fuente.** Las de la doctrina. Y no decir «probadas».
3. **Un enlace por post**: el repositorio público. Los precios van en un comentario propio o en
   la ficha, no en el título.

## Treinta segundos antes de publicar nada

- **Topics del repositorio** (Settings del repo → ⚙ junto a *About* → Topics):
  `claude-code` `claude-skills` `agent-skills` `claude` `dj` `rekordbox` `restaurant`
  `accounts-receivable` `plugin-marketplace` `spanish`. Es lo que hace que aparezca en las
  búsquedas de GitHub. La fábrica no puede ponerlos (403 del proxy).
- **Gumroad → Settings → Discover: apagado** en los 15 productos. Si una venta entra por el
  buscador de Gumroad, la comisión es el 30 %.

---

## 1 · r/ClaudeAI y r/ClaudeCode (inglés) · el primero que sale

**Title:** `I turned my consulting work into Claude Code skills. One is free (restaurant shift checklists), the rest are paid. Here's what they do and don't do.`

**Body:**

> I'm a consultant (restaurants, DJ booths, B2B collections). Over the summer I rewrote the
> procedures I actually use as Claude Code skills, following the open Agent Skills spec. Each one
> reads your own data (a rekordbox XML, an invoice list, a POS export), runs a procedure with
> declared thresholds, and says what it does NOT do.
>
> **Free, installable now:**
> ```
> /plugin marketplace add sberriozabal-rgb/octava-skills
> /plugin install octava-abiertas@octava
> ```
> That's `apertura-cierre-turno`: opening / handover / closing checklists for a restaurant, with an
> owner per task, exact time and a "done" criterion, plus the incident report. Spanish-language
> output (that's my market), but the structure is the point.
>
> **Paid (17 in total, fully documented in the repo):**
> - *Context pack* for anyone with months of work inside a Claude project: one skill exports it to
>   an encrypted bundle with a rebuild script, the other turns it into an ordered library with
>   "the list of what you haven't decided yet". It does **not** migrate your account; the platform
>   doesn't allow it.
> - *Overdue receivables plan*: priority by age × cause, the messages already written, escalation
>   dates, DSO dashboard. B2B only, not legal advice.
> - *Six DJ-booth skills*: library audit by booth risk, gig post-mortem from the exported history,
>   set-for-a-slot, request lists, quote + contract clauses, demo submission timing. They read
>   exports; they never write to rekordbox or Serato.
>
> Every skill ships with four test cases and a "what it doesn't do" section, because I'd rather
> lose a sale than get a refund. Repo with every sheet and price:
> https://github.com/sberriozabal-rgb/octava-skills
>
> Happy to answer anything about how they're structured (the frontmatter, the procedure
> template, the validator) — that part is reusable for anyone writing their own.

**Comentario propio, nada más publicar:** `Prices, since people ask: singles 49 €, DJ bundle of
six 249 €, receivables 79 €, context pack 89 €. Gumroad, one-time, no subscription.`

## 2 · Show HN (inglés) · al día siguiente

**Title:** `Show HN: I packaged 17 consulting procedures as Claude Code skills (one free)`

**Text:** el mismo cuerpo del post 1, sin los bloques de código al principio (HN no renderiza
Markdown) y con el enlace al repositorio en el campo URL. Primer comentario propio: cómo está
hecho el validador de 20 puntos y por qué 19/20 y no 20.

## 3 · Hilo en X (inglés) · mismo día que HN

1. `I turned the procedures I use as a consultant into Claude Code skills. 17 of them. One is free. Thread 🧵`
2. `Free one: restaurant opening/closing checklists with an owner per task and a "done" criterion. Install: /plugin marketplace add sberriozabal-rgb/octava-skills`
3. `For anyone with months inside a Claude project: a context pack. Export to an encrypted bundle, rebuild script, then an ordered library with "what you haven't decided yet". Doesn't migrate accounts: the platform doesn't allow it, and I won't pretend otherwise.`
4. `For DJs: six skills that read your rekordbox/Serato exports. Which tracks will fail at the next gig, what actually happened at the last one, a set rebuilt for the slot they just gave you. Never write to your library.`
5. `Every skill has a "what it does NOT do" section and four test cases. All sheets and prices: github.com/sberriozabal-rgb/octava-skills`

## 4 · r/DJs y r/Beatmatch (inglés) · la semana siguiente

**Title:** `I built a tool that reads your rekordbox XML and tells you which tracks will fail at your next gig, in what order to fix them`

**Body:**

> Not a cleaner. Lexicon cleans; this doesn't touch your library. It reads the exported
> `collection.xml` and ranks what will actually hurt you in the booth: broken paths and missing
> beatgrids first, missing ratings last, and a Top 3 for the gig date you give it.
>
> It runs inside Claude Code as a "skill" (a folder with a procedure the model follows). If you
> don't use Claude Code, this isn't for you yet, and I'd rather say so.
>
> **Offer, no strings:** send me your XML and I'll send back the three most urgent things, free.
> If it's useful, there's a paid version with five more booth skills (gig post-mortem from your
> history export, set for a given slot, request lists, quotes + contract clauses, demo timing).
> Sheets and prices: https://github.com/sberriozabal-rgb/octava-skills

## 5 · LinkedIn (español) · cobro de cartera vencida

> ¿Tienes facturas vencidas y no sabes por cuál empezar?
>
> Convertí el protocolo de cobro que uso en consultoría en una skill para Claude. Le pasas el
> listado y te devuelve: a quién reclamar primero **y por qué causa** —no es lo mismo el que
> discute la factura que el que no tiene la orden de compra—, el mensaje redactado para cada uno,
> y la fecha exacta en la que subes el tono si no paga.
>
> Lo que más recupera no es reclamar antes: es dejar de reclamar sobre facturas mal emitidas.
> Mientras el papel está mal, el reloj no corre a tu favor.
>
> No es asesoría jurídica y no sirve para cobrar a particulares. 79 €, pago único. Ficha
> completa en el primer comentario.

**Primer comentario:** `https://github.com/sberriozabal-rgb/octava-skills/blob/main/catalogo/cobro-cartera-vencida.md`

## 6 · Grupos de DJ en español (Facebook, WhatsApp, foros)

> Llevo años arreglando lo mismo antes de cada bolo, así que lo convertí en herramientas para
> Claude. La que más se entiende: exportas tu colección de rekordbox y te dice qué tracks te van
> a fallar el sábado y en qué orden arreglarlos. No limpia la biblioteca —para eso está Lexicon—;
> te dice qué va primero.
>
> Si quieres probar: mándame tu XML y te devuelvo las tres cosas más urgentes, gratis. Las seis
> skills de cabina, con lo que hacen y lo que no, aquí:
> github.com/sberriozabal-rgb/octava-skills

## 7 · Listas «awesome» en GitHub (inglés) · un *pull request* cada una

Buscar en GitHub `awesome-claude-code` y `awesome-claude-skills` (hay varias; las de más
estrellas primero). En cada una, un PR que añada una línea en la sección de marketplaces o de
skills:

```
- [octava-skills](https://github.com/sberriozabal-rgb/octava-skills) — Plugin marketplace with
  one free restaurant-ops skill and 17 documented consulting skills (DJ booth, B2B collections,
  restaurant operations). Spanish-language output.
```

Título del PR: `Add octava-skills (marketplace + free restaurant-ops skill)`. La fábrica no
puede abrirlos: están fuera del alcance de la sesión.

## 8 · Directorios que listan marketplaces

`claudemarketplaces.com` se actualiza solo desde GitHub según su web: **los topics del paso cero
son lo que lo hace visible ahí**. El correo a `hi@claudemarketplaces.com` está redactado en
`CONSULTAS-PENDIENTES.md` y sin enviar.

---

## Calendario de una semana, sin inventar nada

| Día | Qué | Tiempo |
|---|---|---|
| Hoy | Topics del repo · Discover apagado en Gumroad · post 1 en r/ClaudeAI | 20 min |
| +1 | Show HN · hilo en X · PR a dos listas awesome | 30 min |
| +2 | LinkedIn (cobro) · correo a claudemarketplaces | 10 min |
| +4 | r/DJs y r/Beatmatch · dos grupos de DJ en español | 15 min |
| Cada día | Contestar comentarios. Un «send me your XML» atendido vale más que diez posts | 15 min |

**Qué mide si funciona:** visitas al repositorio (Insights → Traffic, solo lo ve el dueño),
instalaciones de la skill gratuita (no se miden; cuentan las estrellas y los *issues*), y ventas
en Gumroad. Si en dos semanas hay tráfico y cero ventas, el problema es el precio o la ficha, y
se toca. Si hay cero tráfico, el problema es que no se publicó.
