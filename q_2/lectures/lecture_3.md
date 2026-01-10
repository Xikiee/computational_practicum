# Elliptic PDE

## Boundary conditions at the corners

### Introduction to Elliptic PDE

Elliptic PDEs are time indipended. They describe systems which have already reached the steady state and thus are time-indepenent. 
The two independent variables are 2 spatial coordinates 

An example:

$$
\frac{\delta^2u}{\delta x^2} + \frac{\delta^2u}{\delta y^2} = 0 
$${#eq:laplace}

The **Laplace Equation** describes the spatial evolution of a quantity u in 2D through diffusion

#### Boundary Conditions for elliptic PDEs
A second order spatial derivate (like @eq:laplace) requires 4 boundary conditions 

### Case study for elliptic PDEs

$$
\frac{\delta^2T}{\delta x^2} + \frac{\delta^2T}{\delta y^2} = 0
$$

The following conditions are true:
- The temperature on the edges is fixed and known
- The system reached the steady stat $$\frac{\delta T}{\delta t} = 0$$
- How does the temperature field T(x,y) is distributed across the 2D spatial domanin?

#### Handling Boundary conditions

Ideal case is continues boundary conditions. This means that the conrners match up 

$$
T^{(1)} (y=0) = T^{(3)} (x=0)
$$

However it can happen that you have a discontinuous case. Then you use one of the following approaches: 
- Dominance of one BC
- Averaging  (**only applicable to Dirichlet BC**)

