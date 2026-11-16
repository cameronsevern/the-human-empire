"""Place images in a chapter, then delete unused image files and ledger rows.
Any image the chapter already shows is kept.

    from place import place
    place("chapters/10-wheel", [(anchor, file, alt, caption), ...])

Each image goes after the paragraph that starts with `anchor`.
"""
import os
import re


def place(folder, items):
    p = os.path.join(folder, "chapter.md")
    paras = open(p).read().split("\n\n")
    for anchor, f, alt, cap in items:
        assert os.path.exists(os.path.join(folder, "images", f)), f
        hits = [i for i, x in enumerate(paras) if x.startswith(anchor)]
        assert len(hits) == 1, (anchor, len(hits))
        paras.insert(hits[0] + 1, f"![{alt}](images/{f})\n*{cap}*")
    open(p, "w").write("\n\n".join(paras))
    keep = {f for _, f, _, _ in items}
    # files the chapter already uses (drawn maps, charts, diagrams) stay
    keep |= set(re.findall(r"\]\(images/([^)]+)\)", "\n\n".join(paras)))
    d = os.path.join(folder, "images")
    for x in os.listdir(d):
        if x != "ledger.md" and x not in keep:
            os.remove(os.path.join(d, x))
    lp = os.path.join(d, "ledger.md")
    out = []
    for line in open(lp).read().split("\n"):
        cells = [c.strip() for c in line.split("|")]
        if line.startswith("|") and len(cells) > 2 and "." in cells[1] and cells[1] not in keep and not cells[1].lower().startswith("file"):
            continue
        out.append(line)
    open(lp, "w").write("\n".join(out))
    print(folder, len(items), "images placed;", sorted(os.listdir(d)))
