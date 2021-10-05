#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    @__size.setter
    def __size(self, size=0):
        """ Pythonic setter """

        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
