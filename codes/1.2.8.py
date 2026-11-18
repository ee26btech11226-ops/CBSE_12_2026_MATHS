import numpy as np

f = lambda x: np.arccos((np.sin(x) + np.cos(x))/np.sqrt(2))

for h in [1e-1, 1e-2, 1e-3]:
    for x in [-0.5, 0.0, 0.5]:
        D = (f(x + h) - f(x - h))/(2*h)
        print(f"h={h:<6} x={x:5.1f}  f(x+h)={f(x+h):.4f}  f(x-h)={f(x-h):.4f}  D_h={D:.6f}")
