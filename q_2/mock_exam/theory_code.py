import numpy as np
import matplotlib.pyplot as plt

# question 16:
x1 = np.linspace(0,100,10000)
x2 = np.linspace(0,100,10000)
hess = [
    [-2*np.exp(-(x1+x2))-x1*np.exp(-(x1+x2)), np.exp(-(x1+x2))+ x1*np.exp(-(x1+x2))],
    [np.exp(-(x1+x2)) + x1*np.exp(-(x1+x2)),x1*np.exp(-(x1+x2))]
]

# eig = np.linalg.eig(hess)

fun = x1*np.exp(-(x1+x2))

plt.plot(x1,fun)
plt.show()