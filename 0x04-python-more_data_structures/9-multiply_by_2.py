#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    neo_dictionary = []
    for key, val in a_dictionary:
        neo_dictionary[key] = val * 2
    return neo_dictionary
