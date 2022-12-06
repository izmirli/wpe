"""A simple "mypy" version as a decorator.

Apply the "mymypy" decorator to a function, passing it a list of valid types.
For example:

    @mymypy([int, int])
    def mul(a,b):
        return a*b

    print(mul([10,20,30],5))   # raises a TypeError, indicating that
                               # 1st arg must be an int
"""
from typing import Callable, Any, Type


def mymypy(arg_types: list[Type]) -> Callable:
    def mid_wrap(func: Callable) -> Callable:
        def inner_wrap(*args, **kwargs) -> Any:
            if len(args) != len(arg_types):
                raise TypeError(f"mymypy's {func.__name__} takes {len(arg_types)} "
                                f"positional arguments but {len(args)} were given")
            for i, arg_type in enumerate(arg_types):
                if type(args[i]) is not arg_type:
                    raise TypeError(f"{args[i]} must be of type {arg_type.__name__}")
            return func(*args, **kwargs)

        return inner_wrap

    return mid_wrap


def main():
    @mymypy([int, 'str'])
    def mul(a, b):
        return a * b

    mul('a', 'b', 'c')


if __name__ == '__main__':
    main()
