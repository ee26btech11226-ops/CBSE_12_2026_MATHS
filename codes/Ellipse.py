#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q34
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#100 x^2 + 25 y^2 = 2500  <=>  x^T V x = 2500
V = np.diag([100.0, 25.0])
c = 2500.0
lam = np.linalg.eigvalsh(V)
print("eigenvalues of V:", lam, " semi-axes:", np.sqrt(c/lam))

#area by integration: 4 * int_0^5 y dx
area, _ = quad(lambda t: 4*2*np.sqrt(25 - t**2), 0, 5)
print("area by integration =", area, " 50 pi =", 50*np.pi, " pi c/sqrt(det V) =", np.pi*c/np.sqrt(np.linalg.det(V)))

theta = np.linspace(0, 2*np.pi, 400)
fig, ax = plt.subplots(figsize=(5, 6), layout='constrained')
ax.plot(5*np.cos(theta), 10*np.sin(theta), 'b-')
ax.fill(5*np.cos(theta), 10*np.sin(theta), alpha=0.25)
for pt, lab in [((5, 0), '(5,0)'), ((-5, 0), '(-5,0)'), ((0, 10), '(0,10)'), ((0, -10), '(0,-10)')]:
    ax.plot(*pt, 'ko'); ax.annotate(lab, pt, textcoords='offset points', xytext=(5, 5), fontsize=8)
ax.set_aspect('equal'); ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../figs/Ellipse.png'), dpi=200)
