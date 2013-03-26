A **group with operators** is a pair $(G, \ast, \Omega)$ such that $(G, \ast)$ is a group and $\Omega$ is a collection of endomorphisms on $G$.

A **division ring** is a non-trivial ring such that all non-zero elements have a multiplicatiive inverse.

A **field** is a commutative division ring.

A **vector space** is a triple $(V, F, +, \cdot)$ such that:

 - $(V, +, F)$ is a commutative group with operators.
 - $F$ is a field.
 - $\cdot: F \times V \rightarrow V$ is an operation (called *scalar multiplication*) such that for all $v \in V$:

    - $1 \cdot v = v$
    - $(a + b) \cdot v = (a \cdot v) + (b \cdot v)$
    - $(ab) \cdot v = a \cdot (b \cdot v)$

Let $A$ be some finite set of vectors in a vector space $(V, F)$. A **scaling** on $A$ is defined to be a mapping $s: A \rightarrow F$ assigning to every vector in $A$ some scalar. Then a **linear combination** is the pair $(A, s)$, and the **result** from a linear combination is the sum $\Sigma_{a \in A} s(a) \cdot a$. This is a vector in $V$ because any vector space is closed under linear combinations.

A set $A$ is **linearly independent** if the only linear combination of any finite subset $U$ of $A$ that results in $0$ (the zero vector) is the constant scaling $s(a) = 0$ for all $a \in U$. Let's call the linear combination that uses the constant zero scaling a **trivial** combination of $U$. Restated, a set is linearly independent if the only linear combination obtaining zero is the trivial combination.

A vector $v$ is **linearly dependent** on set $A$ if there's linear combination of some finite subset of $A$ resulting in $v$.

The **span** of a set $A$ is the set of all vectors resulting from a linear combination of some finite subset $U$ of $A$. A vector $v$ is linearly dependent on $A$ iff it is in the span of $A$ (notated $v \in span(A)$).

**Lemma:** If $A$ is finite and linearly independent, then for every $v \in span(A)$ there is exactly one linear combination $(A, s_v)$ which results in $v$.

*Proof:* Assume there are two, with scalings $s_v$ and $t_v$. So $\Sigma s_v(a) \cdot a = v = \Sigma t_v(a) \cdot a$. The linear combination with scaling $r_v$ defined by $r_v(a) = s_v(a) - t_v(a)$ results in $0$ because $\Sigma r_v(a) \cdot a = \Sigma s_v(a) \cdot a - \Sigma t_v(a) \cdot a = 0$, so $r_v(a) = 0$ for all $a$. Thus $s_v = t_v$. $\Box$

**Lemma:** If $A$ is linearly independent and $u \notin span(A)$, then $A \cup \{u\}$ is linearly independent.

*Proof:* If $B = A \cup \{u\}$ is not L.I, then there's some finite $U \subset B$ with a non-trivial combination $(B, s)$ that results in $0$. We must have $s(u) \neq 0$ because otherwise $s$ restricted to $A$ is a nontrivial combination on $A$ that results in $0$, contrary to $A$'s independence. Since this contradicts $u \in span(A)$, $B$ is linearly independent. $\Box$

**Lemma:** $A$ is independent iff no $a \in A$ is linearly dependent on $A - \{a\}$.

*Proof:* If some $a \in span(A - \{a\})$, then there is some linear combination $U, s)$, for finite $U \subseteq A-\{a\}$ which results in $a$. Define a scaling $t$ on $U \cup \{a\}$ by: $t(a) = -1$, $t(v) = s(v)$ for all $v \neq a$ in $U$. This is a non-trivial linear combination of a finite subset of $A$ which results in zero. 

Conversely, if $A$ isn't independent, some non-trivial linear combination $(U, s)$ of a finite subset $U$ of $A$ obtains $0$, so letting $x$ be such that $s(x) \neq 0$, then $\Sigma_{a \in U-\{x\}}} -s(x)^{-1} s(a) \cdot a = x$ is a linear combination of $U - \{x\}$ resulting in $x$. $\Box$

A set $A$ is a **spanning set** of $V$ if $span(A) = V$.

**Lemma:** If $A$ is a spanning set of $V$, then there is a linear combination of $A$ resulting in $v$ for every $v \in V$.

*Proof:* Immediate from the definition of the span of a set. $\Box$

**Lemma:** If $x \in A$ is in the span of $A - \{x\}$, then $span(A-\{x\}) = span(A)$.

*Proof:* Clearly $span(A-\{x\}) \subseteq span(A)$. if $v \in span(A)$, then some linear combination $(A, s_v)$ results in $v$. By hypothesis $x = \Sigma t_x(a) \cdot a$ for some linear combination $(A-\{x\}, t_x)$. So we have:

$$v = s_v(x) \cdot x + \Sigma_{a \in A-\{x\}} s_v(a) \cdot a

and we can define $t_v(a) = s_v(x) t_x(a) + s_v(a)$ for all $a \in A - \{x\}$. This is a linear combination on $A-\{x\}$ resulting in $v$. $\Box$

A **maximal independent set** is a linearly independent set $A$ for which no proper superset of $A$ is independent in $V$. A **minimal spanning set** is a spanning set $B$ of $V$ for which no proper subset of $B$ spans $V$.

**Lemma:** (1) A minimal spanning set is independent. (2) A maximal independent set is spanning.

*Proof:* (1) If $A$ is a minimal spanning set of $V$, then if $A$ is not linearly independent we must have some $a \in A$ in the span of $A - \{a\}$. We can remove $a$ from $A$ without affecting the span, which contradicts our minimality assumption.

For (2), If $B$ is a maximal independent set and $v \notin span(B)$, then by a previous lemma $B \cup \{v\}$ is independent. This contradicts maximality, so $B$ spans $V$. $\Box$

**Lemma:** If $u = \Sigma(A, s)$ for some linear combination $(A, s)$, and $a \in A$ with $s(a) \neq 0$, then $a \in span(A-\{a\}+\{u\})$

*Proof:* $u = \Sigma s(a) \cdot a$, so if $s(a) \neq 0$ then $a = - s(a)^{-1} (-u + \Sigma_{x \in A - \{a\}} s(x) \cdot x)$. $\Box$
