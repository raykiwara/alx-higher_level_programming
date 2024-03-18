#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    while length > 1:
        idx = 0
        while idx < length - 1:
            if my_list[idx] < my_list[idx + 1]:
                temp = my_list[idx]
                my_list[idx] = my_list[idx + 1]
                my_list[idx + 1] = temp
            idx += 1
        length -= 1
    return my_list[0]
