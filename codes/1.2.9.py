import os
import numpy as np
import matplotlib.pyplot as plt

# figures are saved in ../figs, relative to this script's folder
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
os.makedirs(figdir, exist_ok=True)

f = lambda x: (x - 2)**2 + 5

# numerical check of the minimum on [-3, 2]
x = np.linspace(-3, 2, 100001)
i = np.argmin(f(x))
print(f"f(-3) = {f(-3):.0f}, f(2) = {f(2):.0f}")
print(f"minimum on [-3, 2]: f({x[i]:.4f}) = {f(x[i]):.4f}")

xx = np.linspace(-3.5, 4.5, 400)
xi = np.linspace(-3, 2, 400)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(xx, f(xx), "--", color="tab:blue", alpha=0.5, label=r"$f(x)=(x-2)^2+5$")
ax.plot(xi, f(xi), color="firebrick", linewidth=2.5, label=r"Interval $[-3,2]$")

ax.plot(-3, f(-3), "ko")
ax.annotate("(-3, 30)", (-3, f(-3)), textcoords="offset points", xytext=(-40, 6),
            fontsize=9, fontweight="bold")
ax.plot(2, f(2), "ro", markersize=8)
ax.annotate("Absolute Min: (2, 5)", (2, f(2)), textcoords="offset points", xytext=(8, 4),
            fontsize=9, fontweight="bold", color="red")

for xv in [-3, 0, 2]:
    ax.axvline(xv, color="k", linestyle=":", linewidth=1)

ax.set_xlim(-4, 5)
ax.set_ylim(0, 35)
ax.set_title(r"Absolute Minimum of $f(x)=(x-2)^2+5$ on $[-3,2]$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.grid(True, linestyle=":", alpha=0.5)
ax.legend(loc="upper center")

plt.savefig(os.path.join(figdir, "1.2.9.png"), dpi=150, bbox_inches="tight")
plt.show()
