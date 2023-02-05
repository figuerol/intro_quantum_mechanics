# Notes on Hermitian inner product.


I asked myself, why is conjugation necessary in the definition of Hermitian inner product for complex numbers?
After trying out the most simple example I could think of, I connected some dots from differential geometry I hadn't thought about in some time.


A hermitian inner product on a complex vector space $V$ is a map $\lt\ \gt:V\times V\rightarrow \mathbb{C}$ such that

* $\lt\ \gt$ is linear in the first factor (sesquilinear)
* $\lt\ \gt$ is positive definite 
* $\lt x\ |\ y\gt = \lt y\ | \ x \gt^\ast$

 The third item above is what I wasn't sure I understood the motivation of. Why not just require symmetry (and hence bilinearity) like the definition for real vector spaces?

As an example to see what would happen, consider $V=\mathbb{C}$ as a on dimensional complex vector space. Then complex multiplication is a symmetric bilinear map and $\lt z_1, z_2 \gt= z_2^\ast \ z_1$ is a Hermitian inner product as in the definition above. 

Complex multiplication, however, is not positive semidefinite $i^2=-1$. So this does not help towards defining a geometry in the space. 

Lets investigate the Real and Imaginary parts of our Hermitian inner product. If we write $a+bi = (a\ b)$ as indentified in $\mathbb{R^2}$, then for the imaginary and real parts of our the complex product are represented (respectively) by the folowing bilinear forms:
```math
\omega=\begin{pmatrix}
            0 & -1\\
            1 & 0
        \end{pmatrix}

Id=\begin{pmatrix}
            1 & 0\\
            0 & 1
        \end{pmatrix}
```
The real part is just the usual inner product on $\mathbb{R}^2$, and the complex part is a alternating non-degenerate 2-form, called the  Kähler form on $\mathbb{C}$ (coinciding with the determinant of the $2\times 2$ matrix obtained by stacking the 2 vector representations of $z_1$ and $z_2$). 

Reference: (https://math.stackexchange.com/questions/3291283/geometric-interpretation-of-complex-inner-products)

At this point I remembered something about complex structures in differential geometry. Restricting to our simple on dimensional complex vector space example, let's examine multiplication by $i$.   Again thinking of our one dimensional complex vector space as $\mathbb{R}^2$, we can represent our $i$ multiplication operator by the following matrix
```math
J=\begin{pmatrix}
            0 & 1\\
            -1 & 0
        \end{pmatrix}
```
This is called a complex structure for $V$.

This $J$ matrix can also be obtained by looking at the image of $i$ under the real $2\times 2$ matrix representation of complex number algebra as 
```math
a+bi\mapsto \begin{pmatrix}
            a & -b\\
            b & a
            \end{pmatrix}
```
One nice fact about this representation, is that conjugation corresponds exactly to taking a transpose of the matrix, which goes back to the relation about conjugation in the Hermitian definition vs symmetry for the real case.
 On the other hand, we can see that the standard inner product in $\mathbb{R}^2$ corresponds to $\omega(z_1,Jz_2)$ for any $z_1,z_2 \in \mathbb{C}$. So $z_2^\ast z_1 = \omega(z_1,Jz_2)+i\omega(z_1,z_2)$

Refs: (https://en.wikipedia.org/wiki/Symplectic_matrix#Symplectic_transformations,
https://en.wikipedia.org/wiki/Linear_complex_structure)

It turns out I still don't have a good motivation for why this conjugate comes into play for complex vector spaces and inner product definitions, but none the less, it was fun working out a simple example for the generalization of this concepts to complex manifolds.
