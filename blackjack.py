
import sys
from cards import *

def main():
	
	deck = Deck()

	deck.shuffle()

	player_hand = Hand()

	dealer_hand = Hand()

	print(deck.deal(player_hand), end=" ")
	print(deck.deal(player_hand))

	print(deck.deal(dealer_hand, True), end=" ")
	print(deck.deal(dealer_hand))



if __name__ == "__main__":
	main()