import numpy as np
from scipy.sparse import spdiags, csc_matrix
import scipy as sc
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

    # A_DF = (1/fo -2)*np.eye(matrix_size)
    # A_DF +=np.diag(np.ones(matrix_size-1), k=+1)
    # A_DF += np.diag(np.ones(matrix_size-1), k=-1)
    # A_DF *= fo
    A_DF = np.diag(np.full(matrix_size,1/fo-2))
    A_DF += np.diag(np.ones(matrix_size-1), k=+1)
    A_DF += np.diag(np.ones(matrix_size-1), k=-1)
 
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
    b = np.zeros(matrix_size)
    b[0] = lbc 
    b[-1] = rbc 
    return b



"""
Question 2: updating the file to inclue the backwards euler method
"""

def define_A_DB(nx:int, fo: float)->np.ndarray:
    """
    abt the function ...
    """
    matrix_size = nx -2
    # define the laplacian matrix L:            Look up what is a laplacian matrix 
    L = (-2*np.eye(matrix_size) + np.eye(matrix_size, k=1) + np.eye(matrix_size,k=-1))

    # A_DB = I - fo*L
    A_DB = np.eye(matrix_size) - fo*L
    return A_DB

def define_B_DB(b_DF:np.ndarray, yk:np.ndarray, fo:float)->np.ndarray:
    """
    Function which impliments the the Drichelet boundary conditions and previous time step values
    Args: 
        b_DF            (np.ndarray): vector which contains dirichlet boundaries
        yk              (np.ndarray): vector containing previous time step values 
        fo              (float)     : fouriers constant 
    
    Return: 
        B_DB            (np.ndarray): the solution vector 
    
    """
    B = yk.copy()

    B[0] += fo*b_DF[0]
    B[-1] += fo*b_DF[-1]
    B_DB = B
    return B_DB




######### making sparse matricies:

# def define_A_DB_sparse(nx:int, fo:float)->csc_matrix:
#     """
#     about the function:

#     """

#     matrix_size = nx -2
#     main_diag = np.ones(matrix_size) *(1/fo-2)
#     off_diag = np.ones(matrix_size)
#     data = np.vstack([off_diag,main_diag,off_diag])
#     diag = np.array([-1,0,1])

#     A_DB = spdiags(data,diag,matrix_size, matrix_size).toarray()
#     return A_DB

def define_A_DB_sparse(nx: int, fo: float) -> csc_matrix:
    m = nx - 2

    main_diag = (1 + 2*fo) * np.ones(m)
    off_diag  = (-fo) * np.ones(m-1)

    data = np.vstack([off_diag, main_diag, off_diag])
    diags = np.array([-1, 0, 1])

    A = spdiags(data, diags, m, m).tocsc()
    return A


fo =0.5
mat = define_A_DB_sparse(10,fo)
print(mat)