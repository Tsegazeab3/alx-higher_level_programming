#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            if row:
                print(' '.join("{:d}".format(x) for x in row))
            else:
                print()
    else:
        return
