
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
        else:
            return self._value + self._suit + " "

class Deck():
    def __init__(self):
        self._cards = []
        for suit in SUIT_UNICODE:
            for value in CARD_VALUES:
                self._cards.append(Card(value, suit))
        self.shuffle()

        self.discarded_cards = []

    def shuffle(self):
        random.shuffle(self._cards)

    def deal_card(self):
        if not self._cards:
            self._cards = self.discarded_cards.copy()
            self.discarded_cards.clear()
            self.shuffle()
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
            else: # HANDLE ACE, CAN BE 1 OR 11
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

    def discard(self, card, deck):
        card.is_hole = False
        self._cards.remove(card)
        deck.discarded_cards.append(card)

    def fold(self, deck):
        self.reveal_hole_cards()
        deck.discarded_cards.extend(self._cards.copy())
        self._cards.clear()

class Player:
    def __init__(self, buy_in):
        self.chips = buy_in
        self.bet = 0
        self.hand = Hand()

    def place_bet(self):
        while True:    
            response = input("Place your bet: ")
            if response.isdigit():
                response = int(response)
                if response > self.chips:
                    print("You can't bet that much")
                else:    
                    self.bet = response
                    return self.bet
            else:
                print("Enter a number") 

class BlackjackGame:
    def __init__(self, buy_in):
        print("$" + str(buy_in) + " buy-in")
        self.dealer_hand = Hand()
        self.deck = Deck()
        self.buy_in = buy_in
        self.player = Player(self.buy_in)

    def start_round(self):
        if not self.player.chips:
            print("You have mortgaged you're house and now have $500")
            self.player.chips = 500

        self.player.place_bet()
        
        self._deal_cards()

        player_bust = self._prompt_player()

        if player_bust:
            print("Bust!")
            self.player.chips -= self.player.bet
            return self.end_game()

        dealer_bust = self._deal_with_dealer()

        if dealer_bust:
            print("Dealer busts. You win!")
            self.player.chips += self.player.bet
            return self.end_game()

        player_score = self.player.hand.get_blackjack_val()
        dealer_score = self.dealer_hand.get_blackjack_val()
        print("Player: " + str(player_score) + " Dealer: " + str(dealer_score))
        time.sleep(1)
        if player_score > dealer_score:
            print("You Win!")
            self.player.chips += self.player.bet
        elif player_score == dealer_score:
            print("Push")
        else:
            print("you lose")
            self.player.chips += self.player.bet

        return self.end_game()

    def _deal_cards(self):
        self.player.hand.add(self.deck.deal_card())
        self.dealer_hand.add(self.deck.deal_card())
        self.player.hand.add(self.deck.deal_card())
        self.dealer_hand.add(self.deck.deal_card(), True)

        print("Player: " + str(self.player.hand))
        print("Dealer: " + str(self.dealer_hand))


    def _prompt_player(self):
        while self.player.hand.is_under():
            response = input("Hit or Stand? ").lower()

            if response == "hit" or response == "h":
                self.player.hand.add(self.deck.deal_card())
            elif response == "stand" or response == "s":
                return False
            else:
                print("Enter 'h' or 's'")
                continue

            print("Player: " + str(self.player.hand))
            time.sleep(1)

        return True

    def _deal_with_dealer(self):
        self.dealer_hand.reveal_hole_cards()
        print("Dealer: " + str(self.dealer_hand))
        time.sleep(1)

        while self.dealer_hand.get_blackjack_val() < 17:
            self.dealer_hand.add(self.deck.deal_card())
            print("Dealer: " + str(self.dealer_hand))
            time.sleep(1)

        return not self.dealer_hand.is_under()

    def end_game(self):
        self._turn_in_cards()
        return self._ask_play_again()

    def _turn_in_cards(self):
        self.player.hand.fold(self.deck)
        self.dealer_hand.fold(self.deck)

    def _ask_play_again(self):
        print("You have $" + str(self.player.chips))
        while True:
            play_again = input("Play again? ").lower()
            if play_again == "yes" or play_again == "y":
                return True
            elif play_again == "no" or play_again == "n":
                return False
            else:
                print("Enter 'y' or 'n'")
