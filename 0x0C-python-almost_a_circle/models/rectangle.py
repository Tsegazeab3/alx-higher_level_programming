#!/usr/bin/python3
""" import super class """

from models.base import Base
import turtle


class Rectangle(Base):
    """
        Class Rectangle

        Method :

        Atrributes : width, height
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Defualt Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Private class """
        return self.__width

    @property
    def height(self):
        """Private class """
        return self.__height

    @property
    def x(self):
        """ Private class """
        return self.__x

    @property
    def y(self):
        """ Private class """
        return self.__y

    @width.setter
    def width(self, value):
        """Setter value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area """
        return self.__width * self.__height

    def display(self):
        """ Rectangle instance
                    return
                    symbol = "#"
               for high in range(self.__height):
                    for widt in range(self.__width):
                    print("{}".format(symbol), end="")
                    print("")
         """
        hash_value = "#"
        rect = ""

        print("\n" * self.y, end="")

        for high in range(self.height):
            rect += ("" * self.x) + (hash_value * self.width) + "\n"
        print(rect, end="")

    def __str__(self):
        """return [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ Update the attributes """
        length = len(args)
        if length == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """ to dictionary """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,

                'width': self.width}
