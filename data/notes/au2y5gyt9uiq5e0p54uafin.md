
Book: [[books.a-walk-through-combinatorics]]

## Theorem

A chess tournament has $n$ participants, and any two players play one game against each other. Then it is true that in any given point of time, there are two players who have finished the same number of games.

## Proof

There are $n$ players. If there is a player $A$ who has finished all of his $n - 1$ games, then all other players must have played at least one game (against player $A$).


So, the set of number of games played by players cannot have the values $0$ and $n - 1$ in it simultaneously.

So, the number of games played has only $n - 1$ possible values. The number of players is $n$. By the [[math.pigeonhole-principle]], there must be two players who have played the same number of games.
