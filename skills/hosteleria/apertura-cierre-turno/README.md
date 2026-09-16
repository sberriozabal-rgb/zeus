# apertura-cierre-turno

Skill de FORJA (Agent Skills, estándar abierto). Genera checklists de apertura, cambio de turno y cierre para un local de hostelería, con responsable por puesto, criterio de "hecho" verificable y parte de incidencias.

## Instalación

Copia esta carpeta completa (o el archivo `.skill` empaquetado) en el directorio de skills del agente que la va a ejecutar, o instálala como plugin desde el marketplace público `sberriozabal-rgb/octava-skills` (plugin `octava-abiertas`).

## Estructura

```
apertura-cierre-turno/
├── SKILL.md                       — método completo, reglas, casos
├── README.md                      — este archivo
├── metadata.json                  — metadatos de empaque
├── CHANGELOG.md                   — historial de versiones
├── LICENSE.txt                    — licencia de uso comercial
├── ANEXO-A-ficha-comercial.md     — a quién se vende y a qué precio
├── references/
│   ├── FUENTES.md                 — fuentes externas verificadas y qué afirmación sostiene cada una
│   ├── plantillas-por-tipo.md     — 5 plantillas base por tipo de local
│   └── tareas-maestras.md         — tareas maestras con criterio de hecho
├── assets/
│   ├── plantilla-checklist.md     — plantilla en blanco para imprimir
│   └── plantilla-parte-incidencias.md
├── scripts/
│   └── coste_rotacion.py          — calculadora determinista, con --autotest
└── cases/
    ├── case_01_happy_path.md
    ├── case_02_edge_case.md
    ├── case_03_failure.md
    └── case_04_integration.md
```

## Verificar antes de entregar a un cliente

```bash
python3 scripts/coste_rotacion.py --autotest
```

Debe devolver "TODO EN VERDE". Si no, no se entrega.

Y la comprobación de versión, que en la 1.1.0 se saltó y produjo un cliente sin
forma de saber qué tenía instalado. Las cinco declaraciones deben dar el mismo
número:

```bash
grep -n "version" SKILL.md metadata.json | head
grep -n "v1\." LICENSE.txt ANEXO-A-ficha-comercial.md
```

Frontmatter `metadata.version` · pie de `SKILL.md` · `metadata.json` ·
cabecera de `LICENSE.txt` · `Estado / Versión` del Anexo A. Si divergen, no se
empaqueta.

## Soporte

Parte del sistema instalable de 7 skills de hostelería (Motor B). No se vende suelta salvo decisión explícita de Sergio.
