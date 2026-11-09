#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q8, Q10, Q22, Q23, Q27, Q28, Q33
import sympy as sp

x, y, u, P, Q = sp.symbols('x y u P Q', positive=True)

#Q8
f = sp.acos((sp.sin(x) + sp.cos(x))/sp.sqrt(2))
print("Q8: f'(0.3) =", sp.N(sp.diff(f, x).subs(x, 0.3)))

#Q10
print("Q10: d/dx[(1/sqrt2) log(sec x + tan x)] at 0.4 :", sp.N(sp.diff(sp.log(sp.sec(x) + sp.tan(x))/sp.sqrt(2), x).subs(x, 0.4)),
      " integrand :", sp.N((1/sp.sqrt(1 + sp.cos(2*x))).subs(x, 0.4)))

#Q22(a): d(x^x)/d(x log x)
du = sp.diff(x**x, x); dv = sp.diff(x*sp.log(x), x)
print("Q22a:", sp.simplify(du/dv))
#Q22(b)
yy = P*sp.cos(u*x) + Q*sp.sin(u*x)
print("Q22b:", sp.simplify(sp.diff(yy, x, 2) + u**2*yy))

#Q23
g = (x - 3)/(x + 1)
print("Q23: f'(x) =", sp.simplify(sp.diff(g, x)))

#Q27(a)
print("Q27a: d/dx[-x cot(x/2)] - integrand at x=1.1 :", sp.N((sp.diff(-x*sp.cot(x/2), x) - (x - sp.sin(x))/(1 - sp.cos(x))).subs(x, 1.1)))
#Q27(b)
val = sp.Integral(1/sp.sqrt(x**2 + 2*x + 3), (x, 0, 2)).evalf()
print("Q27b:", val, sp.N(sp.log((3 + sp.sqrt(11))/(1 + sp.sqrt(3)))))

#Q28: x = y^3 + C y solves (x + 2y^3) dy = y dx
C = sp.symbols('C'); xx = y**3 + C*y
print("Q28:", sp.simplify((xx + 2*y**3) - y*sp.diff(xx, y)))

#Q33(a)
s = sp.sqrt(x**2 + 1)
yy = sp.log(s - x)/s
print("Q33a:", sp.simplify((x**2 + 1)*sp.diff(yy, x) + x*yy + 1))
#Q33(b)
h = x**sp.cot(x) + (2*x**2 - 3)/(2*x**2 - x + 2)
mine = x**sp.cot(x)*(sp.cot(x)/x - sp.csc(x)**2*sp.log(x)) + (-2*x**2 + 20*x - 3)/(2*x**2 - x + 2)**2
print("Q33b:", sp.N((sp.diff(h, x) - mine).subs(x, 1.3)))
