The goal of this lecture is:
    1) formulate a linear and mixed-integer linear programming model from an engineering problem statement
    2) Explain at a high-level different algorithms used to solve linear and mixed-integer linear programming models
    3) analyzed optimal solution obtained on solving these models

# Numerical Optimization - Linear & Mized-Integer Linear Programming

#### Equality constriants, h(x,y) = 0
A set of vector of $n_h$ equality constraints -> typically defines the mathemcal model. 

For all optimization models, degrees of freedom must always be greater than zero
    $$DOF = n + k - n_h$$
where:
- k = number of x variables 
- $n_h$ = number of equality equation (number of equations)

#### Inequlity constraints, g(x,y)<=0

**Feasible region** region where all constraints to the optimization problem are satisfied

#### Convexity of a set 

Convexity of a funciton is different from the convexity for a set. 

For every x1 x2 in the domain, a linear function conneting the two points must stay in the domain. 

**Sufficient condition for convexity**: If equality constraints h(x) are linear and g(x) are convex function then omega is convex -> limited case

## Linear Programming 
### Fundamentals

Feasible region is always a **polyhedron**.
Definition: The possible reagion where optimization fits all the conditions.

Because the conditions for an LP are that the set must be convex.
**All LPs are convex optimization problems so All solutions are global minimums**

#### Where does aptimum lie
Since all LPs are convex: 
- Every local optimum for an LP is a global optimum
- If an LP has a non-constant objective function, then an optimal solution of an LP **cannot** lie in the interior of the feasible region. 
- If an LP has a unique optimal solution, then the optimal ( if optimal is largest value) **must** lie at an extreme point of the feasible region 
- If an LP has multiple optimal solutions then one of them **must** occur at an extreme point of the feasible region 

#### Simplex algorithm

- Only consider adjacent extreme points for improving direction 
- Move along the edge that yield largest rate of improvement 
- Move until another extreme point has been reached 
- Check if further improvement is possible: if 'yes" continue; else terminate 
- Can potentially struggle if there are a high number of extreme points
- Higher number of extreme points occur when there are many variables and constraints but few degrees of freedom

#### Interior point algorithm
- Determine an improving direction 
- Move along that direction, but the feasible point should strictly remain in the interior of the feasible region 
- Check of significant change has been made: if 'yes' continue; else terminate 
- Wroks well when degrees of freedom n is large 
- For smaller problems simplex algorithm may be more efficient

```python
import number as np
from scipy.optimize import linprog

# minimize: c^T x
c = [-1, -1]                            # Coefficients for the objective function

A = [[1, -1], [1, 0], [0, 1]]           # Coefficients for inequality constraints
b = [0, 2, 3]                           # Bounds for inequality constraints

x_bounds = [(0, None), (0, None)]       # Variable bounds

# solve the LP
result = linprog(
    c,
    A_ub=A,
    b_ub=b,
    bounds=x_bounds,
    method="highs"
)
```



### Anlyzing the output of linprog

fun: reports value of objective funciton 
x: vector of optimized input variables 
nit: number of iterations
lower: lower bounds
upper: upper bounds
residual: difference between the value at the optimal solution and the respective bound
marginal: dual cost or shadow price
equality constraints always have a zero residual
Inequality constraints only have a zero residual if the constrain is active

## Mixed-Integer Linear Programming (MILP)

The feasible region is discontiuous -> non-convex
**MILPs are inherently non-convex**

#### Discrete variables 
- **Binary variables**: Can only take values 0 or 1
- **Integer vaiables**: Can take any integer value





