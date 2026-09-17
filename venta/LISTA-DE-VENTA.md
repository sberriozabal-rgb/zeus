# Lista maestra de venta — qué está hecho y qué falta, con su dueño

Estado a 17-sep-2026. Una sola página para no tener que leer las otras diez: lo que la fábrica
ya dejó listo, lo que solo puede hacer Sergio, y en qué orden. Cada línea apunta al documento que
la sostiene.

## 0 · En una frase

**Las 17 skills están a la venta y todo el material de venta existe.** Lo único que no ha pasado
todavía es lo que ningún documento puede hacer: abrir la cuenta de Gumroad, pegar las quince
fichas, enviar los correos que están en borradores y hacer una visita. Y una venta.

## 1 · Lo que ya está hecho (la fábrica)

| Pieza | Dónde | Estado |
|---|---|---|
| 17 skills en `ACORDADO`, 19/20, con `SKILL.md`, `README.md`, `CHANGELOG.md`, `LICENSE.txt`, casos y fuentes | `../skills/` | ✅ 17/17 validan (`empaquetar_gumroad.py` se niega a empaquetar si una falla) |
| Tarifa cerrada, G3 levantado en las 17 | `../catalogo/PRECIOS.md` | ✅ ratificada 15-sep-2026 |
| Decisiones con su razón (11) | `../catalogo/DECISIONES.md` | ✅ |
| Matriz de gates | `../catalogo/ESTADO-GATES.md` | ✅ G1, G3, G5 en 17/17 · G4 en 16/17 · G2 en 0/17 (correcto) |
| **Descripción de los 15 productos de Gumroad**: nombre, slug, precio, resumen, tags, descripción entera, política de devolución | `GUMROAD-ALTA.md` | ✅ 15/15 con tags y portada asignada |
| **Portada y miniatura de los 15 productos** | `portadas/` · `generar_portadas.py` | ✅ 30 imágenes, generadas desde la hoja de alta |
| **Zips de producto** sin material de fábrica | `python3 empaquetar_gumroad.py` → `dist/` | ✅ 16 zips, regenerados 16-sep-2026 (no se suben a git) |
| **Descripción de las instalaciones de hostelería** (Esencial, Completa, suelta), qué incluyen, qué no, cómo se cobran | `OFERTA-HOSTELERIA.md` | ✅ nueva, 16-sep-2026 |
| Guion de la visita de 45 minutos | `GUION-VISITA.md` | ✅ alineado con la Completa de 7 skills |
| Mensajes de primer contacto, confirmación y seguimiento (hostelería, DJ, B2B) | `MENSAJES.md` | ✅ |
| Landing del Diagnóstico Exprés | `landing/octava-diagnostico-expres.html` | ✅ v1.0 |
| Calendario de LinkedIn, cuatro semanas | `CALENDARIO-LINKEDIN.md` | ✅ |
| Locuciones para México | `locuciones/` | ✅ tres tomas |
| Anexo de seguridad alimentaria para `receta-estandar` | `ANEXO-CONTRATO-INOCUIDAD.md` | ✅ redactado · ⚠️ pendiente de abogado y de técnico |
| Consultas a myClaude, SkillHQ y claudemarketplaces | `CONSULTAS-PENDIENTES.md` | ✅ redactadas · ✅ destinatario puesto en los tres borradores de Gmail el 17-sep |
| Pipeline de la campaña de CDMX, prospecto a prospecto | `PIPELINE.md` | ✅ leído y ordenado el 15-sep |
| Escaparate público con ficha y enlace de compra por skill | <https://github.com/sberriozabal-rgb/octava-skills> | ✅ publicado (decisión 10) · sus enlaces apuntan a `cabina.gumroad.com/l/<slug>` |

## 2 · Lo que solo puede hacer Sergio, en este orden

| # | Qué | Con qué | Cuánto tarda |
|---|---|---|---|
| 1 | ~~Enviar la respuesta a Grupo RosaNegra~~ ✅ enviada el 16-sep | `PIPELINE.md` cabecera | — |
| 2 | ~~Seguimientos y primeros contactos~~ ✅ 24 correos enviados el 15 y 16-sep: la respuesta al grupo que contestó, los 14 seguimientos únicos y 9 primeros contactos (dos rebotes pasan a teléfono). **Queda:** un primer contacto que el filtro de permisos bloqueó, con el borrador listo en Gmail | `PIPELINE.md` §1 · pipeline privado en Drive | 1 clic |
| 3 | ~~Abrir la cuenta de Gumroad~~ ✅ tienda <https://cabina.gumroad.com> abierta el 16-sep. **Queda:** verificar identidad, método de cobro desde México y W-8BEN | `GUMROAD-ALTA.md` bloque 0 | la verificación |
| 4 | ~~Dar de alta CABINA COMPLETA y Plan de cobro de cartera vencida~~ ✅ en alta el 16-sep, con los 15 del catálogo suelto | `GUMROAD-ALTA.md` bloques 1 a 3 | — |
| 5 | **Comprar uno a 1 USD** (o esperar la primera venta) y apuntar el desglose real de comisión | `PLAN-DE-TRABAJO.md` §2, paso 1.4 | 10 min |
| 6 | ~~Dar de alta los otros 13~~ ✅ en alta el 16-sep | `GUMROAD-ALTA.md` bloque 6 · `portadas/` | — |
| 7 | **Comprobar que cada enlace del escaparate responde** (`cabina.gumroad.com/l/<slug>` para los 15 slugs) | `octava-skills` | 15 min |
| 8 | **Las dos conversaciones de prueba** (un DJ con nombre, una empresa con nombre): gratis a cambio de la cifra escrita y el permiso de publicarla | `PIPELINE.md` §3 · `MENSAJES.md` | Es el hueco que importa |
| 9 | **La primera visita de hostelería** con el guion y la oferta | `GUION-VISITA.md` · `OFERTA-HOSTELERIA.md` | 45 min + desplazamiento |
| 10 | Revisión del abogado del anexo de inocuidad y del técnico en seguridad alimentaria (`receta-estandar`) | `ANEXO-CONTRATO-INOCUIDAD.md` | Antes de entregar la primera Completa |
| 11 | Enviar las tres consultas a myClaude, SkillHQ y claudemarketplaces. **Los borradores ya llevan destinatario** (17-sep): `hello@myclaude.sh`, `support@skillhq.dev`, `hi@claudemarketplaces.com` | `CONSULTAS-PENDIENTES.md` | 3 clics · solo si se quiere un segundo canal |

Lo que no está en esta lista no bloquea ninguna venta.

## 3 · Los 15 productos de Gumroad, uno a uno

| Slug (URL de Gumroad) | Precio | Zip | Portada | Ficha en la hoja |
|---|---|---|---|---|
| `cabina-completa` | 249 | `dist/cabina-completa.zip` | ✅ | bloque 1 |
| `cobro-cartera-vencida` | 79 | `dist/cobro-cartera-vencida.zip` | ✅ | bloque 2 |
| `cabina-core` | 149 | `dist/cabina-core.zip` | ✅ | bloque 6 |
| `cabina-eventos` | 99 | `dist/cabina-eventos.zip` | ✅ | bloque 6 |
| `auditoria-de-biblioteca` | 49 | `dist/auditoria-de-biblioteca.zip` | ✅ | bloque 6 |
| `postmortem-de-bolo` | 49 | `dist/postmortem-de-bolo.zip` | ✅ | bloque 6 |
| `set-por-encargo` | 49 | `dist/set-por-encargo.zip` | ✅ | bloque 6 |
| `peticiones-a-repertorio` | 49 | `dist/peticiones-a-repertorio.zip` | ✅ | bloque 6 |
| `presupuesto-y-contrato-evento` | 49 | `dist/presupuesto-y-contrato-evento.zip` | ✅ | bloque 6 |
| `demo-a-sello` | 49 | `dist/demo-a-sello.zip` | ✅ | bloque 6 |
| `pack-contexto` | 89 | `dist/pack-contexto.zip` | ✅ | bloque 6 |
| `reporte-inteligencia` | 49 | `dist/reporte-inteligencia.zip` | ✅ | bloque 6 |
| `respaldo-proyecto-ia-cl` | 49 | `dist/respaldo-proyecto-ia-cl.zip` | ✅ | bloque 6 |
| `universal-compilador-contexto` | 49 | `dist/universal-compilador-contexto.zip` | ✅ | bloque 6 |
| `productividad-personal-turno` | 199 | `dist/productividad-personal-turno.zip` | ✅ | bloque 6 |

`cabina-carrera` existe en el empaquetador pero no se da de alta: es `demo-a-sello` con otro
nombre y al mismo precio. Precios en EUR si Gumroad lo admite; si solo USD, la misma cifra.

## 4 · Los productos de hostelería (no van por Gumroad)

| Producto | Skills | Precio | Ficha | Cobro |
|---|---|---|---|---|
| Instalación Esencial | 3 | 2.500 € | `OFERTA-HOSTELERIA.md` §1 | Stripe México o transferencia |
| Instalación Completa | 7 | 4.900 € | `OFERTA-HOSTELERIA.md` §2 | Stripe México o transferencia · anexo de inocuidad firmado antes de entregar `receta-estandar` |
| `productividad-personal-turno` suelta | 1 | 199 € | `GUMROAD-ALTA.md` bloque 6 | Gumroad |

## 5 · Lo que se corrigió el 16-sep-2026 para que todo diga lo mismo

- `catalogo/PRECIOS.md`, `catalogo/DECISIONES.md` §1 y `venta/GUION-VISITA.md` decían que la
  Completa eran 6 skills y que `receta-estandar` no se facturaba; la decisión 11 dice 7 skills
  con anexo firmado. Alineados. Los README y fichas de hostelería que decían "sistema de 6" dicen
  ahora 7.
- `reporte-inteligencia` no tenía `README.md` y su `CHANGELOG.md` se paraba en la 1.1.0 aunque
  la skill es 1.2.0: README escrito y entrada 1.2.0 añadida. Su frontmatter decía "18/20
  pendiente de reauditoría"; ahora dice el 19/20 medido el 15-sep.
- Versiones desalineadas: `apertura-cierre-turno` (frontmatter 1.1.1, resto 1.1.2),
  `productividad-personal-turno` (README v1.1.0, resto 1.1.1) y `universal-compilador-contexto`
  (README v1.0.0, resto 1.1.0). Corregidas.
- El README de `respuesta-resenas` conservaba una nota de auditoría de la v1.1 (16/20 contra
  19/20) que la v1.2.0 dejó sin sentido. Sustituida por la vigente.
- El LEEME de cada zip avisa de que `ANEXO-A-ficha-comercial.md` y `metadata.json` no van
  dentro a propósito, porque varios README los citan.
- La hoja de Gumroad no tenía tags en 13 de los 15 productos ni campo de portada en ninguno, y
  llamaba "skill para Claude" a tres packs de varias skills. Añadidos y corregidos.

## 5b · Revisión de venta del 16-sep-2026 (segunda pasada)

- Empaquetador ejecutado: **las 17 validan y salen los 16 zips** sin `metadata.json` ni ficha comercial.
- Hoja de Gumroad, lista maestra, `PRECIOS.md` y `metadata.json` **dicen el mismo precio en los 15
  productos**; las 30 portadas existen con el nombre de su slug.
- Escaparate `octava-skills`: las 17 fichas llevan la versión y el precio de zeus y los 15 enlaces de
  Gumroad cubren los 15 slugs. La copia de `apertura-cierre-turno` del plugin iba atrasada
  (1.1.1 y «6 skills»): sincronizada con zeus y plugin `octava-abiertas` en 1.0.1.
- Seis `metadata.json` de hostelería no tenían campo de precio; añadido con la misma redacción que
  `reporte-inteligencia-competencia`. Es material de fábrica, no entra en los zips.
- El caso de integración de `apertura-cierre-turno` hablaba de un sistema de seis; ahora siete.
- **No verificable desde la fábrica:** que <https://sberriozabal-rgb.github.io/octava-skills/>
  y los 15 enlaces `cabina.gumroad.com/l/<slug>` respondan. El proxy de la sesión bloquea GitHub
  Pages y Gumroad; lo comprueba Sergio desde su navegador (paso 7 de §2).

## 5c · Ejecución del 17-sep-2026 (tercera pasada, sobre el plan)

Sergio pidió ejecutar el plan de trabajo. Lo que la fábrica podía hacer desde el repositorio, hecho;
lo que no, dicho.

- **La v1.0 del plan (15-sep, «78 skills», «14 no validan», «CORE 249 USD», «cobro 69 USD») está
  retirada**; manda la v1.1 de `PLAN-DE-TRABAJO.md` y la tarifa de `catalogo/PRECIOS.md`. El
  parche de frontmatter de la v1.0 **no se aplica** en este repositorio: no hay nada que parchear.
- Fase 0.1: empaquetador ejecutado de nuevo el 17-sep. **17/17 validan y salen los 16 zips** en
  `dist/`, sin ficha comercial ni `metadata.json`.
- Fase 1.5: <https://github.com/sberriozabal-rgb/octava-skills> **responde en público**,
  verificado desde la fábrica (README con las 17, tres líneas, precios y Gumroad como canal).
- **Sigue sin poder verificarse desde la fábrica**: <https://cabina.gumroad.com>, los 15 enlaces
  `cabina.gumroad.com/l/<slug>` y <https://sberriozabal-rgb.github.io/octava-skills/>. El proxy los
  bloquea también el 17-sep. Lo comprueba Sergio (paso 7 de §2).
- Consultas a terceros: destinatarios localizados y **puestos en los tres borradores de Gmail**, sin
  enviar. `hello@myclaude.sh` está verificado en la página de la organización en GitHub;
  `support@skillhq.dev` y `hi@claudemarketplaces.com` salen de resultados de búsqueda de sus
  propias webs (`skillhq.dev/become-seller`, `claudemarketplaces.com/about`), que el proxy no deja
  abrir. Si uno rebota, la web correspondiente tiene el dato en el pie.
- Fase 2 (la que importa) **sigue en cero**: los dos correos de prueba de `MENSAJES.md` no tienen
  a quién ir hasta que Sergio ponga un DJ y una empresa con nombre (`PROSPECCION.md` §2 y §3).
- Visto en Gmail el 17-sep: **una tanda nueva de más de cincuenta borradores** «Tres hallazgos para
  X, sin costo» creados esa madrugada (02:30–02:37 UTC), sin destinatario. No los toca esta pasada:
  son de la campaña de hostelería y su envío es decisión de Sergio con el pipeline privado delante.

## 6 · Las reglas que siguen sin tocarse

1. Ninguna cifra sin su fuente y su límite. Ninguna promesa de resultado. No decir "probadas"
   hasta que G2 esté levantado.
2. Ante negociación se quita alcance, jamás se baja el precio.
3. Un seguimiento por prospecto, y ninguno más.
4. No se fabrica una skill nueva hasta que haya tres vendidas a alguien que pagó.
