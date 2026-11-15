import numpy as np
import matplotlib.pyplot as plt

# Define x ranges avoiding the vertical asymptote at x = -1
x1 = np.linspace(-6, -1.05, 400)
x2 = np.linspace(-0.95, 6, 400)

# Define f(x) = (x - 3) / (x + 1)
y1 = (x1 - 3) / (x1 + 1)
y2 = (x2 - 3) / (x2 + 1)

plt.figure(figsize=(8, 6))

# Plot the two branches of the function
plt.plot(x1, y1, color='#1f77b4', linewidth=2.5, label=r'$f(x) = \frac{x-3}{x+1}$')
plt.plot(x2, y2, color='#1f77b4', linewidth=2.5)

# Vertical asymptote at x = -1
plt.axvline(-1, color='red', linestyle='--', linewidth=1.5, label=r'Asymptote $x = -1$')

# Horizontal asymptote at y = 1
plt.axhline(1, color='gray', linestyle='--', linewidth=1.2, label=r'Asymptote $y = 1$')

# Annotate that the function is increasing on its intervals
plt.text(-4, 4, 'Increasing on\n$(-\infty, -1)$', fontsize=10, fontweight='bold', color='#1f77b4', bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#1f77b4'))
plt.text(2, -2, 'Increasing on\n$(-1, \infty)$', fontsize=10, fontweight='bold', color='#1f77b4', bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#1f77b4'))

# Formatting graph
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlim(-6, 6)
plt.ylim(-6, 8)
plt.title(r'Graph of $f(x) = \frac{x-3}{x+1}$ (Increasing for all $x \in \mathbb{R} \setminus \{-1\})$', fontsize=11, pad=12)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower right')

# Save and show plot
plt.tight_layout()
plt.savefig('../figs/1.2.23', dpi=300)
plt.show()
