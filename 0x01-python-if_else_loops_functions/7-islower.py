#!/usr/bin/python3
def islower(c):
    ascc = ord(c)
    if ascc in range(97, 123):
        return True
    elif ascc in range(65, 91):
        return False
