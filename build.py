"""Builds OpenDyslexic Mono from source/OpenDyslexic-Mono.glyphs into fonts/.

The source has 44 mark anchors with no name ("_") that stop fontmake, so it
goes through UFO first, those anchors are removed, then the UFO is compiled.
Run: python -m pip install -r requirements.txt, then python build.py
"""

import glob
import re
import subprocess
import sys
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent
UFO = ROOT / "build" / "OpenDyslexicMono-Regular.ufo"


def run(*args):
    subprocess.run([sys.executable, "-m", "fontmake", *args], cwd=ROOT, check=True)


run("-g", "source/OpenDyslexic-Mono.glyphs", "-o", "ufo", "--master-dir", "build")

removed = 0
for path in glob.glob(str(UFO / "glyphs" / "*.glif")):
    text = Path(path).read_text(encoding="utf-8")
    fixed, count = re.subn(r'\s*<anchor [^>]*name="_(?: [^"]*)?"/>', "", text)
    if count:
        removed += count
        Path(path).write_text(fixed, encoding="utf-8")
print(f"removed {removed} nameless anchors")

run("-u", str(UFO), "-o", "ttf", "--output-dir", "fonts")
font = TTFont(ROOT / "fonts" / "OpenDyslexicMono-Regular.ttf")
widths = {font["hmtx"][name][0] for name in font.getGlyphOrder() if font["hmtx"][name][0]}
print(f"advance widths: {sorted(widths)}")
font.flavor = "woff2"
font.save(ROOT / "fonts" / "OpenDyslexicMono-Regular.woff2")
