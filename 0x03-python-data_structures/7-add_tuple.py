#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    extended_tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    extended_tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]
    result_tuple = (extended_tuple_a[0] + extended_tuple_b[0], extended_tuple_a[1] + extended_tuple_b[1])
    return result_tuple
