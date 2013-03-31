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

Let $A$ be some finite set of vectors in a vector space $(V, F)$. A **scaling** on $A$ is defined to be a mapping $s: A \rightarrow F$ assigning to every vector in $A$ some scalar. Then a **linear combination** is the pair $(A, s)$, and the **result** from a linear combination is the vector $\sum{a \in A} s(a) \cdot a$. 

A subset $S$ of vector space $V$ is a **subspace** $V$ if it's closed under linear combinations.

A set $A$ is **linearly independent** if the only linear combination of any finite subset $U$ of $A$ that results in $0$ (the zero vector) is the constant scaling $s(a) = 0$ for all $a \in U$. Let's call the linear combination that uses the constant zero scaling a **trivial** combination of $U$. Restated, a set is linearly independent if the only linear combination obtaining zero is the trivial combination.

A vector $v$ is **linearly dependent** on set $A$ if there's linear combination of some finite subset of $A$ resulting in $v$.

The **span** of a set $A$ is the set of all vectors resulting from a linear combination of some finite subset $U$ of $A$. A vector $v$ is linearly dependent on $A$ iff it is in the span of $A$ (notated $v \in span(A)$).

**Lemma:** If $A$ is finite and linearly independent, then for every $v \in span(A)$ there is exactly one linear combination $(A, s_v)$ which results in $v$.

*Proof:* Assume there are two, with scalings $s_v$ and $t_v$. So $\sum s_v(a) \cdot a = v = \sum t_v(a) \cdot a$. The linear combination with scaling $r_v$ defined by $r_v(a) = s_v(a) - t_v(a)$ results in $0$ because $\sum r_v(a) \cdot a = \sum s_v(a) \cdot a - \sum t_v(a) \cdot a = 0$, so $r_v(a) = 0$ for all $a$. Thus $s_v = t_v$. $\Box$

**Lemma:** If $A$ is linearly independent and $u \notin span(A)$, then $A \cup \{u\}$ is linearly independent.

*Proof:* If $B = A \cup \{u\}$ is not L.I, then there's some finite $U \subset B$ with a non-trivial combination $(B, s)$ that results in $0$. We must have $s(u) \neq 0$ because otherwise $s$ restricted to $A$ is a nontrivial combination on $A$ that results in $0$, contrary to $A$'s independence. Since this contradicts $u \in span(A)$, $B$ is linearly independent. $\Box$

**Lemma:** $A$ is independent iff no $a \in A$ is linearly dependent on $A - \{a\}$.

*Proof:* If some $a \in span(A - \{a\})$, then there is some linear combination $U, s)$, for finite $U \subseteq A-\{a\}$ which results in $a$. Define a scaling $t$ on $U \cup \{a\}$ by: $t(a) = -1$, $t(v) = s(v)$ for all $v \neq a$ in $U$. This is a non-trivial linear combination of a finite subset of $A$ which results in zero. 

Conversely, if $A$ isn't independent, some non-trivial linear combination $(U, s)$ of a finite subset $U$ of $A$ obtains $0$, so letting $x$ be such that $s(x) \neq 0$, then 

$$\sum_{a \in U-\{x\}} -s(x)^{-1} s(a) \cdot a = x$$

is a linear combination of $U - \{x\}$ resulting in $x$. $\Box$

A set $A$ is a **spanning set** of $V$ if $span(A) = V$.

**Lemma:** If $A$ is a spanning set of $V$, then there is a linear combination of $A$ resulting in $v$ for every $v \in V$.

*Proof:* Immediate from the definition of the span of a set. $\Box$

**Lemma:** If $x \in A$ is in the span of $A - \{x\}$, then $span(A-\{x\}) = span(A)$.

*Proof:* Clearly $span(A-\{x\}) \subseteq span(A)$. if $v \in span(A)$, then some linear combination $(A, s_v)$ results in $v$. By hypothesis $x = \sum t_x(a) \cdot a$ for some linear combination $(A-\{x\}, t_x)$. So we have:

$$v = s_v(x) \cdot x + \sum_{a \in A-\{x\}} s_v(a) \cdot a$$

and we can define $t_v(a) = s_v(x) t_x(a) + s_v(a)$ for all $a \in A - \{x\}$. This is a linear combination on $A-\{x\}$ resulting in $v$. $\Box$

A **maximal independent set** is a linearly independent set $A$ for which no proper superset of $A$ is independent in $V$. A **minimal spanning set** is a spanning set $B$ of $V$ for which no proper subset of $B$ spans $V$.

**Lemma:** (1) A minimal spanning set is independent. (2) A maximal independent set is spanning.

*Proof:* (1) If $A$ is a minimal spanning set of $V$, then if $A$ is not linearly independent we must have some $a \in A$ in the span of $A - \{a\}$. We can remove $a$ from $A$ without affecting the span, which contradicts our minimality assumption.

For (2), If $B$ is a maximal independent set and $v \notin span(B)$, then by a previous lemma $B \cup \{v\}$ is independent. This contradicts maximality, so $B$ spans $V$. $\Box$

**Lemma:** If $u = \sum(A, s)$ for some linear combination $(A, s)$, and $a \in A$ with $s(a) \neq 0$, then $a \in span(A-\{a\}+\{u\})$

*Proof:* $u = \sum s(a) \cdot a$, so if $s(a) \neq 0$ then $a = - s(a)^{-1} (-u + \sum_{x \in A - \{a\}} s(x) \cdot x)$. $\Box$

A **basis** for $V$ is an independent spanning set. A vector space is **finite-dimensional** if it has a finite basis.


**Lemma:** If $V$ is finite-dimensional then any finite spanning set can be pared down to a basis.

*Proof:* If $A$ is a finite spanning set, then remove an element $x \in A$ such that $span(A-\{x\}) = span(A)$. If there is no such $x$, then $A$ is a minimal spanning set, and so is independent. Repeat this procedure (which will terminate since we start from a finite set) until we obtain a minimal spanning set. This is a basis.

**Steinitz Exchange Lemma:** If $A$ spans vector space $V$ and $U = \{u_1, \ldots, u_m\}$ is a linearly independent set in $V$, with $|A| = n$, then for any $k \in [m] $ $\{u_1, \ldots, u_k\} \cup A_{n-k}$ spans $V$, for some $n-k$-subset of $A$. In particular, $m \leq n$.

*Proof:* Let $U = \{u_1, \ldots, u_m\}$. Let $A_1 = A$. Since $A_1$ spans $V$, $u_1 \in span(A_1)$. There must be some $x_1 \in A_1$ that doesn't have a zero coefficient, since $u_1$ isn't zero. Letting $A_2 = A_1 - x_1 + u_1$, we have $x_1 \in span(A_2)$ (by a previous lemma). $span(A_2) = span(A_1)$ since any linear combination requiring some amount of $x_1$ can be accounted for (given that $x_1 is in the span of $A_2$).

For $k < m$, we have that $A_k$ spans $V$. So $u_k \in span(A_k)$, and some $x_k$ not in $U$ is in $span(A_{k+1})$, where $A_{k+1} = A_k - x_k + u_k$. (If only elements of $U$ had non-zero coefficients, we'd have a linear combination of elements of $U$ that resulted in another element of $U$, which is an impossibility given that $U$ is linearly independent).

$A_m$ contains all of $U$, meaning that we removed $m$ elements from $A$ and replaced them with elements of $U$. So $n$ cannot be less than $m$. $\Box$

**Theorem:** Every basis of a finite-dimensional vector space has the same number of elements.

*Proof:*  If $B_1$ and $B_2$ are two bases for $V$, then $|B_1| \leq |B_2|$ and $|B_2 \leq |B_1|$ since bases are both independent and spanning. $\Box$

This theorem affords us a useful definition: the **dimension** of a finite-dimensional vector space $V$, notated $dim V$, is the cardinality of any base of $V$. By the previous theorem this is well-defined.

Every vector in a vector space has a unique representation as a linear combination of a basis. This fact gives us an easy way to characterize linear maps, since we need only know where each basis element is mapped to: If $\{b_1, \ldots, b_n\}$ is a basis for $V$ and $v \in V$, then for some linear combination $v = \sum a_i b_i$. So any linear $\phi$ defined on $V$ must have:

$$ \phi(\sum a_i b_i) = \sum a_i \phi(b_i)$$

In fact, the collection of $\phi(b_i)$'s is a basis for the image of $\phi$:

**Lemma:** if $V, W$ are finite-dimensional vector spaces and $\phi: V \rightarrow W$ is a linear map and $B = \{v_1, \ldots, v_n\}$ is a basis for $V$, then the image of $B$ after discarding zero vectors is a basis for the image of $\phi$.

*Proof:* If $w \in img(V)$, then there's a $v \in V$ such that $\phi(v) = w$. So $v$ is some linear combination of $B$, say $v = \sum a_i v_i$. So $w = \sum a_i \phi(v_i)$, meaning $img(B)$ spans $img(V)$. Also, if we were to remove $\phi(v_k)$ from $img(B)$, we could not have $\phi(v_k) \in span(\phi(B - v_k))$, because that would imply $v_k \in span(B - v_k)$, which could not be since $B$ is a basis. $\Box$

## Systems of linear equations

A *linear equation in $m$ variables* is an equation like this:

$$ a_1 x_1  + \ldots + a_m x_m = c$$

where the $a_i$'s and $c$ are fixed elements of some field $\mathbb{F}$ and the $x_i$'s are variables in $\mathbb{F}$. The task is to *solve* the equation for the variables, meaning to find the set of variables for which the equation is true.

It is an easy to generalize this to multiple linear equations which must be solved simultaneously. So we define a **system of linear equations** as a collection of $k$ linear equations:

$$ \sum a_{i1} x_1 = c_i, i \in [k]$$

Note that there are $k (m + 1)$ knowns and $m$ unknowns.

The set of all $(x_1, \ldots, x_m) \in \mathbb{F}^m$ that solve a system of linear equations is called the **solution set**. If $c_i = 0$ for all $i$, then the system is called a **homogeneous** system of linear equations. Clearly the zero vector of $\mathbb{F}^m$ is a solution to a homogeneous system, and it is called the **trivial solution**.

There is a complementary way of viewing a system of linear equations: let

$$v_i = \begin{bmatrix}a_{i1} \\ \vdots \\ a_{ik}\end{bmatrix}$$

and

$$u = \begin{bmatrix} c_1 \\ \vdots \\ c_k \end{bmatrix}$$

be vectors in $\mathbb{F}^k$. The equations say that we are trying to find some linear combination of $v_1, \ldots, v_m$ that results in $u$. If the system is homogeneous, meaning that $u = 0$, any nontrivial solutions imply that $v_1, \ldots, v_m$ are linearly dependent. The converse holds as well. If $m > k$ then there will always be nontrivial solutions, since any collection of more than $k$ vectors in a $k$-dimensional space must be linearly dependent.

**Lemma:** The solution set of a homogeneous system of linear equations is a subspace of $\mathbb{F}^m$

*Proof:* If $x = (x_1, \ldots, x_m)$ and $y = (y_1, \ldots, y_m)$ are two solutions to a homogeneous system $\{a_{11}, \ldots, a_{km} \}$, then for all $i \in [k]$:

$$\sum_j a_{ij} (c x_j + d y_j) = c \sum_j a_{ij} x_j + d \sum_j a_{ij} y_j = 0$$

So $cx + dy$ is a solution as well. The set of solutions is thus closed under linear combination. $\Box$

If $v_1, \ldots, v_m$ do not span $\mathbb{F}^k$, then $u$ may not be in the span, meaning that the system has no solution. This will always happen if $m < k$ (because we don't have enough vectors for a basis of $\mathbb{F}^k$, which is a minimal spanning set), but could also happen if $m \geq k$ and the set of $v_i$'s are linearly dependent.


