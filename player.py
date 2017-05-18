from card import Card
from deck import Deck
from table import Table

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

    def playCard(self, card):
        self.hand.remove(card)

    def playHighestCard(self, table):
        playableCards = self.playableCards(table)
        highValue = 0
        for card in self.hand:
            if card in playableCards:
                if highValue < card.value:
                    highValue = card.value
                    highCard = card
        return highCard

    def playLowestCard(self, table):
        playableCards = self.playableCards(table)
        lowValue = 15
        for card in self.hand:
            if card in playableCards:
                if lowValue > card.value:
                    lowValue = card.value
                    lowCard = card
        return lowCard

    def numSpades(self):
        num = 0
        for card in self.hand:
            if card.suit == card.SPADES:
                num += 1
        return num

    def numDiamonds(self):
        num = 0
        for card in self.hand:
            if card.suit == card.DIAMONDS:
                num += 1
        return num

    def numClubs(self):
        num = 0
        for card in self.hand:
            if card.suit == card.CLUBS:
                num += 1
        return num

    def numHearts(self):
        num = 0
        for card in self.hand:
            if card.suit == card.HEARTS:
                num += 1
        return num

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

    def playableCards(self, table):
        if len(table.plays) == 0:
            playableCards = self.eligablePlay(table.isTrumped)
        elif len(table.plays) > 0:
            playableCards = self.eligablePlay(table.isTrumped, table.plays[0][1].suit)
        return playableCards

    def printTricks(self):
        return self.name + ' ' + str(self.trick) + '/' + str(self.bet) + ' tricks'

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
