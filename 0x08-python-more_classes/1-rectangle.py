#!/usr/bin/python3
"""
module Creates a class called rectangle


>>> Rectangle = __import__('1-rectangle').Rectangle

>>> my_rectangle = Rectangle(2, 4)

>>> print(my_rectangle.__dict__)
{'_Rectangle__height': 4, '_Rectangle__width': 2}
>>> my_rectangle.width = 10

>>> my_rectangle.height = 3

>>> print(my_rectangle.__dict__)
{'_Rectangle__height': 3, '_Rectangle__width': 10}
"""


class Rectangle:
    """ class with a width and height """
    def __init__(self, width=0, height=0):
        """
        initialize width and height with optional value 0
        Args:
            width: width of the rectangle
            height: height of the height
        calls on setter and getter function
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter function for width
        Args:
            value: value that is set to width
        raise:
            typeerror: when width is not an integer
            valueerror: when width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter function for height
        Args:
            value: value that is set to width
        raise:
            typeerror: when height is not an integer
            valueerror: when height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
