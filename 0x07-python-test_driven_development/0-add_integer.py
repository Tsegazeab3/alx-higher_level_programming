#!/usr/bin/python3
"""

This module contains function that adds numbers
func_name: add_integer
"""


def add_integer(a, b=98):
    """Args: a: no1  b: no2 default value 98
    Return:sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return(sum)

