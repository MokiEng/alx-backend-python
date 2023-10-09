#!/usr/bin/env python3
""" a  module to determineelement_length."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a function return values with the appropriate types."""
    return [(i, len(i)) for i in lst]
