#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q15, Q20, Q29
import os
import numpy as np
import matplotlib.pyplot as plt

#Q15: Z = c^T x at the five corner points
c = np.array([4, 3])
P = np.array([[0, 0], [0, 40], [20, 40], [60, 20], [60, 0]]).T
print("Q15: Z =", c@P, " max =", (c@P).max())

#Q20: Z = x + 2y at the corner points (0,3), (6,0)
c = np.array([1, 2])
P = np.array([[0, 3], [6, 0]]).T
print("Q20: Z =", c@P)

#Q29: maximise Z = 2x/5 + 3y/10, 2x + y <= 1000, x + y <= 800, x, y >= 0
A = np.array([[2, 1], [1, 1]], dtype=float)
b = np.array([1000, 800], dtype=float)
V = np.linalg.solve(A, b)             #intersection of the two lines
P = np.array([[0, 0], [500, 0], V, [0, 800]]).T
c = np.array([2/5, 3/10])
Z = c@P
print("Q29: corner points =\n", P, "\n Z =", np.round(Z, 6), " max =", Z.max())

fig, ax = plt.subplots(figsize=(6, 5), layout='constrained')
x = np.linspace(0, 900, 400)
ax.plot(x, 1000 - 2*x, label=r'$2x+y=1000$')
ax.plot(x, 800 - x, label=r'$x+y=800$')
ax.fill(P[0], P[1], alpha=0.3, color='tab:green', label='Feasible region')
for (px, py), z in zip(P.T, Z):
    ax.plot(px, py, 'ko')
    ax.annotate(f'({px:.0f},{py:.0f})\nZ={z:.0f}', (px, py), textcoords='offset points', xytext=(6, 6), fontsize=8)
ax.set_xlim(-30, 650); ax.set_ylim(-30, 950)
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right', fontsize=8)
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../figs/LPP.png'), dpi=200)
