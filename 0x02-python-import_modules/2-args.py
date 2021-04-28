#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arglen = len(argv) - 1
    if arglen == 0:
        print("{} arguments.".format(arglen))
    elif arglen == 1:
        print("{} argument:".format(arglen))
    else:
        print("{} arguments:".format(arglen))
    for i in range(1, arglen + 1):
        print("{0}: {1}".format(i, argv[i]))
