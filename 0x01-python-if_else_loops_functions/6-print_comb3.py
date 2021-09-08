#!/usr/bin/python3
for num in range(10):
    for num2 in range (10):
        if num2 > num:
            print("{}{}".format(num, num2),
            end='\n' if num == 8 and num2 == 9 else ", ")
