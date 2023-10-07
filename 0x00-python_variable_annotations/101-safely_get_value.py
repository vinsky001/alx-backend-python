i#!/usr/bin/env python3

"""
Given the parameters and return values, add type annotations to the function

Hint: look into TypeVar
"""


from typing import Dict, TypeVar, Optional


# create a type variable for the key type
K = Type("K")


def safely_get_value(
    dct: Dict[K, str],
    key: K,
    default: Optional[str] = None
) -> Optional[str]:
if key in dct:
        return dct[key]
    else:
        return default

    if _name__ == '__main__':
        annotations = safely_get_value.__annotations__
        print("Here's what the mappings should look like")
        for k, v in annotations.items():
            print(("{}: {}".format(k, v)))
