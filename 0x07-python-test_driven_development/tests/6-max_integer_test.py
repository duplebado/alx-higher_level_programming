#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Define unittests for max_integer([..])"""

    def test_correct_list(self):
        """ Test that it returns correct result when
            appropriate argument is passed to it.
            This can be an ordered or unordered list
        """
        self.assertEqual(max_integer([3, 49, 45, 102]), 102)
        self.assertEqual(max_integer([3, 49, 45, 102, 499]), 499)
        self.assertEqual(max_integer([1, 2, 3, 4, 2, 4, 4]), 4)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([10, 8, 6, 4, 3, 1]), 10)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)
