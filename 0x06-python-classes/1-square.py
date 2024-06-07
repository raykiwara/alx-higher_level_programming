#!/usr/bin/python3
"""Creates a square class"""


class Square():
    ''' The square class defines a square by size'''
    def __init__(self, size):
        """
        Initializes an instance of the square object.
        Args:
            param1(int): The size of the Square.
        """
        self.__size = size
