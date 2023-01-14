from sympy import *
from sympy.abc import i, k  
from sympy.stats import E, ContinuousRV
from sympy.physics.quantum import qapply
from sympy.physics.quantum.constants import hbar
from sympy.physics.quantum.operator import DifferentialOperator
from sympy.physics.quantum.state import Wavefunction

init_printing() 
c = IndexedBase('c')
n = var('n', integer=True, positive=True)
x = Symbol('x', positive=True, real=True)
a = Symbol('a', positive=True, real=True)
t = Symbol('t')


def display_and_compute(var_name:str, expr):
    var = Symbol(var_name)
    simp_expr =simplify(expr)
    display(Eq(var,simp_expr))
    print()
    return simplify(expr)

# <x^2> 
# from example 2.5 we get 
omega = Symbol('omega', real=True, positive=True)
m = Symbol('m', real=True, positive=True)
V = display_and_compute('V',omega*hbar/2*(n+1/2))
display(f"On the other hand V={m*omega**2/2}*<x**2>")

# <x> and <p>
# Use that  x = C(a_+ + a_-)  and p = K (a_+ - a_-)
# also that psi_n is proportional to a_-(psi_{n+1}) and a_+(psi_{n-1})
# and that psi_n, psi_{n+1} and psi_{n-1} are orthogonal
# we can compute that <x>=<p>=0

#<p^2>
# Similarly using p = K (a_+ - a_-) we should get
# <p**2> = hbar*omega/2*(n-1/2)

# <T> = <p^2>/2m
