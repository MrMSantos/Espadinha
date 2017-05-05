#Card Game Espadinha

import random
from card import card

class deck:

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    S = '♠'
    C = '♣'
    H = '♥'
    D = '♦'
    suits = [S, C, H, D]
    deck = []
    
    def __init__(self):
        for suit in self.suits:
            for value in self.values:
                self.deck += [card(self.values[value], suit, value)]

    def shuffle(self, deck):
        random.shuffle(deck)

    def deal(self, deck):
        return deck[0:13], deck[13:26], deck[26:39], deck[39:52]