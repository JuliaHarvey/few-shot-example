# few-shot-example
Note: Much of the below information is rewritten from the original paper or other sources for my own understanding.  Pls do not sue.
# Dataset
Covers data based option: One large dataset with no specific labeled examples.  For example, training to id robins, you would use a dataset of many different varieties of birds.
# Meta Learning Setup
### Tasks
A task is T = {L(x1, a1, . . . , xH, aH), q(x1), q(xt+1|xt, at), H}, where L is a loss function, q(x1) is the distribution over initial observations, q(xt+1|xt, at) is a transitional distribution, and H is the episode length.  
#### H: Period length
In i.i.d. (independent and identically distributed) supervised learning, H = 1.  Samples are generated using H where a sample at is pulled at time (t) = H*n.  
#### Loss
Loss (L(x1, a1, . . . , xH, aH) → R) provides task specific feedback (misclassification, cost in Markov decision process).

## K-shot learning
distribution over tasks = p(T)
model needs to learn new Task (Ti) drawn from p(T) using only K samples drawn from qi and feedback L(qi) from Ti, testing on new examples from Ti
