import numpy as np
import matplotlib.pyplot as plt

N,H,T = 2,3,20

dh = np.ones((N,H))
np.random.seed(3)
# Wh = np.random.randn(H,H)
Wh = np.random.randn(H,H) * 0.5

norm_list = []
for t in range(T):
    dh = np.dot(dh,Wh.T)
    norm = np.sqrt(np.sum(dh**2)) / N
    norm_list.append(norm)

plt.plot(norm_list)
plt.show()
