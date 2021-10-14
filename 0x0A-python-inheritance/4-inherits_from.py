#!/usr/bin/python3
""" Defines a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
        Evaluate if the object is an instance
        of a class that inherited (directly or
        indirectly) from the from the specified class

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
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
