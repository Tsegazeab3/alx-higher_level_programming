#!/usr/bin/python3
"""
prints out the first and last name of a person
has the functions say_my_name
returns nothing
test file inside tests
"""

def say_my_name(first_name, last_name=""):
    """
    Introduces a person
    Args:
        first_name: The name of the person
        last_name: last name of the personn
    Exceptions:
        Type Error: first and last name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
