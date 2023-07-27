---
id: 64rzkg3ywelj4ihita1ag0b
title: "1"
desc: ""
updated: 1690467065748
created: 1690437914386
---

My solutions: https://github.com/paramsingh/sicp/blob/main/projects/1/basebot.rkt

https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/700dcbfebdb06b0d2cff19c8f8f8e85a_project1.pdf

## Problem 3

> Given an initial upward velocity (in meters per second, or m/s) and initial elevation or
> height (in meters, or m), write a procedure that computes how long the baseball will be in
> flight. Remember that gravity is a downward acceleration of 9.8m/s^2. Note that to solve
> this you will need a root of a quadratic equation. Try using root1, and using root2.
> Only one of these solutions makes sense. Which one? And why? Use this to create a
> correct version of the procedure below.

```
(define time-to-impact
(lambda (vertical-velocity elevation)
YOUR-CODE-HERE))
```

Initial velocity v will be negative because it's going up

$$
position = \frac{1}{2}at^2 + ut + x
$$

We want the position to be 0, so the answer will be a root to this equation, after plugging in values.

Equation:

$$
4.9t^2 - vt - x = 0
$$

Going up is negative. So for our root function, we'll use $$a=4.9$$, $$b = -v$$, $$c = -x$$.

> In some cases, we may want to know how long it takes for the ball to drop to a particular
> height, other than 0. Using your previous procedure as a template, write a procedure that
> computes the time for the ball to reach a given target elevation.

```
(define time-to-height
(lambda (vertical-velocity elevation target-elevation)
YOUR-CODE-HERE))
```

For time to height, the rest will stay the same, just $$c = target - x$$
