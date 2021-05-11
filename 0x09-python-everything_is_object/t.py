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

c = 5
print("ID of c is {}".format(id(c)))
d = c
print("ID of d is {}".format(id(d)))
print("c is d? {}".format(c is d))
c += 1
print("ID of c is {}".format(id(c)))
