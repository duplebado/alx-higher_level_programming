#!/usr/bin/python3


def alt_case_reverse_alpha():
    for i in range(122, 96, -1):
        if (not(i % 2)):
            print("{}".format(chr(i)), end="")
        else:
            print("{}".format(chr(i - 32)), end="")

alt_case_reverse_alpha()            
