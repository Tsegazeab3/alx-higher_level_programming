# #!/usr/bin/bash
# """ write a Square class with:
# -private instance attribute: size
# -encapsulate size and insert setter with Type Error if not integer
# and Value Error if size < 0
# """


# class Square:
#     """ Defining Square"""
#     def __init__(self, size=0):
#         """intitialization function for Square

#         Args:
#             size(int): The size of the new square
#         """
#         self.size = size

#     @property
#     def size(self):
#         """getter function for instance"""
#         return(self.__size)

#     @size.setter
#     def size(self, value):
#         """ setter function for size

#         Args:
#             value(int): value to be inserted"""
#         if type(value) != int:
#             raise TypeError("size must be an integer")
#         if(value < 0):
#             raise ValueError("size must be >= 0")
#         self.__size = value
#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size