#!/usr/bin/python3
""" Defines a function that prints a square with the character '#'."""


def print_square(size):
    """ Prints a square with the character '#'

        Parameter
        ---------
            size: int
                size of the quare to be printed

        Raises
        ------
            TypeError
                if @size is of type float and it is less than 0
                if @size is not of type int

            ValueError
                If @size is less than 0
    """

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    i = size

    while (i):
        print("#" * size)
        i -= 1
