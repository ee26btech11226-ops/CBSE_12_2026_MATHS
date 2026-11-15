#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q3
import os
import numpy as np
import matplotlib.pyplot as plt

d = os.path.dirname(os.path.abspath(__file__))
pi = np.pi
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained')

#(a) cosec x on [-pi/2, pi/2] - {0}: undefined at x = 0, takes values in (-inf,-1] U [1,inf)
xl = np.linspace(-pi/2, -0.15, 300); xr = np.linspace(0.15, pi/2, 300)
a1.plot(xl, 1/np.sin(xl), 'b'); a1.plot(xr, 1/np.sin(xr), 'b')
a1.axvline(0, color='r', linestyle='--', label=r'$x=0$: $\sin x=0$, cosec undefined')
a1.plot([-pi/2, pi/2], [-1, 1], 'ko')
a1.axhspan(-1, 1, color='gray', alpha=0.2, label=r'no values in $(-1,1)$')
a1.set_ylim(-6, 6); a1.set_xlabel('$x$'); a1.set_ylabel(r'$y=\mathrm{cosec}\,x$')
a1.set_title(r'(a) $\mathrm{cosec}\,x$ on $[-\pi/2,\pi/2]-\{0\}$')
a1.grid(True, linestyle='--', alpha=0.5); a1.legend(fontsize=8, loc='lower right')

#(b) inverse: reflect about y = x, so range of cosec^{-1} is [-pi/2, pi/2] - {0}
a2.plot(1/np.sin(xl), xl, 'b'); a2.plot(1/np.sin(xr), xr, 'b')
a2.plot([-1, 1], [-pi/2, pi/2], 'ko')
a2.axhline(0, color='r', linestyle='--', label=r'$y=0$ is never attained')
a2.set_xlim(-6, 6); a2.set_xlabel('$x$'); a2.set_ylabel(r'$y=\mathrm{cosec}^{-1}x$')
a2.set_yticks([-pi/2, 0, pi/2]); a2.set_yticklabels([r'$-\pi/2$', '0', r'$\pi/2$'])
a2.set_title(r'(b) $\mathrm{cosec}^{-1}x$: domain $\mathbb{R}-(-1,1)$')
a2.grid(True, linestyle='--', alpha=0.5); a2.legend(fontsize=8, loc='lower right')
fig.savefig(os.path.join(d, 'Cosec.png'), dpi=200)
