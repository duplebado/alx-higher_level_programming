#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
from sys import arg
save_to_json_file, load_from_json_file = (
            __import__('5-save_to_json_file').save_to_json_file,
            __import__('6-load_from_json_file').load_from_json_file
            )


def run_main():
    """ Aadds all arguments to a Python list, and
        then save them to a file
    """
    try:
        items = load_from_json_file("add_item.json")
    except:
        items = []

    items += arg[1:]

    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    run_main()