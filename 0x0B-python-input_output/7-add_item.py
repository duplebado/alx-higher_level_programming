#!/usr/bin/python3
""" Defines a script that adds all arguments to a Python list,
    and then save them to a file
"""
from sys import arg


if __name__ == "__main__":
    save_to_json_file, load_from_json_file  = (
            __import__('5-save_to_json_file').save_to_json_file,
            __import__('6-load_from_json_file').load_from_json_file
    )

    items = load_from_json_file("add_item.json")

    items += arg[1:]

    save_to_json_file(items, "add_item.json")
