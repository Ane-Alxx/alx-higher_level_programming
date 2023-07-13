#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    b = len(sys.argv) - 1
    if b == 0:
        print("0 arguments.")
    elif b == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(b))
    for i in range(b):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
