#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    while length > 1:
        idx = 0
        while idx < length - 1:
            if my_list[idx] < my_list[idx + 1]:
                temp = my_list[idx]
                my_list[idx] = my_list[idx + 1]
                my_list[idx + 1] = temp
            idx += 1
        length -= 1
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
