#!/usr/bin/python3
def element_at(lst=[], idx=''):
    for x in lst:
        if idx < 0:
            return None
        elif idx >= len(lst):
            return None
        else:
            return lst[idx]
