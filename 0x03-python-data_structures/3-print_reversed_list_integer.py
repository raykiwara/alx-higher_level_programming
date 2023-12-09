#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    print("Length before loop: {}".format(length))
    for i in range(length):
        my_list[i] = my_list[length - 1]
        #length = length - 1
        print("Length: {}".format(length))
        print("{}".format(my_list[i]))
        length = length - 1
