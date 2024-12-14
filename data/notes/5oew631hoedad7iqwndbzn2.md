

Suppose $$X$$ is some uncertain continuous quantity.

Then the probability that $$X$$ lies in any interveal $$a \leq X \leq b$$ can be computed as follows:

Define events $$A = (X \leq a)$$, $$B = (X \leq b)$$ and $$W = (a \lt X \leq b)$$

$$
B = A \cup W
$$

and $$A$$ and $$W$$ are mutually exclusive

This means that

$$
p(B) = p(A) + p(W)
$$

and so

$$
p(W) = p(B) - p(A)
$$

Now define the function $$F(q) = p(X\leq q)$$. This is called the **cumulative distribution function** or cdf.

Now, the **probability density function** is

$$
f(x) = \frac{d}{dx}F(x)
$$
