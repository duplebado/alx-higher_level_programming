#!/usr/bin/python3
""" Defines a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """ Reads and prints a file

        Parameters
        ----------
            filename : str
                name of the file to be read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
