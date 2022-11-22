"""Functions for server."""


def reverse_word(word: str) -> str:
    return word[::-1]


def unicode_map(word: str) -> dict:
    return {letter: ord(letter) for letter in word}
