#!/usr/bin/python3
import sys
if __name__ == "__main__":
    str_len = len(sys.argv)
    result = 0
    for i in range(1, str_len):
        result += int(sys.argv[i])
    print("{}".format(result))
