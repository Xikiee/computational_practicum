import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

"""
Newton-Raphson:
    - converges very fast
    - converges very nicely 
    - works slightly better the bisection method, however this does depend on the situation 

Vector operations: 

dot product: 
    numpy.dot(u,v). # where u and v are the two vectors 
    numpy.vdot(u,v) # this should do the same thing 

cross product:
    numpy.cross(u,v)

"""
# v1 = np.array[1,2,3]
# u1 = np.array[4,5,6]

# np.dot(v1,u1)
# np.cross(v1,u1)

"""
matrix multiplication: the product of matrix  AxB = C, use np.matmul(A,B)

Find the determinant of matrix:
use np.linalg.det(A)

to find the eigenvalues and eigenvector 
    use lambda, v = np.linalg.eig(A)


Definite matricis: 

    M is positive-definite: all eigenvalues of M are> 0
    M is positive-semidefinite: all eigenvalues of `m are >=0
    M is negative-definite: all eigenvalues of M are <0
    M is negative-semidefinite: all eigenvalues of m are <=0


Matrix rank: the rank of a matrix is equal to the minimum number of linearly independent rows or columns 
    you can do this using: 
"""



matrix_a = np.array(([1,2,3], [1,2,3]))
# print(matrix_a)
np.linalg.matrix_rank(matrix_a)

"""
Distillation column exmample

"""
matrix_column = np.array(([0.9,0.3,0.1], [0.1,0.5,0.2], [0,0.2,0.7]))
# print(matrix_column)
product  = (30,25,10)
"""
you are interested in finding the x vector in matrix_column*x = product 
you can do this in the following way:
 ax = b
 a**-1 Ax = A**-1 b
 x = A**-1 b

However the matrix must meet some conditions:
    - have full rank 
    - unique solution 
    - the determinant of A is nonzero
    - homogeneous system Ax = 0 

to invert use
 """
a_invert = np.linalg.inv(matrix_a)

c = np.dot(a_invert,product)

"""
For bigger matrixes, the inversion will take very long. (10 times biggger matrix = 100 times slower)



We preffer itterative methods (such as Jacobi method) over methods like gausian 

Jacobi method: 
remember matrix as for distillation culumn 

    sum of a in row and culumn times c in row = product in row 

    you rewrite this equation to solve for c in stead of roduct 

    you make an initial guess for all c values. from where you will solve the equations 

Convergnece of the Jacobi method: 
    - the Jacobi method is especially suitable for strictly row diagnoal-dominant matricies 



Another indirect solution method: Gauss-Seidel method 

    you use the updated values from with m(k+1) (this is for the ones which you have already calculated) for the terms which you have not yet calculated you use m(k)



Netwon-Raphson for multiple equttions 
    couple the equatios and make both of the function equal to zero 

    the taylor series can then be writen as a matrix where you have: 
    (derivatives)*(deviation) = (function)

    we know the derivatives and the function values, we are interested by how much x deviates by 
    to solve this, one can use jacobian matrix 
    in this case the matrix of derivatives is your jacobian matrix 

    
"""

