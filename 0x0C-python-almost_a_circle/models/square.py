#!/usr/bin/python3
""" Defines a Square class"""
Rectangle = __import("rectangle").Rectangle


class Square(Rectangle):
    """ Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize an instance of Square

            Parameters
            ----------
                size :
                x :
                y :
                id :
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of the Square
            instance

            Returns
            -------
                str
                    the Square instance representation
        """

        return "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width
                )
