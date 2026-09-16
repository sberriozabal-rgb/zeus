# receta-estandar

Skill de FORJA (Agent Skills, estándar abierto). Convierte la forma de cocinar un plato que hoy solo vive en la cabeza de un cocinero —o en notas sueltas, fotos y audios de WhatsApp— en una ficha ejecutable por cualquier cocinero del turno: gramaje exacto, procedimiento en pasos numerados con señal de terminado, puntos críticos de control con el binomio tiempo-temperatura de la norma del país, y criterio de emplatado verificable.

## Instalación

Copia esta carpeta completa (o el archivo `.skill` empaquetado) en el directorio de skills del agente que la va a ejecutar, o desde el paquete entregado en la instalación contratada.

Requiere Python 3.9+ solo para el script de escalado. El uso base no necesita nada.

## Estructura

```
receta-estandar/
├── SKILL.md                       — método completo, umbrales, reglas, antipatrones
├── README.md                      — este archivo
├── metadata.json                  — metadatos de empaque
├── CHANGELOG.md                   — historial de versiones
├── LICENSE.txt                    — licencia de uso comercial
├── ANEXO-A-ficha-comercial.md     — a quién se vende y a qué precio
├── references/
│   ├── temperaturas_haccp.md      — tabla A España (AESAN) y tabla B México (NOM-251), y dónde discrepan
│   ├── equivalencias_cocina.md    — unidad casera a gramaje, declarado como práctica no normada
│   └── FUENTES.md                 — cada cifra con URL, apartado y qué afirmación sostiene
├── scripts/
│   └── escalar_receta.py          — escala gramajes sin tocar tiempos ni temperaturas
└── cases/
    ├── case_01_happy_path.md
    ├── case_02_edge_case.md
    ├── case_03_failure.md
    └── case_04_integration.md
```

## Uso

```bash
python3 scripts/escalar_receta.py --ejemplo                          # formato del contrato JSON
python3 scripts/escalar_receta.py --json receta.json --porciones 50  # escalar a 50 porciones
python3 scripts/escalar_receta.py --json receta.json --factor 12.5   # escalar por factor directo
```

## Verificar antes de entregar a un cliente

```bash
python3 scripts/escalar_receta.py --ejemplo
```

Debe imprimir la receta original, su escalado a 50 porciones y, al pie del JSON escalado, el campo `_aviso_escalado`. Si ese aviso no aparece, no se entrega: el script estaría multiplicando cantidades sin advertir que tiempos, temperaturas y ratios de reducción **no** se han escalado, que es el antipatrón nº 3 de la skill.

El escalado devuelve siempre la ficha a `estado: BORRADOR` a propósito. Una ficha escalada es una hipótesis hasta que alguien la cocina y la pesa.

## Lo que decide todo: el país de operación

Las temperaturas de España y de México **no coinciden**. Pescado en trozo son 68 °C durante 15 s en España (AESAN-2021-004) y 63 °C en México (NOM-251 §7.3.1). Mantenimiento en caliente, ≥63 °C frente a >60 °C. Una ficha sin país declarado no pasa de BORRADOR, y una ficha que viaja de un país al otro se **reescribe**, no se copia. Ninguna de las dos tablas se promedia ni se mezcla.

Para cualquier otro mercado, y para caza, curados, fermentados, conservas y sous-vide —que no están en ninguna de las dos tablas—, la cifra sale marcada `[A VALIDAR — CONSULTAR AUTORIDAD SANITARIA LOCAL]`. No se extrapola por analogía.

## Lo que esta skill NO hace

**No es un plan APPCC.** Una ficha de receta estándar no crea, aplica ni mantiene el procedimiento permanente basado en los principios del APPCC que el artículo 5 del Reglamento (CE) 852/2004 exige al titular del negocio alimentario, y en México no sustituye el cumplimiento de la NOM-251-SSA1-2009. Marcar puntos críticos en una receta es una buena práctica de higiene documentada, no el sistema de autocontrol que la ley obliga a tener, y no incluye la identificación de peligros ni la certificación por quien corresponda. Se declara en cada entrega, no en una nota al pie.

Tampoco calcula coste ni escandallo (eso es `escandallo-ingenieria-menu` con la estructura real del negocio), no valida binomios de sous-vide, curados, fermentados, conservas ni caza, no sustituye el pesaje —una ficha no pesada nunca pasa de BORRADOR—, y no decide alérgenos ni etiquetado: marca dónde hay manejo de alérgenos como punto de atención y la declaración legal va a asesoría.

## Soporte

Parte del sistema instalable de skills de hostelería (Motor B). No se vende suelta salvo decisión explícita de Sergio. Ver `ANEXO-A-ficha-comercial.md`.
