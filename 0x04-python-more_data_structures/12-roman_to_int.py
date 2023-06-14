#!/usr/bin/python3
def to_subtract(list_num):
    sub_i = 0
    max_list = max(list_num)

    i = 0
    while i < len(list_num):
        n = list_num[i]
        if n < max_list:
            sub_i += n
        i += 1

    return max_list - sub_i


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_dict.keys())

    num = 0
    prev_value = 0
    list_num = [0]

    i = 0
    while i < len(roman_string):
        ch = roman_string[i]
        j = 0
        while j < len(list_keys):
            r_num = list_keys[j]
            if r_num == ch:
                if roman_dict.get(ch) <= prev_value:
                    num += to_subtract(list_num)
                    list_num = [roman_dict.get(ch)]
                else:
                    list_num.append(roman_dict.get(ch))

                prev_value = roman_dict.get(ch)
            j += 1
        i += 1

    num += to_subtract(list_num)

    return num
