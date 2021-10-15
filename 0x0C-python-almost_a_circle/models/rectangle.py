#!/usr/bin/python3
""" Defines a Rectangle class. """
Base = __import__("base").Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize an instance of Rectangle

            Parameters
            ----------
                width :
                height :
                x :
                y :
                id :
        """
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter.

            Returns
            -------
                int
                    width of the instance of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter

            Parameter
            ---------
                width : int
                    width of the instance of the rectangle
        """
        self.__width = width

    @property
    def height(self):
        """ height getter.

            Returns
            -------
                int
                    height of the instance of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter

            Parameter
            ---------
                height : int
                    height of the instance of the rectangle
        """
        self.__height = height

    @property
    def x(self):
        """ x getter.

            Returns
            -------
                int
                    x of the instance of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter

            Parameter
            ---------
                x : int
                    x of the instance of the rectangle
        """
        self.__x = x

    @property
    def y(self):
        """ y getter.

            Returns
            -------
                int
                    y of the instance of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ width setter

            Parameter
            ---------
                y : int
                    y of the instance of the rectangle
        """
        self.__y = y
