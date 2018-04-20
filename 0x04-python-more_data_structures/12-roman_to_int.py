#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == "":
        return 0
    num_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    old = 0
    for c in roman_string:
        if num_dic[c] > old:
            total -= old * 2
        total += num_dic[c]
        old = num_dic[c]
    return total
