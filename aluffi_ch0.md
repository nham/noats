# Notes on Aluffi's Algebra: Chapter 0

The first chapter is ground-up presentation of set theory so that the book is entirely self contained. Much of this is review for me, so I will only record here the new things.

The **disjoint union** of sets $A$ and $B$ is the union of two disjoint sets $S$ and $T$ that are isomorphic (same cardinality) to $A$ and $B$. One good way to do this is to set $S = \{0\} \times A$ and $T = \{1\} \times B$.


The restriction of a function $f: A \rightarrow B$ to some subset $S$ of $A$ can be achieved using the inclusion map $i: S \rightarrow A$: $f|_S = f \circ i$.


I already knew this, but I should record it here for posterity: properties of set functions form the basis for various algebraic notions. The fact that we can compose functions to get another function is a binary operation on functions. Function composition is associative, which is why we study associative algebraic structures in elementary abstract algebra. Composing with the identity function leaves any function unchanged, which is why we often consider units. Bijective functions have inverses, meaning they can be undone. This leads to studying *groups*, or collections of bijections.


A **monomorphism** between sets is a function $f: B \rightarrow C$ such that for any $g, h: A \rightarrow B$, $f \circ g = f \circ h$ implies $g = h$.

**Proposition:** A function is a monomorphism iff it is injective.

*Proof:* If $f(x) = f(y)$ for $x, y \in B$, $x \neq y$, then let $g$ and $h$ differ only on some $a \in A$, such that $g(a) = x$ and $h(a) = y$. Then $f \circ g = f \circ h$ without $g = h$, clearly violating the monomorphism condition.

Conversely, if $f$ is injective, then for distinct functions $g, h: A \rightarrow B$ $g(x) \neq h(x)$ for some $x \in A$, so $f(g(x)) \neq f(h(x))$. This says that $f \circ g \neq f \circ h$, so $f$ is a monomorphism. $\Box$

A monomorphism is a function that doesn't obscure any differences in output between two other functions.

It is easy to prove a lemma characterizing injective functions: a function is injective iff it has a left-inverse. We can use this fact to supply a different proof, one that doesn't involve looking at the individual values the function takes on:

*Alt Proof:* If $f$ is injective, there's some $t$ s.t. $t \circ f = id_B$. So if $g, h: A \rightarrow B$ and $f \circ g = f \circ h$, then $g = id_B \circ g = (t \circ f) \circ g = t \circ (f \circ g) = t \circ (f \circ h) = (t \circ f) \circ h = h$. So $f$ is a monomorphism.

Conversely, it is not clear how to provide a proof that does not look at values. We will be content with supplying a different proof here, not by contrapositive. If $f \circ g = f \circ h$ implies $g = h$, consider all functions from a singleton set $\{0\}$ to $B$. In this case, $f \circ z_1 = f \circ z_2$ means that $f(z_1(0)) = f(z_2(0))$. This implies $z_1(0) = z_2(0)$ But we can find functions $z$ mapping $0$ to any and every element in $B$. So for all $b,c \in B$, $f(b) = f(c)$ implies $b = c$. I.e., $f$ is injective. $\Box$

To go along with the above fact about left inverses and injections, we have: a function is surjective iff it has a right-inverse. Surprisingly this depends on the axiom of choice, but at this point I'm resigned to it. The axiom of choice is essentially the cost of doing business with infinite sets, which are often useful.

Adding these two facts together, we get: a set is bijective iff it has an inverse.

This is the reason that Aluffi talks about bijections being "isomorphisms" of sets: in a category, an isomorphism is a function with a two-sided inverse. So bijections actually are the isomorphisms in the category of sets.

## Categories

A **quiver** is a set of *objects* $\mathcal{C}_0$, a set of *arrows* $\mathcal{C}_1$ and two functions $s, t: $\mathcal{C}_1 \rightarrow \mathcal{C}_0$. For any arrow $f$, $s(f)$ is called the **source** of $f$, and $t(f)$ is called the **target**. For any two objects $A$, $B$, we can form the set $Hom(A,B)$ of arrows with a source $A$ and a target $B$. To generalize this a bit, $Hom(-, B)$ is the set of all arrows with target $B$, and $Hom(A, -)$ is the set of all arrows with source $A$.

A **composition quiver** is a quiver along with for every object $A$, an operation $Hom(-, A) \times Hom(A, -) \rightarrow \mathcal{C}_1$ such that 

 - for any $f \in Hom(-, A)$ and $g \n Hom(A, -)$, the result of the operation on $(f,g)$, written $g \circ f$, is an arrow  with $s(g \circ f) = s(f)$ and $t(g \circ f) = t(g)$.

 - if $g \circ f$ and $h \circ g$ are defined, then $h \circ (g \circ f) = (h \circ g) \circ f$.

We say that $g \circ f$ is the **composition** of $g$ with $f$. The second stipulation says that composition is *associative*.

From associativity, it follows that any string of arrows $f_1, \ldots, f_n$ with t(f_1) = s(f_2), \ldots, t(f_{n-}) = s(f_n)$ has a unique composition, and when denoting it we omit parentheses: $f_n \circ \cdots \circ f_1$.


A **category** is a composition quiver with, for every object $A$, an **identity** arrow $id_A$ in $Hom(A, A)$ such that for any $f \in Hom(A, -)$ $f \circ id_A = f$ and for any $g \in Hom(-, A)$ $id_A \circ g = g$.

We actually need a little bit more. Categories are often bigger than sets will allow. For example, we will need to consider a category of all sets. The "object set" of such a category could not exist, since no set can contain itself. So we will consider a broader notion of a "class". So in all the definitions above, replace "set" with "class". A category where the class of objects really *is* a set is called a **small** category. A category  (not necessarily small) where each class $Hom(A,B)$ of arrows really *is* a proper set is called a **locally small** category. It is interesting to note that in Aluffi actually defines categories to be locally small. I am assuming that locally small categories will be sufficient for virtually all of the contents of the book.
