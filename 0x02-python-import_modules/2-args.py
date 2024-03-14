#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 2:
        print("{} argument:".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))
    counter = 0
    for i in range(1, length):
        counter += 1
        print("{}: {}".format(counter, sys.argv[i]))
