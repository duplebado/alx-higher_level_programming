#!/usr/bin/python3
""" Defines a class Student"""


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ initializes an instance of Student"""
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

    def to_json(self):
        return self.__dict__
