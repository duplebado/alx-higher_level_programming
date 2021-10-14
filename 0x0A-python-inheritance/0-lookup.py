#!/usr/bin/python3
""" Defines a function that returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """
        returns the list of available attributes and
        methods of an object

        Parameters
        ----------
            obj : Object
                a python object

        Returns
        -------
            list
                list of available attributes and methods of an object
    """

    return dir(obj)
