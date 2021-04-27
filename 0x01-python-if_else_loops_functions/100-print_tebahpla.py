#!/usr/bin/python3
# it's a weird alphabet, short for WeirdAl
for WeirdAl in range(122, 96, -1):
    if WeirdAl % 2 > 0:
        WeirdAl -= 32
    print("{}".format(chr(WeirdAl)), end="")
