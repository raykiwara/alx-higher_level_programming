#!/usr/bin/python3
def uniq_add(my_list=[]):
    length = len(my_list)
    j = 0
    for i in my_list:
        if my_list:
            if (my_list[i] < my_list[i + 1]):
                j += my_list[i + 1]
        length -= length
    return j
