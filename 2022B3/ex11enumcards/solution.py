"""Enum cards.

Create deck of 52 cards in which each instance of Card has both a suit and a value.
Then you'll choose five random cards from the deck and print them.
Use Enum classes: CardSuit & CardValue.
"""
from enum import Enum
from random import choices


class CardSuit(Enum):
    """Enum class for playing cards suits."""
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class CardValue(Enum):
    """Enum class for playing cards values."""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    """Enable creating cards with suit & value, display and compare them."""

    def __init__(self, suit: CardSuit, val: CardValue):
        self.suit = suit
        self.value = val

    def __repr__(self):
        return f"{self.value.name} of {self.suit.name}"

    def __gt__(self, other):
        return self.suit.value > other.suit.value or (
                self.suit.value == other.suit.value and self.value.value > other.value.value
        )

    def __lt__(self, other):
        return self.suit.value < other.suit.value or (
                self.suit.value == other.suit.value and self.value.value < other.value.value
        )

    def __eq__(self, other):
        return not (self.__lt__(other) and self.__gt__(other))

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return not self.__gt__(other)


def main():
    """Create full deck, choose and print sorted five random cards."""
    deck = [Card(s, v) for s in CardSuit for v in CardValue]
    hand = sorted(choices(deck, k=5), key=lambda c: c.suit.value * 100 + c.value.value)
    print(hand)


if __name__ == '__main__':
    main()
