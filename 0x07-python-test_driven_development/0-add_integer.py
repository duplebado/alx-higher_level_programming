#!/usr/bin/python3
""" Defines a function that adds integers."""


def add_integer(a, b=98):
    """Computes the sum of two integers

    Parameters
    ----------
        a: int, float
            The first number
        b: int, float, optional
            The second number

    Raises
    ------
        TypeError
            If either of a or b is a non-integer and non-float

    Note
    ----
        Parameters/Arguments are typecasted to ints before addition
        is performed

    Returns
    -------
        int
            The sum of the two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
