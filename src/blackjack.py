#!/usr/bin/env python3

import cards

def main():
    game = cards.BlackjackGame(500)

    while game.start_round():
        pass

if __name__ == "__main__":
    main()
