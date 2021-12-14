import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))

from gradient_descent import minimize

def fprime(x):
    return 2 * x

def fprime2(x):
    return (2 * x) - 2

assert minimize(fprime, 4, 0.001, 1000000) < 0.01
print(minimize(fprime2, 3, 0.001, 10000))
assert minimize(fprime2, 2, 0.001, 10000) < -0.9