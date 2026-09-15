#!/usr/bin/env python3
"""
historial — lee el export de historial de una sesion y saca los hechos.

El historial de rekordbox/Serato dice QUE sono y CUANDO. De ahi se deducen
hechos que el DJ no recuerda con precision: cuanto duro cada track en el aire,
donde se acelero o se freno, que artistas se repitieron, que saltos de tempo
o de clave hubo y en que momento.

Lo que este script NO hace: decir si el set fue bueno. Eso depende de la sala,
y la sala no esta en el fichero. El script produce los hechos; el criterio lo
pone quien estuvo alli.

Entrada: CSV/TSV de historial con al menos titulo y hora.
         Opcional: artista, bpm, key, deck.
"""

from __future__ import annotations

import os
import re
import sys
from collections import Counter
from typing import Dict, List, Optional, Sequence

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dj_toolkit import (  # noqa: E402
    CAMELOT_TO_NAME, key_distance, normalize_key, read_history_csv,
)

__version__ = "1.0.0"

_HORA = re.compile(r"(\d{1,2})[:h](\d{2})(?:[:.](\d{2}))?")


def _segundos(valor: str) -> Optional[int]:
    """Convierte '23:14:02' o '2026-08-11 23:14' en segundos desde medianoche."""
    if not valor:
        return None
    m = _HORA.search(str(valor))
    if not m:
        return None
    h, mi = int(m.group(1)), int(m.group(2))
    s = int(m.group(3) or 0)
    if h > 23 or mi > 59 or s > 59:
        return None
    return h * 3600 + mi * 60 + s


def _mmss(seg: Optional[float]) -> str:
    if seg is None:
        return "?"
    seg = int(seg)
    return f"{seg // 60}:{seg % 60:02d}"


def analizar(filas: Sequence[Dict[str, str]],
             umbral_corto: int = 150,
             umbral_largo: int = 480) -> Dict[str, object]:
    """Extrae los hechos de una sesion. No juzga: describe."""
    tracks: List[Dict[str, object]] = []
    for f in filas:
        t: Dict[str, object] = {
            "titulo": f.get("titulo", ""),
            "artista": f.get("artista", ""),
            "hora_texto": f.get("hora", ""),
            "hora_s": _segundos(f.get("hora", "")),
            "camelot": normalize_key(f.get("key", "")),
            "deck": f.get("deck", ""),
        }
        try:
            t["bpm"] = float(str(f.get("bpm", "")).replace(",", ".")) or None
        except ValueError:
            t["bpm"] = None
        tracks.append(t)

    # Duracion en el aire = diferencia con la hora del siguiente
    saltos_medianoche = 0
    for i, t in enumerate(tracks[:-1]):
        a, b = t["hora_s"], tracks[i + 1]["hora_s"]
        if a is None or b is None:
            t["aire_s"] = None
            continue
        d = b - a
        if d < 0:  # cruce de medianoche
            d += 86400
            saltos_medianoche += 1
        t["aire_s"] = d if 0 < d < 3600 else None
    if tracks:
        tracks[-1]["aire_s"] = None  # del ultimo no se sabe cuanto sono

    aires = [t["aire_s"] for t in tracks if t.get("aire_s")]
    media = sum(aires) / len(aires) if aires else None

    # Hechos observables
    cortos = [t for t in tracks if t.get("aire_s") and t["aire_s"] < umbral_corto]
    largos = [t for t in tracks if t.get("aire_s") and t["aire_s"] > umbral_largo]

    saltos_bpm, saltos_clave = [], []
    for i in range(len(tracks) - 1):
        a, b = tracks[i], tracks[i + 1]
        if a.get("bpm") and b.get("bpm"):
            delta = b["bpm"] - a["bpm"]
            if abs(delta) >= 5:
                saltos_bpm.append({
                    "posicion": i + 1, "de": a["titulo"], "a": b["titulo"],
                    "bpm_de": a["bpm"], "bpm_a": b["bpm"],
                    "delta": round(delta, 1), "hora": a["hora_texto"],
                })
        if a.get("camelot") and b.get("camelot"):
            d = key_distance(str(a["camelot"]), str(b["camelot"]))
            if d is not None and d >= 3:
                saltos_clave.append({
                    "posicion": i + 1, "de": a["titulo"], "a": b["titulo"],
                    "clave_de": a["camelot"], "clave_a": b["camelot"],
                    "pasos": d, "hora": a["hora_texto"],
                })

    artistas = Counter(str(t["artista"]).strip() for t in tracks
                       if str(t.get("artista") or "").strip())
    repetidos = {a: n for a, n in artistas.items() if n > 1}

    # Repeticiones del mismo track
    claves_track = Counter(
        f"{str(t.get('artista','')).strip().lower()}|{str(t.get('titulo','')).strip().lower()}"
        for t in tracks if str(t.get("titulo") or "").strip())
    track_repetido = {k: n for k, n in claves_track.items() if n > 1}

    horas = [t["hora_s"] for t in tracks if t.get("hora_s") is not None]
    duracion_total = None
    if len(horas) >= 2:
        duracion_total = horas[-1] - horas[0]
        if duracion_total < 0:
            duracion_total += 86400

    # Curva de BPM por tramos de 15 min
    tramos: Dict[int, List[float]] = {}
    if horas:
        t0 = horas[0]
        for t in tracks:
            if t.get("hora_s") is None or not t.get("bpm"):
                continue
            rel = t["hora_s"] - t0
            if rel < 0:
                rel += 86400
            tramos.setdefault(rel // 900, []).append(float(t["bpm"]))
    curva = [{"tramo_min": k * 15,
              "bpm_medio": round(sum(v) / len(v), 1),
              "tracks": len(v)}
             for k, v in sorted(tramos.items())]

    return {
        "tracks": tracks,
        "resumen": {
            "total_tracks": len(tracks),
            "duracion_total_s": duracion_total,
            "aire_medio_s": round(media) if media else None,
            "tracks_con_hora": len(horas),
            "tracks_con_bpm": sum(1 for t in tracks if t.get("bpm")),
            "tracks_con_clave": sum(1 for t in tracks if t.get("camelot")),
            "cruces_de_medianoche": saltos_medianoche,
        },
        "cortos": cortos,
        "largos": largos,
        "saltos_bpm": saltos_bpm,
        "saltos_clave": saltos_clave,
        "artistas_repetidos": repetidos,
        "tracks_repetidos": track_repetido,
        "curva_bpm": curva,
        "umbrales": {"corto_s": umbral_corto, "largo_s": umbral_largo},
    }


def render(r: Dict[str, object]) -> str:
    s = r["resumen"]
    L: List[str] = []
    L.append("HECHOS DE LA SESION")
    L.append(f"  {s['total_tracks']} tracks · duracion {_mmss(s['duracion_total_s'])}"
             f" · tiempo medio en el aire {_mmss(s['aire_medio_s'])}")
    L.append(f"  con hora: {s['tracks_con_hora']} · con BPM: {s['tracks_con_bpm']}"
             f" · con clave: {s['tracks_con_clave']}")
    if s["cruces_de_medianoche"]:
        L.append(f"  (se detectaron {s['cruces_de_medianoche']} cruces de medianoche)")

    if r["curva_bpm"]:
        L.append("")
        L.append("CURVA DE TEMPO (media por tramos de 15 min)")
        pico = max(x["bpm_medio"] for x in r["curva_bpm"])
        for c in r["curva_bpm"]:
            barra = "#" * max(1, int((c["bpm_medio"] / pico) * 34))
            L.append(f"  min {c['tramo_min']:>3}  {c['bpm_medio']:6.1f}  {barra}")

    L.append("")
    L.append(f"CORTADOS PRONTO — menos de {r['umbrales']['corto_s']}s en el aire "
             f"({len(r['cortos'])})")
    L.append("  Un track cortado pronto suele significar que no funciono, o que")
    L.append("  entro para tapar un hueco. Solo el DJ sabe cual de las dos.")
    for t in r["cortos"]:
        L.append(f"  · [{t['hora_texto']}] {t['artista']} — {t['titulo']}"
                 f"   ({_mmss(t['aire_s'])})")

    L.append("")
    L.append(f"SOSTENIDOS — mas de {r['umbrales']['largo_s']}s en el aire "
             f"({len(r['largos'])})")
    for t in r["largos"]:
        L.append(f"  · [{t['hora_texto']}] {t['artista']} — {t['titulo']}"
                 f"   ({_mmss(t['aire_s'])})")

    L.append("")
    L.append(f"SALTOS DE TEMPO de 5 BPM o mas ({len(r['saltos_bpm'])})")
    for x in r["saltos_bpm"]:
        L.append(f"  · [{x['hora']}] {x['bpm_de']:g} -> {x['bpm_a']:g} "
                 f"({x['delta']:+g})  {x['de']} -> {x['a']}")

    L.append("")
    L.append(f"SALTOS ARMONICOS de 3 pasos o mas ({len(r['saltos_clave'])})")
    for x in r["saltos_clave"]:
        L.append(f"  · [{x['hora']}] {x['clave_de']} -> {x['clave_a']} "
                 f"({x['pasos']} pasos)  {x['de']} -> {x['a']}")

    if r["artistas_repetidos"]:
        L.append("")
        L.append("ARTISTAS REPETIDOS")
        for a, n in sorted(r["artistas_repetidos"].items(), key=lambda x: -x[1]):
            L.append(f"  · {a}: {n} veces")

    if r["tracks_repetidos"]:
        L.append("")
        L.append("TRACKS REPETIDOS EN LA MISMA SESION")
        for k, n in r["tracks_repetidos"].items():
            L.append(f"  · {k.replace('|', ' — ')}: {n} veces")

    L.append("")
    L.append("LIMITE DE ESTE INFORME")
    L.append("  Esto son hechos, no conclusiones. El fichero no sabe si la pista")
    L.append("  estaba llena ni por que se vacio. Cruza estos hechos con lo que")
    L.append("  recuerdes de la sala antes de sacar ninguna leccion.")
    return "\n".join(L)


def _cli() -> int:
    import argparse
    import json
    p = argparse.ArgumentParser(description="analiza el historial de una sesion")
    p.add_argument("historial", help="CSV/TSV exportado de rekordbox o Serato")
    p.add_argument("--formato", choices=["texto", "json"], default="texto")
    p.add_argument("--corto", type=int, default=150)
    p.add_argument("--largo", type=int, default=480)
    a = p.parse_args()

    filas = read_history_csv(a.historial)
    if not filas:
        print("Historial vacio o ilegible.", file=sys.stderr)
        return 1
    r = analizar(filas, a.corto, a.largo)
    print(json.dumps(r, ensure_ascii=False, indent=2, default=str)
          if a.formato == "json" else render(r))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
