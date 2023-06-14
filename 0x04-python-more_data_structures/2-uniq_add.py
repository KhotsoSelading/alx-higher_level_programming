#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    index_number = 0

    for x in uniq_list:
        index_number += x

    return (index_number)
