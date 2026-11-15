#!/usr/bin/env python3
"""Typeset chapters as a designed PDF with Typst.

    uv run --with typst build/pdf.py 12 12 "Part II: Conquest"

Everything is generated from the chapter and tool-page markdown, so the layout
survives edits: nothing is placed by hand. The design lives in build/book.typ.
Output: build/the-human-empire-chNN-NN-designed.pdf
"""
import glob, os, re, sys
import typst

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
first, last = int(sys.argv[1]), int(sys.argv[2])
subtitle = sys.argv[3] if len(sys.argv) > 3 else f"Chapters {first} to {last}"

PARTS = [(1, 7), (8, 22), (23, 39), (40, 51), (52, 70), (71, 83)]
PART_FIRST, PART_LAST = next((a, b) for a, b in PARTS if a <= first <= b)

SPECIAL = re.compile(r'([\\#$*_`<>@~\[\]])')


def esc(t):
    return SPECIAL.sub(r'\\\1', t)


def inline(t):
    """Markdown inline (bold, italic) to Typst markup."""
    out = []
    for part in re.split(r'(\*\*.+?\*\*|\*.+?\*)', t):
        if part.startswith('**') and part.endswith('**') and len(part) > 4:
            out.append('#strong[' + esc(part[2:-2]) + ']')
        elif part.startswith('*') and part.endswith('*') and len(part) > 2:
            out.append('#emph[' + esc(part[1:-1]) + ']')
        else:
            out.append(esc(part))
    s = ''.join(out)
    return re.sub(r'^([-+=/])', r'\\\1', s)


def years(where):
    """The span of a chapter in years ago, read from the line under its title."""
    vals = []
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
    for w, n in words.items():   # "seven million years ago"
        where = re.sub(rf"\b{w} million\b", f"{n} million", where)
    for num, mil in re.findall(r'([\d][\d,\.]*)\s*(million)?\s*years ago', where):
        vals.append(float(num.replace(',', '')) * (1e6 if mil else 1))
    if 'years ago' in where:
        for num in re.findall(r'from about ([\d][\d,]*) to', where):   # "from about 2,500 to about 2,400 years ago"
            vals.append(float(num.replace(',', '')))
        for num in re.findall(r'the year (\d{1,4})\b', where):       # "... to the year 337"
            vals.append(2025.0 - int(num))
    else:                                                            # plain years: "from 602 to about 750"
        for num in re.findall(r'(?<![\d,])(\d{3,4})(?![\d,])', where):
            vals.append(2025.0 - int(num))
    if 'before our species' in where:
        vals.append(6e6)
    return (max(vals), min(vals)) if vals else (0, 0)


IMG_MAX, IMG_Q = os.environ.get("IMG_MAX", "1400"), os.environ.get("IMG_Q", "82")
IMGDIR = os.path.join(ROOT, "build", "work", f"pdfimg-{IMG_MAX}-{IMG_Q}")
os.makedirs(IMGDIR, exist_ok=True)


def shrink(src):
    """A smaller JPEG copy of an image, made once and reused, so the PDF stays a sensible size."""
    import hashlib, subprocess
    out = os.path.join(IMGDIR, hashlib.md5(src.encode()).hexdigest()[:12] + ".jpg")
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        subprocess.run(["magick", src + "[0]", "-background", "white", "-flatten",
                        "-resize", f"{IMG_MAX}x{IMG_MAX}>", "-quality", IMG_Q, "-strip", out], check=True)
    return out


def blocks(md):
    return [b for b in re.split(r'\n\s*\n', md.strip()) if b.strip()]


def figure(folder, block, placement="auto"):
    m = re.match(r'!\[(.*?)\]\((.*?)\)\n?\*?(.*?)\*?$', block, re.S)
    alt, src, cap = m.group(1), m.group(2), m.group(3).strip()
    path = '/' + os.path.relpath(shrink(os.path.join(folder, src)), ROOT)
    credit = ''
    cm = re.search(r'\s((?:Photo|Map|Drawing|Diagram|Painting|Painter)[^.]*:.*)$', cap)
    if cm:
        credit, cap = cm.group(1).strip(), cap[:cm.start()].strip()
    return f'#fig("{path}", [{inline(cap)}], [{inline(credit)}], placement: {placement})\n'


def chapter(n):
    folder = glob.glob(os.path.join(ROOT, 'chapters', f'{n:02d}-*'))[0]
    bl = blocks(open(os.path.join(folder, 'chapter.md')).read())
    title = re.sub(r'^# \d+\.\s*', '', bl[0])
    where = bl[1].strip('*')
    a, b = years(where)
    # A picture that closes a chapter would float onto a page of its own.
    # Move it up two paragraphs so it shares its page with the ending.
    if bl[-1].startswith('![') and len(bl) > 8:
        bl.insert(len(bl) - 3, bl.pop())
    out = [f'#chapter({n}, [{inline(title)}], [{inline(where)}], {a}, {b})\n', f'#lede[{inline(bl[2])}]\n']
    first_para = True
    IND = '#h(1.2em)'    # a paragraph that follows a block needs its indent put back by hand
    held, indent_next = None, False   # held: a heading waiting for enough text to keep it company

    def flush():
        nonlocal held, indent_next
        if held is not None:
            out.append('#block(breakable: false, above: 8mm)[\n' + '\n'.join(held) + ']\n')   # space before a new section
            indent_next = len(held) > 1
            held = None

    for k, x in enumerate(bl[3:], start=3):
        if x.startswith('## '):
            flush()
            held = [f'#section[{inline(x[3:])}]\n']
        elif x.startswith('!['):
            flush()
            # near the end of a chapter a picture sits in the text, so it cannot float to a page by itself
            out.append(figure(folder, x, placement="none" if k >= len(bl) - 4 else "auto"))
        elif first_para:
            words = x.split(' ')
            out.append(f'#opening[{inline(" ".join(words[:4]))}][{inline(" " + " ".join(words[4:]))}]\n')
            first_para = False
        elif held is not None:
            # A heading stays on one page with at least two or three lines of what follows it,
            # so it is never stranded at the foot of a page above a single line.
            held.append(inline(x.replace('\n', ' ')) + '\n')
            if sum(len(h) for h in held[1:]) >= 150 or len(held) >= 3:
                flush()
        else:
            out.append((IND if indent_next else '') + inline(x.replace('\n', ' ')) + '\n')
            indent_next = False
    flush()
    # the closing ornament stays with the last paragraph, so it never sits alone on a page
    last = out[-1] if out[-1].startswith('#') else IND + out[-1]
    out[-1] = '#block(breakable: false)[\n' + last + '\n#tailpiece()\n]\n'
    return '\n'.join(out)


DROP = {'How it works', 'Where it went'}


def tool(n):
    """Every tool page that follows chapter n, in folder order. A chapter may have several."""
    hits = sorted(glob.glob(os.path.join(ROOT, 'toolbox', f'{n:02d}-*', 'profile.md')))
    return '\n'.join(tool_page(h) for h in hits)


def tool_page(profile):
    folder = os.path.dirname(profile)
    bl = blocks(open(profile).read())
    title = bl[0][2:]
    rows = re.findall(r'\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|', bl[1])
    card = ', '.join(f'([{inline(k)}], [{inline(v)}])' for k, v in rows)
    diagram, photo, text, skip, sect = 'none', 'none', [], False, ''
    for x in bl[2:]:
        if x.startswith('## '):
            sect = x[3:].strip()
            # a tool page is one page: the diagram's own labels say how it works
            skip = sect in DROP
            if not skip and sect != 'The real thing':
                text.append(f'#toolhead[{inline(sect)}]\n')
        elif x.startswith('!['):
            f = figure(folder, x, placement="none").strip()
            if sect == 'The real thing':
                photo = f[1:].replace('placement: none', 'placement: none, maxh: 34mm')
            else:
                diagram = re.sub(r', \[.*\], \[.*\], placement: none\)$', ', [], [], placement: none, maxh: 60mm)', f[1:])
        elif skip or sect == 'The real thing':
            continue
        else:
            text.append(inline(x.replace('\n', ' ')) + '\n')
    return f'#toolpage([{inline(title)}], ({card},), {diagram}, {photo})[\n' + '\n'.join(text) + ']\n'


# every chapter's span, so the timeline can show the whole book faintly behind the current one
spans = []
part_a, part_b = 0, 10**9
for f in sorted(glob.glob(os.path.join(ROOT, 'chapters', '[0-9][0-9]-*', 'chapter.md'))):
    n = int(os.path.basename(os.path.dirname(f))[:2])
    lines = open(f).read().split('\n')
    if len(lines) > 2 and lines[2].startswith('*'):
        a, b = years(lines[2].strip('*'))
        if a and n <= 40:
            spans.append(f'({n}, {a}, {b})')
        if a and PART_FIRST <= n <= PART_LAST:
            part_a, part_b = max(part_a, a), min(part_b, b)

body = [f'#import "book.typ": *\n#show: book.with(subtitle: [{inline(subtitle)}], spans: ({", ".join(spans)},), part: (a: {part_a}, b: {part_b}))\n']
import datetime
# No preface for now: it will be rewritten before release. book.typ still has preface() for when it returns.
from partcolours import split
_roman, _title, _colour = split(subtitle)
body.append(f'#cover("{_roman}", [{inline(_title)}], rgb("{_colour}"))\n#titlepage([{inline(subtitle)}], [Draft of {datetime.date.today():%-d %B %Y}])\n#contents()\n')
for n in range(first, last + 1):
    body.append(chapter(n))
    body.append(tool(n))

src = os.path.join(ROOT, 'build', 'work', 'book-main.typ')
os.makedirs(os.path.dirname(src), exist_ok=True)
open(src, 'w').write('\n'.join(body))
# book.typ sits beside the generated file so the import resolves
open(os.path.join(ROOT, 'build', 'work', 'book.typ'), 'w').write(open(os.path.join(ROOT, 'build', 'book.typ')).read())
# SUFFIX=-sharp names a second copy, built with larger pictures (IMG_MAX), which the site draws its page images from
out = os.path.join(ROOT, 'build', f'the-human-empire-ch{first:02d}-{last:02d}-designed{os.environ.get("SUFFIX", "")}.pdf')
# The book is set in P052, a Palatino-style face. FONT=... tries another, into a separately named file.
DEFAULT_FONT = "P052"
FONT = os.environ.get("FONT", "") or DEFAULT_FONT
if FONT != DEFAULT_FONT:
    out = out[:-4] + "-" + FONT.replace(" ", "") + ".pdf"
# wider typefaces need slightly smaller type on the one-page tool pages
TOOLSIZE = {"P052": "8.3", "C059": "8.2", "URW Bookman": "7.8", "Libertinus Serif": "8.7"}.get(FONT, "8.3")
typst.compile(src, output=out, root=ROOT, sys_inputs={"font": FONT, "toolsize": TOOLSIZE})
print(out, f'{os.path.getsize(out)/1e6:.1f} MB')
