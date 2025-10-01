import numpy as np


""""
Composite trapezoid Method: 

- you can extend the theory and consider a linear interpolation of each grid interval 

Task compute I = (integration) f(x) dx

    - number of grid points, N 
    - Number of intervals, N-1 (inveral width h= (b-a)/(N-1))
    - both conrners of the intervals: (closed method)


The error of the trapezoid method: 
    - the error can be considering the 4th order Taylor approximaiton of the function 
    - the numericla error committed by using the trapezoid method is the same order as the midpoint method (~h**2)

    Error <= max|(second derivative)|(b-a) h^2/12


Simposon's 1/3 rule 
    - better approximation is a quadratic interpolation 
    - the integral of the funciton can be approximated by the integral of the interpolatn 
        - 3 grid points: extremes and halfway point
        - over 2 intervals (interval width h = (b-a)/2)
    -considering the function evaluation in three points 
        I = h/3 * (func(a) + 4f((a+b)/2) + func(b))

    - name "1/3 rule" comes from the normalizaiton coefficient in the formula 




"""