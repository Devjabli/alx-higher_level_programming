#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw_lst = []
    if my_list:
        for x in my_list:
            nw_lst.append(False if x % 2 else True)
        return nw_lst
