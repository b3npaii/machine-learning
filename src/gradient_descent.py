def minimize(function, x0, learning_rate=0.001, num_iterations=1000):
    while num_iterations > 0:
        fprimex = function(x0)
        x_new = x0 - learning_rate * fprimex
        x0 = x_new
        num_iterations -= 1
    return x0
