#!/usr/bin/python3

def element_at(my_list, idx):

    a = len(my_list)
    a = int(a)
    if (idx < 0):
        return None
    elif (idx < a) or (idx == a - 1):
        return my_list[idx]
    else:
        return None
