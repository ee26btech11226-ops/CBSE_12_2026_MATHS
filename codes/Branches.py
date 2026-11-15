#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q3, all four principal value branches
import os
import numpy as np
import matplotlib.pyplot as plt

d = os.path.dirname(os.path.abspath(__file__))
pi = np.pi
x = np.linspace(-6, 6, 1000)
xp = np.linspace(1, 6, 500)          #x >= 1
xn = -xp[::-1]                       #x <= -1
ticks = [0, pi/2, pi]; tl = ['0', r'$\pi/2$', r'$\pi$']
tick2 = [-pi/2, 0, pi/2]; tl2 = [r'$-\pi/2$', '0', r'$\pi/2$']

fig, ax = plt.subplots(2, 2, figsize=(10, 8), layout='constrained')

#(A) tan^{-1}: R -> (-pi/2, pi/2)
a = ax[0, 0]
a.plot(x, np.arctan(x), 'b')
for y in (-pi/2, pi/2): a.axhline(y, color='r', linestyle='--')
a.set_yticks(tick2); a.set_yticklabels(tl2)
a.set_title(r'(A) $\tan^{-1}x$: $\mathbb{R}\to(-\pi/2,\pi/2)$')

#(B) sec^{-1}: R-(-1,1) -> [0,pi]-{pi/2}
a = ax[0, 1]
a.plot(xp, np.arccos(1/xp), 'b'); a.plot(xn, np.arccos(1/xn), 'b')
a.plot([1, -1], [0, pi], 'ko')
a.axhline(pi/2, color='r', linestyle='--', label=r'$y=\pi/2$ not attained')
a.set_yticks(ticks); a.set_yticklabels(tl); a.legend(fontsize=8, loc='lower right')
a.set_title(r'(B) $\sec^{-1}x$: $\mathbb{R}-(-1,1)\to[0,\pi]-\{\pi/2\}$')

#(C) cot^{-1}: R -> (0,pi)
a = ax[1, 0]
a.plot(x, pi/2 - np.arctan(x), 'b')
for y in (0, pi): a.axhline(y, color='r', linestyle='--')
a.set_yticks(ticks); a.set_yticklabels(tl)
a.set_title(r'(C) $\cot^{-1}x$: $\mathbb{R}\to(0,\pi)$')

#(D) cosec^{-1}: R-(-1,1) -> [-pi/2,pi/2]-{0}  (the paper's option omits {0})
a = ax[1, 1]
a.plot(xp, np.arcsin(1/xp), 'b'); a.plot(xn, np.arcsin(1/xn), 'b')
a.plot([1, -1], [pi/2, -pi/2], 'ko')
a.axhline(0, color='r', linestyle='--', label=r'$y=0$ not attained')
a.set_yticks(tick2); a.set_yticklabels(tl2); a.legend(fontsize=8, loc='lower right')
a.set_title(r'(D) $\mathrm{cosec}^{-1}x$: $\mathbb{R}-(-1,1)\to[-\pi/2,\pi/2]-\{0\}$')

for a in ax.ravel():
    a.set_xlim(-6, 6); a.set_xlabel('$x$'); a.set_ylabel('$y$')
    a.grid(True, linestyle='--', alpha=0.5)
fig.savefig(os.path.join(d, 'Branches.pdf'))
