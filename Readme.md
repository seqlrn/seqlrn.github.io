_Elective for [CS graduate students](https://www.th-nuernberg.de/fakultaeten/in/studium/masterstudiengang-informatik/) at the [Technische Hochschule Nürnberg](https://www.th-nuernberg.de/)._


## Class Schedule and Credits

**Time and Location:**  Mondays & Tuesdays at 11.30a (**SP.467**)

**Announcements and Discussions:** Join on Teams wih code: `endtu0s`.

Each week, we will discuss algorithms and their theory before implementing them to get a better hands-on understanding.
The materials consist of a mix of required and recommended readings, slides as well as a set of mandatory programming and analysis assignments.
Pair programming encouraged, [_BYOD_](https://en.wikipedia.org/wiki/Bring_your_own_device) strongly recommended!


### Assignments

Lectures are accompanied by mandatory assignments that will be reviewed and discussed every week.
All assignments are in form of prepared [`python3` jupyter notebooks](https://github.com/seqlrn/assignments).
Depending on the topic, they consist of programming, evaluation and/or discussion sections.
Please submit the notebooks (including state/rendered cells) the Teams channel under [`Files > Assignment Submissions`](https://technischehochschulen.sharepoint.com/:f:/r/sites/SeqLrn2024/Freigegebene%20Dokumente/General/Assignment%20Submissions?csf=1&web=1&e=Ne8upU) (see schedule below).
Pair-programming is encouraged, but everyone needs to submit an individual file.


### Credits

Credits are earned through two components:

1. All assignments must be completed on time (see schedule below; pass/fail).
2. Oral exam (20') covering theory and assignments (graded; individual exams).


_Note: Materials will be (mostly) in English, the lectures/tutorials will be taught in German unless English speaker present; oral exam in language of choice._


## Recommended Textbooks

- Chao, K.-M. and Zhang, L.: [Sequence Comparison](https://link.springer.com/book/10.1007%2F978-1-84800-320-0) (Springer). [available online through Ohm Library](https://ebookcentral.proquest.com/lib/thnuernberg/reader.action?docID=418343)
- Sun, R., Giles, L. and van Leeuwen, J.: [Sequence Learning: Paradigms, Algorithms and Applications]() (Springer). [available online through Ohm Library](https://ebookcentral.proquest.com/lib/thnuernberg/detail.action?docID=3072729)
- Huang, Acero, Hon: _Spoken Language Processing: A Guide to Theory, Algorithm and System Development._ (ISBN-13: 978-0130226167)
- Jurafsky, D and Martin, J: _Speech and Language Processing._ 2017 ([available online](http://web.stanford.edu/~jurafsky/slp3/))
- Manning, C, Raghavan P and Schütze, H: _Introduction to Information Retrieval_, Cambridge University Press. 2008. ([available online](https://nlp.stanford.edu/IR-book/))
- Goodfellow, I and Bengio,Y and Courville, A: _Deep Learning._ 2016 ([available online](http://www.deeplearningbook.org/))
- Schukat-Talamazzini, E.-G. Automatische Spracherkennung. 1995 ([available online](https://www.minet.uni-jena.de/fakultaet/schukat/asebuch.html))

**Please note the _required reading_ remarks in the syllabus.**


## Schedule

| Date | Topic | Required Reading | Materials | Assignment due |
|------|-------|------------------|-----------|----------------|
Mar 17 | no class
Mar 18 | comparing sequences: ED/Levenshtein, NW, DTW, modeling cost; intro A1	| Chao/Zhang Ch. 1.2 through 1.4, 2.4 and 3.	| [introduction](/pdf/00-introduction.pdf), [comparing sequences](/pdf/01-comparing-sequences.pdf)	| 
Mar 24 | no class
Mar 25 | Assignment 1 | | [A1 Dynamic Programming](https://github.com/seqlrn/assignments/tree/master/1-dynamic-programming)
Mar 31 | Markov chains: statistical modeling of discrete sequences; discussion A1, intro A2	| Schukat-Talamazzini Ch. 7.2.{1,2}, 7.3	| [markov chains](/pdf/02-markov-chains.pdf)	| A1
Apr 1 | review A1; Assignment 2 | | [A2 Markov chains](https://github.com/seqlrn/assignments/tree/master/2-markov-chains) |
Apr 7 | HMMs, pt. 1: basics, BW, time-alignments; intro A3.1; 	| Schukat-Talamazzini Ch. 5 & 8	| [Hidden Markov Models](/pdf/hmm.pdf) | A2
Apr 8 | review A2; Assignment 3, pt. 1 | | [A3 HMM](https://github.com/seqlrn/assignments/tree/master/3-hmm) |
Apr 14 | HMMs, pt. 2: Viterbi, beam-decoding, higher order modeling; intro A3.2 | [Decoding](/pdf/decoding.pdf) curtesy of [Elmar Nöth](https://lme.tf.fau.de/person/noeth/)
Apr 15 | Assignment 3, pt. 2 | | [A3 HMM](https://github.com/seqlrn/assignments/tree/master/3-hmm)
Apr 21 | no class (Easter)
Apr 22 | no class (Easter)
Apr 28	| nnets 1: fundamentals, FF, AE, Word2Vec, FastText, ConvNets, embeddings, HMM-DNN; intro A4	| Karpathy 2016: [Yes you should understand backprop](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b), Mikolov et al., 2013. [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), Waibel et al., 1989. [Phoneme Recognition Using Time-Delay Neural Networks](http://www.cs.toronto.edu/~fritz/absps/waibelTDNN.pdf), LeCun et al., 1998. [Gradient-based learning applied to document recognition](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)	|[nnets basics](/pdf/nnets.pdf), [nnets pt.1](/pdf/04-nnets-1.pdf)	| A3
Apr 29  | Assignment 4 | | [A4 nnets](https://github.com/seqlrn/assignments/tree/master/4-nnet)
May 5 | no class
May 6 | no class
May 12	| nnets2: RNN, LSTM, GRU; intro A5	| [Pytorch Seq2Seq Tutorial](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html), Pascanu et al. [On the difficulty of training recurrent neural networks](http://proceedings.mlr.press/v28/pascanu13.pdf), Chris Olah [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)	| [slides](/pdf/07-recurrent_updated.pdf) | A4
May 13 | Assignment 5 | | [A5 RNN](https://github.com/seqlrn/assignments/tree/master/5-nnet_rnn)
May 19	| nnets3: s2s, Attn, CTC, RNN-T; intro A6	| Graves et al., 2006. [Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks](https://www.cs.toronto.edu/~graves/icml_2006.pdf), Loren Lugosch's [Introduction to RNN-T](https://lorenlugosch.github.io/posts/2020/11/transducer/), Graves et al., 2012. [Sequence Transduction with Recurrent Neural Networks](https://arxiv.org/abs/1211.3711)	| [attention](/pdf/08-attention_updated.pdf), [ctc](/pdf/ctc.pdf), [rnn-t](/pdf/gatech_cs7643_24_subset.pdf) [transfer learning](/pdf/09-transfer.pdf)	| A5
May 20 | Assignment 6 | [A6 attention](https://github.com/seqlrn/assignments/tree/master/6-nnet_attn)
May 26	| tranformers: basics, architectures for text (BERT, SBERT, GPT) and speech (Wav2Vec2); intro A8 | Łukasz Kaiser: [Attention is all you need](https://www.youtube.com/watch?v=rBCqOTEfxvg), esp. at 15:45ff. Vaswani et al. [Attention Is All You Need](https://arxiv.org/abs/1706.03762.pdf), Jay Alammar [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), Devlin et al. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805), [wav2vec: Unsupervised Pre-training for Speech Recognition](https://arxiv.org/abs/1904.05862), Radford et al. [Improving Language Understanding by Generative Pre-Training](https://www.cs.ubc.ca/~amuham01/LING530/papers/radford2018improving.pdf)	| [attention](/pdf/08-attention_updated.pdf), [ctc](/pdf/ctc.pdf), [rnn-t](/pdf/gatech_cs7643_24_subset.pdf) [transfer learning](/pdf/09-transfer.pdf)	| A6
Jun 2	| LLMs as foundation models: benchmarks, GPT, BPE, data (pretraining and fine-tuning), instructGPT, RLHL; intro A9; conditioning of transformers: zero-/few-shot, CoT	| 	[road to gpt](/pdf/10-gpt.pdf) | 	| 
Jun 3 | Assignment 7 | | [A7 Transformers](https://github.com/seqlrn/assignments/tree/master/7-transformers_wav2vec)
Jun 9 | no class (Pentecost)
Jun 10 | no class (Pentecost)
Jun 16 | no class
Jun 17 | no class
Jun 23	| reinforcement learning; discussion A9 & A10; intro A11	| [reinforcement learning](/pdf/11-reinforcement-learning.pdf)	| 	| A7
Jun 24 | Assignment 8 | | [A8 Summarization](https://github.com/seqlrn/assignments/tree/master/8-transformers_sum)
Jun 30 | state space models (tbd) | | | A8
Jul 1 | wrap-up 
Calendar Week 28 | Exam week 



_Subscribe to [https://github.com/sikoried/sequence-learning/](https://github.com/seqlrn/seqlrn.github.io/) to follow updates._
