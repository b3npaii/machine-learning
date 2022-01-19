import sys
sys.path.append('src')
from euler import euler_method

def derivative(points):
    return points[0] + 1

a = euler_method(derivative)
print(a.calc_derivative_at_point([1, 4]))
a.calc_estimated_points([1, 4], 0.5, 4)