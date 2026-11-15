import numpy as np
import matplotlib.pyplot as plt

# Define the line y = x - 5
x = np.linspace(-4, 2, 400)
y = x - 5

plt.figure(figsize=(6, 4))
plt.plot(x, y, label=r'$f(x) = \frac{x^2 - 4x - 5}{x+1} = x - 5$', color='blue', linewidth=2)

# Highlight the point of continuity at (-1, -6)
plt.plot(-1, -6, 'ro', markersize=8, label=r'Continuous point $(k = -6)$')

# Formatting graph
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.title(r'Continuity of $f(x)$ at $x = -1$', fontsize=12)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower right')

# Save and show plot
plt.tight_layout()
plt.savefig('../figs/Continuous_plot.png', dpi=300)
plt.show()
