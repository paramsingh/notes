
Suppose we're trying to solve [[machine-learning.tenenbaum-number-guessing]]. This is [[machine-learning.concept-learning]] which is a [[machine-learning.supervised-learning.classification]] problem.

We have
* [[machine-learning.prior]]: the likelihood of a hypothesis before we've seen any data. So for example, the concept "powers of 2" would have a larger prior that "powers of 2, except 32" or "powers of 2, but with 38". Let's say this is simply $$p(h)$$.
* [[machine-learning.likelihood]]: the probability of seeing a distribution. see [[machine-learning.tenenbaum-number-guessing.occams-razor]]. This is $$p(D|h) = \frac{1}{(\text{size of hypothesis})^n}$$
* [[machine-learning.posterior]]: the probability of a particular concept, given the data. This is likelihood times the prior, normalized.

$$
p(h|D) = \frac{p(h)p(D|h)}{\sum_{h'}{p(h')p(D|h')}}
$$

Now the posterior predictive distribution uses these to figure out the probability that the next number belongs to our concept or not.

$$
p(x \in C|D) = \sum_hp(y=1|x, h)p(h|D)
$$

This is the weighted average of each particular hypothesis.


This method of classification is also called *Bayes model averaging*.
