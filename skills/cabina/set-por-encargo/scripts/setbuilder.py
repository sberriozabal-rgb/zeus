#!/usr/bin/env python3
"""
setbuilder — construye un set ordenado a partir de un pool real de tracks.

No inventa musica: solo ordena lo que ya esta en la biblioteca del DJ y
justifica cada transicion con criterios verificables (clave, tempo, energia,
separacion de artista). Lo que no puede decidir, lo declara.

Entrada:  rekordbox collection XML, o CSV con columnas
          artista,titulo,bpm,key[,energia,genero,duracion_s]
Salida:   set ordenado + nota de transicion por par + huecos declarados
          (texto, JSON o M3U)

Depende solo de dj_toolkit y de la biblioteca estandar.
"""

from __future__ import annotations

import csv
import json
import os
import re
import sys
from typing import Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dj_toolkit import (  # noqa: E402
    CAMELOT_TO_NAME, bpm_compatible, key_distance, normalize_key,
    read_rekordbox_xml,
)

__version__ = "1.0.0"

# --------------------------------------------------------------------------
# CURVAS DE ENERGIA
# --------------------------------------------------------------------------
# Cada curva devuelve la energia objetivo (1-10) en la posicion relativa p
# (0.0 = primer track, 1.0 = ultimo).

def _curva_rampa(p: float, lo: float, hi: float) -> float:
    return lo + (hi - lo) * p


def _curva_arco(p: float, lo: float, hi: float) -> float:
    # sube hasta el 70% del set, luego cae un tercio del recorrido
    if p <= 0.7:
        return lo + (hi - lo) * (p / 0.7)
    return hi - (hi - lo) * 0.33 * ((p - 0.7) / 0.3)


def _curva_meseta(p: float, lo: float, hi: float) -> float:
    if p < 0.25:
        return lo + (hi - lo) * (p / 0.25)
    if p > 0.85:
        return hi - (hi - lo) * 0.25 * ((p - 0.85) / 0.15)
    return hi


def _curva_descenso(p: float, lo: float, hi: float) -> float:
    return hi - (hi - lo) * p


def _curva_dientes(p: float, lo: float, hi: float) -> float:
    # tension y alivio: tres subidas con caida parcial, tendencia ascendente
    base = lo + (hi - lo) * p
    import math
    return max(lo, min(hi, base + (hi - lo) * 0.18 * math.sin(p * 3 * 2 * math.pi)))


CURVAS = {
    "rampa": (_curva_rampa, "sube de forma continua de principio a fin"),
    "arco": (_curva_arco, "sube al pico en el 70% del set y baja al cierre"),
    "meseta": (_curva_meseta, "sube rapido, sostiene el pico, cierra bajando poco"),
    "descenso": (_curva_descenso, "empieza arriba y baja: cierre o after"),
    "dientes": (_curva_dientes, "tension y alivio en tres oleadas ascendentes"),
}

# --------------------------------------------------------------------------
# CARGA DE POOL
# --------------------------------------------------------------------------

_ENERGY_RE = re.compile(r"energy\s*[-:]?\s*(\d{1,2})", re.I)


def _energia_de_comentario(comentario: str) -> Optional[int]:
    """Mixed In Key escribe 'Energy 7' en el campo Comments."""
    if not comentario:
        return None
    m = _ENERGY_RE.search(str(comentario))
    if m:
        v = int(m.group(1))
        return v if 1 <= v <= 10 else None
    return None


def _energia_de_rating(rating: object) -> Optional[int]:
    """rekordbox guarda el rating en 0/51/102/153/204/255 (0-5 estrellas)."""
    try:
        r = int(rating or 0)
    except (TypeError, ValueError):
        return None
    if r <= 0:
        return None
    estrellas = round(r / 51.0)
    return int(max(1, min(10, estrellas * 2)))


def cargar_pool(ruta: str) -> Tuple[List[Dict[str, object]], List[str]]:
    """Devuelve (pool, avisos). Nunca lanza por un track malo: lo descarta y avisa."""
    avisos: List[str] = []
    pool: List[Dict[str, object]] = []

    if ruta.lower().endswith(".xml"):
        col = read_rekordbox_xml(ruta)
        for t in col["tracks"]:
            pool.append({
                "artista": str(t.get("Artist") or "").strip(),
                "titulo": str(t.get("Name") or "").strip(),
                "bpm": t.get("bpm"),
                "camelot": t.get("camelot"),
                "energia": (_energia_de_comentario(str(t.get("Comments") or ""))
                            or _energia_de_rating(t.get("Rating"))),
                "genero": str(t.get("Genre") or "").strip(),
                "duracion_s": t.get("duracion_s"),
                "ruta": t.get("ruta"),
                "_energia_inferida": _energia_de_comentario(str(t.get("Comments") or "")) is None,
            })
    else:
        with open(ruta, "r", encoding="utf-8", errors="replace", newline="") as fh:
            muestra = fh.read(8192)
            fh.seek(0)
            try:
                dial = csv.Sniffer().sniff(muestra, delimiters=",;\t|")
            except csv.Error:
                dial = csv.excel
            alias = {
                "artist": "artista", "artista": "artista",
                "title": "titulo", "name": "titulo", "titulo": "titulo", "track": "titulo",
                "bpm": "bpm", "tempo": "bpm", "averagebpm": "bpm",
                "key": "camelot", "tonality": "camelot", "camelot": "camelot", "tono": "camelot",
                "energy": "energia", "energia": "energia", "energy level": "energia",
                "genre": "genero", "genero": "genero",
                "time": "duracion_s", "duracion_s": "duracion_s", "duration": "duracion_s",
            }
            for i, fila in enumerate(csv.DictReader(fh, dialect=dial), start=2):
                d: Dict[str, object] = {}
                for k, v in fila.items():
                    if k is None:
                        continue
                    d[alias.get(k.strip().lower(), k.strip().lower())] = (v or "").strip()
                if not d.get("titulo"):
                    avisos.append(f"linea {i}: sin titulo, descartada")
                    continue
                try:
                    d["bpm"] = float(str(d.get("bpm") or "").replace(",", ".")) or None
                except ValueError:
                    d["bpm"] = None
                d["camelot"] = normalize_key(str(d.get("camelot") or ""))
                try:
                    e = int(float(str(d.get("energia") or "") or 0))
                    d["energia"] = e if 1 <= e <= 10 else None
                except ValueError:
                    d["energia"] = None
                d["_energia_inferida"] = d["energia"] is None
                try:
                    d["duracion_s"] = int(float(str(d.get("duracion_s") or "") or 0)) or None
                except ValueError:
                    d["duracion_s"] = None
                pool.append(d)

    for t in pool:
        t.setdefault("artista", "")
        t.setdefault("genero", "")
        if t.get("energia") is None:
            # Sin energia declarada: se infiere del BPM dentro del rango del pool.
            t["energia"] = None
    return pool, avisos


def _inferir_energia_por_bpm(pool: Sequence[Dict[str, object]]) -> int:
    bpms = [t["bpm"] for t in pool if t.get("bpm")]
    if not bpms:
        return 0
    lo, hi = min(bpms), max(bpms)
    span = max(hi - lo, 1e-6)
    n = 0
    for t in pool:
        if t.get("energia") is None and t.get("bpm"):
            t["energia"] = int(max(1, min(10, round(1 + 9 * (t["bpm"] - lo) / span))))
            t["_energia_inferida"] = True
            n += 1
    return n


# --------------------------------------------------------------------------
# PUNTUACION DE TRANSICION
# --------------------------------------------------------------------------

PESOS_DEFECTO = {
    "clave": 4.0,
    "tempo": 3.0,
    "energia": 3.0,
    "artista": 2.5,
    "genero": 1.0,
    "estancamiento": 2.0,
}

# A partir de cuantos tracks seguidos en la misma clave se empieza a penalizar.
# Quedarse en la misma clave es armonicamente seguro pero aplana el set: tres
# tracks seguidos es una decision, seis es un descuido.
MAX_MISMA_CLAVE = 3


def coste_transicion(
    a: Dict[str, object],
    b: Dict[str, object],
    energia_objetivo: float,
    recientes: Sequence[Dict[str, object]],
    tolerancia_bpm: float,
    pesos: Dict[str, float],
) -> Tuple[float, Dict[str, object]]:
    """Coste de poner b despues de a. Menor es mejor. Devuelve (coste, detalle)."""
    detalle: Dict[str, object] = {}
    coste = 0.0

    # -- Clave -------------------------------------------------------------
    ka, kb = a.get("camelot"), b.get("camelot")
    if not ka or not kb:
        c_key = 1.5  # penalizacion moderada por dato ausente, no descarte
        detalle["clave"] = "sin dato de clave en uno de los dos: no verificable"
    else:
        d = key_distance(str(ka), str(kb))
        c_key = {0: 0.0, 1: 0.4, 2: 1.6}.get(d, 3.0 + (d or 0) * 0.4)
        etiqueta = {0: "misma clave", 1: "movimiento vecino", 2: "salto de 2"}.get(
            d, f"salto de {d} pasos")
        detalle["clave"] = f"{ka} -> {kb} ({etiqueta})"
    coste += c_key * pesos["clave"]

    # -- Tempo -------------------------------------------------------------
    ba, bb = a.get("bpm"), b.get("bpm")
    if not ba or not bb:
        c_bpm = 1.5
        detalle["tempo"] = "sin BPM en uno de los dos: no verificable"
    else:
        r = bpm_compatible(float(ba), float(bb), tolerancia_bpm)
        pct = abs(r["ajuste_pct"] or 0)
        c_bpm = min(pct / max(tolerancia_bpm, 1e-6), 3.0)
        detalle["tempo"] = (f"{ba:g} -> {bb:g} BPM ({r['relacion']}, "
                            f"{r['ajuste_pct']:+.1f}%)")
        detalle["_tempo_ok"] = bool(r["compatible"])
    coste += c_bpm * pesos["tempo"]

    # -- Energia -----------------------------------------------------------
    eb = b.get("energia")
    if eb is None:
        c_e = 1.0
        detalle["energia"] = "sin energia: no verificable"
    else:
        desvio = abs(float(eb) - energia_objetivo)
        c_e = min(desvio / 3.0, 3.0)
        detalle["energia"] = f"E{eb} vs objetivo E{energia_objetivo:.1f}"
    coste += c_e * pesos["energia"]

    # -- Repeticion de artista --------------------------------------------
    art_b = str(b.get("artista") or "").strip().lower()
    c_art = 0.0
    dist_match: Optional[int] = None
    if art_b:
        for dist, prev in enumerate(reversed(recientes[-4:]), start=1):
            if str(prev.get("artista") or "").strip().lower() == art_b:
                castigo = (5 - dist) / 4.0 * 3.0
                if castigo > c_art:
                    c_art, dist_match = castigo, dist
        if dist_match is not None:
            detalle["artista"] = (f"'{b.get('artista')}' ya sono hace {dist_match} "
                                  f"track{'s' if dist_match > 1 else ''}")
    coste += c_art * pesos["artista"]

    # -- Estancamiento armonico -------------------------------------------
    # Repetir clave es gratis en coste armonico, asi que sin este freno el
    # buscador se queda clavado en una sola clave todo el set.
    c_est = 0.0
    if kb:
        seguidos = 0
        for prev in reversed(recientes):
            if prev.get("camelot") == kb:
                seguidos += 1
            else:
                break
        if seguidos >= MAX_MISMA_CLAVE:
            c_est = min((seguidos - MAX_MISMA_CLAVE + 1) * 1.2, 4.0)
            detalle["estancamiento"] = (
                f"{seguidos} tracks seguidos ya en {kb}: el set se aplana")
    coste += c_est * pesos["estancamiento"]

    # -- Coherencia de genero ---------------------------------------------
    ga = str(a.get("genero") or "").strip().lower()
    gb = str(b.get("genero") or "").strip().lower()
    c_gen = 1.0 if (ga and gb and ga != gb) else 0.0
    if c_gen:
        detalle["genero"] = f"{a.get('genero')} -> {b.get('genero')}"
    coste += c_gen * pesos["genero"]

    return coste, detalle


# --------------------------------------------------------------------------
# BUSQUEDA
# --------------------------------------------------------------------------

def construir_set(
    pool: List[Dict[str, object]],
    n_tracks: int,
    curva: str = "arco",
    energia_min: float = 3.0,
    energia_max: float = 9.0,
    tolerancia_bpm: float = 6.0,
    apertura: Optional[str] = None,
    obligatorios: Optional[Sequence[str]] = None,
    vetados: Optional[Sequence[str]] = None,
    anchura_haz: int = 12,
    pesos: Optional[Dict[str, float]] = None,
) -> Dict[str, object]:
    """Beam search sobre el pool. Devuelve el set y el porque de cada paso."""
    pesos = {**PESOS_DEFECTO, **(pesos or {})}
    if curva not in CURVAS:
        raise ValueError(f"Curva desconocida: {curva}. Opciones: {list(CURVAS)}")
    fn_curva, desc_curva = CURVAS[curva]

    def coincide(t: Dict[str, object], patron: str) -> bool:
        p = patron.strip().lower()
        return p in f"{t.get('artista','')} {t.get('titulo','')}".lower()

    disponibles = list(pool)
    if vetados:
        antes = len(disponibles)
        disponibles = [t for t in disponibles
                       if not any(coincide(t, v) for v in vetados)]
        vetados_n = antes - len(disponibles)
    else:
        vetados_n = 0

    inferidos = _inferir_energia_por_bpm(disponibles)

    if len(disponibles) < n_tracks:
        n_tracks = len(disponibles)

    # Track de apertura
    if apertura:
        cands = [t for t in disponibles if coincide(t, apertura)]
        if not cands:
            raise ValueError(f"Ningun track del pool coincide con la apertura {apertura!r}")
        primero = cands[0]
    else:
        objetivo0 = fn_curva(0.0, energia_min, energia_max)
        primero = min(disponibles,
                      key=lambda t: abs(float(t.get("energia") or 5) - objetivo0))

    obligatorios_pend: List[Dict[str, object]] = []
    for o in (obligatorios or []):
        cands = [t for t in disponibles if coincide(t, o) and t is not primero]
        if cands:
            obligatorios_pend.append(cands[0])

    # Posiciones donde hubo que romper el tope de clave por falta de alternativa
    forzado_estancamiento: List[int] = []

    # Estado del haz: (coste_acumulado, secuencia, ids_usados, notas)
    haz: List[Tuple[float, List[Dict[str, object]], set, List[Dict[str, object]]]] = [
        (0.0, [primero], {id(primero)}, [])
    ]

    for paso in range(1, n_tracks):
        p = paso / max(n_tracks - 1, 1)
        objetivo = fn_curva(p, energia_min, energia_max)
        restantes = n_tracks - paso
        nuevo_haz = []
        for coste_acc, seq, usados, notas in haz:
            a = seq[-1]
            # Forzar obligatorios si se acaba el margen
            pendientes = [o for o in obligatorios_pend if id(o) not in usados]
            candidatos = disponibles
            if pendientes and len(pendientes) >= restantes:
                candidatos = pendientes
            # Cuantos tracks seguidos lleva ya la clave actual
            clave_actual = a.get("camelot")
            seguidos_actual = 0
            if clave_actual:
                for prev in reversed(seq):
                    if prev.get("camelot") == clave_actual:
                        seguidos_actual += 1
                    else:
                        break

            puntuados = []
            bloqueados = []
            for b in candidatos:
                if id(b) in usados:
                    continue
                c, det = coste_transicion(a, b, objetivo, seq, tolerancia_bpm, pesos)
                if b in pendientes:
                    c -= 6.0  # incentivo para colocar los obligatorios
                # Tope duro: no encadenar mas de MAX_MISMA_CLAVE en la misma clave
                if (clave_actual and b.get("camelot") == clave_actual
                        and seguidos_actual >= MAX_MISMA_CLAVE
                        and b not in pendientes):
                    bloqueados.append((c, b, det))
                else:
                    puntuados.append((c, b, det))
            if not puntuados:
                # El pool no ofrece alternativa de clave: se admite y se declara.
                puntuados = bloqueados
                forzado_estancamiento.append(paso + 1)
            puntuados.sort(key=lambda x: x[0])
            for c, b, det in puntuados[:anchura_haz]:
                nuevo_haz.append((coste_acc + c, seq + [b], usados | {id(b)},
                                  notas + [{"objetivo_energia": round(objetivo, 1), **det}]))
        if not nuevo_haz:
            break
        nuevo_haz.sort(key=lambda x: x[0])
        haz = nuevo_haz[:anchura_haz]

    coste_final, seq, _, notas = haz[0]

    no_colocados = [f"{o.get('artista')} - {o.get('titulo')}"
                    for o in obligatorios_pend if o not in seq]

    duracion = sum(int(t.get("duracion_s") or 0) for t in seq)
    sin_duracion = sum(1 for t in seq if not t.get("duracion_s"))

    return {
        "set": seq,
        "transiciones": notas,
        "curva": {"nombre": curva, "descripcion": desc_curva,
                  "energia_min": energia_min, "energia_max": energia_max},
        "coste_total": round(coste_final, 2),
        "coste_medio_transicion": round(coste_final / max(len(seq) - 1, 1), 2),
        "duracion_estimada_s": duracion,
        "declaraciones": {
            "tracks_en_pool": len(pool),
            "vetados_excluidos": vetados_n,
            "energia_inferida_de_bpm": inferidos,
            "tracks_sin_duracion": sin_duracion,
            "obligatorios_no_colocados": no_colocados,
            "aviso_energia": (
                f"{inferidos} tracks no traian energia declarada; se infirio del BPM "
                "dentro del rango del pool. Es una aproximacion, no una medicion."
            ) if inferidos else None,
            "aviso_duracion": (
                f"{sin_duracion} tracks sin duracion: la duracion estimada del set "
                "esta incompleta."
            ) if sin_duracion else None,
            "aviso_estancamiento": (
                f"En las posiciones {sorted(set(forzado_estancamiento))} no habia ningun "
                f"track en otra clave disponible: hay mas de {MAX_MISMA_CLAVE} seguidos "
                "en la misma clave. El pool es demasiado estrecho en armonia."
            ) if forzado_estancamiento else None,
        },
    }


# --------------------------------------------------------------------------
# SALIDAS
# --------------------------------------------------------------------------

def _mmss(seg: int) -> str:
    return f"{seg // 60}:{seg % 60:02d}"


def render_texto(r: Dict[str, object]) -> str:
    L: List[str] = []
    c = r["curva"]
    L.append(f"SET — curva '{c['nombre']}': {c['descripcion']}")
    L.append(f"{len(r['set'])} tracks · duracion estimada {_mmss(r['duracion_estimada_s'])} "
             f"· coste medio por transicion {r['coste_medio_transicion']}")
    L.append("")
    acumulado = 0
    for i, t in enumerate(r["set"]):
        marca = _mmss(acumulado)
        clave = t.get("camelot") or "??"
        nombre_clave = CAMELOT_TO_NAME.get(str(clave), "")
        bpm = f"{t['bpm']:g}" if t.get("bpm") else "??"
        L.append(f"{i+1:2d}. [{marca:>5}] {t.get('artista','?')} — {t.get('titulo','?')}")
        L.append(f"          {bpm} BPM · {clave} {nombre_clave} · E{t.get('energia','?')}"
                 + (f" · {t.get('genero')}" if t.get("genero") else ""))
        if i < len(r["transiciones"]):
            n = r["transiciones"][i]
            piezas = [f"clave: {n.get('clave','-')}", f"tempo: {n.get('tempo','-')}",
                      f"energia: {n.get('energia','-')}"]
            if n.get("artista"):
                piezas.append(f"AVISO {n['artista']}")
            if n.get("genero"):
                piezas.append(f"cambio de genero {n['genero']}")
            L.append(f"       -> {' | '.join(piezas)}")
        acumulado += int(t.get("duracion_s") or 0)
    d = r["declaraciones"]
    L.append("")
    L.append("DECLARACIONES")
    L.append(f"  pool: {d['tracks_en_pool']} tracks · vetados excluidos: {d['vetados_excluidos']}")
    for k in ("aviso_energia", "aviso_duracion", "aviso_estancamiento"):
        if d.get(k):
            L.append(f"  {d[k]}")
    if d["obligatorios_no_colocados"]:
        L.append(f"  NO COLOCADOS (pediste incluirlos): {', '.join(d['obligatorios_no_colocados'])}")
    return "\n".join(L)


def render_m3u(r: Dict[str, object]) -> str:
    L = ["#EXTM3U"]
    for t in r["set"]:
        dur = int(t.get("duracion_s") or -1)
        L.append(f"#EXTINF:{dur},{t.get('artista','')} - {t.get('titulo','')}")
        L.append(str(t.get("ruta") or f"{t.get('artista','')} - {t.get('titulo','')}"))
    return "\n".join(L)


def _cli() -> int:
    import argparse
    p = argparse.ArgumentParser(description="setbuilder — ordena un set desde tu pool real")
    p.add_argument("pool", help="rekordbox XML o CSV (artista,titulo,bpm,key[,energia,genero,duracion_s])")
    p.add_argument("-n", "--tracks", type=int, default=15)
    p.add_argument("-c", "--curva", default="arco", choices=list(CURVAS))
    p.add_argument("--energia-min", type=float, default=3.0)
    p.add_argument("--energia-max", type=float, default=9.0)
    p.add_argument("--tolerancia-bpm", type=float, default=6.0)
    p.add_argument("--apertura", help="texto que identifica el track de apertura")
    p.add_argument("--incluir", action="append", default=[], help="track obligatorio (repetible)")
    p.add_argument("--vetar", action="append", default=[], help="track o artista vetado (repetible)")
    p.add_argument("--formato", choices=["texto", "json", "m3u"], default="texto")
    a = p.parse_args()

    pool, avisos = cargar_pool(a.pool)
    for av in avisos[:10]:
        print(f"[aviso] {av}", file=sys.stderr)
    if not pool:
        print("Pool vacio: no hay nada que ordenar.", file=sys.stderr)
        return 1
    try:
        r = construir_set(
            pool, a.tracks, curva=a.curva, energia_min=a.energia_min,
            energia_max=a.energia_max, tolerancia_bpm=a.tolerancia_bpm,
            apertura=a.apertura, obligatorios=a.incluir, vetados=a.vetar,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if a.formato == "json":
        print(json.dumps(r, ensure_ascii=False, indent=2, default=str))
    elif a.formato == "m3u":
        print(render_m3u(r))
    else:
        print(render_texto(r))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
