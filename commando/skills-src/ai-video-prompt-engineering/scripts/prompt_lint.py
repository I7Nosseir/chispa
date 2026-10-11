#!/usr/bin/env python3
"""Checks an AI video/image prompt against the skill's rules before credits are spent.

Usage: python3 prompt_lint.py prompt.txt [--image]      (or pipe text: ... | python3 prompt_lint.py -)
Exit code 1 if any ERROR is found.

Rules checked (SKILL.md section in brackets):
  ERROR  vague quantities ("a few", "some", "several", "a couple")        [§3]
  ERROR  orbit/circle camera language without the ring/halo guard          [§7]
  ERROR  "replace/swap/transforms into" product logic                      [§5]
  ERROR  missing NEGATIVE PROMPT                                           [§9]
  ERROR  video prompt missing SCENE / CHARACTERS / BEATS / CAMERA / STYLE  [§1]
  WARN   explosive verbs next to containment words                         [§6]
  WARN   beats with more than one action ("and then", two verbs joined)    [§2]
  WARN   product mentioned without a reference Element / exact variant     [§4, §10]
  WARN   real luxury brand names used as aesthetic shorthand               [§10]
  WARN   dialogue/speech in a clip that also needs identity lock           [§8]
  WARN   over 2,500 characters                                             [§13]
  WARN   no capture device / lens / light source named                     [realism card]
"""
import re
import sys

VAGUE = r"\b(a few|few|some|several|a couple( of)?|many|a bunch of|lots of|numerous)\b"
EXPLOSIVE = r"\b(explod\w*|burst\w*|pops?\b|popping|slam\w*|blast\w*|shatter\w*|erupt\w*|launch\w*|smash\w*|crash\w*)"
CONTAIN = r"\b(stay\w* (in place|still|put)|don't move|remain\w* (still|in place)|not scatter|no scatter\w*)"
LUXURY = r"\b(rolls[- ]royce|lamborghini|ferrari|louis vuitton|gucci|chanel|dior|hermes|hermès|rolex|cartier|apple logo)\b"
DEVICE = r"\b(\d{2,3}\s?mm|iphone|front cam\w*|sony|canon|arri|fx3|macro|f/\d)"
LIGHT = r"\b(light|sun|window|lamp|fluorescent|softbox|ring light|daylight)\b"


def lint(text, image=False):
    issues = []
    low = text.lower()
    neg_idx = low.find("negative")

    def err(m):
        issues.append(("ERROR", m))

    def warn(m):
        issues.append(("WARN", m))

    for m in re.finditer(VAGUE, low):
        if neg_idx != -1 and m.start() > neg_idx:
            continue
        ctx = text[max(0, m.start() - 25):m.end() + 25].replace("\n", " ")
        err(f'§3 vague quantity "{m.group(0)}" → give an exact number: …{ctx}…')

    if re.search(r"\b(orbit\w*|circl\w* (around|the)|360)\b", low) and not re.search(r"\b(no ring|no halo|no portal)\b", low):
        err("§7 orbit/circle used without guard: add 'camera motion only — no ring, halo, portal or circular object' (+ negative)")

    if re.search(r"\b(replac\w*|swap\w*|transforms? into|turns? into|morphs? into)\b", low):
        err("§5 replace/transform logic detected: make the product 'already there', or stage a visible causal event")

    if neg_idx == -1:
        err("§9 no NEGATIVE PROMPT section")

    if not image:
        for key in ("scene", "characters", "beats", "camera", "style"):
            if not re.search(rf"^\s*{key}\s*:", low, re.M):
                err(f"§1 missing '{key.upper()}:' block (use --image for stills)")
        beats = re.findall(r"^\s*\d+(\.\d+)?\s*-\s*\d+(\.\d+)?\s*s\s*:(.*)$", text, re.M)
        for b in beats:
            line = b[2].lower()
            if re.search(r"\b(and then|then)\b", line) or len(re.findall(r",\s*(and\s+)?\w+s\b", line)) >= 2:
                warn(f"§2 beat may hold more than one action → split it: {b[2].strip()[:90]}")
        if re.search(r"\b(says|speaks|talks|dialogue|line:|\"[^\"]{6,}\")", low) and re.search(r"identity lock|reference image|@\w+", low):
            warn("§8 speech + identity lock: dialogue is the main cause of face drift — prefer silent clip + separate VO")

    if re.search(EXPLOSIVE, low) and re.search(CONTAIN, low):
        warn("§6 explosive verb next to a containment constraint — the explosive verb usually wins; use calm verbs")

    if re.search(r"\b(product|bottle|can|box|jar|pack|abaya|necklace|serum|perfume)\b", low) and not re.search(r"(@\w+|reference|exact)", low):
        warn("§4/§10 product without a reference Element or exact variant — upload the real photo and name the variant")

    for m in re.finditer(LUXURY, low):
        warn(f'§10 brand name "{m.group(0)}" as style shorthand pulls its real logo — describe the aesthetic instead')

    if len(text) > 2500:
        warn(f"§13 {len(text)} characters — many tools cap near 2,500; trim boilerplate, keep beat detail")

    if not re.search(DEVICE, low):
        warn("realism: no capture device or lens named (iPhone front cam, 35mm, 90mm macro…)")
    if not re.search(LIGHT, low):
        warn("realism: no light source/direction named")
    return issues


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    image = "--image" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(2)
    text = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    issues = lint(text, image)
    for level, msg in issues:
        print(f"{level:5}  {msg}")
    n_err = sum(1 for lvl, _ in issues if lvl == "ERROR")
    print(f"\n{n_err} error(s), {len(issues) - n_err} warning(s), {len(text)} chars")
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
