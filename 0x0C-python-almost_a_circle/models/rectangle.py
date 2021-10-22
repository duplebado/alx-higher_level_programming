#!/usr/bin/python3
""" Defines a Rectangle class. """
from models.base import Base


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
        super().__init__(id)
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
        if value < 0:
            raise TypeError("{:s} must be >= 0".format(name))

    def area(self):
        """ Calculate area of Rectangle instance

            Returns
            -------
                int
                    area of rectangle instance
        """

        return self.__height * self.__width

    def display(self):
        """ Prints Rectangle instance with the
            character #
        """
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """ String representation of the Rectangle
            instance

            Returns
            -------
                str
                    the Rectangle instance representation
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id, self.__x, self.__y, self.__width, self.__height
                )

    def update(self, *args, **kwargs):
        """ Updates the Rectangle instance

            Parameter
            ---------
                *args : tuple
                    1st argument should be the id attribute
                    2nd argument should be the width attribute
                    3rd argument should be the height attribute
                    4th argument should be the x attribute
                    5th argument should be the y attribute

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
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg

        if args_does_not_exist:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ gets dictionary representation of a Rectangle

            Returns
            -------
                dict
                    dictionary representation of a Rectangle
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
