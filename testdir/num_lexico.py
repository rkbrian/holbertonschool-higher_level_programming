#!/usr/bin/python3

n = 10
list_a = list(range(1, n + 1))
status = 1
print(list_a)
while len(list_a) > 1:
    x = len(list_a)
    y = 0
    for i in range(y, int(x / 2), status):
        list_a.pop(i)
    list_a.pop(len(list_a) - 1)
    print(list_a)
    x, y = y, x
    status = status * (-1)
