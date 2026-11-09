#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q38
import os
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

r, S = sp.symbols('r S', positive=True)
h = (S - sp.pi*r**2)/(2*sp.pi*r)          #open tumbler: S = pi r^2 + 2 pi r h
V = sp.simplify(sp.pi*r**2*h)
dV = sp.diff(V, r)
print("V =", V, "  dV/dr =", sp.simplify(dV))
rstar = sp.solve(dV, r)[0]
print("r* =", rstar, "  h(r*) =", sp.simplify(h.subs(r, rstar)), "  d2V/dr2 =", sp.simplify(sp.diff(V, r, 2).subs(r, rstar)))

Sv = 3*np.pi                               #S = 3 pi  =>  r* = 1 = h*
rr = np.linspace(0.05, np.sqrt(Sv/np.pi) - 0.05, 300)
Vv = (Sv*rr - np.pi*rr**3)/2
fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')
ax.plot(rr, Vv)
ax.plot(1, np.pi, 'ro'); ax.annotate(r'$r^*=h^*=1$', (1, np.pi), textcoords='offset points', xytext=(8, -14))
ax.set_xlabel('$r$'); ax.set_ylabel('$V$'); ax.grid(True, linestyle='--', alpha=0.5)
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../figs/Tumbler_V.png'), dpi=200)
