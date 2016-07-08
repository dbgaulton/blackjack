
import sys
from cards import *


def main():
	
	while 1:
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

		if (player_hand.get_blackjack_val() == 21):
			print("You got a blackjack!")

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
		else:
			dealer_hand.reveal_hole_cards()
			print("Dealer: " + str(dealer_hand))

			while dealer_hand.get_blackjack_val() < 17:
				dealer_hand.add(deck.deal())
				time.sleep(1)
				print("Dealer: " + str(dealer_hand))

			if not dealer_hand.is_under():
				print("Dealer busts. You win!")
			else:
				player_score = player_hand.get_blackjack_val()
				dealer_score = dealer_hand.get_blackjack_val()
				print("Player: " + str(player_score) + " Dealer: " + str(dealer_score))
				if player_score > dealer_score:
					print("You Win!")
				elif player_score == dealer_score:
					print("Push")
				else:
					print("you suck")

		while 1:
			play_again = input("Play again? ").lower()
			if play_again == "yes" or play_again == "y":
				break
			elif play_again == "no" or play_again == "n":
				sys.exit()
			else:
				print("Enter \"yes\" or \"no\"")


if __name__ == "__main__":
	main()