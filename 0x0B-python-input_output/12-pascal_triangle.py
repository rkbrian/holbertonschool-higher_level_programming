#!/usr/bin/python3
"""
module for function pascal_triangle
It looks so fun! Hahahahaha...
Hahahahahahahahahahahahahahahahahaha......
"""


def pascal_triangle(n):
    """function to create pasccal triangle"""

    if n <= 0:
        return []
    list_a = [1]
    list_b = [1]
    list_c = []
    lily = []
    print(list_a)
    for i in range(1, n):
        list_a.insert(0, 0)
        list_b.append(0)
        list_c = [a + b for a, b in zip(list_a, list_b)]
        lily.append(list_c)
        list_a = list(list_c)
        list_b = list(list_c)
    return(lily)
