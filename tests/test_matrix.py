import sys
sys.path.append('src')

from matrix import Matrix

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
print(Ay.recursive_determinant_calc())
print(Ay.determinant())
