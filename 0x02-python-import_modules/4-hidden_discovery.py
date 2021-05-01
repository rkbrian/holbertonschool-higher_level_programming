#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i in range(len(dir(hidden_4))):
        thename = dir(hidden_4)[i]
        if thename[0] == "_" and thename[1] == "_":
            continue
        print("{}".format(thename))
