#!/usr/bin/python3
def roman_to_int(roman_string):
    rody = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prtstr = []
    num = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    else:
        for latinum in roman_string:
            num += rody.get(latinum)
            prtstr.append(rody.get(latinum))
            i = len(prtstr) - 1
            if i > 0 and prtstr[i - 1] < prtstr[i]:
                num -= prtstr[i - 1] * 2
        return int(num)
