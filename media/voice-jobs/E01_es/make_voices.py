#!/usr/bin/env python3
"""Genera las voces de plan.json con VoiceStudio (OmniVoice) y las mezcla sobre el video.

Requiere el backend de VoiceStudio corriendo (por defecto http://127.0.0.1:3900) y ffmpeg.
Solo usa la librería estándar. Uso:

    python3 make_voices.py [--steps 32] [--takes 3] [--api http://127.0.0.1:3900]
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


def generate(api, text, instruct, seed, steps, duration=None):
    form = {"text": text, "language": "es", "instruct": instruct,
            "seed": str(seed), "num_step": str(steps)}
    if duration:
        form["duration"] = f"{duration:.2f}"
    req = urllib.request.Request(f"{api}/generate", data=urllib.parse.urlencode(form).encode())
    t0 = time.time()
    # La primera llamada descarga el modelo (~2.4 GB): timeout amplio.
    with urllib.request.urlopen(req, timeout=3600) as r:
        return r.read(), time.time() - t0


def synth_lines(plan, api, steps, takes, out):
    report = []
    for line in plan["lines"]:
        voice = plan["voices"][line["voice"]]
        window = line["end"] - line["start"]
        best = None
        # Varias tomas (seed base + i); se queda con la más larga que quepa en la ventana:
        # las tomas muy cortas suelen sonar atropelladas.
        for i in range(takes):
            seed = voice["seed"] + i
            audio, secs = generate(api, line["text"], voice["instruct"], seed, steps)
            tmp = out / f"{line['id']}_take{i}.wav"
            tmp.write_bytes(audio)
            dur = wav_duration(tmp)
            print(f"  {line['id']} take {i} seed={seed}: {dur:.2f}s (ventana {window:.2f}s) en {secs:.0f}s")
            fits = dur <= window * 0.95
            if best is None or (fits and (not best["fits"] or dur > best["dur"])):
                best = {"path": tmp, "dur": dur, "seed": seed, "fits": fits, "gen_s": secs}
        if not best["fits"]:
            # Ninguna toma cabe: forzar duración con la seed de la mejor toma.
            target = window * 0.9
            audio, secs = generate(api, line["text"], voice["instruct"], best["seed"], steps, target)
            best["path"].write_bytes(audio)
            best.update(dur=wav_duration(best["path"]), fits=True, gen_s=secs, forced=round(target, 2))
            print(f"  {line['id']} forzada a {target:.2f}s")
        final = out / f"{line['id']}.wav"
        best["path"].replace(final)
        for f in out.glob(f"{line['id']}_take*.wav"):
            f.unlink()
        report.append({"id": line["id"], "voice": line["voice"], "text": line["text"],
                       "seed": best["seed"], "duration_s": round(best["dur"], 2),
                       "window_s": round(window, 2), "gen_time_s": round(best["gen_s"], 1),
                       **({"forced_duration_s": best["forced"]} if "forced" in best else {})})
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
    inputs += ["-f", "lavfi", "-i", "sine=f=880:d=0.45,afade=t=out:st=0.05:d=0.4",
               "-f", "lavfi", "-i", "sine=f=698:d=0.7,afade=t=out:st=0.05:d=0.65",
               "-f", "lavfi", "-i", "anoisesrc=d=0.9:c=brown:a=0.9,lowpass=f=180,afade=t=out:st=0.05:d=0.85"]
    for k, sfx in enumerate(plan["sfx"]):
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
    ap.add_argument("--takes", type=int, default=3, help="tomas por línea (seeds consecutivas)")
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
