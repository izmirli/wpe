"""Numbers function for server."""


def numbers(length: str = '10') -> list:
    return list(range(int(length if length else '10')))
