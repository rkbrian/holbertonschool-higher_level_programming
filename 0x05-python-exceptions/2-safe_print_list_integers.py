#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counti = 0
    for i in range(x):
        try:
            if isinstance(i, int):
                print("{:d}".format(my_list[i]), end="")
                counti += 1
        except (TypeError, ValueError):
            print("", end="")
    print()
    return counti
