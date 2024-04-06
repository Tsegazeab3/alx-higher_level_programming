#!/usr/bin/bash
""" write a Square class with:
-private instance attribute: size
-encapsulate size and insert setter with Type Error if not integer
and Value Error if size < 0
"""


class Square:
    """ Defining Square"""
    def __init__(self, size):
        """intitialization function for Square"""
        self.size = size

    @property
    def size(self):
        """getter function for instance"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """ setter function for size"""
        if value != int:
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
