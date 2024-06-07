#!/usr/bin/python3
'''Creates class square'''


class Square:
    '''defines a square based on size'''
    def __init__(self, size=0):
        '''initializes an instance of square object
            Args:
                param1 (int): size of the square'''
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
