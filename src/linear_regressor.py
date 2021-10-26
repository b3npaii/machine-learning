from matrix import Matrix

class LinearRegression:
    def fit(self, points):

        self.data = points
        rows = [[point[1]] for point in points]
        y_matrix = Matrix(rows)

        coefficient_rows = [[1, point[0]] for point in points]
        coefficient_matrix = Matrix(coefficient_rows)

        coefficient_transpose = coefficient_matrix.transpose()
        transpose_times_y = coefficient_transpose.matrix_multiplication(y_matrix)
        tranpose_times_coefficients = coefficient_transpose.matrix_multiplication(coefficient_matrix)

        inverse_matrix = tranpose_times_coefficients.inverse()
        a_b_matrix = inverse_matrix.matrix_multiplication(transpose_times_y)
        self.coefficients = []
        for i in range(a_b_matrix.num_rows):
            self.coefficients.append(a_b_matrix.rows[i][0])

    def predict(self, x):
        return self.coefficients[1] * x + self.coefficients[0]