#!/usr/bin/python3
"""Defines a class Rectangle ."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle  """

    def __init__(self, width, height):
        """
            Initialize a new Rectangle instance

            Parameters
            ----------
                width : int
                    width of the rectangle

                height : int
                    height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            Calculate area of the rectangle.

            Returns
            -------
                area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
            String representation of the rectangle

            Returns
            -------
                str
                    the rectangle representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
