#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)

    c = 0 if lenA == 0 else tuple_a[0]
    c += 0 if lenB == 0 else tuple_b[0]

    d = 0 if lenA < 2 else tuple_a[1]
    d += 0 if lenB < 2 else tuple_b[1]

    return (c, d)
