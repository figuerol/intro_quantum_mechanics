#Time indep Sch \hat{H}\phi=E\phi
from sympy import *
from sympy.physics.quantum.constants import hbar

init_printing() 

psi = Function('psi')
x = Symbol('x')
m = Symbol('m')
E = Symbol('E')
V = Function('V')
V_min = Symbol('V_min')
display("Rewriting Schrodinger (time indep) using the hint:")
display(Eq(psi(x).diff(x), 2*m/hbar*(V(x)-E)*psi(x)))
display("As:")
display(0<V_min-E)
display('Then:')
display(0<V(x)-E)
display(f'Hence {psi} and {psi(x).diff(x)} must have the same sign')
display(f'Try different cases and examples to see that {psi} must be unbounded at {oo}')