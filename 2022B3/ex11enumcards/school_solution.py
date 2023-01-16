#!/usr/bin/env python3

import random
from enum import IntEnum, auto, unique


@unique
class CardSuit(IntEnum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()


@unique
class CardValue(IntEnum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        if self.suit < other.suit:
            return True

        elif self.value < other.value:
            return True

        else:
            return False

    def __repr__(self):
        return f"{self.value.name} of {self.suit.name}"
