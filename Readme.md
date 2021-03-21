# Sequence Learning

_Elective for [CS grad students](https://www.th-nuernberg.de/fakultaeten/in/studium/masterstudiengang-informatik/) at the [Technische Hochschule Nürnberg](https://www.th-nuernberg.de/)._


## Class Schedule and Credits

**Time and Location:** Mondays at 9.45a (online, Zoom link on Moodle)

**Announcements and Discussions:** [Moodle Course #5312](https://elearning.ohmportal.de/course/view.php?id=5312)

**Teams** for discussion around assignments: `4fbxju8`.

Each week, we will discuss algorithms and their theory before implementing them to get a better hands-on understanding.
The materials consist of a mix of required and recommended readings, slides as well as a set of programming assignments.
These assignments are mandatory and in `python3`.
Pair-programming encouraged, [_BYOD_](https://en.wikipedia.org/wiki/Bring_your_own_device) strongly recommended!


### Credits

Credits are earned through two components:

1. All six assignments (dynamic programming, Markov chains, hidden Markov models, recurrent neural networks, attention, transformer) must be completed throughout the semester; assigments are ass/fail, pair programming encouraged (ie. you can submit as teams of two).
2. Oral exam (20') covering theory and assignments (graded; individual exams).


_Note: Materials will be (mostly) in English, the lectures/tutorials will be taught in German unless English speaker present; oral exam in language of choice._


### Important Dates

_TBA_


## Recommended Textbooks

- Chaeo, K.-M. and Zhang, L.: [Sequence Comparison](https://link.springer.com/book/10.1007%2F978-1-84800-320-0) (Springer). [available online through Ohm Library](https://ebookcentral.proquest.com/lib/thnuernberg/reader.action?docID=418343)
- Sun, R., Giles, L. and van Leeuwen, J.: [Sequence Learning: Paradigms, Algorithms and Applications]() (Springer). [available online through Ohm Library](https://ebookcentral.proquest.com/lib/thnuernberg/detail.action?docID=3072729)
- Huang, Acero, Hon: _Spoken Language Processing: A Guide to Theory, Algorithm and System Development._ (ISBN-13: 978-0130226167)
- Jurafsky, D and Martin, J: _Speech and Language Processing._ 2017 ([available online](http://web.stanford.edu/~jurafsky/slp3/))
- Manning, C, Raghavan P and Schütze, H: _Introduction to Information Retrieval_, Cambridge University Press. 2008. ([available online](https://nlp.stanford.edu/IR-book/))
- Goodfellow, I and Bengio,Y and Courville, A: _Deep Learning._ 2016 ([available online](http://www.deeplearningbook.org/))


## Syllabus


- **March 22: Introduction** 

	We'll start with the general concepts of supervised vs. unsupervised learning and classification of independent observations vs. sequences of observations.
	To get you motivated, we'll look at a list of recent "AI products" that utilize sequence learning, as well as some of our related research projects.

- **March 22: Comparing Sequences.**
	
	We'll start with looking at discrete sequences and how to (pair-wise)compare them using dynamic programming algorithms.

- **March 29: States and Cost Functions.**
	
	Understand how DP can be used on an abstraction of distances and states, and how that can be used for simple sequence decoding.

> _April 5: no class (Tuesday following Easter)_

- **April 12: Markov Chains**
	
	Learn about Markov chains (aka. n-grams), a simple yet effective approach to learn contexts of distcrete symbols.

- **April 19: Hidden Markov Models: Basics**
	
	We'll take a close look at hidden Markov models and how to (efficiently) evaluate and train them.
	The Viterbi decoding algorithm tells us the most likely sequence and the path that lead to it.
	
- **April 26: HMM: Higher-Level Sequence Modeling**
	
	Using one HMM per class, we can do multi-class ("word") recognition.
	By modeling shared subwords, we can model a large number of classes while keeping the actual number of parameters under control.

- **May 3: HMM: Decoding**

	Learn how to decode sequences of arbitrary length using beam search.

- **May 10: Feed-Forward Neural Networks**
	
	After a brief introduction to neural network (fundamentals, topologies and training), we look at how to apply those to sequential data.
	
- **May 17: Recurrent Neural Networks**

	Recurrent neural networks use feedback loops to introduce temporal context or "memory" into the network.

> _May 24: no class (Pentecost)_

- **May 31: Attention**

	Attention is a modeling concept which allows the networks to learn an even better understanding of the context.
	We'll study them using two examples: language modeling and sentiment analysis.

- **June 7: Transformers and Transfer Learning**

	Large-scale self-attention-based Transformer networks can be pretrained on large amounts of unlabaled data before fine-tuning them to actual classification tasks.

- **June 14: Sequence-to-Sequence Learning**

	Encoder-decoder networks are a special kind of topology of recurrent neural networks that can be used to model sequence to sequence mappings.
	
> _June 21: no class_

- **June 28: Anomaly Detection**

	We look at algorithms to detect anomalies in sequences of data.
	We'll start with basic algorithms as BUTLA and OTALA, and extend to auto-encoder based approaches.

- Week of July 5: Oral Exams


_Subscribe to [https://github.com/sikoried/sequence-learning/](https://github.com/seqlrn/seqlrn.github.io/) to follow updates._
