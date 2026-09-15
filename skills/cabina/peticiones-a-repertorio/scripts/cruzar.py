#!/usr/bin/env python3
"""
cruzar — cruza una lista de peticiones en texto sucio contra la biblioteca real.

El caso de uso: el cliente manda por WhatsApp o email una lista de canciones
mal escritas, mezcladas con prohibiciones y comentarios. El DJ tiene que saber
que tiene, que le falta comprar y que esta en una version que no sirve.

Entrada:
  · biblioteca: rekordbox XML o CSV con columnas artista,titulo[,...]
  · peticiones: fichero de texto libre, una por linea (o prosa)

Salida: informe con cuatro cubos
  TENGO · NO TENGO · DUDOSO (varias coincidencias o parcial) · PROHIBIDO

Coincidencia por similitud de cadena de la biblioteca estandar (difflib),
sin dependencias externas. NO adivina: lo que no supera el umbral alto
cae a DUDOSO para que lo decida una persona.
"""

from __future__ import annotations

import csv
import os
import re
import sys
import unicodedata
from difflib import SequenceMatcher
from typing import Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dj_toolkit import read_rekordbox_xml  # noqa: E402

__version__ = "1.0.0"

UMBRAL_SEGURO = 0.86   # por encima: se da por encontrado
UMBRAL_DUDA = 0.62     # entre duda y seguro: requiere decision humana

# Marcadores de prohibicion en lenguaje natural (es/en).
# El orden importa: las formas largas van primero para que se consuman enteras
# y no dejen restos como 'quiero perreo' al quitar solo el 'no'.
_PROHIBICION = re.compile(
    r"^\s*(?:que\s+no\s+(?:suene|pongan?|se\s+oiga)|no\s+(?:quiero|queremos|"
    r"pongas?|pongan|me\s+gusta|nos\s+gusta)|nada\s+de|ni\s+se\s+te\s+ocurra|"
    r"prohibid[oa]s?|vetad[oa]s?|evitar|odio|odiamos|nunca|jam[aá]s|sin|no|"
    r"don'?t\s+(?:play|want)|do\s+not\s+play|avoid|no\s+more|ban(?:ned)?|not)\b",
    re.I)

# Lineas de conversacion que no son peticiones. Se apartan y se reportan,
# nunca se descartan en silencio: si el sistema se come una peticion de verdad
# el DJ tiene que poder verlo.
_CHARLA = re.compile(
    r"^\s*(?:hola|buenas|hey|hi|hello|gracias|thanks|thank\s+you|un\s+saludo|"
    r"saludos|besos|abrazo|perfecto|vale|ok(?:ay)?|genial|te\s+paso|os\s+paso|"
    r"aqu[ií]\s+(?:va|te|os)|adjunto|como\s+(?:hablamos|quedamos|comentamos)|"
    r"lo\s+que\s+hablamos|la\s+lista\s+(?:que|de)|estas?\s+son|estos?\s+son|"
    r"algunas?\s+(?:ideas|canciones)|a\s+ver\s+qu[eé]|dime|av[ií]same|"
    r"cualquier\s+cosa|nos\s+vemos|un\s+placer|buenos\s+d[ií]as|"
    r"buenas\s+(?:tardes|noches))\b", re.I)

# Ruido tipico de una lista pegada de WhatsApp/email
_RUIDO = re.compile(
    r"^\s*(?:[-*·•‣>#]+|\d{1,3}[.)\]]|\[\s?\]|\(\s?\))\s*")
_HORA_WA = re.compile(r"^\s*\[?\d{1,2}[:/]\d{2}(?:[:.]\d{2})?\]?\s*[-–]?\s*"
                      r"(?:[^:]{1,40}:)?\s*")
_PARENTESIS = re.compile(r"\s*[\(\[]([^)\]]*)[\)\]]\s*")

# Palabras que no aportan a la comparacion de titulos
_VERSIONES = re.compile(
    r"\b(original mix|extended mix|radio edit|radio mix|club mix|club edit|"
    r"clean|dirty|explicit|instrumental|acapella|acappella|remix|rmx|edit|"
    r"version|versi[oó]n|remaster(?:ed)?|feat\.?|ft\.?|with|vs\.?|bootleg|"
    r"mashup|intro|outro|short|long|official|video|audio|lyrics?|hd|hq)\b", re.I)


def _plano(s: str) -> str:
    """Minusculas, sin acentos, sin puntuacion, espacios colapsados."""
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"&", " and ", s)
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _nucleo(s: str) -> str:
    """Version comparable de un titulo: sin marcas de version ni parentesis."""
    s = _PARENTESIS.sub(" ", str(s or ""))
    s = _VERSIONES.sub(" ", s)
    return _plano(s)


def _similitud(a: str, b: str) -> float:
    """Similitud robusta al orden de las palabras.

    El cliente escribe 'Despecha rosalia' y la biblioteca dice 'Rosalia -
    DESPECHA': la comparacion literal de cadenas hunde ese par. Se toma el
    mejor de tres criterios: literal, con tokens ordenados, y contencion
    de tokens (una lista es subconjunto de la otra).
    """
    if not a or not b:
        return 0.0
    literal = SequenceMatcher(None, a, b).ratio()

    ta, tb = a.split(), b.split()
    if not ta or not tb:
        return literal
    ordenado = SequenceMatcher(None, " ".join(sorted(ta)), " ".join(sorted(tb))).ratio()

    sa, sb = set(ta), set(tb)
    comunes = len(sa & sb)

    # La contencion solo entra en juego con 2+ palabras en comun. Con una sola
    # palabra compartida generaba falsos positivos graves: 'Queen' encajaba con
    # 'Dancing Queen' al 0.86 y colaba Bohemian Rhapsody como si estuviera en
    # la biblioteca. Una palabra suelta no sostiene una coincidencia.
    if comunes < 2:
        return max(literal, ordenado)

    contencion = comunes / min(len(sa), len(sb))
    # Se pondera por cuanto del texto largo queda explicado, para que una
    # peticion corta no se coma un titulo mucho mas largo.
    cobertura = comunes / max(len(sa), len(sb))
    contencion = contencion * (0.72 + 0.28 * cobertura)

    return max(literal, ordenado, contencion)


# --------------------------------------------------------------------------
# PARSEO DE LA LISTA DE PETICIONES
# --------------------------------------------------------------------------

def parsear_peticiones(texto: str) -> List[Dict[str, object]]:
    """Convierte prosa sucia en peticiones estructuradas.

    Reconoce 'Artista - Titulo', 'Titulo de Artista', 'Titulo — Artista',
    numeracion, vinietas, marcas de hora de WhatsApp y lineas de prohibicion.
    Lo que no puede separar en artista/titulo lo deja como consulta libre.
    """
    peticiones: List[Dict[str, object]] = []
    seccion_prohibida = False

    for bruto in str(texto or "").splitlines():
        linea = bruto.strip()
        if not linea:
            continue

        # Encabezado de seccion: "NO PONER:", "Prohibidas:", "Do not play"
        if re.fullmatch(r"[^a-z0-9]*(?:lista\s+)?(?:de\s+)?"
                        r"(?:no\s*poner|prohibid[oa]s?|vetad[oa]s?|"
                        r"do\s*not\s*play|banned|blacklist)[^a-z0-9]*",
                        linea, re.I):
            seccion_prohibida = True
            continue
        if re.fullmatch(r"[^a-z0-9]*(?:si\s*poner|imprescindibles?|"
                        r"must\s*play|peticiones|requests?)[^a-z0-9]*",
                        linea, re.I):
            seccion_prohibida = False
            continue

        linea = _HORA_WA.sub("", linea)
        linea = _RUIDO.sub("", linea).strip()
        if not linea or len(_plano(linea)) < 2:
            continue

        prohibida = seccion_prohibida or bool(_PROHIBICION.match(linea))

        # Charla: solo se aparta si NO esta marcada como prohibicion ni vive
        # dentro de la seccion de prohibidas.
        if not prohibida and _CHARLA.match(linea):
            peticiones.append({
                "linea_original": bruto.strip(), "texto": linea,
                "artista": "", "titulo": "", "nota": "",
                "prohibida": False, "ignorada": True,
            })
            continue

        limpia = (_PROHIBICION.sub("", linea, count=1).strip(" ,;:.-–—")
                  if _PROHIBICION.match(linea) else linea)

        nota = ""
        m = _PARENTESIS.search(limpia)
        if m:
            nota = m.group(1).strip()

        artista, titulo = "", ""
        # "Artista - Titulo" / "Artista — Titulo" / "Artista: Titulo"
        m = re.match(r"^(.{2,60}?)\s+[-–—:]\s+(.{2,80})$", limpia)
        if m:
            artista, titulo = m.group(1).strip(), m.group(2).strip()
        else:
            # "Titulo de Artista" / "Titulo by Artista"
            m = re.match(r"^(.{2,80}?)\s+(?:de|by|of)\s+(.{2,60})$", limpia, re.I)
            if m:
                titulo, artista = m.group(1).strip(), m.group(2).strip()

        peticiones.append({
            "linea_original": bruto.strip(),
            "texto": limpia,
            "artista": artista,
            "titulo": titulo,
            "nota": nota,
            "prohibida": prohibida,
            "ignorada": False,
        })
    return peticiones


# --------------------------------------------------------------------------
# CARGA DE BIBLIOTECA
# --------------------------------------------------------------------------

def cargar_biblioteca(ruta: str) -> List[Dict[str, object]]:
    tracks: List[Dict[str, object]] = []
    if ruta.lower().endswith(".xml"):
        for t in read_rekordbox_xml(ruta)["tracks"]:
            tracks.append({
                "artista": t.get("Artist") or "",
                "titulo": t.get("Name") or "",
                "mix": t.get("Mix") or "",
                "genero": t.get("Genre") or "",
                "bpm": t.get("bpm"),
                "camelot": t.get("camelot"),
                "duracion_s": t.get("duracion_s"),
                "ruta": t.get("ruta") or "",
            })
    else:
        with open(ruta, "r", encoding="utf-8", errors="replace", newline="") as fh:
            muestra = fh.read(8192)
            fh.seek(0)
            try:
                dial = csv.Sniffer().sniff(muestra, delimiters=",;\t|")
            except csv.Error:
                dial = csv.excel
            alias = {"artist": "artista", "artista": "artista",
                     "title": "titulo", "name": "titulo", "titulo": "titulo",
                     "track": "titulo", "mix": "mix", "genre": "genero",
                     "genero": "genero", "bpm": "bpm", "key": "camelot",
                     "tonality": "camelot", "location": "ruta"}
            for fila in csv.DictReader(fh, dialect=dial):
                d = {}
                for k, v in fila.items():
                    if k is None:
                        continue
                    d[alias.get(k.strip().lower(), k.strip().lower())] = (v or "").strip()
                if d.get("titulo") or d.get("artista"):
                    tracks.append(d)
    for t in tracks:
        # El BPM llega como texto desde CSV y como float desde XML: unificar,
        # porque el informe lo formatea como numero.
        if not isinstance(t.get("bpm"), float):
            try:
                t["bpm"] = float(str(t.get("bpm") or "").replace(",", ".")) or None
            except ValueError:
                t["bpm"] = None
        t["_k_art"] = _plano(t.get("artista", ""))
        t["_k_tit"] = _nucleo(t.get("titulo", ""))
        t["_k_full"] = f"{t['_k_art']} {t['_k_tit']}".strip()
    return tracks


# --------------------------------------------------------------------------
# CRUCE
# --------------------------------------------------------------------------

def _par(campo_a: str, campo_b: str, t: Dict[str, object]) -> float:
    """Puntua asumiendo campo_a=artista y campo_b=titulo."""
    s_art = _similitud(campo_a, t["_k_art"])
    s_tit = _similitud(campo_b, t["_k_tit"])
    # El titulo pesa mas: el cliente suele acertar el titulo y fallar el artista
    base = 0.65 * s_tit + 0.35 * s_art
    # Si el titulo encaja casi perfecto, un artista mal escrito no debe hundirlo
    if s_tit >= 0.95:
        base = max(base, 0.80 + 0.20 * s_art)
    return base


def _puntuar(p: Dict[str, object], t: Dict[str, object]) -> float:
    """Similitud entre una peticion y un track de la biblioteca.

    Prueba las dos lecturas del separador. Nadie escribe la lista de forma
    consistente: 'Bad Bunny - Titi' y 'Titi - Bad Bunny' aparecen en la misma
    lista del mismo cliente, asi que se puntua en ambos sentidos y se toma
    el mejor.
    """
    campo1 = _plano(str(p.get("artista", "")))
    campo2 = _plano(str(p.get("titulo", "")))
    p_full = _nucleo(str(p.get("texto", "")))

    if campo1 and campo2:
        directo = _par(campo1, _nucleo(str(p.get("titulo", ""))), t)
        invertido = _par(campo2, _nucleo(str(p.get("artista", ""))), t)
        # Aun asi se compara la linea entera: cubre el caso de titulos que
        # contienen un guion y que la division parte por la mitad.
        entero = _similitud(p_full, t["_k_full"])
        return max(directo, invertido, entero)

    return max(_similitud(p_full, t["_k_full"]), _similitud(p_full, t["_k_tit"]))


def cruzar(
    peticiones: Sequence[Dict[str, object]],
    biblioteca: Sequence[Dict[str, object]],
    umbral_seguro: float = UMBRAL_SEGURO,
    umbral_duda: float = UMBRAL_DUDA,
    max_candidatos: int = 3,
) -> Dict[str, object]:
    tengo, no_tengo, dudoso, prohibido, ignoradas = [], [], [], [], []

    for p in peticiones:
        if p.get("ignorada"):
            ignoradas.append({"linea_original": p.get("linea_original"),
                              "texto": p.get("texto")})
            continue
        puntuados = sorted(
            ((_puntuar(p, t), t) for t in biblioteca),
            key=lambda x: -x[0],
        )[:max_candidatos]
        mejor_score, mejor = (puntuados[0] if puntuados else (0.0, None))

        candidatos = [{
            "artista": t.get("artista"), "titulo": t.get("titulo"),
            "mix": t.get("mix"), "bpm": t.get("bpm"), "camelot": t.get("camelot"),
            "similitud": round(s, 3),
        } for s, t in puntuados if s >= umbral_duda]

        item = {
            "peticion": p.get("texto"),
            "linea_original": p.get("linea_original"),
            "nota": p.get("nota"),
            "candidatos": candidatos,
            "similitud": round(mejor_score, 3),
        }

        if p.get("prohibida"):
            item["encontrado_en_biblioteca"] = mejor_score >= umbral_seguro
            prohibido.append(item)
        elif mejor_score >= umbral_seguro:
            # Segundo candidato casi igual de bueno -> ambiguo, decide una persona
            if len(puntuados) > 1 and puntuados[1][0] >= mejor_score - 0.04:
                item["motivo_duda"] = ("dos o mas versiones casi identicas en "
                                       "biblioteca: elige cual va")
                dudoso.append(item)
            else:
                item["match"] = {
                    "artista": mejor.get("artista"), "titulo": mejor.get("titulo"),
                    "mix": mejor.get("mix"), "bpm": mejor.get("bpm"),
                    "camelot": mejor.get("camelot"), "genero": mejor.get("genero"),
                    "ruta": mejor.get("ruta"),
                }
                tengo.append(item)
        elif mejor_score >= umbral_duda:
            item["motivo_duda"] = ("parecido pero por debajo del umbral seguro: "
                                   "confirmalo a ojo antes de darlo por bueno")
            dudoso.append(item)
        else:
            no_tengo.append(item)

    return {
        "tengo": tengo, "no_tengo": no_tengo,
        "dudoso": dudoso, "prohibido": prohibido,
        "ignoradas": ignoradas,
        "resumen": {
            "lineas_leidas": len(peticiones),
            "peticiones_reales": len(peticiones) - len(ignoradas),
            "tengo": len(tengo), "no_tengo": len(no_tengo),
            "dudoso": len(dudoso), "prohibido": len(prohibido),
            "ignoradas": len(ignoradas),
            "tracks_en_biblioteca": len(biblioteca),
        },
        "umbrales": {"seguro": umbral_seguro, "duda": umbral_duda},
    }


def render(r: Dict[str, object]) -> str:
    L: List[str] = []
    s = r["resumen"]
    L.append(f"CRUCE DE PETICIONES — {s['peticiones_reales']} peticiones contra "
             f"{s['tracks_en_biblioteca']} tracks de biblioteca")
    L.append("")

    L.append(f"TENGO ({s['tengo']})")
    for i in r["tengo"]:
        m = i["match"]
        extra = " · ".join(x for x in [
            f"{m['bpm']:g} BPM" if m.get("bpm") else "",
            str(m.get("camelot") or ""), str(m.get("mix") or "")] if x)
        L.append(f"  · {i['peticion']}")
        L.append(f"      -> {m['artista']} — {m['titulo']}" + (f"  [{extra}]" if extra else ""))

    L.append("")
    L.append(f"NO TENGO — hay que comprarlo ({s['no_tengo']})")
    for i in r["no_tengo"]:
        L.append(f"  · {i['peticion']}" + (f"   (nota: {i['nota']})" if i.get("nota") else ""))

    L.append("")
    L.append(f"DUDOSO — decide una persona ({s['dudoso']})")
    for i in r["dudoso"]:
        L.append(f"  · {i['peticion']}  — {i.get('motivo_duda','')}")
        for c in i["candidatos"]:
            L.append(f"      ? {c['artista']} — {c['titulo']}"
                     f"{(' (' + str(c['mix']) + ')') if c.get('mix') else ''}"
                     f"   [similitud {c['similitud']}]")

    L.append("")
    L.append(f"PROHIBIDO — no debe sonar ({s['prohibido']})")
    for i in r["prohibido"]:
        estado = ("ESTA en biblioteca: sacalo de la playlist"
                  if i.get("encontrado_en_biblioteca") else
                  "no aparece en biblioteca: sin riesgo")
        L.append(f"  · {i['peticion']}  [{estado}]")

    if r.get("ignoradas"):
        L.append("")
        L.append(f"APARTADAS POR PARECER CONVERSACION ({s['ignoradas']}) — "
                 "revisa que no se haya colado una peticion real")
        for i in r["ignoradas"]:
            L.append(f"  · {i['linea_original']}")

    L.append("")
    L.append("COMO LEER ESTO")
    L.append(f"  Umbral seguro {r['umbrales']['seguro']} · umbral de duda "
             f"{r['umbrales']['duda']}. Lo que cae en DUDOSO no es un fallo: es")
    L.append("  el sistema negandose a adivinar. Reviselo antes del evento.")
    return "\n".join(L)


def _cli() -> int:
    import argparse
    import json
    p = argparse.ArgumentParser(description="cruza peticiones sucias contra tu biblioteca")
    p.add_argument("biblioteca", help="rekordbox XML o CSV")
    p.add_argument("peticiones", help="fichero de texto con la lista del cliente")
    p.add_argument("--formato", choices=["texto", "json"], default="texto")
    p.add_argument("--umbral-seguro", type=float, default=UMBRAL_SEGURO)
    p.add_argument("--umbral-duda", type=float, default=UMBRAL_DUDA)
    a = p.parse_args()

    bib = cargar_biblioteca(a.biblioteca)
    if not bib:
        print("Biblioteca vacia o ilegible.", file=sys.stderr)
        return 1
    with open(a.peticiones, "r", encoding="utf-8", errors="replace") as fh:
        pets = parsear_peticiones(fh.read())
    if not pets:
        print("No se reconocio ninguna peticion en el fichero.", file=sys.stderr)
        return 1
    r = cruzar(pets, bib, a.umbral_seguro, a.umbral_duda)
    print(json.dumps(r, ensure_ascii=False, indent=2, default=str)
          if a.formato == "json" else render(r))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
