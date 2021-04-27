#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
la = "Last digit of "
gr = " and is greater than 5"
le = " and is less than 6 and not 0"
if number > 5:
    print("{0}{1} is {2}{3}".format(la, number, number % 10, gr))
elif number == 0:
    print("{0}{1} is {2} and is 0".format(la, number, number % 10))
else:
    print("{0}{1} is {2}{3}".format(la, number, number % 10, le))
