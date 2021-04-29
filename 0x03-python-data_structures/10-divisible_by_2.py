#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    evennums = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            evennums.append(True)
        else:
            evennums.append(False)
    return evennums
