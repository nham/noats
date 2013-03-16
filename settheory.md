# Set theory odds and ends

One fact that's important for some lemmas in topology is this: Given $A$, $B$ are subsets of $X$, then $A \subseteq X - B$ iff $B \subseteq X - A$. There are two ways to see this:

 1. First we need the following lemma: $A \subseteq B$ iff $X-B \subseteq X-A$. This is easily proved via taking the contrapositive. You can also think pictorially: if $A$ is just a section of $B$, then inverting $A$ and $B$ results in the inversion of $B$ being just a section of the inversion of $A$.
    With this lemma, it is straightforward to prove. $A \subseteq X-B$ implies $X - (X - B) \subseteq X - A$, and $X - (X - B) = B$.

 2. For $x \in X$, $A \subseteq X - B$ really  means that $x \in A$ implies that $x \notin B$. Take the contrapositive: $x \in B$ implies $x \notin A$, or $B \subseteq X - A$. The other way obviously works too.

This fact is especially important for reasoning about closed sets, since our definitions are in terms of open sets and complements of closed sets are open.

---

If $A \subseteq B$ and $X$ intersects $A$, then $X$ intersects $B$. Kind of obvious, but there you go.

---

$f(f^{pre}(S) ) = S$, but $f^{pre}(f(S))$ could be a strict superset of $S$. One way to get equality is if $f$ is injective, but there's actually a weaker condition that works: we just need $S$ to be the only points that map into $f(S)$ (i.e. the restriction of $f$ to $S$ must be injective). The LHS of the first is the image of all the points that map into S, which is obviously still S. The LHS of the second is the set of all points that map into the same points that S maps into, which could be more than just S.

---

If $f: X \rightarrow Y$ is a function, $S \subseteq X$ and $\mathcal{U}$ is a collection of subsets in $Y$, then let $\mathcal{P} := \{f^{pre}(A) : A \in \mathcal{U}\}$ ($\mathcal{P}$ is the collection of preimages of sets in $\mathcal{U}$.) Then we have the following true:

If $\mathcal{U}$ covers $f(S)$, then $\mathcal{P}$ covers $S$. *Proof:* for $x \in S$, $f(x) \in f(S)$, so it's in one $A_x \in \mathcal{U}$, and hence $f^{pre}(A_x)$ is in $\mathcal{P}$. $x$ is in $f^{pre}(A_x)$ for obvious reasons.

---

You can use this in the proof that the image of a continuous function on a compact metric space is compact: $f^{pre}(\bigcup \mathcal{F}) = \bigcup \{ f^{pre}(A) : A \in \mathcal{F}\}$. The idea is that $f(x) \in \bigcup \mathcal{F}$ iff $f(x) \in A$ for some $A \in \mathcal{F}$.

---

$(A \times B) \cap (X \times Y) = (A \cap X) \times (B \cap Y)$, but the same does not hold for union.
