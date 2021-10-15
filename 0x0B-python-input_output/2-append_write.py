#!/usr/bin/python3
""" Defines a function appends a string at the end of a text
    file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Appends a string to a text file (UTF8) and returns the
        number of characters added

        Parameters
        ----------
            filename : str
                name of file to append to

            text : str
                text to append to @filename

        Returns
        -------
            number of characters append
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
