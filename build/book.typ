// The Human Empire: page design. Used by build/pdf.py; nothing here is placed by hand.

#let bodyfont = sys.inputs.at("font", default: "P052")
#let ink = rgb("#2f2a26")
// letterspaced capitals: works in any typeface, unlike true small capitals
#let caps(body, size: 7.4pt, tracking: 1.4pt) = text(size: size, tracking: tracking, upper(body))
#let soft = rgb("#8a8178")
#let acc = rgb("#b5523b")
#let paper = rgb("#faf6ee")
#let tint = rgb("#f3ecdd")

// state shared with the page furniture
#let cur = state("cur", (n: 0, title: [], a: 0, b: 0))
#let allspans = state("spans", ())
#let istool = state("istool", false)
#let front = state("front", true)

// ---------- ornaments, all drawn in code ----------

// a lozenge between two tapering rules
#let flourish(width: 46mm, colour: acc) = box(width: width, height: 3mm, {
  place(horizon + left, line(length: width / 2 - 3.2mm, stroke: 0.5pt + colour))
  place(horizon + right, line(length: width / 2 - 3.2mm, stroke: 0.5pt + colour))
  place(horizon + center, rotate(45deg, square(size: 1.7mm, fill: colour)))
  place(horizon + center, dx: -3.4mm, rotate(45deg, square(size: 0.9mm, fill: colour)))
  place(horizon + center, dx: 3.4mm, rotate(45deg, square(size: 0.9mm, fill: colour)))
})

// a woven band: two rows of small triangles, like the rim of a painted pot
#let band(width: 100%, colour: acc) = layout(size => {
  let w = if type(width) == ratio { size.width * width } else { width }
  let step = 2.4mm
  let n = calc.floor(w / step)
  box(width: w, height: 3.4mm, {
    place(top, line(length: w, stroke: 0.4pt + colour))
    place(bottom, line(length: w, stroke: 0.4pt + colour))
    for i in range(n) {
      place(top + left, dx: i * step + (w - n * step) / 2, dy: 0.7mm,
        polygon(fill: if calc.even(i) { colour } else { none }, stroke: 0.3pt + colour,
          (0mm, 2mm), (step / 2, 0mm), (step, 2mm)))
    }
  })
})

// the chapter number in a ring of small lozenges
#let medallion(n) = box(width: 26mm, height: 26mm, {
  place(center + horizon, circle(radius: 11mm, stroke: 0.5pt + acc))
  place(center + horizon, circle(radius: 9.6mm, stroke: 0.25pt + acc))
  for i in range(24) {
    let a = i * 15deg
    place(center + horizon, dx: 12.4mm * calc.cos(a), dy: 12.4mm * calc.sin(a),
      rotate(45deg, square(size: if calc.rem(i, 6) == 0 { 1.3mm } else { 0.7mm }, fill: acc)))
  }
  place(center + horizon, dy: -0.6mm, text(size: 25pt, fill: acc, str(n)))
})

// closes a chapter
#let tailpiece() = align(center, {
  v(3mm)
  box(width: 30mm, height: 5mm, {
    place(center + horizon, rotate(45deg, square(size: 2.2mm, stroke: 0.5pt + acc)))
    place(center + horizon, rotate(45deg, square(size: 1mm, fill: acc)))
    place(horizon + left, line(length: 11.5mm, stroke: 0.5pt + acc))
    place(horizon + right, line(length: 11.5mm, stroke: 0.5pt + acc))
    place(horizon + left, dx: 0mm, rotate(45deg, square(size: 0.9mm, fill: acc)))
    place(horizon + right, dx: 0mm, rotate(45deg, square(size: 0.9mm, fill: acc)))
  })
})

// a small corner piece for framed pages
#let corner(colour: acc) = box(width: 5mm, height: 5mm, {
  place(top + left, line(start: (0mm, 0mm), end: (5mm, 0mm), stroke: 0.6pt + colour))
  place(top + left, line(start: (0mm, 0mm), end: (0mm, 5mm), stroke: 0.6pt + colour))
  place(top + left, dx: 1.2mm, dy: 1.2mm, rotate(45deg, square(size: 1.3mm, fill: colour)))
})

// ---------- the timeline at the foot of every page ----------
// Log scale, from seven million years ago on the left to today on the right.
#let tl-pos(y, w) = {
  let lo = calc.log(50); let hi = calc.log(7000000)
  let v = calc.log(calc.max(y, 50))
  w * (hi - v) / (hi - lo)
}

#let partspan = state("partspan", (a: 0, b: 0))

// One timeline, the same on every page of the book: all of human history on a
// compressed scale, with a single marker for the chapter being read.
#let timeline() = context {
  let c = cur.get()
  layout(size => {
    let w = size.width
    let lab(body) = text(size: 5.6pt, fill: soft, tracking: 0.3pt, body)
    box(width: w, height: 8mm, {
      place(left, dy: 2.6mm, line(length: w, stroke: 0.5pt + soft))
      for (y, t) in ((7000000, "7 million"), (1000000, "1 million"), (100000, "100,000"), (10000, "10,000"), (1000, "1,000 years ago"), (50, "today")) {
        let x = tl-pos(y, w)
        place(left, dx: x, dy: 1.7mm, line(angle: 90deg, length: 1.8mm, stroke: 0.4pt + soft))
        if y == 7000000 { place(left, dy: 4.8mm, lab(t)) }
        else if y == 50 { place(left, dx: w - 12mm, dy: 4.8mm, box(width: 12mm, align(right, lab(t)))) }
        else { place(left, dx: x - 9mm, dy: 4.8mm, box(width: 18mm, align(center, lab(t)))) }
      }
      if c.a > 0 {
        let x1 = tl-pos(c.a, w); let x2 = tl-pos(c.b, w)
        place(left, dx: x1, dy: 1.5mm, rect(width: calc.max(x2 - x1, 1.4mm), height: 2.2mm, fill: acc))
      }
    })
  })
}

// ---------- the book ----------
#let book(subtitle: [], spans: (), part: (a: 0, b: 0), body) = {
  set document(title: "The Human Empire", author: "Claude and Cameron Severn")
  set text(font: bodyfont, size: 10.2pt, fill: ink, lang: "en")
  set par(justify: true, leading: 0.68em, spacing: 0.68em, first-line-indent: (amount: 1.2em, all: false))
  set page(
    width: 148mm, height: 210mm,
    margin: (top: 17mm, bottom: 24mm, inside: 17mm, outside: 15mm),
    fill: paper,
    header: context {
      let c = cur.get()
      let pg = counter(page).get().first()
      if c.n > 0 and not front.get() and query(selector(<chapter-start>).or(selector(<tool-start>))).filter(m => m.location().page() == here().page()).len() == 0 {
        set text(fill: soft)
        // the words sit on the rule: text first, then the line 1.3 mm beneath it
        stack(dir: ttb, spacing: 1.3mm,
          grid(columns: (auto, 1fr, auto), align: (left, center, right),
            caps(size: 6.2pt)[The Human Empire], [], caps(size: 6.2pt, c.title)),
          line(length: 100%, stroke: 0.3pt + soft))
      }
    },
    footer: context {
      let pg = counter(page).get().first()
      if front.get() { return }
      grid(columns: (1fr, 9mm), column-gutter: 4mm, align: (left + horizon, right + top),
        timeline(),
        text(size: 9pt, fill: ink, weight: "bold", str(pg)))
    },
    footer-descent: 6mm,
  )
  allspans.update(spans)
  partspan.update(part)
  body
}

// chapter opening: numeral, question, place and time, ornament
#let chapter(n, title, where, a, b) = {
  pagebreak(weak: true)
  istool.update(false)
  cur.update((n: n, title: title, a: a, b: b))
  context { if front.get() { counter(page).update(1) } }
  front.update(false)
  [#metadata((n: n, title: title)) <chapter-start>]
  v(6mm)
  align(center, {
    band(width: 100%)
    v(5mm)
    medallion(n)
    v(3mm)
    block(width: 88%, par(justify: false, leading: 0.5em, text(size: 21pt, weight: "regular", title)))
    v(2.5mm)
    flourish()
    v(1.5mm)
    block(width: 80%, par(justify: false, text(size: 9pt, style: "italic", fill: soft, where)))
    v(4mm)
  })
}

// the answer: the chapter's first line, set large
#let lede(body) = {
  block(width: 100%, inset: (x: 5mm), par(justify: false, first-line-indent: 0pt, leading: 0.62em,
    text(size: 12.6pt, style: "italic", body)))
  v(3mm)
}

// the first paragraph of the story: a raised initial run in small capitals
// the first paragraph of the story: a raised initial in colour, then a run of capitals
#let plain(c) = {
  if c.has("text") { c.text }
  else if c.has("children") { c.children.map(plain).join() }
  else if c.func() == smartquote { if c.double { "\u{201D}" } else { "\u{2019}" } }
  else if c == [ ] { " " }
  else { "" }
}
#let opening(lead, rest) = context {
  let t = plain(lead)
  par(first-line-indent: 0pt)[#text(size: 27pt, fill: acc, baseline: 0pt, t.first())#caps(size: 8.4pt, tracking: 1pt, t.slice(1))#rest]
}

#let section(title) = {
  // clear space above a section heading, so the old section visibly ends before the new one starts
  block(width: 100%, sticky: true, above: 8mm, below: 3.2mm, align(center, {
    caps(size: 8.6pt, tracking: 1.8pt, title)
    v(-1.6mm)
    flourish(width: 22mm, colour: soft)
  }))
}

// a figure floats to the top or bottom of a page, so text fills the space around it.
// Tall pictures are capped in height and centred.
#let figbody(path, caption, credit, maxh: 78mm) = block(width: 100%, layout(size => {
  let full = measure(image(path, width: size.width))
  let img = if full.height > maxh { image(path, height: maxh) } else { image(path, width: size.width) }
  let line-of(body) = block(width: size.width, align(center, par(justify: false, first-line-indent: 0pt, leading: 0.45em, body)))
  // picture, then the credit centred directly beneath it, then the caption
  let parts = (align(center, block(clip: true, radius: 1pt, stroke: 0.4pt + soft, img)),)
  if credit != [] { parts.push(line-of(text(size: 5.8pt, fill: soft, tracking: 0.3pt, credit))) }
  if caption != [] { parts.push(line-of(text(size: 8pt, style: "italic", caption))) }
  stack(dir: ttb, spacing: 1.3mm, ..parts)
}))

#let fig(path, caption, credit, placement: auto, maxh: 78mm) = {
  if placement == none { figbody(path, caption, credit, maxh: maxh) }
  else { place(auto, float: true, clearance: 4mm, figbody(path, caption, credit, maxh: maxh)) }
}

// ---------- tool page: always one page ----------
#let toolhead(title) = {
  v(2.5mm, weak: true)
  block(sticky: true, text(fill: acc, caps(size: 6.8pt, tracking: 1.6pt, title)))
  v(1.2mm, weak: true)
}

#let steps(..items) = {
  set text(size: 8.6pt)
  for (i, it) in items.pos().enumerate() {
    grid(columns: (5mm, 1fr), column-gutter: 1mm,
      box(circle(radius: 2mm, stroke: 0.5pt + ink, align(center + horizon, text(size: 7pt, weight: "bold", str(i + 1))))),
      par(justify: false, first-line-indent: 0pt, leading: 0.52em, it))
    v(-1.3mm)
  }
}

#let toolpage(title, card, diagram, photo, body) = {
  pagebreak(weak: true)
  istool.update(true)
  [#metadata((n: 0, title: title)) <tool-start>]
  let inner = {
    set par(first-line-indent: 0pt, leading: 0.55em, spacing: 0.85em, justify: true)
    set text(size: float(sys.inputs.at("toolsize", default: "8.3")) * 1pt)
    align(center, {
      text(size: 19pt, title)
      v(-1mm)
      flourish(width: 34mm)
    })
    v(1mm)
    grid(columns: card.len(), column-gutter: 2.2mm,
      ..card.map(r => block(width: 100%, {
        text(fill: acc, caps(size: 5.4pt, tracking: 1pt, r.at(0)))
        v(-0.6mm)
        par(justify: false, leading: 0.45em, text(size: 7.2pt, r.at(1)))
      })))
    v(1mm)
    line(length: 100%, stroke: 0.4pt + soft)
    v(0.5mm)
    diagram
    v(1mm)
    if photo == none { body } else { grid(columns: (1fr, 31%), column-gutter: 4mm, body, photo) }
  }
  // A tool page is exactly one page. If the text is too long, say so loudly in the PDF.
  layout(size => {
    let need = measure(block(width: size.width - 10mm, inner)).height + 10mm
    block(width: 100%, height: 100%, fill: tint, stroke: 0.6pt + ink, inset: 5mm, clip: true, {
      place(top + left, dx: -3.6mm, dy: -3.6mm, rect(width: size.width - 2.8mm, height: size.height - 2.8mm, stroke: 0.3pt + acc))
      place(top + left, dx: -3.6mm, dy: -3.6mm, corner())
      place(top + right, dx: 3.6mm, dy: -3.6mm, rotate(90deg, corner()))
      place(bottom + right, dx: 3.6mm, dy: 3.6mm, rotate(180deg, corner()))
      place(bottom + left, dx: -3.6mm, dy: 3.6mm, rotate(270deg, corner()))
      inner
      if need > size.height { place(bottom + right, box(fill: red, inset: 2pt, text(fill: white, size: 8pt)[TOOLPAGE-OVERFLOW])) }
    })
  })
}


// ---------- front matter ----------

// a large ring ornament for the cover and title page
#let roundel(r: 20mm, colour: acc) = box(width: 2 * r + 8mm, height: 2 * r + 8mm, {
  place(center + horizon, circle(radius: r, stroke: 0.7pt + colour))
  place(center + horizon, circle(radius: r - 1.6mm, stroke: 0.3pt + colour))
  place(center + horizon, circle(radius: r * 0.52, stroke: 0.3pt + colour))
  for i in range(48) {
    let a = i * 7.5deg
    place(center + horizon, dx: (r + 2.6mm) * calc.cos(a), dy: (r + 2.6mm) * calc.sin(a),
      rotate(45deg, square(size: if calc.rem(i, 12) == 0 { 2mm } else if calc.rem(i, 4) == 0 { 1.2mm } else { 0.7mm }, fill: colour)))
  }
  // twelve rays, like the hours of a dial
  for i in range(12) {
    let a = i * 30deg
    // each ray is centred on its own midpoint, so the twelve stay evenly spaced round the centre
    let r1 = r * 0.56; let r2 = r - 2.4mm; let mid = (r1 + r2) / 2
    place(center + horizon, dx: mid * calc.cos(a), dy: mid * calc.sin(a), rotate(a, line(length: r2 - r1, stroke: 0.3pt + colour)))
  }
  place(center + horizon, rotate(45deg, square(size: r * 0.34, stroke: 0.6pt + colour)))
  place(center + horizon, rotate(45deg, square(size: r * 0.16, fill: colour)))
})

// The cover: the part's name set large on the left, a pale numeral behind it, and a strip of the part's colour at the spine.
#let cover(roman, title, colour) = page(margin: 0mm, header: none, footer: none, fill: tint, {
  place(left, rect(width: 9mm, height: 100%, fill: colour))
  place(right + bottom, dx: 4mm, dy: -30mm, text(size: 250pt, fill: colour.transparentize(80%), roman))
  place(top + left, dx: 20mm, dy: 20mm, caps(size: 11.5pt, tracking: 3.5pt)[The Human Empire])
  place(top + left, dx: 20mm, dy: 27mm, line(length: 30mm, stroke: 1.2pt + colour))
  place(top + left, dx: 20mm, dy: 58mm, block(width: 118mm, {
    if roman != "" { text(fill: colour, caps(size: 11pt, tracking: 3.5pt)[Part #roman]); v(2mm) }
    par(justify: false, leading: 0.35em, text(size: if roman != "" { 70pt } else { 40pt }, title))
  }))
  place(bottom + left, dx: 20mm, dy: -18mm, text(size: 13pt)[Claude and Cameron Severn])
})

#let titlepage(subtitle, date) = page(header: none, footer: none, {
  align(center, {
    v(30mm)
    text(size: 30pt)[The Human Empire]
    v(3mm)
    block(width: 78%, par(justify: false, text(size: 11pt, style: "italic", fill: soft)[How technology, resources, and wars over ideas made one intertwined world]))
    v(7mm)
    flourish(width: 50mm)
    v(7mm)
    text(fill: acc, caps(size: 9pt, tracking: 2.2pt, subtitle))
    v(1fr)
    text(size: 12.5pt)[Claude and Cameron Severn]
    v(3mm)
    text(size: 8.5pt, style: "italic", fill: soft, date)
    v(12mm)
  })
})

// Contents, built from the chapters and tool pages actually in the file
#let contents() = page(header: none, footer: none, {
  align(center, {
    v(8mm)
    text(size: 21pt)[Contents]
    v(-1mm)
    flourish(width: 34mm)
    v(5mm)
  })
  context {
    let items = query(selector(<chapter-start>).or(<tool-start>))
    set par(first-line-indent: 0pt, justify: false, leading: 0.5em)
    for it in items {
      let pg = counter(page).at(it.location()).first()
      let m = it.value
      if m.n > 0 {
        v(2.2mm, weak: true)
        grid(columns: (8mm, 1fr, 9mm), column-gutter: 1.5mm, align: (right + top, left + top, right + bottom),
          text(fill: acc, size: 10.5pt, str(m.n)),
          link(it.location(), text(size: 10.5pt, m.title)),
          text(size: 9.5pt, str(pg)))
      } else {
        grid(columns: (8mm, 1fr, 9mm), column-gutter: 1.5mm, align: (right + top, left + top, right + bottom),
          [], link(it.location(), text(size: 8.6pt, style: "italic", fill: soft, m.title)),
          text(size: 8pt, fill: soft, str(pg)))
      }
    }
  }
})

#let preface(body) = page(header: none, footer: none, {
  align(center, {
    v(2mm)
    text(size: 21pt)[Preface]
    v(-1mm)
    flourish(width: 34mm)
    v(3mm)
  })
  // the preface is kept to one page
  set text(size: 9.3pt)
  set par(leading: 0.6em, spacing: 0.6em)
  body
})
