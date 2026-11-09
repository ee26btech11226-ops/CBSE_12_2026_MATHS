#Code by EE26BTECH11202
#CBSE 2026 Mathematics, Set 1 (65/5/1): Q32, matrix method
import numpy as np

#rows: apples, oranges, bananas; unknowns: price of one apple, orange, banana
A = np.array([[4, 3, 2],
              [2, 4, 6],
              [6, 2, 3]], dtype=float)
y = np.array([[60], [90], [70]], dtype=float)

detA = np.linalg.det(A)
adjA = detA*np.linalg.inv(A)          #adj A = |A| A^{-1}
x = adjA@y/detA                       #x = A^{-1} y

print("|A| =", round(detA))
print("adj A =\n", np.round(adjA))
print("[apple, orange, banana] =", np.round(x.ravel(), 6))
