import sys
sys.path.append('src')

from linear_regressor import LinearRegression
from logistic_regressor import LogisticRegression
from linear_regressor  import GeneralLinearRegression
from logistic_regressor import GeneralLogisticRegression
from analysis import BetterSandwich
from gen_logistic import EvenBetterSandwich

"""
print("For logistic Regression:")
a = LogisticRegression()
a.fit([[1, 0.2], [2, 0.25], [3, 0.5]])
if 0.636 - a.predict(4) <= 0.001:
    print("True")
b = LogisticRegression()
b.fit([[5, 0.6], [3, 0.4], [1, 0.2], [7, 0.8]])
if 0.5 - b.predict(4) <= 0.001:
    print("True")

c = LogisticRegression()
c.fit([[69, 0.69], [420, 0.420], [69, 0.420]])
if 0.585 - c.predict(4) <= 0.001:
    print("True")

print()
print("For linear regression:")
d = LinearRegression()
d.fit([[1, 0.2], [2, 0.25], [3, 0.5]])
if 0.617 - d.predict(4) <= 0.001:
    print("True")
e = LinearRegression()
e.fit([[5, 0.6], [3, 0.4], [1, 0.2], [7, 0.8]])
if 0.5 - e.predict(4) <= 0.001:
    print("True")
f = GeneralLinearRegression()
f.fit([[69, 0.69], [420, 0.420], [69, 0.420]])
if 0.58 - f.predict([4]) <= 0.001:
    print("True")

g = GeneralLinearRegression()
g.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6]])
assert g.coefficients == [0.6000000000000005, 1.799999999999999, 0.675]


h = GeneralLinearRegression()
h.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6], [0, 6, 7]])
assert h.coefficients == [0.8203124999999973, 1.7265625000000013, 0.7851562500000004]

i = GeneralLogisticRegression()
i.fit([[0.1, 0.2, 0.5], [0.9, 0.7, 0.9], [0.5, 0.6, 0.1]])
assert i.coefficients == [-2.7465307216702812, -16.479184330021653, 21.972245773362218]

j = GeneralLogisticRegression()
j.fit([[9, 0, 0.1], [1, 0, 0.2], [2, 0, 0.4], [4, 0, 0.8], [0, 8, 0.6]])
assert j.coefficients == [0.017376675350033788, 0.15832393650276563, -0.05285522293227472]
"""
a = BetterSandwich()
a.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6], [2, 2, 1], [3, 4, 1]], [(1, 2)])
assert a.coefficients == {(1, 2): -0.6641667008659251, 0: 0.9396930274551654, 1: 1.4395493905692112, 2: 0.7837751877539292}
assert a.predict([5, 5]) == -4.5478516025772615

interaction_term_test_2 = BetterSandwich()
interaction_term_test_2_data = [[0, 0, 0, 1], [1, 0, 5, 2], [2, 0, 1, 4], [4, 0, 0, 8], [6, 0, 0, 9], [0, 2, 0, 2], [0, 4, 0, 5], [0, 6, 0, 7], [0, 8, 0, 6], [2, 2, 0, 1], [3, 4, 0, 1], [5, 0, 1, 9], [5, 0, 5 ,3], [0, 3, 3, 1], [3, 3, 3, 1]]
interaction_term_test_2.fit(interaction_term_test_2_data, [(1, 2), (2, 3)])

for i in range(0, len(interaction_term_test_2_data)):
    interaction_term_test_2_data[i].insert(-1, interaction_term_test_2_data[i][0] * interaction_term_test_2_data[i][1])
    interaction_term_test_2_data[i].insert(-1, interaction_term_test_2_data[i][2] * interaction_term_test_2_data[i][1])

check = BetterSandwich()
check.fit(interaction_term_test_2_data)
assert check.predict([5, 0, 2, 0, 0]) ==  interaction_term_test_2.predict([5, 0, 2])

b = EvenBetterSandwich()
b.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6], [2, 2, 1], [3, 4, 1]], [(1, 2)], 0, 10)
b.predict([5, 5])

x = BetterSandwich()
x.fit([[0, 0, 0], [2, 0, 1], [3, 0, 2], [-1, 1, 2], [-6, 4, 5], [(1, 2)]])
print(x.coefficients)