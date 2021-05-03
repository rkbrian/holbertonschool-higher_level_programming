#!/usr/bin/python3
def safe_print_integer(value):
    if not value:
        return 0
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
