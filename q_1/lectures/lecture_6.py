import numpy as np
import matplotlib.pyplot as plt

"""
Lecture topic: Boundary value problems
    - categorize boundary conditions for boudary value problems (BVP)
    - impolement the finite diff method for BVPs from scratch 
    - discuss the principles and application of BVPs 

heat is a basic example of boundary value problems (this is something that you are very likely to get on exam)
    -> when you heat a plate you have diff values on either end

Assume d^2y/dx^2 = f(x)

- dirichlet boundary condition: 
    - specifies the value of the function 
    - y = g
    exampel: constant velocity due to friction at wall 
        dc/dr (at r=0) = 0

Neumann boundary condition: 
    - specifies the value of the derivative 
    - dy/dx = g
    example: diffusion at catalyst pellet center is zero due to symmetry 


Mixed boundary condition: 
    - robin boundary condition: 
        -specifes the combination of function and derivative value 
        - ay +b*(dy/dx) = g

    -cauchy boundary condition: 
        - specifies the value of the function and the derivative at different sections of the boundary 
        - y= g * (gradien) * dy/dx = p 

        
Periodic boundary condition: 
A periodic boundary condition states that the solution or its derivatives at two distinct points x=x0 and x = x1 are equal
ie: 
y(x0) = y(x1) or dy/dx(at x0) = dy/dx(at x1)
In practice, these two periodic boundary conditions often occur together



For integration methods: 
in general the only one ever used in central difference method. But you should know all.



The finite difference approach: 
equation: 
(d^2y/dx^2) + alpha *dy/dx + betta*y = f(x)

discretization: h = x[1] - x[0]

finite diff: 
dy/dx[i] = (y[i+1] - y[i-1])/(2*h)
d2y/dx2[i] = (y[i+1] - 2*y[i] + y[i-1])/h**2    for 1<=i<=n-2

imp notice that number of points used in the for loop must be n-2
--> for i in range(0,n-1): (since last point not counted)


finite (central) difference eq applied to the ex eq: 

(y[i+1] - 2*y[i] + y[i-1])/h**2 + alpha* (y[i+1] - y[i-1])/(2*h) + betta*y[i] = f(x[i]) for i<=i<=n-2


rearrange: 
y[i-1] * (1-alpha*(h/2)) + y[i]*(h**2 * alpha-2) + y[i+1]*(1+alpha*(h/2)) = h**2 * f(x[i])

if you write this in an array: look slide (lecture 6 p 25)

there are 2 methods for setting the boundary values: 
option 1 (not preffered/ dont use it): manually set these values in the matrix
    - slow and introduces error 

option 2 (preffered/ should use this method):
    move the knows from the matrix to the solution side
    this will leave the vector with only unknowns
    same amount of equations as we have unknows -> solving for less eqs makes method faster and more accurate 



"""

#coding for finite diff: 
#define the remaining variables from the git hub code for this lecture
#this is a more prefered method as the other one is more computationally intense + being more intuative 

# M = len(y)-2 
# A = -2*np.eye(M)
# A +=np.diag(np.ones(M-1),k=-1)
# A += np.diag(np.ones(M-1),k+1)
# print(A)


"""
Discretization with Neumann boundary condition: 

Consider a rod of length. and themral conductivity k. Suppose the rod has a constant volumetric heat source Q. The temperature distribution in the rod is governed by the steady-state heat equation: 
-k*(d2T/dx2) = Q

Backward-difference is only first order accurate
    to combat this you can include a 'ghost point'

Ghost Point
    - extend the grid by adding a shot point
    - then we can use the central diff scheme to achieve second order accuracy. 
    - notice on the slide (39) inside of the matrix there is a new equation at N-1 

Advection-diffusion equation: discretization: 

peclet number: Pe= (u*deltax)/D 
if Pe<<1: diffusionis the dominating phenomena
if Pe>>1: convection is the dominating phenonmena 

general rule: if Pe > 2: use upwind/downwind method
if Pe<2 you can use cental diff method
l

"""