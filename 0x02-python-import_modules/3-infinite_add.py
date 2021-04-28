#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arglen = len(argv) - 1
    sumus = 0
    for i in range(1, arglen + 1):
        sumus += int(argv[i])
    print("{}".format(sumus))
