import sys
sys.path.append('src')
from euler import euler_method
from euler import generalEuler
"""
def derivative(points):
    return points[0] + 1

a = euler_method(derivative)
print(a.calc_derivative_at_point([1, 4]))
#a.calc_estimated_points([1, 4], 0.5, 4)

def derv(points):
    return 4 * points[0] * points[1]

b = euler_method(derv)
b.calc_estimated_points([1, 2], 0.5, 9 )
"""

def x_(t, state):
    return state['x'] + 1

def y_(t, state):
    return state['x'] + state['y']

def z_(t, state):
    return 2 * state['y'] + 3 * t

derivatives = {"x": x_, "y": y_, "z": z_}

initial_state = {"x": -0.45, "y": -0.05, 'z': 0}
initial_point = (-0.4, initial_state)


c = generalEuler(derivatives)
print(c.calc_estimated_points(initial_point, step_size = 2, num_steps = 3))
