#!/usr/bin/python3
def max_integer(my_list=[]):
    maxwell = my_list[0]
    for i in range(len(my_list) - 1):
        if maxwell < my_list[i]:
            maxwell = my_list[i]
    return maxwell