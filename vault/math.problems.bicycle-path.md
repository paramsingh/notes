---
id: 15e1awhi60g4b2bd5hyo6v4
title: Bicycle Path
desc: ''
updated: 1649520717736
created: 1649520233069
---

Book: [[books.a-walk-through-combinatorics]]

## Problem

A bicycle path is 30 miles long, with four rest areas.
Prove there either there are two rest areas that are at
most six miles from each other, or there is a rest area
that is at most six miles away from the endpoints of
the path.

## Solution

Let the rest areas divide the path as follows:

```
|----|-----|-----|-----|-----|
  a_1  a_2   a_3   a_4    a_5
```

We know that
$$
a_1 + a_2 + a_3 + a_4 + a_5 = 30
$$

We need to prove that there is some $i$ so that, for some $i$, $a_i \leq 6$.

By contradiction, if we assume that for all $i$, $a_i \gt 6$, then

$$
a_1 + a_2 + a_3 + a_4 + a_5 \gt 6 + 6 + 6 + 6 + 6
$$

$$
a_1 + a_2 + a_3 + a_4 +a_5 > 30
$$

which is a contradiction, we know the sum is equal to $30$. So our initial assumption is wrong, there must be some $i$ so that $a_i \leq 6$.
