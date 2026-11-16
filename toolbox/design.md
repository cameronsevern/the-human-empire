# Tool pages: design

A tool page sits between two chapters. It profiles one tool that appeared in the chapter just read. The chapters tell the story and mention tools in passing. These pages stop and look at one of them.

## What every page has, in this order

A tool page is one page, and it has to fit on one in the designed PDF.

1. **Title.** The tool's plain name: "The sickle". The page carries no section name.
2. **Card.** Five short facts, always the same five: First made, Made of, What it does, Before it, After it. Keep each to a line or two.
3. **Illustration.** One code-drawn diagram with five numbered labels. The labels are the explanation of how the tool works, so there is no separate "How it works" list.
4. **Why it mattered.** Two short paragraphs, 100 to 130 words in all, in the book's voice.
5. **The real thing.** One photograph of a surviving example with a caption of about 25 words and a credit, when a licensed one exists.

"How it works" and "Where it went" were dropped on 13 November 2026: the first repeated the diagram's labels and the second repeated the card's "After it". The page never retells the chapter. It may add facts the chapter left out.

`build/pdf.py` stamps TOOLPAGE-OVERFLOW on any tool page whose content does not fit, so check for that after editing one.

## The illustration

Each page has one illustration, drawn in code. A short Python script in `toolbox/draw/` lays out the tool, its five numbered parts and the exact wording of each label. The scripts share `lib.py`, which supplies the palette, the frame, the callouts and the look: aged paper with grain, a slight wobble in every line, uneven watercolour washes that pool at the edges, and a soft shadow under each object. Labels are drawn crisp on top.

Rules for a diagram: five numbered callouts; every label inside the frame; no label crossing another label, a leader line or the drawing (use `anchor="end"` when the part lies to the right of its label); terracotta on the one part that makes the tool work. Run the script, look at the PNG, and fix what overlaps before the page is done.

Generated art was tried and used for a while (the `-gen.png` files and `prompt.txt` in each folder, made with `draw/generate.sh`). The pages went back to code-drawn diagrams on 13 November 2026. The generated files are kept but no page shows them.

## Which tool for which chapter

A chapter can have more than one tool page: if a tool is interesting, it gets a page. Any tool from the chapter can be chosen, weapons included. While the pictures were generated, weapons were avoided because the image service refused them. The diagrams are drawn in code now, so that limit is gone.

| After chapter | Tool | Why this one |
|---|---|---|
| 1 | The hand axe | The first thing made to a plan |
| 1 | The hearth | Fire kept in one place |
| 2 | The eyed needle | What let a tropical ape live in the cold |
| 2 | The voyaging canoe | A village that floats |
| 3 | The lamp | How the painters saw in the dark |
| 3 | The bead | An object that only means something |
| 4 | The bow | Killing from a distance |
| 4 | The spear | The weapon that made tyrants unsafe |
| 5 | The sickle | The tool that changed wheat |
| 5 | The grinding stone | The daily cost of bread |
| 6 | The clay tablet | Memory outside the head |
| 6 | The ration bowl | A day's pay in clay |
| 7 | The sledge and ramp | How a ten-ton block moves |
| 7 | The Nile boat | A river that runs both ways |
| 8 | The cylinder seal | A signature for people who cannot write |
| 9 | The clay envelope | A contract nobody can alter unseen |
| 10 | The spoked wheel | The wheel made light enough for a horse |
| 11 | The copper slab | Metal as a cargo |
| 12 | The bloomery | Iron from common ore |
| 12 | The siege ram | The machine that ended the safety of walls |
| 13 | The qanat | Water carried under the desert |
| 14 | The scroll | A text that can be carried anywhere |
| 15 | The coin die | A stamp that strangers trust |
| 16 | The memorised verse | A book kept without writing |
| 17 | The bamboo book | The page the Chinese thinkers wrote on |
| 18 | The allotment machine | Choosing by chance, so that nobody can be bought |
| 18 | The trireme | The warship rowed by the poor |
| 19 | The long pike | Five points in front of every man |
| 19 | The shadow stick | Measuring the Earth with a shadow |
| 20 | The edict pillar | A king's words set where all can see |
| 21 | The crossbow | A bow that a farmer can aim |
| 21 | The standard measure | One size for a whole empire |
| 22 | The layered bow | The horse archer's weapon |
| 22 | The silk reel | The thread the frontier was paid in |
| 23 | The boarding bridge | How a land power won at sea |
| 24 | The rods and axe | The power to punish, carried in the street |
| 25 | The book with pages | The book the Christians chose |
| 26 | The begging bowl | A monk's whole property, filled by others |
| 27 | The triple wall | Why the eastern capital held |
| 28 | The camel saddle | A seat over the hump, and the desert crossed |
| 29 | The fire siphon | Fire that burned on water, and a recipe nobody knows |
| 30 | The paper mould | One sheet a dip, all day long |
| 31 | The printing block | A page carved once and printed for centuries |
| 32 | The fire lance | A tube of powder on a spear, the ancestor of the gun |
| 32 | The compass needle | North and south under a clouded sky |
| 33 | The sewn ship | A hull held together with coconut cord |
| 34 | The walking statue | Ten tonnes of stone rocked upright along a road |
| 35 | The longship | Overlapping planks, one sail, and a metre of water |
| 36 | The heavy plough | A slab of wet clay cut and turned upside down |
| 36 | The flying buttress | A stone arm that took the push, so the wall could be glass |
| 37 | The stirrup | A loop for the foot that steadied the rider |
| 38 | The salt slab | The cargo that bought the gold |
| 39 | The knotted cord | Accounts kept in knots, in tens |
| 39 | The three sisters | Three crops in one mound, each helping the others |
| 40 | The relay tablet | A metal order that bought a fresh horse at every station |
| 42 | The great bombard | The gun that broke the walls, in two halves that screw together |
| 43 | The brick dome | Two shells of brick, raised with no frame beneath |
| 43 | The vanishing point | Depth on a flat wall, from one point on the horizon |
| 44 | The caravel | The small ship that could work against the wind |
| 44 | The sea astrolabe | The sun's height, read from a brass wheel hung from the thumb |
| 45 | The type mould | Thousands of identical letters a day from one small box |
| 46 | The obsidian sword | A club edged with volcanic glass, made to take men alive |
| 47 | The piece of eight | Silver cut from a bar and stamped by hand |
| 49 | The matchlock | A trigger that brings the burning cord to the powder |
| 49 | The turtle ship | A warship roofed with spikes, so that nobody could board it |
| 50 | The log fort | A stockade at a river crossing, holding furs and hostages |
| 51 | The telescope | Two lenses in a tube, and the sky made new |
| 51 | The air pump | A globe emptied of air, stroke by stroke |
| 52 | The cowrie | Shell money, brought to Africa as ballast |
| 53 | The sugar mill | Three rollers that crushed each cane twice |
| 54 | The company share | Money pooled for good, and a stake anyone could sell |
| 54 | The flintlock musket | A spark from a flint, and a blade that let it keep firing |
| 56 | The tax stamp | A tax pressed into the paper itself, with no ink |
| 57 | The guillotine | One blade and one death for everyone |
| 61 | The atmospheric engine | Steam turned to water, and the air did the pushing |
| 61 | The separate condenser | Cool the steam somewhere else, and keep the cylinder hot |
| 61 | The water frame | Rollers that did the spinner's drawing, turned by a river |
| 63 | The survey grid | A continent ruled into numbered squares before it was sold |
| 64 | The Minié ball | A bullet that dropped in loose and gripped the grooves on firing |
| 64 | The telegraph | A key, a wire and a magnet: words at the speed of a hand |
| 65 | The iron steamship | A shallow iron hull that steamed upriver against wind and current |
| 66 | The battleship | Big guns behind armour, bought from Britain and fired at Tsushima |
| 67 | The swan-neck flask | Open to the air, closed to the dust |
| 67 | The Petri dish | A lidded dish of seaweed jelly, where each germ grows into a spot |
| 69 | The Maxim gun | The kick of each shot loads and fires the next |
| 69 | Quinine | A bitter bark, a daily dose, and the fever held back |
| 70 | The safety bicycle | A chain to the back wheel, and a tube of air in each tyre |
| 70 | The typewriter | Type bars that strike one spot, and a carriage that steps along |

## Files

Each page lives in `toolbox/NN-name/` with `profile.md`, the schematic as `name.svg` and `name.png`, the subject brief as `prompt.txt`, and one photograph named `photo-*.jpg` with a row in `toolbox/ledger.md`.
