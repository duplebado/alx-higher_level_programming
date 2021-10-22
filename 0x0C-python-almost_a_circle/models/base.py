#!/usr/bin/python
""" Defines Base class. """
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """ get list of the JSON string representation

            Paramter
            --------
                json_string : str
                    string representing a list of dictionaries

            Returns
            -------
                list
                    the list of the JSON string representation
                    @json_string
        """

        if json_string is None or json_string == []:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance of a class

            Parameter
            ---------
                **dictionary : dict
                    keyworded variable length of arguments

            Returns
            -------
                class instance
                    an instance with all attributes already
                    set
        """

        new_instance = None

        if cls is Rectangle:
            new_instance = cls(1, 2)
        else:
            new_instance = cls(1)

        new_instance.update(**dictionary)

        return new_instance

    @classmethod
    def load_from_file(cls):
        """ get a list of instances

            Returns
            -------
                list
                    a list of instances
        """
        filename = cls.__name__ + ".json"

        try:
            dict_list = None

            with open(filename) as f:
                dict_list = cls.from_json_string(f.read())

            result = []

            for dict_item in dict_list:
                result.append(cls.create(dict_item))

            return result
        except:
            return []

    def save_to_file_csv(cls, list_objs):
        """ writes the serialized csv format of @list_objs
            to a file

            Parameter
            ---------
                list_objs : list
                    list of instances who inherits from this class
                    (i.e Base clase) e.g list of Rectangle or list
                    of Square instances
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)

            for obj in list_objs:
                obj = obj.to_dictionary()
                row = []
                row.append(obj["id"])

                if cls is Rectangle:
                    row.append(obj["width"])
                    row.append(obj["height"])
                else:
                    row.append(obj["size"])

                row.append(obj["x"])
                row.append(obj["y"])

                writer.writerow(row)

    def load_from_file_csv(cls):
        """ deserialize csv format of @list_objs
            to a file
        """
        filename = cls.__name__ + ".csv"

        try:
            dict_list = None

            with open(filename) as f:
                csv_list = csv.reader(filename, delimiter=',')

            result = []

            for csv_item in dict_list:
                if cls is Rectangle:
                    result.append(cls.create({
                        "id": csv_item[0],
                        "width": csv_item[1],
                        "height": csv_item[2],
                        "x": csv_item[3],
                        "y": csv_item[4]
                        }))
                else:
                    result.append(cls.create({
                        "id": csv_item[0],
                        "size": csv_item[1],
                        "x": csv_item[2],
                        "y": csv_item[3]
                        }))

            return result
        except:
            return []
