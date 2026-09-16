# reporte-inteligencia-competencia

Skill de la línea **Hostelería** (Agent Skills, estándar abierto). Es la **vertical de
restauración** de `reporte-inteligencia`.

Reporte semanal de **una página**: cómo va un restaurante frente a seis competidores nombrados,
qué hacen ellos que la marca no, y tres acciones para esta semana con responsable y día.

## Los cuatro cortes de decisión

| Métrica | 🟢 | 🟡 | 🔴 | Cifra que lo sostiene |
|---|---|---|---|---|
| Calificación | ≥ 4,5★ | 4,0–4,4★ | < 4,0★ | 31 % solo usa negocios de 4,5★+ |
| Volumen | ≥ 100 | 20–99 | < 20 | 47 % evita negocios con < 20 reseñas |
| Recencia | ≤ 7 d | 8–14 d | > 14 d | 32 % solo se fía de reseñas de 2 semanas |
| Tasa de respuesta | 100 % | 50–99 % | < 50 % | > 80 % cree que hay que responder a todas |

**La diana no es 5,0.** Solo el 10 % exige cinco estrellas y un 5,0 clavado se lee como falso.
El objetivo es **4,5–4,8**.

## Las dos reglas que evitan el reporte inútil

1. **Mediana, nunca media.** Un competidor con 5,0 y 6 reseñas dispara una falsa alarma en cuanto
   entra en una media.
2. **Si dos fuentes divergen, se reportan las dos.** La divergencia **es** el hallazgo: casi
   siempre significa una plataforma abandonada.

## Cobertura mínima

Tres plataformas, no solo Google. El consumidor consulta **seis fuentes de media**, Google ha
caído del 83 % al 71 % como plataforma de descubrimiento, y los asistentes de IA ya pesan un 45 %.

## Límites

Solo fuentes públicas. **No responde reseñas** — eso es `respuesta-resenas`. No es *due
diligence* ni asesoría legal o financiera. Los umbrales de comportamiento vienen de paneles de
consumidores de EE. UU. y van marcados `[CONTEXTO EE. UU. — A VALIDAR ES/MX]`: **no se usan como
promesa de venta sin esa etiqueta**.

Si un competidor está bajo relación contractual o personal con el cliente, **se detiene esa ficha
y se avisa**.

## Ficheros

- `references/FUENTES.md` — las tres ediciones de BrightLocal y qué corte sostiene cada cifra.
- `cases/` — los 4 casos de prueba.
- `ANEXO-A-ficha-comercial.md` — comprador, precio, canal y gates.

## Licencia

Propietaria. Copyright 2026 Sergio Berriozábal Serrano. Prohibida la redistribución del artefacto. Ver `LICENSE.txt`.
