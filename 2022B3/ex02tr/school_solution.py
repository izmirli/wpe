#!/usr/bin/env python3

from itertools import zip_longest


def tr(source, dest):
    d = dict(zip_longest(source, dest, fillvalue=dest[-1]))

    def replace(s):
        output = list(s)
        for index, item in enumerate(output):
            output[index] = d.get(item, item)

        return ''.join(output)

    return replace


vowels_to_y = tr('aeiou', 'y')
print(vowels_to_y('the quick brown fox jumps over the lazy dog'))
