#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ Calculates area of base geometry
            but not implemented

            Raises
            ------
                Exception
                    always
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates an integer

            Parameters
            ----------
                name : str
                    name of the integer to be validated

                value: int
                    integer to be validated

            Raises
            ------
                TypeError
                    if @value is not an integer

                ValueError
                    if @value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
