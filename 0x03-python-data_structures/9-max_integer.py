#!/usr/bin/python3
def imax_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        imax = my_list[0]
        for x in range(len(my_list)):
            if my_list[x] > imax:
                imax = my_list[x]
        return (imax)
