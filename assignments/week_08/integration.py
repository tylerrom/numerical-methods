import numpy as np
def trapezoidal_rule(f, a, b, N):
    ''' Approximate the integral of f from a to b using the trapezoidal rule with N slices.'''
    
    h = (b - a) / N  # step size
    x = np.linspace(a, b, N+1)  # N+1 points from a to b
    y = f(x)  # evaluate function at all points
    
    # Trapezoidal rule: (h/2) * [f(a) + 2*sum(f(x_i)) + f(b)]
    integral = (h/2) * (y[0] + 2*np.sum(y[1:-1]) + y[-1])
    
    return integral



def simpsons_rule(f, a, b, N):
    if N % 2 != 0:
        raise ValueError("N must be even for Simpson's rule")
    
    h = (b - a) / N  # step size
    x = np.linspace(a, b, N+1)  # N+1 points from a to b
    y = f(x)  # evaluate function at all points
    
    # Simpson's rule: (h/3) * [f(a) + 4*sum(odd indices) + 2*sum(even indices) + f(b)]
    integral = (h/3) * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[-1])
    
    return integral
