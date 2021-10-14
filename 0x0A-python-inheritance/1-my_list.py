#!/usr/bin/python3
""" Defines class MyList that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """Prints the sorted list in ascending order"""
        print(sorted(self))
