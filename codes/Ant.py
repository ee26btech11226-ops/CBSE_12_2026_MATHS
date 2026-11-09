#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q12
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#area between y = 2x - 4, the x-axis, the y-axis and x = 1
area, _ = quad(lambda t: abs(2*t - 4), 0, 1)
print("Area =", area)

x = np.linspace(-0.5, 2.5, 200)
fig, ax = plt.subplots(figsize=(6, 5), layout='constrained')
ax.plot(x, 2*x - 4, 'b-', label=r'$y=2x-4$')
ax.axvline(1, color='r', linestyle='--', label=r'$x=1$')
xs = np.linspace(0, 1, 100)
ax.fill_between(xs, 2*xs - 4, 0, color='tab:green', alpha=0.35, label='Area $=3$')
for pt, lab in [((0, -4), '(0,-4)'), ((1, -2), '(1,-2)'), ((2, 0), '(2,0)'), ((1, 0), '(1,0)')]:
    ax.plot(*pt, 'ko'); ax.annotate(lab, pt, textcoords='offset points', xytext=(6, 6), fontsize=8)
ax.axhline(0, color='k', linewidth=1); ax.axvline(0, color='k', linewidth=1)
ax.set_xlim(-0.5, 2.5); ax.set_ylim(-4.6, 1)
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.grid(True, linestyle='--', alpha=0.5); ax.legend(loc='lower right', fontsize=8)
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Ant.pdf'))
