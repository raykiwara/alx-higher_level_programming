#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i != j) and (i < j):
            if (i + j < 17):
                print(f"{i:01d}", end="")
                print(f"{j:d}", end=", ")
            else:
                print(f"{i:d}{j:d}")
