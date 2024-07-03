#!/usr/bin/python3
'''Defines a class Square'''


class Square:
    '''Defines a square based on size'''
    def __init__(self, size=0):
        '''Initializes an instance of square object'''
        self.__size = size

    @property
    def size(self):
        '''Retrieves size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter for size attribute'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Method that gets area'''
        size = self.__size
        area = size * size
        return area

    def my_print(self):
        '''Prints "#" as per the area'''
        size = self.__size
        if size == 0:
            print()
        for i in range(size):
            for j in range(1, size):
                print("#", end="")
            print("#")
