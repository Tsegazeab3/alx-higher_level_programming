#!/usr/bin/python3
"""
This module contains the matrix function
"""
def matrix_divided(matrix, div):
    """performs scalar division
        Args:
            matrix: an array of arrays
            div: the divisor
        expectations:
            matrix should only contain integers/floats 0
            matrix should be arectangle 0
            div must be a number 0
            div can't be 0 0
            all should be divided by div, round to 2 decimal places 0
        Return:
            new matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int,float)):
        raise TypeError("div must be a number")
    x = len(matrix[0])
    result_matrix = []

    for array in matrix:
        #checking whether the array is a rectangle
        if len(array) != x:
            raise TypeError("Each row of the matrix must have the same size")
        result_row = []
        for no in array:
            #checking whether number is a number
            if not isinstance(no,(int, float)):
                raise TypeError("Each row of the matrix must have the same size")
            result_row.append = round(no/div, 2)
        result_matrix.append(result_row)
    return(result_matrix)




