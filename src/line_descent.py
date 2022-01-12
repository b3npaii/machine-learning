from gradient_descent import multivariable_descent
"""
def rss(data, coefficients):
    distance = 0
    for point in data:
        for i in range(0, len(data[0])):
            distance += (coefficients[i] - point[i]) ** 2
    return distance
    
def descend(data, points, functions, learning_rate=0.01):
    distance = rss(data, points)
    i = 0
    while distance > 1:
        for i in range(0, len(functions)):
            points[i] = points[i] - learning_rate * functions[i](points)
            
        for function in functions:
            points[functions.index(function)] = points[functions.index[function]] - learning_rate * function(points)
            
        distance = rss(data, points)
        if i % 100 == 0:
            print(i)
            #print(points)
            print(distance)
        i += 1
    return points


def a(inputs):
    return 4 * (2 * inputs[0] + inputs[1] - 3) + 6 * (3* inputs[0] + inputs[1] - 5)

def b(inputs):
    return 2 * (inputs[1] - 1) + 2 * (2 * inputs[0] + inputs[1] - 3) + 2 * (3 * inputs[0] + inputs[1] - 5)

print(descend([[0, 1], [2, 3], [3, 5]], [1, 0], [a, b]))
"""

def RSS(a, b, a_function, b_function, learning_rate = 0.01, num_iterations = 1000):
    for i in range(0, num_iterations):
        a = a - (learning_rate * a_function(a, b))
        b = b - (learning_rate * b_function(a, b))
    return(a, b)

def RSS_three(a, b, c, a_function, b_function, c_function, learning_rate = 0.01, num_iterations = 1000):
    for i in range(0, num_iterations):
        a = a - (learning_rate * a_function(a, b, c))
        b = b - (learning_rate * b_function(a, b, c))
        c = c - (learning_rate * c_function(a, b, c))
    return(a, b, c)