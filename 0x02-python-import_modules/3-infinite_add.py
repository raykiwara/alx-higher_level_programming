#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = len(sys.argv)
    sum = 0

    for i in range(1, arg):
        sum += int(sys.argv[i])
    print("{:d}".format(sum))
