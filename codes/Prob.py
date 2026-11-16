import numpy as np
from fractions import Fraction as F

one = lambda n: np.ones(n)

# ---------- 1.2.16 : joint pmf of the indicators of A and B ----------
PA, PB, PA_given_B = 1/5, 3/5, 2/3
p22 = PA_given_B*PB                       # Pr(AB)
p21 = PA - p22                            # Pr(AB')
p12 = PB - p22                            # Pr(A'B)
p11 = 1 - p21 - p12 - p22                 # Pr(A'B')
P = np.array([[p11, p12], [p21, p22]])
e = np.array([0, 1])
print("1.2.16 pmf matrix:\n", P)
print("Pr(A)  =", e @ P @ one(2), " Pr(B) =", one(2) @ P @ e)
print("Pr(A+B) = 1 - p11 =", 1 - p11)
print("min entry of P =", P.min(), "(negative => data inconsistent)")

# ---------- 1.2.28(a) : die, indicator vectors ----------
p = np.full(6, 1/6)
a = np.array([1, 1, 0, 0, 1, 0])
b = np.array([0, 0, 1, 0, 1, 0])
c = np.array([0, 1, 1, 1, 1, 0])
pr = lambda v: p @ v
print("\n1.2.28(a)")
print("Pr(A|C)   =", pr(a*c)/pr(c))
print("Pr(C|A)   =", pr(a*c)/pr(a))
print("Pr(AB|C)  =", pr(a*b*c)/pr(c))
print("Pr(A+B|C) =", pr((a + b - a*b)*c)/pr(c))

# ---------- 1.2.28(b) : two draws, joint pmf matrix ----------
q = np.full(6, 1/6)
P = np.outer(p, q)                        # independent draws
i, j = np.meshgrid(range(1, 7), range(1, 7), indexing="ij")
EA = (i + j == 10).astype(float)
EB = (i != 4).astype(float)
PrA, PrB, PrAB = (P*EA).sum(), (P*EB).sum(), (P*EA*EB).sum()
print("\n1.2.28(b)")
print("Pr(A) =", PrA, " Pr(B) =", PrB, " Pr(AB) =", PrAB)
print("Pr(A)Pr(B) =", PrA*PrB, "-> independent?", np.isclose(PrA*PrB, PrAB))

# ---------- 1.2.36 : vaccines ----------
pv = np.array([0.25, 0.35, 0.40])
qv = np.array([0.60, 0.55, 0.50])
P = np.column_stack([pv*qv, pv*(1 - qv)])  # columns: E, E'
col = P.T @ one(3)                         # pmf of the outcome
row = P @ one(2)                           # pmf of the vaccine
print("\n1.2.36\nP =\n", P, "\nvaccine pmf =", row, " outcome pmf =", col)
print("(i)   Pr(E'|A2) =", P[1, 1]/row[1])
print("(ii)  Pr(E)     =", col[0], "=", F(col[0]).limit_denominator(1000))
print("(iii) Pr(A1|E') =", P[0, 1]/col[1], "=", F(P[0, 1]/col[1]).limit_denominator(1000))
print("      Pr(A3|E)  =", P[2, 0]/col[0], "=", F(P[2, 0]/col[0]).limit_denominator(1000))
