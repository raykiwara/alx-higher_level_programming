#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list) - 1
    while length > 1:
        idx = 0
        while idx < length:
            if my_list[idx] > my_list[idx + 1]:
                temp = my_list[idx]
                my_list[idx] = my_list[idx + 1]
                my_list[idx + 1] = temp
            idx += 1
        length -= 1
    i = len(my_list) - 1
    max_value = my_list[i]
    return max_value
