# The Human Empire

A history of humanity told through the rise and fall of empires.

The full plan is in [the_human_empire.md](the_human_empire.md): vision, argument, all 89 chapter briefs, indexes, and how the book is made. The voice is set in [style.md](style.md). Chapter 48 is drafted as a pilot.

## Website

`site/` is a static page: eight books on a desk, and a 3D reader that opens the parts that are out.

    python3 build/site.py                         # page images, downloads and parts.json from the PDFs in build/
    python3 -m http.server 4173 --directory site  # then open http://localhost:4173

The page images, downloads and `parts.json` are build outputs and are not committed. To release a part, add its
chapter range to `PARTS` and its number to `RELEASED` in `build/site.py`, run the script again, then `build/deploy.sh` to publish. `?slow=4` on the address slows the animations.
