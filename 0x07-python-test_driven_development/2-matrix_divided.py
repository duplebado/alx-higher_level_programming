#!/usr/bin/python3
""" Defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

        Parameters
        ----------
            matrix: list
                list of lists of integers/floats

            div: int, float
                A number to divide all elements of @matrix by

        Raises
        ------
            TypeError
                If @matrix isn't a list of lists of integers or floats
                If each row of @matrix isn't of the same size
                if @div isn't an int or a float

            ZeroDivisionError
                If @div is 0

        Returns
        -------
            list
                A new list of lists (matrix) containing the result of dividing
                each element in @matrix by @div rounded to 2 decimal places
    """

    err_msgs = (
        'matrix must be a matrix (list of lists) of integers/floats',
        'Each row of the matrix must have the same size',
        'div must be a number',
        'division by zero'
    )

    if type(div) not in [int, float]:
        raise TypeError(err_msgs[2])

    if div == 0:
        raise ZeroDivisionError(err_msgs[3])

    if type(matrix) is not list or matrix == []:
        raise TypeError(err_msgs[0])

    MATRIX_SIZE = 0

    if type(matrix[0]) is list and len(matrix[0]) > 0:
        MATRIX_SIZE = len(matrix[0])

    result = []

    for item in matrix:
        item_result = []

        if type(item) is not list or item == []:
            raise TypeError(err_msgs[0])

        if len(item) is not MATRIX_SIZE:
            raise TypeError(err_msgs[1])

        for digit in item:
            if type(digit) not in [int, float]:
                raise TypeError(err_msgs[0])

            item_result.append(round(digit / div, 2))

        result.append(item_result)

    return result
