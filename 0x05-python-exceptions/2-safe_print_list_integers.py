#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list:
        return 0
    counti = 0
    printi = 0
    for i in range(x):
        try:
            if isinstance(i, int):
                print("{:d}".format(my_list[i]), end="")
                printi += 1
                counti += 1
        except (TypeError, ValueError):
            print("", end="")
    print()
    return printi
