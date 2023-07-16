#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    twos = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            twos.append(True)
        else:
            twos.append(False)

    return (twos)
