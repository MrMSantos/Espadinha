from card import Card
from deck import Deck

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bet = 0
        self.trick = 0

    def setHand(self, hand):
        self.hand = hand

    def setBet(self, bet):
        self.bet = int(bet)

    def getHand(self):
        return self.hand

    def getBet(self):
        return self.bet

    def getName(self):
        return self.name

    def reset(self):
        self.hand = []
        self.bet = 0
        self.trick = 0

    def incTrick(self):
        self.trick += 1

    def playCard(self, card):
        self.hand.remove(card)

    #def canPlay(self, isFirstTrick, isFirst, suit = None):
    #    print(deck.suits)

    def eligablePlay(self, isTrumped, suit = None):
        eligableCards = []
        if suit == None:
            if isTrumped:
                return self.hand
            else:
                for card in self.hand:
                    if card.suit != Card.SPADES:
                        eligableCards.append(card)
                return eligableCards
        else:
            for card in self.hand:
                if card.suit == suit:
                    eligableCards.append(card)
            if len(eligableCards) == 0:
                return self.hand
            return eligableCards

    def printHand(self):
        i = 1
        for card in self.hand:
            print(i, '-', card.toString(), end = ' | ')
            i += 1
        print()

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