#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int, float): First integer or float.
        b (int, float): Second integer or float. Default is 98.

    Returns:
        int: The sum of a and b, casted to integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
