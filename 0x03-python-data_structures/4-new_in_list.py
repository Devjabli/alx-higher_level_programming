#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        elem = []
        if idx < 0:
            return my_list
        elif idx >= len(my_list):
            return my_list
        else:
            elem += my_list
            elem[idx] = element
            return elem
