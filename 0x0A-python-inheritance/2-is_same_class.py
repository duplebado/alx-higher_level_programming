#!/usr/bin/python3
""" Defines a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
        Evaluate if the object is exactly an instance
        of the specified class

        Parameters
        ----------
            obj : Object
                an object

            a_class : Class
                a class

        Returns
        -------
            Boolean
                true or false

    """
    return isinstance(obj, a_class)
