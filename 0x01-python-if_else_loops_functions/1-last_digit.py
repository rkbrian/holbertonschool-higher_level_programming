#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    mo = (-1 * number) % 10 * (-1)
else:
    mo = number % 10
la = "Last digit of "
gr = " and is greater than 5"
le = " and is less than 6 and not 0"
if mo > 5:
    print("{0}{1} is {2}{3}".format(la, number, mo, gr))
elif mo == 0:
    print("{0}{1} is {2} and is 0".format(la, number, mo))
else:
    print("{0}{1} is {2}{3}".format(la, number, mo, le))
