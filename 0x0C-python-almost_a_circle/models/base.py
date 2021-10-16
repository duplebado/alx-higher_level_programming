#!/usr/bin/python
""" Defines Base class. """
import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize Base class instance

            Parameter
            ---------
                id : int
                    id of the new instance
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ gets JSON representation of a list_dictionaries

            Returns
            -------
                JSON
                    JSON representation of a list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)
