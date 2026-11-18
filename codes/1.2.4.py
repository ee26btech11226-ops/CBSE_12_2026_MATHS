import numpy as np

# Define matrices A and B given in problem 1.2.4
A = np.array([[0, -3, 4], 
              [1,  0, 2]])

B = np.array([[-3, 0, 1], 
              [ 2, 4, 0]])

# Since A + B + C = O, compute C = -(A + B)
C = -(A + B)

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nCalculated Matrix C:")
print(C)
