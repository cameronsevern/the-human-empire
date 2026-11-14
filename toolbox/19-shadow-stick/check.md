I found the following issues. No files were edited.

1. **The “Before it” entry has the wrong chronology.** [Line 8](toolbox/19-shadow-stick/profile.md:8):
   > “A figure of 400,000 stades for the Earth, passed on with no method attached”

   Aristotle reports this figure in the fourth century BCE, long after shadow clocks existed. It precedes Eratosthenes’ measurement, not the shadow stick. This also fails the design requirement that “Before it” describe what people did without the tool. The figure itself is legitimate; its placement is wrong. Sources: [Aristotle, *On the Heavens*, II.14](https://classicalliberalarts.com/wp-content/uploads/ARISTOTLE_DE_CAELO.pdf); [NIST’s history of early clocks](https://www.nist.gov/pml/time-and-frequency-division/popular-links/walk-through-time/walk-through-time-early-clocks).

2. **The Syene statement contradicts the chapter’s explicit correction.** [Line 16](toolbox/19-shadow-stick/profile.md:16):
   > “At Syene, at noon on the longest day of the year, the sun stands overhead.”
   > “An upright stick there casts no shadow.”

   This describes the idealised geometry, not Syene’s exact position. Syene lay slightly north of the tropic. The [chapter, line 193](chapters/19-alexander/chapter.md:193), explicitly says: “Syene does not lie exactly south of Alexandria, and the midsummer sun was not quite overhead there.” The profile needs to identify the simplified model or preserve that correction. Source: [Eratosthenes biography, *Dictionary of Scientific Biography*, hosted by St Andrews](https://mathshistory.st-andrews.ac.uk/DSB/Eratosthenes.pdf).

3. **The explanation omits a necessary geographical assumption.** [Lines 17–19](toolbox/19-shadow-stick/profile.md:17):
   > “At Alexandria, at the same noon, an upright stick casts a short shadow.”
   > “The ground has curved by that same angle between the two towns.”
   > “The towns are 5,000 stades apart, and that distance is one fiftieth of the way round.”

   The calculation assumes the towns lie on the same north–south meridian, with Syene under the overhead sun. Their actual longitudes differ by about three degrees, so their local solar noons are not simultaneous. The chapter supplies the approximate north–south alignment and later acknowledges the discrepancy; the profile supplies neither. Describe 5,000 stades as the distance used in the calculation, rather than an exact geographical measurement. This is a missing premise, not merely excessive confidence. Source: [Lucio Russo’s discussion of Cleomedes’ assumptions](https://msp.org/memocs/2013/1-1/memocs-v1-n1-p04-s.pdf).

4. **The seasonal rule needs a geographical limit.** [Line 23](toolbox/19-shadow-stick/profile.md:23):
   > “Its noon shadow is shortest of all on the longest day of the year, and so it marks the turning of the seasons.”

   This works for the Egyptian locations discussed, but not as a general rule for shadow sticks. Inside the tropics, the shortest noon shadow occurs when the sun passes overhead, usually twice a year, rather than on the longest day. Adding a local scope would retain the confident explanation while making it accurate. Source: [NASA, “Tropical Solstice Shadows”](https://science.nasa.gov/solar-system/skywatching/night-sky-network/tropical-solstice-shadows/).

5. **The “After it” entry makes the page’s timeline misleading.** [Lines 9 and 31](toolbox/19-shadow-stick/profile.md:9):
   > “The sundial”
   > “The stick's main descendant is the sundial, which is a shadow stick with a scale under it for reading the hours.”

   A sundial can reasonably be described as a development of a basic shadow stick. However, paired with the fourth-century-BCE “Before it” entry and Eratosthenes-centred explanation, this implies that sundials followed his measurement. Egyptian sundials existed around 1500 BCE, and the [chapter explicitly says he used a sundial’s pointer](chapters/19-alexander/chapter.md:185). The card needs a consistent timeline for either the tool or this application. Source: [NIST](https://www.nist.gov/pml/time-and-frequency-division/popular-links/walk-through-time/walk-through-time-early-clocks).

6. **Label 2 loses the seasonal condition in step 2.**
   > Step 2: “At Syene, at noon on the longest day of the year, the sun stands overhead.”
   > Label 2: “At Syene the noon sun is overhead, and a stick casts no shadow”

   The label, in both `prompt.txt` and the generated illustration, omits “on the longest day,” making it read as an everyday occurrence. Otherwise, **numbers 1–5 correspond correctly to their steps**; I found no swapped or missing numbered labels.

7. **“Stades” is unexplained at first use.** [Line 8](toolbox/19-shadow-stick/profile.md:8):
   > “A figure of 400,000 stades for the Earth, passed on with no method attached”

   `style.md` requires historical terms to be explained in the sentence where they first appear. The profile never defines this unit. The preceding chapter does: “A stade was the length of a Greek running track.”

8. **There is direct repetition of the chapter, against the toolbox design.** [Line 15](toolbox/19-shadow-stick/profile.md:15):
   > “The sun is so far away that its rays reach the Earth side by side, like the lines on ruled paper.”

   This is copied verbatim from [chapter line 174](chapters/19-alexander/chapter.md:174). More broadly, all five steps repeat the chapter’s extended explanation of the measurement. Some overlap is necessary to explain the tool, but the exact repetition and repeated sequence conflict with the design instruction: “The page never retells the chapter.”

9. **The page exceeds the prescribed length.** It contains approximately **470 words of visible text**, including the card and headings but excluding image alt text and Markdown syntax. `toolbox/design.md` specifies **300–450 words**. This is a page-level issue, so there is no individual offending sentence.