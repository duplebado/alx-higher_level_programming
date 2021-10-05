#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    actual_printed = 0

    try:
        while i < x:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            actual_printed += 1

        print(end="\n")
        return actual_printed
    except IndexError:
        raise;
    except:
        i += 1
