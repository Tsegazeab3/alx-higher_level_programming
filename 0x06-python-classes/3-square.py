#!/usr/bin/python3
""" a module that creates a class named square"""


class Square:
    """ attributes of a class"""
    def __init__(self, size=0):
        """initiate a new square

        Args:
            size(int): is not an integer
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area of the square

        Returns:
            The size Squared.
        """
        return self.__size ** 2
