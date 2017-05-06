#Card Game Espadinha

import random
from card import Card

class Deck:

    deck = []

    def __init__(self):
        for suit in Card.suits:
            for value in Card.values:
                self.deck.append(Card(Card.values[value], suit, value))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck[0:13], self.deck[13:26], self.deck[26:39], self.deck[39:52]