#!/usr/bin/python3
def roman_to_int(roman_string):
    rody = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if roman_string is None or isinstance(roman_string, str):
        return 0
    else:
        for latinum in roman_string:
            num += rody.get(latinum)
        lasti = len(roman_string) - 1
        if roman_string[lasti - 1] == 'I' and roman_string[lasti] != 'I':
            num -= 2
        return num
