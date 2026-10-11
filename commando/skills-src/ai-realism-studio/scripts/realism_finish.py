#!/usr/bin/env python3
"""Adds real-camera texture to AI output so it stops looking 'too clean'.

Presets
  phone   social/UGC video: slight desaturation, phone-style noise, mild sharpening, 30 fps, social compression
  cinema  brand film: film grain, gentle softness, vignette, 24 fps, muted colour
  still   images: grain, subtle chromatic aberration, vignette, slight desaturation, JPEG ~88

Usage
  python3 realism_finish.py in.mp4 --preset phone [--out out.mp4] [--strength 1.0]
  python3 realism_finish.py in.png --preset still [--out out.jpg] [--strength 1.0]

Video audio is loudness-normalised to -14 LUFS (social). Needs ffmpeg; stills need Pillow + numpy.
"""
import argparse
import subprocess
from pathlib import Path

VIDEO_EXT = {".mp4", ".mov", ".m4v", ".webm", ".mkv"}


def video_filters(preset, s):
    if preset == "phone":
        return [
            f"eq=saturation={1 - 0.08 * s:.3f}:contrast={1 - 0.03 * s:.3f}",
            f"unsharp=5:5:{0.35 * s:.2f}",
            f"noise=alls={int(5 * s)}:allf=t",
            "fps=30",
        ], ["-c:v", "libx264", "-crf", str(int(22 + 2 * s)), "-preset", "medium"]
    if preset == "cinema":
        return [
            f"eq=saturation={1 - 0.10 * s:.3f}:contrast={1 - 0.04 * s:.3f}:brightness={0.01 * s:.3f}",
            f"gblur=sigma={0.4 * s:.2f}",
            f"noise=alls={int(7 * s)}:allf=t+u",
            "vignette=PI/5",
            "fps=24",
        ], ["-c:v", "libx264", "-crf", "18", "-preset", "slow"]
    raise SystemExit(f"preset {preset} is for stills only")


def finish_video(src, out, preset, s):
    vf, venc = video_filters(preset, s)
    has_audio = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                                "stream=index", "-of", "csv=p=0", str(src)], capture_output=True, text=True).stdout.strip()
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", ",".join(vf + ["format=yuv420p"])] + venc
    cmd += ["-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "160k"] if has_audio else ["-an"]
    cmd += ["-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)


def finish_still(src, out, s):
    import numpy as np
    from PIL import Image, ImageEnhance

    im = Image.open(src).convert("RGB")
    im = ImageEnhance.Color(im).enhance(1 - 0.07 * s)
    a = np.asarray(im).astype(np.float32)
    h, w, _ = a.shape
    # subtle chromatic aberration: shift red/blue by ~1px per 1000px
    shift = max(1, int(round(w / 1000 * s)))
    a[:, :, 0] = np.roll(a[:, :, 0], shift, axis=1)
    a[:, :, 2] = np.roll(a[:, :, 2], -shift, axis=1)
    # luminance grain
    rng = np.random.default_rng()
    a += rng.normal(0, 4.5 * s, (h, w, 1))
    # vignette
    y, x = np.ogrid[:h, :w]
    r = np.sqrt(((x - w / 2) / (w / 2)) ** 2 + ((y - h / 2) / (h / 2)) ** 2)
    a *= (1 - 0.12 * s * np.clip(r - 0.5, 0, 1) ** 1.5)[..., None]
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(out, quality=88, subsampling=0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--preset", required=True, choices=["phone", "cinema", "still"])
    ap.add_argument("--strength", type=float, default=1.0, help="0.5 = subtle, 1 = default, 1.5 = strong")
    ap.add_argument("--out")
    a = ap.parse_args()
    src = Path(a.input)
    is_video = src.suffix.lower() in VIDEO_EXT
    if is_video and a.preset == "still":
        raise SystemExit("use phone or cinema for video")
    if not is_video and a.preset != "still":
        raise SystemExit("use --preset still for images")
    out = Path(a.out) if a.out else src.with_name(f"{src.stem}_real{'.mp4' if is_video else '.jpg'}")
    (finish_video(src, out, a.preset, a.strength) if is_video else finish_still(src, out, a.strength))
    print(out)


if __name__ == "__main__":
    main()
