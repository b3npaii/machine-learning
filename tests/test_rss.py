import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from line_descent import RSS
from line_descent import RSS_three
from line_descent import general_rss
from line_descent import RSS_rounded
import math

# LINEAR 

def b_one_grad_lin(a, b):
    return ((10 * a) + (6 * b) - 18)

def a_one_grad_lin(a,b): 
    return ((26 * a) + (10 * b) - 42)

line_one = RSS(1, 0, a_one_grad_lin, b_one_grad_lin, learning_rate=0.01, num_iterations = 1000000)

assert round(line_one[0], 4) == 1.2857
assert round(line_one[1], 4) == 0.8571

#LINEAR 

def a_two_grad_lin(a, b):
    return (28 * a) + (12 * b) + 2

def b_two_grad_lin(a,b): 
    return (12 * a) + (8 * b) - 4

line_two = RSS(1, 0, a_two_grad_lin, b_two_grad_lin, learning_rate=0.01, num_iterations = 1000000)

assert round(line_two[0], 2) == -0.8
assert round(line_two[1], 2) == 1.7



def a_one_grad_pb(a,b,c): 
    return ((196 * a) + (72 * b) + (28 * c) -26)

def b_one_grad_pb(a,b,c): 
    return ((72 * a) + (28 * b) + (12 * c) - 10)

def c_one_grad_pb(a,b,c): 
    return ((28 * a) + (12 * b) + (8 * c) - 8)

parobola_1 = RSS_three(1,0,0,a_one_grad_pb, b_one_grad_pb, c_one_grad_pb, learning_rate=0.01, num_iterations = 1000000)
print(parobola_1)

assert round(parobola_1[0], 2) == 0.5
assert round(parobola_1[1], 2) == -1.7
assert round(parobola_1[2], 2) == 1.8

#PARABOLA
def a_two_grad_pb(a,b,c): 
    return ((196 * a) + (40 * b) + (28 * c) -62)

def b_two_grad_pb(a,b,c): 
    return ((40 * a) + (28 * b) + (1 * c) -1)

def c_two_grad_pb(a,b,c): 
    return ((28 * a) + (4 * b) + (6 * c) - 12)

parobola_2 = RSS_three(1,0,0,a_two_grad_pb, b_two_grad_pb, c_two_grad_pb, learning_rate=0.0001, num_iterations = 1000000)

assert round(parobola_2[0], 2) == 0.18
assert round(parobola_2[1], 2) == -0.27
assert round(parobola_2[2], 2) == 1.34

def a_logistic(a, b):
    return 2 * (0.5 - 1/(1 + math.e ** (a + b))) * (-1 * (math.e ** (a + b) / ((1 + math.e ** a + b) ** 2))) + 2 * (1 - (1/(1 + math.e ** (4 * a + b)))) * (-1 * (4 * math.e ** (4 * a + b))/(1 + math.e ** (4 * a + b)) ** 2)
def b_logistic1(a, b):
    return 2 * (-1 * ((math.e ** b) / ((1 + (math.e ** (a + b))) ** 2))) + 2 * (0.5 - (1/(1 + math.e ** (a + b)))) * (-1 * (math.e ** (a + b) / ((1 + math.e ** a + b) ** 2))) 
def b_logistic2(a, b):
    return 2 * (1 - (1/(1 + math.e ** (4 * a + b)))) * (-1 * (math.e ** (4 * a + b)) / (1 + math.e ** (4 * a + b)) ** 2)
def b_logistic(a, b):
    return b_logistic1(a, b) + b_logistic2(a, b)
print(a_logistic(1, 0))
print(b_logistic(1, 0))

logistic_1 = RSS_rounded(-1, 0, a_logistic, b_logistic, learning_rate = 0.01, num_iterations = 10000)
