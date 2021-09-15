#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None

    result = 0

    for key in a_dictionary:
        if a_dictionary[key] > result:
            result = a_dictionary[key]

    return result
