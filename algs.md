# Algorithms

## Gale-Shapley algorithm (Stable-Matching Problem)
In the stable-matching problem we have two finite, disjoint sets of equal size, $A$ and $B$, and each element of $A$ has associated with it a total order on $B$ (the "preferences" of that entity), ditto for every element of $B$. We want to establish a bijection between the two that is "stable", in the sense that if any element $a \in A$ is paired with some $b \in B$, then there isn't any $b' \in B$ such that $b'$

 1. $a$ prefers $b'$ to $b$.
 2. $b'$ prefers $a$ to its current partner

To more easily import this problem into human minds, it is often anthropomorphized and recast as the "stable marriage problem": We have $n$ men and $n$ women, and each person has a ranking of the members of the other sex. We want to marry them off in pairs such that no two people would switch if given the chance (i.e. if there was no pair of a man and a woman that prefer each other to their partners).

I won't present pseudocode or describe the algorithm here, since I wrote a Python implementation of it! It's ugly as of yet though, so check the github repo if you want code. I'll just analyze it theoretically now.

**Lemma:** Any element of $B$ is paired at every step in the process after it first becomes paired.

*Proof:* We only alter the pairing of any $b \in B$ by either 1) making it paired for the first time or 2) pairing it with an entity of $A$ that it $b$ prefers more than it's current 'mate'. After being paired, at no point does $b$ become unpaired. $\Box$

**Lemma:** The entities that $a \in A$ proposes to decrease over time in terms of $a$'s preference ordering on $B$.

*Proof:* Immediate from the algorithm. $\Box$

**Lemma:** At any step in the algorithm, $b \in B$ is unpaired iff $\exists a \in A$ such that $a$ is unpaired.

*Proof:* No two elements of $A$ can be paired with the same $b \in B$, since once $a'$ successfully proposes to some $b$ that $a$ was previously paired with, then $a$ is immediately set free. No two elements of $B$ can be paired with one $a$, since only free elements of $A$ propose.

**Lemma:** If some $a \in A$ is free, then $\exists b \in B$ such that $a$ has not yet proposed to $b$.

*Proof:* Since $a$ is free, by the previous lemma some $b \in B$ is also unpaired. This means $b$ has not been proposed to, since the first time $b$ had been proposed to, it would have become paired, and after that it would have to remain paired (to some element of $A$) for the remaining duration of the algorithm.

**Lemma:** The algorithm returns a full pairing (a "perfect matching" by K&T's terminology).

*Proof:* If needed, any $a \in A$ wll propose to every $b \in B$. By the converse, after proposing the every $b$, $a$ will not be free. So every entity in $A$, and a previous lemma implies that every $B$ will be paired as well.


**Theorem:** The Gale-Shapley algorithm returns a stable matching.

*Proof:* If it were false, the algorithm would return $(a_1, b_1)$ and $(a_2, b_2)$ matched such that (without loss of generality) $a_1$ prefers $b_2$ to $b_1$ and $b_2 prefers $a_1$ to $a_2$. We break it into two cases:

$(a_1, b_1)$ is matched first, then $a_1$ must have already proposed to $b_2$ (since $a_1$ prefers $b_2$ to $b_1$) and there is some $a_3$ such that $b_2$ prefers $a_3$ to, and either $(a_3, b_2)$ was already a pair, or that $a_3$ proposed later. That $a_3$ could not have been $a_2$, since $b_2$ prefers $a_1$ to a_2$. But for $a_2$ to steal $b_2$ away from $a_3$, $b_2$ must have preferred $a_2$ to $a_3$, which violates transitivity of the preference ordering. $\Box$


**Missing Lemma:** If $a \in A$ proposes to $b \in B$, then it must have proposed to all the $b' \in B$ that it prefers to $b$ first.


**Theorem:** No matter how free entities in $A$ are chosen, Gale-Shapley returns the same stable matching.

*Proof:* Suppose we have the set of all stable matchings that different G-S algorithm executions return (for every conceivable choce method). Let $b \in B$ be a *valid partner* for $a$ if $(a, b)$ is in some execution. We want to derive a contradiction from supposing that two executions, $S$ and $T$ return different partners for some $a \in A$. Suppose that in $T$ a valid partner of some entity in $A$ rejects that entity. Let $a$ be the first entity rejected by a valid partner in $T$, and call the partner $x$. Then in some execution $S$, $a$ and $x$ are paired, while $b$ and $x$ are paired in $T$.

$x$ clearly prefers $b$ to $a$, so why didn't $b$ & $x$ pair in $S$? It must have been the case that $b$ never proposed to $x$ (otherwise $x$ would have rejected $a$ for $b$ in $S$ as well). So there was some $y$ that $b$ was happily paired up with in $S$.  Now why didn't $b$ pair with $y$ in $T$? $b$ would have proposed to $y$ before proposing to $x$ in $T$ (since $b$ prefers $y$ to $x$), so $b$ must have been rejected by $y$. But this rejection had to have happened before $b$ proposed to $x$, which caused our "first rejection" of $a$ by $x$. And $y$ is a valid partner for $b$. This is a contradiction. So all executions of Gale-Shapley return the same stable matching. $\Box$

## Some problems

**Interval scheduling problem:** You have a set $R$ of $n$ closed intervals $[s_i, f_i]$ in $\mathbb{R}$, such that every $s_i < f_i$. Find a pairwise-disjoint subset of $R$ of maximum size.

**Bipartite matching problem:** Given a bipartite graph $G$, find a matching (collecting of edges that are pairwise non-adjacent) of maximum size.

**Independent set problem:** Given any graph, find an independent set (set of nodes that are pairwise non-neighboring, a.k.a. a set of nodes whose induced subgraph has no edges) of max size.
