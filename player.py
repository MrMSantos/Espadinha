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

    def canPlay(self, isFirstTrick, isFirst, suit = None):
        print(deck.suits)

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