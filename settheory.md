One fact that's important for some lemmas in topology is this: Given $A$, $B$ are subsets of $X$, then $A \subseteq X - B$ iff $B \subseteq X - A$. There are two ways to see this:

 1. First we need the following lemma: $A \subseteq B$ iff $X-B \subseteq X-A$. This is easily proved via taking the contrapositive. You can also think pictorially: if $A$ is just a section of $B$, then inverting $A$ and $B$ results in the inversion of $B$ being just a section of the inversion of $A$.
    With this lemma, it is straightforward to prove. $A \subseteq X-B$ implies $X - (X - B) \subseteq X - A$, and $X - (X - B) = B$.

 2. For $x \in X$, $A \subseteq X - B$ really  means that $x \in A$ implies that $x \notin B$. Take the contrapositive: $x \in B$ implies $x \notin A$, or $B \subseteq X - A$. The other way obviously works too.

This fact is especially important for reasoning about closed sets, since our definitions are in terms of open sets and complements of closed sets are open.

---

If $A \subseteq B$ and $X$ intersects $A$, then $X$ intersects $B$. Kind of obvious, but there you go.

---

$f(f^{pre}(S) ) = S$, but $f^pre(f(S))$ could be a strict superset of $S$. One way to get equality is if $f$ is injective, but there's actually a weaker condition that works: we just need $S$ to be the only points that map into $f(S)$ (i.e. the restriction of $f$ to $S$ must be injective). The LHS of the first is the image of all the points that map into S, which is obviously still S. The LHS of the second is the set of all points that map into the same points that S maps into, which could be more than just S.
