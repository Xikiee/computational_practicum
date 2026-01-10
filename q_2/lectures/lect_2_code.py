""" 
The following code is from lecture 3 on elliptical PDEs. The code is from the gitlab.

Soliving the 2D Steady-State Heat Equaiton suing Finite Differences


"""

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt


def solve_poisson(
        nx: int, lx: float, ly: float, f_boundary: callable, T_bound: float
)-> np.ndarray:
    """
    Solves the 2D steady-state heat equation (Poisson equation) on a rectangular domain using finite differences with equal step sizes in x and y.
    
    Params:
        ...
    Returns:
        u           (np.ndarray): 2D array of the solution u(x, y) including boundary points
    """

    # compute the number of grid points in y to ensure equal step size
    dx = lx/(nx-1)
    ny = int(ly/dx)+ 1

    # domain discretization 
    x = np.linspace(0,lx,nx)
    y = np.linspace(0,ly,ny)

    # number of unknows 
    N = (nx - 2)*(ny-2)         # you have -2 for both the x and y because these values you get from the boundary conditions. 

    # construct the laplacian operator using finite differences
    diagonal = -4
    off_diagonal_x = 1                  # x off-set as in left and right 
    off_diagonal_y = 1                  # y off-set as in lower and upper

    # Main diagonal
    main_diag = np.full(N, diagonal)

    # Off-diagonals:
    # create the off-diagonal entries of the Poisson matrix that represent the coupling between neighboring points in the discretized 2D domain
    off_diag_x_vals = np.full(N-1, off_diagonal_x)
    off_diag_y_vals = np.full(N-(nx-2), off_diagonal_y)                 # the size of this (N-(nx-1)) comes from the fact that these are the upper and lower terms which occure nx-2 away from the point. There for there needs to be N-(nx-2) terms

    # Adjust for boundary conditions:
    for j in range(1, ny-2):
        idx = j* (nx-2) -1
        off_diag_x_vals[idx]  = 0           # to insert the zeros interupting the upper and lower diagonals 
    
    diagonals = [
        main_diag, 
        off_diag_x_vals,
        off_diag_x_vals, 
        off_diag_y_vals, 
        off_diag_y_vals 
    ]

    offsets = [0,-1,1,-(nx-2), +(nx-2)]

    A = diags(diagonals, offsets, shape= (N,N), format="csr")           # csr is "Compressed Sparse Row" format, which is efficient for solving linear systems and matrix-vector products

    # Apply boundary conditions
    # Right-hand side vector 
    b = np.zeros(N)

    # Apply boundary conditions
    idx_bottom = np.arange(0,nx-2)
    idx_top = np.arange(N-(nx-2),N)

    # The +1 offset in the line below is needed because idx_bottom refers to indices in the interior points vector (which excludes boundaries), while x is the full grid (which includes boundaries). Interior point index 0 corresponds to x[1], index 1 to x[2], ..., up to index nx-3 corresponding to x[xn-2].
    b[idx_bottom] -= off_diagonal_y * f_boundary(x[idx_bottom +1], T_bound)
    b[idx_top] -= off_diagonal_y *T_bound

    # LHS and RHS boundaries
    idx_left = np.arange(0,N-(nx-2)+1, nx-2)
    idx_right = np.arange((nx-2)-1, N+1, nx-2)          # look into why this is structured the way it is, but i think it has to do which the general matrix size and what points this boundary condition is affecting
    b[idx_left] -= off_diagonal_x*T_bound
    b[idx_right] -= off_diagonal_x * T_bound

    # solve the linear system
    u_inner = spsolve(A,b)
    
    # Construct the matrix
    u = np.zeros((nx,ny))

    # insert the interior solution
    u[1:-1,1:-1] = u_inner.reshape((ny-2,nx-2)).T           # reshape the vector to match the actual field          

    # apply boundary conditions
    u[:,0] = f_boundary(x,T_bound)          # bottom (y=0)
    u[:,-1] = T_bound                       # top    (y=4)
    u[0,:] = T_bound                        # left   (x=0)
    y[-1,:] = T_bound                       # right  (x=2)

    return u