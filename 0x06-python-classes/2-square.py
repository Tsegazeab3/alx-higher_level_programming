#!/usr/bin/python3
""" a module that creates a class named square"""


class Square:
    """ attributes of a class"""

    def __init__(self, size=0):
        """initiate a new square

        Args:
            size(int): is not an integer

        Raises:
            TypeError: if size not an int
            ValueEror: if size less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
