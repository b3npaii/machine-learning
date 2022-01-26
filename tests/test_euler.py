import sys
sys.path.append('src')
from euler import euler_method

def derivative(points):
    return points[0] + 1

a = euler_method(derivative)
print(a.calc_derivative_at_point([1, 4]))
#a.calc_estimated_points([1, 4], 0.5, 4)

def derv(points):
    return 4 * points[0] * points[1]

b = euler_method(derv)
b.calc_estimated_points([1, 2], 0.5, 9 )