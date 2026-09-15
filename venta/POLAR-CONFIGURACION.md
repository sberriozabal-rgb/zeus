# Configuración de Polar — lista para copiar

Plan **gratuito** (5 % + 0,50 $, sin cuota fija). No saltes al plan de 20 $/mes hasta que el
script `punto_equilibrio.py` de `forja-fabrica-de-skills` diga que compensa: con pocos productos
al mes, la cuota fija se come el ahorro de comisión.

## Antes de crear nada

1. Crear la organización en Polar con tus datos fiscales.
2. Conectar la integración de **GitHub** y apuntarla a `sberriozabal-rgb/zeus`.
3. Verificar que Polar concede y revoca acceso al repositorio al comprar y al cancelar. **Es todo
   el mecanismo de entrega.** Si eso no funciona, no publiques nada todavía.

## Productos a crear

### Línea CABINA (DJ) — pago único, entrega por acceso al repo

| Producto | Precio | Qué da acceso |
|---|---|---|
| Auditoría de biblioteca | 49 € | `skills/cabina/auditoria-de-biblioteca/` |
| Parte de bolo | 49 € | `skills/cabina/postmortem-de-bolo/` |
| Set por encargo | 49 € | `skills/cabina/set-por-encargo/` |
| Peticiones a repertorio | 49 € | `skills/cabina/peticiones-a-repertorio/` |
| Presupuesto y contrato de evento | 49 € | `skills/cabina/presupuesto-y-contrato-evento/` |
| Demo a sello | 49 € | `skills/cabina/demo-a-sello/` |
| **CABINA CORE** | **149 €** | auditoría + parte de bolo + set por encargo |
| **CABINA EVENTOS** | **99 €** | peticiones + presupuesto y contrato |
| **CABINA COMPLETA** | **249 €** | las seis |

### Línea neutra — pago único

| Producto | Precio | Qué da acceso |
|---|---|---|
| Plan de cobro de cartera vencida | **79 €** | `skills/neutro/cobro-cartera-vencida/` |
| Reporte semanal de inteligencia competitiva | 49 € | `skills/neutro/reporte-inteligencia/` |
| Respaldo cifrado de proyecto de IA | 49 € | `skills/neutro/respaldo-proyecto-ia-cl/` |
| Compilador de contexto de proyecto | 49 € | `skills/neutro/universal-compilador-contexto/` |
| **PACK CONTEXTO** | **89 €** | respaldo + compilador |

### Hostelería — NO va por Polar

La instalación se vende presencial y se cobra por **Stripe México** (pesos) o transferencia. El
ticket alto justifica la comisión menor pese a no ser *merchant of record*. Polar es para
catálogo, no para servicio.

## Texto de producto — plantilla

Cada producto lleva, en este orden:

1. **La frase de anuncio** de su `ANEXO-A-ficha-comercial.md`. Está escrita para eso.
2. **Qué entrega**, en tres o cuatro líneas.
3. **Qué NO hace.** Literal, de la sección `Límites` de la skill. No lo suavices: es lo que evita
   la devolución y la reseña mala.
4. **Requisitos técnicos**, si los hay (Python, export de rekordbox, etc.).
5. **Licencia**: uso comercial permitido, prohibida la redistribución.

## Lo que NO se pone en ningún texto de producto

- **Ninguna cifra sin su fuente.** Si citas el 5-9 % de ingresos por estrella, va con sus tres
  límites pegados: es Yelp, es EE. UU., y es ingresos, no margen. Si citas los umbrales de
  BrightLocal, van con `[CONTEXTO EE. UU.]`.
- **Ninguna promesa de resultado.** Ni "conseguirás más reseñas", ni "te firmarán el demo", ni
  "recuperarás tu cartera". Las tres son falsas y las tres son denunciables.
- **Ninguna mención a que la skill está "probada"** hasta que G2 esté levantado. Los casos de
  prueba son de fabricación y así está escrito en las fichas.

## Después de la primera venta

Anota en la ficha del comprador: qué compró, qué datos reales ejecutó y qué falló. **Eso es lo
que levanta G2**, y tres de esos cierran el gate en toda la línea.
