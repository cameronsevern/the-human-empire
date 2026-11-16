# 107. Who invented the internet?

*The United States, Britain, Switzerland and Taiwan, from 1943 to 2025*

Nobody invented the internet. It was built in layers over fifty years, each resting on the one beneath: a machine that calculates with switches, a switch with no moving parts, a way of printing millions of such switches on a chip of silicon, a method of sending messages in small pieces, and a scheme for linking documents that its author gave away. Most of those layers were paid for by governments, and then made into products by private companies.

At half past ten on the night of 29 October 1969, a student named Charley Kline sat down at a terminal in a windowless room at the University of California in Los Angeles. Beside him stood a grey steel cabinet the size of a refrigerator, which had been delivered eight weeks before. A telephone line, rented from the telephone company, ran from it to an identical cabinet at a research institute five hundred and fifty kilometres to the north, where another young programmer was waiting with a telephone headset on.

The plan was for Kline to log in to the northern computer from his own, over a network built for the purpose, which nobody had yet done. He was to type the word LOGIN. He typed L, and asked over the telephone whether it had arrived. It had. He typed O. That arrived too. He typed G, and the computer at the other end crashed.

They had it working an hour later. Kline wrote a line in the laboratory's logbook: talked to SRI, host to host. The first message sent over what became the internet was therefore "lo".

## Switches

The computer at each end was the first layer, and the idea of it was twenty-five years old.

A computer is at bottom a very large collection of switches. A switch can be on or off, and so it can stand for a one or a nought. A row of switches can stand for any number, written with only those two digits, and switches wired together in the right patterns can add two such numbers, or compare them, or pass the result on to another group of switches. Everything a computer does is built up from those steps, performed in sequence, millions of times.

Two further ideas turned a calculator into something more. The first was that anything at all can be turned into numbers. A letter of the alphabet can be given a number, and so a book becomes a long string of them. The brightness of each dot in a picture can be given a number, and the height of a sound wave at each instant. The second was that the list of instructions telling the machine what to do can itself be stored in the machine as numbers, and changed. A single machine can then do any task for which someone can write the instructions. An English mathematician, Alan Turing, had described such a universal machine on paper in 1936, before anyone could build one. The first machines fell short of it, and had to be rewired for each new task.

The war paid for the building. At the British code-breaking centre, a telephone engineer delivered a machine at the start of 1944 that used some sixteen hundred glass electronic valves as its switches, to break the ciphers of the German high command. It was so secret that after the war most of the machines were broken up, the drawings were later burned, and its existence was not admitted for thirty years.

The Americans built theirs to calculate the paths of artillery shells. It was finished in 1945, too late for the war, and filled a room in Philadelphia. It had eighteen thousand valves, weighed thirty tons, and used as much electricity as a small town. Its first job was a calculation for the hydrogen bomb. To set it up for a new problem took days of unplugging and replugging hundreds of cables, and the people who worked out how to do that, its first programmers, were six young women who had been hired as mathematicians. They were not invited to the dinner that celebrated the machine.

## A grain of sand

Valves were the weakness. Each was a glass bulb with a glowing filament, like a light bulb, and like light bulbs they burned out. The Philadelphia machine lost one every couple of days.

In December 1947 three physicists at the research laboratories of the American telephone company found a replacement. Certain materials, of which the commonest is silicon, the main ingredient of sand, conduct electricity only under some conditions. The three men showed that a small current applied to a sliver of such a material could turn a larger current on and off. It was a switch with no filament, no vacuum and no moving parts. It had nothing to burn out, it used a fraction of the power, and it could be made very small indeed. They called it a transistor.

One of the three was a brilliant and impossible man who quarrelled with the others and, in 1956, went home to California to found his own company, in the valley of fruit orchards south of San Francisco where his mother lived. He hired the best young engineers in the country. Within a year, eight of them had had enough of him and resigned together to start a rival firm, Fairchild. Two of those eight later left it to found another, Intel, and their colleagues founded dozens more, all within a few miles. The orchards became Silicon Valley.

The first transistors were made one at a time and wired together by hand. In 1958 and 1959 two engineers, one in Texas and one of the eight in California, each saw that a whole circuit could be formed in a single piece of material, and the Californian worked out how to lay the connections down flat on the silicon as well. The pattern is laid down by a process like photography. Light is shone through a stencil onto a wafer coated with a sensitive film, and chemicals eat away the exposed parts. Any number of circuits can be printed side by side on one wafer, which is then cut up into chips.

Chips were at first extremely expensive, and there were two customers who would pay almost anything. One was the air force, for the guidance systems of its missiles. The other was the programme to put a man on the Moon.

## Doubling

In 1965 one of the eight, Gordon Moore, was asked by a magazine to predict the future of the industry. He had noticed that the number of transistors that could be fitted on a chip had doubled every year, and he supposed that it would go on doing so for another ten. He later adjusted the rate to every two years.

It has gone on for sixty. In 1971 Intel sold the first chip that contained the whole central part of a computer. It had two thousand three hundred transistors. The chip in a present-day telephone has about twenty billion, each far too small to be seen with any ordinary microscope. Nothing else that human beings make has improved at that rate. The cost of a transistor has fallen to less than a millionth of what it was, and a machine that once filled a room and belonged to a government now sits in a child's pocket.

## Packets

The network had its origin in a fright. In 1957 the Soviet Union launched the first satellite, and the American government, to make sure that it was not surprised again, set up an agency to pay for advanced research. One of its officials was a psychologist who believed that computers would be most useful as a means for people to communicate. He wrote memos to his colleagues, only half in jest, about an "intergalactic computer network".

The agency had a practical problem. It was paying for large computers at a dozen universities. Each was different, each was fully booked, and a researcher in Utah could not use a program that ran only on a machine in Massachusetts. It decided to connect them.

The telephone network of the day worked by circuits. To make a call, the exchanges set up a continuous electrical path between two telephones and reserved it for as long as the call lasted. That suited conversation, which is steady, and was hopeless for computers, which send data in sudden bursts with long silences between.

A different method had been thought of twice, independently. An engineer at an American military research institute had been asked how a communications system might go on working after a nuclear attack had destroyed most of it. A physicist at a British government laboratory had been thinking about how to share lines efficiently. Both arrived at the same answer. Chop every message into small pieces. Put on each piece the address that it is going to and a number giving its place in the sequence. Send each piece off separately through a mesh of connected machines, each of which simply passes it on to a neighbour that is closer to the destination. The pieces may go by different routes and arrive out of order, and the receiving machine puts them back together. If part of the mesh is busy or broken, the pieces go another way. The Englishman called the pieces packets.

By the end of 1969 the agency's network joined four computers. Two years later an engineer working on it wrote a program for leaving a message for a user of another machine, and needed a way to separate the person's name from the machine's. He looked down at his keyboard and chose a symbol that was hardly used for anything, the @ sign. Within two years, electronic mail was three quarters of everything on the network. The machines had been linked to share computing power, and their users had turned out to want to talk to each other.

## A network of networks

Other networks soon appeared, using radio, satellites and different rules, and they could not speak to one another. In 1974 two American engineers published a common language for joining them. It specified how packets should be addressed and how the machines at each end should check that everything had arrived, and it said nothing at all about what the packets contained or what kind of wire or radio carried them. Any network that followed these rules could be joined to any other. On 1 January 1983 the original network switched over to them, and the result, a network of networks, was called the internet.

The decisions made by those engineers have shaped everything since. The network was built to be simple and ignorant. It moves packets and does not know or care whether they are part of a letter, a film or a bank transfer. All the intelligence is in the machines at the edges. That meant that anybody could invent a new use for it without asking permission from whoever ran the wires, which no telephone company would have allowed.

It also meant that the network had no means of knowing who anyone was. Its builders were a few hundred researchers who trusted one another, and they did not design it to keep out thieves, spies or liars. A great many later problems of security on the internet go back to that.

No government and no company owned it. Its technical rules were, and are, settled by engineers who meet in open working groups and publish their proposals for anyone to criticise. One of them summed up their creed: we reject kings, presidents and voting. We believe in rough consensus and running code.

## On every desk

Until the mid-1970s computers belonged to institutions. Then the price of chips fell far enough for hobbyists to build one at home. In 1977 two young men who had started in a garage in Silicon Valley put on sale a computer in a plastic case that could be taken out of the box and plugged into a television. In 1981 the largest computer company in the world brought out its own, and bought the basic program that ran it from a small firm whose founder, a twenty-five-year-old named Bill Gates, kept the right to sell it to others. That contract made him the richest man in the world.

Most of what made these machines usable by ordinary people came from a single research laboratory, owned by a maker of photocopiers. In 1973 its scientists built a computer with a screen that showed overlapping windows and little pictures, controlled by a hand-held pointer called a mouse, and connected to others in the building by a cable. Their employer never managed to make money from it. A visitor from the garage firm did.

## Vague but exciting

By the late 1980s the internet joined a few hundred thousand computers, nearly all in universities, and using it required typed commands and a good deal of patience.

At the European laboratory for particle physics, on the border of Switzerland and France, thousands of scientists from dozens of countries came and went, each with his own kind of computer and his own way of filing things, and information was constantly lost. In March 1989 an English physicist on the staff, Tim Berners-Lee, wrote a proposal for dealing with this. The internet could carry messages between machines. His scheme would use it to fetch pages. Any document on any computer would have an address. Any document could contain a link to any other, and a reader who selected the link would be taken straight there, wherever in the world it was. His manager wrote three words across the top: vague but exciting.

He was given time to try. By the end of 1990 he had written the three pieces that were needed: a way of giving every document an address, a set of rules for fetching one from another machine, and a simple code for marking up a page with headings and links. He called the whole thing the World Wide Web. The first website explained what the Web was.

In April 1993 the laboratory announced that anyone could use the technology, for anything, without payment. Berners-Lee had insisted on it. Had it been patented, there would probably have been several rival webs, each behind a toll gate. That same year a team at a university in Illinois, most of them students, released a program that displayed web pages with pictures and let the user move between them by clicking. In 1995 sixteen million people were online. Amazon, Google and Facebook were all founded within ten years of the laboratory's announcement, the last two by students. In 2007 a telephone appeared that was really a computer with a glass screen. By 2024 five and a half billion people, two thirds of humanity, were connected.

## Under the sea

People speak of data as being in the cloud. It is in buildings and on the sea bed.

Almost everything that crosses an ocean on the internet travels as pulses of light through glass fibres, bundled into cables no thicker than a garden hose and laid across the ocean floor by ships. There are about six hundred of them, a million and a half kilometres in all. Many follow the routes of the telegraph cables that the British laid in the nineteenth century, and come ashore at the same beaches.

The pages, films and photographs themselves are kept on rows of computers in windowless warehouses the size of several football pitches, cooled by rivers of water. These already use about one and a half per cent of the world's electricity, and the share is rising fast.

## One island

The most remarkable objects in the whole system are the chips, and the way they are made shows how narrow its base has become.

The features on the most advanced chips are a few dozen atoms across. A beam of light cannot draw a line finer than its own waves. To print such features, the light used must have an extremely short wavelength, and there is one company in the world, in the Netherlands, that makes machines able to do it. Inside each machine, a droplet of molten tin a fraction of the width of a hair is fired across a vacuum, fifty thousand times a second, and each droplet is hit twice by a laser, which turns it into a glowing cloud hotter than the surface of the Sun. The light that it gives off is gathered by mirrors, made by a German firm, that are the smoothest objects ever manufactured. One machine costs about two hundred million dollars and is delivered in forty shipping containers.

The chips are designed, for the most part, in California. The great majority of the most advanced ones are manufactured by a single company in Taiwan, founded in 1987 by an engineer who had been passed over for the top job at an American chip firm. A factory to make them costs twenty billion dollars. No other country can at present do it at the same scale.

Taiwan lies a hundred and sixty kilometres from the coast of China, whose government regards the island as its own territory and has not renounced the use of force to take it. In 2022 the United States restricted the sale of the most advanced chips, and of the machines that make them, to China, and began paying companies to build factories on American soil. The world's most complicated product, on which every bank, hospital, army and telephone depends, comes from a few buildings in the most dangerous strait on Earth.

## Who is in charge

The network that nobody owned is used, by most people, through the services of five or six American companies and a similar number of Chinese ones. One of them answers nine out of ten of the questions that the world types into a search box. They built those services on foundations that the public had paid for: the research agency's network, the physicists' Web, the university grants that supported their founders. Governments that had mostly left the internet alone for twenty years began, in the 2010s, to try in earnest to bring it under their laws. China had done so from the start.

In the logbook that is kept at the university in Los Angeles, the entry for 29 October 1969 takes up one line in blue ink, between notes about loading programs and testing the telephone connection. The professor in charge of the laboratory has said that if he had known what it would become, he would have arranged for a better first message. As it was, the network's first word was "lo", as in lo and behold.
