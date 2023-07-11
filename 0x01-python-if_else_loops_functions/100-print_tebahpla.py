#!/usr/bin/python3
mono = 0
for mc in range(d('z'), d('a') - 1, -1):
    print("{}".format(chr(mc - mono)), end="")
    mono = 32 if mono == 0 else 0
