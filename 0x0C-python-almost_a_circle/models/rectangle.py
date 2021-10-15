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

            Raises
            ------
                TypeError
                    if @width is not an integer

                ValueError
                    if @width is less than or equal to zero
        """
        self.integer_validator("width", width)
        self.less_than_or_equal_zero_validator("width", width)
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

            Raises
            ------
                TypeError
                    if @height is not an integer

                ValueError
                    if @height is less than or equal to zero
        """
        self.integer_validator("height", height)
        self.less_than_or_equal_zero_validator("height", height)
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

            Raises
            ------
                TypeError
                    if @x is not an integer

                ValueError
                    if @x is less than zero
        """
        self.integer_validator("x", x)
        self.less_than_zero_validator("x", x)
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
        """ y setter

            Parameter
            ---------
                y : int
                    y of the instance of the rectangle

            Raises
            ------
                TypeError
                    if @y is not an integer

                ValueError
                    if @y is less than zero
        """

        self.integer_validator("y", y)
        self.less_than_zero_validator("y", y)
        self.__y = y

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
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

    def less_than_or_equal_zero_validator(self, name, value):
        """
            Validates that an integer is not less than
            or equal zero

            Parameters
            ----------
                name : str
                    name of the integer to be validated

                value: int
                    integer to be validated

            Raises
            ------
                ValueError
                    if @value is less than or equal to zero
        """
        if value <= 0:
            raise TypeError("{:s} must be > 0".format(name))

    def less_than_zero_validator(self, name, value):
        """
            Validates that an integer is not less than
            zero

            Parameters
            ----------
                name : str
                    name of the integer to be validated

                value: int
                    integer to be validated

            Raises
            ------
                ValueError
                    if @value is less than zero
        """
        if value <= 0:
            raise TypeError("{:s} must be >= 0".format(name))
