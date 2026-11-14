#!/usr/bin/env python3
"""Build an EPUB of the chapters written so far.

    uv run --with markdown build/epub.py 1 7 "Part I: Origins"

Arguments: first chapter, last chapter, and a subtitle for this edition.
Each chapter is followed by its
tool page. Images are shrunk to 1400 px so the file stays small.
Output: build/the-human-empire-chNN-NN.epub (the PDF comes from build/pdf.py)
"""
import datetime, glob, html, os, re, subprocess, sys, uuid, zipfile
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
first, last = int(sys.argv[1]), int(sys.argv[2])
subtitle = sys.argv[3] if len(sys.argv) > 3 else f"Chapters {first} to {last}"
TITLE, AUTHOR = "The Human Empire", "Claude and Cameron Severn"
WORK = os.path.join(ROOT, "build", "work")
# Smaller files for sending: IMG_MAX=1000 IMG_Q=68 uv run ...
IMG_MAX, IMG_Q = os.environ.get("IMG_MAX", "1400"), os.environ.get("IMG_Q", "82")
os.makedirs(os.path.join(WORK, "img"), exist_ok=True)

CSS = """
body { font-family: serif; line-height: 1.5; }
h1 { font-size: 1.6em; margin: 2em 0 0.3em; line-height: 1.2; }
h2 { font-size: 1.15em; margin: 2em 0 0.5em; }
p { margin: 0 0 0.9em; }
p.where { font-style: italic; color: #555; margin-bottom: 2em; }
figure { margin: 1.5em 0; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; height: auto; }
figcaption { font-size: 0.82em; font-style: italic; color: #555; text-align: left; margin-top: 0.4em; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.9em; }
td { border-top: 1px solid #bbb; padding: 0.4em 0.5em; vertical-align: top; }
td:first-child { width: 28%; }
div.tool { border-top: 3px solid #b5523b; padding-top: 0.5em; }
p.kicker { text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.75em; color: #b5523b; margin: 2em 0 0; }
div.tool h1 { margin-top: 0.2em; }
div.titlepage { text-align: center; margin-top: 25%; }
div.titlepage h1 { font-size: 2.2em; }
"""

images = {}  # source path -> name inside the book


def shrink(src):
    if src not in images:
        name = f"i{len(images):03d}.jpg"
        subprocess.run(
            ["magick", src + "[0]", "-background", "white", "-flatten",
             "-resize", f"{IMG_MAX}x{IMG_MAX}>", "-quality", IMG_Q, "-strip",
             os.path.join(WORK, "img", name)], check=True)
        images[src] = name
    return images[src]


def to_xhtml(md_text, folder):
    body = markdown.markdown(md_text, extensions=["tables"], output_format="xhtml")

    def img(m):
        src = os.path.normpath(os.path.join(folder, html.unescape(m.group(2))))
        return f'<img alt="{m.group(1)}" src="img/{shrink(src)}" />'

    body = re.sub(r'<img alt="([^"]*)" src="([^"]*)" />', img, body)
    body = re.sub(r'<p>(<img [^>]*/>)\s*<em>(.*?)</em></p>',
                  r'<figure>\1<figcaption>\2</figcaption></figure>', body, flags=re.S)
    body = re.sub(r'<p>(<img [^>]*/>)</p>', r'<figure>\1</figure>', body)
    body = re.sub(r'<thead>.*?</thead>', '', body, flags=re.S)
    return body


def page(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">\n'
            f'<head><meta charset="utf-8" /><title>{html.escape(title)}</title>'
            '<link rel="stylesheet" type="text/css" href="style.css" /></head>\n'
            f'<body>\n{body}\n</body></html>\n')


def heading(md_text):
    return re.match(r'# (.*)', md_text).group(1).strip()


docs = []  # (file name, toc title, xhtml)

docs.append(("title.xhtml", TITLE, page(TITLE,
    f'<div class="titlepage"><h1>{TITLE}</h1><p>{html.escape(subtitle)}</p>'
    f'<p>{AUTHOR}</p><p><em>Draft of {datetime.date.today():%-d %B %Y}</em></p></div>')))

plan = open(os.path.join(ROOT, "the_human_empire.md")).read()
preface = re.search(r'## Preface\n(.*?)\n## ', plan, re.S).group(1)
# No preface for now: it will be rewritten before release.
# docs.append(("preface.xhtml", "Preface", page("Preface", "<h1>Preface</h1>" + to_xhtml(preface, ROOT))))

for n in range(first, last + 1):
    folder = glob.glob(os.path.join(ROOT, "chapters", f"{n:02d}-*"))[0]
    text = open(os.path.join(folder, "chapter.md")).read()
    body = to_xhtml(text, folder)
    body = re.sub(r'(</h1>\s*)<p><em>(.*?)</em></p>', r'\1<p class="where">\2</p>', body, count=1, flags=re.S)
    docs.append((f"ch{n:02d}.xhtml", heading(text), page(heading(text), body)))

    # a chapter may be followed by several tool pages
    for k, tdir in enumerate(sorted(glob.glob(os.path.join(ROOT, "toolbox", f"{n:02d}-*")))):
        if not os.path.exists(os.path.join(tdir, "profile.md")):
            continue
        text = open(os.path.join(tdir, "profile.md")).read()
        body = '<div class="tool">' + to_xhtml(text, tdir) + '</div>'
        docs.append((f"tool{n:02d}{'abcdef'[k]}.xhtml", heading(text), page(heading(text), body)))

# cover
cover = os.path.join(WORK, "img", "cover.jpg")
# The designed PDF of the same chapters carries the real cover; use it when it has been built, and a plain one otherwise.
designed = os.path.join(ROOT, "build", f"the-human-empire-ch{first:02d}-{last:02d}-designed.pdf")
if os.path.exists(designed):
    subprocess.run(["pdftoppm", "-f", "1", "-l", "1", "-scale-to-x", "1600", "-scale-to-y", "-1", "-jpeg",
                    "-singlefile", designed, cover[:-4]], check=True)
else:
    subprocess.run(["magick", "-size", "1600x2400", "xc:#faf6ee",
                    "-font", "Liberation-Serif", "-fill", "#2f2a26", "-gravity", "north",
                    "-pointsize", "150", "-annotate", "+0+700", "The Human\nEmpire",
                    "-fill", "#b5523b", "-pointsize", "64", "-annotate", "+0+1150", subtitle,
                    "-fill", "#2f2a26", "-pointsize", "70", "-annotate", "+0+2050", AUTHOR,
                    "-quality", "88", cover], check=True)
docs.insert(0, ("cover.xhtml", "Cover", page("Cover",
    '<figure style="margin:0"><img alt="The Human Empire" src="img/cover.jpg" /></figure>')))

nav = ('<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>' +
       "".join(f'<li><a href="{f}">{html.escape(t)}</a></li>' for f, t, _ in docs[2:]) +
       '</ol></nav>')
docs.insert(2, ("nav.xhtml", "Contents", page("Contents", nav)))

manifest = ['<item id="css" href="style.css" media-type="text/css" />',
            '<item id="cover-img" href="img/cover.jpg" media-type="image/jpeg" properties="cover-image" />']
for f, _, _ in docs:
    prop = ' properties="nav"' if f == "nav.xhtml" else ""
    manifest.append(f'<item id="{f[:-6]}" href="{f}" media-type="application/xhtml+xml"{prop} />')
for name in sorted(images.values()):
    manifest.append(f'<item id="{name[:-4]}" href="img/{name}" media-type="image/jpeg" />')
spine = "".join(f'<itemref idref="{f[:-6]}" />' for f, _, _ in docs)
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="id">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="id">urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, "the-human-empire")}</dc:identifier>
<dc:title>{TITLE}</dc:title><dc:creator>{AUTHOR}</dc:creator><dc:language>en</dc:language>
<meta property="dcterms:modified">{now}</meta><meta name="cover" content="cover-img" />
</metadata>
<manifest>{"".join(manifest)}</manifest>
<spine>{spine}</spine>
</package>'''

out = os.path.join(ROOT, "build", f"the-human-empire-ch{first:02d}-{last:02d}.epub")
with zipfile.ZipFile(out, "w") as z:
    z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
    z.writestr("META-INF/container.xml",
               '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
               '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>',
               zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/content.opf", opf, zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/style.css", CSS, zipfile.ZIP_DEFLATED)
    for f, _, x in docs:
        z.writestr("OEBPS/" + f, x, zipfile.ZIP_DEFLATED)
    for name in ["cover.jpg"] + sorted(images.values()):
        z.write(os.path.join(WORK, "img", name), "OEBPS/img/" + name, zipfile.ZIP_STORED)
print(out, f"{os.path.getsize(out)/1e6:.1f} MB,", len(docs), "pages,", len(images), "images")

# The PDF is made separately, by build/pdf.py.
