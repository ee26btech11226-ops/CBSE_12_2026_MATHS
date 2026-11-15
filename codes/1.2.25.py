import numpy as np
col = lambda *v: np.array(v, dtype=float).reshape(-1, 1)
m1, m2 = col(3, 2, 6), col(1, 2, 2)
cs = (m1.T@m2)[0, 0]/(np.linalg.norm(m1)*np.linalg.norm(m2))
print("Q25: cos(theta) =", cs, " 19/21 =", 19/21, " theta =", np.degrees(np.arccos(cs)))

