import numpy as np
import matplotlib.pyplot as plt

"""
Ordinary differential equations: 
reaction: A->B (first order: k)

ODE: d(Ca)/dt = -kCa

concentration of Cb = 1- Ca (where 1 is the total concentration)

initail condition: Ca(t=0)=1
analytical solution : Ca(t) = exp(-kt), Cb(t) = 1-exp(-kt)

to do this in python:
"""

t= np.linspace(0,30,100)
k = 0.2
def cA(t:float,k:float)->float:
    return np.exp(-k*t)

def cB(t:float,k:float)->float:
    return 1-np.exp(-k*t)

plt.plot(t,cA(t,k), label= 'cA')
plt.plot(t,cB(t,k), label = 'cB')
plt.legend()
# plt.show()

"""
Rewriting implicit equation as explicit eq:
...

An ODE is easiest to solve when its first order and autonomous 


scipy optimze, is a root finding algorithem, it will try to make the function equal to zero. 
instead of this you can use smth like newton-raphson or bisection method (look at Assignment_Q1_L3.ipynb)


"""