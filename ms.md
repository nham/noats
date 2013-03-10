Metric spaces are an abstract characterization of spaces equipped with a notion of distance. To each pair of elements we assign a number, the *distance*, between the two points. We must employ the real numbers to quantify distance since the hypotenuse of a unit square is irrational, and it would be silly to lay out a theory of distance that could not account for the euclidean plane. We also only make use of the nonnegative reals, since it's not clear how to interpret *negative* distance (how, exactly, would -5 distance differ from +5 distance?).

Let $X$ be a set, and let $X_k$ for $k \leq |X|$ be the set of all subsets of $X$ with cardinality $k$. For example, $X_1$ is the collection of all singletons, and $X_0$ is a set consisting of the empty set.

A **metric space** is a pair $(X, d)$ where $d$ is a function $X_1 \cup X_2 \rightarrow \mathbb{R}$ such that:

  - For all $A \in X_1 \cup X_2$, $d(A) \geq 0$
  - $d(A) = 0$ iff $A$ is a singleton
  - For $A = \{x,y\}$, $B = \{y,z\}$, $C = \{x,z\}$ in $X_2$, $d(C) \leq d(A) + d(B)$ 

The first two just say that distances are nonnegative and distinct points have nonzero distance. Probably the most important property is the third, commonly known as the *triangle inequality*. It says, simply, that there's no way to shorten a trip from point A to point B by visiting some other point C on the way.

The most common formulation of metric spaces (and definitely easier to work with) is this: *d* is a function $X \times X \rightarrow \mathbb{R}$ such that:

  - $d(x,y) \geq 0$ for all $x$, $y$, and $d(x,y) = 0$ iff $x = y$.
  - $d(x,y) = d(y,x)$
  - $d(x,z) \leq d(x,y) + d(y,z)$

An **open ball** of radius r around x is the set of all points in the metric space that are less than a distance r from x. In symbols:

  $$ B_r(x_0) = \{ x : d(x, x_0) < r \}$$

An **open set** is a set $U$ such that every $x \in U$ has an open ball $B_\epsilon(x)$ which is entirely contained in $U$. An **open neighborhood* of $x$ is an open set that contains $x$. A **neighborhood** of $x$ is a set that contains an open neighborhood of $x$.

