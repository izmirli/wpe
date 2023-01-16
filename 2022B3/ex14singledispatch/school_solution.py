#!/usr/bin/env python3

from functools import singledispatch
from typing import Sequence


@singledispatch
def mysum(numbers: Sequence[float]):
    total = 0
    for one_number in numbers:
        total += one_number
    return total


@mysum.register
def _(numbers: dict):
    total = 0
    for one_number in numbers.values():
        total += one_number
    return total


@mysum.register
def _(numbers: str):
    total = 0
    for one_number in numbers:
        if one_number.isdigit():
            total += int(one_number)
    return total
