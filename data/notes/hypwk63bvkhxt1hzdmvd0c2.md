
# Problem

A state has seven counties. In one year, three
candidates run in a statewide election. Is it possible
that in each county the same number of people vote,
and the candidate who gets the highest number of
votes statewide does not get the highest number of votes
in any county?

# Solution

Let the votes for each candidate (say $X$, $Y$, $Z$) be

$$
x_1, x_2, \dots, x_7
$$
$$
y_1, y_2, \dots, y_7
$$
$$
z_1, z_2, \dots, z_7
$$

Let's assume that $X$ won the election. Then,

$$
    \sum{x_i} \gt \sum{y_i}
$$
$$
    \sum{x_i} \gt \sum{z_i}
$$

Now, let's assume that for all $i$, $x_i \leq y_i$ and $x_i \leq z_i$.
