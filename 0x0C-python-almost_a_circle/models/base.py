#!/usr/bin/python
""" Defines Base class. """


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
