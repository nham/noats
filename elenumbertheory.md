The **division theorem** (proved in Euclid's Elements, so it's very old) says that for any integers $a \geq 0$, $b > 0$, there's a unique pair $(q,r)$ such that $a = qb + r$, with $0 \leq r < b$. This is so intuitively clear that if this weren't true in whatever system of math we were using, we would make a new system of math to force it to be true (and if we couldn't do that, we would give up hope of ever using mathematics). However, we can prove it using the basic properties of the integers!

The idea to show existence is that we want to subtract as many copies of $b$ as we can from $a$. Once we can take away no more, the remainder must be left over. So formally we consider the set

$$\{a - zb : z \in \mathbb{Z}\}$$

We consider the smallest positive element of this set (There's at least one positive element, since $a = a - zb$ for $z = 0$.), $r = a - qb$, where $q \in \mathbb{Z}$ is the "max number of copies of $b$ we could take from $a$". 

$r$ must be less than $b$ because, if it were not, $r - b = a - qb - b = a - (q+1)b$ would be positive, and we already assumed that $a - qb$ was the smallest positive element.


To prove uniqueness, assume we have

$$a = q_1 b + r_1$$
$$a = q_2 b + r_2$$

with each $r_i < b$. Then $0 = (q_1 - q_2)b + (r_1 - r_2)$. We must have $(q_1 - q_2) = 0$, because $|r_1 - r_2|$ is less than $b$. (Any multiples of $b$ could never be balanced out by $r_1 - r_2$). So we have:

$$q_1 = q_2$$
$$r_1 = r_2$$.
