#!/usr/bin/python3
def the_max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        the_max = my_list[0]
        for x in range(len(my_list)):
            if my_list[x] > the_max:
                the_max = my_list[x]
        return (the_max)
