#!/usr/bin/python3
def no_c(my_string):
    neo_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            neo_string += char
    return neo_string
