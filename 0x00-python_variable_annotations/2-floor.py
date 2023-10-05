#!/usr/bin/env python3
"""
A type-annotated function flor which takes float n as an argument
and  returns the floor of the float
"""


import math


def floor(n: float) -> int:
    """
    takes a float n as argument and returns the floor of the float.
    """
    return math.floor(n)

    if __name__ == "__main__":
        ans = floor(3.14)

        print(ans == math.floor(3.14))
        print(floor.__annotations__)
        print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
