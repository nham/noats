# Notes on projective geometry

## Axioms
A **projective plane** is a triple $(\mathcal{P}, \mathcal{L}, \diamond)$ such that $\diamond \subseteq \mathcal{P} \times \mathcal{L}$ and the following hold:

 - For all $p \neq q \in \mathcal{P}$, there's a unique $l \in \mathcal{L}$ with $p \diamond l$ and $q \diamond l$.
 - For all $l \neq m \in \mathcal{L}$, there's a unique $p \in \mathcal{P}$ with $p \diamond l$ and $p \diamond m$.
 - There is a subset $D$ of $\mathcal{P}$ with four elements in it such that no subset of 3 elements is incident to the same $l \in \mathcal{L}$.


The elements of $\mathcal{P}$ are called points, and the elements of $\mathcal{L}$ are called lines. We call the unique line incident to two points the *join* of those points, notated $p \vee q$a. The unique point incident to two lines is the *meet* of the points, notated $l \wedge m$.
