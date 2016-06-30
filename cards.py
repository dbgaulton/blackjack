
import random

SUIT_UNICODE = {
    "spades": chr(0x2664),
    "hearts": chr(0x2665),
    "diamonds": chr(0x2666),
    "clubs": chr(0x2667)
}

CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, value, suit):
        if suit in SUIT_UNICODE:
            self.suit = SUIT_UNICODE[suit]
        else:
            print("suit is out of range")
        if value in CARD_VALUES:
            self.value = value
        else:
            print("card value out of range")

    def __repr__(self):
        if self.value == "10":
            return self.value + self.suit
        else:
            return " " + self.value + self.suit


class Deck():
    def __init__(self):
        self._cards = []
        for suit in SUIT_UNICODE:
            for value in CARD_VALUES:
                self._cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, hand, is_hole=False):
        return hand.add(self._cards.pop(), is_hole)

    def __repr__(self):
        return str(self._cards)


class Hand():
    def __init__(self):
        self._cards = []

    def add(self, card, is_hole):
        self._cards.append(card)
        if not is_hole:
            return str(card)
        else:
            return " **"

    def __repr__(self):
        output = ""
        for card in self._cards:
            output += str(card) + " "
        return output