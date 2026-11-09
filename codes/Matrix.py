#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q1, Q2, Q4, Q5
import sympy as sp

#Q1: A^2 = I for A = [[-p, q],[r, p]]
p, q, r = sp.symbols('p q r')
A = sp.Matrix([[-p, q], [r, p]])
print("Q1: A^2 =", sp.simplify(A**2))              # (p^2 + qr) I
print("Q1: A^2 = I  <=>  1 - p^2 - qr = 0")

#Q2: A^2 = A  =>  (A - I)^3 - A = -I (checked on the idempotent A = [[1,0],[0,0]] and [[1,1],[0,0]])
I2 = sp.eye(2)
for A in (sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[1, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 1]])):
    assert A**2 == A
    print("Q2:", (A - I2)**3 - A)

#Q4: A + B + C = O
A = sp.Matrix([[0, -3, 4], [1, 0, 2]])
B = sp.Matrix([[-3, 0, 1], [2, 4, 0]])
print("Q4: C =", (-(A + B)).tolist())

#Q5: |adj A| = |A|^(n-1) != 0 for non-singular A
M = sp.Matrix([[2, 1, 0], [0, 3, 1], [1, 0, 1]])
print("Q5: |A| =", M.det(), " |adj A| =", M.adjugate().det())
