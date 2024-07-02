#!/usr/bin/python3
'''Creates a class square'''


class Square:
    '''Defines square based on size'''

    def __init__(self, size=0):
        '''Initializes an instance of Square object
            Args:
                param1 (int): size of the square'''
        self.__size = size

    @property
    def size(self):
        '''Retrieves size attribute'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter for size attribute
            Args:
                param1 (int): size of the square'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Method that gets the area of the square'''
        size = self.__size
        area = size * size
        return area
