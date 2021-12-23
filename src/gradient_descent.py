def minimize(function, x0, learning_rate=0.001, num_iterations=1000):
    while num_iterations > 0:
        fprimex = function(x0)
        x_new = x0 - learning_rate * fprimex
        x0 = x_new
        num_iterations -= 1
    return x0

def multivariable_descent(functions, initial_points, learning_rate=0.001, num_iterations=1000):
    for i in range(0, num_iterations):
        for i in range(0, len(functions)):
            prime = functions[i](initial_points[i])
            initial_points[i] = initial_points[i] - learning_rate * prime
    return initial_points
