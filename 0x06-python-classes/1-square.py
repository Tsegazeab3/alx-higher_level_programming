#!/usr/bin/python3
"""writing a Square that defines a square(based on 0-square.py)"""


class Square:
    """Represent a Square. """
    def __init__(self, size) -> None:
        """Initializing a new square

        Args:
            size(Int): the size of the new square
        """
        self.__size = size
