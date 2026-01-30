Book: [[books.a-walk-through-combinatorics]]

[[math.induction]]

## Problem
At a tennis tournament, every two players played against
each other exactly once. After all the games were over,
each player listed the names of those he defeated, and
the names of those defeated by someone he defeated.

Prove that at least one player listed the names of
everyone else.


## Solution

**Base case**, for 2 players, one player will write the other player's name.

**Induction step:**

For $$n$$ players, someone (say player $$X$$) has written the name of all other players.

Adding player $$n + 1$$, player $$n + 1$$ has either won all games, then he has the list.

Or player $$n + 1$$ has lost at least one game to one
of the players $$1$$ to $$n$$. Now since player $X$ has beaten all of these players, their list will get player $$n + 1$$.

So in any case, there is one player who has the list.
