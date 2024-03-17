#!/usr/bin/python3
def no_c(strs):
    dengo = ''
    for x in strs:
        if x != 'c' and x != 'C':
            dengo += x
    return dengo
