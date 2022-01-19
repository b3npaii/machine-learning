from gradient_descent import multivariable_descent
import math

def rss(data, coefficients):
    distance = 0
    for i in range(0, len(data)):
        distance += ((coefficients[i] ** 2) - (data[i] ** 2))
    return distance
"""
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
    points = [a, b, c]
    for i in range(0, num_iterations):
        a = a - (learning_rate * a_function(a, b, c))
        b = b - (learning_rate * b_function(a, b, c))
        c = c - (learning_rate * c_function(a, b, c))
    return(a, b, c)

def bonus(a, b, c, a_function, b_function, c_function, learning_rate = 0.01, num_iterations = 1000):
    points = [a, b, c]
    for i in range(0, num_iterations):
        a = a - (learning_rate * a_function(a, b, c))
        b = b - (learning_rate * b_function(a, b, c))
        c = c - (learning_rate * c_function(a, b, c))
        array = [a, b, c]
        accuracy = 0
        for j in range(0, len(array)):
            array[j] = round(array[j], 4)
        for j in range(0, len(points)):
            if round(points[j], 4) == array[j]:
                accuracy += 1
        if accuracy == len(points):
            return i
        else:
            accuracy = 0
        points = array
    print(a, b, c)

def a_one_grad_pb(a,b,c): 
    return ((196 * a) + (72 * b) + (28 * c) -26)

def b_one_grad_pb(a,b,c): 
    return ((72 * a) + (28 * b) + (12 * c) - 10)

def c_one_grad_pb(a,b,c): 
    return ((28 * a) + (12 * b) + (8 * c) - 8)

parobola_3 = bonus(1,0,0,a_one_grad_pb, b_one_grad_pb, c_one_grad_pb, learning_rate=0.013303, num_iterations = 1000000)
print(parobola_3)

def general_rss(coefficients, functions, step = 0.001,iteration = 10):
    copyfficients = list(coefficients)
    coefficients_the_second = coefficients
    for i in range(iteration):
        data_points = coefficients_the_second
        for item in functions:
            coefficients_the_second[functions.index(item)] = coefficients_the_second[functions.index(item)] - step * item(coefficients)
    return coefficients

def RSS_rounded(a, b, a_function, b_function, learning_rate = 0.01, num_iterations = 1000):
    for i in range(0, num_iterations):
        a = a - (learning_rate * a_function(a, b))
        b = b - (learning_rate * b_function(a, b))
        a = round(a, 15)
        b = round(b, 15)
    return(a, b)