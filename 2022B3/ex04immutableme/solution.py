"""Immutable class "mixin".

When a class inherits from ImmutableParent, they should *not* implement
__init__ on their own. Instead, __init__ will take **kwargs, and will
use the key-value pairs there to set attributes on the object.
"""


class ImmutableParent:
    """Immutable base class."""

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)

    def __setattr__(self, name: str, value: any):
        raise ImmutableMeansImmutableError(
            f"Cannot set {name} in this immutable object."
        )

    def __getattr__(self, item: str):
        if item in self.__dict__:
            return object.__getattribute__(self, item)
        else:
            raise AttributeError


class ImmutableMeansImmutableError(Exception):
    """Exception for trying to set/update an immutable object."""
