# Notes on matroids

From Whitney's original 1935 paper:

A **matroid** is a finite set $M$ together with a function $r: \mathcal{P}(M) \rightarrow \mathbb{N}$ called the **rank** of a set in $M$, such that:

1. $r(\emptyset) = 0$
2. For $S \subseteq M$, $x \notin S$ $r(S) \leq r(S+x) \leq r(S) + 1
3. For $S \subseteq M$ and $x_1, x_2 \notin S$, if $r(S+x_1) = r(S+x_2) = r(S)$, then $r(N+x_1+x_2) = r(N)$

Define the **nullity** of a subset $S$ of a matroid $M$ to be $n(S) := |S| - r(S)$. A set $X$ is **independent** if $n(X) = 0$ and **dependent** otherwise.


**Lemma:** If $S \subseteq T$ are subsets of a matroid $M$, then $r(S) \leq r(T)$.

*Proof:* For any $S \subseteq T$, $|T - S| = k$ for some $k$ with $0 \leq k \leq |T|$. So we can find $k$ elements $x_1, \ldots, x_k$ in $T$ and not in $S$. So we can construct a sequence $A_0 = T$, $A_1 = A_0 - x_1, \ldots, $A_j = A_{j-1} - x_j$. By axiom 2, $r(T) = r(A_0) \geq r(A_1) \geq \ldots \geq r(A_k) = r(S)$. $\Box$

**Lemma:** For all $S \subseteq M$ of a matroid $M$, $r(S) \geq 0$ and $n(S) \geq 0$.

*Proof:* $\emptyset \subseteq S$ for any subset $S$, so $0 = r(\emptyset) \leq r(S)$.

To prove $n(S) \geq 0$, we need to show $|S| \geq r(S)$.
