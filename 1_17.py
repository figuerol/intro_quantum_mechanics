from sympy import *
from sympy.physics.quantum.constants import hbar

init_printing() 
# a)
# Equation 1.24 needs to be modified if V has non zero imaginary part. 
# The result can be easily deduced by following the same calculations that arrive at 1.27
# b) 
Gamma = symbols('Gamma', positive=True, real=True)
t, tau = symbols('t tau', real=True)
P = Function('P')
print(dsolve(Eq(P(t).diff(t),-2*Gamma/hbar*P(t)), P(t)))
print(tau,"=",solveset(Eq(2*Gamma*t/hbar,t/tau), tau))