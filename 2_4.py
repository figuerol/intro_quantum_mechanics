from sympy import *
from sympy.abc import i, k, m 
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

psi_n = display_and_compute('psi_n',Wavefunction(sqrt(2/a)*sin(n*pi/a*x),x))
#<x>
E_x = display_and_compute('<x>',integrate(psi_n(x)*x*conjugate(psi_n(x)), (x,0,a)))
#<x^2>
E_x_sq = display_and_compute('<x**2>',integrate(psi_n(x)*x**2*conjugate(psi_n(x)), (x,0,a)))
#sigma_x
sigma_x = display_and_compute('sigma_x',sqrt(E_x_sq - E_x**2))
#<p>
f = Function('f')
p = DifferentialOperator(-I*hbar*Derivative(f(x),x), f(x))
E_p = display_and_compute('<p>',integrate(conjugate(psi_n(x))*qapply(p*psi_n)(x), (x,0,a)))
E_p_sq = display_and_compute('<p**2>',integrate(conjugate(psi_n(x))*qapply(p**2*psi_n)(x), (x,0,a)))
# sigma_p
sigma_p = display_and_compute('sigma_p',sqrt(E_p_sq - E_p**2))
# "sigma_x*sigma_p"
display_and_compute("sigma_x*sigma_p",simplify(sigma_x*sigma_p))
print("uncertainty priniple check")
#display(reduce_inequalities([simplify(sigma_x*sigma_p)>=hbar/2],[]))
display(simplify(sigma_x*sigma_p)>=hbar/2)
print("Check for n=1, the  lfs of above is increasing with n")
display(simplify(sigma_x*sigma_p).subs(n,1)>=hbar/2)
