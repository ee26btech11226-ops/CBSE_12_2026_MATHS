import numpy as np
from fractions import Fraction

b  = np.array([2, -4, 5])
a0 = np.array([3, 2, 0])          # a = a0 + lambda*e3
e3 = np.array([0, 0, 1])

# a^T b = a0^T b + lambda (e3^T b) = 0
lam = Fraction(-int(a0 @ b), int(e3 @ b))
print("lambda =", lam, "=", float(lam))

a = a0 + float(lam)*e3
print("a =", a)
print("a^T b =", a @ b)
print("angle between a and b =", np.degrees(np.arccos(a @ b/(np.linalg.norm(a)*np.linalg.norm(b)))), "degrees")

# the other options do not make the strips perpendicular
for opt, l in [("A", 1), ("B", 5/2), ("C", 2/5), ("D", 0)]:
    print(f"({opt}) lambda = {l:.2f}: a^T b = {np.array([3, 2, l]) @ b:.2f}")
