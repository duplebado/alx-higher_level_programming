#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if argv[2] in ops:
        print("{:d} {:s} {:d} = {:d}".format(
            int(argv[1]),
            argv[2],
            int(argv[3]),
            ops[argv[2]](int(argv[1]), int(argv[3]))
            ))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
