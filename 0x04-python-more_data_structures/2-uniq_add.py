#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    uniqlist = list(uniq)
    sum = 0
    for i in range(len(uniqlist)):
        sum += uniqlist[i - 1]
    return sum
