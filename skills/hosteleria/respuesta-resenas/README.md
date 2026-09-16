# respuesta-resenas

Skill de FORJA (Agent Skills, estándar abierto). Convierte un export de reseñas de Google o TripAdvisor en dos cosas dentro del mismo informe: las respuestas listas para publicar —una por reseña, con el tono y la estructura de cada categoría— y el **patrón operativo**, que es lo que de verdad vale: si el mismo problema aparece tres o más veces en sesenta días, eso ya no es un cliente difícil, es algo que el dueño puede arreglar el lunes.

## Instalación

Copia esta carpeta completa (o el archivo `.skill` empaquetado) en el directorio de skills del agente que la va a ejecutar, o desde el paquete entregado en la instalación contratada.

## Estructura

```
respuesta-resenas/
├── SKILL.md                       — método, categorías, umbral de patrón, formato de informe
├── README.md                      — este archivo
├── metadata.json                  — metadatos de empaque
├── CHANGELOG.md                   — historial de versiones
├── LICENSE.txt                    — licencia de uso comercial
├── ANEXO-A-ficha-comercial.md     — a quién se vende y a qué precio
├── references/
│   ├── FUENTES.md                 — cada cifra con URL y límite de uso, y la política de
│   │                                Google, Tripadvisor y la ley española sobre incentivar reseñas
│   └── umbrales-resenas.md        — impacto de las estrellas, umbral de patrón, señales de alarma
├── assets/
│   └── plantillas-respuestas.md   — 5 estructuras de respuesta por categoría
├── scripts/
│   └── resenas.py                 — motor determinista, con --ejemplo y --autotest
└── cases/
    ├── case_01_happy_path.md
    ├── case_02_edge_case.md
    ├── case_03_failure.md
    └── case_04_integration.md
```

## Uso

```bash
python3 scripts/resenas.py --ejemplo      # formato de entrada
python3 scripts/resenas.py datos.json     # análisis completo
python3 scripts/resenas.py --autotest     # comprobación aritmética
```

## Verificar antes de entregar a un cliente

```bash
python3 scripts/resenas.py --autotest
```

Debe imprimir **"AUTOTEST OK — 6 comprobaciones aritméticas pasadas"**. Si no, no se entrega.

La comprobación del patrón es la que sostiene el producto: verifica que tres menciones del mismo motivo separadas por más de un mes entran igualmente en la ventana de 60 días, y que un motivo con una sola mención **no** se marca como patrón. Un informe que llame patrón a una queja suelta manda al dueño a rehacer un turno que funciona.

## La línea que esta skill no cruza, y por qué está escrita

El apartado 5 del informe recomienda **cómo pedir reseñas**. Pedirlas está permitido; premiarlas o filtrar quién las deja, no. No es una opinión de la casa: Google prohíbe expresamente ofrecer *"payment, discounts, free goods and/or services"* a cambio de una reseña y *"selectively solicit positive reviews from customers"*; Tripadvisor prohíbe *"offer or promise anything in exchange for any reviews, irrespective of rating"*, incluido premiar al camarero por reseñas conseguidas; y en España el filtrado de reseñas cae en el artículo 27.8 de la Ley de Competencia Desleal, con régimen sancionador propio. Las citas literales y las URL están en `references/FUENTES.md` §3, §4 y §5. **Esto no es asesoría legal**, y así se dice también en el informe.

## Lo que esta skill NO hace

No publica ninguna respuesta: entrega el texto para que lo revise y lo publique el dueño. No gestiona la eliminación de reseñas falsas ante la plataforma (Google y TripAdvisor tienen su propio proceso de disputa). No es asesoría legal ante difamación. Y no promete ninguna cifra de ingresos: el rango de +5% a +9% por estrella se presenta siempre como escenario de referencia con su fuente, nunca como resultado. Ver la sección "Límites" de `SKILL.md`.

## Nota de auditoría

La v1.2.0 (15-sep-2026) reestructuró la skill con las cuatro piezas del ADN de la línea que le
faltaban en la v1.1: procedimiento en pasos atómicos con la rama "si falta el dato", tabla de
reglas SIEMPRE, tabla NUNCA y antipatrones. `metadata.json` y `ANEXO-A-ficha-comercial.md`
declaran la misma nota, **19/20** (`validar_skill.py`, 15-sep-2026; el validador da 20/20
mecánico y no se firma el 20 porque el punto 19 exige URLs reverificadas una a una). La
afirmación de que Google y TripAdvisor penalizan las respuestas idénticas se retiró: no se
sostenía al verificarla, y `references/FUENTES.md` §6 documenta la corrección.

## Soporte

Pieza 4 de 7 del sistema instalable de hostelería (Motor B). No se vende suelta salvo decisión explícita de Sergio.
