#!/usr/bin/python3
""" Defines a function that writes a string to a text file (UTF8) and
    returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8) and returns the
        number of characters written

        Parameters
        ----------
            filename : str
                name of file to write to

            text : str
                text to write to @filename

        Returns
        -------
            number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    return len(text)
