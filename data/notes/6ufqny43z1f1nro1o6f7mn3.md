
Let $[n]$ = $\{1, 2, 3, \dots, n\}$.

## Theorem
For all positive integers n, the number of all subsets of $[n]$ is $2^n$.

## Proof:

By induction

Base case: for $n$ = 1, the statement is true as $[1]$
has two subsets, the empty set $\phi$ and $$\{1\}$$.

Induction step:

Assume we know that the statement is true for $$n$$, and want to prove it for $$n + 1$$.

We divide all subsets of $$[n + 1]$$ into two groups:

1. Subsets containing $$n + 1$$
2. Subsets not containing $$n + 1$$

Now, each subset not containing $$n + 1$$ is a subset of
$$[n]$$. We know there are $$2^n$$ such sets, by the induction hypothesis.

Now, those subsets that contain $$n + 1$$ have $$n + 1$$ and a subset of $$[n]$$. The subset of $$[n]$$ can be any subset, so the total number of subsets containing $$n + 1$$ is also $$2^n$$.

Therefore, total number of subsets of $$[n + 1] = 2^n + 2^n = 2^{n+1}$$.

Hence proved.
