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
    def position(self,value):
        """settes position to value

        Args:
            Value(tuple): a tuple of 2 positive integers
        """
        if not isinstance(value, tuple(int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ area of the square"""
        return(self.size ** 2)

    def my_print(self):
        print("_"*self.position[1])

        if self.size == 0:
            print("")
        else:
            for i in range (0,self.size):
               for j in range (0, self.size):
                    print('#',end="")
               print("")

