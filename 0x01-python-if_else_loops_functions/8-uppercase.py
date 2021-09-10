#!/usr/bin/python3
def uppercase(str):
    str_len = len(str)

    for i in range(str_len):
        if (str[i] >= "a" and str[i] <= "z"):
            print(chr(ord(str[i]) - 32), end='\n' if (i == str_len - 1) else '')
        else:
            print(str[i], end='\n' if (i == str_len - 1) else '')
