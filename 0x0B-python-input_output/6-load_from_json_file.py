#!/usr/bin/python3
""" a function that creates an Object from a 'JSON file'"""
import json


def load_from_json_file(filename):
    """ Creates an Object from a 'JSON file'

        Paramter
        --------
            filename : str
                name of the JSON file

        Returns
        -------
            the object created from the JSON file
    """

    with open(filename) as f:
        return json.loads(f.read())
