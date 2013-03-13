# Notes on computability

## Basic notions
Let $[n] = \{1, \ldots, n\}$. $\mathbb{P}$ is the positive integers, while $\mathbb{N}$ is the nonnegative integers (also referred to as the natural numbers).

A n-ary *predicate* on a set $A$ is some subset of $A^n$. Note that the 0-ary predicate on any set is just some singleton set. We might as well define it as $A^0 := \{\emptyset\}$ (the set consisting of one element, the empty set.)


## Unlimited register machines

An **unlimited register machine (URM)** is

 - an *initial register state* $\text{init}: \mathbb{P} \rightarrow \mathbb{N}$
 - a $k$-tuple $(I_1, \ldots, I_k)$ of *instructions*, where each $I_j$ is one of the following: $(Z, n)$, $(S, n)$, $(T, m, n)$, $(J, m, n, i)$ with $m, n, i \in \mathbb{P}$. We call $k$ the *length* of the URM.

The interpretation is that an URM is a machine with an infinite collection of registers, each register capable of storing an arbitrarily large natural number. The machine accepts four different kinds of instructions: a *zero* instruction, $(Z, n)$, for setting the $n$-th register to 0, a *successor* instruction, $(S, n)$ for incrementing the $n$-th register by 1, a *transfer* instruction, $(T, m, n)$ for copying the current contents of register $m$ to register $n$, and a *jump* instruction, $(J, m, n, i)$, which compares the values in registers $m$ and $n$ and sets the next instruction to be instruction $i$ iff the values are equal.

We will often abbreviate the above instructions as $Z\ n$, $S\ n$, $T\ m\ n$, and $J\ m\ n\ i$.

Being a machine, an URM needs some notion of *running* or *executing*. One might also say *computing*, since that is our subject here; an URM is a model of computation. The instructions, along with the initial state, entirely determine how it runs.

Let us say that a **state of the machine** or just **state** of an URM is any function $\mathbb{P} \rightarrow \mathbb{N}$. So the state of the machine is actually the state of all of the individual registers, considered as a whole.

Each of the first three kinds of instructions define a transformation of the state. Furthermore, in each transformation, exactly one register is affected. Here we could say that, given any instruction, we can obtain the *transformation* associated with that instruction by feeding the instruction into some function. That would be tediously formal, however, and we shall go ahead and say that, e.g. $(Z, n)$ *is* a transformation of the state.

Formally, given any state $s: \mathbb{P} \rightarrow \mathbb{N}$, we have:

$$ ([Z\ n] \circ s)(x) := \cases{
    0 & \text{if } x = n \cr
    s(x) & \text{otherwise}}$$

$$ ([S\ n] \circ s)(x) := \cases{
    s(x)+1 & \text{if } x = n \cr
    s(x) & \text{otherwise}}$$

$$ ([T\ m\ n] \circ s)(x) := \cases{
    s(m) & \text{if } x = n \cr
    s(x) & \text{otherwise}}$$


That all seems fairly straightforward. Unfortunately, of our four instructions, one of these things is not like the others. That would be the jump instruction, which does not transform the state at all (or rather, it's the identity transformation). What it does do is change which instruction we execute next, which brings us to a topic that we have thus far neglected: the order of executing our instructions.

We already have a natural ordering of instructions by virtue of the fact that we store them in a tuple. So a reasonable place to start would be at the first instruction, and upon executing that instruction moving onto the second instruction, and so forth. We just need to accomodate the wrinkle introduced by jump instructions, which is done easily enough:

Let $\mathcal{I}$ be the set of all possible instructions and $\mathcal{S}$ be the set of all possible states (functions $\mathbb{P} \rightarrow \mathbb{N}$). We will say that the *instruction counter* is a register (separate from the registers of the URM) which holds values in $\mathbb{P}$. This register is initially set to 1 and is updated according to a function $u: \mathbb{P} \times \mathcal{I} \times \mathcal{S} \rightarrow \mathbb{P}$ defined by:

$$ u(p, I, s) := \cases{
    k & \text{if } I = (J\ m\ n\ k) \text{ and } s(m) = s(n) \cr
    p+1 & \text{otherwise}}$$

Here's a question: what happens when the instruction counter no longer points to a valid instruction (by acquiring a value that exceeds the index on the last instruction)? We can't really expect the URM to do anything, so it must stop. Therefore, supposing that an URM has length $k$, the machine runs as long as its instruction counter doesn't exceed $k$.

We might also think of introducing some kind of notion for the *trace* of an URM, meaning the sequence of states that the machine goes through. This could be useful, but it turns out that it is more interesting to consider just the *final* state of the machine. Actually, we don't need the whole state, just the state of one of the registers.

The state at the time when the URM stops running will be called the *final state*. If $s$ is the final state for an URM, then we will define the **output** of that URM to be $s(1)$. That is, the output of an URM is the value of the first register in the final state.

## Computable functions

The reason we care about so-called "outputs" of an URM is that we will be studying "computable functions", which are functions whose input/output pairs can be given by an URM. One consideration is that URMs may not terminate for every input. For instance, consider the set of URMs defined by these instructions:

$$ [S\ 1]; [J\ 1\ 1\ 1] $$.

Given any initial register state, each machine does essentially the same thing: increment the first register forever. The machine will never stop. Does this machine correspond to a function?

We need to clean up some loose/ambiguous language here. I've been talking about "inputs" to a machine and I've just considered all the machines with the same list of instructions to be "the same". That clearly doesn't make any sense. Remember: the initial state was considered to be part of the data specifying an URM, meaning if you change the initial state, you get a different machine.

However, as we saw above, we have instances where "different machines" behave basically identically. This sounds like a job for an equivalence relation! The equivalence classes will be the set of all machines with the same tuple of instructions. Then each class of URMs differs only by the initial configuration. We  might call each equivalence class a "dynamic URM", but it actually be more useful to consider this more general notion to be the "real" definition of an URM. So let's rename our original definition to something like "static URM", and then say an URM is an equivalence class of static URMs with the same instruction tuple.

So our new definition: an **unlimited register machine** is just some $k$-tuple of instructions.

It now makes sense to talk about an "input" to an URM: an **input** of an URM is a state of the machine. Given an input, we can select the static URM in the equivalence class with an initial state the same as the input state and start running that static machine.

Which brings us to our second point, which we touched on above: for any given input, the machine might not terminate. In our first example, the machine didn't terminate for *any* input. If we have in mind the idea of representing functions by a machine, it seems that some inputs will have no outputs.

Hence, we need a broader class of functions than those normally used in mathematics. We need to consider *partial funcitons*, which are just like total functions, except that they  may not be defined for every point in the domain. In the example above the URM "computes" the empty function, which is the (partial) function defined nowhere. This is our first example of a computable function.

An **URM-computable function** is a partial function $f: \mathbb{N}^n \rightarrow \mathbb{N}$ for some $n \in \mathbb{N}$ such that there is an URM $M$ for which $x \in Dom(f)$ (i.e. $x$ is in the subset of $\mathbb{N}^n$ on which $f$ is defined) iff when $x$ is the input of $M$, the output of $M$ is $f(x)$. In this case we also say that $M$ **computes** $f$.

From now on, "function" means "partial function" (though we will occasionally explicitly distinguish between total and partial functions). Also, we will use "computable" as shorthand for "URM-computable" unless otherwise noted.

We will also need a piece of shorthand. When we say that an URM $M$ has an input $(x_1, \ldots, x_n)$, we mean that the first $n$ registers are $x_1$ through $x_n$, and all the registers after that are zero. This will be useful for setting the input of an URM to an element $x = (x_1, \ldots, x_n)$ in the domain of a function $f: \mathbb{N}^n \rightarrow \mathbb{N}$.

### Example

Let's prove that the following function is computable:

$$ f(x) := \cases{
    \frac{x}{2} & \text{if } x \text{ is even} \cr
    \text{undefined} & \text{otherwise}}$$

To do this we will find a tuple of instructions which leads to an URM that terminates only when the initial state is an even number, and which does not terminate when the initial state is an odd number.

$$ [J\ 1\ 3\ 5]; [S\ 2]; [S\ 3]; [S\ 3]; [J\ 1\ 1\ 1]; [T\ 2\ 1]$$

The strategy is to add two's up until we get our number, then return the number of two's we had to add. This strategy handles the case of an odd number since we can never add up two's and get an odd number. Hence the initial jump instruction, $[J\ 1\ 3\ 5]$ will never jump if the initial number is odd.

To be boringly thorough, we prove this explicitly: If we are given an input of $n = 2k$ for some $k$, then the instructions $I_1$ through $I_4$ will be repeated $k$ times. At this point the state is $(n, k, n, 0, 0, \ldots)$ and the instruction counter is $1$ (due to $I_4$). We then execute $I_1$, and the equality check works, so the instruction counter is updated to $5$. $I_5$ then changes the state to $(k, k, n, 0, 0, \ldots)$, and the machine terminates. So the output is $k$.

On the other hand, if the input $n$ is not even, then the equality check in $I_1$ will never succeed, because if we did we would have $n = 2k$ for some $k$, which could not be the case. If that check never succeeds, we will never break out of the loop of instructions $I_1$ through $I_4$. So the machine will never terminate.

So the URM above is an implementation of the function $f$, and thus $f$ is computable.

We should note here that the above tuple of instructions is not the only URM that computes $f$. We could have swapped registers 2 and 3, for instance. We could also add any number of pointless instructions, for instance incrementing the 9-billionth register 5 times on each loop. Such instructions have no effect on the rest of the program, and the only thing that matters in the output is the value of the first register in the final state.

We could have used an entirely different strategy, as well. Consider subtracting 1 from the input and adding 1 to a counter until both values are equal. If the input is even, this will terminate when the input is halved. If it is odd, it will never terminate. The big picture reason is that for an integer $n = 2k + 1$, after substracting $k$, the value will equal $k + 1$ and the counter will equal $k$, and the next decrement/increment will just swap the values. So these two values will never be equal.

Unfortunately, this program is a bit difficult to construct, primarily because we don't have a primitive decrement instruction. We will go ahead and do it anyways for fun and/or practice, but if you already get the point, feel free to skip to the next section. The main thing to realize here is that computable functions are not in one-to-one correspondence with URMs.

To begin, we'll construct a machine for decrementing the input by one. It should only not terminate if the input is zero.

$$ [S\ 3]; [J\ 1\ 3\ 6]; [S\ 2]; [S\ 3]; [J\ 1\ 1\ 2]; [T\ 2\ 1]$$

You can check that this computes the function $f(x) := x - 1$, with $f(0)$ undefined.

If we had a decrement or *predecessor* instruction $[P\ n]$, we could make an alternative machine in this way:

$$ [J\ 1\ 2\ 5]; [P\ 1]; [S\ 2]; [J\ 1\ 1\ 1]$$

If we squint hard enough, we can see that our machine for computing $f(x) = x - 1$ can be thought of as a kind of decrement instruction. So we'll try to just plug it in.

The complication is that the subtract-by-1 machine (call it $O$) and the work-in-progress divide-by-2 machine step on each others toes. $O$ doesn't just subtract one from the first register -- it uses other registers in the process. So we need to ensure that it doesn't mess with any registers that the divide-by-2 machine depends on.

Here's a modification of $O$:

$$ [S\ 4]; [J\ 1\ 4\ 6]; [S\ 3]; [S\ 4]; [J\ 1\ 1\ 2]; [T\ 3\ 1]; [Z\ 3]; [Z\ 4]$$

I've changed two things here. The first is to move the registers we use from 2 and 3 to 3 and 4. This is needed because the halving machine that we're making already uses register 2 as a counter. The second change is to zero out registers 3 and 4 at the end. This is needed because we're going to be decrementing multiple times, and we need a clean workspace every time we start again.

One last thing: the jump instruction indices need to be changed so that they work harmoniously in the new combined program:
 
$$
\begin{split}
&[J\ 1\ 2\ 12];\\
&[S\ 4]; [J\ 1\ 4\ 7]; [S\ 3]; [S\ 4]; [J\ 1\ 1\ 3]; [T\ 3\ 1]; [Z\ 3]; [Z\ 4];\\
&[S\ 2];\\
&[J\ 1\ 1\ 1]
\end{split}
$$

This URM also computes $f$, though it is much more complicated (and less efficient!) than our previous machine. It is easy enough to verify (at least through an example) that the machine works in case the input is even. But does the machine not terminate if the input is odd? If you trace the execution, eventually the machine's state becomes $(0, 3, 0, 0, \ldots)$. At that point it jumps back to the first instruction, the check fails, so it goes to the second line to subtract one from the first register, which in this case is 0. The subtraction sub-process here fails to terminate, for the same reason that the standalone subtraction machine failed to terminate for inputs of 0.

## Decidability

One of our concerns will be finding out whether we can determine computationally if some given candidate is a member of some set. Since our model of computation is URMs, which deal only with functions of numbers, we will be trying to determine if some given number is a member of some distinguished set of natural numbers. It is interesting and easy enough to generalize this to n-tuples of natural numbers, so that we will be interested in computing membership in some n-ary predicate.

Given some $n$-ary predicate $M$, we define a characteristic function $c_M: \mathbb{N}^n \rightarrow \mathbb{N}$ by:

$$ c_M(\overline{x}) := \cases{
    1 & \text{if } \overline{x} \in M \cr
    0 & \text{otherwise}}$$

The predicate $M$ is **decidable** if $c_M$ is computable.

### Example

The set of even numbers is decidable, with this URM:

$$[J\ 1\ 2\ 7]; [J\ 1\ 3\ 8]; [S\ 2]; [S\ 2]; [S\ 3]; [J\ 1\ 1\ 1]; [S\ 4]; [T\ 4\ 1]$$

We use two counters. The first counter we repeatedly add two to, the second just gets increments by one. Using the first counter we check whether the input is a multiple of two. If so, we return 1. The second counter in fact checks every number, not just odd numbers. However, the first counter checks each even number before the second counter checks it, so the second counter will never find a multiple of two (since the first counter would have found it first). So if the second counter matches the input must be odd, and thus the machine returns 0.

It is straightforward to modify this so the second counter only checks odds.

## Combining machines

Can we compose URMs? That is, can we take the instructions of two URMs and put one sequence right after the other, combining them into a single URM? We can, but we shall have to avoid some potential issues.

Let's call the number of instructions of an URM $M$ the **length** $M$. The way that an URM terminates is when its instruction counter exceeds the length. This can happen normally after it executes the last instruction, but it also might happen when a jump instruction jumps to some instruction index greater than the length. This is a problem for composing URMs, because depending on which index a jump in the first machine $M_1$ specifies, we could jump to the first instruction in the second machine, $M_2$, or some instruction in the middle. We want to stipulate that whenever $M_1$ terminates via jumping, that we always start with the first instruction of $M_2$.

So if $M$ is any URM of length $k$, we will want to ensure that the jump index is, at most, $k+1$ (so that we're either jumping to some instruction in $M$, or we jump just past the last instruction). If $M$ satisfies this requirement, then we shall say that $M$ is in **standard form**.

It is an easy task to put a machine into standard form: take any non-standard jump instructions and change them!
