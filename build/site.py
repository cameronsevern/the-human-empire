#!/usr/bin/env python3
"""Fill the website with the released parts.

    python3 build/site.py

For each part that has a designed PDF in build/, this renders every page to an
image for the 3D reader (site/pages/<n>/001.webp ...), copies the PDF and EPUB
to site/downloads/, and writes site/parts.json, which the page reads.
The page images and downloads are build outputs and are not committed.
"""
import glob, json, os, re, shutil, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
DPI = 170          # A5 at 170 dpi is about 990 x 1405 pixels: sharp when a page fills the screen

RELEASED = {1, 2}    # parts that are public on the site; add a number here when a part is ready

PARTS = [
    (1, "I", "Origins", (1, 7)),
    (2, "II", "Conquest", (8, 22)),
    (3, "III", "Faith", None),
    (4, "IV", "Expansion", None),
    (5, "V", "Wealth", None),
    (6, "VI", "War", None),
    (7, "VII", "Dominion", None),
    (8, "VIII", "Decline", None),
]


def chapters(first, last, pdf):
    """Chapter titles with the PDF page each one starts on, for the reader's contents list."""
    out = []
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout.split("\f")
    for n in range(first, last + 1):
        folder = glob.glob(os.path.join(ROOT, "chapters", f"{n:02d}-*"))[0]
        title = re.sub(r"^# \d+\.\s*", "", open(os.path.join(folder, "chapter.md")).readline().strip())
        lede = open(os.path.join(folder, "chapter.md")).read().split("\n\n")[2].strip()[:40]
        key = re.sub(r"\s+", " ", lede)
        page = next((i + 1 for i, t in enumerate(text) if i > 2 and key[:25] in re.sub(r"\s+", " ", t)), None)
        out.append({"n": n, "title": title, "page": page})
    return out


data = []
for n, roman, title, span in PARTS:
    entry = {"n": n, "roman": roman, "title": title, "released": False}
    shutil.rmtree(os.path.join(SITE, "pages", str(n)), ignore_errors=True)
    for ext in ("pdf", "epub"):
        old = os.path.join(SITE, "downloads", f"the-human-empire-part-{n}.{ext}")
        if os.path.exists(old):
            os.remove(old)
    if span and n in RELEASED:
        stem = f"the-human-empire-ch{span[0]:02d}-{span[1]:02d}"
        pdf = os.path.join(ROOT, "build", stem + "-designed.pdf")
        epub = os.path.join(ROOT, "build", stem + ".epub")
        if os.path.exists(pdf):
            pages_dir = os.path.join(SITE, "pages", str(n))
            shutil.rmtree(pages_dir, ignore_errors=True)
            os.makedirs(pages_dir)
            with tempfile.TemporaryDirectory() as tmp:
                subprocess.run(["pdftoppm", "-r", str(DPI), "-png", pdf, os.path.join(tmp, "p")], check=True)
                shots = sorted(glob.glob(os.path.join(tmp, "p-*.png")))
                for i, shot in enumerate(shots, start=1):
                    subprocess.run(["magick", shot, "-quality", "80", os.path.join(pages_dir, f"{i:03d}.webp")], check=True)
            os.makedirs(os.path.join(SITE, "downloads"), exist_ok=True)
            name = f"the-human-empire-part-{n}"
            shutil.copy(pdf, os.path.join(SITE, "downloads", name + ".pdf"))
            entry.update(released=True, pages=len(shots), pdf=f"downloads/{name}.pdf",
                         chapters=chapters(span[0], span[1], pdf))
            if os.path.exists(epub):
                shutil.copy(epub, os.path.join(SITE, "downloads", name + ".epub"))
                entry["epub"] = f"downloads/{name}.epub"
            size = sum(os.path.getsize(f) for f in glob.glob(os.path.join(pages_dir, "*.webp"))) / 1e6
            print(f"Part {roman}: {len(shots)} pages, {size:.0f} MB of page images")
    data.append(entry)

json.dump(data, open(os.path.join(SITE, "parts.json"), "w"), indent=1)
print("wrote", os.path.join(SITE, "parts.json"))
