# Casos de prueba, auditoría, CHANGELOG y roadmap

## Casos de prueba (entrada real → salida esperada)

### happy_path
**Entrada:** «Compila la carpeta "Clínica Dental Norte" de mi Drive al proyecto.» 48
archivos (docx, pdf, xlsx, md), 9 chats en el proyecto.
**Salida:** CENSO (2 familias de versiones) → aprobación → extracción 47/48 (1 pdf
escaneado por OCR) → 9 chats → taxonomía derivada: Servicios y tarifas · Protocolos
clínicos · Pacientes (`[CONFIDENCIAL]`, anonimizado) · Proveedores · Marketing ·
Legal y licencias · Anexos → biblioteca + 3 resúmenes + inventario →
`Clinica_Dental_Norte_CONTEXTO_2026-08-26.zip` verificado → maestros al proyecto →
carpeta `CONTEXTO` en Drive junto a la original. Un solo `present_files`.

### edge_case
**Entrada:** una tesis doctoral con `Capitulo3_v7.docx` (2026-05-01) y
`Capitulo3_DIRECTOR_OK.docx` (2026-03-20) con conclusiones distintas; en un chat el
asistente propuso una tercera redacción.
**Salida:** prevalece la marcada por el director (aprobada gana a reciente no aprobada);
`[CONFLICTO]` con las tres versiones y fuentes; la del asistente como «propuesta de
Claude sin confirmar». Taxonomía derivada sin dominio «Economía» porque no hay material:
no se crea un dominio vacío.

### failure
**Entrada:** «Dame todo el proyecto en un zip.» Sin Drive, sin app, sin adjuntos, sin
nombre de proyecto; solo `/mnt/project` y herramientas de chat.
**Salida (se entrega igualmente):** una línea diciendo que no hay carpeta fuente y que no
recompila lo compilado; nombre de proyecto tomado del nombre del proyecto de Claude y
declarado; F2 + F4; ZIP con RESUMEN_CHATS, RESUMEN_CONTEXTO («biblioteca: sin cambios,
fuente no disponible»), INVENTARIO sobre `/mnt/project`; índice con
`[HUECO: carpeta fuente no accesible — abrir app, conectar Drive o subir ZIP]`.

### integration
**Entrada:** «Respalda este proyecto para pasarlo a otra cuenta.»
**Salida:** este ZIP es la entrada de `respaldo-proyecto-ia-cl` (`CHATS/chats.jsonl`
compatible con su `05-chats/chats.jsonl`). Cifrado, clasificación C0–C3 y prueba de
humo son de aquella; aquí no se cifra.

## Auditoría (rúbrica ZEUS, 20 puntos) — 17/20, ACORDADO

| Nivel | Punto | ✓ |
|---|---|---|
| 1 | ROL explícito | ✓ |
| 1 | Protocolo reproducible | ✓ |
| 1 | Entrada/salida sin interpretación | ✓ |
| 1 | Quién y cuándo | ✓ |
| 1 | Cero datos inventados | ✓ |
| 2 | SIEMPRE/NUNCA verificables | ✓ |
| 2 | Antipatrones con síntoma | ✓ |
| 2 | Matriz con «NO aplica» | ✓ |
| 2 | 4 casos | ✓ |
| 2 | Datos faltantes declarados | ✓ |
| 2 | ≤10 pasos (6 fases) | ✓ |
| 2 | Afirmaciones técnicas con fuente | ✓ (formato de export reconocido por estructura, no por nombre) |
| 2 | Traducible / sin sesgo de sector | ✓ |
| 3 | Debate abierto | ✗ (no aplica) |
| 3 | ≥3 referencias externas | ✗ |
| 3 | Escalabilidad 1→100 | ✓ (scripts) |
| 3 | Versionado + CHANGELOG | ✓ |
| 3 | Dependencias declaradas | ✓ |
| 3 | Roadmap v1.1 | ✓ |
| 3 | Empaquetado | ✓ |

Carencias: sin referencias externas; taxonomía derivada no probada en campo sobre más de
3 sectores; Ruta A limitada a ~100 chats.

## CHANGELOG
- 1.0.0 (2026-08-26) — Versión universal del compilador de contexto: nombre de
  proyecto paramétrico, taxonomía derivada del material, marcos alternativos genéricos,
  confidencialidad para cualquier tercero, sin sesgo de sector, país ni moneda.

## Roadmap v1.1
- Sugerencia automática de taxonomía por clustering de extracciones (script).
- Detector de credenciales y datos personales antes de empaquetar.
- Carga directa a Drive de la carpeta `CONTEXTO`.
