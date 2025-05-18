
Source: [[books.art_of_doing_science_and_engineering]]

The Kraft inequality gives a limit on the lengths $l_i$ of each symbol in the alphabet.

$$
K = \sum_{i=1}^q \frac{1}{2^{l_i}} \leq 1
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
\frac{K'}{2} + \frac{K''}{2} \leq 1
$$
