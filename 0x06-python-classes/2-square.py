#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
