from matrix import Matrix
class PolynomialRegression:
    def fit(self, points, degree):

        self.data = points
        length = len(self.data[0])
        rows = [[point[-1]] for point in points]
        y_matrix = Matrix(rows)

        coefficient_rows = [[] for point in points]
        for i in range(0, len(self.data)):
            for j in range(0, degree + 1):
                coefficient_rows[i].append(self.data[i][0] ** j)
        
        coefficient_matrix = Matrix(coefficient_rows)

        coefficient_transpose = coefficient_matrix.transpose()
        transpose_times_y = coefficient_transpose.matrix_multiplication(y_matrix)
        transpose_times_coefficients = coefficient_transpose.matrix_multiplication(coefficient_matrix)

        inverse_matrix = transpose_times_coefficients.inverse()
        a_b_matrix = inverse_matrix.matrix_multiplication(transpose_times_y)
        self.coefficients = []
        for i in range(a_b_matrix.num_rows):
            self.coefficients.append(a_b_matrix.rows[i][0])

        

    def predict(self, input):
        answer = self.coefficients[0]
        for i in range(1, len(self.coefficients)):
            print(self.coefficients[1])
            answer += self.coefficients[i] * (input ** i)
        return answer
