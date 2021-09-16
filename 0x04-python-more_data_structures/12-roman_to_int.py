#!/usr/bin/python3


def roman_to_int(roman_string):
    if (roman_string is None) or (not isinstance(roman_string, str)):
        return 0

    r_nums = {
                "I": 1, "V": 5,
                "IV": 4, "IX": 9,
                "X": 10, "L": 50,
                "C": 100, "D": 500,
                "M": 1000
              }

    result = 0
    strLen = len(roman_string)
    i = 0

    while i < strLen:
        if roman_string[i] == "I" and i + 1 < strLen:
            if roman_string[i + 1] == "V" or roman_string[i + 1] == "X":
                makeshift_key = roman_string[i] + roman_string[i + 1]
                result += r_nums[makeshift_key]
                i += 2
            else:
                result += r_nums[roman_string[i]]
        else:
            result += r_nums[roman_string[i]]

        i += 1

    return result
