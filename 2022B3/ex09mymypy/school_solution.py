#!/usr/bin/env python3


def mymypy(types):
    def wrapper(f):
        def inner(*args, **kwargs):
            for one_arg, one_type in zip(args, types):
                if not isinstance(one_arg, one_type):
                    raise TypeError(f"{one_arg} must be of type {one_type}")
            return f(*args, **kwargs)
        return inner
    return wrapper
