#!/usr/bin/env python3
"""Genera las voces de plan.json con VoiceStudio (OmniVoice) y las mezcla sobre el video.

Requiere el backend de VoiceStudio corriendo (por defecto http://127.0.0.1:3900) y ffmpeg.
Solo usa la librería estándar. Uso:

    python3 make_voices.py [--steps 32] [--takes 1] [--api http://127.0.0.1:3900]
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent


def wav_duration(path):
    with wave.open(str(path)) as w:
        return w.getnframes() / w.getframerate()


MAX_ATEMPO = 1.25


def generate(api, text, instruct, seed, steps, duration=None):
    """Devuelve (wav_bytes, segundos, n_fragmentos_descartados)."""
    # effect_preset=raw: sin DSP en el backend; el procesado lo hace mix() una sola vez.
    form = {"text": text, "language": "es", "instruct": instruct,
            "seed": str(seed), "num_step": str(steps), "effect_preset": "raw"}
    if duration:
        form["duration"] = f"{duration:.2f}"
    req = urllib.request.Request(f"{api}/generate", data=urllib.parse.urlencode(form).encode())
    t0 = time.time()
    try:
        # La primera llamada descarga el modelo (~2.4 GB): timeout amplio.
        with urllib.request.urlopen(req, timeout=3600) as r:
            dropped = int(r.headers.get("X-OmniVoice-Dropped-Chunks") or 0)
            return r.read(), time.time() - t0, dropped
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            body = json.loads(body).get("detail", body)
        except ValueError:
            pass
        sys.exit(f"VoiceStudio respondió {e.code} en /generate: {body}\n"
                 "Revisa el log del backend (~/VoiceStudio/backend.log).")


def atempo(path, factor):
    """Acelera el WAV in situ sin cambiar el tono."""
    tmp = path.with_suffix(".atempo.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path),
                    "-af", f"atempo={factor:.4f}", str(tmp)], check=True)
    tmp.replace(path)


def synth_lines(plan, api, steps, takes, out):
    report = []
    for line in plan["lines"]:
        voice = plan["voices"][line["voice"]]
        window = line["end"] - line["start"]
        limit = window * 0.95
        best = None
        # Varias tomas (seed base + i); se queda con la más larga que quepa en la ventana:
        # las tomas muy cortas suelen sonar atropelladas.
        for i in range(takes):
            seed = voice["seed"] + i
            audio, secs, dropped = generate(api, line["text"], voice["instruct"], seed, steps)
            tmp = out / f"{line['id']}_take{i}.wav"
            tmp.write_bytes(audio)
            dur = wav_duration(tmp)
            print(f"  {line['id']} take {i} seed={seed}: {dur:.2f}s (ventana {window:.2f}s) en {secs:.0f}s"
                  + (f"  ¡{dropped} fragmento(s) de texto sin audio!" if dropped else ""))
            # Una toma que perdió texto solo se usa si no hay otra.
            fits = dur <= limit and not dropped
            if best is None or (fits and (not best["fits"] or dur > best["dur"])):
                best = {"path": tmp, "dur": dur, "seed": seed, "fits": fits, "gen_s": secs,
                        "dropped": dropped}
        if not best["fits"]:
            # Ninguna toma cabe: forzar duración con la seed de la mejor toma.
            target = window * 0.9
            audio, secs, dropped = generate(api, line["text"], voice["instruct"], best["seed"], steps, target)
            best["path"].write_bytes(audio)
            best.update(dur=wav_duration(best["path"]), gen_s=secs, dropped=dropped,
                        forced=round(target, 2))
            print(f"  {line['id']} forzada a {target:.2f}s -> {best['dur']:.2f}s")
        if best["dur"] > limit:
            # Sigue sin caber: acelerar hasta MAX_ATEMPO (receta del plan).
            factor = min(best["dur"] / limit, MAX_ATEMPO)
            atempo(best["path"], factor)
            best.update(dur=wav_duration(best["path"]), atempo=round(factor, 3))
            print(f"  {line['id']} atempo {factor:.3f} -> {best['dur']:.2f}s")
        if best["dur"] > window:
            print(f"  AVISO {line['id']}: {best['dur']:.2f}s no cabe en {window:.2f}s; se solapará")
        if best["dropped"]:
            print(f"  AVISO {line['id']}: el backend descartó texto; escúchala")
        final = out / f"{line['id']}.wav"
        best["path"].replace(final)
        for f in out.glob(f"{line['id']}_take*.wav"):
            f.unlink()
        report.append({"id": line["id"], "voice": line["voice"], "text": line["text"],
                       "seed": best["seed"], "duration_s": round(best["dur"], 2),
                       "window_s": round(window, 2), "gen_time_s": round(best["gen_s"], 1),
                       **({"forced_duration_s": best["forced"]} if "forced" in best else {}),
                       **({"atempo": best["atempo"]} if "atempo" in best else {}),
                       **({"dropped_chunks": best["dropped"]} if best["dropped"] else {})})
    return report


def mix(plan, out, video, dest):
    inputs, filt, labels = [], [], []
    for i, line in enumerate(plan["lines"]):
        d = int(line["start"] * 1000)
        inputs += ["-i", str(out / f"{line['id']}.wav")]
        filt.append(f"[{i}:a]aresample=48000,highpass=f=80,"
                    f"acompressor=threshold=-18dB:ratio=3:attack=5:release=80,adelay={d}|{d}[v{i}]")
        labels.append(f"[v{i}]")
    n = len(plan["lines"])
    for k, sfx in enumerate(plan["sfx"]):
        # Cada efecto se sintetiza desde su propia entrada del plan (campo "lavfi").
        inputs += ["-f", "lavfi", "-i", sfx["lavfi"]]
        d = int(sfx["at"] * 1000)
        filt.append(f"[{n + k}:a]aresample=48000,volume={sfx['gain']},adelay={d}|{d}[s{k}]")
        labels.append(f"[s{k}]")
    total = plan["duration_s"]
    filt.append("".join(labels) + f"amix=inputs={len(labels)}:duration=longest:normalize=0,"
                f"apad=whole_dur={total + 0.1},loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[out]")
    mixwav = out / "mix.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt),
                    "-map", "[out]", "-ac", "2", str(mixwav)], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(mixwav),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-t", str(total), str(dest)], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--api", default="http://127.0.0.1:3900")
    ap.add_argument("--steps", type=int, default=32, help="8 borrador · 16 equilibrado · 32 calidad")
    # 1 toma = siempre la seed del personaje, misma voz en todas sus líneas.
    # Más tomas prueban seed+1, seed+2…, que pueden cambiar el timbre.
    ap.add_argument("--takes", type=int, default=1,
                    help="tomas por línea (seeds consecutivas; >1 puede cambiar la voz entre líneas)")
    args = ap.parse_args()

    plan = json.loads((HERE / "plan.json").read_text())
    out = HERE / "lines"
    out.mkdir(exist_ok=True)
    try:
        urllib.request.urlopen(f"{args.api}/health", timeout=5)
    except (urllib.error.URLError, OSError):
        sys.exit(f"El backend de VoiceStudio no responde en {args.api}/health. Arráncalo primero.")

    print(f"Generando {len(plan['lines'])} líneas (steps={args.steps}, takes={args.takes})...")
    report = synth_lines(plan, args.api, args.steps, args.takes, out)
    dest = HERE / "E01_es_voicestudio.mp4"
    mix(plan, out, HERE / plan["video"], dest)
    (out / "report.json").write_text(json.dumps(
        {"steps": args.steps, "takes": args.takes,
         "voices": {k: v for k, v in plan["voices"].items() if not k.startswith("_")},
         "lines": report}, ensure_ascii=False, indent=2))
    print(f"\nListo: {dest}\nDetalle por línea: {out / 'report.json'}")


if __name__ == "__main__":
    main()
