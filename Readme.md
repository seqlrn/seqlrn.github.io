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

_Exact deadlines are set on the Moodle assignments!_

- April 11: [Assignment 1 (Dynamic Programming)](https://github.com/seqlrn/1-dynamic-programming)
- April 25: [Assignment 2 (Markov Chains)](https://github.com/seqlrn/2-markov-chains)
- May 16: [Assignment 3 (Hidden Markov Models)](https://github.com/seqlrn/3-hmm)
- Juyne 6: [Assignment 4 (Neural Networks)](https://github.com/seqlrn/4-nnets) (_note:_ due date updated)
- June 27: [Assignment 5 (Attention)](https://github.com/seqlrn/5-attention) (_note:_ due date updated)
- June 27: [Assignment 6 (Transformers)](https://github.com/seqlrn/6-transformers)
- Week of July 5: oral exams; **schedule was distributed via email!**


## Recommended Textbooks

- Chao, K.-M. and Zhang, L.: [Sequence Comparison](https://link.springer.com/book/10.1007%2F978-1-84800-320-0) (Springer). [available online through Ohm Library](https://ebookcentral.proquest.com/lib/thnuernberg/reader.action?docID=418343)
- Sun, R., Giles, L. and van Leeuwen, J.: [Sequence Learning: Paradigms, Algorithms and Applications]() (Springer). [available online through Ohm Library](https://ebookcentral.proquest.com/lib/thnuernberg/detail.action?docID=3072729)
- Huang, Acero, Hon: _Spoken Language Processing: A Guide to Theory, Algorithm and System Development._ (ISBN-13: 978-0130226167)
- Jurafsky, D and Martin, J: _Speech and Language Processing._ 2017 ([available online](http://web.stanford.edu/~jurafsky/slp3/))
- Manning, C, Raghavan P and Schütze, H: _Introduction to Information Retrieval_, Cambridge University Press. 2008. ([available online](https://nlp.stanford.edu/IR-book/))
- Goodfellow, I and Bengio,Y and Courville, A: _Deep Learning._ 2016 ([available online](http://www.deeplearningbook.org/))
- Schukat-Talamazzini, E.-G. Automatische Spracherkennung. 1995 ([available online](https://www.minet.uni-jena.de/fakultaet/schukat/asebuch.html))

**Please note the _required reading_ remarks in the syllabus.**


## Syllabus


- **March 22: Introduction** ([slides](/pdf/01-introduction.pdf))

	We'll start with the general concepts of supervised vs. unsupervised learning and classification of independent observations vs. sequences of observations.
	To get you motivated, we'll look at a list of recent "AI products" that utilize sequence learning, as well as some of our related research projects.

- **March 22: Comparing Sequences** ([slides](/pdf/dp_and_edit_dist.pdf))
	
	We'll start with looking at discrete sequences and how to (pair-wise)compare them using dynamic programming algorithms.

	_Required reading_: Chao/Zhang Ch. 1.2 through 1.4, 2.4 and 3.

- **March 29: Cost Functions and States** ([slides](/pdf/03-costs-states.pdf))
	
	We'll look at more fine-grained ways of modeling distances and similarities.
	Understand how DP can be used on an abstraction of states, and how that can be used for simple sequence decoding.

> _April 5: no class (Easter)_

- **April 12: Markov Chains** ([slides](/pdf/04-markov-chains.pdf))
	
	Learn about Markov chains (aka. n-grams), a simple yet effective approach to learn contexts of distcrete symbols.

	_Required reading_: Schukat-Talamazzini Ch. 7.2.{1,2}, 7.3

> _April 19: no class_


- **April 26: Hidden Markov Models: Basics** ([slides](/pdf/hmm.pdf) curtesy of [Elmar Nöth](https://lme.tf.fau.de/person/noeth/))

	We'll take a close look at hidden Markov models and how to (efficiently) evaluate and train them.
	The Viterbi decoding algorithm tells us the most likely sequence and the path that lead to it.

	_Required reading_: Schukat-Talamazzini Ch. 5

- **May 3: HMM: Higher-Level Sequence Modeling and Decoding** ([slides](/pdf/decoding.pdf) curtesy of [Elmar Nöth](https://lme.tf.fau.de/person/noeth/))

	Using one HMM per class, we can do multi-class ("word") recognition.
	By modeling shared subwords, we can model a large number of classes while keeping the actual number of parameters under control.
	Learn how to decode sequences of arbitrary length using beam search.

	_Required reading_: Schukat-Talamazzini Ch. 8

- **May 10: Feed-Forward Neural Networks** ([slides pt. 1](/pdf/nnets.pdf) curtesy of Stefan Steidl, [slides pt. 2](/pdf/06b-nnets-sequences.pdf))
	
	After a brief introduction to neural network (fundamentals, topologies and training), we look at how to apply those to sequential data.
	Namely, we'll look at three concrete examples: Word2Vec, TDNN, ConvNets and HMM-DNN.

	_Strongly recommended: [Deep Learning with PyTorch](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)_
	
	_Required Reading_:
	- Karpathy 2016: [Yes you should understand backprop](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b)
	- Mikolov et al., 2013. [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
	- Waibel et al., 1989. [Phoneme Recognition Using Time-Delay Neural Networks](http://www.cs.toronto.edu/~fritz/absps/waibelTDNN.pdf)
	- LeCun et al., 1998. [Gradient-based learning applied to document recognition](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)

	
- **May 17: Recurrent Neural Networks** (slides based on Chris Manning's [cs224n](http://web.stanford.edu/class/cs224n/): slides [1](http://web.stanford.edu/class/cs224n/slides/cs224n-2021-lecture05-rnnlm.pdf), [2](http://web.stanford.edu/class/cs224n/slides/cs224n-2021-lecture06-fancy-rnn.pdf) and [notes](http://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes05-LM_RNN.pdf); see Moodle for relevant subset)

	Recurrent neural networks use feedback loops to introduce temporal context or "memory" into the network.
	We look at causes of vanishing gradient, and how it can be mitigated using long short-term memory (LSTM) networks or gated recurrent units (GRUs).

	_Recommended Readings:_ 
	- Pascanu et al. "[On the difficulty of training recurrent neural networks](http://proceedings.mlr.press/v28/pascanu13.pdf)"
	- Chris Olah "[Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)"

> _May 24: no class (Pentecost)_

- **May 31: Sequence-to-Sequence and Attention** (slides for [ctc](/pdf/ctc.pdf); more slides based on Chris Manning's cs224n NMT [slides](http://web.stanford.edu/class/cs224n/slides/cs224n-2021-lecture07-nmt.pdf) and [notes](http://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes06-NMT_seq2seq_attention.pdf), see Moodle for relevant subset)

	After a brief digression into _connectionist temporal classification_ (CTC), we'll look neural machine translation (NMT) as a _sequence to sequence_ (seq2seq, s2s) encoder-decoder example, before diving into attention, a modeling concept which allows the networks to learn an even better understanding of the context.

	_Required Readings:_
	- [Pytorch Seq2Seq Tutorial](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)

- **June 7: Self-Attention and Transformers** (slides based on Chris Mannings and John Hewitt's cs224n [slides](http://web.stanford.edu/class/cs224n/slides/cs224n-2021-lecture09-transformers.pdf) and [notes](http://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes07-QA.pdf); see Moodle for relevant subset)

	We'll revisit attention and have a closer look how self-attention and positional encodings as a more efficient way to look at sequence context.
	Transformers use self- and cross-attention (and a number of other tricks) to form a recurrence-free network topology that can be efficiently trained.

	_Required Readings:_
	- Łukasz Kaiser: [Attention is all you need](https://www.youtube.com/watch?v=rBCqOTEfxvg), esp. at 15:45ff.

	_Recommended Readings:_
	- Vaswani et al. "[Attention Is All You Need](https://arxiv.org/abs/1706.03762.pdf)"
	- Jay Alammar "[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)"

- **June 14: Pre-Training and Transfer Learning** (slides based on Chris Mannings and John Hewitt's cs224n [slides](http://web.stanford.edu/class/cs224n/slides/cs224n-2021-lecture10-pretraining.pdf) and [notes](http://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes07-QA.pdf); see Moodle for relevant subset)

	We'll look back at some occasions where we already used pre-training, maybe without realizing it.
	The concept of masking together with pseudo-targets allow us to leverage large amounts of unlabeled data to pre-train large models, before fine-tuning them to the actual tasks.

	_Required Readings:_
	- Devlin et al. "[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805)"

	_Recommended Readings:_
	- Radford et al. "[Improving Language Understanding by Generative Pre-Training](https://www.cs.ubc.ca/~amuham01/LING530/papers/radford2018improving.pdf)"
	
> _June 21: no class_

- **June 28: Reinforcement Learning**

	We'll look at a different kind of temporal sequences: actions and rewards in an interactive environment such as board games.
	We'll start with basic Q-learning and then expand to Deep-Q-Learning.

- Week of July 5: Oral Exams


_Subscribe to [https://github.com/sikoried/sequence-learning/](https://github.com/seqlrn/seqlrn.github.io/) to follow updates._
