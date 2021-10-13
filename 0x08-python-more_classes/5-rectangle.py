#!/usr/bin/python3
""" Defines a class Rectangle"""


class Rectangle:
    """
        A class to represent a rectangle

        Attributes
        ----------
            __width : int
                width of the rectangle

            __height : int
                height of the rectangle

        Setters
        -------
            width(self, value):
                sets new width of the rectangle

            height(self, value):
                sets new height of the rectangle

        Getters
        -------
            def width(self):
                returns the width of the rectangle

            def height(self):
                returns the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
            Initialize a new Rectangle.

            Parameters
            ----------
            width: int, optional
                width of the rectangle (default is 0)

            height: int, optional
                height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            width attribute getter of the rectangle.

            Returns
            -------
                int
                    the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter of the rectangle.

            Parameter
            ---------
                value: int
                    new width of the rectangle
            Raises
            ------
                TypeError
                    If @value is not an integer

                ValueError
                    If @value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
            height attribute getter of the rectangle.

            Returns
            -------
                int
                    the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter of the rectangle.

            Parameter
            ---------
                value: int
                    new height of the rectangle

            Raises
            ------
                TypeError
                    If @value is not an integer

                ValueError
                    If @value is less than 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
            Calculate area of the rectangle.

            Returns
            -------
                area of the rectangle
        """
        return self.__width * self.height

    def perimeter(self):
        """
            Calculate perimeter of the rectangle.

            Returns
            -------
                perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            String representation of the rectangle with
            the character '#' generator

            Returns
            -------
                str
                    the rectangle represented by '#'
        """
        result = ""

        if self.__height == 0 or self.__width == 0:
            return result

        for i in range(self.__height - 1):
            result += ("#" * self.__width) + '\n'

        result += ("#" * self.__width)

        return result

    def __repr__(self):
        """
            String representation of the rectangle to be
            able to recreate a new instance by using eval()

            Returns
            -------
                str
                    string representation of the rectangle to be able to
                    recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
            Prints 'Bye rectangle...' when the rectangle
            instance gets deleted
        """
        print("Bye rectangle...")
