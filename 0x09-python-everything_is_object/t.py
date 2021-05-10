#!/usr/bin/python3
a = [1, 2, 3]
print("ID of a is {}".format(id(a)))
b = a
print("ID of b is {}".format(id(b)))
print("a is b? {}".format(a is b))

a += [4]
print("after a += [4]")
print(a)
print(b)
print("ID of a is {}".format(id(a)))
print("ID of b is {}".format(id(b)))
