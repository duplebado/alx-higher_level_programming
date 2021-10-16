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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of @list_objs
            to a file

            Parameters
            ----------
                list_objs : list
                    list of instances who inherits from this class
                    (i.e Base clase) e.g list of Rectangle or list
                    of Square instances
        """
        obj_dicts = []

        for obj in list_objs:
            obj_dicts.append(obj.to_dictionary())

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(to_json_string(obj_dicts))
