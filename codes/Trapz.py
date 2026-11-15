import numpy as np

# integrand f(x) = 1/sqrt(1+cos 2x) = 1/(sqrt(2) cos x) for cos x > 0
f = lambda x: 1/np.sqrt(1 + np.cos(2*x))

# candidate antiderivatives (options A-D), each chosen with F(0) = 0 where defined
opts = {
    "A": lambda x: np.log(np.cos(x)),
    "B": lambda x: np.log(1/np.cos(x) + np.tan(x))/np.sqrt(2),
    "C": lambda x: np.log(1/np.cos(x) - np.tan(x))/np.sqrt(2),
}

h = 0.01
x = np.arange(0, 1 + h/2, h)

# cumulative trapezoidal rule: F[n+1] = F[n] + (h/2)(f[n] + f[n+1])
F = np.zeros_like(x)
for n in range(len(x) - 1):
    F[n+1] = F[n] + (h/2)*(f(x[n]) + f(x[n+1]))

print(" x    trapz    B(x)     A(x)     C(x)")
for xv in [0.2, 0.5, 0.8, 1.0]:
    i = int(round(xv/h))
    print(f"{xv:.1f} {F[i]:8.5f} {opts['B'](xv):8.5f} {opts['A'](xv):8.5f} {opts['C'](xv):8.5f}")
print("max |trapz - B| =", np.max(np.abs(F - opts['B'](x))))
