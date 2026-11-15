import numpy as np
import matplotlib.pyplot as plt



# Define vectors a, b, and c
a = np.array([2, -3, 1])
b = np.array([0, 4, -2])
c = np.array([3, 0, 2])

# We need (a + lambda * b) . c = 0
# a.c + lambda * (b.c) = 0 => lambda = - (a.c) / (b.c)
a_dot_c = np.dot(a, c)
b_dot_c = np.dot(b, c)

lambd = -a_dot_c / b_dot_c

print(f"a . c = {a_dot_c}")
print(f"b . c = {b_dot_c}")
print(f"Calculated lambda: {lambd}")

# Verify
result_vector = a + lambd * b
dot_check = np.dot(result_vector, c)
print(f"Result vector (a + lambda*b): {result_vector}")
print(f"Dot product with c (should be 0): {dot_check}")




# Given vectors from A to B and A to C
AB = np.array([1, 2, -1])
AC = np.array([2, -3, 0])

# Compute cross product AB x AC
cross_prod = np.cross(AB, AC)
area = 0.5 * np.linalg.norm(cross_prod)

print(f"AB x AC: {cross_prod}")
print(f"Area of triangle ABC: {area} sq. units (approx {np.sqrt(62)/2:.4f})")

# 3D Plotting of triangle ABC
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')

# Let A be at origin (0, 0, 0) for visualization
A = np.array([0, 0, 0])
B = A + AB
C = A + AC

# Coordinates for plotting
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]
z = [A[2], B[2], C[2], A[2]]

ax.plot(x, y, z, color='blue', linewidth=2, marker='o')
ax.plot_trisurf([A[0], B[0], C[0]], [A[1], B[1], C[1]], [A[2], B[2], C[2]], color='cyan', alpha=0.4)

ax.text(A[0], A[1], A[2], '  A(0,0,0)', fontweight='bold')
ax.text(B[0], B[1], B[2], '  B(1,2,-1)', fontweight='bold')
ax.text(C[0], C[1], C[2], '  C(2,-3,0)', fontweight='bold')

ax.set_title(r'3D Plot of $\triangle ABC$ (Area = $\frac{\sqrt{62}}{2}$)', fontsize=11)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.tight_layout()
plt.savefig('../figs/1.2.24.png', dpi=300)
plt.show()
