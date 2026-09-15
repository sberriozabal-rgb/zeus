# Fuentes externas — postmortem-de-bolo

## Software de origen del historial

rekordbox (AlphaTheta) — exportación desde la pestaña Historial.
<https://rekordbox.com/> · Consultado: 2026-09-15.

Serato — exportación desde History, botón Export (csv o txt).
<https://serato.com/> · Consultado: 2026-09-15.

## Precisión de la clave que viaja en el historial

La clave del historial es la que calculó el software del DJ, no una medición independiente.
Un test de laboratorio sobre 200 tracks dio 69% de acierto a rekordbox 7 frente a 89% de
Mixed In Key. Por eso un salto armónico detectado se trata como pregunta, no como sentencia.
<https://www.mixedinkey.com/> · Consultado: 2026-09-15.
**Límite:** muestra de 200 tracks, publicación del sector, sin contraste de hipótesis
publicado. Orden de magnitud, no cifra exacta.

## Umbrales sin fuente externa — criterio de oficio de la casa

`[A VALIDAR]` en los cuatro casos. No proceden de literatura ni de estudio publicado, y por
eso son configurables:

| Umbral | Valor por defecto | Parámetro |
|---|---|---|
| Track cortado pronto | < 120 s en el aire | `--corto` |
| Track sostenido | > 420 s en el aire | `--largo` |
| Salto de tempo relevante | >= 5 BPM | — |
| Salto armónico relevante | >= 3 pasos Camelot | — |

Un DJ de techno y uno de bodas no comparten estas fronteras. Se calibran con el histórico del
propio DJ en cuanto haya dos o tres sesiones registradas.

## Hueco de mercado declarado

La investigación de campo no localizó ninguna herramienta comercial que haga diagnóstico
posterior a la sesión. **No haber encontrado la herramienta no prueba que no exista**, y así
se declara en el producto. `[A VALIDAR — búsqueda no exhaustiva]`
