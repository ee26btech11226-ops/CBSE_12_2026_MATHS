import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return (x - 2)**2 + 5

# Domain for full curve
x_full = np.linspace(-3.5, 4.5, 400)
y_full = f(x_full)

# Domain for the interval [-3, 2]
x_interval = np.linspace(-3, 2, 200)
y_interval = f(x_interval)

plt.figure(figsize=(8, 6))

# Plot full curve faintly or in dashed style
plt.plot(x_full, y_full, color='#1f77b4', linestyle='--', alpha=0.5, label=r'$f(x) = (x-2)^2 + 5$')

# Highlight the curve on the specified interval [-3, 2]
plt.plot(x_interval, y_interval, color='#b22222', linewidth=2.5, label='Interval $[-3, 2]$')

# Highlight endpoints and minimum point
plt.scatter([-3, 2], [f(-3), f(2)], color=['black', 'red'], zorder=5)
plt.text(-3, f(-3) + 1, f'(-3, {f(-3)})', fontsize=10, fontweight='bold', ha='right')
plt.scatter(2, f(2), color='red', s=80, zorder=6)
plt.text(2.1, f(2) + 0.5, f'Absolute Min: (2, {f(2)})', fontsize=10, fontweight='bold', color='red')

# Vertical dashed lines for interval boundaries
plt.axvline(-3, color='black', linestyle=':', alpha=0.7)
plt.axvline(2, color='black', linestyle=':', alpha=0.7)

# Formatting graph
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.xlim(-4, 5)
plt.ylim(0, 35)
plt.title(r'Absolute Minimum of $f(x) = (x-2)^2 + 5$ on $[-3, 2]$', fontsize=12, pad=12)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper center')

# Save and show plot
plt.tight_layout()
plt.savefig('../figs/abs_min_plot.png', dpi=300)
plt.show()
