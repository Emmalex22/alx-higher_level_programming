#!/usr/bin/python3
def lookup(obj):
    # Get all attributes and methods using dir() function
    attributes_and_methods = dir(obj)

    # Filter out any private or special attributes/methods
    filtered_attributes_and_methods = [
        attr for attr in attributes_and_methods if not attr.startswith("__")
    ]
    return filtered_attributes_and_methods
