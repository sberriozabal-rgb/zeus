# postmortem-de-bolo

Skill de la línea **CABINA**, paquete **CABINA CORE** (Agent Skills, estándar abierto).

Convierte el export de historial de una sesión más lo que el DJ recuerda de la sala en un
parte de aprendizaje que separa los hechos verificables de las hipótesis, y cierra con un
máximo de tres decisiones comprobables para el próximo bolo.

## La regla que lo sostiene

Todo lo que aparece en el parte lleva su origen marcado:

| Caja | Origen |
|---|---|
| **HECHO** | Sale del fichero |
| **RELATO** | Lo dice el DJ |
| **HIPÓTESIS** | Cruce de ambos, marcado para contrastar |

El historial dice qué sonó y cuándo, con precisión de segundo. **No sabe si había gente.**
Confundir las dos cosas es el error que convierte un postmortem en una superstición.

## Uso

```bash
python3 scripts/historial.py <historial.csv>
python3 scripts/historial.py <historial.csv> --formato json
python3 scripts/historial.py <historial.csv> --corto 120 --largo 420
```

Exporta el historial desde rekordbox (pestaña Historial → botón derecho → exportar) o desde
Serato (History → Export, csv o txt). Cualquier CSV con `title,artist,start time` vale.

## Antes de leer el parte, responde a esto

1. ¿A qué hora se llenó y a qué hora se vació?
2. ¿Hubo algún momento en que notaras que la perdías?
3. ¿Qué track dio el mejor momento de la noche?
4. ¿Algo te sorprendió, para bien o para mal?
5. ¿Qué condiciones había? (aforo, sonido, hora, DJ anterior, clima)

Sin estas respuestas no hay postmortem: hay descripción. Guion completo en
`references/preguntas-de-sala.md`.

## Ficheros

- `SKILL.md` — la skill.
- `references/preguntas-de-sala.md` — guion de entrevista al DJ.
- `references/FUENTES.md` — fuentes y umbrales declarados.
- `scripts/historial.py` — extractor de hechos de la sesión.
- `assets/plantilla-parte.md` — plantilla del parte.
- `cases/` — los 4 casos de prueba.

## Licencia

Propietaria. Uso permitido al comprador; prohibida la redistribución. Ver `LICENSE.txt`.
