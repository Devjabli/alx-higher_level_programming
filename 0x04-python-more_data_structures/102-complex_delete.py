#!/usr/bin/python3
def complex_delete(my_dict, value):
    for k, v in my_dict.items():
        if v == value:
            my_dict.pop(k)
        return my_dict