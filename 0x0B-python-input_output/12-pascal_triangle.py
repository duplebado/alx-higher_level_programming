#!/usr/bin/python3
""" Defines a function that creates pascal's triangle"""


def pascal_triangle(n):
    """ Creates  pascal's traingle

        Parameter
        ---------
            n : int
                height of the triangle

        Returns
        -------
            list
                list of lists of ints
    """

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

            loop_result.append(result[i - 2][j - 1] + result[i - 2][j]])

        result.append(loop_result)
        i += 1

    return result
