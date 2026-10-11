#!/usr/bin/env python3
"""Realism QA contact sheet: pulls evenly spaced frames from a clip into one labelled image,
so every frame can be checked for tells (hands, labels, face drift, warping).

Usage: python3 contact_sheet.py clip.mp4 [--frames 12] [--cols 4] [--out sheet.jpg]
Needs ffmpeg/ffprobe and Pillow.
"""
import argparse
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", str(path)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("--frames", type=int, default=12)
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--width", type=int, default=480, help="width of each thumbnail")
    ap.add_argument("--out")
    a = ap.parse_args()

    clip = Path(a.clip)
    out = Path(a.out) if a.out else clip.with_name(clip.stem + "_qa_sheet.jpg")
    dur = duration(clip)
    times = [dur * (i + 0.5) / a.frames for i in range(a.frames)]

    thumbs = []
    with tempfile.TemporaryDirectory() as td:
        for i, t in enumerate(times):
            f = Path(td) / f"{i:03d}.png"
            subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", str(clip), "-frames:v", "1",
                            "-vf", f"scale={a.width}:-2", str(f), "-y"], check=True)
            thumbs.append((t, Image.open(f).convert("RGB")))

    w, h = thumbs[0][1].size
    rows = -(-len(thumbs) // a.cols)
    pad, label = 8, 24
    sheet = Image.new("RGB", (a.cols * (w + pad) + pad, rows * (h + label + pad) + pad), (20, 20, 20))
    d = ImageDraw.Draw(sheet)
    for i, (t, im) in enumerate(thumbs):
        x = pad + (i % a.cols) * (w + pad)
        y = pad + (i // a.cols) * (h + label + pad)
        sheet.paste(im, (x, y + label))
        d.text((x + 4, y + 5), f"#{i + 1}  t={t:.2f}s", fill=(230, 230, 230))
    sheet.save(out, quality=90)
    print(f"{out}  ({len(thumbs)} frames over {dur:.2f}s)")
    print("Check each frame: hands · product/label · text · face identity · physics · light direction · background warping · skin texture")


if __name__ == "__main__":
    main()
