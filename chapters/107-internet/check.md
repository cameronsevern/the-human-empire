I found the following issues in [chapter 107](chapters/107-internet/chapter.md), ordered roughly by seriousness. Confidence refers to the correction, not the chapter’s wording.

1. **Wrong chronology — government regulation (line 101).**  
   > “Governments that had left the internet alone for twenty years began, in the 2010s, to try to bring it under their laws.”

   Governments were legislating specifically for the internet well before the 2010s. For example, the United States enacted the Children’s Online Privacy Protection Act in 1998. The 2010s brought intensified regulation, not its beginning. **Confidence: high.** [FTC history of COPPA](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions).

2. **False causal absolute — security (line 61).**  
   > “Every later problem of security on the internet goes back to that.”

   Missing authentication in early networking explains some vulnerabilities. It does not explain every subsequent software flaw, compromised device or malicious insider. A buffer overflow, for example, results from unsafe handling of memory and can occur entirely offline. This also directly breaks the rule against absolutes defeated by one exception. **Confidence: high.** [OWASP’s explanation of buffer overflows](https://community.owasp.org/vulnerabilities/Buffer_Overflow).

3. **Doubtful statistic — Taiwan’s share (line 95).**  
   > “Nine tenths of the most advanced ones are manufactured by a single company in Taiwan, founded in 1987 by an engineer who had been passed over for the top job at an American chip firm.”

   “Most advanced” needs a definition and reference year. The widely repeated nine-tenths figure cannot safely stand as an undated description of all advanced chips. SIA/BCG’s 2024 figures assign Taiwan **69% of global manufacturing capacity for logic chips below 10 nanometres in 2022**, with South Korea holding 31%. Capacity, actual production and company market share are different measures. **Confidence: high that the sentence needs qualification; medium that its intended, unspecified measure is wrong.** [SIA’s report summary](https://www.semiconductors.org/wp-content/uploads/2024/05/Emerging-Resilience-in-the-Semiconductor-Supply-Chain_SIA-Summary.pdf).

4. **Wrong priority claim — the opening connection (line 9).**  
   > “The plan was for Kline to log in to the northern computer from his own, which nobody had done between two machines of different makes.”

   In 1965 Lawrence Roberts and Thomas Merrill connected the TX-2 in Massachusetts to the Q-32 in California; their experiment included running programs and retrieving data remotely. The 1969 event should be identified as the first ARPANET host-to-host message, without this broader claim. **Confidence: high.** [Internet history written by its pioneers](https://www.internetsociety.org/internet/history-internet/brief-history-internet/).

5. **Wrong account of the integrated circuit (line 33).**  
   > “In 1958 and 1959 two engineers, one in Texas and one of the eight in California, each saw that a whole circuit, transistors and the connections between them, could be formed in a single flat piece of silicon.”

   Kilby’s 1958 demonstration used **germanium and external connecting wires**. Noyce’s subsequent silicon design supplied the practical route to integrated interconnections. The sentence gives both men the same material and solution, obscuring the advance it is explaining. **Confidence: high.** [Computer History Museum’s account of Kilby’s device](https://www.computerhistory.org/siliconengine/all-semiconductor-solid-circuit-is-demonstrated/).

6. **False physical claim — transistor size (line 29).**  
   > “It did not burn out, it used a fraction of the power, and there was no limit in principle to how small it could be made.”

   Transistors removed the fragile heated filament, but they can fail, and there are physical limits to miniaturisation. Quantum tunnelling allows current to leak through sufficiently thin barriers; this has already required changes in transistor materials and design. “Much smaller” would preserve the point accurately. **Confidence: high.** [Intel’s explanation of tunnelling and gate leakage](https://www.intel.com/pressroom/kits/advancedtech/doodle/ref_HiK-MG/high-k.htm).

7. **Misleading commercial history — Xerox (line 69).**  
   > “Their employer saw no way to make money from it.”

   Xerox did attempt to commercialise these ideas, introducing the Star office system in 1981. Its failure to turn them into a mass-market success is a different story from seeing no commercial use. **Confidence: high.** [Retrospective by the Star’s developers](https://www.dcn.org/go/dwnelson/XeroxStarRetrospective.html).

8. **Wrong date — Amazon (line 79).**  
   > “The bookshop, the search engine and the social network that now dominate their fields were founded in the next nine years, the last two by students.”

   The preceding sentence establishes 1995 as the starting point. Amazon was incorporated in **1994** and opened its website in July 1995. It therefore was not founded in the following nine years. Naming Amazon, Google and Facebook would also spare the reader this guessing game. **Confidence: high.** [Amazon’s SEC filing](https://www.sec.gov/Archives/edgar/data/1018724/000119312505047032/d10k.htm).

9. **Conflated versions — Colossus (line 21).**  
   > “At the British code-breaking centre, a telephone engineer constructed a machine in 1943 that used two and a half thousand glass electronic valves as its switches, to break the ciphers of the German high command.”

   The 1943 Mark I had roughly **1,500–1,600 valves**; the larger count belongs to the later Mark II. Flowers also built the original at the Post Office research station at Dollis Hill before it was transported to Bletchley Park. **Confidence: high on the conflation and location; sources differ slightly on valve counts.** [Colossus reconstruction leader Tony Sale’s account](https://www.codesandciphers.org.uk/virtualbp/fish/colossus.htm).

10. **Misleading destruction story — Colossus (line 21).**  
    > “It was so secret that after the war the machines were broken up and the drawings burned, and its existence was not admitted for thirty years.”

    This suggests immediate, complete destruction. Two machines were retained for intelligence work after the war; their dismantling and the destruction of drawings came much later, around 1960. “Most were destroyed after the war” would preserve the secrecy story without erasing their continued use. **Confidence: high.** [Tony Sale’s account](https://www.codesandciphers.org.uk/virtualbp/fish/colossus.htm).

11. **Overbroad description of export controls (line 97).**  
    > “In 2022 the United States forbade the sale of the most advanced chips, and of the machines that make them, to China, and began paying companies to build factories on American soil.”

    The October measures imposed licensing requirements on specified advanced computing chips, manufacturing equipment and activities, with defined thresholds and exceptions. They were not a blanket prohibition on every advanced chip and every machine used to make one. “Restricted exports” is the accurate plain-language description. **Confidence: high.** [The original 2022 rule](https://www.govinfo.gov/app/details/FR-2022-10-13/2022-21658).

12. **False exclusivity — early chip customers (line 35).**  
    > “Chips were at first extremely expensive, and there were only two customers who would pay.”

    Apollo and missile programmes were crucial customers, but commercial buyers were also purchasing early integrated circuits. NASA’s history records Fairchild selling to commercial clients from 1961. “Two especially important customers” retains the argument and complies with the rule against brittle absolutes. **Confidence: high.** [NASA’s history of spaceflight’s technological impact](https://www.nasa.gov/wp-content/uploads/2016/01/historical-studies-societal-impact-spaceflight-ebook_tagged.pdf).

13. **Overbroad priority claim — programmers (line 23).**  
    > “To set it up for a new problem took days of unplugging and replugging hundreds of cables, and the people who worked out how to do that, the first programmers, were six young women who had been hired as mathematicians.”

    They were ENIAC’s first programmers, not the first programmers without qualification. Grace Hopper was already working on Harvard’s Mark I in July 1944. Adding “ENIAC’s” fixes the claim without diminishing the women’s achievement. **Confidence: high.** [Hopper’s oral history](https://archive.computerhistory.org/resources/text/Oral_History/Hopper_Grace/102702026.05.01.pdf).

14. **Incorrect description of the Mosaic team (line 79).**  
    > “That same year a group of students in Illinois released a program that displayed web pages with pictures and let the user move between them by clicking.”

    Mosaic was developed by students **and staff** at NCSA. Co-creator Eric Bina had joined its staff as a programmer in 1991. **Confidence: high.** [University of Illinois biography of Bina](https://grainger.illinois.edu/alumni/hall-of-fame/eric-bina).

15. **Reader loses the distinction between the internet and the Web (line 5).**  
    > “It was built in layers over fifty years, each resting on the one beneath: a machine that calculates with switches, a switch with no moving parts, a way of printing millions of such switches on a chip of silicon, a method of sending messages in small pieces, and a scheme for linking documents that its author gave away.”

    The organising metaphor is useful, but the Web is a service built **on** the internet, not a necessary layer of the internet itself. Explain that distinction explicitly when Berners-Lee arrives: the internet carries messages; the Web uses it to retrieve linked pages. Otherwise the reader cannot explain why email existed before the Web.

16. **Unclear referent and misleading literal meaning (line 15).**  
    > “The machine at each end was the first layer, and it was twenty-five years old.”

    This reads as though the actual computers used in 1969 were twenty-five years old. Presumably the intended subject is electronic computing. The preceding scene also includes terminals, cabinets and host computers without distinguishing their jobs. Identify which machine performs the calculations and which passes messages along.

17. **Missing explanation — stored instructions (line 19).**  
    > “The second was that the list of instructions telling the machine what to do can itself be stored in the machine as numbers, and changed.”

    The next examples are Colossus and the original ENIAC, followed by an account of changing cables to change the program. A general reader will reasonably wonder what happened to the instructions stored as numbers. Add a short bridge explaining that these early machines did not yet implement that arrangement.

18. **Too much anonymity to follow the story (line 31).**  
    > “Two of those eight later left that firm to found another, and their colleagues founded dozens more, all within a few miles.”

    The reader must retain several unnamed companies and nested groups, then recognise one of the men as Moore and the later company as the maker of the 1971 processor. The “few names” rule explicitly permits names needed to follow the story. Naming Fairchild and Intel would reduce the mental bookkeeping.

19. **Unexplained technical terms and stacked figures (line 93).**  
    > “To print them, the light used must have an extremely short wavelength, and there is one company in the world, in the Netherlands, that makes machines able to do it.”

    Explain why shorter waves let the machine print smaller features; otherwise the elaborate tin-droplet description never completes its causal chain. “Plasma” in the next sentence also needs a plain explanation.

    > “One machine has a hundred thousand parts, costs about two hundred million dollars, and is delivered in forty shipping containers.”

    This directly breaks “one number per point”: three statistics establish the same point about extraordinary complexity and scale. Choose the strongest image.

I found **no clear direct contradictions with chapters 93 or 101**. Their accounts of Apollo’s chip purchases, Taiwan’s manufacturing role and Chinese internet control are compatible with this chapter. I also found no clear hedging stacks, chapter self-mentions, body cross-references or explicit answer-announcing signposts. No files were edited.