#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)
    # Iterate through the elements of the input matrix and square each value
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2
        return new_matrix
