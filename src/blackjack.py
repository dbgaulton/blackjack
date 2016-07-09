
import sys
from cards import *


def main():

    chips = 500
    print("$" + str(chips) + " buy-in")

    while 1:

        if chips == 0:
            print("You have mortgaged you're house and now have $500")
            chips = 500

        deck = Deck()

        deck.shuffle()

        while 1:
            bet = input("Place your bet: ")
            if bet.isdigit():
                bet = int(bet)
                if bet > chips:
                    print("You can't bet that much")
                else:    
                    break
            else:
                print("Enter a number") 

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
                print("Enter 'h' or 's'")
                continue

            print("Player: " + str(player_hand))

        if not player_hand.is_under():
            print("Bust!")
            chips -= bet
        else:
            dealer_hand.reveal_hole_cards()
            print("Dealer: " + str(dealer_hand))
            time.sleep(1)

            while dealer_hand.get_blackjack_val() < 17:
                dealer_hand.add(deck.deal())
                print("Dealer: " + str(dealer_hand))
                time.sleep(1)

            if not dealer_hand.is_under():
                print("Dealer busts. You win!")
                chips += bet
            else:
                player_score = player_hand.get_blackjack_val()
                dealer_score = dealer_hand.get_blackjack_val()
                print("Player: " + str(player_score) + " Dealer: " + str(dealer_score))
                time.sleep(1)
                if player_score > dealer_score:
                    print("You Win!")
                    chips += bet
                elif player_score == dealer_score:
                    print("Push")
                else:
                    print("you suck")
                    chips -= bet

        time.sleep(1)

        while 1:
            print("You have $" + str(chips))
            play_again = input("Play again? ").lower()
            if play_again == "yes" or play_again == "y":
                break
            elif play_again == "no" or play_again == "n":
                sys.exit()
            else:
                print("Enter 'y' or 'n'")


if __name__ == "__main__":
    main()