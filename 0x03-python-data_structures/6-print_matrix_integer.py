#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for x in range(len(matrix)):
            for n in range(len(matrix[x])):
                if n != len(matrix[x]) - 1:
                    space = ' '
                else:
                    space = ''
                print("{:d}".format(matrix[x][n]), end=space)
            print()
