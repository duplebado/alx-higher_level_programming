#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    def my_map(fn, a_list):
        for list_item in a_list:
            fn(list_item)

    def del_key(key):
        if a_dictionary[key] == value:
            del a_dictionary[key]

    my_map(del_key, list(a_dictionary.keys()))
    return a_dictionary
