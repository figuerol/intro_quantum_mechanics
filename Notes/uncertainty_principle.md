# Thoughts on uncertainty principle

I was thinking on how uncertainty principle, commutators and obervables are related. I had asked myself the following question.


     Where do Hermitian operators come from in Quantum mechanics?

This was a question I had difficulty finding an answer I could digest with my limited understanding in stack-overflow and wikipedia. But the answer is actually very nicely stated in chapter 1 and 3 of Griffiths' book.
 The first part is that position and momentum can be viewed as operators, namely, $x$ and $i\hbar \frac{\partial }{\partial x}$. Now, Griffith's claims that any observable $Q$ in physics can be viewed as a function of position $x$ and momentum $p$, $Q(x,p)$. Hence, any observable can be viewed as an operator by replacing $x$ and $p$ with its corresponding operator in their formula $Q(x,\frac{\partial }{\partial x_i})$.

Now, the second piece of the answer is found in chapter three. The expectation (mean measurement of repeated experiments) of any observable should be a real number. Hence, 
```math
\lt Q \gt=\lt Q \gt^{\ast}
```
where $^\ast$ is used to symbolize the conjugate and $<>$ denores the expectation. Denote by $<.\ ,\ .>$, the inner product of the Hilbert space of states.
Therefore, for any state $\Psi$ we have 
```math
\lt\Psi,Q\Psi\gt=\lt Q \gt=\lt Q \gt^*=\lt \Psi,Q^*\Psi \gt=\lt Q\Psi,\Psi \gt
```
Which by definition means that the operator $Q$ is self adjoint.

 Then I read the excercise in chapter three that asks wether the composition of two self adjoint operators is self adjoint. So I gave it a try using the definitions and I realized that this true if the operators commute ( TODO:check necessity too, should be true). Then I rememebered the following fact from linear algebra, if two self adjoint linear transformations commute then they are simultanueously diagonalizable.
 
  When this came into the picture I remembered the wikipedia post on uncertainty principle and commutator relation of $x$ and $p$, $[x,p]=-i\hbar$. This is where it got really interesting. I recalled that Qiskit tutorial had mentioned on choosing the right basis for a sequence of gates and also the wikipedia article on the probability amplitudes (TODO: check this) that given an obervable, we want to choose a basis which diagonalizes it, so that measurements become certain in every direction of the basis. This is what ultimately gave it out.

  Uncertainty principle says:"you cannot narrow down measurements of position and momentum at the same time", that is , the more certain you are about momentum, the less certain you will be about its position. Griffiths displays it in chapter one as the equation $\sigma_x\sigma_p\geq\frac{\hbar}{2}$ where $\sigma$ denotes the corresponding standard deviation of the observable in the current state.
  But this can be viewed as a fact purely on their corresponding operators. Since $x$ and $p$ do not commute, then you cannot simultaneously diagonalize them. That is, you cannot pick a state basis which makes the measurements of $x$ and $p$ certain for every element in it. 

  Then I started thinking, what does this mean in terms of a basis diagonalizing $x$ ?  Since the basis of eigenvalues can be made orthonormal (from self adjointness), then we know the probability density of a position measurement would be given by the sum of the norms of the coefficients of the state of the particle when expressed as a linear combination of the diagonalizing basis. 
  
  The above observation seems part of something even deeper. Having certainty of the measurement means the norms of the basis coefficients are mostly (or actually) 0 except for a single element. So that means that for an eigenstate of position, its representation in a diagonalizing basis of momentum, will necessarily by "flatter" in terms of coefficients (which represents the probability distribution of momentum measurement). 
  So I wonder, what exactly algebro-geometrically is going on here between simultaneous diagonalization and the norm of the coefficients of  a position diagonalizing eigenstate when represented in a diagonalizing states of momentum?
