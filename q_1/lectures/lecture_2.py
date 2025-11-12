import numpy as np
import matplotlib.pyplot as plt
import math

#ways to find the zero of a function 

# function types: 
# - univariate functions: they have scalar variables 
# - multivariate functions: multi-dimensional domain scalar output
# - vector-valued functions: scalar or multi-dimensional domain, but multi-dimensional output (ex. velocity profile)



#example for approximating the derivative: 
# def f(x): return x**2 + x

# x = np.linspace(-5,5,100)

# h=0.01

# cal_derivative = (f(x+h) - f(x))/(h)

# plt.plot(x, f(x), label = "function")
# plt.plot(x, cal_derivative)
# plt.show()




#hassian matrix is a matrix of the second derivative matrix
#jacobian matrix first derivative matrix


#example solving propane gas tank using van der Waals 

# (P + a(n/v)**2)*(V - nb) = nRT

def van_der_wall(P,a,b,V,n,b,R,T):
    return (P + a(n/V)**2)*(V - n*b) - n*R*T

