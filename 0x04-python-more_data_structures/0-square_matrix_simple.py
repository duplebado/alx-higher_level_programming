#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    def square_each_cell(array):
        result = []
        for num in array:
            result.append(num ** 2)

        return result

    return list(map(square_each_cell, matrix))
