#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q18, Q31, Q37
from fractions import Fraction as F
import itertools

#Q18
PA, PB = F(3, 5)/3, F(3, 5)
PAB = F(2, 3)*PB
print("Q18: P(A)=", PA, " P(A and B)=", PAB, " P(A or B)=", PA + PB - PAB, " (note P(AB) > P(A))")

#Q31(a): one throw of a die
S = set(range(1, 7)); A, B, C = {1, 2, 5}, {3, 5}, {2, 3, 4, 5}
pr = lambda E: F(len(E), len(S))
cond = lambda E, G: pr(E & G)/pr(G)
print("Q31a:", cond(A, C), cond(C, A), cond(A & B, C), cond(A | B, C))

#Q31(b): two cards with replacement
S2 = list(itertools.product(range(1, 7), repeat=2))
EA = [s for s in S2 if sum(s) == 10]
EB = [s for s in S2 if s[0] != 4]
EAB = [s for s in EA if s in EB]
print("Q31b: P(A)=", F(len(EA), 36), " P(B)=", F(len(EB), 36), " P(AB)=", F(len(EAB), 36), " P(A)P(B)=", F(len(EA), 36)*F(len(EB), 36))

#Q37
p = [F(25, 100), F(35, 100), F(40, 100)]       #P(A1), P(A2), P(A3)
q = [F(60, 100), F(55, 100), F(50, 100)]       #P(E|Ai), E: protected
PE = sum(pi*qi for pi, qi in zip(p, q))
print("Q37: (i)", 1 - q[1], " (ii)", PE, float(PE))
print("     (iii a) P(A1 | infected) =", p[0]*(1 - q[0])/(1 - PE), float(p[0]*(1 - q[0])/(1 - PE)))
print("     (iii b) P(A3 | not infected) =", p[2]*q[2]/PE, float(p[2]*q[2]/PE))
