# Notes on projective geometry

## Axioms
A **projective plane** is a triple $(\mathcal{P}, \mathcal{L}, \diamond)$ such that $\diamond \subseteq \mathcal{P} \times \mathcal{L}$ and the following hold:

 - For all $p \neq q \in \mathcal{P}$, there's a unique $l \in \mathcal{L}$ with $p \diamond l$ and $q \diamond l$.
 - For all $l \neq m \in \mathcal{L}$, there's a unique $p \in \mathcal{P}$ with $p \diamond l$ and $p \diamond m$.
 - There is a subset $D$ of $\mathcal{P}$ with four elements in it such that no subset of 3 elements is incident to the same $l \in \mathcal{L}$.


The elements of $\mathcal{P}$ are called points, and the elements of $\mathcal{L}$ are called lines. We call the unique line incident to two points the *join* of those points, notated $p \vee q$a. The unique point incident to two lines is the *meet* of the points, notated $l \wedge m$.

**Lemma:** Every projective plane has at least six lines.

*Proof:* $a \vee b$, $a \vee c$, $a \vee d$, $b \vee c$, $b \vee d$, $c \vee d$ are all distinct from each other, since no three lie on the same line. $\Box$


**Lemma:** If $p \diamond l$, $q \diamond l$, $p \diamond m$, $q \diamond m$, then $p = q$ or $l = m$.

Restated: Two distinct lines intersect in at most one point, and two distinct points are both incident upon at most one line.

*Proof:* Really just a re-packaging of axioms 1 and 2. If we assume that $p$ is distinct from $q$, $l$ is distinct from $m$, then $p \vee q$ is the unique line that $p$ and $q$ are both incident upon (by Axiom 1) it could not hold for both $l$ and $m$. Alternatively, we could have considered $l \wedge m$ and used Axiom 2. $\Box$

**Lemma:** Every line is incident upon at least 3 distinct points.

*Proof:* If $a,b,c,d$ are the four points in $D$ from axiom 3 and $l$ is an arbitrary line, then $l$ fails to be incident upon two of the points in $D$ (by definition of those points). Without loss of generality, assume the two points are $a$ and $b$. Then $a \vee b$, $a \vee c$, $a \vee d$ are all distinct lines, so they each have a unique intersection with $l$. These distinct lines already all intersect at $a$, so none of the intersections of $a \vee b$, $a \vee c$, and $a \vee d$ with $l$ can be equal, since by the previous lemma two lines cannot intersect at two different points. $\Box$

**Lemma:** No point of a projective plane is incident upon every line in the plane.

*Proof 1:* Let $a, b, c, d$ be the four points from axiom 3 that ensure non-degeneracy, and suppose $p$ is some arbitrary point. WLOG, suppose $p \neq a$. Then $a \vee b$ and $a \vee c$ are distinct lines by axiom 3, and they intersect at $a$. These lines can't also intersect at $p$, so one of them doesn't hit $p$. $\Box$

*Proof 2:* Let $p$ be an arbitrary point, and $l$ and $m$ be arbitrary distinct lines. If both are incident on $p$, then they intersect at $p$ so that $l \wedge m = p$. There's three distinct points on each line by an earlier lemma, so there's at least one other point, $p_l$, on $l$ and one, $p_m$, on $m$ that aren't $p$. These have to be distinct from each other, because two lines can't intersect in two different places (and they already intersect at $p$). $p_l \vee p_m$ is distinct from $l$ and from $m$ because $p_l$ is already on $l$, so it can't be on $m$ because the only point on both is $p$, which we've already established is distinct from both $p_l$ and $p_m$.

Hence, $p_l \vee p_m$ does not have $p$ on it, because $p_l \vee p_m$ already intersects both $l$ and $m$ at one point each, and $p$ is the intersection of $l$ and $m$, so adding $p$ to $p_l \vee p_m$ would be creating two distinct intersections between two lines. $\Box$
