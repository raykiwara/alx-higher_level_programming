#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if my_list[i] < my_list[i + 1]:
            temp = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = temp
        print("{:d}".format(my_list[i]))
