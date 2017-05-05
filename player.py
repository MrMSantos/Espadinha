import deck
class player:

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