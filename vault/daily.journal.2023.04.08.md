---
id: ge4pfttacj237tzemmg0li6
title: "2023-04-08"
desc: ""
updated: 1680948448443
created: 1680946835724
traitIds:
  - journalNote
---

The fast.ai book goes into much more detail than the course. It's quite cool.

High level learnings from Chapter 5:

- Multi-class classifiers use cross-entropy loss which you get by softmax followed by negative log likelihood
- fastai uses different learning rates, slower for base layers and faster for newer layers. This is called discriminative learning rates.
- if selecting number of epochs, a good idea is to train it for as long as you can wait and then see how good the results are.
- Kaggle is slow as fuck. Things that take 20s in the fastai notebook take 2 minutes on the kaggle notebook.

I still need to figure out a good small project to start with.
