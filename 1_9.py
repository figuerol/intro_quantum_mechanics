from sympy import *
from sympy.physics.quantum.operator import DifferentialOperator
from sympy.physics.quantum.qapply import qapply
from sympy.physics.quantum.state import Wavefunction
from sympy.physics.quantum.constants import hbar
init_printing() 

# Setup
x, t = symbols('x t', real=True)
a, A, m = symbols('a A m', positive=True, real=True)
Psi = A*exp(-a*((m*x**2/hbar)+I*t))
f = Function('f')
p = DifferentialOperator(-I*hbar*Derivative(f(x,t),x), f(x,t))
dt = DifferentialOperator(diff(f(t),t), f(t))

# a)
A = solve(integrate(Psi*conjugate(Psi), (x,-oo,oo))-1, A )[0]
Psi = A*exp(-a*((m*x**2/hbar)+I*t))
# b)
V = symbols('V', real=True, negative=False)
Sch = I*hbar*diff(Psi, t) - (-hbar**2/(2*m)*diff(Psi,x,2) + V*Psi)
V = simplify(solve(Sch,V))
# c)
E_x = integrate(Psi*x*conjugate(Psi), (x,-oo,oo)) 
E_x_sq = integrate(Psi*x**2*conjugate(Psi), (x,-oo,oo)) 
E_p = integrate(conjugate(Psi)*-I*hbar*diff(Psi,x), (x,-oo,oo))
E_p_sq = integrate(conjugate(Psi)*-I*hbar*diff(-I*hbar*diff(Psi,x),x), (x,-oo,oo)) 
# d)
sigma_x = sqrt(E_x_sq - E_x**2)
sigma_p = sqrt(E_p_sq - E_p**2)
assert sigma_x*sigma_p>=hbar/2

PsiWave = Wavefunction(A*exp(((x**2/hbar)+I*t)))
qapply(p*PsiWave)