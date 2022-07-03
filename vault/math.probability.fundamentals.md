---
id: cf147lw88jm456huk5ca76u
title: Fundamentals
desc: ''
updated: 1656888331882
created: 1656887728180
---

## Union of two events

$$
p(A \cup B) = p(A) + p(B) - p(A \cap B)
$$

## Joint probabilities

$$
p(A, B) = p(A \cap B) = p(A|B)p(B)
$$

This is known as the __product rule__.

Given a joint distribution on two events $$p(A, B)$$, we define the marginal distribution as follows:

$$
p(A) = \sum_{b}p(A, B) = \sum_{b}{p(A|B=b)p(B=b)}
$$

This is the __sum rule__ or the __rule of total probability__.

## Conditional probability

Conditional probability of event $$A$$, given that $$B$$ is true:

$$
p(A|B) = \frac{p(A,B)}{p(B)} \text{ if } p(B) > 0
$$
