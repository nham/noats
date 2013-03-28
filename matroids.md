# Notes on matroids

From Whitney's original 1935 paper:

A **matroid** is a finite set $M$ together with a function $r: \mathcal{P}(M) \rightarrow \mathbb{N}$ called the **rank** of a set in $M$, such that:

1. $r(\emptyset) = 0$
2. For $S \subseteq M$, $x \notin S$ $r(S) \leq r(S+x) \leq r(S) + 1
3. For $S \subseteq M$ and $x_1, x_2 \notin S$, if $r(S+x_1) = r(S+x_2) = r(S)$, then $r(N+x_1+x_2) = r(N)$

Define the **nullity** of a subset $S$ of a matroid $M$ to be $n(S) := |S| - r(S)$. A set $X$ is **independent** if $n(X) = 0$ and **dependent** otherwise.

**Lemma:** If $S \subseteq T$ are subsets of a matroid $M$, then $r(S) \leq r(T)$, and $n(S) \leq n(T)$.

*Proof:* For any $S \subseteq T$, $|T - S| = k$ for some $k$ with $0 \leq k \leq |T|$. So we can find $k$ elements $x_1, \ldots, x_k$ in $T$ and not in $S$. Hence we can construct a sequence $A_0 = S$, $A_1 = A_0 + x_1, \ldots, $A_j = A_{j-1} + x_j$. By axiom 2, $r(S) = r(A_0) \leq r(A_1) \leq \ldots \leq r(A_k) = r(T)$.

Also, for every $i$ $0 \leq i < k$, $r(A_{i+1}) - r(A_i) \leq 1$ (again by axiom 2), so $r(T) - r(S) = r(A_k) - r(A_{k-}) + \ldots + r(A_1) - r(A_0) \leq k = |T| - |S|$. We can rearrange this to produce:

$$|S| - r(S) \leq |T| - r(T)$$

Or: $n(S) \leq n(T)$. $\Box$

**Lemma:** For all $S \subseteq M$ of a matroid $M$, $r(S) \geq 0$ and $n(S) \geq 0$.

*Proof:* $\emptyset \subseteq S$ for any subset $S$, so $0 = r(\emptyset) \leq r(S)$.

To prove $n(S) \geq 0$, we need to show $|S| \geq r(S)$. This is an easy proof by induction using axiom 2. $\Box$ 

**Lemma:** Every subset of an independent set is independent.

*Proof:* If $T$ is independent, $n(T) = 0$. For any $S \subseteq T$, $n(S) \leq n(T)$. But $n(S) \geq 0$ as well. $\Box$

A **base** is a maximal independent set. A **circuit** is a minimal dependent set.

**Theorem:** $N$ is independent iff $N$ is contained in a base iff $N$ contains no circuit.

*Proof:* If $N$ is independent, it's either the biggest independent set containing $N$ in the matroid, or we can find one bigger. Repeat this until we find a maximal independent set. This terminates eventually because the containing matroid is finite. So $N$ is contained in a base.

If $N$ is contained in a base, then it cannot contain a circuit, because that would imply that a base contains a circuit. A base is independent, however, so all subsets are independent (hence they are not circuits).

If $N$ contains no circuit, then it can't contain a dependent set at all (otherwise we could find a circuit by removing elements until we can't remove any more without making it independent). So every subset is independent, and in particular $N$ is independent. $\Box$
