#!/usr/bin/env python3
"""
Contains a type-annotated function add that takes a float a
and a float b as arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """
    Returns float a and b as arguments and returns
    their sum as a float.
    """
    return a + b

    if __name__ == '__main__':
        print(add(1.11, 2.22) == 1.11 + 2.22)
        print(add.__annotations__)
