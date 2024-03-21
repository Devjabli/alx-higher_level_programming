#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dis = {}
    for k, v in a_dictionary.items():
        dis[k] = v * 2
    return dis
