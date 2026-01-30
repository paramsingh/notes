
The query system is based around two operations: pattern matching and unification.

## Pattern matching

- Test whether a datum matches a pattern
- `((a b) c (a b))` matches `(?x c ?x)` with `?x` bound to `(a b)`
- The pattern matcher takes as input: the datum, the pattern and a frame with any previous bindings.
- If match in a way consistent with the frame, it returns a new frame extended with new bindings.
- If no match, it says no match

### Streams of frames

Given a single frame, the matching process runs through the database entries one by one.
For each database entry, we get a result. The results for all the database entries
are collected into a stream.

![](/assets/images/streams.png)

![](/assets/images/and-stream.png)

## Unification

Unification is the generalization of pattern matching. In this case, both
the pattern and the datum may have variables.

For example, unify `(?x ?x)` and `((a ?y c) (a b ?z))`. To do this, we need
to infer that `?y` is `b`, then `?x` is `(a b c)` and so `?z` is `c`

## How it works

1. Unify the query with the conclusion of the rule to form an extension of the original frame
2. Relative to this extended frame, evaluate the query formed by the body of the rule

Similar to eval-apply loop.

---

Next: [[engineering.sicp.is-logic-programming-mathematical-logic]]
