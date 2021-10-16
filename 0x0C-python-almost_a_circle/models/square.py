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
                    size of the instance of the square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Updates the Square instance

            Parameter
            ---------
                *args : tuple
                    1st argument should be the id attribute
                    2nd argument should be the size attribute
                    3rd argument should be the x attribute
                    4th argument should be the y attribute

                **kwargs : dict
                    key-value pairs of attributes
        """

        args_does_not_exist = True

        for i, arg in enumerate(args):
            args_does_not_exist = False

            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
                self.height = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg

        if args_does_not_exist:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
