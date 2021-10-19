import sys
sys.path.append('src')

from linear_regressor import LinearRegression
from logistic_regressor import LogisticRegression

print("For logistic Regression:")
a = LogisticRegression()
a.fit([[1, 0.2], [2, 0.25], [3, 0.5]])
if 0.636 - a.predict(4) <= 0.01:
    print("True")
b = LogisticRegression()
b.fit([[5, 0.6], [3, 0.4], [1, 0.2], [7, 0.8]])
if 0.5 - b.predict(4) <= 0.01:
    print("True")

c = LogisticRegression()
c.fit([[69, 0.69], [420, 0.420], [69, 0.420]])
if 0.585 - c.predict(4) <= 0.01:
    print("True")

print()
print("For linear regression:")
d = LinearRegression()
d.fit([[1, 0.2], [2, 0.25], [3, 0.5]])
if 0.617 - d.predict(4) <= 0.01:
    print("True")
e = LinearRegression()
e.fit([[5, 0.6], [3, 0.4], [1, 0.2], [7, 0.8]])
if 0.5 - e.predict(4) <= 0.01:
    print("True")
f = LinearRegression()
f.fit([[69, 0.69], [420, 0.420], [69, 0.420]])
if 0.58 - f.predict(4) <= 0.01:
    print("True")