import sympy as sp
x = sp.symbols('x', positive=True)
#Q27(a)
print("Q27a: d/dx[-x cot(x/2)] - integrand at x=1.1 :", sp.N((sp.diff(-x*sp.cot(x/2), x) - (x - sp.sin(x))/(1 - sp.cos(x))).subs(x, 1.1)))
#Q27(b)
val = sp.Integral(1/sp.sqrt(x**2 + 2*x + 3), (x, 0, 2)).evalf()
print("Q27b:", val, sp.N(sp.log((3 + sp.sqrt(11))/(1 + sp.sqrt(3)))))
