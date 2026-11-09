#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q7, Q16, Q17, Q24, Q25, Q30, Q35
import numpy as np

col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)

#Q7: area = 5, A(3,1), B(-2,1), C(0,k)
for k in (3, -1):
    A, B, C = col(3, 1), col(-2, 1), col(0, k)
    print("Q7: k =", k, " area =", abs(np.linalg.det(np.hstack((B - A, C - A))))/2)

#Q16
print("Q16: n =", np.sqrt(25**2 - 24**2))

#Q17
a, b = col(3, 2, 0), col(2, -4, 5)
print("Q17: lambda =", -(a.T@b)[0, 0]/5)

#Q24(a)
a, b, c = col(2, -3, 1), col(0, 4, -2), col(3, 0, 2)
lam = -(a.T@c)[0, 0]/(b.T@c)[0, 0]
print("Q24a: lambda =", lam, " (a + lam b)^T c =", ((a + lam*b).T@c)[0, 0])
#Q24(b)
AB, AC = col(1, 2, -1), col(2, -3, 0)
cr = np.cross(AB.ravel(), AC.ravel())
print("Q24b: AB x AC =", cr, " area =", np.linalg.norm(cr)/2, " sqrt(62)/2 =", np.sqrt(62)/2)

#Q25
m1, m2 = col(3, 2, 6), col(1, 2, 2)
cs = (m1.T@m2)[0, 0]/(np.linalg.norm(m1)*np.linalg.norm(m2))
print("Q25: cos(theta) =", cs, " 19/21 =", 19/21, " theta =", np.degrees(np.arccos(cs)))

#Q30(a): A, B, C collinear  <=>  det[B-A, C-A] = 0
A, B = col(55, -2), col(5, 8)
a_ = 305
C = col(a_, -52)
print("Q30a: det[B-A, C-A] =", np.linalg.det(np.hstack((B - A, C - A))))
#Q30(b): random unit vectors
rng = np.random.default_rng(0)
worst = 0
for _ in range(100000):
    u, v, w = (lambda z: z/np.linalg.norm(z))(rng.normal(size=(3, 3)).T).T
    worst = max(worst, np.sum((u - v)**2) + np.sum((v - w)**2) + np.sum((w - u)**2))
print("Q30b: max of the sum over 1e5 samples =", worst, "(<= 9)")

#Q35(a): foot of the perpendicular
P0, m, Q = col(-3, 1, -4), col(5, 2, 3), col(0, 2, 3)
lam = (m.T@(Q - P0))[0, 0]/(m.T@m)[0, 0]
F = P0 + lam*m
print("Q35a: lambda =", lam, " F =", F.ravel(), " length =", np.linalg.norm(F - Q), " sqrt(21) =", np.sqrt(21))
#Q35(b): d = |(A2-A1)^T (m1 x m2)| / ||m1 x m2||
m1, m2, A1 = col(1, -1, 1), col(2, 1, 2), col(1, 2, 1)
n = np.cross(m1.ravel(), m2.ravel()).reshape(-1, 1)
for p in (2, -4):
    A2 = col(p, -1, -1)
    print("Q35b: p =", p, " d =", abs((A2 - A1).T@n)[0, 0]/np.linalg.norm(n), " 3/sqrt2 =", 3/np.sqrt(2))
