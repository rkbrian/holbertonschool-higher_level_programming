#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        lett = ord(str[i])
        if lett in range(97, 123):
            lett -= 32
        print("{}".format(chr(lett)), end="")
    print("\n", end="")
