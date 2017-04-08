#Card Game Espadinha

import random

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def create():
    return ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC','JC', 'QC', 'KC',\
            'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD','JD', 'QD', 'KD']

def shuffle(deck):
    random.shuffle(deck)

def deal(deck):
    return deck[0:13], deck[13:26], deck[26:39], deck[39:52]

def remove_card(deck, card):
    deck.remove(card)

def get_card(deck, pos):
    return deck[pos]