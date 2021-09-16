#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    numerator = 0
    denominator = 0

    for tups in my_list:
        x, y = tups
        numerator += x * y
        denominator += y

    return numerator / denominator

