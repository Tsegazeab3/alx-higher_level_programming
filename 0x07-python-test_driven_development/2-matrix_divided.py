#!/usr/bin/python3
"""
This module contains the matrix function
"""


def matrix_divided(matrix, div):
    """performs scalar division
    Args:
        matrix: an array of arrays
        div: the divisor
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        new matrix
    """
    string = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError(string)
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    x = len(matrix[0])
    result_matrix = []
    for array in matrix:
        if len(array) != x:
            raise TypeError("Each row of the matrix must have the same size")
        result_row = []
        for no in array:
            if not isinstance(no, (int, float)):
                raise TypeError(string)
            result = round(no/div, 2)
            result_row.append(result)
        result_matrix.append(result_row)
    return(result_matrix)
