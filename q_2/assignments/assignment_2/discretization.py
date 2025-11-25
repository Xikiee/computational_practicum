import numpy as np
import scipy as sp


def define_A_DF(nx:int, fo:float)->np.ndarray:

    """Defines a matrix ...
    
    Args: 
        nx (int): this number number of points
        fo (float): furiers number : F0 = alpha * (change in t)/ (change in x)**2
        
    Returns: 
        A_DF (np.ndarray): matrix of ...
        
    """
    x = np.linspace(0,np.pi*3)
    matrix_size = nx -2

    A_DF = np.eye(matrix_size) * (-2)
    A_DF +=np.diag(np.ones(matrix_size-1), k=+1)
    A_DF += np.diag(np.ones(matrix_size-1), k=-1)
    A_DF *= fo

    
    return A_DF


print(define_A_DF(10,1))

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

    np.zeros()

