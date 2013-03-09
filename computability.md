# Notes on computability

## Basic notions
Let $[n] = \{1, \ldots, n\}$. $\mathbb{P}$ is the positive integers, while $\mathbb{N}$ is the nonnegative integers (also referred to as the natural numbers).

An **unlimited register machine (URM)** is

 - an *initial register state* $\text{init}: \mathbb{P} \rightarrow \mathbb{N}$
 - a k-tuple $(I_1, \ldots, I_k)$ of *instructions*, where each $I_j$ is one of the following: $(Z, n)$, $(S, n)$, $(T, m, n)$, $(J, m, n, i)$ with $m, n, i \in \mathbb{P}$.

The interpretation is that an URM is a machine with an infinite collection of registers, each register capable of storing an arbitrarily large natural number. The machine accepts four different kinds of instructions: a *zero* instruction, $(Z, n)$, for setting the $n$-th register to 0, a *successor* instruction, $(S, n)$ for incrementing te $n$-th register by 1, a *transfer* instruction, $(T, m, n)$ for copying the current contents of register $m$ to register $n$, and a *jump* instruction, $(J, m, n, i)$, which compares the values in registers $m$ and $n$ and sets the next instruction to be instruction $i$ iff the values are equal.

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

Here's a question: what happens when the instruction counter no longer points to a valid instruction (by acquiring a value that exceeds the index on the last instruction)? We can't really expect the URM to do anything, so it must stop. Therefore, supposing that an URM has $k$ instructions, the machine runs as long as its instruction counter has a value in $[k]$.

We might also think of introducing some kind of notion for the *trace* of an URM, meaning the sequence of states that the machine goes through. This could be useful, but it turns out that it is more interesting to consider the *final* state of the machine. Actually, we don't need the whole state, just the state of one of the registers.

The state at the time when the URM stops running will be called the *final state*. If $s$ is the final state for an URM, then we will define the **output** of that URM to be $s(1)$. That is, the output of an URM is the value of the first register in the final state.

## Computable functions

The reason we care about so-called "outputs" of an URM is that we will be studying "computable functions", which are functions whose input/output pairs can be given by an URM. One consideration is that URMs may not terminate for every input. For instance, consider the set of URMs defined by these instructions:

$$ [S\ 1]; [J\ 1\ 1\ 1] $$.

Given any initial register state, each machine does essentially the same thing: increment the first register forever. The machine will never stop. Does this machine correspond to a function?

We need to clean up some loose/ambiguous language here. I've been talking about "inputs" to a machine and I've just considered all the machines with the same list of instructions to be "the same". That clearly doesn't make any sense. Remember: the initial state was considered to be part of the data specifying an URM, meaning if you change the initial state, you get a different machine.

However, as we saw above, we have instances where "different machines" behave basically identically. This sounds like a job for an equivalence relation! The equivalence classes will be the set of all machines with the same tuple of instructions. Then each class of URMs differs only by the initial configuration. We  might call each equivalence class a "dynamic URM", but it actually be more useful to consider this more general notion to be the "real" definition of an URM. So let's rename our original definition to something like "static URM", and then say an URM is an equivalence class of static URMs with the same instruction tuple.

It now makes sense to talk about an "input" to an URM: an **input** of an URM is a state of the machine. Given an input, we can select the static URM in the equivalence class with an initial state the same as the input state and start running that static machine.

Which brings us to our second point, which we touched on above: for any given input, the machine might not terminate. In our first example, the machine didn't terminate for *any* input. If we have in mind the idea of representing functions by a machine, it seems that some inputs will have no outputs.

Hence, we need a broader class of functions than those normally used in mathematics. We need to consider *partial funcitons*, which are just like total functions, except that they  may not be defined for every point in the domain. In the example above the URM "computes" the empty function, which is the (partial) function defined nowhere. This is our first example of a computable function.

An **URM-computable function** is a partial function $f: \mathbb{N}^n \rightarrow \mathbb{N}$ such that there is an URM $M$ for which $x \in Dom(f)$ iff when $x$ is the input of $M$, the output of $M$ is $f(x)$.

From now on, "function" means "partial function" (though we will occasionally explicitly distinguish between total and partial functions). Also, we will use "computable" as shorthand for "URM-computable" unless otherwise noted.
