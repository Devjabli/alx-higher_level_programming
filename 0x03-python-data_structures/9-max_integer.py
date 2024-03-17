#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_vl = my_list[0]
    for x in my_list:
        if x > max_vl:
            max_vl = x
    return max_vl
