#Card Game Espadinha

import random

S = '♠'
C = '♣'
H = '♥'
D = '♦'

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def create():
    return ['A'+S, '2'+S, '3'+S, '4'+S, '5'+S, '6'+S, '7'+S, '8'+S, '9'+S, 'T'+S, 'J'+S, 'Q'+S, 'K'+S, 'A'+C, '2'+C, '3'+C, '4'+C, '5'+C, '6'+C, '7'+C, '8'+C, '9'+C, 'T'+C,'J'+C, 'Q'+C, 'K'+C,\
            'A'+H, '2'+H, '3'+H, '4'+H, '5'+H, '6'+H, '7'+H, '8'+H, '9'+H, 'T'+H, 'J'+H, 'Q'+H, 'K'+H, 'A'+D, '2'+D, '3'+D, '4'+D, '5'+D, '6'+D, '7'+D, '8'+D, '9'+D, 'T'+D,'J'+D, 'Q'+D, 'K'+D]

def shuffle(deck):
    random.shuffle(deck)

def deal(deck):
    return deck[0:13], deck[13:26], deck[26:39], deck[39:52]

def remove_card(deck, card):
    deck.remove(card)

def get_card(deck, pos):
    return deck[pos]

d = create()
print(d)