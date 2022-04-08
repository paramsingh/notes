---
id: yzjyd7u7y2shgci5l46j0of
title: Eight Integers
desc: ''
updated: 1649434345157
created: 1649432782587
---

Book: [[books.a-walk-through-combinatorics]]

Prove that among eight integers, there are always two whose difference is divisible by seven.

## Proof

Let's write each number as $7x_i+y_i$.

If $y_i = y_j$ for some $i, j$, then the difference between the $i$th and $j$th number

$$
7x_i + y_i - 7x_j - y_j = 7(x_i - x_j)
$$

which is divisible by $7$.

Now we prove that there must always be some $i, j$ such that $y_i = y_j$ via the [[math.pigeonhole-principle]].

The possible set of values for $y_i$ is $\{0, 1, 2, 3, 4, 5, 6\}$.

The set only contains $7$ values while we have $8$ integers. So by the pigeonhole principle, one of the $7$ values will be repeated.
