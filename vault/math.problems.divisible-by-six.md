---
id: lihhzm67e3lt6t8gop1j1f9
title: Divisible by Six
desc: ''
updated: 1651158897632
created: 1651158442967
---

* Book: [[books.a-walk-through-combinatorics]]
* [[math.induction]]

## Problem

Prove that for all natural numbers $$n$$, the number $$a(n) = n^3 + 11n$$ is divisible by $$6$$.

## Proof

By Induction

For $$n = 1$$, $$a_n = 12$$, which is divisible by $$6$$.

Now the induction step, suppose $$a_n$$ is divisible by $$6$$.

$$$
a_{n+1} = (n+1)^3 + 11(n + 1)
$$$
$$$
\implies a_{n+1} =  n^3 + 1 + 3n^2+3n + 11n + 11
$$$
$$$
\implies a_{n+1} = n^3 + 11n + 3n^2 + 3n + 12
$$$
$$$
\implies a_{n+1}= a_n + 3n(n+1) + 12
$$$

Each of these is divisible by 6.

* $$a_n$$ based on the induction hypothesis
* $$12$$ is trivial
* $$3n(n+1)$$, either $$n$$ or $$n+1$$ is odd and divisible by 2, hence this can be written as $$6x$$o

Hence proved
