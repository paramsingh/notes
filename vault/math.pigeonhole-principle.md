---
id: ht0jheu2dftmdx3umljgcar
title: Pigeonhole Principle
desc: ''
updated: 1649351493308
created: 1649351104807
---

Book: [[books.a-walk-through-combinatorics]]

## Pigeonhole principle:

Let $n$ and $k$ be positive integers and let $n \gt k$. Suppose we have to place $n$ identical balls into $k$ boxes. At least one box will need to contain at least 2 balls.

## Proof (by contradiction):

Let's assume there is no box with more than 1 ball.
Thus each box has either 0 or 1 ball in it. Let the number of boxes with 0 balls be $m$; $m \geq 0$.

Thus, there are $k - m$ boxes which have 1 ball in them.

Thus we've only placed $k - m$ balls into boxes

Now, $k - m \leq k \lt n$. Therefore we haven't placed all $n$ balls. Hence if we want to place all $n$ balls, our initial assumption must be falsified, and we need to have at least one box with more than 1 ball.
