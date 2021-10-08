#!/usr/bin/python3
""" Defines a function that prints a text with 2 new lines after
    each of these characters: `.`, `?` and `:`
"""


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these
        characters: `.`, `?` and `:`

        Parameter
        ---------
            text: string
                text whose characters are to be printed

        Raise
        -----
            TypeError
                If text is not a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    print_start, current_point = 0, 0
    str_len = len(text)

    while (current_point < str_len):
        while text[print_start] == " ":
            print_start, current_point = print_start + 1, current_point + 1

        print(text[current_point], end="")

        if text[current_point] == "." or\
            text[current_point] == "?" or \
                text[current_point] == ":":
                print('\n')
                print_start = current_point + 1

        current_point += 1
