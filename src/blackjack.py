
import sys
from cards import *


PLAY = True

def ask_play_again():
	while 1:
		play_again = input("Play again? ").lower()
		if play_again == "yes" or play_again == "y":
			PLAY = True
			#print()
			return 
		elif play_again == "no" or play_again == "n":
			PLAY = False
			return
		else:
			print("Enter \"yes\" or \"no\"") 


def main():
	
	while PLAY:

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
			ask_play_again()
			continue

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
			if player_hand.get_blackjack_val() > dealer_hand.get_blackjack_val():
				print("You Win!")
			else:
				print("you suck")

		ask_play_again()


if __name__ == "__main__":
	main()