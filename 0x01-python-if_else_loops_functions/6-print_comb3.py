#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i != j) and (i < j):
            if (i + j < 17):
                print("{:01d}".format(i), end="")
                print("{:d}".format(j), end=", ")
            else:
                print("{:d}{:d}".format(i, j))
