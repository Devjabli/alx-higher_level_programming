#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    roman_str = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for symbol in roman_string:
        value = roman_str.get(symbol, 0)
        if value == 0:  # If it's not a valid Roman numeral
            return 0

        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total
