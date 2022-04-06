---
id: ekao8hGT2ytEtvmeZjp6q
title: Kraft Inequality
desc: ''
updated: 1649237499946
created: 1649177852066
---

Source: [[books.art_of_doing_science_and_engineering]]

The Kraft inequality gives a limit on the lengths $l_i$ of each symbol in the alphabet.

$$
K = \sum_{i=1}^q 1/2^l_i \leq 1
$$

## Proof

by induction

base case: trivially true for q = 1 and q = 2

* $K = 1$ for $q = 1$
* $K = 1$ for $q = 2$

Induction:

true for $K'$ and $K''$

we join these trees, increasing length of each node by one, adding a factor of two to the denominator.

$$
K'/2 + K''/2 \leq 1
$$
