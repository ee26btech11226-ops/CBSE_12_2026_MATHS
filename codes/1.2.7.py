import numpy as np
import matplotlib.pyplot as plt

A = np.array([3, 1])
B = np.array([-2, 1])

# area of triangle ABC = (1/2)|det[B-A  C-A]|
def area(C):
    return 0.5*abs(np.linalg.det(np.column_stack((B - A, C - A))))

fig, ax = plt.subplots(figsize=(7, 7))

for k, col in [(3, "tab:green"), (-1, "tab:orange")]:
    C = np.array([0, k])
    print(f"k = {k:2d}, area = {area(C):.1f}")
    pts = np.array([A, B, C, A])
    ax.fill(pts[:, 0], pts[:, 1], color=col, alpha=0.3)
    ax.plot(pts[:, 0], pts[:, 1], color=col, linewidth=1.8,
            label=f"$k={k}$, area $={area(C):.0f}$")
    ax.plot(*C, "ko")
    ax.annotate(f"C({C[0]},{C[1]})", C, textcoords="offset points", xytext=(8, 6), fontsize=9)

for P, name, off in [(A, "A", (8, 6)), (B, "B", (2, 6))]:
    ax.plot(*P, "ko")
    ax.annotate(f"{name}({P[0]},{P[1]})", P, textcoords="offset points", xytext=off, fontsize=9)

ax.axhline(0, color="k", linewidth=1)
ax.axvline(0, color="k", linewidth=1)
ax.set_xlim(-3, 5)
ax.set_ylim(-2, 4)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(loc="lower right")

plt.savefig("figs/Triangle.png", dpi=150, bbox_inches="tight")
plt.show()
