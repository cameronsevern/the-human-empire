## Changed facts

No names, dates, numbers or quotations were changed or removed. Most revisions expand or restate existing material. However, several additions introduce factual claims or make previously implicit causal claims explicit.

| Old sentence | New sentence | Change |
|---|---|---|
| “He proposed a test.” | “Instead of trying to define thinking, he proposed a test.” | Adds Turing’s reason for substituting the test. |
| “It failed at almost everything that a small child does without effort.” | “The same approach, however, failed at almost everything that a small child does without effort.” | Changes the subject from an ambiguous “it”—apparently Deep Blue—to the rule-based approach generally. |
| “The method fell out of favour for decades.” | “After promises like that, the disappointment was great, and the method fell out of favour for decades.” | Adds disappointment after inflated promises as the historical explanation. |
| “After that the results came quickly.” | “After that the results came quickly, and the most public of them came in a game.” | Adds a claim about the relative publicity of the Go result. |
| “They have a characteristic fault.” | “They have a characteristic fault, and it follows directly from how they are trained.” | Makes training the explicit cause of hallucination. |
| “The most capable models belong to a handful of companies.” | “All of this costs so much that few can afford it. As a result, the most capable models belong to a handful of companies.” | Adds cost as the explanation for concentrated ownership. |
| “A third group expects people and machines to merge.” | “A third group expects people and machines to merge, and the first small steps have been taken.” | Classifies existing brain implants as steps towards that predicted merger. |
| “It was read by the few people who had been trained to read it.” | “It was read by the few people who had been trained to read it, and everyone else depended on them.” | Adds universal dependence on the literate minority. |

These standalone additions have **no old sentence**:

- “No single nudge does much.” Adds a categorical claim about individual training updates.
- “A network that learns from examples can only be as good as the examples it sees, and it learns only as fast as the arithmetic can be done.” Adds two general limits on learning.
- “Each of them then had to be labelled by a person, which was a vast job in itself.” Explicitly extends human labelling to every photograph.
- “Games, in effect, had already paid for the hardware that the new method needed.” Adds an economic explanation for the availability of GPUs.
- “The machine had not merely copied human play; it had found something that people had passed over.” Adds an interpretation of AlphaGo’s novelty.
- “To know the shape is to begin to know what the protein does.” Adds an explanatory claim about structure and function.
- “Now anyone with an internet connection could try one, and a great many people did.” Adds universal availability.
- “A tool that makes a beginner as good as a veteran can lift the beginner up, or it can make the veteran unnecessary.” Strengthens the preceding productivity finding into equivalence between beginners and veterans, then adds possible employment consequences.
- “In these uses, a mistake falls on one particular person.” Adds a claim about the distribution of harm.
- “It has no way to tell a pattern worth copying from an old injustice.” Adds an absolute limitation on the system.
- “In a race, every pause for safety is a chance for a rival to pull ahead.” Adds a competitive incentive claim.
- “Meanwhile, the two largest powers have gone their own ways.” Introduces the United States and China as the two largest powers, without specifying the measure.

These are not all errors. They do mean the revision is not strictly fact-neutral. Other additions chiefly repeat facts already present or articulate the book’s interpretation.

## Factual flags

1. **Minor — Dartmouth’s proposed attendance becomes actual attendance.**

   > “Six years later ten American scientists gathered for a summer at a college in New Hampshire to study what one of them had named artificial intelligence.”

   Ten was the proposed group size, not a reliable count of everyone who participated. Dartmouth’s historical account gives about twenty participants, with attendance ranging from hours to the whole summer. McCarthy likewise recalled people arriving at different times and staying for different durations. The correct account is a summer workshop with a changing group of researchers. [Dartmouth’s account](https://dartmouthalumnimagazine.com/articles/birth-artificial-intelligence), [McCarthy’s recollection](https://www-formal.stanford.edu/jmc/slides/dartmouth/dartmouth/node1.html).

2. **Major — the ImageNet scoring rule remains missing.**

   > “The next best entry failed on one picture in four. Theirs failed on one in seven.”

   These were **top-five** error rates: an image counted as correctly classified if its correct label appeared among five guesses. The sentences read as single-answer accuracy. The correct figures are 26.2% and 15.3% top-five error. The earlier check’s correction to the comparison year has been made; this separate scoring issue remains. [Original AlexNet paper](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf).

3. **Minor — the GPU explanation overstates parallelism.**

   > “The arithmetic of a neural network consists of an enormous number of simple multiplications that can all be done at once.”

   Many operations can run simultaneously, but not all: later layers depend on earlier results. This also contradicts the chapter’s own step-by-step description of information passing through layers. The correct point is that GPUs perform large batches of independent arithmetic operations in parallel. [AlexNet’s description of its layered architecture and GPU implementation](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf).

4. **Minor — newly introduced universal access claim.**

   > “Now anyone with an internet connection could try one, and a great many people did.”

   Internet access alone did not make ChatGPT available everywhere. OpenAI restricted registration geographically; contemporary reporting identifies mainland China, Hong Kong, Iran and Russia among excluded locations. The correct claim is that ChatGPT made this technology readily accessible to the public in supported countries. [Reuters’s February 2023 report](https://finance.yahoo.com/news/1-chatgpt-frenzy-sweeps-china-032342709.html), [OpenAI’s supported-country policy](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries).

5. **Minor — Hinton’s departure and its announcement are conflated.**

   > “That month Hinton resigned from his post so that he could say so freely.”

   “That month” refers to May 2023. Hinton says he left Google at the **end of April 2023**; the departure became public in May. His own account also distinguishes retirement from using the opportunity to warn about AI. [Hinton’s June 2024 interview, first page](https://groups.inf.ed.ac.uk/aics_history/AICSCSHistory_Interview005_GeoffreyHinton_publish.pdf).

6. **Minor — the EU law’s application dates remain unclear.**

   > “The European Union passed a law in 2024 that bans some uses outright, such as scoring citizens for general trustworthiness, and requires that systems used for certain serious decisions about people, in hiring, credit, policing and the like, be documented, tested for bias, and overseen by a human being who is able to overrule them.”

   The earlier scope problem has been corrected. The timing problem remains: in a chapter ending in 2025, this reads as though all these requirements were already applicable. Under the enacted timetable, the prohibitions applied from February 2025, while most relevant high-risk requirements were scheduled for August 2026, with some later. Distinguish what the law enacted from what had taken effect. [AI Act, Article 113](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng).

## Clarity flags

- **Repeated setup and signposting:**  
  > “The machines that most people have met are of one particular kind, and they are trained to do something that sounds trivial.”  
  > “The task that such a model is trained on is simple.”  
  > “The task looks shallow, but doing it well is not.”

  These announce the same contrast three times. The first also postpones identifying the machines. This goes beyond helpful orientation into repeated setup.

- **Signpost sentence:**  
  > “That finding cuts both ways.”

  It announces the interpretation supplied by the next sentence rather than stating it, contrary to the explicit prohibition on signposts.

- **Padding that duplicates adjacent evidence:**  
  > “They were confident.”  
  > “The gap between them and everyone else was wide.”  
  > “The owners of that work have fought back.”

  The proposal, error rates and lawsuits immediately following already establish each point. These additions contribute little orientation.

- **An undefined limit:**  
  > “A network that learns from examples can only be as good as the examples it sees, and it learns only as fast as the arithmetic can be done.”

  “As good as” is unclear: data quality, accuracy, or human performance? Readers may take it to mean a model cannot surpass its examples, making the later human-benchmark result puzzling.

- **An absolute whose intended scope is missing:**  
  > “It has no way to tell a pattern worth copying from an old injustice.”

  This needs to distinguish learning from historical examples alone from a system supplied with additional fairness criteria or corrective training. Such interventions exist, although they do not confer independent moral judgment. [Research on adjusting learned predictors to meet a fairness criterion](https://arxiv.org/abs/1610.02413).

- **An unnecessarily universal consequence:**  
  > “In these uses, a mistake falls on one particular person.”

  An erroneous decision can affect a household or multiple applicants. The Dutch opening itself describes consequences for spouses and children. “One particular person” narrows the harm unnecessarily.

- **Ambiguous antecedent:**  
  > “Meanwhile, other models make pictures, music and film from a typed description. This book was written with the help of one.”

  “One” now most naturally refers to a picture-, music- or film-making model. The authorised disclosure is not itself a style violation; its placement makes the intended model unclear.

- **Unclear scope creates an apparent contradiction:**  
  > “Institutes to test the systems and a yearly scientific report have followed, and no binding rules.”

  If this means no binding rules resulted from the summit process, that scope needs to be explicit. Otherwise it appears to contradict the EU law already described.

- **Narrative cross-reference:**  
  > “At the beginning of this story there was a small clay tablet from the city of Uruk, more than five thousand years old.”

  “At the beginning of this story” sends readers back through the book instead of simply recalling the historical object. It breaks the style sheet’s preference for natural historical reminders over cross-references.

No hedging stacks stood out.

## Overall

The revision generally improves pacing and preserves the numerical record, but introduces several broader claims and some repetitive setup. The clearest remaining factual fixes concern benchmark scoring, parallel computation, access restrictions and chronology. Fixed concerns from the earlier check have not been repeated. No files were edited.