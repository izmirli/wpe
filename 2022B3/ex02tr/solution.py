"""Translation function generator.

Implement "tr" as a function that takes two strings, and returns a
function that performs the translation on a string. In other words,
we should be able to do the following:

    vowels_to_y = tr('aeiou', 'y')
    print(vowels_to_y('the quick brown fox jumps over the lazy dog'))

and we should see:

    thy qyyck brywn fyx jymps yvyr thy lxzy dyg

"""
from typing import Callable


def tr(from_chars: str, to_chars: str) -> Callable:
    """Generate a translation function for given to/from strings.

    :param from_chars: characters to translate from (at least one character)
    :param to_chars: characters to translate to (at least one character)
    :return: translation function
    """
    if not from_chars or not to_chars:
        raise TypeError("Arguments expected to be strings with at least one character.")

    tr_dict = {c: to_chars[i] if i < len(to_chars) else to_chars[-1] for i, c in enumerate(from_chars)}

    def this_tr(to_translate: str) -> str:
        """Translate given string according to outer function parameters."""
        return ''.join([tr_dict.get(c, c) for c in to_translate])

    return this_tr
