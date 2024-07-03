#!/usr/bin/python3
'''Defines a class square'''


class Square:
    '''Defines a square based on size'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Retrieves size attribute'''
        return self.__size

    @property
    def position(self):
        '''Retrieves position attribute'''
        return self.__position

    @size.setter
    def size(self, value):
        '''Setter for size attribute'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        '''Setter for position attribute'''
        if len(value) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''Gets the area'''
        size = self.__size
        area = size * size
        return area

    def my_print(self):
        '''Prints "#" as per the area'''
        size = self.__size
        position = self.__position
        if size == 0:
            print()
        for i in range(size):
            print("_" * position[0], end="")
            for j in range(1, size):
                print("#", end="")
            print("#")
