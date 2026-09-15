# set-por-encargo

Skill de la línea **CABINA**, paquete **CABINA CORE** (Agent Skills, estándar abierto).

Ordena un set a partir del pool real del DJ **y del brief del bolo** —slot, hora, duración,
público, prohibiciones del cliente, BPM de entrada y de relevo—, no solo de la armonía.

## Por qué no es un ordenador armónico

Ordenar por Camelot y BPM lo hacen DJ.Studio ("Harmonize") y Mixed In Key Pro ("DJ Mix Mode")
con un clic, mejor y más barato. **Si eso es todo lo que necesitas, usa esas herramientas.**

Esta skill sirve cuando el criterio es contextual: que eres el telonero y el cabeza de cartel
abre a 128, que los novios han prohibido reggaetón, que el primer baile va en un momento fijo,
o que te acaban de cambiar el slot de 90 a 50 minutos a una hora de entrar.

## Uso

```bash
python3 scripts/setbuilder.py <pool> -n <tracks> -c <curva> \
  --energia-min <n> --energia-max <n> \
  [--apertura "texto"] [--incluir "track"] [--vetar "artista o track"]
```

Salidas: `--formato texto` (por defecto, con notas de transición), `--formato m3u`
(importable), `--formato json`.

## Las seis curvas

| Franja | Curva | Energía |
|---|---|---|
| Calentamiento / telonero | `rampa` | 3 → 7 |
| Peak time | `meseta` | 6 → 9 |
| Set completo de noche | `arco` | 3 → 9 (pico al 70%) |
| Cierre / closing | `descenso` | 8 → 4 |
| After | `descenso` | 6 → 3 |
| Sesión larga con oleadas | `dientes` | 4 → 9 |

## La regla de relevo

Si hay DJ después, los últimos tracks aterrizan **entre 4 y 8 BPM por debajo** de su BPM de
apertura. Si abre a 128, cierras entre 120 y 124. **Verifícalo a mano:** el motor no conoce al
DJ siguiente.

## Aviso que viaja con el producto

Esta skill **no oye**. Lee clave, BPM y energía del export; no los detecta. Un test sobre 200
tracks dio 69% de acierto de clave a rekordbox 7 frente a 89% de Mixed In Key
([fuente](https://blog.dubspot.com/dubspot-lab-report-mixed-in-key-vs-beatport)): alrededor de
un tercio de las claves pueden estar mal y desde aquí no hay forma de detectarlo. Las
transiciones armónicas son propuesta, no garantía.

## Licencia

Propietaria. Uso permitido al comprador; prohibida la redistribución. Ver `LICENSE.txt`.
