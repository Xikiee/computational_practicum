# Lecture 4: Numerical Optimization - Introduction 

#### Definition of Mathematical Optimization 
Mathematical optimization or mathematical programming is the selection of a **best element**, with regaard to some **criteria**, from some set of **available alternatives**.

#### Objective function 

- Objective funciton quantifies the performace of different decisions 
- It is possible to specify multiple objective functions -> "Multi-objective optimization"
- You can only **Minimize** a function: min f(x) = max - f(x)

**Key Take Away** : We formulate everything as a **minimization** problem

### Variables and Degrees of Freedom
- If no constraints exist, the number of variables corresponds to the **degree of freedom** (DOF)
- **x** is a set of *N* continuous variables that can have any vlaue within a given copact domain (bounds) $x^L, x^U$ 

Examples of some varialbes:
**Process design**
- size of heat exchanger
- number of stages
- volume of reactor

**Process operation**
- operating pressure 
- valve opening

**Experiments**
- flowrate of pumps
- temperature of reacotr

### Conditions for optimality

#### Local vs Global Minimum

Local minimum: 
    If and only if $f(x^*)<=f(x)$ for all x in neighborhood of $x^*$, then $x^*$ is a **local minimum**.

Global minimum:
    If and only if $f(x^*)<= f(x)$ **for all** x in $[x^L, x^U]$, then $x^*$ is a **global minimum**.

#### Weak vs Strict (strong) minima

Strict:
    $f(x^*)<f(x)$ for all x in neighbourhood of $x^*$, then $x^*$ is a **strict local minimum**

Weak: 
    $f(x^*)<=f(x)$ for all x in neighbourhood of $x^*$, then $x^*$ is a **weak local minimum**

#### Critical point (Stationary points)

For a Lipshitz continuous and twice-differentiable function, a critical point $x^*$ is defined as:
    $$f'(x^*) = 0$$ 

This critical point can be:
- Minimum 
- Maximum 
- Inflection point

The condition $f'(x^*) = 0$ **is a necessary condition for (local) optimality**
-> if there is no minimum it is not possible to achieve an optimum value.

Finding the Lipshits constant (L):
    $$|f(x_1) - f(x_2)| <= L|x_1-x_2|$$


#### Convexity of a function 
A fucntion is (strictly)convex over a domain $[x^L, x^U]$, if and only if for any two points $x_1$ and $x_2$:

**Convex:**
$$f(\alpha x_1 + (1-\alpha)x_2)<= \alpha f(x_1) + (1-\alpha)f(x_2)$$

**Strictly Convex**:
$$f(\alpha x_1 + (1- \alpha) x_2) < \alpha f(x_1) + (1 - \alpha) f(x_2)$$

#### Importanct of convexity for optimization 
Helps determine whether a funciton will have a local minima or not (+ detemrine global minimum)
- Convex = **weak** global minimum
- **Strictly** convex = **strong** global minimum
- Not convex -> no minimum

#### Testing for convexity in multivariate functions
- f(x) is convex if its Hessian matrix **H(x)** is positive semi-definite
- f(x) is **strictly** convex if its Hessian matrix **H(x)** is positive definite

Positive semi-definite matrix: All of its eigenvalues are non-negative (convex)
Positve definite matrix: All of its eigenvalues are positive (so its strictly convex)

#### Sufficient condition for optimality 

