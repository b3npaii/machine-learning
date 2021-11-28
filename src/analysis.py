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


class BetterSandwich:
    def fit(self, points, interaction = None):

        self.data = points
        self.coefficients = {}
        self.num_interaction = 0

        length = len(self.data[0])
        rows = [[point[-1]] for point in points]
        y_matrix = Matrix(rows)

        coefficient_rows = []
        for point in points:
            row = point[:-1]
            row.append(1)
            coefficient_rows.append(row)

        if interaction is not None:
            self.num_interaction = len(interaction)
            for term in interaction:
                self.coefficients[term] = None
                for i in range(0, len(rows)):
                    term_to_append = 1
                    for item in term:
                        term_to_append *= points[i][item - 1]
                    coefficient_rows[i].insert(-1, term_to_append)

        coefficient_matrix = Matrix(coefficient_rows)
        coefficient_transpose = coefficient_matrix.transpose()
        transpose_times_y = coefficient_transpose.matrix_multiplication(y_matrix)
        transpose_times_coefficients = coefficient_transpose.matrix_multiplication(coefficient_matrix)

        inverse_matrix = transpose_times_coefficients.inverse()
        a_b_matrix = inverse_matrix.matrix_multiplication(transpose_times_y)

        coefficient_first = a_b_matrix.rows[-1]
        for i in range(0, len(a_b_matrix.rows) - 1):
            coefficient_first.append(a_b_matrix.rows[i][0])

        for i in range(0, len(points[0])):
            self.coefficients[i] = coefficient_first.pop(0)

        for key in self.coefficients:
            if self.coefficients[key] is None:
                self.coefficients[key] = coefficient_first.pop(0)

    def predict(self, inputs):
        if self.coefficients is None:
            return "no data to fit"
        if len(inputs) != len(self.coefficients) - self.num_interaction - 1:
            return "broken"
        answer = 0
        for beta in self.coefficients:
            if beta == 0:
                continue
            elif isinstance(beta, int):
                answer += self.coefficients[beta] * inputs[beta - 1]
            else:
                interaction_term = self.coefficients[beta]
                for term in beta:
                    interaction_term *= inputs[term - 1]
                answer += interaction_term
        answer += self.coefficients[0]
        return answer
