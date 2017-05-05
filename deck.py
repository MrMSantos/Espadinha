#Card Game Espadinha

import random
from card import card

class Deck:

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    SPADES = '♠'
    CLUBS = '♣'
    HEARTS = '♥'
    DIAMONDS = '♦'

    suits = [SPADES, CLUBS, HEARTS, DIAMONDS]
    deck = []

    def __init__(self):
        for suit in self.suits:
            for value in self.values:
                self.deck += [card(self.values[value], suit, value)]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck[0:13], self.deck[13:26], self.deck[26:39], self.deck[39:52]
