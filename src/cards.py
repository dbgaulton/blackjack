
import random
import time

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
			return "** "
		#elif self._value == "10"
		#	return self._value + self._suit
		else:
			return self._value + self._suit + " "


class Deck():
	def __init__(self):
		self._cards = []
		for suit in SUIT_UNICODE:
			for value in CARD_VALUES:
				self._cards.append(Card(value, suit))
		self.discarded_cards = []

	def shuffle(self):
		random.shuffle(self._cards)

	def deal(self):
		return self._cards.pop()

	def __repr__(self):
		return str(self._cards)


class Hand():
	def __init__(self):
		self._cards = []
		self.hole_cards = []

	def add(self, card, is_hole=False):
		card.is_hole = is_hole
		self._cards.append(card)
		if is_hole:
			self.hole_cards.append(card)

	def __repr__(self):
		output = ""
		for card in self._cards:
			output += str(card) + " "
		return output

	def get_blackjack_val(self):
		tot = 0;
		for card in self._cards:
			royals = ['J', 'Q', 'K']
			if card._value in royals:
				tot += 10
			elif card._value != 'A':
				tot += int(card._value)
			else:
				if tot + 11 > 21:
					tot += 1
				else:
					tot += 11
		return tot

	def is_under(self):
		return self.get_blackjack_val() <= 21

	def reveal_hole_cards(self):
		for card in self.hole_cards:
			card.is_hole = False