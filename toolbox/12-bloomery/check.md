I found three factual problems, one doubtful fuel comparison, and several explanatory/design issues. The five numbered steps match the labels in both `prompt.txt` and the generated illustration. No files were edited.

1. **Slag chemistry is wrong, and contradicts the chapter.** [Profile, line 18](toolbox/12-bloomery/profile.md:18):

   > “Sand and clay from the ore melt into a black liquid called slag.”

   Slag is not simply melted sand and clay. Silica reacts with iron oxide to form a lower-melting, iron-rich slag; other materials also enter it. [Experimental study by Blakelock and colleagues](https://www.sciencedirect.com/science/article/pii/S030544030900123X).

   The [chapter correctly explains](chapters/12-assyria/chapter.md:39):

   > “In the heat, they combine with a part of the ore to make a black, glassy liquid called slag, which melts at a lower heat than iron does.”

   This is the clearest direct contradiction.

2. **The blast-furnace explanation omits the change that makes the metal melt.** [Line 31](toolbox/12-bloomery/profile.md:31):

   > “In China, and much later in Europe, taller furnaces with stronger bellows grew hot enough to melt the metal, and iron could then be poured like bronze.”

   The explanation makes this sound like crossing the melting temperature of the same low-carbon iron described earlier. Crucially, the iron absorbs carbon, lowering its melting point and producing cast iron. Iron containing about 4.3% carbon melts at roughly 1,150°C, compared with roughly 1,540°C for pure iron. Height and blast matter, but increased temperature alone is an incomplete account of the transition. [Liu and Wood, section 4](https://www.intarch.ac.uk/journal/issue69/14/full-text.html).

   The card repeats that misleading simplification:

   > “The blast furnace, which is hot enough to melt iron”

3. **Copper is incorrectly given tin’s restricted distribution.** [Line 25](toolbox/12-bloomery/profile.md:25):

   > “Copper and tin lie in a few places, and bronze depended on ships and caravans to bring the two together.”

   Copper deposits are widely distributed; tin is much scarcer. The sound historical point is that *tin bronze required access to two supplies that often lay far apart*, not that both metals occur in only a few places. The chapter makes the narrower argument about tin. [USGS on copper distribution](https://pubs.usgs.gov/publication/sir20265081/full), [USGS on tin](https://www.usgs.gov/centers/national-minerals-information-center/tin-statistics-and-information).

4. **The “stand of trees” comparison is doubtful.** [Line 23](toolbox/12-bloomery/profile.md:23):

   > “A day's work by several people, and a heap of charcoal that took a stand of trees to make, yields a few kilos of iron.”

   The labour and small output are plausible; the woodland comparison lacks a defensible scale. Experimental smelts can consume charcoal measured in tens of kilograms: one documented run charged roughly 50 kg of charcoal with 50 kg of ore and recovered about 12 kg of metal. Traditional charcoal yields vary considerably, commonly around 15–25% of wood weight. Those figures support substantial wood consumption, but do not establish a whole stand of trees for a few kilos of iron. This is a doubtful comparison, not a demonstrated impossibility. [Smelt report](https://www.wealdeniron.org.uk/Expt/Owens%20Smelt.htm), [FAO charcoal yields](https://www.fao.org/4/i1673e/i1673e00.pdf).

5. **“How it works” skips the central mechanism.** [Line 19](toolbox/12-bloomery/profile.md:19):

   > “The iron never melts.”
   >
   > “It gathers at the bottom as a bloom, a spongy lump the size of a loaf of bread, which the smith then hammers into a solid bar.”

   The preceding steps explain charging, air and slag, but never explain how ore becomes iron. This breaks the style requirement that readers should be able to explain the device afterwards. The chapter supplies the missing causal step: gas from the charcoal removes oxygen from the ore. The later sentence—

   > “It still does what the clay shaft did, and strips the oxygen from ore with burning carbon.”

   —arrives after the operating explanation and still leaves the gas’s role unclear.

6. **The temperature lacks a scale.** [Line 17](toolbox/12-bloomery/profile.md:17):

   > “The charcoal beside the pipe burns at about 1,200 degrees, which is some 300 degrees short of the heat that melts iron.”

   Specify Celsius. The rounded comparison is reasonable for low-carbon iron, but “degrees” alone is ambiguous for the intended general reader.

7. **The page substantially repeats the chapter, against the design brief.** For example:

   > “The furnace is a shaft of clay about as tall as a child, with thick walls to hold the heat in.”
   >
   > “That is how iron became the metal of ordinary people.”

   The chapter already gives the child-height shaft, alternating charges, skin bellows, bread-sized bloom, hammering, day’s labour and spread to ordinary users. Some mechanical overlap is necessary, but almost all of “Why it mattered” repeats the chapter’s argument. This conflicts with `design.md`: “The page never retells the chapter.”

The visible text is approximately **445 words**, within the 300–450-word limit. There are **no numbering/label mismatches** and no further clear chapter contradictions. The required photograph section is absent despite a local `photo-bloomery.jpg`; its licence and credit are also absent from the ledger, so eligibility for inclusion remains unverified.