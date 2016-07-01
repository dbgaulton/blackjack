
import sys
from cards import *


def play_game():
	pass


def main():

	play = True
	
	while play:

		deck = Deck()

		deck.shuffle()

		player_hand = Hand()

		dealer_hand = Hand()

		player_hand.add(deck.deal())
		player_hand.add(deck.deal())

		dealer_hand.add(deck.deal(), True)
		dealer_hand.add(deck.deal())

		print("Player: " + str(player_hand))
		print("Dealer: " + str(dealer_hand))


		while player_hand.is_under():
			response = input("Hit or Stand? ").lower()

			if response == "hit" or response == "h":
				player_hand.add(deck.deal())
			elif response == "stand" or response == "s":
				break
			else:
				print("Enter \"hit\" or \"stand\"")
				continue

			print("Player: " + str(player_hand))

		if not player_hand.is_under():
			print("Bust!")
			continue

		else:
			dealer_hand.reveal_hole_cards()
			print("Dealer: " + str(dealer_hand))

			while dealer_hand.get_blackjack_val() < 17:
				dealer_hand.add(deck.deal())
				time.sleep(1)
				print("Dealer: " + str(dealer_hand))

		if not dealer_hand.is_under():
			print("Dealer busts. You Win!")
		else:
			if player_hand.get_blackjack_val() > dealer_hand.get_blackjack_val():
				print("You Win!")
			else:
				print("you suck")

		play_again = input("Play again? ").lower()
		confirm = ["yes", "y"]
		if play_again in confirm:
			play = True
		else:
			play = False





if __name__ == "__main__":
	main()