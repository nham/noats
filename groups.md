# Notes on group theory

We can define a mapping $\phi_y(x) := y^{-1} x y$ for every $y$ in a group $G$. This mapping is called **conjugation by $y$**. It is 1) a group homomorphism on $G$ (hence an endomorphism), and 2) bijective, hence an automorphism. We call this the **inner automorphism induced by $y$**.

Notice that for abelian groups, all the inner automorphisms are just identity functions. So we can say that conjugacy gives us a view on whether two elements commute: if the conjugation of $x$ by $y$ isn't $x$, then $x$ and $y$ do not commute. The converse holds too, so that $x$ and $y$ commute iff the conjugation of $x$ by $y$ is $x$.

It turns out that the **conjugacy relation** defined by $x \sim z$ iff for some $y$, $\phi_y(x) = z$ is an equivalence relation. Every elment in the **conjugacy class** $[x]$ (the equivalence class under the conjugacy relation) has associated with it some element of $G$ that $x$ does not commute with.
