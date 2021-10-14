#!/usr/bin/python3
"""Defines a class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square"""

    def __init__(self, size):
        """
            Initialize a new Square instance

            Parameters
            ----------
                size : int
                    size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            Calculate area of the square.

            Returns
            -------
                area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
            String representation of the square

            Returns
            -------
                str
                    the square representation
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
