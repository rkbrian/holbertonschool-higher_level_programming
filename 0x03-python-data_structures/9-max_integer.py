#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maxwell = my_list[0]
        if len(my_list) > 1:
            for i in my_list:
                if maxwell < i:
                    maxwell = i
        return maxwell
