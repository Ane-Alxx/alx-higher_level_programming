#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    a = 0
    for b in range(len(sys.argv) - 1):
        a += int(sys.argv[b + 1])
    print("{}".format(a))
