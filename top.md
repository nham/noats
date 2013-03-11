# Notes on point-set topology

It is useful, for various purposes, to generalize [metric spaces](ms.html). But how to discuss continuity with no notion of distance? We use the equivalent characterization of continuous functions, which are functions for which open sets in the target space have open pre-images. We can do this by axiomatizing an abstract space that behaves like the open sets in a metric space do.

A **topological space** is a pair $(X, \mathcal{T})$ where $X$ is some set and $\mathcal{T}$ is a subset of the powerset $\mathcal{P}(X)$ which obeys the following:

 1. $\emptyset$, $X$ are in $\mathcal{T}
 2. For any $\mathcal{U} \subseteq \mathcal{T}$, $\bigcup \mathcal{U} \in \mathcal{T}$
 3. For any $U_1, U_2 \in \mathcal{T}$, $U_1 \cap U_2 \in mathcal{T}$

We are in need of an analog of open balls for general topological spaces so we can describe building up topological spaces from certain *basic* open sets. First I introduce some silly definition that helped me wrap my head around bases.

Given any subcollection $\mathcal{C}$ of $\mathcal{P}(X)$ and a point $x \in X$, we define a *$\mathcal{C}$-host* of $x$ to be a set $S$ such that there is some $C \in mathcal{C}$ for which $x \in C \subseteq S$.

For example, in metric space $(X, d)$, if we let $\mathcal{O}$ be the set of all open sets, then a *neighborhood* of $x$ is a $\mathcal{O}$-host of $x$. If we let $\mathcal{B}$ be the set of all open balls, then the open sets are defined to be the sets that are $\mathcal{B}$-hosts for every element they contain.

Let's make two last silly definitions: a *$\mathcal{C}$-omnihost* is a set $S$ that is a $\mathcal{C}$-host$ of $x$ for all $x \in S$. And we will define $\Theta(\mathcal{C}$ to be the set of all $\mathcal{C}$-omnihosts in a set $X$ (call it the *omnifamily* of $\mathcal{C}$, or something).


