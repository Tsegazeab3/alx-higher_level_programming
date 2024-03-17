#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv) - 1
    if x == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(x))
        for i in range(1, x + 1):
            print("{}: {}".format(i, sys.argv[i]))