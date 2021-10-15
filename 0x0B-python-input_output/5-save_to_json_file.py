#!/usr/bin/python3
""" Defines a function that writes an Object to a text file,
    using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using
        a JSON representation

        Parameters
        ----------
            my_obj : python object
                object whose JSON rep. is to be written
                to @filename

            filename : str
                name of the file to write to
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
