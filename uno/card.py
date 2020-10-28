from enum import Enum


class CardColor(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    SPECIAL = 5

    @staticmethod
    def normal_colors():
        return [CardColor.RED, CardColor.GREEN, CardColor.YELLOW, CardColor.BLUE]
    def __str__(self):
        return self.name

class CardValue(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    PLUS2 = 10
    PLUS4 = 11
    REVERSE = 12
    SKIP = 13
    COLOR_CHANGE = 14

    @staticmethod
    def normal_values():
        return [CardValue.ZERO, CardValue.ONE, CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE,
                CardValue.SIX, CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE]

    @staticmethod
    def action_values():
        return [CardValue.PLUS2, CardValue.REVERSE, CardValue.SKIP]

    @staticmethod
    def special_values():
        return [CardValue.PLUS4, CardValue.COLOR_CHANGE]
    def __str__(self):
        return self.name


class Card:
    def __init__(self, color: CardColor, value: CardValue):
        self.color = color
        self.value = value

    def __eq__(self, other):
        if type(other) != type(Card):
            return False
        return self.value == other.value and self.color == other.color

    def __str__(self):
        return "( " + str(self.color) + " : " + str(self.value) + " )"
