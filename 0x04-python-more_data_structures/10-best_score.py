#!/usr/bin/python3
def best_score(a_dictionary):
    max_size = 0
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if v > max_size:
            max_size = v
    for k, v in a_dictionary.items():
        if v == max_size:
            return k
