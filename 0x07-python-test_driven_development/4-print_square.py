#!/usr/bin/python3
"""
this module contains the print_square
it prints the "#" multiplied by size
test file be in tests
"""


def print_square(size):
    """
    this function prints "#" multiplied by size
    Args:
        size
    raises:
        TypeError: size must be an integer
        valueerror: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(size * "#")
