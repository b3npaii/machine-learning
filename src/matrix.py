class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])

    def print(self):
        for row in self.rows:
            print(row)

    def copy(self):
        copied_matrix = [[element for element in row] for row in self.rows]
        return Matrix(copied_matrix)

    def add(self, other_matrix):
        answer = []
        for i in range(0, self.num_rows):
            answer.append([])
            for j in range(0, self.num_cols):
                answer[i].append(self.rows[i][j] + other_matrix.rows[i][j])
        return Matrix(answer)

    def subtract(self, other_matrix):
        new_rows = other_matrix.rows
        result = []
        for row in self.rows:
            result.append([])
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                result[i].append(self.rows[i][j] - new_rows[i][j])
        return Matrix(result)

    def transpose(self):
        if self.num_cols == self.num_rows:
            transposed_rows = []
            for i in range(0, self.num_rows):
                transposed_rows.append([])
                for j in range(0, self.num_cols):
                    transposed_rows[i].append(self.rows[j][i])
            return Matrix(transposed_rows)
        else:
            transposed_rows = []
            for i in range(0, self.num_cols):
                transposed_rows.append([])
                for j in range(0, self.num_rows):
                    transposed_rows[i].append(self.rows[j][i])
            return Matrix(transposed_rows)

    def scalar_multiply(self, scalar):
        rescaled_rows = []
        for row in self.rows:
            rescaled_rows.append([])
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                rescaled_rows[i].append(self.rows[j][i] * scalar)
        return Matrix(rescaled_rows)

    def matrix_multiplication(self, other_matrix):
        result = [[sum(a*b for a,b in zip(row,col)) for col in zip(*other_matrix.rows)] for row in self.rows]
        return Matrix(result)
        """
        product = []
        for i in range(self.num_rows):
            product.append([])
            for j in range(other_matrix.num_cols):
                product[i].append(0)
                for k in range(self.num_cols):
                    product[i][j] += self.rows[i][k] * other_matrix.rows[k][j]
        return Matrix(product)
        """


    def trim_matrix(self, i):
        trimmed_rows = self.copy().rows
        del trimmed_rows[0]
        for row in trimmed_rows:
            del trimmed_rows[trimmed_rows.index(row)][i]
        return Matrix(trimmed_rows)

    def recursive_determinant_calc(self):
        #print("taking the determinant of:")
        #self.print()
        #print("this matrix has ", self.num_cols, "columns")
        #print("this matrix has ", self.num_rows, "rows")
        if self.num_cols != self.num_rows:
            return "cannot take a determinant"

        elif self.num_rows == 2 and self.num_cols == 2:
            #print("got to the base case")
            det = (self.rows[0][0] * self.rows[1][1]) - (self.rows[0][1] * self.rows[1][0])
            return det

        else:
            determinant = 0
            for i in range(0, self.num_cols):
                #print("trimming the following matrix:")
                #self.print()
                coefficient = self.rows[0][i] * ((-1) ** i)
                smaller_matrix = self.trim_matrix(i)
                #print("coefficient = ", coefficient)
                #print("the smaller matrix is")
                #smaller_matrix.print()
                cofactor = coefficient * smaller_matrix.recursive_determinant_calc()
                determinant += cofactor
            return determinant

    def first_nonzero(self, i):
        for j in range(0, self.num_cols):
            if self.rows[i][j] != 0:
                return j
            elif j == self.num_cols - 1:
                break

    def check_pivot(self, i):
        for j in range(0, self.num_rows):
            if self.rows[i][j] != 0:
                if self.rows[i][:] == 0:
                    break
                else:
                    return j
            elif j == self.num_rows:
                return False

    def add_rows(self, i, j, scalar):
        added_row = self.copy().rows
        for k in range(0, self.num_cols):
            added_row[i][k] += scalar * self.rows[j][k]
        return Matrix(added_row)

    def row_swap(self, i, j):
        swapped_rows = self.copy().rows
        swapped_rows[i], swapped_rows[j] = swapped_rows[j], swapped_rows[i]
        return Matrix(swapped_rows)

    def rescale_row_by_element_of_row(self, i, j):
        changed_rows = self.copy().rows
        for k in range(0, self.num_cols):
            changed_rows[i][k] = (1 / self.rows[i][j]) * self.rows[i][k]
        return Matrix(changed_rows)

    def clear_above(self, i):
        cleared_rows = self.copy().rows
        nonzero = self.first_nonzero(i)
        for j in range(0, i):
            scalar = -1 * cleared_rows[j][nonzero]/cleared_rows[i][nonzero]
            cleared_matrix = Matrix(cleared_rows)
            cleared_matrix = cleared_matrix.add_rows(j, i, scalar)
            cleared_rows = cleared_matrix.rows
        return Matrix(cleared_rows)

    def clear_below(self, i):
        cleared_rows = self.copy().rows
        nonzero = self.first_nonzero(i)
        if i + 1 < self.num_rows:
            for j in range(i + 1, self.num_rows):
                scalar = - 1 * cleared_rows[j][nonzero]/cleared_rows[i][nonzero]
                cleared_matrix = Matrix(cleared_rows)
                cleared_matrix = cleared_matrix.add_rows(j, i, scalar)
                cleared_rows = cleared_matrix.rows
        return Matrix(cleared_rows)

    def first_nonzero_element_is_1(self, i):
        j = self.first_nonzero(i)
        copy = self.copy().rows
        for k in range(0, self.num_cols):
            copy[i][k] /= self.rows[i][j]
        return Matrix(copy)

    def check_if_zero_row(self, i):
        counter = 0
        for element in self.rows[i]:
            if element == 0:
                counter += 1
        if counter == self.num_cols:
            return True
        else:
            return False

    def check_if_reduced_row(self, i):
        counter = 0
        for element in self.rows[i]:
            if element == 0 or element == 1:
                counter += 1
        if counter == self.num_cols:
            return True
        else:
            return False

    def rref(self):
        copied_matrix = self.copy()
        if copied_matrix.num_cols > copied_matrix.num_rows:
            for i in range(0, copied_matrix.num_rows):
                if copied_matrix.check_if_zero_row(i) == True:
                    copied_matrix = copied_matrix.row_swap(i, self.num_rows - 1)
                    continue
                copied_matrix = copied_matrix.first_nonzero_element_is_1(i)
                copied_matrix = copied_matrix.clear_above(i)
                copied_matrix = copied_matrix.clear_below(i)
            for i in range(0, copied_matrix.num_rows - 1):
                if copied_matrix.check_if_zero_row(i) == True or copied_matrix.check_if_zero_row(i + 1) == True:
                    continue
                elif copied_matrix.first_nonzero(i) > copied_matrix.first_nonzero(i + 1):
                    copied_matrix = copied_matrix.row_swap(i, i + 1)
        elif copied_matrix.num_cols == copied_matrix.num_rows:
            for j in range(0, copied_matrix.num_rows):
                for i in range(0, copied_matrix.num_rows):
                    if copied_matrix.check_if_reduced_row(i) == True:
                        continue
                    if copied_matrix.check_if_zero_row(i) == True:
                        copied_matrix = copied_matrix.row_swap(i, self.num_cols)
                        continue
                    copied_matrix = copied_matrix.first_nonzero_element_is_1(i)
                    copied_matrix = copied_matrix.clear_above(i)
                    copied_matrix = copied_matrix.clear_below(i)
            for i in range(0, copied_matrix.num_rows - 1):
                if copied_matrix.check_if_zero_row(i) == True or copied_matrix.check_if_zero_row(i + 1) == True:
                    continue
                elif copied_matrix.first_nonzero(i) > copied_matrix.first_nonzero(i + 1):
                    copied_matrix = copied_matrix.row_swap(i, i + 1)
        elif copied_matrix.num_cols < copied_matrix.num_rows:
            for j in range(0, copied_matrix.num_rows):
                for i in range(0, copied_matrix.num_rows):
                    if copied_matrix.check_if_zero_row(i) == True:
                        copied_matrix = copied_matrix.row_swap(i, self.num_cols)
                        continue
                    copied_matrix = copied_matrix.first_nonzero_element_is_1(i)
                    copied_matrix = copied_matrix.clear_above(i)
                    copied_matrix = copied_matrix.clear_below(i)
            for i in range(0, copied_matrix.num_rows - 1):
                if copied_matrix.check_if_zero_row(i) == True or copied_matrix.check_if_zero_row(i + 1) == True:
                    continue
                elif copied_matrix.first_nonzero(i) > copied_matrix.first_nonzero(i + 1):
                    copied_matrix = copied_matrix.row_swap(i, i + 1)
        return copied_matrix

    def identity_matrix(self):
        Identity = []
        for i in range(0, self.num_rows):
            Identity.append([])
            for j in range(0, self.num_cols):
                Identity[i].append(0)
        for i in range(0, self.num_rows):
            Identity[i][i] += 1
        return Matrix(Identity)
    
    def inter(self):
        inted_matrix = self.copy().rows
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                inted_matrix[i][j] = int(self.rows[i][j])
        return Matrix(inted_matrix)
    
    def rescale_row(self, i, scalar):
        rescaled_rows = self.copy().rows
        for j in range(0, self.num_cols):
            rescaled_rows[i][j] *= scalar
        return Matrix(rescaled_rows)

    def augment_matrix(self, right_matrix):
        if self.num_rows != right_matrix.num_rows:
            return False
        copied_matrix = self.copy()
        for i in range(0, self.num_rows):
            copied_matrix.rows[i] = self.rows[i] + right_matrix.rows[i]
        return copied_matrix

    def un_augment_matrix(self, side):
        copied_matrix = self.copy()
        for i in range(0, self.num_rows):
            for j in range(0, int(self.num_cols/2)):
                if side == 1:
                    del copied_matrix.rows[i][0]
                if side == 2:
                    del copied_matrix.rows[i][-1]
        return copied_matrix

    def inverse(self):
        if self.num_cols != self.num_rows:
            return False
        Identity = self.identity_matrix()
        copied_matrix = self.copy()
        copied_matrix = copied_matrix.augment_matrix(Identity)
        row_reduced = copied_matrix.rref()
        """
        if row_reduced.un_augment_matrix(2).rows != Identity.rows:
            return False
        """
        answer = row_reduced.un_augment_matrix(1)
        return answer

    def determinant(self):
        det = 1
        row_reduced = self.rref().inter()
        if row_reduced.rows != self.identity_matrix().rows:
            det = 0
            return det
        copied_matrix = self.copy()
        for j in range(0, copied_matrix.num_rows):
            for i in range(0, copied_matrix.num_rows):
                if copied_matrix.check_if_reduced_row(i) == True:                        continue
                if copied_matrix.check_if_zero_row(i) == True:
                    copied_matrix = copied_matrix.row_swap(i, self.num_cols)
                    det *= -1
                    continue
                scalar_index = copied_matrix.first_nonzero(i)
                scalar = copied_matrix.rows[i][scalar_index]
                det *= scalar
                copied_matrix = copied_matrix.first_nonzero_element_is_1(i)
                copied_matrix = copied_matrix.clear_above(i)
                copied_matrix = copied_matrix.clear_below(i)
        for i in range(0, copied_matrix.num_rows - 1):
            if copied_matrix.check_if_zero_row(i) == True or copied_matrix.check_if_zero_row(i + 1) == True:
                continue
            elif copied_matrix.first_nonzero(i) > copied_matrix.first_nonzero(i + 1):
                copied_matrix = copied_matrix.row_swap(i, i + 1)
                det *= -1
        return det