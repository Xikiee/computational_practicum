# Interpolation vs Regression

**Interpolation**
- The curve passes through all the data points
- Estimates values *between* known data points

**Regression (Approximation)**
- The curve does not have to pass through all the data points
- Fits a model to data to describe general trends and make predictions

---

## Interpolation

### Minimizing the residual sum-of-squares

$$
\text{RSS} = (y -Xw)^T(y-Xw) = y^Ty - y^TXw - (Xw)^Ty + (Xw)^TXW\\
= \dots
$$

Differentiating RSS(w) w.r.t **w** and setting the resulting equaiton equal to zero, we can derive the **Normal Equation**. This leads to:

$$
w = (X^TX)^{-1}X^Ty
$$

The model parameters **w** can be directly calculated unless **X^TX** is singular (non-invertible).

Options for solving the normal equation:

- **Option A**: Solve **w = (X^TX)^{-1}X^Ty** analytically (Direct method)
    - Inversion of **X^TX** necessary (using numpy.linalg.inv(**X^TX**)), or solve linear system of linear equations numpy.linalg.solve(**X^TX, X^Ty**)
- **Option B**: Interative approximation of the solution of the linear system of eqautions (Indirect method) using Jacobi method or Gauss Seidel:
$$
(X^TX)w = X^Ty
$$

- **Option C**: solve an optimization problem with the objective function L(w) using scipy.optimize.minimize(objective,x0=0)

## Regression

- **Regression**: Find a model that best fits the data without the constraint of passing through all data points necessarily
- Accounts for data variability and noise by finding a *best-fit* curve
- **Interpretation**: Can use physical model equations that are easier to interpret

**Types of Regression**
- **Linear regression**: Fit a straight line
- **Polynomial regression**: Fit higher-degree polynomials
- **Nonlinear regression**: Fit parameters of general nonlinear models (functions)

---

### Linear Regression: General Idea

**Residual Sum of Squares (RSS)**

$$
\text{RSS} = \sum_{i=1}^{n} e_i^2
           = \sum_{i=1}^{n} \left( y_i - w_0 - w_1 x_i \right)^2
$$

The task is to find $(w_0, w_1)$ such that the RSS is minimized.

---

### Polynomial Regression

Polynomial regression transforms the input variables (features) such that a polynomial is used to fit the data.  
We consider one-dimensional input.

$$
y_i = \sum_{j=0}^{M} w_j x_i^j
$$

Where:
- $M$ is the order of the polynomial
- $x_i^j$ denotes $x_i$ raised to the power of $j$
- The polynomial coefficients $w_0, \dots, w_M$ are represented by a parameter vector


