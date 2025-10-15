import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp


"""
Lecture 7:
Continuation of boundary value problems, however now they are going to be solved with solve_ivp and solve_bvp. These methods use the shooting method.

In the case that we have:
Ay=c(y) : this is a non-linear problem 
y = A**-1 * c(y)
use a root finding method to solve for y

Objectives for this method:
you should be able to program the shooting method (solve_ivp) and should be able to impliment it 

What does the shooting method do:
Example:
ODE: d2y/dx2 = 4(y-x)

boundary condition: (dirichler, one is homogeneous, the other one is not)
y(0) = 0
y(1) = 2

If this was an initial boundary problem (not a boundary value problem) you would want to convert the second order derivative into a first order derivative 
therefore: dy1/dx = y2 and dy2/dx = 4(y1-x)
and then you would want to find the inital conditions: y1(0) = 0 and y2(0) = ?
What the shooting method does, it guesses for what the value should be 

lets say y2(0)= 1 (this is an initial guess)

2. solve the ODE system with IVP methods from lecture 5 (ex forward Euler)
3. Evaluate the solution and update the guess y for y2(0)

dy1/dx = y2     dy2/dx = 4(y1-x)   y1(0)=0

first guess y0: y2(0)=y0 = 1 (y here is gamma)
second guess y1: y2(0) = y1= 0
third guess y2: y2(0) = y2 = 1.55 (this is a correct guess)

Updating the guess with Linear Interpolation: 
The relation between the right hand side and gamma is linear, that is why this works
The ODE should be linear for you to get the right guess right away, if the system is non-linear you will not get the right ans

If you have a non-linear problem, you use a root finding method (similarly to Ay=c(y) were you also have to do root finding)

to solve this, it is the same thing as I did for assignment_6
residual function: 
in this case: 
residual: phi(gamma[i+1]) = y_1

if you dont know how the function look, how do you get a derivative: use the secant method
use a finite 

The scheme for coding shooting method residual function: 
Start: 
    -system of 1st order ODEs dy/dx=f(x,y)
    - initial guesses gamma_0, gamma_1
    - sovle IVP with gamma_0,gamma_1 -> y1(x[N-1];gamma_0)y1(x[N-1],gamma_1)
    Check:
    - phi = y1(x[N-1];gammai) -y1(x[N-1])< tolerance 

.... (there is more here, didnt get time to copy )


Shooting method for M equation: (this is just the exact same thing as assignemnt 6 question 2)
dyi/dx = fi(x,y1,y2,...ym)
improve the guesses gamma...

The multiple shooting method:
    -advanced shooting method
    - breaks domain into sub-domains and solves IVP in each sub-domain (you use this if you know values at differnt point)
    - Add continuity and boundary conditions for each sub-domain
    - Advantages:
        - improved stabiltiy 
        - Paralllelization
        - more flexibility for initial guesses

        
Solve BVP:
"""

def dy(x:np.ndarray,y:np.ndarray)->np.ndarray:
    """First order ODEs from d2y/dx2=4(y-x)
    Args:
        x (np.ndarray): Grid points.
        y (np.ndarray): function values.
    Returns: np.ndarray: Right hand-side of ODEs
    """
    dydx = np.zeros(y.shape)
    dydx[0] = y[1]
    dydx[1] = 4*(y[0]-x )
    return dydx

def my_bc(ya:np.ndarray,yb:np.ndarray)->np.ndarray:
    """Residuals of the boundary conditions.
    args:
        ya (np.ndarray): function values at x0
        yb (np.ndarray): function vlaues at x(N-1)
    Returns: 
        np.ndarray : residuals fo boundary condition 
    """
    return np.array([ya[0],yb[0]-2])


x = np.linspace(0,1,101) #x grid points
y_guess = np.zeros((2,len(x)))
bvp_results = sp.integrate.solve_bvp(dy,my_bc,x,y_guess)



`