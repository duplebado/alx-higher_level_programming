#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv

    print("{:d} {:s}{}".format(
        len(argv) - 1,
        "arguments" if len(argv) != 2 else "argument",
        "." if len(argv) == 1 else ":"
        ))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
