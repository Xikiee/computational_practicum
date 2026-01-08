import numpy as np
import scipy as sc

def define_A_DF(nx: int, fo:float)->np.ndarray:

    """
    The A matrix after applying forward euler, and discritizing the temporal and spacial terms. 
    
    """

    matrix_size = nx - 2
    A = np.eye(matrix_size) * (1/fo - 2) 
    A += np.diag(np.ones(matrix_size-1), k= +1)
    A += np.diag(np.ones(matrix_size-1), k=-1)


    return A



def define_B_DF(nx: int, lbc: float, rbc: float) -> np.ndarray:
    """
    Returns the b vector which is a result of applying the boundary conditions to the discretization. 

    Args: 
        nx      (int)   : number of x points 
        lbc     (float) : left hand boundary conditions, this is T(0, t) = 0
        rbc     (float) : right hand boundary conditions, this is T(L, t) = 0
    
    Returns: 
        b       (np.ndarray): the solution vector b which consists of all known values of temperature at different positions and times 
    """
    matrix_size = nx -2
    b = np.zeros(matrix_size)
    b[0] = lbc
    b[-1] = rbc
    return b



##### backward (implicit) Euler method 

def define_A_DB(nx: int, fo:float)->np.ndarray:
    """
    This function defines the A matrix for implicit Euler method. After the temporal and spacial terms are discretized, the equation follows the following form:

        (I - FoA)T^{k+1} = T^k + Fob 

    Args: 
        nx          (int)   : number of x steps 
        fo          (float) : the fouriers number defined by : alpha * dt/dx**2

    Returns:
        A_DB    (np.ndarray): the coefficient matrix for the T^{k+1} term
    """
    
    matrix_size = nx -2

    A = np.eye(matrix_size) * (1/fo - 2)
    A += np.diag(np.ones(matrix_size-1), k = +1) 
    A -= np.diag(np.ones(matrix_size-1), k = -1)


    return A

def define_B_DB(b_DF: np.ndarray, yk: np.ndarray, fo: float)-> np.ndarray:
    """
    This fuction computes the B matrix for the implicit euler method. 

    In this case the b vector is a summation of two vectors, the current values and the boundary condition vector: 
        b = T^k + b


    This is because you want to use np.linalg.solve to compute the next value (T^{k+1}) which takes two arguments A and b

    Args: 
        b_DF            (np.ndarray): the implicit b vector computed from the boundary condition
        yk              (np.ndarray): the last computed terms which serve as the new boundary for the next calculation 
                                    

        fo                   (float): the fouriers number

    Returns:
        b               (np.ndarray):
    """

    B  = yk.copy()

    B[0] += -fo*b_DF[0]
    B[-1] += -fo*b_DF[-1]            # Notice that here it is += as you are adding the boundary value to the previous value, this follows from the equation written in the docstring 

    return B



##### Implementing Backward Euler with Spare Matrix Definition


def define_A_DB_sparse(nx: int, fo: float)->sc.sparse.csc_matrix:
    """
    This function computes the coefficient matrix for T^{k+1} in sparse matrix form

    Args:
        nx                    (int): number of x steps
        fo                  (float): fouries number
    Returns:
        A    (sc.sparse.csc_matrix): A coefficient matrix of sie (nx-2, nx-2)
    """
    matrix_size = nx - 2

    main_diag = np.ones(matrix_size)* (1 + 2*fo)
    off_diag = np.ones(matrix_size) * (-fo)

    diag = [off_diag,main_diag,off_diag]
    A = sc.sparse.spdiags(diag, [-1,0,1],matrix_size,matrix_size).toarray()
    return A

print(define_A_DB_sparse(10,1))