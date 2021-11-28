data = [[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6]]
from matrix import Matrix
for point in data:
    point.append(point[0] * point[1])
a = Matrix(data)
b = Matrix([[1], [2], [4], [8], [9], [2], [5], [7], [6]])
c = Matrix([[1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 4, 0], [1, 6, 0], [1, 0, 2], [1, 0, 4], [1, 0, 6], [1, 0, 8]])
ct = c.transpose()
ty = ct.matrix_multiplication(b)
tc = ct.matrix_multiplication(c)
tci = tc.inverse()
ab = tci.matrix_multiplication(ty)
ab.print()