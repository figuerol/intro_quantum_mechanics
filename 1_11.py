from sympy import *
init_printing() 
# a)
E, V, m, v = symbols('E V m v', real=True, negative=False)
T = m * v**2/2
v = solve(E-(T+V), v, domain=Interval(0,oo))

# b)
x, v, a, b = symbols('x v a b', real=True)
E, m, k = symbols('E m k', real=True, positive=True)
KE = m * v**2/2
V = k*x**2/2
v = solve(E-(KE+V), v, domain=Interval(0,oo))[1]
T = simplify(integrate(1/v, (x,a,b)))
rho = simplify(1/(v*T))
# Assert normalization
assert simplify(integrate(rho, (x, a,b)))==1

# c)
E_x = simplify(integrate(x*rho, (x,a,b)))
E_x_sq = simplify(integrate(x**2*rho, (x,a,b)))
sigma_x = simplify(sqrt(E_x_sq-E_x**2))