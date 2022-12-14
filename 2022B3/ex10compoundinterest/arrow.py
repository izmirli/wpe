"""Arrow date.

Wrapper for datetime.date with external function `get` that returns an
Arrow date object.
"""
import datetime


class Arrow(datetime.date):
    pass


def get(year: int, month: int, day: int) -> Arrow:
    return Arrow(year, month, day)
