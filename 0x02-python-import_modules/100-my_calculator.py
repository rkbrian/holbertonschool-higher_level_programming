#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arglen = len(argv) - 1
    if arglen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        opstr = "+-*/"
        if op == opstr[0]:
            print("{0} + {1} = {2}".format(a, b, add(a, b)))
        elif op == opstr[1]:
            print("{0} - {1} = {2}".format(a, b, sub(a, b)))
        elif op == opstr[2]:
            print("{0} * {1} = {2}".format(a, b, mul(a, b)))
        elif op == opstr[3]:
            print("{0} / {1} = {2}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
