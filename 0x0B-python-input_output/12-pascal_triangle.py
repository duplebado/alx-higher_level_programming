#!/usr/bin/python3
'''A module containing combinatorial mathematical functions.
'''


def pascal_triangle(n):
    '''Generates a list of lists of integers representing the
    Pascal’s triangle of a given integer.
    Args:
        n (int): The number of rows in the triangle.
    Returns:
        list: A list of integers containing the values of their
        respective row in Pascal's triangle for the given number.
    '''
    result = []

    if n <= 0:
        return result

    result.append([1])

    i = 1

    while i < n:
        loop_result = []

        for j, num in result[i - 1]:
            if j == 0 or j == len(result[i - 1]) - 1:
                loop_result.append(1)
                continue

            loop_result.append(result[i - 2][j - 1] + result[i - 2][j])

        result.append(loop_result)

        i += 1

    return result
