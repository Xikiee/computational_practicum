import numpy as np
import matplotlib.pyplot as plt
import scipy 


"""
What is a pde: function with derivatives
How to recognize a pde: is the function of more than one variable? 
    yes: its a pde
    ex: f(x,y)

How to solve a pde: 
    - search for a function u: R**2 -> R that: 
        - satisfies the relationship prescribed by a given PDE on a specified domain 
        - meets the imposed initial and/ or boundary conditions 
        - in case of two independent variables, the solution is a bivariate function u and can be visualzed as a surface over the 2D domain (x,t) or (x,y)

        u_dot = du/dt (u with a . on top)

Classification: (when is it Parabolic vs Hyperbolic)

look at slide 14
example: 
u(x,y)
a_0(x,y)*du/dx + a_1(x,y)*du/dy + a_2*u = f(x,y)        -> so the function is linear since non of the terms are interdependant 

another example: 
x**2*du/dx + 1/(xy) + 5*u = 3*x*ln(y)           -> this is linear? idk how since you have x**2


example which is non-linear:
x*u*du/dx + dy...           -> this is non-linear because you have x*u*du/dx


Classification of bivariate second order PDEs: 
We define the descriminat as the quantity D=b**2 -4ac

D>0: Hyperbolic PDE  (hyperbolic is not going to be covered in this course)
D=0: Parabolic PDE 
D<0: Eliptic PDE

example:
du/dt = D*(d**2*u)/(d*x**2)
rewriting this: 
D*(d**2*u)/(d*x**2) + D*(d**2*u)/(dx*dt) + D*(d**2u)/(dt**2) + D*du/dx - D*du/dt + Du

D*(d**2u)/(dx**2) - du/dt = 0
There was some other stuff written here. 


Parabolic PDEs describe time-dependent, dissipative physical processes, like diffusion, which evolve toward a steady state. 



example: 
d**2u/dy**2 + alpha * d**2u/dx**2 = f(x,y)

second order in y: need 2BC in y direction 
second order in x: need 2 BC in x direction 

Chemical Engineering applications:
slide 27

example: 

dC/dt = D * (d**2C)/(dx**2) + u*(dC)/(dx)           the formula for this will be different 
this example is still parobolic

you can also add a reaction term and make it non-linear (add: r(C))



Temperature profile inside of a rod: 


"""