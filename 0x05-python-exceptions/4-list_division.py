#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0

    while i < list_length:
        calc = 0
        try:
            calc = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            result.append(calc)
            i += 1
