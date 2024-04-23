#!/usr/bin/python3
""" Import the module base """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Name : Square

        Method :

        Attributes :
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Construstor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Private class """
        return self.height

    @size.setter
    def size(self, value):
        """ setter method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0.")
        self.__size = value
        self.__size = value

    def __str__(self):
        """ overloading method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)

    def update(self, *args, **kwargs):

        """ Update the attributes """
        length = len(args)
        if length == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """ Sqaure instance to dictionary representation """
        return {'id': self.id, 'x': self.x, "size": self.width, "y": self.y}
