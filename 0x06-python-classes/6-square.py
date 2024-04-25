#!/usr/bin/python3
""" a module that creates a class named square"""


class Square:
    """ attributes of a class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ gets size"""
        return(self.__size)

    @property
    def position(self):
        """gets position"""
        return(self.__position)

    @size.setter
    def size(self, value):
        """ settes size to value

        Args:
            Value: value of the size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    @position.setter
    def position(self, value):
        """settes position to value

        Args:
            Value(tuple): a tuple of 2 positive integers
        """
        bool1 = isinstance(value, tuple)
        bool2 = isinstance((value[0], value[1]), int)
        bool3 = value[0] >= 0 and value[1] >=0
        bool3 = len(value) == 2
        if not (bool1 or bool2 or bool3):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ area of the square"""
        return(self.size ** 2)

    def my_print(self):
        """ print the square with the character #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
