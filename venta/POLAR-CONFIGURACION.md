# Configuración de Polar — caída de Gumroad, con repositorio de entrega propio

> **Canal vigente: Gumroad** (decisión 8 de [`../catalogo/DECISIONES.md`](../catalogo/DECISIONES.md));
> la hoja de alta es [`GUMROAD-ALTA.md`](GUMROAD-ALTA.md). Polar es la caída si Gumroad no paga a
> México, y **desde el 16-sep-2026 tiene su repositorio de entrega listo** (decisión 13):
> `sberriozabal-rgb/zeus-entrega`, privado, el mismo para Polar y para cualquier otro canal que
> entregue por acceso a repositorio. La plantilla de texto de producto y la lista de lo que NO se
> pone siguen valiendo tal cual.

Plan **gratuito** (5 % + 0,50 $, sin cuota fija). No saltes al plan de 20 $/mes hasta que el
script `punto_equilibrio.py` de `forja-fabrica-de-skills` diga que compensa: con pocos productos
al mes, la cuota fija se come el ahorro de comisión.

## 0 · El repositorio de entrega: `zeus-entrega` (16-sep-2026)

`zeus` es el repositorio de fábrica: lleva las fichas comerciales, los `metadata.json` de
auditoría y la carpeta `venta/`. Dar acceso a un comprador a `zeus` sería entregarle el material
de fábrica junto con el producto (y el 16-sep, además, era público). La entrega por acceso
revocable necesita un repositorio **privado y solo con producto**, y Sergio decidió que sea
**uno solo para Polar y para el resto de canales**.

| Qué | Valor |
|---|---|
| Repositorio | `https://github.com/sberriozabal-rgb/zeus-entrega` · **privado** · rama `main` |
| Contenido | `productos/<slug>/` para los 15 productos del catálogo suelto, con exactamente lo mismo que el zip de Gumroad (skills completas + `LEEME.txt`, sin ficha comercial ni `metadata.json`), más `README.md` y `LICENSE` de comprador |
| Quién lo genera | `python3 venta/publicar_entrega.py` construye `dist/entrega/`; con `--push` lo empuja entero (un solo commit, `--force`: el repo de entrega no lleva historial de fábrica) |
| Quién lo crea | **Sergio, a mano, vacío y privado, sin README.** La sesión de fábrica no puede crear repositorios (`403: sessions are bound to their configured repositories`) ni cambiar su configuración, igual que pasó con `octava-skills` |
| Validación | El mismo validador que el empaquetador: si una skill no pasa, no se construye nada |

**Lo que hay que saber antes de usarlo con Polar, y que Sergio asume al pedir un solo repo:**
la ventaja «GitHub Repository Access» de Polar concede acceso al **repositorio entero**. Con un
solo repositorio, quien compra una skill suelta a 49 € puede leer las 15 carpetas, incluida
CABINA COMPLETA a 249 €. La licencia lo prohíbe, pero el acceso no lo impide. Dos salidas, a
elegir cuando llegue el caso: (a) asumirlo, o (b) crear
después un repositorio por producto con el mismo script (`--remote` a otro remoto y una lista de
productos más corta), que es media hora de trabajo cuando haya un comprador que lo justifique.

## 1 · Abrir Polar y conectarlo — pasos de Sergio, en orden

Ni polar.sh ni api.polar.sh se pueden leer desde la sesión de fábrica (el proxy responde 403),
así que esto lo hace Sergio en el navegador; son diez minutos.

1. **Crear el repositorio vacío** `zeus-entrega` en GitHub (privado, sin README, sin licencia)
   y avisar a la fábrica, que lo llena con `python3 venta/publicar_entrega.py --push`.
   O hacerlo él mismo desde su Mac con el repo `zeus` clonado: el mismo comando.
2. Entrar en <https://polar.sh> con **Continuar con Google → `sberriozabal@gmail.com`**, que es
   la cuenta de Gmail de la casa y la que está unida a la cuenta de GitHub `sberriozabal-rgb`.
3. Crear la organización con los datos fiscales de Sergio y **conectar Stripe con México como
   país**. Si Polar no ofrece México en el alta de cobro, parar aquí: es el hueco que el plan de
   trabajo deja abierto y no tiene sentido crear productos.
4. En *Settings → Integrations → GitHub*, instalar la app de Polar en la cuenta
   `sberriozabal-rgb` **solo con acceso a `zeus-entrega`**, nunca a `zeus` ni a `octava-skills`.
5. Crear una ventaja (*Benefit*) de tipo **GitHub Repository Access** apuntando a
   `sberriozabal-rgb/zeus-entrega` con permiso de **lectura** (*pull*).
6. Crear los productos de la tabla de abajo (pago único, precio en EUR) y asociarles esa
   ventaja. El texto de cada producto sale de la plantilla de §3.
7. **Comprobar el mecanismo antes de publicar nada:** comprar uno a precio de prueba con otra
   cuenta de GitHub, ver que llega la invitación al repositorio, reembolsar y ver que el acceso
   se retira. Si eso no funciona, no hay producto.

## 2 · Productos a crear

### Línea CABINA (DJ) — pago único, entrega por acceso a `zeus-entrega`

| Producto | Precio | Qué da acceso |
|---|---|---|
| Auditoría de biblioteca | 49 € | `productos/auditoria-de-biblioteca/` |
| Parte de bolo | 49 € | `productos/postmortem-de-bolo/` |
| Set por encargo | 49 € | `productos/set-por-encargo/` |
| Peticiones a repertorio | 49 € | `productos/peticiones-a-repertorio/` |
| Presupuesto y contrato de evento | 49 € | `productos/presupuesto-y-contrato-evento/` |
| Demo a sello | 49 € | `productos/demo-a-sello/` |
| **CABINA CORE** | **149 €** | `productos/cabina-core/` |
| **CABINA EVENTOS** | **99 €** | `productos/cabina-eventos/` |
| **CABINA COMPLETA** | **249 €** | `productos/cabina-completa/` |

### Línea neutra — pago único

| Producto | Precio | Qué da acceso |
|---|---|---|
| Plan de cobro de cartera vencida | **79 €** | `productos/cobro-cartera-vencida/` |
| Reporte semanal de inteligencia competitiva | 49 € | `productos/reporte-inteligencia/` |
| Respaldo cifrado de proyecto de IA | 49 € | `productos/respaldo-proyecto-ia-cl/` |
| Compilador de contexto de proyecto | 49 € | `productos/universal-compilador-contexto/` |
| **PACK CONTEXTO** | **89 €** | `productos/pack-contexto/` |

### `productividad-personal-turno` · 199 € · `productos/productividad-personal-turno/`

Única pieza de hostelería con precio suelto; va en el repositorio de entrega como en Gumroad.

### El resto de hostelería — NO va por Polar

La instalación se vende presencial y se cobra por **Stripe México** (pesos) o transferencia. El
ticket alto justifica la comisión menor pese a no ser *merchant of record*. Polar es para
catálogo, no para servicio.

## 3 · Texto de producto — plantilla

Cada producto lleva, en este orden:

1. **La frase de anuncio** de su `ANEXO-A-ficha-comercial.md`. Está escrita para eso.
2. **Qué entrega**, en tres o cuatro líneas.
3. **Qué NO hace.** Literal, de la sección `Límites` de la skill. No lo suavices: es lo que evita
   la devolución y la reseña mala.
4. **Requisitos técnicos**, si los hay (Python, export de rekordbox, etc.).
5. **Licencia**: uso comercial permitido, prohibida la redistribución.

## 4 · Lo que NO se pone en ningún texto de producto

- **Ninguna cifra sin su fuente.** Si citas el 5-9 % de ingresos por estrella, va con sus tres
  límites pegados: es Yelp, es EE. UU., y es ingresos, no margen. Si citas los umbrales de
  BrightLocal, van con `[CONTEXTO EE. UU.]`.
- **Ninguna promesa de resultado.** Ni "conseguirás más reseñas", ni "te firmarán el demo", ni
  "recuperarás tu cartera". Las tres son falsas y las tres son denunciables.
- **Ninguna mención a que la skill está "probada"** hasta que G2 esté levantado. Los casos de
  prueba son de fabricación y así está escrito en las fichas.

## 5 · Después de la primera venta

Anota en la ficha del comprador: qué compró, qué datos reales ejecutó y qué falló. **Eso es lo
que levanta G2**, y tres de esos cierran el gate en toda la línea.
