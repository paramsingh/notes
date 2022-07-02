---
id: bsu4r9viecgm2dqik484ljp
title: K Nearest Neighbours
desc: ''
updated: 1656804432184
created: 1656803492601
---

* [[non-parametric|machine-learning.parametric-and-non-parametric-models]] classifier
* Simply look at the K points in the training set that are closest to the input, counts how many members of each class are in this set, and returns the probability


$$
p(y=c|x, D, K) = \frac{1}{K}\sum_{i \in N_k(x, D)}{I(y_i = c)}
$$

Here

$$N_k(x, D)$$ are the indices of the K nearest points to $$x$$ in $$D$$.

$$I(e)$$ is the __indicator function__ defined as followes:

$$
I(e) = \{\begin{array}{lr}
    1 \text{ if } e \text{ is true} \\
    2 \text{ if } e \text{ is false}
\end{array}
$$

* Generally works quite well if the distance metric is good and has enough labeled training data.
* The main problem is that they do not work well with high dimensional inputs due to the need for dense datasets and the [[machine-learning.curse-of-dimensionality]].
