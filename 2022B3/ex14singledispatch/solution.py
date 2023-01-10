"""Single dispatch.

Use "singledispatch" to create functionality that extends "mysum" as described here:

    - if we get a string, then we should turn each character into an
      integer. We'll ignore non-integers, but will turn integers into
      numbers and add them.

    - if we get a dict, then we should iterate over the values, adding
      them together. If there's a non-number among the values, then
      the function can raise a TypeError.

    - In all other cases, then we should iterate over the argument and
      add the numbers.  If there's a non-number, then the function can
      raise a TypeError exception.
"""
from functools import singledispatch


@singledispatch
def mysum(numbers):
    total = 0
    for one_number in numbers:
        total += one_number
    return total


@mysum.register
def _(numbers: str):
    return sum([int(i) for i in numbers if i.isdigit()])


@mysum.register
def _(numbers: dict):
    return sum([v for v in numbers.values()])


if __name__ == '__main__':
    cases = ((0, 1, 2, 4), "abc123", {'k1': 40, 'k2': 2})
    for case in cases:
        print(f"mysum({case}): {mysum(case)}")
