#!/usr/bin/python3
""" Defines a functuon matrix_divided
    Errors:
            TypeError: if matrix is not a list of lists
            TypeError: if the matrix is not of the same size
            ZeroDivisionError: if the matrix is divided by 0
            content of the matrix must be either an int or float
"""


def matrix_divided(matrix, div):
    """ The function the divides a matrix
        Arguments:
            matrix: a list of lists containing floats or ints
        div:
            the divisor
        Return:
            a new matrix whose value has been divided
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix "
                            "must have the same size")
        for data in row:
            if not isinstance(data, (int, float)):
                raise TypeError("div must be a number")
    return [(list(map(lambda data: round(data / div, 2), row))) for row in matrix]
