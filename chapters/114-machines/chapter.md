# 114. What is artificial intelligence?

*The world, from 1950 to 2025*

Artificial intelligence, in the form that now matters, is software that has learned from examples, in place of following rules that somebody wrote down. Nobody tells it how to recognise a face or compose a sentence. It is shown millions of faces, or billions of sentences, and it adjusts itself until it can. In the last few years such systems have learned to write, draw, translate and reason well enough to do work that had always needed a person.

In 2013 the tax office of the Netherlands began using a computer system to search for fraud among families who claimed a benefit that helps with the cost of childcare. The system gave each application a score for risk. It had been built from the records of earlier cases, and it weighed dozens of facts about each family. One of the facts that its designers gave it was whether the applicant was a Dutch national, and those who were not scored higher.

A family that the system flagged was investigated, and thousands of them then received a letter. It said that they had claimed money to which they were not entitled and must repay all of it, back to the first year, at once. The sums ran to tens of thousands of euros. No reason was given. When parents telephoned to ask what they had done wrong, the officials could not tell them why they had been picked out, because the officials did not know either. Often the offence was a missing signature or a form filed late.

About twenty-six thousand families were treated in this way over six years. People lost their homes and their jobs. Marriages broke up. More than a thousand children were taken into care. It took a small group of parents, one lawyer and two journalists years to establish what had happened. In January 2021 the entire Dutch government resigned over it.

## A summer's work

The idea that a machine might think is as old as the computer. In 1950 Alan Turing, the English mathematician who had described the universal computing machine, published a paper that began with the question: can machines think? He proposed a test. If a person exchanging typed messages with a machine could not tell that it was not another person, the question was settled as far as it ever could be.

Six years later ten American scientists gathered for a summer at a college in New Hampshire to study what one of them had named artificial intelligence. Their proposal said that they thought a significant advance could be made if a carefully selected group worked on it together for a summer.

It took rather longer. For thirty years most researchers tried to build intelligence by writing down rules. A program for medical diagnosis would be given thousands of statements of the form: if the patient has a fever and a rash, consider measles. This worked for tasks with clear rules, such as chess. In 1997 a machine that could examine two hundred million positions a second beat the world champion. It failed at almost everything that a small child does without effort. Nobody could write down the rules for telling a cat from a dog, or for understanding a joke, because nobody knows what rules they follow when they do it.

## Learning

A second approach had been tried from the start and mostly dismissed. It took its inspiration from the brain, which is a mass of cells, each connected to thousands of others, and which learns by strengthening some connections and weakening others.

The artificial version is called a neural network, and it is made of numbers. Imagine wanting a machine to say whether a photograph shows a cat. The photograph is turned into a long list of numbers, one for the brightness of each dot. These are fed into a first layer of simple units. Each unit multiplies its inputs by a set of numbers called weights, adds up the results, stays silent if the total is too small, and otherwise passes its answer to the units in the next layer, which do the same, and so on through many layers. Out of the last layer comes a single number, the machine's estimate of how likely the picture is to be a cat.

At the start the weights are random and the answer is rubbish. The machine is then shown a picture that a person has already labelled. Its answer is compared with the label, and a piece of mathematics works backwards through the layers, calculating for every single weight whether a slight increase or a slight decrease would have made the answer a little less wrong. Each weight is nudged accordingly. Then the next picture is shown. After millions of pictures and billions of nudges, the weights have settled into a pattern that picks out cats, including cats that the machine has never seen. Nobody chose those weights, and nobody can read off from them how the machine decides. The network may have a hundred million of them.

![Diagram of one step in training a small neural network of three layers. A picture of a cat, made of dots and labelled "cat" by a person, is turned into numbers, one for the brightness of each dot, which go into the first layer. Lines, the weights, join each unit to every unit of the next layer, and the next layer to a single unit in the last layer, which gives the guess, 0.3. The guess is compared with the label, 1, for an error of 0.7. A dashed arrow runs backwards through the layers, and some of the weights are marked as nudged up or down](images/diagram_network.png)
*One step in training a small neural network: a labelled picture goes in as numbers, a guess comes out, the guess is compared with the label, and every weight is nudged to make the answer a little less wrong. Diagram: drawn for this book.*

The first and far simpler machine of this kind was built in 1958, and a leading newspaper reported that the navy expected it to walk, talk, see, write, reproduce itself and be conscious of its existence. It could barely tell left from right. The method fell out of favour for decades. A handful of researchers kept at it, among them an English psychologist in Canada, Geoffrey Hinton, who was told repeatedly that he was wasting his career.

## Two video-game cards

The method needed far more examples and far more arithmetic than anyone had been able to give it.

The examples came first. A computer scientist who had come to America from China as a teenager decided that the field needed a far larger collection of labelled pictures than anyone had thought worth making. She gathered fourteen million photographs from the internet. The labels were supplied by nearly fifty thousand people in a hundred and sixty-seven countries, who were paid a few cents a picture through a website that farms out small tasks.

Speed came from an unexpected quarter. The arithmetic of a neural network consists of an enormous number of simple multiplications that can all be done at once. Chips designed for exactly that already existed. They had been built to draw the moving pictures in video games.

In 2012 two of Hinton's students trained a network on that collection of photographs, using two video-game cards in a bedroom, and entered it in the annual competition for recognising objects in pictures. The next best entry failed on one picture in four. Theirs failed on one in seven. Within three years such networks were making fewer mistakes on that test than people did.

After that the results came quickly. In March 2016, in a hotel in Seoul, a program beat one of the world's strongest players at Go, an ancient board game with more possible positions than there are atoms in the universe, which experts had thought was a decade beyond any machine. Two hundred million people watched. In the second game the program made a move so strange that the commentators took it for a blunder. It was the move that won. The program itself reckoned that a human player would have made it one time in ten thousand.

In 2020 a network solved a problem that biologists had been working on for half a century, which is how to predict the folded shape of a protein from the list of its parts. Proteins are the molecules that do nearly all the work in a living cell, and what each one does depends on its shape. Predicted shapes for two hundred million of them were soon published free. In 2024 the Nobel prizes for both physics and chemistry went to people who work on these systems, Hinton among them.

## The next word

The machines that most people have met are of one particular kind, and they are trained to do something that sounds trivial.

In 2017 eight researchers at an American internet company published a new design of network that was especially good at handling language. A model of this design is given the beginning of a piece of text and asked to guess the next word. Its guess is compared with the word that actually came next, and its weights are nudged. This is repeated across a library far larger than any person could read in a thousand lifetimes: a large part of the public internet, with millions of books, articles, conversations and computer programs.

To predict the next word well, it turns out, a system has to absorb a great deal about what the words refer to. To continue a sentence about the boiling point of water at the top of a mountain, it helps to have captured something about air pressure. To continue a line of computer code, it helps to have captured how the language works. Whether this amounts to understanding is argued over. The practical result is a machine that can answer a question, summarise a report, translate between languages, write a working program, or produce a poem in the manner of any poet, by generating one likely word after another.

On 30 November 2022 a company in San Francisco put such a model on the internet with a box to type into, and called it ChatGPT. A hundred million people were using it within two months, which was faster than any product on the internet had been taken up before. By 2025 it had eight hundred million users a week. Other models make pictures, music and film from a typed description. This book was written with the help of one.

They have a characteristic fault. A system built to produce a likely continuation will produce one whether or not it is true. Asked for a reference, it will supply an author, a title and a page number, all perfectly plausible and sometimes all invented. In 2023 a lawyer in New York submitted a brief to a court citing six earlier cases in support of his client. The judge could not find them. The lawyer had asked a language model, which had made them up, complete with quotations. He and his firm were fined five thousand dollars.

## What it is made of

A model of this kind looks like pure thought, floating free. It rests on the same sort of foundations as every powerful technology before it.

It needs chips. Most of the ones used for training are designed by a single American firm, Nvidia, which began by making cards for video games and in 2025 became the most valuable company in the world, and they are manufactured in the factories of Taiwan. One chip costs about as much as a car, and the largest models are trained on hundreds of thousands of them.

It needs electricity. The world's data centres already consume about one and a half per cent of its supply, a share that these chips are driving up fast, and the companies that own them have been signing contracts to restart closed nuclear power stations.

It needs the written and drawn work of other people. Most of the models were trained on books, newspapers, paintings and photographs that were copied without asking and without payment. Authors, artists and publishers have sued, and in 2025 one of the companies, which had built its library partly from pirated copies, agreed to pay writers and publishers a billion and a half dollars.

And it needs labour. Before a model is released, people must label its training examples and teach it what not to say, which means reading and marking thousands of descriptions of violence and abuse. Much of that work has been done in Nairobi, Manila and Caracas, for one or two dollars an hour.

The most capable models belong to a handful of companies. In 2025 the four largest of them together spent more than three hundred billion dollars on buildings and chips, which is more than the yearly cost, in today's money, of the programme that put men on the Moon at its height.

## Work

Each great change in technology has altered who does what. Writing created the clerk. The printing press put the copyists of manuscripts out of work and made a living for typesetters. New machines destroyed the trades of the stocking knitters and handloom weavers of England, some of whom, in 1811 and 1812, took hammers to them. Those craftsmen were right about what would happen to them. Their grandchildren were better off, but it took two generations for the gains from the factories to reach the people who worked in them.

What is different this time is the kind of work. Earlier machines replaced muscle and then routine. This one produces text, pictures, computer code and analysis, which are what office workers, translators, illustrators, programmers and call-centre staff are paid for. An international body estimated in 2024 that two jobs in five in the world, and three in five in the rich countries, involve tasks that such systems could change.

What has actually been measured so far is modest. When a large company gave a language model to five thousand of its customer-service agents, they resolved about a seventh more customers' problems an hour, and the improvement was largest among the newest and least skilled, who were in effect being handed the habits of the best. Whether that means better jobs or fewer jobs depends on who owns the system and who decides how the gain is shared, as it did with the loom.

## Decisions

The other use of these systems is to judge people. They decide, or help to decide, who is offered a loan, shortlisted for a job, stopped at a border, or investigated for fraud.

A system that learns from past decisions learns the prejudices in them. A large online retailer built a program to sort job applications, trained on the applications that it had received over ten years, most of which came from men. The program taught itself to mark down any application that contained the word "women's". The company scrapped it. In January 2020 a man in Detroit was arrested on his front lawn, in front of his daughters, because a face-recognition system had matched a blurred image from a shop's security camera to his driving licence photograph. He had not been near the shop. Tests by a government laboratory had found that many such systems made far more mistakes with dark faces than with pale ones.

The deeper difficulty is explanation. A clerk who refuses a benefit can be asked why. A network with a billion weights cannot answer in a way that a person can readily check. Its makers themselves often cannot say why it gave one answer and not another.

The European Union passed a law in 2024 that bans some uses outright, such as scoring citizens for general trustworthiness, and requires that systems used for certain serious decisions about people, in hiring, credit, policing and the like, be documented, tested for bias, and overseen by a human being who is able to overrule them.

## Three predictions

About what comes next, the people who know most disagree. Some of them are afraid. In May 2023 several hundred researchers and executives, including the heads of the three leading laboratories and two of the scientists who had done most to invent the method, signed a statement of a single sentence. Mitigating the risk of extinction from AI, it said, should be a global priority alongside other societal-scale risks such as pandemics and nuclear war. Their reasoning is that a system far more capable than any person, pursuing whatever goal it had been given, might not be something that its makers could correct or switch off. That month Hinton resigned from his post so that he could say so freely.

Others hold that the danger lies in going too slowly. They point out that these systems may cure diseases, speed up science and make every person on Earth richer, and that each year of delay costs lives. They add that if cautious countries hold back, less cautious ones will not.

A third group expects people and machines to merge. In January 2024 a man who had been paralysed from the shoulders down in a diving accident had a device the size of a coin set into his skull, with threads finer than a hair reaching into his brain. Within weeks he was moving a cursor on a screen and playing chess by thinking about it.

A fourth view is that all three are carried away. On this account the language models are elaborate mimics, which reproduce the patterns of human writing with no grasp of what any of it means, and the talk of salvation and extinction serves mainly to sell them.

Nothing in the record so far settles which of these is right.

## Who decides

For the present, the decisions are being made by the companies. They choose what the systems are trained on, what they will refuse to do, and when they are safe enough to release, and they are racing one another.

Governments have begun to assert themselves. In November 2023 the representatives of twenty-eight countries, including the United States and China, met for two days at the country house north of London where Turing and his colleagues had broken the German ciphers, and signed a declaration that the most advanced systems posed risks that no country could manage alone. Institutes to test the systems and a yearly scientific report have followed, and no binding rules. The United States withdrew the main safety order of its previous government in 2025. China requires its companies to keep their models in line with the views of the party.

The choice is among the futures that every powerful technology in this story has offered: control by a few owners, oversight by public bodies, or agreement among nations. Printing, the railway and the atom each went through some version of all three.

At the beginning of this story there was a small clay tablet from the city of Uruk, more than five thousand years old. It recorded a quantity of barley, and it carried the mark of the official who had charge of it. Writing was invented to keep that kind of record, of who had delivered what and who was owed what. It was read by the few people who had been trained to read it. A farmer who believed that the count was wrong had to find someone who could tell him what the tablet said, and then someone with the power to change it.

The parents in the Netherlands were in the farmer's position. Somewhere there was a record with their names in it, and a score, and they were not allowed to see either. The machine is new. The questions to ask of it are the old ones: who can read the record, who can challenge a decision made from it, and who will put it right.
