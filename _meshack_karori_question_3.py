import numpy as nmp
import scipy.integrate as integrate

# Define the function

def integrand(x):
    return nmp.exp(-(x ** 2) / 2)

# Find solution to the integrand

solution = integrate.quad(integrand, 0, nmp.inf)

# Show solution
print('\nSOLUTION\n')
print('\n===================================================\n')
print (solution)
print('\n===================================================\n')