import numpy as np
import scipy as sp
import sympy 

def define_A_DF(nx:int, fo:float)->np.ndarray:

    """Defines a matrix ...
    
    Args: 
        nx (int): this number number of points
        fo (float): furiers number : F0 = alpha * (change in t)/ (change in x)**2
        
    Returns: 
        A_DF (np.ndarray): matrix of ...
        
    """
    matrix_size = nx -2

    # A_DF = np.eye(matrix_size) * (-2)
    # A_DF +=np.diag(np.ones(matrix_size-1), k=+1)
    # A_DF += np.diag(np.ones(matrix_size-1), k=-1)
    # A_DF *= fo

    A_DF = np.eye(matrix_size)* (-1/fo +2)
    A_DF += np.diag(np.ones(matrix_size-1), k=+1)
    A_DF += np.diag(np.ones(matrix_size-1), k=-1)
    A_DF *= fo   

    return A_DF

# fo = sympy.symbols('fo')
# print(define_A_DF(10,fo))

def define_B_DF(nx: int, lbc:float, rbc:float)->np.ndarray:
    """
    Defines matrix B

    Args: 
        nx (int)    : 
        lbc (flaot) : left boundary condition 
        rbc (flaot) : right boundary condition 

    Returns: 
        b_DF (np.ndarray): matrix of ...
    """
    matrix_size = nx - 2
    b = np.zeros(nx)
    b[0] += lbc
    b[-1] += rbc
    np.zeros()
