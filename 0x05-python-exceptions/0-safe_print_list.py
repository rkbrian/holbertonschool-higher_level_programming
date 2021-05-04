#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counti = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counti += 1
        print()
        return counti
    except:
        print()
        return counti
