#!/usr/bin/python3
from hidden_4 import name
if __name__ == "__main__":
    for i in range(len(name)):
        if name[i][0] != chr(95):
            print("{}".format(name[i]))
