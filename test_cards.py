#!/usr/bin/env python3
    
import sys
from cards import *


def main():

    deck = Deck()

    deck.shuffle()

    print(deck)

    for i in range(0,5):
        print(deck.deal())

    print(deck)


if __name__ == "__main__":
    main()