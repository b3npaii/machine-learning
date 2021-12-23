import math
import sys

sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from gradient_descent import minimize
from gradient_descent import multivariable_descent

def fprime_test_1(x):
    return 2 * x


def fprime_test_2(x):
    return 2 * x + 9 * (x ** 2) + 4 * (x ** 3) + 3


assert math.isclose(minimize(fprime_test_1, -12, 0.91, 100000), 0, abs_tol=1e-09)
assert math.isclose(minimize(fprime_test_2, 10, 0.001, 100000), -2.17851, rel_tol=1e-5)

def fprimex(x):
    return 2 * x

def fprimey(y):
    return 2 * (y - 2)

def fprimez(z):
    return 3 * (z - 3)

def fprimex2(x):
    return 2 * (x - 1)

def fprimey2(y):
    return 2 * (y - 1)

def fprimez2(z):
    return 3 * (z - 1)

assert multivariable_descent([fprimex, fprimey, fprimez], [1, 1, 1]) == [0.13506452244668363, 1.864935477553314, 2.900873834353689]
assert multivariable_descent([fprimex2, fprimey2, fprimez2], [1, 1, 1]) == [1.0, 1.0, 1.0]
