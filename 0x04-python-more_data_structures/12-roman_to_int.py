#!/usr/bin/python3


def roman_to_int(roman_string):
    if (roman_string is None) or (not isinstance(roman_string, str)):
        return 0

    r_nums = {
                "I": 1, "V": 5,
                "X": 10, "L": 50,
                "C": 100, "D": 500,
                "M": 1000
              }

    result = 0
    strLen = len(roman_string)
    i = 0

    for i in range(strLen):
        if i != strLen - 1 and r_nums[roman_string[i]] < r_nums[roman_string[i + 1]]:
           result += r_nums[roman_string[i]] * -1
        else:
            result += r_nums[roman_string[i]]

    return result
