#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        mo = (-1 * number) % 10
    else:
        mo = number % 10
    print("{}".format(mo), end="")
    return mo
