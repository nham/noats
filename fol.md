# Prerequisites
As in every (or at least most.) branches of mathematical study, we will make use of variables to range over some set of objects. In other branches it is common to use letters like $x$, $y$, $z$, $S$, $X$, $\phi$ and so on to stand for said objects, but we have a complication here because we are studying formal systems and the variables inside them. The complication, essentially, is that we are using math to study math. We are assuming an ambient mathematical theory with which to conduct our study of formal mathematical theories. That is, we will be studying formal mathematical theories using a *metatheory*. Inside the metatheory we have *metavariables* which will stand for and range over (among other things) variables in the formal systems being studied.

To avoid confusion, we must set out a special notation to make metavariables distinct from variables. We will use bold letters like $\textbf{A}, \textbf{B}, \textbf{x}, textbf{y}$ for metavariables. Later on we will designate certain letters to stand exclusively for certain kinds of objects under study.

# Formal systems

<div class="chatter">
Here we are concerned with studying strings of symbols and operations on these strings. So first we will consider a set of symbols by taking any set, $S$, and treating each of its elements as a symbol. Formally it's just a set, but we should keep in mind that we are dealing with symbols.

(Quote Shoenfield here by saying a symbol is something you can write on a page)

For any set $M$, we can form the **free monoid** on $M$, which we denote $F(M)$ and which consists of the set of all finite strings of symbols in $M$ together with an operation for *concatenating* two strings together. Being a monoid, we of course have an "identity" symbol, the *empty string*, which consists of no symbols at all. Concatenating any string with the empty string, in either order, results in the original string.

Each string of symbols, being a concatenation of some finite number of symbols, has associated with it a *length*, the (natural) number of symbols in the string. The monoid identity (the empty string) is the unique string of length 0 in $F(M)$.

We can also think of *indexing* all the symbols in a string, so that if $x, y, z, w$ are symbols in $M$, then for some string $x y \cdots z w$ in $F(M)$, and we can assign an ordering $f(x) = 1$, $f(y) = 2$, $\ldots$, $f(z) = n-1$, $f(w) = n$ to the symbols in the string.

We could be more formal about the above and say that the free monoid on a set $M$ consists of all the finite tuples of elements of $M$ together with a concatenation operation which takes two finite tuples, an $m$-tuple $a$ and an $n$-tuple $b$ \and returns a $(m+n)$-tuple where the first $m$ elements are $a$ (in the same order), and the remaining $n$ elements are $b$. Then the unique 0-tuple is the empty string, and the index of each symbol in a tuple provides the notion of the index of a symbol in a string.

A *sub-tuple* of a given tuple $(a_1, \ldots, a_n)$ is a tuple $(a_i, \ldots, a_j)$ for $1 \leq i \leq j \leq n$. We similarly speak of a *substring* of a string.
</div>

A **formal language** is a pair $L = (\Sigma, F)$ where $\Sigma$ is a set and $F \subseteq F(\Sigma)$ ($F$ is subset of the free monoid on $\Sigma$). The set $A$ is called the *alphabet* of $L$, and $F$ is called the *formulae* of $L$. A *subformula* of a formula $\textbf{A}$ is a formula of $F$ that's also a substring of $\textbf{A}$.

<div class="chatter">
A formal language is a model of a system of strings where only some of the strings are considered *well-formed* (i.e., the formulae).

We can build on top of this notion by considering a system where only some of the well-formed strings are *true*. Such a system is called a *formal system*:
</div>

A **formal system** is a triple $\Phi = (\Sigma, F, R \subset \mathcal{F} \times F)$ where $(\Sigma, F)$ is a formal language and $R$ is a relation on the powerset of $F$ and $F$, which we call the *rules of inference*. For every pair in this relation, the left term is a set of formulae called the *hypotheses* or *premise*, and the right term is a formula called the *conclusion*. The set of rules which have the empty set as the left term are called *axioms*.

<div class="chatter">
We might have simply specified the subset of $F$ which constitutes the true formulae of the system, but that doesn't give us much structure to work with. Also, the motivation here comes from mathematics, where we don't know in advance which formulae are true. All we know is methods for producing new true formulae from previously known true formulae, and our task is to discover valid derivations of expressions which seem to be true.

Speaking of derivations, we can introduce this notion formally. The idea is that we build up a collection of "true" formulas (theorems) by starting with some specified set of formulas $\Gamma$ and producing new formulas via the rules of inference. I.e. we take rules whose premises are true and add their conclusions to the collection of true formulas. If $\Gamma = \emptyset$, then the formulas derivable from there are the *theorems* of the formal system. (Recall that even starting from the empty set, we can pull all the axioms into the set of theorems, then using the axioms use rules to derive more theorems.)

Formally:
</div> 

A **derivation** in a formal system $\Phi$ of a formula $\textbf{A}$ from a set of formulas $\Gamma$ is a sequence (tuple, really) of formulas ending in $\textbf{A}$ such that each term is either in $\Gamma$ or is the conclusion of a rule whose hypotheses are all previous terms in the sequence. We will say that $\textbf{A}$ is *derivable* or *inferrable* from $\Gamma$ if there's a derivation of $\textbf{A}$ from $\Gamma$ in $\Phi$, and we will denote this in symbols by $\Gamma \vdash_{\Phi} \textbf{A}$.

If $\textbf{A}$ is derivable from $\Gamma = \emptyset$, we will use the shorthand notation $\vdash_{\Phi} \textbf{A}$. Such a formula is called a **theorem** of $\Phi$.

<div class="chatter">
It seems we could have just as well defined a derivation of $\textbf{A}$ as a sequence of rules ending in a rule whose conclusion is $\textbf{A}$, with each term being a rule whose premises are either in $\Gamma$ or are conclusions of previous rules in the sequence. Is there any advantage or disadvantage to this?
</div>

# First order languages
