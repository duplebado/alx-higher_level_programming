#!/usr/bin/python3
""" Defines a function that returns an object (Python data
    structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ Returns an object (Python data structure)
        represented by a JSON string

        Paramter
        --------
            my_str : JSON str
                string to be converted to object

        Returns
        -------
            object (Python data structure)
    """

    return json.loads(my_str)
