#!/usr/bin/python3
def lookup(obj):
    """
    Get a list of public attributes and methods of an object.

    Args:
    - obj: The object for which to retrieve attributes and methods.

    Returns:
    - A list containing the public attributes and methods of the object.
    """
    # Get all attributes and methods using dir() function
    attributes_and_methods = dir(obj)

    # Filter out any private or special attributes/methods
    filtered_attributes_and_methods = [
        attr for attr in attributes_and_methods if not attr.startswith("__")
    ]
    return filtered_attributes_and_methods
