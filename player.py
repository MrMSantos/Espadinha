from card import Card
from deck import Deck

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bet = 0
        self.trick = 0

    def reset(self):
        self.hand = []
        self.bet = 0
        self.trick = 0

    #def incTrick(self):
    #    self.trick += 1

    def playCard(self, card):
        self.hand.remove(card)

    def eligablePlay(self, isTrumped, suit = None):
        eligableCards = []
        if suit == None:
            if isTrumped:
                return self.hand
            else:
                for card in self.hand:
                    if card.suit != Card.SPADES:
                        eligableCards.append(card)
                if len(eligableCards) > 0:
                    return eligableCards
                else:
                    return self.hand
        else:
            for card in self.hand:
                if card.suit == suit:
                    eligableCards.append(card)
            if len(eligableCards) == 0:
                return self.hand
            return eligableCards

    def printHand(self):
        hand = ''
        i = 1
        for card in self.hand:
            hand += str(i) + ' - ' + card.toString() + ' | '
            i += 1
        return hand

    def orderHand(self):
        hand = []
        switch = True
        #order by suit
        for suit in Card.suits:
            for card in self.hand:
                if card.suit == suit:
                    hand.append(card)
        #order by value
        while switch:
            switch = False
            for i in range(len(hand) - 1):
                if hand[i].value < hand[i + 1].value and hand[i].suit == hand[i + 1].suit:
                    hand[i], hand[i + 1] = hand[i + 1], hand[i]
                    switch = True
        self.hand = hand
