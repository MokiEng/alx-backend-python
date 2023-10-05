#!/usr/bin/env python3
"""a string and int/float to tuple module."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ a type-annotated function to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple.
    """
    return (k, float(v**2))
