---
id: u7skh7qm0pg1nggwafu199t
title: For a minimum length code, length of symbols should be in the opposite order of the probability of the symbol occuring.
desc: ''
updated: 1649259855436
created: 1649258985673
---

We want a instantaneous, uniquely decodable code for given set of input symbols $s_i$, along with their probabilities $p_i$.

### Theorem

If $p_i$ are in descending order, then $l_i$ should be in ascending order

$$
p_1 \geq p_2 \geq ... \geq p_q
$$
$$
l_1 \leq l_2 \leq ... \leq l_q
$$

### Proof

Suppose $p_i$ are in order, but at least one pair of $l_i$ are not.

Their contribution to the average length $L$ is

$$
before = p_nl_n + p_ml_m
$$

After interchanging the two codes

$$
after = p_nl_m + p_ml_m
$$

Difference is

$$
before - after = p_n(l_n - l_m) + p_m(l_m - l_n) = (p_n - p_m)(l_n - l_m)
$$

One of these two is factors is negative, hence the difference is negative. So if we interchange, we get a smaller contribution to the average length $L$. This means that in a minimum length code, the two running inequalities must be true.

Source: [[books.art_of_doing_science_and_engineering]]
