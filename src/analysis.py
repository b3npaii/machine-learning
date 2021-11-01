from matrix import Matrix

class LinearRegression:
    def fit(self, points):

        self.data = points
        length = len(self.data[0])
        rows = [[point[-1]] for point in points]
        y_matrix = Matrix(rows)

        coefficient_rows = [[1] for point in points]
        for i in range(0, len(self.data)):
            for j in range(0, length - 1):
                coefficient_rows[i].append(self.data[i][j])
        
        coefficient_matrix = Matrix(coefficient_rows)

        coefficient_transpose = coefficient_matrix.transpose()
        transpose_times_y = coefficient_transpose.matrix_multiplication(y_matrix)
        transpose_times_coefficients = coefficient_transpose.matrix_multiplication(coefficient_matrix)

        inverse_matrix = transpose_times_coefficients.inverse()
        a_b_matrix = inverse_matrix.matrix_multiplication(transpose_times_y)
        self.coefficients = []
        for i in range(a_b_matrix.num_rows):
            self.coefficients.append(a_b_matrix.rows[i][0])

    def predict(self, x, y):
        return self.coefficients[1] * x + self.coefficients[2]*y + self.coefficients[0]

a = LinearRegression()
a.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6]])
print(a.predict(5, 5))
