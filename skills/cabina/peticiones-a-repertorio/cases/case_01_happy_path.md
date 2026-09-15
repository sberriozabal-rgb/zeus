# Caso 1 · Happy path (lista de boda por WhatsApp)

## Entrada — pegada tal cual, sin limpiar

```
[21/03 22:14] Novia: hola!! te mando las canciones
[21/03 22:14] Novia: 1. perfect de ed sheeran (primer baile)
[21/03 22:15] Novia: 2. la de bizarrap con shakira
[21/03 22:15] Novia: 3. despacito
[21/03 22:16] Novia: 4. bailando de enrique iglesias
[21/03 22:17] Novia: ah y mi madre quiere paquito el chocolatero PERO NO LO PONGAS
[21/03 22:17] Novia: 5. la del anuncio del coche, la que suena ahora
[21/03 22:18] Novia: nada de reggaeton por favor que viene mi abuela
[21/03 22:19] Novia: mañana te llamo para hablar de la ceremonia
...
```

28 líneas útiles en total. Biblioteca: `collection.xml` con 8.412 tracks.

## Ejecución

```bash
python3 scripts/cruzar.py collection.xml peticiones.txt --formato texto
```

## Salida esperada

```
CRUCE DE PETICIONES — Boda, 14-jun
Peticiones detectadas: 28   Biblioteca: 8.412 tracks

TENGO (19)
  Ed Sheeran - Perfect                          0.98   [MOMENTO: primer baile]
  Enrique Iglesias - Bailando                   0.95
  ...

NO TENGO (5)
  Bizarrap, Shakira - Music Sessions #53        (ver DUDOSO)
  ...

DUDOSO (3)
  "la de bizarrap con shakira"     -> BZRP Music Sessions #53      0.71
  "despacito"                      -> 2 versiones: original / ft. Bieber
  "la del anuncio del coche"       -> sin candidato fiable         0.41

PROHIBIDO (2)
  Paquito el Chocolatero
  Reggaeton (genero completo)

APARTADAS (4 lineas que parecen conversacion) — REVISAR A MANO
  "hola!! te mando las canciones"
  "mañana te llamo para hablar de la ceremonia"
  ...
```

## Revisión del cubo DUDOSO (paso 3)

- **"la de bizarrap con shakira"** → propuesta: *BZRP Music Sessions #53*. Es la colaboración
  con Shakira y no hay otra. Sube al cliente para confirmar porque 0.71 está por debajo de
  0.86.
- **"despacito"** → hay dos versiones en biblioteca. Contexto: boda con abuela presente y
  familia. Propuesta: **la original**, no la de Bieber. Sube al cliente.
- **"la del anuncio del coche"** → 0.41, sin candidato fiable. **No se propone nada**: se
  pregunta de qué anuncio habla.

## Documento de confirmación enviado al cliente

```markdown
## Confirmado — sonará seguro
Perfect (Ed Sheeran) para el primer baile, Bailando, [...19 títulos...]

## Necesito que me confirmes
- "La de Bizarrap con Shakira": ¿te refieres a la Session #53? Es la que hizo con ella.
- "Despacito": ¿la original o la versión con Justin Bieber? Tengo las dos.
- "La del anuncio del coche": no doy con ella. ¿Sabes la marca o alguna palabra de la letra?

## Anotado como no poner
- Paquito el Chocolatero
- Reggaetón
```

## Lista de compra (paso 4), por criticidad

| # | Track | Prioridad | Motivo |
|---|---|---|---|
| 1 | BZRP Music Sessions #53 | **Crítica** | Petición explícita, pendiente de confirmar |
| 2 | [track 2] | Alta | Petición repetida |
| 3-5 | [relleno] | Baja | Ambiente; solo si sobra presupuesto |

Formato mínimo: **320 kbps o WAV** — los CDJ no leen todos los formatos.

## Por qué es el caso central

Las tres cosas que aporta la skill están aquí: la abuela no oirá reggaetón y consta por
escrito, la Dirty de Despacito no va a sonar por accidente, y la línea "mañana te llamo" no se
ha confundido con una petición.
