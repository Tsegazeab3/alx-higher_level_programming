#!/usr/bin/python3
""" a module that creates a class named square"""


class Square:
    """ attributes of a class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ gets size

        return
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ settes size to value

        Args:
            Value: value of the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area of the square"""
        return self.__size ** 2

    def my_print(self):
        """ prints out the square with the caracter #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
