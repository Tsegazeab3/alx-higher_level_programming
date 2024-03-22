#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            if matrix[row] is None:
                for column in matrix[row]:
                    print("{:d}".format(column), end=' ')
            else:
                continue
            print()

