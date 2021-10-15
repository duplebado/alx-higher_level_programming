#!/usr/bin/python3
""" Defines a function that returns the JSON representation
    of an object (string)
"""
import json


def to_json_string(my_obj):
    """ Return JSON representation of an object

        Parameter
        ---------
            my_obj : Object
                object to be converted to JSON

        Returns
        -------
            JSON representation of an @my_obj
    """
    return (json.dumps(my_obj))
