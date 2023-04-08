---
id: utb5wjh3p73ne5fg0fwb1n3
title: Cross Entropy Loss
desc: ""
updated: 1680945507674
created: 1680427351525
---

- Cross-entropy loss works with multiple categories
- Results in faster and more reliable training
- default in fastai

When we first take the softmax, and then the log likelihood of that,
that combination is called cross-entropy loss. In PyTorch, this is
available as `nn.CrossEntropyLoss` (which, in practice, actually
does log_softmax and then nll_loss).
