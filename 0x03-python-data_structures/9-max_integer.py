#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    result = 0

    for num in my_list:
        result = num if num > result


    return result
