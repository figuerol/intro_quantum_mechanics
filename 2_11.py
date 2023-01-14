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

def check_uncertainty(psi_wave_fn):

    psi = display_and_compute('psi',psi_wave_fn)
    #<x>
    E_x = display_and_compute('<x>',integrate(psi(x)*x*conjugate(psi(x)), (x,-oo,oo)))
    #<x^2>
    E_x_sq = display_and_compute('<x**2>',integrate(psi(x)*x**2*conjugate(psi(x)), (x,-oo,oo)))
    #sigma_x
    sigma_x = display_and_compute('sigma_x',sqrt(E_x_sq - E_x**2))
    #<p>
    f = Function('f')
    p = DifferentialOperator(-I*hbar*Derivative(f(x),x), f(x))
    E_p = display_and_compute('<p>',integrate(conjugate(psi(x))*qapply(p*psi)(x), (x,-oo,oo)))
    E_p_sq = display_and_compute('<p**2>',integrate(conjugate(psi(x))*qapply(p**2*psi)(x), (x,-oo,oo)))
    # sigma_p
    sigma_p = display_and_compute('sigma_p',sqrt(E_p_sq - E_p**2))
    # "sigma_x*sigma_p"
    display_and_compute("sigma_x(sigma_p)",simplify(sigma_x*sigma_p))
    print("uncertainty principle check")
    #display(reduce_inequalities([simplify(sigma_x*sigma_p)>=hbar/2],[]))
    display(simplify(sigma_x*sigma_p)>=hbar/2)

# a) and b)
omega = Symbol('omega', real=True, positive=True)
m = Symbol('m', real=True, positive=True)
psi_0_expr = (omega*m/(pi*hbar))**(1/4)*exp(-m*omega/(2*hbar)*x**2)
print('psi_0')
psi_0 = Wavefunction(psi_0_expr,x)
check_uncertainty(psi_0) 
print('psi_1')
psi_1 =  Wavefunction(simplify(psi_0_expr*x*sqrt(2*m*omega/hbar)),x)
check_uncertainty(psi_1) 

# c)
# by Example 2.5 <V> = m*omega**2/2*<x^2> and <T> = <p^2>/2m
# Hence (looking at stdout from above)
# From Eq 2.62 we expect E_n = (n+1/2)*hbar*omega
# For psi_0 
# <T>+<V> = m*omega/2*<x^2> + <p^2>/2m = h*omega/4 + h*omega/4 = h*omega/2 = E_0
# For psi_1
# <T>+<V> = m*omega/2*<x^2> + <p^2>/2m = 3*h*omega/4 + 3*h*omega/4 = 3*h*omega/2 = E_1
