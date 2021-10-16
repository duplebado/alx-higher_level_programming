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

    @property
    def size(self):
        """ size getter.

            Returns
            -------
                int
                    size (i.e width/height) of the instance of the
                    square
        """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter

            Parameter
            ---------
                size : int
                    size of the instance of the rectangle
            Raises
            ------
                TypeError
                    if @size is not an integer
                ValueError
                    if @size is less than or equal to zero
        """
        self.width = size
        self.height = size
