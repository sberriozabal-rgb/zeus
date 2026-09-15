#!/usr/bin/env python3
"""
dj_toolkit — nucleo tecnico compartido de la linea CABINA.

Sin dependencias externas: solo biblioteca estandar de Python 3.8+.

Cubre:
  · Normalizacion de clave musical  -> Camelot canonico
  · Reglas de compatibilidad armonica (rueda Camelot)
  · Lectura de rekordbox collection XML
  · Lectura de M3U/M3U8 y CSV genericos de historial
  · Auditoria de biblioteca (huecos, duplicados, rutas rotas)

Fuentes de la tabla Camelot/Open Key (verificadas 2026-08-11):
  https://neume.io/camelot-wheel
  https://vibesdj.io/dj-tools/harmonic-mixing-chart
"""

from __future__ import annotations

import csv
import os
import re
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import unquote, urlparse

__version__ = "1.0.0"

# --------------------------------------------------------------------------
# 1 · TABLA CANONICA DE CLAVES
# --------------------------------------------------------------------------
# (camelot, open_key, nombre canonico, alias aceptados)
_KEY_TABLE: List[Tuple[str, str, str, Tuple[str, ...]]] = [
    ("1A", "6m", "Ab minor", ("abm", "g#m", "gsharpm", "abmin", "g#min")),
    ("1B", "6d", "B major", ("b", "bmaj", "bmajor")),
    ("2A", "7m", "Eb minor", ("ebm", "d#m", "dsharpm", "ebmin", "d#min")),
    ("2B", "7d", "F# major", ("f#", "gb", "f#maj", "gbmaj", "fsharp")),
    ("3A", "8m", "Bb minor", ("bbm", "a#m", "asharpm", "bbmin", "a#min")),
    ("3B", "8d", "Db major", ("db", "c#", "dbmaj", "c#maj", "csharp")),
    ("4A", "9m", "F minor", ("fm", "fmin")),
    ("4B", "9d", "Ab major", ("ab", "g#", "abmaj", "g#maj")),
    ("5A", "10m", "C minor", ("cm", "cmin")),
    ("5B", "10d", "Eb major", ("eb", "d#", "ebmaj", "d#maj")),
    ("6A", "11m", "G minor", ("gm", "gmin")),
    ("6B", "11d", "Bb major", ("bb", "a#", "bbmaj", "a#maj")),
    ("7A", "12m", "D minor", ("dm", "dmin")),
    ("7B", "12d", "F major", ("f", "fmaj")),
    ("8A", "1m", "A minor", ("am", "amin")),
    ("8B", "1d", "C major", ("c", "cmaj")),
    ("9A", "2m", "E minor", ("em", "emin")),
    ("9B", "2d", "G major", ("g", "gmaj")),
    ("10A", "3m", "B minor", ("bm", "bmin")),
    ("10B", "3d", "D major", ("d", "dmaj")),
    ("11A", "4m", "F# minor", ("f#m", "gbm", "fsharpm", "f#min", "gbmin")),
    ("11B", "4d", "A major", ("a", "amaj")),
    ("12A", "5m", "Db minor", ("dbm", "c#m", "csharpm", "dbmin", "c#min")),
    ("12B", "5d", "E major", ("e", "emaj")),
]

CAMELOT_TO_NAME: Dict[str, str] = {r[0]: r[2] for r in _KEY_TABLE}
CAMELOT_TO_OPENKEY: Dict[str, str] = {r[0]: r[1] for r in _KEY_TABLE}
OPENKEY_TO_CAMELOT: Dict[str, str] = {r[1]: r[0] for r in _KEY_TABLE}

_ALIAS_TO_CAMELOT: Dict[str, str] = {}
for _cam, _ok, _name, _aliases in _KEY_TABLE:
    _ALIAS_TO_CAMELOT[_cam.lower()] = _cam
    _ALIAS_TO_CAMELOT[_ok.lower()] = _cam
    _ALIAS_TO_CAMELOT[_name.lower().replace(" ", "")] = _cam
    for _a in _aliases:
        _ALIAS_TO_CAMELOT[_a] = _cam

# Normalizaciones ortograficas frecuentes en tags ID3 reales
_KEY_CLEANUP = [
    (re.compile(r"[♯]"), "#"),          # ♯
    (re.compile(r"[♭]"), "b"),          # ♭
    (re.compile(r"\bmajor\b|\bmaj\b"), ""),
    (re.compile(r"\bminor\b|\bmin\b"), "m"),
    (re.compile(r"[\s\-_/\.]+"), ""),
]


def normalize_key(raw: Optional[str]) -> Optional[str]:
    """Devuelve el codigo Camelot canonico o None si no se puede resolver.

    Acepta Camelot ('8A', '8a'), Open Key ('1m'), nombre ('A minor',
    'Am', 'Abm', 'G#m', 'F# major'). Devuelve None ante cadena vacia o
    valor irreconocible: NUNCA adivina.
    """
    if raw is None:
        return None
    s = unicodedata.normalize("NFKC", str(raw)).strip()
    if not s:
        return None

    # Camelot directo, tolerando '08A'
    m = re.fullmatch(r"0?(\d{1,2})\s*([ABab])", s)
    if m and 1 <= int(m.group(1)) <= 12:
        return f"{int(m.group(1))}{m.group(2).upper()}"

    # Open Key directo
    m = re.fullmatch(r"0?(\d{1,2})\s*([mdMD])", s)
    if m and 1 <= int(m.group(1)) <= 12:
        return OPENKEY_TO_CAMELOT.get(f"{int(m.group(1))}{m.group(2).lower()}")

    t = s.lower()
    for pattern, repl in _KEY_CLEANUP:
        t = pattern.sub(repl, t)
    return _ALIAS_TO_CAMELOT.get(t)


def _split_camelot(camelot: str) -> Tuple[int, str]:
    m = re.fullmatch(r"(\d{1,2})([AB])", camelot.upper())
    if not m:
        raise ValueError(f"Camelot invalido: {camelot!r}")
    return int(m.group(1)), m.group(2)


def _wrap(n: int) -> int:
    return ((n - 1) % 12) + 1


def compatible_keys(camelot: str, include_advanced: bool = False) -> List[Dict[str, str]]:
    """Movimientos armonicos desde una clave Camelot.

    Los tres movimientos base son los documentados por la rueda Camelot:
    misma clave, +/-1 misma letra, mismo numero cambiando letra.
    Con include_advanced=True se anaden dos movimientos que la literatura
    de DJ describe como validos pero mas audibles: +7 (dominante) y +/-2.
    """
    n, letra = _split_camelot(camelot)
    otra = "B" if letra == "A" else "A"
    movimientos = [
        {"camelot": f"{n}{letra}", "movimiento": "misma clave",
         "efecto": "energia plana, mezcla invisible", "riesgo": "bajo"},
        {"camelot": f"{_wrap(n + 1)}{letra}", "movimiento": "+1 misma letra",
         "efecto": "sube energia un paso", "riesgo": "bajo"},
        {"camelot": f"{_wrap(n - 1)}{letra}", "movimiento": "-1 misma letra",
         "efecto": "baja energia un paso", "riesgo": "bajo"},
        {"camelot": f"{n}{otra}", "movimiento": "cambio de modo",
         "efecto": "cambia el color mayor/menor sin mover la tonica",
         "riesgo": "bajo"},
    ]
    if include_advanced:
        movimientos += [
            {"camelot": f"{_wrap(n + 7)}{letra}", "movimiento": "+7 dominante",
             "efecto": "salto de energia marcado", "riesgo": "medio: se oye el salto"},
            {"camelot": f"{_wrap(n + 2)}{letra}", "movimiento": "+2",
             "efecto": "subida agresiva", "riesgo": "medio: mejor sobre percusion"},
            {"camelot": f"{_wrap(n - 2)}{letra}", "movimiento": "-2",
             "efecto": "bajada agresiva", "riesgo": "medio"},
        ]
    for mv in movimientos:
        mv["clave"] = CAMELOT_TO_NAME.get(mv["camelot"], "?")
        mv["open_key"] = CAMELOT_TO_OPENKEY.get(mv["camelot"], "?")
    return movimientos


def key_distance(a: str, b: str) -> Optional[int]:
    """Distancia en pasos de rueda entre dos claves Camelot.

    0 = misma clave. 0.5 se representa como 0 con cambio de letra
    (devuelve 1 para el cambio de modo puro por convencion de coste).
    None si alguna clave es invalida.
    """
    try:
        na, la = _split_camelot(a)
        nb, lb = _split_camelot(b)
    except (ValueError, AttributeError):
        return None
    paso = min((na - nb) % 12, (nb - na) % 12)
    if la != lb:
        paso += 1
    return paso


# --------------------------------------------------------------------------
# 2 · TEMPO
# --------------------------------------------------------------------------

def bpm_compatible(a: float, b: float, tolerancia_pct: float = 6.0) -> Dict[str, object]:
    """Compatibilidad de tempo entre A (sonando) y B (entrando).

    Contempla la mezcla a medio y doble tiempo. Las etiquetas dicen SIEMPRE
    que hay que hacerle a B, nunca a A, para que no haya ambiguedad en cabina:
      '1:1'  -> B entra tal cual
      'B x2' -> B se cuenta/reproduce al doble (B es el track lento)
      'B /2' -> B se cuenta/reproduce a la mitad (B es el track rapido)

    tolerancia_pct por defecto 6.0: rango de pitch conservador de un CDJ
    (los CDJ Pioneer ofrecen +/-6, +/-10, +/-16 y WIDE).
    """
    if not a or not b or a <= 0 or b <= 0:
        return {"compatible": False, "motivo": "BPM ausente o invalido",
                "ajuste_pct": None, "relacion": None, "bpm_objetivo": None}
    candidatos = [("1:1", b), ("B x2", b * 2.0), ("B /2", b / 2.0)]
    etiqueta, valor, pct = min(
        ((et, val, (val - a) / a * 100.0) for et, val in candidatos),
        key=lambda c: abs(c[2]),
    )
    ok = abs(pct) <= tolerancia_pct
    explica = {
        "1:1": "B entra a su tempo real",
        "B x2": f"B es el track lento: se cuenta al doble ({b:g} -> {valor:g})",
        "B /2": f"B es el track rapido: se cuenta a la mitad ({b:g} -> {valor:g})",
    }[etiqueta]
    return {
        "compatible": ok,
        "relacion": etiqueta,
        "bpm_objetivo": round(valor, 2),
        "ajuste_pct": round(pct, 2),
        "motivo": (f"{explica}; ajuste de pitch {pct:+.2f}%" if ok else
                   f"{explica}; requiere {pct:+.2f}%, fuera de +/-{tolerancia_pct}%"),
    }


# --------------------------------------------------------------------------
# 3 · LECTURA DE BIBLIOTECAS
# --------------------------------------------------------------------------

_RB_FIELDS = [
    "TrackID", "Name", "Artist", "Composer", "Album", "Grouping", "Genre",
    "Kind", "Size", "TotalTime", "DiscNumber", "TrackNumber", "Year",
    "AverageBpm", "DateAdded", "DateModified", "BitRate", "SampleRate",
    "Comments", "PlayCount", "LastPlayed", "Rating", "Location", "Remixer",
    "Tonality", "Label", "Mix", "Colour",
]


def _location_to_path(location: str) -> str:
    """rekordbox guarda Location como URI file://localhost/..."""
    if not location:
        return ""
    if location.startswith("file://"):
        parsed = urlparse(location)
        return unquote(parsed.path)
    return unquote(location)


def read_rekordbox_xml(path: str) -> Dict[str, object]:
    """Lee un rekordbox collection XML.

    Devuelve {"tracks": [...], "playlists": [...], "version": str}.
    Cada track incluye los atributos crudos, mas campos derivados:
      camelot, bpm (float), duracion_s (int), ruta, cue_points (int),
      memory_cues (int), hot_cues (int), tiene_beatgrid (bool).
    Lanza ValueError si el XML no es un DJ_PLAYLISTS.
    """
    tree = ET.parse(path)
    root = tree.getroot()
    if root.tag != "DJ_PLAYLISTS":
        raise ValueError(
            f"No es un rekordbox XML: raiz <{root.tag}>, se esperaba <DJ_PLAYLISTS>"
        )

    tracks: List[Dict[str, object]] = []
    for node in root.findall("./COLLECTION/TRACK"):
        t: Dict[str, object] = {f: node.get(f, "") for f in _RB_FIELDS}
        marks = node.findall("POSITION_MARK")
        tempos = node.findall("TEMPO")
        t["camelot"] = normalize_key(t.get("Tonality"))
        try:
            t["bpm"] = float(t.get("AverageBpm") or 0) or None
        except ValueError:
            t["bpm"] = None
        try:
            t["duracion_s"] = int(float(t.get("TotalTime") or 0)) or None
        except ValueError:
            t["duracion_s"] = None
        try:
            t["rating"] = int(t.get("Rating") or 0)
        except ValueError:
            t["rating"] = 0
        t["ruta"] = _location_to_path(str(t.get("Location", "")))
        t["cue_points"] = len(marks)
        t["hot_cues"] = len([m for m in marks if (m.get("Num") or "-1") != "-1"])
        t["memory_cues"] = len([m for m in marks if (m.get("Num") or "-1") == "-1"])
        t["tiene_beatgrid"] = len(tempos) > 0
        tracks.append(t)

    playlists: List[Dict[str, object]] = []

    def _walk(node: ET.Element, ruta: str) -> None:
        for child in node.findall("NODE"):
            nombre = child.get("Name", "")
            completo = f"{ruta}/{nombre}" if ruta else nombre
            if child.get("Type") == "0":
                _walk(child, completo)
            else:
                playlists.append({
                    "nombre": nombre,
                    "ruta": completo,
                    "key_type": child.get("KeyType", "0"),
                    "track_keys": [k.get("Key", "") for k in child.findall("TRACK")],
                })

    for pl_root in root.findall("./PLAYLISTS"):
        _walk(pl_root, "")

    return {"tracks": tracks, "playlists": playlists,
            "version": root.get("Version", "")}


def read_m3u(path: str) -> List[Dict[str, str]]:
    """Lee M3U/M3U8. Devuelve [{'titulo','duracion_s','ruta'}]."""
    entradas: List[Dict[str, str]] = []
    pendiente: Dict[str, str] = {}
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            if linea.upper().startswith("#EXTINF:"):
                cuerpo = linea.split(":", 1)[1]
                dur, _, titulo = cuerpo.partition(",")
                pendiente = {"titulo": titulo.strip(),
                             "duracion_s": dur.strip().split(".")[0]}
            elif linea.startswith("#"):
                continue
            else:
                entrada = dict(pendiente)
                entrada["ruta"] = _location_to_path(linea)
                entradas.append(entrada)
                pendiente = {}
    return entradas


def read_history_csv(path: str) -> List[Dict[str, str]]:
    """Lee un CSV/TSV de historial (Serato, rekordbox, export manual).

    Detecta el delimitador y normaliza las cabeceras mas comunes a:
    artista, titulo, hora, bpm, key, deck. Las columnas no reconocidas
    se conservan con su nombre original.
    """
    alias = {
        "artist": "artista", "artista": "artista", "artist name": "artista",
        "name": "titulo", "title": "titulo", "track": "titulo",
        "track name": "titulo", "titulo": "titulo", "song": "titulo",
        "start time": "hora", "played": "hora", "time": "hora",
        "start_time": "hora", "hora": "hora", "date": "hora",
        "bpm": "bpm", "tempo": "bpm", "averagebpm": "bpm",
        "key": "key", "tonality": "key", "tono": "key",
        "deck": "deck", "player": "deck",
    }
    with open(path, "r", encoding="utf-8", errors="replace", newline="") as fh:
        muestra = fh.read(8192)
        fh.seek(0)
        try:
            dialecto = csv.Sniffer().sniff(muestra, delimiters=",;\t|")
        except csv.Error:
            dialecto = csv.excel
        lector = csv.DictReader(fh, dialect=dialecto)
        filas = []
        for fila in lector:
            out: Dict[str, str] = {}
            for k, v in fila.items():
                if k is None:
                    continue
                clave = alias.get(k.strip().lower(), k.strip())
                out[clave] = (v or "").strip()
            if any(out.values()):
                filas.append(out)
    return filas


# --------------------------------------------------------------------------
# 4 · AUDITORIA DE BIBLIOTECA
# --------------------------------------------------------------------------

def _clave_dedup(t: Dict[str, object]) -> str:
    def limpia(s: object) -> str:
        s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
        s = re.sub(r"\((original mix|extended mix|radio edit|clean|dirty)\)", "", s, flags=re.I)
        return re.sub(r"[^a-z0-9]", "", s.lower())
    return f"{limpia(t.get('Artist'))}|{limpia(t.get('Name'))}"


def audit_library(
    tracks: List[Dict[str, object]],
    comprobar_rutas: bool = False,
    min_bitrate: int = 256000,
) -> Dict[str, object]:
    """Audita una coleccion ya leida. Devuelve hallazgos por categoria.

    comprobar_rutas=True verifica en disco que cada Location existe. Solo
    tiene sentido si el script corre en la misma maquina que la biblioteca.
    """
    total = len(tracks)
    hallazgos: Dict[str, List[Dict[str, object]]] = defaultdict(list)

    def ficha(t: Dict[str, object], extra: Optional[Dict[str, object]] = None) -> Dict[str, object]:
        d = {
            "id": t.get("TrackID"),
            "artista": t.get("Artist"),
            "titulo": t.get("Name"),
            "ruta": t.get("ruta"),
        }
        if extra:
            d.update(extra)
        return d

    vistos: Dict[str, List[Dict[str, object]]] = defaultdict(list)

    for t in tracks:
        if not t.get("camelot"):
            hallazgos["sin_clave"].append(ficha(t, {"valor_crudo": t.get("Tonality")}))
        if not t.get("bpm"):
            hallazgos["sin_bpm"].append(ficha(t))
        if not t.get("tiene_beatgrid"):
            hallazgos["sin_beatgrid"].append(ficha(t))
        if t.get("cue_points", 0) == 0:
            hallazgos["sin_cue_points"].append(ficha(t))
        if not str(t.get("Genre") or "").strip():
            hallazgos["sin_genero"].append(ficha(t))
        if not t.get("rating"):
            hallazgos["sin_rating"].append(ficha(t))
        try:
            br = int(t.get("BitRate") or 0)
        except ValueError:
            br = 0
        if br and br * 1000 < min_bitrate:
            hallazgos["bitrate_bajo"].append(ficha(t, {"bitrate_kbps": br}))
        dur = t.get("duracion_s") or 0
        if dur and dur < 120:
            hallazgos["muy_corto"].append(ficha(t, {"duracion_s": dur}))
        if comprobar_rutas and t.get("ruta") and not os.path.exists(str(t["ruta"])):
            hallazgos["ruta_rota"].append(ficha(t))
        vistos[_clave_dedup(t)].append(t)

    for clave, grupo in vistos.items():
        if len(grupo) > 1 and clave.strip("|"):
            hallazgos["duplicados"].append({
                "clave": clave,
                "copias": len(grupo),
                "rutas": [g.get("ruta") for g in grupo],
                "artista": grupo[0].get("Artist"),
                "titulo": grupo[0].get("Name"),
            })

    generos = Counter(str(t.get("Genre") or "").strip() for t in tracks if str(t.get("Genre") or "").strip())
    variantes: Dict[str, List[str]] = defaultdict(list)
    for g in generos:
        variantes[re.sub(r"[^a-z0-9]", "", g.lower())].append(g)
    for _, grupo in variantes.items():
        if len(grupo) > 1:
            hallazgos["genero_inconsistente"].append({
                "variantes": sorted(grupo),
                "usos": {g: generos[g] for g in grupo},
            })

    resumen = {k: len(v) for k, v in sorted(hallazgos.items())}
    pesos = {
        "sin_beatgrid": 3.0, "sin_bpm": 3.0, "ruta_rota": 3.0,
        "sin_clave": 2.0, "sin_cue_points": 1.5, "duplicados": 1.5,
        "sin_genero": 1.0, "bitrate_bajo": 1.0, "sin_rating": 0.5,
        "muy_corto": 0.5, "genero_inconsistente": 0.5,
    }
    penalizacion = sum(pesos.get(k, 0.5) * n for k, n in resumen.items())
    max_pen = max(total, 1) * sum(pesos.values())
    salud = round(max(0.0, 100.0 * (1 - penalizacion / max_pen)), 1)

    return {
        "total_tracks": total,
        "resumen": resumen,
        "salud_0_100": salud,
        "hallazgos": dict(hallazgos),
        "distribucion_camelot": dict(Counter(
            t["camelot"] for t in tracks if t.get("camelot")
        )),
        "distribucion_bpm": dict(Counter(
            f"{int(t['bpm'] // 5 * 5)}-{int(t['bpm'] // 5 * 5 + 4)}"
            for t in tracks if t.get("bpm")
        )),
        "distribucion_genero": dict(generos.most_common(40)),
    }


# --------------------------------------------------------------------------
# 5 · UTILIDAD DE LINEA DE COMANDOS
# --------------------------------------------------------------------------

def _cli() -> int:
    import argparse
    import json

    p = argparse.ArgumentParser(description="dj_toolkit — utilidades de biblioteca DJ")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("audit", help="audita un rekordbox collection XML")
    pa.add_argument("xml")
    pa.add_argument("--comprobar-rutas", action="store_true")
    pa.add_argument("--json", action="store_true", help="salida JSON completa")
    pa.add_argument("--limite", type=int, default=15, help="ejemplos por categoria")

    pk = sub.add_parser("key", help="normaliza y expande una clave")
    pk.add_argument("clave")
    pk.add_argument("--avanzado", action="store_true")

    pb = sub.add_parser("bpm", help="compatibilidad de tempo entre dos BPM")
    pb.add_argument("a", type=float)
    pb.add_argument("b", type=float)
    pb.add_argument("--tolerancia", type=float, default=6.0)

    args = p.parse_args()

    if args.cmd == "audit":
        col = read_rekordbox_xml(args.xml)
        rep = audit_library(col["tracks"], comprobar_rutas=args.comprobar_rutas)
        if args.json:
            print(json.dumps(rep, ensure_ascii=False, indent=2, default=str))
            return 0
        print(f"Tracks: {rep['total_tracks']}   Salud: {rep['salud_0_100']}/100")
        print(f"Playlists: {len(col['playlists'])}\n")
        print("HALLAZGOS")
        for k, n in sorted(rep["resumen"].items(), key=lambda x: -x[1]):
            pct = 100.0 * n / max(rep["total_tracks"], 1)
            print(f"  {k:24s} {n:6d}  ({pct:5.1f}% de la coleccion)")
        for k in ("sin_beatgrid", "ruta_rota", "duplicados", "sin_clave"):
            ejemplos = rep["hallazgos"].get(k, [])[: args.limite]
            if ejemplos:
                print(f"\n  -- {k} (primeros {len(ejemplos)}) --")
                for e in ejemplos:
                    print(f"     {e.get('artista','?')} - {e.get('titulo','?')}")
        return 0

    if args.cmd == "key":
        cam = normalize_key(args.clave)
        if not cam:
            print(f"No reconocida: {args.clave!r}")
            return 1
        print(f"{args.clave!r} -> Camelot {cam} | Open Key {CAMELOT_TO_OPENKEY[cam]} "
              f"| {CAMELOT_TO_NAME[cam]}\n")
        for mv in compatible_keys(cam, include_advanced=args.avanzado):
            print(f"  {mv['camelot']:4s} {mv['clave']:10s} {mv['movimiento']:20s} "
                  f"{mv['efecto']}  [riesgo {mv['riesgo']}]")
        return 0

    if args.cmd == "bpm":
        r = bpm_compatible(args.a, args.b, args.tolerancia)
        print(f"{args.a} -> {args.b}: {'OK' if r['compatible'] else 'NO'} | {r['motivo']}")
        return 0 if r["compatible"] else 1

    return 1


if __name__ == "__main__":
    raise SystemExit(_cli())
