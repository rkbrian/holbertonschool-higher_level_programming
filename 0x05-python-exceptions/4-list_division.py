#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    add_list = []
    for i in range(list_length):
        try:
            addy = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            addy = 0
            print("division by 0")
        except TypeError:
            addy = 0
            print("wrong type")
        except IndexError:
            addy = 0
            print("out of range")
        finally:
            add_list.append(addy)
    return add_list
