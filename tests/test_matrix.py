import sys
sys.path.append('src')

from matrix import Matrix
import math
import random

A = Matrix([[4, 3], [2, 1]])
B = Matrix([[4, 3], [2, 1]])
Identity = Matrix([[1, 0], [0, 1]])
A_and_identity = Matrix([[5, 3], [2, 2]])
At = Matrix([[4, 2], [3, 1]])
Ad = Matrix([[1, 1], [-1, -1]])
double_identity = Matrix([[2, 0], [0, 2]])
Three_Identity = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

if A.transpose().rows != At.rows:
    print("Transpose failed")
    A.transpose().print()
if A.add(Identity).rows != A_and_identity.rows:
    print("addition failed")
    A.add(Identity).print()
if A_and_identity.subtract(Identity).rows != A.rows:
    print("subtraction failed")
if Identity.scalar_multiply(2).rows != double_identity.rows:
    print("scalar_multiply failed")
    Identity.scalar_multiply(2).print()
C = Matrix([[4, 7], [0, -3], [9, 1]])
D = Matrix([[1, 2, -1], [1, 0, 1]])
Ay = Matrix([[7, -1, 11, 0], [8, -2, 3, 1], [-5, 4, -2, 6], [0, 5, -8, -9]])
X = Matrix([[3, 0, 0, 2], [8, 0, 3, 9], [2, 0, 2, 2], [1, 0, 1, 1]])
Three = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
if Ay.recursive_determinant_calc() != -4352:
    print("recursive_determinant_calc is broken")
if B.recursive_determinant_calc() != -2:
    print("recursive_determinant_calc is broken")
"""
print("The row reduced echelon form of")
D.print()
print("is:")
D.rref().print()
print()
print("The row reduced echelon form of")
Ay.print()
print("is:")
Ay.rref().print()
print()
print("The row reduced echelon form of")
C.print()
print("is:")
C.rref().print()
print()
print("The row reduced echelon form of")
X.print()
print("is:")
X.rref().print()
"""
"""
print("The inverse of the matrix")
A.print()
print("is: ")
A.inverse().print()
print()
print("The inverse of the matrix")
At.print()
print("is: ")
At.inverse().print()
print()
print("The inverse of the matrix")
A_and_identity.print()
print("is: ")
A_and_identity.inverse().print()
print()
print("The inverse of the matrix")
Three.print()
print("is: ")
Three.inverse().print()
"""
if Ay.recursive_determinant_calc() != Ay.determinant():
    print("broken 1")
if A.recursive_determinant_calc() != A.determinant():
    print("broken 2")
if X.recursive_determinant_calc() != X.determinant():
    print("broken 3")

L = Matrix([[3, 5, 7, 1.1, -4, 0, 7, 9, 2, 10], [7, 6, 5, 4, 8, 2, 4, 6, 7, 8], [9, 0, 0, 3, 6, 1, 8, 4.4, 7.9, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.2], [7, 8, 6, 5, 1, 2, 3, 9, 20, 7], [0, 0, -4, -1, -2, 7, 8, 6, 1.111, 9.34678], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 4, 5, 1, 2, 3, 7, 9, 8, 6]])
print(L.num_cols)
print(L.num_rows)
print(L.determinant())