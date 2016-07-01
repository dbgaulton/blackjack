
import sys
from cards import *

def main():
	
	deck = Deck()

	deck.shuffle()

	player_hand = Hand()

	dealer_hand = Hand()

	player_hand.add(deck.deal())
	player_hand.add(deck.deal())

	dealer_hand.add(deck.deal(), True)
	dealer_hand.add(deck.deal())

	print(player_hand)
	print(dealer_hand)


if __name__ == "__main__":
	main()