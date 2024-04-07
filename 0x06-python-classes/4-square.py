#!/usr/bin/python3
""" a module that creates a class named square"""


class Square:
    """ attributes of a class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ gets size"""
        self.size = self.__size

    @size.setter
    def size(self,value):
        """ settes size to value

        Args:
            Value: value of the size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area of the square"""
        return(self.__size ** 2)
