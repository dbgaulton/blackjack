
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
		self._suit = SUIT_UNICODE[suit]
		self._value = value
		self.is_hole = False;

	def __repr__(self):
		if self.is_hole:
			return " **"
		elif self._value == "10":
			return self._value + self._suit
		else:
			return " " + self._value + self._suit


class Deck():
	def __init__(self):
		self._cards = []
		for suit in SUIT_UNICODE:
			for value in CARD_VALUES:
				self._cards.append(Card(value, suit))

	def shuffle(self):
		random.shuffle(self._cards)

	def deal(self):
		return self._cards.pop()

	def __repr__(self):
		return str(self._cards)


class Hand():
	def __init__(self):
		self._cards = []

	def add(self, card, is_hole=False):
		card.is_hole = is_hole
		self._cards.append(card)

	def __repr__(self):
		output = ""
		for card in self._cards:
			output += str(card) + " "
		return output

	def get_blackjack_val(self):
		tot = 0;
		for card in self.cards:
			royals = ['J', 'Q', 'K']
			if card.value in royals:
				tot += 10
			elif card.value != 'A':
				tot += int(card.value)
			else:
				pass
				# handle ace case
		return tot